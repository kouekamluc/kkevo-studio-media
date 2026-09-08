from django.http import HttpResponse
from apps.articles.models import Article

def robots_txt_view(request):
    content = """User-agent: *
Allow: /
Disallow: /admin/
Disallow: /editorial/
Disallow: /api/editorial/

Sitemap: https://kkevostudiomedia.com/sitemap.xml
Sitemap: https://kkevostudiomedia.com/news-sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")

def sitemap_xml_view(request):
    articles = Article.objects.filter(
        status__in=[Article.Status.PUBLISHED, Article.Status.CORRECTED]
    ).order_by('-published_at')[:500]

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    # Core pages
    for path in ['', '/news', '/geopolitics', '/economy', '/resources', '/technology', '/history', '/video', '/analysis']:
        xml.append(f'  <url><loc>https://kkevostudiomedia.com{path}</loc><changefreq>hourly</changefreq><priority>1.0</priority></url>')

    for a in articles:
        date_str = a.published_at.strftime('%Y-%m-%d') if a.published_at else ''
        xml.append(f'  <url><loc>https://kkevostudiomedia.com/article/{a.slug}</loc><lastmod>{date_str}</lastmod><priority>0.8</priority></url>')

    xml.append('</urlset>')
    return HttpResponse("\n".join(xml), content_type="application/xml")
