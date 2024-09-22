
from rest_framework import generics
from .models import Post ,Comment  ,Like
from .serializers import PostSerializer,CommentSerializer ,LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permissions import IsAuthorOrReadOnly
from rest_framework.views import APIView 
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from notifications.models import Notification
from django.shortcuts import get_object_or_404


from rest_framework import viewsets
# Create your views here.
# the modelviewset allows implementation such as list create or retrieve
class PostViewset(viewsets.ModelViewSet): #handles all basic crud operations for the post model
        queryset = Post.objects.all()
        serializer_class = PostSerializer
        permission_classes = [IsAuthorOrReadOnly]
        filter_backends = [DjangoFilterBackend,filters.SearchFilter ]
        filterset_fields = [ 'title'] # allows filtering based on title and content
        search_fields = ['title'] # allows searching by title and content


        
        def perform_create(self, serializer):
           serializer.save(author=self.request.user)






class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes =  [IsAuthorOrReadOnly]
  
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FeedView(generics.ListAPIView): # lists all the posts of the people the user is following
     serializer_class = PostSerializer
     permission_classes = [permissions.IsAuthenticated]
     
     def get_queryset(self):
        user = self.request.user
        following_users = user.following.all() # users that the current user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
     

class LikePostView(generics.GenericAPIView):
     permission_classes = [permissions.IsAuthenticated]


     def post(self, request, pk):
        # Use generics.get_object_or_404 to fetch the post or raise a 404
        post = generics.get_object_or_404(Post, pk=pk)  
        
        # Check if the user has already liked the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            # If the user has already liked the post, we remove the like (unlike)
            like.delete()
            message = 'Post unliked'
        else:
            # If the like was newly created, we send a notification and return a success message
            Notification.objects.create(
                actor=request.user,
                recipient=post.author,  # Assuming the post has an author field
                verb='liked',
                target=post
            )
            message = 'Post liked'

        return Response({'message': message}, status=status.HTTP_200_OK)




class UnLikePostView(APIView):
     permission_classes = [permissions.IsAuthenticated]
     def delete(self, request, post_id): #this gets the post and the user
          try:
               post = Post.objects.get(id=post_id)
          except Post.DoesNotExist:
               return Response({"info":"Post not found."}, status=status.HTTP_404_NOT_FOUND)
          
          user = request.user

          try:
               like = Like.objects.get(post=post , user=user)
               like.delete()
               return Response({"detail":" You have unliked the post."}) 
          
          except:
               return Response({"info":"You have not liked this post."})
          

