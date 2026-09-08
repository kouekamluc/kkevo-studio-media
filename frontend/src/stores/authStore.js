import { defineStore } from 'pinia';
import { api } from '../services/api';

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
      if (!this.user) {
        this.authModalOpen = true;
        return;
      }
      try {
        await api.addBookmark(articleId);
        this.fetchBookmarks();
      } catch (err) {
        console.error('Bookmark error', err);
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
