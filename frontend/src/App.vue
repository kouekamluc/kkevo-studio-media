<template>
  <div class="min-h-screen flex flex-col bg-kkevo-navy-950 text-kkevo-silver selection:bg-kkevo-blue selection:text-white font-sans">
    <!-- Top Header -->
    <AppHeader />

    <!-- Main Content Area -->
    <main class="flex-grow">
      <router-view />
    </main>

    <!-- Global Footer -->
    <AppFooter />

    <!-- Modals -->
    <SearchModal
      :is-open="newsStore.searchModalOpen"
      @close="newsStore.toggleSearchModal(false)"
    />

    <NewsletterModal
      :is-open="newsStore.newsletterModalOpen"
      @close="newsStore.toggleNewsletterModal(false)"
    />

    <AuthModal
      :is-open="authStore.authModalOpen"
      @close="authStore.toggleAuthModal(false)"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useNewsStore } from './stores/newsStore';
import { useAuthStore } from './stores/authStore';
import AppHeader from './components/common/AppHeader.vue';
import AppFooter from './components/common/AppFooter.vue';
import SearchModal from './components/common/SearchModal.vue';
import NewsletterModal from './components/common/NewsletterModal.vue';
import AuthModal from './components/common/AuthModal.vue';

const newsStore = useNewsStore();
const authStore = useAuthStore();

onMounted(() => {
  authStore.checkAuth();
});
</script>
