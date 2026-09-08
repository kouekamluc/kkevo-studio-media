<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 flex items-start justify-center pt-16 px-4 sm:px-6 bg-black/60 dark:bg-black/80 backdrop-blur-sm">
    <div class="bg-white dark:bg-[#0B101B] border border-slate-200 dark:border-white/[0.08] rounded-2xl max-w-2xl w-full p-6 sm:p-7 shadow-2xl space-y-4 transition-colors">
      <div class="flex items-center justify-between border-b border-slate-200 dark:border-white/[0.08] pb-3">
        <h3 class="text-sm font-bold uppercase tracking-widest text-slate-900 dark:text-white font-mono flex items-center gap-2">
          <svg class="w-4 h-4 text-kkevo-blue dark:text-kkevo-blue-glow" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          Search KKEVO Media
        </h3>
        <button @click="$emit('close')" class="text-slate-400 hover:text-slate-800 dark:hover:text-white transition-colors">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Search Input -->
      <div class="relative">
        <input
          v-model="searchQuery"
          @keyup.enter="handleSearch"
          type="text"
          placeholder="Search by topic, country, mineral, treaty, or author..."
          class="w-full bg-slate-50 dark:bg-[#06090E] border border-slate-300 dark:border-white/[0.1] rounded-xl px-4 py-3 text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:border-kkevo-blue text-sm"
          autofocus
        />
        <button
          @click="handleSearch"
          class="absolute right-2 top-2 px-3.5 py-1.5 bg-kkevo-blue text-white rounded-lg text-xs font-semibold hover:bg-kkevo-blue-dark transition shadow-sm"
        >
          Search
        </button>
      </div>

      <!-- Suggested Topics -->
      <div class="pt-2">
        <span class="text-xs uppercase font-mono text-slate-500 dark:text-slate-400 block mb-2 font-bold">Priority Focus Areas:</span>
        <div class="flex flex-wrap gap-2">
          <button
            v-for="kw in quickKeywords"
            :key="kw"
            @click="selectKeyword(kw)"
            class="px-2.5 py-1 rounded-md bg-slate-100 dark:bg-white/[0.05] border border-slate-200 dark:border-white/[0.08] text-xs text-slate-700 dark:text-slate-300 hover:text-slate-950 dark:hover:text-white hover:bg-slate-200 dark:hover:bg-white/[0.1] transition font-medium"
          >
            {{ kw }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

defineProps({
  isOpen: Boolean
});

const emit = defineEmits(['close']);
const router = useRouter();
const searchQuery = ref('');

const quickKeywords = [
  'Geological Data DRC',
  'AfCFTA Rail',
  'Ghana Gold Refineries',
  'Zimbabwe Lithium Mandate',
  'Alliance of Sahel States',
  'Critical Minerals'
];

function handleSearch() {
  if (!searchQuery.value.trim()) return;
  emit('close');
  router.push({ path: '/search', query: { q: searchQuery.value.trim() } });
}

function selectKeyword(kw) {
  searchQuery.value = kw;
  handleSearch();
}
</script>
