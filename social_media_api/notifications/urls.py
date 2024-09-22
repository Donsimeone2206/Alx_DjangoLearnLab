from django.urls import path
from .views import NotificationView , NotificationReadView
from rest_framework.routers import DefaultRouter
from .models import Notification

urlpatterns = [
    path('notifications/', NotificationView.as_view(), name='notification'),
    path('notifications/<int:notification_id>/reaad/', NotificationReadView.as_view(), name='read_notifications')
]