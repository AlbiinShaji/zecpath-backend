from django.db import models
from django.contrib.auth.models import User


class Employer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    company_name = models.CharField(max_length=200)
    company_domain = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name


class Candidate(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    skills = models.TextField()
    education = models.TextField()
    experience = models.TextField()

    def __str__(self):
        return self.user.username


class Job(models.Model):
    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE,
        related_name="jobs"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Application(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    status = models.CharField(
        max_length=50,
        default="Applied"
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate} - {self.job}"