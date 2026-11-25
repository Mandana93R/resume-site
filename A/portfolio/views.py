from django.shortcuts import render
from .models import Profile, SocialLink, Project, Experience, Skill, Education, Language, Conference, Testimonial


def home(request):
    profile = Profile.objects.first()
    social_links = SocialLink.objects.filter(is_active=True)
    latest_projects = Project.objects.filter(project_type='latest', is_active=True)
    other_projects = Project.objects.filter(project_type='other', is_active=True)
    experiences = Experience.objects.all()
    skills = Skill.objects.filter(is_active=True)
    educations = Education.objects.all()
    languages = Language.objects.all()
    conferences = Conference.objects.filter(is_active=True)
    testimonials = Testimonial.objects.filter(is_active=True)

    return render(
        request,
        'portfolio/index.html',
        {
            'profile': profile,
            'social_links': social_links,
            'latest_projects': latest_projects,
            'other_projects': other_projects,
            'experiences': experiences,
            'skills': skills,
            'educations': educations,
            'languages': languages,
            'conferences': conferences,
            'testimonials': testimonials,
        }
    )