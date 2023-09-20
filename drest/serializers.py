from rest_framework import serializers
from django.contrib.auth.models import User

from auditloggs.models import AuditLog

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('id', 'username', 'email', 'password')


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = AuditLog
        fields = '__all__'