<template>
  <div class="min-h-screen py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <!-- Loading State -->
      <div v-if="loading" class="py-20 text-center">
        <div class="w-10 h-10 border-4 border-kkevo-green border-t-transparent rounded-full animate-spin mx-auto"></div>
      </div>

      <template v-else-if="country">
        <!-- Country Header Dossier Banner -->
        <div class="bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/90 dark:to-[#080D17] border border-slate-200 dark:border-white/[0.08] rounded-2xl p-6 sm:p-8 space-y-6 shadow-sm dark:shadow-xl transition-colors">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-white/[0.08] pb-6">
            <div class="flex items-center gap-4">
              <span class="text-5xl sm:text-6xl">{{ country.flag_emoji }}</span>
              <div>
                <span class="text-xs uppercase font-mono tracking-widest text-kkevo-green font-bold block">
                  Sovereign Country Intelligence Hub
                </span>
                <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white font-headline">
                  {{ country.name }}
                </h1>
                <span class="text-xs text-slate-500 dark:text-slate-400 font-mono">
                  {{ country.capital }} &bull; {{ country.region_name }} &bull; ISO: {{ country.iso_code }}
                </span>
              </div>
            </div>
          </div>

          <!-- Key Metrics Grid -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 text-xs">
            <div class="p-3.5 bg-slate-50 dark:bg-[#06090E] rounded-xl border border-slate-200 dark:border-white/[0.08]">
              <span class="text-slate-500 dark:text-slate-400 block font-mono text-[11px]">Nominal GDP</span>
              <span class="text-base font-bold text-slate-900 dark:text-white font-mono">{{ country.gdp_nominal_usd || 'N/A' }}</span>
            </div>
            <div class="p-3.5 bg-slate-50 dark:bg-[#06090E] rounded-xl border border-slate-200 dark:border-white/[0.08]">
              <span class="text-slate-500 dark:text-slate-400 block font-mono text-[11px]">Population</span>
              <span class="text-base font-bold text-slate-900 dark:text-white font-mono">{{ country.population || 'N/A' }}</span>
            </div>
            <div class="p-3.5 bg-slate-50 dark:bg-[#06090E] rounded-xl border border-slate-200 dark:border-white/[0.08] col-span-2">
              <span class="text-slate-500 dark:text-slate-400 block font-mono text-[11px]">Primary Strategic Resources</span>
              <div class="flex flex-wrap gap-1.5 mt-1">
                <span
                  v-for="res in country.strategic_resources"
                  :key="res"
                  class="px-2.5 py-0.5 rounded-md bg-white dark:bg-[#111A29] text-slate-800 dark:text-slate-200 text-[11px] font-semibold border border-slate-200 dark:border-white/[0.1] shadow-sm"
                >
                  {{ res }}
                </span>
              </div>
            </div>
          </div>

          <!-- National Sovereignty Directive -->
          <div v-if="country.sovereignty_notes" class="p-4 bg-blue-50 dark:bg-blue-950/30 border-l-4 border-kkevo-blue dark:border-kkevo-blue-glow rounded-r-lg text-xs text-slate-800 dark:text-slate-200 leading-relaxed">
            <span class="font-bold text-kkevo-blue dark:text-kkevo-blue-glow block mb-1 font-mono uppercase text-[11px]">
              National Sovereignty & Industrial Retaining Mandate:
            </span>
            {{ country.sovereignty_notes }}
          </div>
        </div>

        <!-- Tagged Stories from this Nation -->
        <div class="space-y-6">
          <div class="flex items-center justify-between border-b border-slate-200 dark:border-white/[0.08] pb-3">
            <h2 class="text-xl font-bold text-slate-900 dark:text-white font-headline">
              Reports & Investigations on {{ country.name }}
            </h2>
            <span class="text-xs text-slate-400 font-mono">{{ articles.length }} Stories Filed</span>
          </div>

          <div v-if="!articles.length" class="py-12 text-center text-xs text-slate-400">
            No reports filed under this sovereign hub yet.
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
const country = ref(null);
const articles = ref([]);
const loading = ref(true);

async function loadCountryHub() {
  loading.value = true;
  try {
    const slug = route.params.slug;
    const [cData, artData] = await Promise.all([
      api.getCountry(slug),
      api.getArticles({ country: slug })
    ]);
    country.value = cData;
    articles.value = artData.results || artData;
    document.title = `${cData.name} Sovereign Hub | KKEVO STUDIO MEDIA`;
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
}

onMounted(loadCountryHub);
watch(() => route.params.slug, loadCountryHub);
</script>
