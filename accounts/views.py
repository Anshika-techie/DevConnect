from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from projects.models import Project, JoinRequest
from .forms import ForgotPasswordForm
from django.contrib.auth.models import User
from projects.models import Notification
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.models import JoinRequest
from projects.models import SavedProject
import pdfplumber
from projects.models import Project
from django.contrib import messages

@login_required
def home(request):

    projects_count = Project.objects.filter(
        created_by=request.user
    ).count()

    requests_count = JoinRequest.objects.filter(
        project__created_by=request.user
    ).count()

    applications_count = JoinRequest.objects.filter(
        user=request.user
    ).count()
   
    team_members_count= JoinRequest.objects.filter(
        project__created_by=request.user,
        status='Accepted'
    ).count()

    recent_projects = Project.objects.filter(
        created_by=request.user
    ).order_by('-id')[:5]
    for project in recent_projects:

        project.current_members = JoinRequest.objects.filter(
            project=project,
            status='Accepted'
        ).count()
    user_skills = []

    if request.user.profile.skills:

        user_skills = [
            skill.strip().lower()
            for skill in request.user.profile.skills.split(',')
        ]

    recommended_projects = []

    all_projects = Project.objects.exclude(
        created_by=request.user
    )

    for project in all_projects:

        project_skills = [
            skill.strip().lower()
            for skill in project.tech_stack.split(',')
        ]

        matched = len(
            set(user_skills) &
            set(project_skills)
        )

        total = len(project_skills)

        if total > 0:

            match_score = round(
                (matched / total) * 100
            )

            if match_score > 0:

                project.match_score = match_score

                recommended_projects.append(
                    project
                )

    recommended_projects = sorted(
        recommended_projects,
        key=lambda x: x.match_score,
        reverse=True
    )[:5]

    notifications_count = Notification.objects.filter(
        user=request.user,
        is_read=False
    ).count()

    activities = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')[:5]
    saved_projects_count = SavedProject.objects.filter(
        user=request.user
    ).count()

    context = {

        'projects_count': projects_count,

        'requests_count': requests_count,

        'applications_count': applications_count,

        'team_members_count': team_members_count,

        'saved_projects_count': saved_projects_count,   

        'recent_projects': recent_projects,

        'notifications_count': notifications_count,

        'activities': activities,

        'recommended_projects': recommended_projects,

    }

    return render(
        request,
        'home.html',
        context
    )


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Automatically login after registration
            login(request, user)

            return redirect('/')

    else:
        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )
from django.contrib import messages

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            profile = user.profile

            if (
                not profile.college
                or not profile.bio
                or not profile.github_link
            ):
                return redirect('/complete-profile/')

            next_url = request.GET.get('next')

            if next_url and next_url.startswith('/'):
                return redirect(next_url)

            return redirect('/')

        else:
            messages.error(
                request,
                'Invalid username or password'
            )

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def profile(request):

    profile = request.user.profile

    return render(
        request,
        'profile.html',
        {'profile': profile}
    )
@login_required
def edit_profile(request):

    profile = request.user.profile

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if request.POST.get('remove_profile_image'):

            profile.profile_image.delete(save=False)
            profile.profile_image = None

        if form.is_valid():

            form.save()

            profile.refresh_from_db()

            if profile.resume:

                try:

                    resume_text = ""

                    with pdfplumber.open(
                        profile.resume.path
                    ) as pdf:

                        for page in pdf.pages:

                            resume_text += (
                                page.extract_text() or ""
                            )

                    skills_list = [
                        'Python',
                        'Java',
                        'C++',
                        'Django',
                        'React',
                        'Node.js',
                        'MongoDB',
                        'MySQL',
                        'JavaScript',
                        'HTML',
                        'CSS',
                        'Git',
                        'AWS'
                    ]

                    found_skills = []

                    for skill in skills_list:

                        if skill.lower() in resume_text.lower():

                            found_skills.append(skill)

                    if found_skills:

                        profile.skills = ", ".join(
                            found_skills
                        )

                    if len(found_skills) <= 3:

                        profile.experience_level = "Beginner"

                    elif len(found_skills) <= 7:

                        profile.experience_level = "Intermediate"

                    else:

                        profile.experience_level = "Advanced"

                    profile.save()

                except Exception as e:

                    print("Resume Error:", e)

            return redirect('/profile/')

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        'edit_profile.html',
        {
            'form': form,
            'profile': profile
        }
    )



def forgot_password(request):

    if request.method == 'POST':

        form = ForgotPasswordForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            new_password = form.cleaned_data['new_password']

            try:

                user = User.objects.get(
                    username=username
                )

                user.set_password(
                    new_password
                )

                user.save()

                return redirect('/login/')

            except User.DoesNotExist:

                pass

    else:

        form = ForgotPasswordForm()

    return render(
        request,
        'forgot_password.html',
        {
            'form': form
        }

    )
def complete_profile(request):

    profile = request.user.profile

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect('/')

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        'complete_profile.html',
        {'form': form}
    )


def skip_profile(request):
    return redirect('/')

@login_required
def upload_profile_image(request):

    if request.method == "POST":

        profile = request.user.profile

        if request.FILES.get("profile_image"):
            profile.profile_image = request.FILES["profile_image"]
            profile.save()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})


@login_required
def upload_cover_image(request):

    if request.method == "POST":

        profile = request.user.profile

        if request.FILES.get("cover_image"):
            profile.cover_image = request.FILES["cover_image"]
            profile.save()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})

@login_required
def remove_profile_image(request):

    profile = request.user.profile

    if profile.profile_image:

        profile.profile_image.delete(
            save=False
        )

        profile.profile_image = None
        profile.save()

    return redirect('/profile/')
@login_required
def remove_cover_image(request):

    profile = request.user.profile

    if profile.cover_image:

        profile.cover_image.delete(
            save=False
        )

        profile.cover_image = None
        profile.save()

    return redirect('/profile/')