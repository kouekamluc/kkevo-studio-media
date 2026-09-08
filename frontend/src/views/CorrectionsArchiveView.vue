<template>
  <div class="min-h-screen py-8">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <div class="border-b border-red-500/30 pb-6 space-y-2">
        <div class="flex items-center gap-2 text-xs font-mono font-bold tracking-widest text-red-400 uppercase">
          <span class="w-2 h-2 rounded-full bg-red-500"></span>
          KKEVO Institutional Transparency Ledger
        </div>
        <h1 class="text-3xl sm:text-4xl font-extrabold text-white font-headline">
          Public Corrections & Clarifications
        </h1>
        <p class="text-xs sm:text-sm text-slate-400 leading-relaxed">
          KKEVO STUDIO MEDIA adheres to rigorous evidence standards. When an error of fact, number, or attribution occurs, we promptly issue a transparent correction detailing the error, its source, and the corrective action taken.
        </p>
      </div>

      <div v-if="loading" class="py-20 text-center">
        <div class="w-10 h-10 border-4 border-red-500 border-t-transparent rounded-full animate-spin mx-auto"></div>
      </div>

      <div v-else-if="!corrections.length" class="py-16 text-center text-slate-400 text-xs">
        No active correction notices in the archive.
      </div>

      <div v-else class="space-y-6">
        <article
          v-for="c in corrections"
          :key="c.id"
          class="bg-kkevo-navy-900 border border-red-900/40 rounded-lg p-6 space-y-4 shadow-xl"
        >
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-kkevo-navy-800 pb-3">
            <div>
              <span class="text-[11px] font-mono text-red-400 font-bold uppercase tracking-wider block">
                CORRECTION LOGGED &bull; {{ formatDate(c.corrected_at) }}
              </span>
              <router-link
                v-if="c.article_slug"
                :to="`/article/${c.article_slug}`"
                class="text-base font-bold text-white hover:text-kkevo-blue-glow transition font-headline"
              >
                Story: {{ c.article_title }} &rarr;
              </router-link>
            </div>
            <span class="text-xs text-slate-400 font-mono">Reviewed by: {{ c.corrected_by_name || 'Senior Editor' }}</span>
          </div>

          <h3 class="text-sm font-bold text-slate-100">{{ c.title }}</h3>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
            <div class="p-3 bg-kkevo-navy-950 rounded border border-red-950 text-slate-300 space-y-1">
              <span class="text-[11px] uppercase font-mono font-bold text-red-400 block">Original Statement:</span>
              <p>{{ c.original_claim }}</p>
            </div>
            <div class="p-3 bg-kkevo-navy-950 rounded border border-emerald-950 text-slate-200 space-y-1">
              <span class="text-[11px] uppercase font-mono font-bold text-kkevo-green block">Corrected Record:</span>
              <p>{{ c.corrected_claim }}</p>
            </div>
          </div>

          <div class="p-3 bg-black/40 rounded text-xs text-slate-400 leading-relaxed border border-kkevo-navy-800">
            <strong class="text-slate-300 font-mono text-[11px] uppercase block mb-1">Reason & Source of Discrepancy:</strong>
            {{ c.reason_for_correction }}
          </div>
        </article>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { api } from '../services/api';

const corrections = ref([]);
const loading = ref(true);

function formatDate(d) {
  if (!d) return '';
  return new Date(d).toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
}

onMounted(async () => {
  loading.value = true;
  try {
    const res = await api.getCorrections();
    corrections.value = res.results || res;
    document.title = 'Corrections Ledger | KKEVO STUDIO MEDIA';
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
});
</script>
