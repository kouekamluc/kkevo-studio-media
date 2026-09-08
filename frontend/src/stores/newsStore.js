import { defineStore } from 'pinia';
import { api } from '../services/api';

export const useNewsStore = defineStore('news', {
  state: () => ({
    homepageData: null,
    breakingAlert: null,
    categories: [],
    countries: [],
    topics: [],
    loading: false,
    error: null,
    searchModalOpen: false,
    newsletterModalOpen: false,
  }),

  getters: {
    heroStory: (state) => state.homepageData?.hero || null,
    secondaryLeads: (state) => state.homepageData?.secondary_leads || [],
    latestNews: (state) => state.homepageData?.latest_news || [],
    analysisStories: (state) => state.homepageData?.analysis || [],
    explainers: (state) => state.homepageData?.explainers || [],
    resourceStories: (state) => state.homepageData?.resources || [],
    historyStories: (state) => state.homepageData?.history || [],
    mostRead: (state) => state.homepageData?.most_read || [],
  },

  actions: {
    async fetchHomepage(force = false) {
      if (this.homepageData && !force) return;
      this.loading = true;
      try {
        const data = await api.getHomepage();
        this.homepageData = data;
        if (data.breaking) {
          this.breakingAlert = data.breaking;
        }
      } catch (err) {
        this.error = err.message;
      } finally {
        this.loading = false;
      }
    },

    async fetchTaxonomy() {
      if (this.categories.length && this.countries.length) return;
      try {
        const [cats, countries, topics] = await Promise.all([
          api.getCategories(),
          api.getCountries(),
          api.getTopics({ featured: 'true' })
        ]);
        this.categories = cats;
        this.countries = countries;
        this.topics = topics;
      } catch (err) {
        console.error('Failed to fetch taxonomy:', err);
      }
    },

    toggleSearchModal(open) {
      this.searchModalOpen = open !== undefined ? open : !this.searchModalOpen;
    },

    toggleNewsletterModal(open) {
      this.newsletterModalOpen = open !== undefined ? open : !this.newsletterModalOpen;
    },

    dismissBreaking() {
      this.breakingAlert = null;
    }
  }
});
