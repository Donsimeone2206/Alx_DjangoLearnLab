from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List view for all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only access to everyone

# Detail view for a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only access to everyone

# Create view for adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

    def perform_create(self, serializer):
        # Custom logic or validation before saving
        serializer.save()

# Update view for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

    def perform_update(self, serializer):
        # Custom logic or validation before saving
        serializer.save()

# Delete view for removing a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

    def perform_destroy(self, instance):
        # Custom logic before deleting
        instance.delete()

