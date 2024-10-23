from django.test import TestCase
from .models import Article
from django.contrib.auth.models import User

class ArticleTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.article = Article.objects.create(
            title="Test Title",
            author="Test Author",
            body="This is the body of the test article.",
            owner=self.user
        )

    def test_article_creation(self):
        """Test that an article is correctly created."""
        self.assertEqual(self.article.title, "Test Title")
        self.assertEqual(self.article.author, "Test Author")
        self.assertEqual(self.article.body, "This is the body of the test article.")
        self.assertEqual(self.article.owner.username, "testuser")
        self.assertIsNotNone(self.article.created_at)

    def test_article_str(self):
        """Test that the __str__ method returns the title."""
        self.assertEqual(str(self.article), "Test Title")

    def test_article_ordering(self):
        """Test the ordering of articles by 'created_at'."""
        article2 = Article.objects.create(
            title="Second Article",
            author="Second Author",
            body="This is the second test article.",
            owner=self.user
        )
        articles = Article.objects.all()
        self.assertEqual(articles[0], self.article)
        self.assertEqual(articles[1], article2)
