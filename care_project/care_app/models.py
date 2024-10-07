from django.db import models
class Study(models.Model):
    STUDY_PHASES = [
        ('Phase I', 'Phase I'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
        ('Phase IV', 'Phase IV'),]
    study_name = models.CharField(max_length=255)
    study_description = models.TextField()
    study_phase = models.CharField(choices=STUDY_PHASES, max_length=20)
    sponsor_name = models.CharField(max_length=255)
