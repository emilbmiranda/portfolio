from django.db import models

# Create your models here.
class Me(models.Model):
    first_name = models.CharField(max_length=4)
    last_name = models.CharField(max_length=13)
    phone_number = models.CharField(max_length=13)
    email_address = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    summary = models.CharField(max_length=300)

class JobResponsibility(models.Model):
    responsibility = models.CharField(max_length=300)

class Job(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    responsibilties = models.ManyToManyField(JobResponsibility)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

class SchoolDescription(models.Model):
    description = models.CharField(max_length=100)

class School(models.Model):
    school = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    degree_type = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    descriptions = models.ManyToManyField(SchoolDescription)

class Skill(models.Model):
    PROGRAMMING_LANGUAGE = 'Programming Language'
    PROFICIENT = 'Proficient'
    KNOWLEDGE = 'Knowledge of'
    DATABASE = 'Database'
    IDE = 'Integrated Development Environment/Text Editor'
    REPORT = 'Report/Analytics'
    ETL = 'ETL'
    NON_TECHNICAL = 'Non-technical'
    
    SKILL_TYPE_CHOICES = (
        (PROGRAMMING_LANGUAGE, 'Programming Language'),
        (DATABASE, 'Database'),
        (IDE, 'Integrated Development Environment/Text Editor'),
        (REPORT, 'Report/Analytics'),
        (ETL, 'ETL'),
        (NON_TECHNICAL, 'Non-technical'),
    )
    SKILL_SUBTYPE_CHOICES = (
        (PROFICIENT, 'Proficient'),
        (KNOWLEDGE, 'Knowledge of'),
    )
    
    skill = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=100, choices=SKILL_TYPE_CHOICES)
    skill_subtype = models.CharField(max_length=20, choices=SKILL_SUBTYPE_CHOICES, blank=True, null=True)

class Project(models.Model):
    PROFESSIONAL = 'Professional'
    PERSONAL = 'Personal'

    PROJECT_TYPES = (
        (PROFESSIONAL, 'Professional'),
        (PERSONAL, 'Personal'),
    )

    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    picture = models.ImageField()

class Award(models.Model):
    description = models.CharField(max_length=100)
    