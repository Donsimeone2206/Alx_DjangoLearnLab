from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .forms import ExampleForm
# Create your views here.
from .models import Book
book1 = Book.objects.create(title = "Inheritance", author = "Kasoo", publication_year = 2010)
@permission_required('bookshelf.can_create', raise_exception=True) # permission required to edit the model instance
def edit_view(request): # function to edit the view
    return HttpResponse ("Edit view accessed")
def book_list(request):
    books = Book.objects.all()
    context = {'lists_all_books':books}
    return render(request ,'bookshelf/book_list.html', context )

def example(request):
 return render(request ,'form_example.html')
