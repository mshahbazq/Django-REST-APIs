# models.py
from django.db import models
from django.contrib.auth.models import User

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    request_method = models.CharField(max_length=10)
    request_path = models.CharField(max_length=255)
    response_status_code = models.IntegerField()
    
    # Additional fields for more detailed auditing
    client_ip = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    
    # Add more fields as needed for your audit log

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'Audit Log Entry - {self.timestamp}'
