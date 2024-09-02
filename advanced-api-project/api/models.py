from django.db import models

class Author(models.Model):
    """
    Author model to store information about book authors.
    Fields:
        name (CharField): A string field to store the author's name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model to store details about books.
    Fields:
        title (CharField): A string field for the book's title.
        publication_year (IntegerField): An integer field for the year the book was published.
        author (ForeignKey): A foreign key linking to the Author model, establishing a one-to-many relationship from Author to Books.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

