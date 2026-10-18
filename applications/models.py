from django.db import models
from django.utils import timezone

class JobApplication(models.Model):

    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    application_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20,
                              choices=[("Applied", "Applied"),
        ("Interview", "Interview"),
        ("Selected", "Selected"),
        ("Rejected", "Rejected"), ],
        default="Applied")
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.company_name