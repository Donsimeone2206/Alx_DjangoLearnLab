from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for the test case
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(title="Test Book", publication_year=2020, author=self.author)
        self.client = APIClient()

    def test_create_book(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-create')
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, 'New Book')
        self.client.logout()

    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.book.title, response.data['title'])

    def test_update_book(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-update', args=[self.book.id])
        data = {'title': 'Updated Book', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')
        self.client.logout()

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
        self.client.logout()

    def test_list_books_filtering(self):
        url = reverse('book-list') + '?title=' + self.book.title
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming there's only one book with this title

    def test_list_books_search(self):
        url = reverse('book-list') + '?search=' + self.book.title
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(book['title'] == self.book.title for book in response.data))

    def test_list_books_ordering(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]['publication_year'] <= response.data[-1]['publication_year'])

