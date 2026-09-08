from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from apps.articles.models import Article

class LatestStoriesFeed(Feed):
    feed_type = Rss201rev2Feed
    title = "KKEVO STUDIO MEDIA | Facts. Perspective. Impact."
    link = "/"
    description = "Independent African-centred global digital media institution. Verified facts, geopolitical analysis, and strategic perspectives."

    def items(self):
        return Article.objects.filter(
            status__in=[Article.Status.PUBLISHED, Article.Status.CORRECTED]
        ).order_by('-published_at')[:30]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary or item.subtitle

    def item_pubdate(self, item):
        return item.published_at

    def item_link(self, item):
        return f"/article/{item.slug}"

class AnalysisStoriesFeed(Feed):
    title = "KKEVO STUDIO MEDIA | In-Depth Analysis"
    link = "/analysis"
    description = "Rigorous analytical journalism on African geopolitics, sovereignty, resources, and industrialisation."

    def items(self):
        return Article.objects.filter(
            status__in=[Article.Status.PUBLISHED, Article.Status.CORRECTED],
            content_type=Article.ContentType.ANALYSIS
        ).order_by('-published_at')[:20]

    def item_title(self, item):
        return f"[ANALYSIS] {item.title}"

    def item_description(self, item):
        return item.summary or item.subtitle

    def item_pubdate(self, item):
        return item.published_at

    def item_link(self, item):
        return f"/article/{item.slug}"
