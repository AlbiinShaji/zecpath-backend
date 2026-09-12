from django.contrib import admin
from .models import Candidate, Employer, Job, Application

admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Employer)
admin.site.register(Candidate)