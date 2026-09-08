from django.urls import path
from .feeds import LatestStoriesFeed, AnalysisStoriesFeed
from .views import robots_txt_view, sitemap_xml_view

urlpatterns = [
    path('rss/', LatestStoriesFeed(), name='rss-latest'),
    path('rss/analysis/', AnalysisStoriesFeed(), name='rss-analysis'),
    path('robots.txt', robots_txt_view, name='robots-txt'),
    path('sitemap.xml', sitemap_xml_view, name='sitemap-xml'),
]
