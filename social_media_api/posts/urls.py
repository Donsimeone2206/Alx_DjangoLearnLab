from .views import CommentViewSet , PostViewset , FeedView
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LikePostView , UnLikePostView

router = DefaultRouter()
router.register(r'Post',PostViewset)
router.register(r'Comment',CommentViewSet)

urlpatterns = [
    path('feed/',FeedView.as_view(), name='user_feed'),
    path('' , include(router.urls)),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='liked_posts'),
    path('posts/<int:pk>/unlike/', UnLikePostView.as_view(), name='unlike_view')
]
