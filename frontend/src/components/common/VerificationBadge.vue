<template>
  <span
    :class="[
      'inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-xs font-semibold uppercase tracking-wider',
      badgeStyles
    ]"
  >
    <span :class="['w-1.5 h-1.5 rounded-full', dotStyles]"></span>
    {{ label || statusDisplay }}
  </span>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  status: {
    type: String,
    required: true,
  },
  label: {
    type: String,
    default: '',
  }
});

const statusDisplay = computed(() => {
  switch (props.status) {
    case 'VERIFIED_FACT':
      return 'Verified Fact';
    case 'OFFICIAL_CLAIM':
      return 'Official Claim';
    case 'ALLEGATION':
      return 'Allegation / Third-Party';
    case 'ANALYSIS':
      return 'KKEVO Analysis';
    case 'CORRECTION':
      return 'Correction';
    default:
      return props.status;
  }
});

const badgeStyles = computed(() => {
  switch (props.status) {
    case 'VERIFIED_FACT':
      return 'bg-emerald-50 text-emerald-800 border border-emerald-300 dark:bg-emerald-950/80 dark:text-kkevo-green dark:border-kkevo-green/30';
    case 'OFFICIAL_CLAIM':
      return 'bg-blue-50 text-blue-800 border border-blue-300 dark:bg-blue-950/80 dark:text-kkevo-blue-glow dark:border-kkevo-blue/30';
    case 'ALLEGATION':
      return 'bg-amber-50 text-amber-800 border border-amber-300 dark:bg-amber-950/80 dark:text-amber-400 dark:border-amber-500/30';
    case 'ANALYSIS':
      return 'bg-purple-50 text-purple-800 border border-purple-300 dark:bg-purple-950/80 dark:text-purple-300 dark:border-purple-500/30';
    case 'CORRECTION':
      return 'bg-red-50 text-red-800 border border-red-300 dark:bg-red-950/90 dark:text-red-400 dark:border-red-500/40';
    default:
      return 'bg-slate-100 text-slate-700 border border-slate-300 dark:bg-[#111A29] dark:text-slate-300 dark:border-white/10';
  }
});

const dotStyles = computed(() => {
  switch (props.status) {
    case 'VERIFIED_FACT':
      return 'bg-emerald-600 dark:bg-kkevo-green animate-pulse';
    case 'OFFICIAL_CLAIM':
      return 'bg-blue-600 dark:bg-kkevo-blue-glow';
    case 'ALLEGATION':
      return 'bg-amber-600 dark:bg-amber-400';
    case 'ANALYSIS':
      return 'bg-purple-600 dark:bg-purple-400';
    case 'CORRECTION':
      return 'bg-red-600 dark:bg-red-400';
    default:
      return 'bg-slate-500 dark:bg-slate-400';
  }
});
</script>
