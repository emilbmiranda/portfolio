from django.contrib import admin
from .models import Me, JobResponsibility, Job, School, SchoolDescription, Skill, Project, Award

# Register your models here.
admin.site.register(Me)
admin.site.register(JobResponsibility)
admin.site.register(Job)
admin.site.register(SchoolDescription)
admin.site.register(School)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Award)
