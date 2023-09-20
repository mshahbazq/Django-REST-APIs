
from django.urls import re_path
from . import views

urlpatterns = [
    re_path('signup',views.signup),
    re_path('login',views.login),
    re_path('test_token',views.test_token),
    re_path('get_audit_loggs',views.get_audit_loggs),
]
