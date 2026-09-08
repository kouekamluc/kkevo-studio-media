from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from apps.articles.models import Article
from apps.taxonomy.models import Category
from apps.accounts.models import User

class ArticleSystemTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name='Resources', slug='resources')
        self.editor = User.objects.create_user(
            username='test_editor',
            email='test_editor@kkevo.com',
            password='password123',
            role=User.Role.EDITOR
        )
        self.article = Article.objects.create(
            title='Test Critical Mineral Report',
            slug='test-critical-mineral-report',
            body='This is an in-depth report on African lithium reserves.',
            category=self.category,
            status=Article.Status.PUBLISHED
        )

    def test_article_auto_reading_time(self):
        """Reading time should be calculated based on word count."""
        self.assertGreaterEqual(self.article.reading_time_minutes, 1)

    def test_homepage_endpoint(self):
        """Homepage aggregated endpoint returns 200 and expected keys."""
        response = self.client.get('/api/v1/homepage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('hero', response.data)
        self.assertIn('latest_news', response.data)

    def test_article_detail_view_increment(self):
        """Viewing an article should atomically increment view count."""
        initial_views = self.article.views_count
        response = self.client.get(f'/api/v1/articles/{self.article.slug}/')
        self.assertEqual(response.status_code, 200)
        self.article.refresh_from_db()
        self.assertEqual(self.article.views_count, initial_views + 1)
