import { defineStore } from 'pinia';
import { api } from '../services/api';
import { useAlertStore } from './alertStore';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    bookmarks: [],
    loading: false,
    authModalOpen: false,
  }),

  getters: {
    isAuthenticated: (state) => !!state.user,
    isStaff: (state) => state.user?.is_staff || false,
    role: (state) => state.user?.role || 'VISITOR',
    displayName: (state) => state.user?.first_name ? `${state.user.first_name} ${state.user.last_name || ''}`.trim() : (state.user?.username || 'Reader'),
  },

  actions: {
    async checkAuth() {
      try {
        const res = await api.getCurrentUser();
        this.user = res.id ? res : null;
        if (this.user) {
          this.fetchBookmarks();
        }
      } catch {
        this.user = null;
      }
    },

    async login(email, password) {
      this.loading = true;
      try {
        const res = await api.login(email, password);
        this.user = res.user;
        this.authModalOpen = false;
        this.fetchBookmarks();
        const alertStore = useAlertStore();
        alertStore.success('Newsroom Sign-In', `Welcome back, ${this.displayName}.`);
        return true;
      } finally {
        this.loading = false;
      }
    },

    async logout() {
      try {
        await api.logout();
      } finally {
        this.user = null;
        this.bookmarks = [];
        const alertStore = useAlertStore();
        alertStore.info('Session Ended', 'You have safely signed out.');
      }
    },

    async fetchBookmarks() {
      if (!this.user) return;
      try {
        const res = await api.getBookmarks();
        this.bookmarks = res.results || res;
      } catch (err) {
        console.error('Failed to load bookmarks', err);
      }
    },

    async toggleBookmark(articleId) {
      const alertStore = useAlertStore();
      if (!this.user) {
        alertStore.info('Reader Sign-In Required', 'Create a free account or sign in to save stories to your dossier.');
        this.authModalOpen = true;
        return;
      }
      const wasBookmarked = this.isBookmarked(articleId);
      try {
        await api.addBookmark(articleId);
        await this.fetchBookmarks();
        if (wasBookmarked) {
          alertStore.info('Dossier Updated', 'Story removed from your saved reading list.');
        } else {
          alertStore.success('Story Saved to Dossier', 'Article preserved in your verified reading library.');
        }
      } catch (err) {
        console.error('Bookmark error', err);
        alertStore.error('Bookmark Notice', 'Could not update your reading dossier.');
      }
    },

    isBookmarked(articleId) {
      return this.bookmarks.some(b => b.article === articleId || b.article_data?.id === articleId);
    },

    toggleAuthModal(open) {
      this.authModalOpen = open !== undefined ? open : !this.authModalOpen;
    }
  }
});
