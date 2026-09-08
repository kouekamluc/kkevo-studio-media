from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

def health_check(request):
    return JsonResponse({
        'status': 'healthy',
        'platform': 'KKEVO STUDIO MEDIA',
        'tagline': 'Facts. Perspective. Impact.',
        'version': '1.0.0'
    })

urlpatterns = [
    # Health check
    path('api/v1/health/', health_check, name='health-check'),

    # Django Administration
    path('admin/', admin.site.urls),

    # OpenAPI 3 Schema & Interactive Swagger UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Core API v1 Endpoints
    path('api/v1/auth/', include('apps.accounts.urls')),
    path('api/v1/', include('apps.taxonomy.urls')),
    path('api/v1/', include('apps.authors.urls')),
    path('api/v1/', include('apps.media_library.urls')),
    path('api/v1/', include('apps.sources.urls')),
    path('api/v1/', include('apps.articles.urls')),
    path('api/v1/', include('apps.video.urls')),
    path('api/v1/', include('apps.live.urls')),
    path('api/v1/newsletter/', include('apps.newsletter.urls')),
    path('api/v1/community/', include('apps.community.urls')),
    path('api/v1/analytics/', include('apps.analytics.urls')),

    # SEO, Feeds, Sitemaps
    path('feeds/', include('apps.seo.urls')),
]

# Static & Media serving during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
