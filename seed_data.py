import random

from django.contrib.auth.models import User
from projects.models import Project


domains = [
    "AI", "Smart", "Campus", "Cloud", "Dev", "Code",
    "Health", "Finance", "Travel", "Food", "Career",
    "Research", "Learning", "Crypto", "Social",
    "Fitness", "Job", "Student", "Event", "Startup"
]

products = [
    "Assistant", "Tracker", "Manager", "Portal",
    "Platform", "Hub", "System", "Dashboard",
    "Analyzer", "Network", "Marketplace",
    "Planner", "Builder", "Engine", "Studio"
]

roles = [
    "Frontend Developer",
    "Backend Developer",
    "Full Stack Developer",
    "ML Engineer",
    "UI/UX Designer",
    "DevOps Engineer"
]

experiences = [
    "Beginner",
    "Intermediate",
    "Advanced"
]

techs = [
    "Django, React",
    "Node.js, MongoDB",
    "Flutter, Firebase",
    "Python, ML",
    "Java, Spring Boot",
    "React, Express",
    "Next.js, PostgreSQL"
]

users = list(User.objects.all())

created_titles = set()

while len(created_titles) < 250:

    title = f"{random.choice(domains)} {random.choice(products)}"

    if title in created_titles:
        continue

    created_titles.add(title)

for title in created_titles:

    Project.objects.create(

        title=title,

        description=f"{title} project for developer collaboration and innovation.",

        tech_stack=random.choice(techs),

        team_size=random.randint(2, 8),

        role_needed=random.choice(roles),

        experience_level=random.choice(experiences),

        project_status="Open",

        created_by=random.choice(users)

    )

print("250 Projects Created 🚀")