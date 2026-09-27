from django.shortcuts import render

from .models import (
    Certification,
    Education,
    Experience,
    Profile,
    Project,
    SkillCategory,
)


def home(request):
    context = {
        "profile": Profile.objects.first(),
        "educations": Education.objects.all(),
        "experiences": Experience.objects.all(),
        "skill_categories": SkillCategory.objects.prefetch_related("skills").all(),
        "projects": Project.objects.all(),
        "certifications": Certification.objects.all(),
    }
    return render(request, "core/home.html", context)