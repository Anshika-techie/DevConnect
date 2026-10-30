from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project
from django.shortcuts import get_object_or_404
from .models import JoinRequest
from django.core.paginator import Paginator
from .models import SavedProject
from .models import Notification
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from accounts.models import Profile
from .models import Message
from .models import MessageReaction



def create_project(request):

    if request.method == 'POST':

        form = ProjectForm(request.POST)

        if form.is_valid():

            project = form.save(commit=False)

            project.created_by = request.user

            project.save()

            return redirect('/')

    else:
        form = ProjectForm()

    return render(
        request,
        'create_project.html',
        {'form': form}
    )
def all_projects(request):

    projects = Project.objects.all().order_by('-id')
    profiles = Profile.objects.none()

    role = request.GET.get('role')
    experience = request.GET.get('experience')
    search = request.GET.get('search')

    if role:
        projects = projects.filter(
            role_needed__icontains=role
        )

    if experience:
        projects = projects.filter(
            experience_level=experience
        )

    if search:

        projects = projects.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(tech_stack__icontains=search) |
            Q(role_needed__icontains=search)
        )

        profiles = Profile.objects.filter(
            Q(user__username__icontains=search) |
            Q(skills__icontains=search) |
            Q(college__icontains=search)
        )

    paginator = Paginator(
        projects,
        12
    )

    page_number = request.GET.get('page')

    projects = paginator.get_page(
        page_number
    )

    return render(
        request,
        'all_projects.html',
        {
            'projects': projects,
            'profiles': profiles
        }
    )

    projects = Project.objects.all().order_by('-id')

    role = request.GET.get('role')
    experience = request.GET.get('experience')
    search = request.GET.get('search')

    if role:
        projects = projects.filter(
            role_needed__icontains=role
        )

    if experience:
        projects = projects.filter(
            experience_level=experience
        )

    if search:
        projects = projects.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(tech_stack__icontains=search)|
            Q(role_needed__icontains=search)

            
        )
        profiles = Profile.objects.filter(
        Q(user__username__icontains=search) |
        Q(skills__icontains=search) |
        Q(college__icontains=search)
    )

    paginator = Paginator(
        projects,
        12
    )

    page_number = request.GET.get('page')

    projects = paginator.get_page(
        page_number
    )

    return render(
        request,
        'all_projects.html',
        {
            'projects': projects,
        }
    )
def project_detail(request, id):

    project = get_object_or_404(
        Project,
        id=id
    )

    team_count = JoinRequest.objects.filter(
        project=project,
        status='Accepted'
    ).count()

    return render(
        request,
        'project_details.html',
        {
            'project': project,
            'team_count': team_count
        }
    )


def apply_to_join(request, project_id):

    project = Project.objects.get(id=project_id)

    # Owner apne hi project mein apply nahi kar sakta
    if project.created_by == request.user:
        return redirect('/projects/')

    join_request, created = JoinRequest.objects.get_or_create(
    project=project,
    user=request.user
    )

    if created:
        Notification.objects.create(
            user=project.created_by,
            message=f"New application received for {project.title}"
        )


    return redirect('/projects/')
def my_projects(request):

    projects = Project.objects.filter(
        created_by=request.user
    )

    return render(
        request,
        'my_projects.html',
        {'projects': projects}
    )
def project_requests(request, project_id):

    project = Project.objects.get(id=project_id)

    # Sirf project owner requests dekh sakta hai
    if project.created_by != request.user:
        return redirect('/projects/')

    requests = JoinRequest.objects.filter(
        project=project
    )
    for request_obj in requests:

        user_skills = []

        if request_obj.user.profile.skills:
            user_skills = [
                skill.strip().lower()
                for skill in request_obj.user.profile.skills.split(',')
            ]

        project_skills = [
            skill.strip().lower()
            for skill in project.tech_stack.split(',')
        ]

        matched = len(
            set(user_skills)
            &
            set(project_skills)
        )

        total = len(project_skills)

        if total > 0:
            request_obj.compatibility_score = round(
                (matched / total) * 100
            )
        else:
            request_obj.compatibility_score = 0

    return render(
        request,
        'project_requests.html',
        {
            'project': project,
            'requests': requests
        }
    )
def accept_request(request, request_id):

    join_request = JoinRequest.objects.get(
        id=request_id
    )

    if join_request.project.created_by != request.user:
        return redirect('/projects/')

    current_members = JoinRequest.objects.filter(
        project=join_request.project,
        status="Accepted"
    ).count() + 1

    if current_members >= join_request.project.team_size:

        return redirect(
            f'/requests/{join_request.project.id}/'
        )

    join_request.status = "Accepted"
    join_request.save()

    project = join_request.project

    accepted_members = JoinRequest.objects.filter(
        project=project,
        status="Accepted"
    ).count()

    if accepted_members + 1 >= project.team_size:

        project.project_status = "Closed"
        project.save()

    Notification.objects.create(
        user=join_request.user,
        message=f"Your request for {join_request.project.title} was accepted"
    )

    return redirect(
        f'/requests/{join_request.project.id}/'
    )


