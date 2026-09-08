<template>
  <section class="mt-16 bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/80 dark:to-[#070B13] border border-slate-200 dark:border-white/[0.08] rounded-2xl p-6 sm:p-8 shadow-sm dark:shadow-[0_10px_35px_-5px_rgba(0,0,0,0.8)] transition-colors">
    <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between pb-6 border-b border-slate-200 dark:border-white/[0.08] gap-4">
      <div>
        <div class="flex items-center gap-2 text-xs font-mono font-bold tracking-widest text-kkevo-green uppercase">
          <span class="w-2 h-2 rounded-full bg-kkevo-green"></span>
          KKEVO Continental Hub Explorer
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white font-headline mt-1">
          The Map Explains It: African Strategic Sovereignty
        </h2>
      </div>
      <p class="text-xs text-slate-600 dark:text-slate-300 max-w-md">
        Select a sovereign nation to explore domestic mineral retention laws, energy corridors, strategic reserve policies, and investigative field reporting.
      </p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 mt-6">
      <!-- Country Selection Buttons -->
      <div class="lg:col-span-5 space-y-2">
        <span class="text-xs uppercase font-mono text-slate-500 dark:text-slate-400 block mb-2 font-bold">Select Sovereign Hub:</span>
        <div class="grid grid-cols-2 gap-2.5">
          <button
            v-for="c in countries"
            :key="c.slug"
            @click="selectedSlug = c.slug"
            :class="[
              'p-3.5 rounded-lg text-left border transition-all flex items-center justify-between',
              selectedSlug === c.slug
                ? 'bg-slate-100 dark:bg-kkevo-green/10 border-kkevo-green text-slate-900 dark:text-white shadow-md font-bold'
                : 'bg-slate-50 dark:bg-[#060A12] border-slate-200 dark:border-white/[0.06] text-slate-700 dark:text-slate-300 hover:border-slate-400 dark:hover:border-white/[0.18] hover:text-slate-900 dark:hover:text-white'
            ]"
          >
            <div class="flex items-center gap-2.5 min-w-0">
              <span class="text-2xl">{{ c.flag_emoji }}</span>
              <span class="text-xs truncate">{{ c.name }}</span>
            </div>
            <span class="text-[10px] font-mono text-slate-400">{{ c.iso_code }}</span>
          </button>
        </div>
      </div>

      <!-- Country Dossier Card -->
      <div v-if="activeCountry" class="lg:col-span-7 bg-slate-50 dark:bg-[#060910] border border-slate-200 dark:border-white/[0.08] rounded-xl p-6 sm:p-7 flex flex-col justify-between space-y-6 shadow-sm">
        <div class="space-y-5">
          <div class="flex items-start justify-between gap-4">
            <div class="flex items-center gap-4">
              <span class="text-5xl sm:text-6xl">{{ activeCountry.flag_emoji }}</span>
              <div>
                <h3 class="text-xl sm:text-2xl font-extrabold text-slate-900 dark:text-white font-headline">{{ activeCountry.name }}</h3>
                <span class="text-xs font-mono text-kkevo-green font-bold">Capital: {{ activeCountry.capital }} &bull; {{ activeCountry.region_name }}</span>
              </div>
            </div>

            <router-link
              :to="`/country/${activeCountry.slug}`"
              class="px-3.5 py-1.5 rounded-lg bg-kkevo-blue text-white text-xs font-bold uppercase tracking-wider hover:bg-kkevo-blue-dark transition shadow-sm shrink-0"
            >
              Open Hub &rarr;
            </router-link>
          </div>

          <!-- Indicators Grid -->
          <div class="grid grid-cols-2 gap-3 py-3 border-y border-slate-200 dark:border-white/[0.08] text-xs">
            <div class="bg-white dark:bg-[#0C1322] p-3.5 rounded-lg border border-slate-200 dark:border-white/[0.07]">
              <span class="text-slate-500 dark:text-slate-400 block font-mono text-[11px]">Nominal GDP</span>
              <span class="text-base font-bold text-slate-900 dark:text-white font-mono">{{ activeCountry.gdp_nominal_usd || 'N/A' }}</span>
            </div>
            <div class="bg-white dark:bg-[#0C1322] p-3.5 rounded-lg border border-slate-200 dark:border-white/[0.07]">
              <span class="text-slate-500 dark:text-slate-400 block font-mono text-[11px]">Population</span>
              <span class="text-base font-bold text-slate-900 dark:text-white font-mono">{{ activeCountry.population || 'N/A' }}</span>
            </div>
          </div>

          <!-- Strategic Resources -->
          <div v-if="activeCountry.strategic_resources?.length">
            <span class="text-xs uppercase font-mono text-slate-500 dark:text-slate-400 block mb-2 font-bold">Strategic Mineral & Energy Assets:</span>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="res in activeCountry.strategic_resources"
                :key="res"
                class="px-2.5 py-1 rounded-md bg-white dark:bg-[#111C30] text-slate-800 dark:text-slate-200 text-xs font-semibold border border-slate-200 dark:border-white/[0.1] shadow-sm"
              >
                {{ res }}
              </span>
            </div>
          </div>

          <!-- Sovereignty Note -->
          <div v-if="activeCountry.sovereignty_notes" class="bg-blue-50 dark:bg-blue-950/20 border-l-4 border-kkevo-blue dark:border-kkevo-blue-glow p-4 rounded-r-lg text-xs text-slate-800 dark:text-slate-200 leading-relaxed">
            <span class="font-bold text-kkevo-blue dark:text-kkevo-blue-glow block mb-1 font-mono uppercase text-[11px]">National Sovereignty Priority:</span>
            {{ activeCountry.sovereignty_notes }}
          </div>
        </div>

        <div class="text-xs text-slate-500 dark:text-slate-400 font-mono pt-3 border-t border-slate-200 dark:border-white/[0.08] flex items-center justify-between">
          <span>Source: KKEVO Geopolitical & Resource Observatory</span>
          <span class="text-kkevo-green font-bold">Verified Data Point</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  countries: {
    type: Array,
    default: () => [],
  }
});

const selectedSlug = ref('drc');

const activeCountry = computed(() => {
  if (!props.countries?.length) return null;
  return props.countries.find(c => c.slug === selectedSlug.value) || props.countries[0];
});
</script>
