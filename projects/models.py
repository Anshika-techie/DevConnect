from django.db import models
from django.contrib.auth.models import User
import math

class Project(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField()

    tech_stack = models.CharField(max_length=300)

    team_size = models.IntegerField()

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
#     role_needed = models.CharField(max_length=100,default='Developer'
# )
    role_needed = models.CharField(
    max_length=100,
    default='Frontend Developer'
    )
    EXPERIENCE_LEVELS = (
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
)

    experience_level = models.CharField(
        max_length=50,choices=EXPERIENCE_LEVELS,
        default='Beginner'
    )

    PROJECT_STATUS = (
    ('Open', 'Open'),
    ('Closed', 'Closed'),
    )

    project_status = models.CharField(
        max_length=20,
        choices=PROJECT_STATUS,
        default='Open'
    )

    def __str__(self):
        return self.title
    
class JoinRequest(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    def __str__(self):
        return f"{self.user.username} -> {self.project.title}"
class SavedProject(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (
            'user',
            'project'
        )

    def __str__(self):
        return f"{self.user.username} saved {self.project.title}"
class Notification(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    message = models.CharField(
        max_length=255
    )

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
#     linkedin_link = models.URLField(
#     blank=True,
#     null=True
# )

    def __str__(self):
        return self.message
    
class Message(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    message = models.TextField(
        blank=True
    )

    reply_to = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='replies'


)
    image = models.ImageField(
        upload_to='chat_images/',
        blank=True,
        null=True
    )

    file = models.FileField(
        upload_to='chat_files/',
        blank=True,
        null=True
    )

    voice_note = models.FileField(
        upload_to='voice_notes/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    edited = models.BooleanField(
        default=False
    )


    def __str__(self):
        return f"{self.user.username}: {self.message[:20]}"
    
class MessageReaction(models.Model):

    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    emoji = models.CharField(
        max_length=10
    )

    class Meta:

        unique_together = (
            'message',
            'user',
            'emoji'
        )