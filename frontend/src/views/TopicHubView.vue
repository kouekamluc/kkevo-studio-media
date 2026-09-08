<template>
  <div class="min-h-screen py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <!-- Loading State -->
      <div v-if="loading" class="py-20 text-center">
        <div class="w-10 h-10 border-4 border-kkevo-blue border-t-transparent rounded-full animate-spin mx-auto"></div>
      </div>

      <template v-else-if="topic">
        <!-- Topic Header Dossier -->
        <div class="bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg p-6 sm:p-8 space-y-4">
          <div class="flex items-center gap-2 text-xs font-mono font-bold tracking-widest text-kkevo-blue-glow uppercase">
            <router-link to="/" class="hover:text-white">Home</router-link>
            <span>&rsaquo;</span>
            <span>Strategic Topic Hub</span>
          </div>

          <h1 class="text-3xl sm:text-4xl font-extrabold text-white font-headline">
            {{ topic.name }}
          </h1>

          <p v-if="topic.description" class="text-sm text-slate-300 max-w-3xl leading-relaxed">
            {{ topic.description }}
          </p>

          <div class="pt-3 border-t border-kkevo-navy-800 flex items-center justify-between text-xs text-slate-400 font-mono">
            <span>{{ articles.length }} Deep Reports & Strategic Analyses</span>
            <span class="text-kkevo-green font-semibold">Priority Observational Nexus</span>
          </div>
        </div>

        <!-- Tagged Stories -->
        <div class="space-y-6">
          <div v-if="!articles.length" class="py-16 text-center text-xs text-slate-400">
            No articles filed under this strategic topic yet.
          </div>

          <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <SecondaryLeadCard
              v-for="story in articles"
              :key="story.id"
              :story="story"
            />
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import { api } from '../services/api';
import SecondaryLeadCard from '../components/editorial/SecondaryLeadCard.vue';

const route = useRoute();
const topic = ref(null);
const articles = ref([]);
const loading = ref(true);

async function loadTopicHub() {
  loading.value = true;
  try {
    const slug = route.params.slug;
    const [tData, artData] = await Promise.all([
      api.getTopic(slug),
      api.getArticles({ topic: slug })
    ]);
    topic.value = tData;
    articles.value = artData.results || artData;
    document.title = `${tData.name} Hub | KKEVO STUDIO MEDIA`;
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
}

onMounted(loadTopicHub);
watch(() => route.params.slug, loadTopicHub);
</script>
