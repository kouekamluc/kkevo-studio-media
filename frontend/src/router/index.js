import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ArticleDetailView from '../views/ArticleDetailView.vue';
import CategoryView from '../views/CategoryView.vue';
import CountryHubView from '../views/CountryHubView.vue';
import AnalysisHubView from '../views/AnalysisHubView.vue';
import VideoHubView from '../views/VideoHubView.vue';
import CorrectionsArchiveView from '../views/CorrectionsArchiveView.vue';
import SearchResultsView from '../views/SearchResultsView.vue';
import EditorialDashboardView from '../views/EditorialDashboardView.vue';
import LegalView from '../views/LegalView.vue';

import TopicHubView from '../views/TopicHubView.vue';
import LiveBlogView from '../views/LiveBlogView.vue';
import ReaderProfileView from '../views/ReaderProfileView.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/article/:slug',
    name: 'article-detail',
    component: ArticleDetailView,
  },
  {
    path: '/category/:slug',
    name: 'category',
    component: CategoryView,
  },
  {
    path: '/country/:slug',
    name: 'country-hub',
    component: CountryHubView,
  },
  {
    path: '/topic/:slug',
    name: 'topic-hub',
    component: TopicHubView,
  },
  {
    path: '/analysis',
    name: 'analysis',
    component: AnalysisHubView,
  },
  {
    path: '/video',
    name: 'video',
    component: VideoHubView,
  },
  {
    path: '/live/:slug?',
    name: 'live-blog',
    component: LiveBlogView,
  },
  {
    path: '/corrections',
    name: 'corrections',
    component: CorrectionsArchiveView,
  },
  {
    path: '/profile',
    name: 'reader-profile',
    component: ReaderProfileView,
  },
  {
    path: '/search',
    name: 'search',
    component: SearchResultsView,
  },
  {
    path: '/editorial',
    name: 'editorial-dashboard',
    component: EditorialDashboardView,
  },
  {
    path: '/legal/:page?',
    name: 'legal',
    component: LegalView,
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/',
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { top: 0 };
    }
  },
});

export default router;
