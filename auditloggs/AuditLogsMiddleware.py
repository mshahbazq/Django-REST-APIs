# middleware/logs.py
import logging
from django.utils import timezone
from .models import AuditLog  # Import your AuditLog model

class AuditLogsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        custom_request = request
        user = None
        if custom_request.user.is_authenticated:
            user = custom_request.user

        request_method = custom_request.method
        request_path = custom_request.path

        response = self.get_response(request)
        response_status_code = response.status_code

        client_ip = custom_request.META.get('REMOTE_ADDR')
        user_agent = custom_request.META.get('HTTP_USER_AGENT')

        audit_log_entry = AuditLog.objects.create(
            user=user,
            timestamp=timezone.now(),
            request_method=request_method,
            request_path=request_path,
            response_status_code=response_status_code,
            client_ip=client_ip,
            user_agent=user_agent,
        )
        audit_log_entry.save()
        
        logging.info(f"Audit Log Entry Created: {audit_log_entry}")

        return response