def reject_request(request, request_id):

    join_request = JoinRequest.objects.get(
        id=request_id
    )

    if join_request.project.created_by != request.user:
        return redirect('/projects/')

    join_request.status = "Rejected"
    join_request.save()
    Notification.objects.create(
    user=join_request.user,
    message=f"Your request for {join_request.project.title} was rejected"
)

    return redirect(
        f'/requests/{join_request.project.id}/'
    )
def my_applications(request):

    applications = JoinRequest.objects.filter(
        user=request.user
    )

    return render(
        request,
        'my_applications.html',
        {
            'applications': applications
        }
    )
def save_project(request, project_id):

    project = Project.objects.get(
        id=project_id
    )

    SavedProject.objects.get_or_create(
        user=request.user,
        project=project
    )

    return redirect(
        f'/project/{project_id}/'
    )
def saved_projects(request):

    saved_projects = SavedProject.objects.filter(
        user=request.user
    )

    return render(
        request,
        'saved_projects.html',
        {
            'saved_projects': saved_projects
        }
    )
@login_required
def notifications(request):

    notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')

    notifications.update(
        is_read=True
    )

    return render(
        request,
        'notifications.html',
        {
            'notifications': notifications
        }
    )




@login_required
def edit_project(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id
    )

    if project.created_by != request.user:
        return redirect('/projects/')

    if request.method == 'POST':

        form = ProjectForm(
            request.POST,
            instance=project
        )

        if form.is_valid():
            form.save()
            return redirect(
                f'/project/{project.id}/'
            )

    else:

        form = ProjectForm(
            instance=project
        )

    return render(
        request,
        'edit_project.html',
        {
            'form': form,
            'project': project
        }
    )


@login_required
def delete_project(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id
    )

    if project.created_by == request.user:
        project.delete()

    return redirect('/my-projects/')
@login_required
def project_chat(request, project_id):

    project = get_object_or_404(
        Project,
        id=project_id
    )

    messages = Message.objects.filter(
        project=project
    ).order_by('created_at')
    members = JoinRequest.objects.filter(
    project=project,
    status='Accepted'
)

    if request.method == 'POST':

        text = request.POST.get('message')

        image = request.FILES.get(
            'image'
        )

        file = request.FILES.get(
            'file'
        )

        voice_note = request.FILES.get(
            'voice_note'
        )
        print("IMAGE =", image)
        print("FILE =", file)
        print("VOICE =", voice_note)

        if (
            text
            or image
            or file
            or voice_note
        ):

            Message.objects.create(

                project=project,

                user=request.user,

                message=text,

                image=image,

                file=file,

                voice_note=voice_note

            )

        return redirect(
            f'/chat/{project.id}/'
        )

    return render(
        request,
        'project_chat.html',
        {
            'project': project,
            'messages': messages,
            'members': members

        }
    )
@login_required
def delete_message(request, message_id):

    message = get_object_or_404(
        Message,
        id=message_id
    )

    if message.user == request.user:

        project_id = message.project.id

        message.delete()

        return redirect(
            f'/chat/{project_id}/'
        )

    return redirect('/')

@login_required
def edit_message(request, message_id):

    message = get_object_or_404(
        Message,
        id=message_id
    )

    if message.user != request.user:

        return redirect('/')

    if request.method == "POST":

        message.message = request.POST.get(
            'message'
        )

        message.save()

        return redirect(
            f'/chat/{message.project.id}/'
        )

    return render(
        request,
        'edit_message.html',
        {
            'message_obj': message
        }
    )
@login_required
def react_message(
    request,
    message_id,
    emoji
):

    message = get_object_or_404(
        Message,
        id=message_id
    )

    MessageReaction.objects.get_or_create(
        message=message,
        user=request.user,
        emoji=emoji
    )

    return redirect(
        f'/chat/{message.project.id}/'
    )
@login_required
def reply_message(request, message_id):

    original_message = get_object_or_404(
        Message,
        id=message_id
    )

    if request.method == "POST":

        text = request.POST.get('message')

        Message.objects.create(
            project=original_message.project,
            user=request.user,
            message=text,
            reply_to=original_message
        )

        return redirect(
            f'/chat/{original_message.project.id}/'
        )

    return render(
        request,
        'reply_message.html',
        {
            'original': original_message
        }
    )