<template>
  <div class="min-h-screen py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <div class="border-b border-purple-500/30 pb-6 space-y-2">
        <div class="flex items-center gap-2 text-xs font-mono font-bold tracking-widest text-purple-400 uppercase">
          <span class="w-2 h-2 rounded-full bg-purple-500"></span>
          KKEVO In-Depth Synthesis
        </div>
        <h1 class="text-3xl sm:text-4xl font-extrabold text-white font-headline">
          Geopolitical & Economic Analysis
        </h1>
        <p class="text-xs sm:text-sm text-slate-400 max-w-2xl leading-relaxed">
          Rigorous context, historical lineage, structural implications, and scenario forecasting for African policy, industry, and sovereign decision makers.
        </p>
      </div>

      <div v-if="loading" class="py-20 text-center">
        <div class="w-10 h-10 border-4 border-purple-500 border-t-transparent rounded-full animate-spin mx-auto"></div>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <article
          v-for="story in stories"
          :key="story.id"
          class="bg-kkevo-navy-900 border border-purple-500/30 rounded-lg p-6 flex flex-col justify-between hover:border-purple-400 transition group shadow-xl"
        >
          <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
              <span class="px-2 py-0.5 rounded bg-purple-950 text-purple-300 font-semibold border border-purple-500/40 text-[11px]">
                ANALYSIS
              </span>
              <span v-if="story.country_flag" class="text-xs text-slate-300">{{ story.country_flag }} {{ story.country_name }}</span>
            </div>

            <router-link :to="`/article/${story.slug}`" class="block">
              <h3 class="text-lg font-bold text-white leading-snug group-hover:text-purple-300 transition font-headline">
                {{ story.title }}
              </h3>
            </router-link>

            <p v-if="story.subtitle" class="text-xs text-slate-400 leading-relaxed line-clamp-3">
              {{ story.subtitle }}
            </p>
          </div>

          <div class="pt-4 mt-4 border-t border-kkevo-navy-800 flex items-center justify-between text-xs text-slate-400 font-mono">
            <span>{{ story.authors?.[0]?.display_name || 'KKEVO Analyst' }}</span>
            <span>{{ story.reading_time_minutes }}m read</span>
          </div>
        </article>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { api } from '../services/api';

const stories = ref([]);
const loading = ref(true);

onMounted(async () => {
  loading.value = true;
  try {
    const res = await api.getArticles({ type: 'ANALYSIS' });
    stories.value = res.results || res;
    document.title = 'KKEVO Analysis | Facts. Perspective. Impact.';
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
});
</script>
