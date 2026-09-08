<template>
  <section class="mt-16 bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg p-6 sm:p-8">
    <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between pb-6 border-b border-kkevo-navy-800 gap-4">
      <div>
        <div class="flex items-center gap-2 text-xs font-mono font-bold tracking-widest text-kkevo-green uppercase">
          <span class="w-2 h-2 rounded-full bg-kkevo-green"></span>
          KKEVO Continental Hub Explorer
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-white font-headline mt-1">
          The Map Explains It: African Strategic Sovereignty
        </h2>
      </div>
      <p class="text-xs text-slate-400 max-w-md">
        Select a sovereign nation to explore domestic mineral retention laws, energy corridors, strategic reserve policies, and investigative field reporting.
      </p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 mt-6">
      <!-- Country Selection Buttons -->
      <div class="lg:col-span-5 space-y-2">
        <span class="text-xs uppercase font-mono text-slate-400 block mb-2">Select Sovereign Hub:</span>
        <div class="grid grid-cols-2 gap-2">
          <button
            v-for="c in countries"
            :key="c.slug"
            @click="selectedSlug = c.slug"
            :class="[
              'p-3 rounded text-left border transition flex items-center justify-between',
              selectedSlug === c.slug
                ? 'bg-kkevo-navy-950 border-kkevo-green text-white shadow-lg'
                : 'bg-kkevo-navy-950/60 border-kkevo-navy-800 text-slate-300 hover:border-kkevo-navy-700 hover:text-white'
            ]"
          >
            <div class="flex items-center gap-2 min-w-0">
              <span class="text-xl">{{ c.flag_emoji }}</span>
              <span class="text-xs font-bold truncate">{{ c.name }}</span>
            </div>
            <span class="text-[10px] font-mono text-slate-400">{{ c.iso_code }}</span>
          </button>
        </div>
      </div>

      <!-- Country Dossier Card -->
      <div v-if="activeCountry" class="lg:col-span-7 bg-kkevo-navy-950 border border-kkevo-navy-800 rounded-lg p-6 flex flex-col justify-between space-y-6">
        <div class="space-y-4">
          <div class="flex items-start justify-between">
            <div class="flex items-center gap-3">
              <span class="text-4xl">{{ activeCountry.flag_emoji }}</span>
              <div>
                <h3 class="text-xl font-extrabold text-white font-headline">{{ activeCountry.name }}</h3>
                <span class="text-xs font-mono text-kkevo-green">Capital: {{ activeCountry.capital }} &bull; {{ activeCountry.region_name }}</span>
              </div>
            </div>

            <router-link
              :to="`/country/${activeCountry.slug}`"
              class="px-3 py-1.5 rounded bg-kkevo-blue text-white text-xs font-bold uppercase tracking-wider hover:bg-kkevo-blue-dark transition shrink-0"
            >
              Open Hub &rarr;
            </router-link>
          </div>

          <!-- Indicators Grid -->
          <div class="grid grid-cols-2 gap-3 py-3 border-y border-kkevo-navy-800 text-xs">
            <div class="bg-kkevo-navy-900/80 p-3 rounded border border-kkevo-navy-800">
              <span class="text-slate-400 block font-mono text-[11px]">Nominal GDP</span>
              <span class="text-sm font-bold text-white font-mono">{{ activeCountry.gdp_nominal_usd || 'N/A' }}</span>
            </div>
            <div class="bg-kkevo-navy-900/80 p-3 rounded border border-kkevo-navy-800">
              <span class="text-slate-400 block font-mono text-[11px]">Population</span>
              <span class="text-sm font-bold text-white font-mono">{{ activeCountry.population || 'N/A' }}</span>
            </div>
          </div>

          <!-- Strategic Resources -->
          <div v-if="activeCountry.strategic_resources?.length">
            <span class="text-xs uppercase font-mono text-slate-400 block mb-2">Strategic Mineral & Energy Assets:</span>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="res in activeCountry.strategic_resources"
                :key="res"
                class="px-2.5 py-1 rounded bg-kkevo-navy-900 text-slate-200 text-xs font-semibold border border-kkevo-navy-700"
              >
                {{ res }}
              </span>
            </div>
          </div>

          <!-- Sovereignty Note -->
          <div v-if="activeCountry.sovereignty_notes" class="bg-blue-950/30 border-l-2 border-kkevo-blue p-3 rounded-r text-xs text-slate-300 leading-relaxed">
            <span class="font-bold text-kkevo-blue-glow block mb-1 font-mono uppercase text-[11px]">National Sovereignty Priority:</span>
            {{ activeCountry.sovereignty_notes }}
          </div>
        </div>

        <div class="text-xs text-slate-400 font-mono pt-2 border-t border-kkevo-navy-800">
          Source: KKEVO Geopolitical & Resource Intelligence Observatory
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
