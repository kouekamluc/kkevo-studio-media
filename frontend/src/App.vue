<template>
  <div class="min-h-screen flex flex-col bg-[#F8FAFC] dark:bg-[#06090E] text-slate-900 dark:text-[#E2E8F0] selection:bg-kkevo-blue selection:text-white font-sans transition-colors duration-200">
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

    <!-- Global Interactive Alert Notification Toast System -->
    <GlobalAlertToast />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useNewsStore } from './stores/newsStore';
import { useAuthStore } from './stores/authStore';
import { useThemeStore } from './stores/themeStore';
import AppHeader from './components/common/AppHeader.vue';
import AppFooter from './components/common/AppFooter.vue';
import SearchModal from './components/common/SearchModal.vue';
import NewsletterModal from './components/common/NewsletterModal.vue';
import AuthModal from './components/common/AuthModal.vue';
import GlobalAlertToast from './components/common/GlobalAlertToast.vue';

const newsStore = useNewsStore();
const authStore = useAuthStore();
const themeStore = useThemeStore();

onMounted(() => {
  themeStore.initTheme();
  authStore.checkAuth();
});
</script>
