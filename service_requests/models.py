from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')]
    TYPE_CHOICES = [('gas_leakage', 'Gas Leakage'), ('billing', 'Billing Issue'), ('new_connection', 'New Connection')]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.request_type}"

