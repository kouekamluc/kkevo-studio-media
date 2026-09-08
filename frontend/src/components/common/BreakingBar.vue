<template>
  <div v-if="alert" class="bg-gradient-to-r from-red-950 via-kkevo-navy-900 to-kkevo-navy-900 border-y border-red-800/40 text-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2 flex items-center justify-between gap-4">
      <div class="flex items-center gap-3 min-w-0">
        <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-red-600 text-white font-bold text-xs uppercase tracking-widest animate-pulse shrink-0">
          Breaking
        </span>
        <router-link
          :to="alert.target_url || '#'"
          class="font-medium text-slate-100 hover:text-white truncate hover:underline flex items-center gap-2 transition-colors"
        >
          <span>{{ alert.headline }}</span>
          <span class="text-xs text-red-400 shrink-0 font-mono">Live &rarr;</span>
        </router-link>
      </div>

      <button
        @click="$emit('dismiss')"
        class="text-slate-400 hover:text-slate-200 p-1 shrink-0"
        title="Dismiss Alert"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  alert: {
    type: Object,
    default: null,
  }
});

defineEmits(['dismiss']);
</script>
