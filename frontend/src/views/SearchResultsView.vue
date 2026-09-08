<template>
  <div class="min-h-screen py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <div class="border-b border-slate-200 dark:border-white/[0.08] pb-6 space-y-4">
        <h1 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white font-headline flex items-center gap-3">
          <svg class="w-7 h-7 text-kkevo-blue dark:text-kkevo-blue-glow" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          Search Results: <span class="text-kkevo-blue dark:text-kkevo-blue-glow">&ldquo;{{ query }}&rdquo;</span>
        </h1>
        <span class="text-xs text-slate-500 dark:text-slate-400 font-mono font-bold">{{ results.length }} stories matched across verified archives</span>
      </div>

      <div v-if="loading" class="py-20 text-center">
        <div class="w-10 h-10 border-4 border-kkevo-blue border-t-transparent rounded-full animate-spin mx-auto"></div>
      </div>

      <div v-else-if="!results.length" class="py-16 text-center space-y-3">
        <p class="text-sm text-slate-700 dark:text-slate-300 font-medium">No articles found matching &ldquo;{{ query }}&rdquo;.</p>
        <p class="text-xs text-slate-500 dark:text-slate-400 font-mono">Try searching for broader keywords such as DRC, Lithium, Gold, AfCFTA, or Sahel.</p>
      </div>

      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <SecondaryLeadCard
          v-for="story in results"
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
const results = ref([]);
const loading = ref(true);

const query = computed(() => route.query.q || '');

async function performSearch() {
  if (!query.value) {
    results.value = [];
    loading.value = false;
    return;
  }
  loading.value = true;
  try {
    const res = await api.getArticles({ q: query.value });
    results.value = res.results || res;
    document.title = `Search: "${query.value}" | KKEVO STUDIO MEDIA`;
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
}

onMounted(performSearch);
watch(() => route.query.q, performSearch);
</script>
