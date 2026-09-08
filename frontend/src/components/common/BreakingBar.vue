<template>
  <div
    v-if="alert"
    class="bg-gradient-to-r from-red-600 via-rose-600 to-red-700 dark:from-[#18070B] dark:via-[#130508] dark:to-[#0A0406] border-b border-red-700 dark:border-red-900/60 text-white dark:text-slate-100 text-sm shadow-md transition-colors duration-200"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2 flex items-center justify-between gap-4">
      <div class="flex items-center gap-3 min-w-0">
        <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-white dark:bg-red-600 text-red-700 dark:text-white font-extrabold text-[11px] uppercase tracking-wider shadow-sm shrink-0">
          <span class="w-2 h-2 rounded-full bg-red-600 dark:bg-white animate-ping"></span>
          Breaking Alert
        </div>
        <router-link
          :to="alert.target_url || '#'"
          class="font-bold text-white dark:text-slate-100 hover:text-red-100 dark:hover:text-red-300 truncate flex items-center gap-2 transition-colors group"
        >
          <span class="truncate">{{ alert.headline }}</span>
          <span class="hidden sm:inline-flex items-center text-xs text-red-100 dark:text-red-400 shrink-0 font-mono font-bold bg-white/15 dark:bg-red-950/60 border border-white/20 dark:border-red-500/30 px-2 py-0.5 rounded group-hover:bg-white/25 transition">
            Live Coverage &rarr;
          </span>
        </router-link>
      </div>

      <button
        @click="$emit('dismiss')"
        class="text-white/80 hover:text-white dark:text-slate-400 dark:hover:text-white p-1 rounded hover:bg-white/10 dark:hover:bg-white/5 shrink-0 transition-colors"
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
