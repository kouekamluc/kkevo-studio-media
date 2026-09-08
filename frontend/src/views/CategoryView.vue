<template>
  <div class="min-h-screen py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <!-- Category Header -->
      <div class="border-b border-slate-200 dark:border-white/[0.08] pb-6 space-y-2">
        <div class="flex items-center gap-2 text-xs font-mono font-bold tracking-widest text-kkevo-green uppercase">
          <router-link to="/" class="hover:text-slate-900 dark:hover:text-white transition-colors">Home</router-link>
          <span>&rsaquo;</span>
          <span>Section Desk</span>
        </div>
        <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white font-headline capitalize">
          {{ categoryName }}
        </h1>
        <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 max-w-2xl leading-relaxed">
          Comprehensive, evidence-led reporting and strategic intelligence on {{ categoryName }}.
        </p>
      </div>

      <!-- Loading / Empty / Grid -->
      <div v-if="loading" class="py-20 text-center">
        <div class="w-10 h-10 border-4 border-kkevo-blue border-t-transparent rounded-full animate-spin mx-auto"></div>
      </div>

      <div v-else-if="!articles.length" class="py-16 text-center text-slate-500 dark:text-slate-400 text-xs font-mono">
        No articles published under this section yet.
      </div>

      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <SecondaryLeadCard
          v-for="story in articles"
          :key="story.id"
          :story="story"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import { api } from '../services/api';
import SecondaryLeadCard from '../components/editorial/SecondaryLeadCard.vue';

const route = useRoute();
const articles = ref([]);
const loading = ref(true);

const categorySlug = computed(() => route.params.slug);
const categoryName = computed(() => {
  const s = categorySlug.value || '';
  return s.replace(/-/g, ' ');
});

async function loadCategoryArticles() {
  loading.value = true;
  try {
    const res = await api.getArticles({ category: categorySlug.value });
    articles.value = res.results || res;
    document.title = `${categoryName.value.toUpperCase()} | KKEVO STUDIO MEDIA`;
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
}

onMounted(loadCategoryArticles);
watch(() => route.params.slug, loadCategoryArticles);
</script>
