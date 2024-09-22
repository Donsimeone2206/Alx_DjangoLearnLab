from django.shortcuts import render
from .serializers import NotificationSerializer
from .models import Notification
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class NotificationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user = request.user

        # getting all the nofications for the user

        notifications = Notification.objects.filter(user=user).order_by('-timestamp')

        unread_notifications = notifications.filter(read=False)
        read_notifications = notifications.filter(read=True)

        def serialize_notification(notification):
            return {
                'id': notification.id,
                'actor': notification.actor.username,
                'verb': notification.verb,
                'target': str(notification.target),
                'read': notification.read,
                'timestamp': notification.timestamp,

            }
        
        return Response({
            "unread_notifications": [serialize_notification(m) for m in unread_notifications],
            "unread_notifications": [serialize_notification(m) for m in read_notifications],

        })

class NotificationReadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self , request , notification_id):
        user = request.user

        try:
            notification = Notification.objects.get(id=notification_id, user=user)
            notification.read = True
            notification.save()
            return Response({"info": "Notification marked as read."}, status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response({"info": "Notification not found."}, status=status.HTTP_404_NOT_FOUND)
    