from django.urls import path
from . import views

urlpatterns = [
    path('create-project/', views.create_project, name='create_project'),
    path('projects/', views.all_projects, name='all_projects'),
    path(
    'project/<int:id>/',
    views.project_detail,
    name='project_detail'
)   ,
    path(
    'apply/<int:project_id>/',
    views.apply_to_join,
    name='apply_to_join'
    ),
    path(
    'my-projects/',
    views.my_projects,
    name='my_projects'
),
path(
    'requests/<int:project_id>/',
    views.project_requests,
    name='project_requests'
),
path(
    'accept/<int:request_id>/',
    views.accept_request,
    name='accept_request'
),

path(
    'reject/<int:request_id>/',
    views.reject_request,
    name='reject_request'
),
path(
    'my-applications/',
    views.my_applications,
    name='my_applications'
),
path(
    'save-project/<int:project_id>/',
    views.save_project,
    name='save_project'
),

path(
    'saved-projects/',
    views.saved_projects,
    name='saved_projects'
),
path(
    'notifications/',
    views.notifications,
    name='notifications'
),

path(
    'edit-project/<int:project_id>/',
    views.edit_project,
    name='edit_project'
),

path(
    'delete-project/<int:project_id>/',
    views.delete_project,
    name='delete_project'
),
path(
    'chat/<int:project_id>/',
    views.project_chat,
    name='project_chat'
),
path(
    'delete-message/<int:message_id>/',
    views.delete_message,
    name='delete_message'
),

path(
    'edit-message/<int:message_id>/',
    views.edit_message,
    name='edit_message'
),
path(
    'react/<int:message_id>/<str:emoji>/',
    views.react_message,
    name='react_message'
),
path(
    'reply/<int:message_id>/',
    views.reply_message,
    name='reply_message'
),


]