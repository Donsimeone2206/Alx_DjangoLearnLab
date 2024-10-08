from django.urls import path
from .views import register_view, login_view, logout_view, profile_view, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, post_detail_view, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
   path('register/', register_view, name='register'),
   path('login/', login_view, name='login'),
   path('logout/', logout_view, name='logout'),
   path('profile/', profile_view, name='profile'),
   path('posts/', PostListView.as_view(), name='post-list'),
   path('post/new/', PostCreateView.as_view(), name='post-create'),
   path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
   path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
   path('posts/<int:pk>/', post_detail_view, name='post-detail'),
   path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
   path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
   path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
   path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
   path('search/', views.search_posts, name='search_posts'),
]

