from django.shortcuts import render
from .models import Me, Job, School, Skill, Project, Award

# Create your views here.
def home(request):
    mes = Me.objects
    jobs = Job.objects
    schools = School.objects
    skills = Skill.objects
    projects = Project.objects
    awards = Award.objects
    return render(request, "me/home.html",
        {'mes':mes, 'jobs':jobs, 'schools':schools, 'skills':skills, 'projects':projects, 'awards':awards})
