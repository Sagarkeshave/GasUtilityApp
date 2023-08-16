from django.db import models
from django.contrib.auth.models import User


class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved")
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    submitted_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.customer

class SupportRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mob_no = models.IntegerField(blank=False, default=77777777)
    email = models.EmailField(blank=False, default="support@gmail.com")

    def __str__(self):
        return self.user,
