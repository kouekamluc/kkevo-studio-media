<template>
  <div class="bg-white dark:bg-kkevo-navy-900 border border-slate-200 dark:border-kkevo-navy-800 rounded-xl p-5 shadow-sm dark:shadow-none transition-colors">
    <div class="flex items-center justify-between border-b border-slate-200 dark:border-kkevo-navy-800 pb-3 mb-4">
      <div class="flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full bg-kkevo-green animate-ping"></span>
        <h3 class="text-xs uppercase font-bold tracking-widest text-slate-900 dark:text-white font-mono">
          Latest Verified Developments
        </h3>
      </div>
      <router-link to="/category/news" class="text-xs text-kkevo-blue dark:text-kkevo-blue-glow hover:underline font-mono">
        All News &rarr;
      </router-link>
    </div>

    <div class="divide-y divide-slate-100 dark:divide-kkevo-navy-800/80">
      <article
        v-for="item in newsItems"
        :key="item.id"
        class="py-3.5 first:pt-0 last:pb-0 group"
      >
        <div class="flex items-baseline gap-2 mb-1">
          <span class="text-[11px] font-mono font-semibold text-slate-500 dark:text-slate-400">
            {{ formatTime(item.published_at) }}
          </span>
          <span class="text-slate-300 dark:text-slate-600">&bull;</span>
          <span class="text-[11px] uppercase tracking-wider text-kkevo-green font-bold">
            {{ item.category_name }}
          </span>
        </div>

        <router-link :to="`/article/${item.slug}`" class="block">
          <h4 class="text-sm font-semibold text-slate-800 dark:text-slate-200 group-hover:text-kkevo-blue dark:group-hover:text-white leading-snug transition-colors">
            {{ item.title }}
          </h4>
        </router-link>
      </article>

      <div v-if="!newsItems.length" class="py-6 text-center text-xs text-slate-500">
        No recent updates at this hour.
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  newsItems: {
    type: Array,
    default: () => [],
  }
});

function formatTime(timestamp) {
  if (!timestamp) return 'Just now';
  const date = new Date(timestamp);
  return date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: false });
}
</script>
