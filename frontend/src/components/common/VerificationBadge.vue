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
      return 'bg-emerald-950/80 text-kkevo-green border border-kkevo-green/30';
    case 'OFFICIAL_CLAIM':
      return 'bg-blue-950/80 text-kkevo-blue-glow border border-kkevo-blue/30';
    case 'ALLEGATION':
      return 'bg-amber-950/80 text-amber-400 border border-amber-500/30';
    case 'ANALYSIS':
      return 'bg-purple-950/80 text-purple-300 border border-purple-500/30';
    case 'CORRECTION':
      return 'bg-red-950/90 text-red-400 border border-red-500/40';
    default:
      return 'bg-kkevo-navy-800 text-kkevo-silver-dim border border-kkevo-navy-700';
  }
});

const dotStyles = computed(() => {
  switch (props.status) {
    case 'VERIFIED_FACT':
      return 'bg-kkevo-green animate-pulse';
    case 'OFFICIAL_CLAIM':
      return 'bg-kkevo-blue-glow';
    case 'ALLEGATION':
      return 'bg-amber-400';
    case 'ANALYSIS':
      return 'bg-purple-400';
    case 'CORRECTION':
      return 'bg-red-400';
    default:
      return 'bg-slate-400';
  }
});
</script>
