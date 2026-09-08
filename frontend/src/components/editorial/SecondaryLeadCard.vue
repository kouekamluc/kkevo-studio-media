<template>
  <article v-if="story" class="group bg-white dark:bg-kkevo-navy-900 border border-slate-200 dark:border-kkevo-navy-800 rounded-xl overflow-hidden hover:border-slate-300 dark:hover:border-kkevo-navy-700 transition-all duration-300 flex flex-col justify-between shadow-sm hover:shadow-lg dark:shadow-none hover:-translate-y-0.5">
    <div>
      <!-- Thumbnail -->
      <router-link :to="`/article/${story.slug}`" class="block relative aspect-[16/10] overflow-hidden bg-slate-900">
        <img
          :src="story.effective_hero_image || 'https://images.unsplash.com/photo-1541888946425-d0fbb18086f6?auto=format&fit=crop&w=600&q=80'"
          :alt="story.title"
          class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 opacity-95 group-hover:opacity-100"
          loading="lazy"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-60"></div>
        
        <div class="absolute top-2.5 left-2.5 flex items-center gap-1.5 z-10">
          <span class="px-2.5 py-0.5 bg-black/80 text-kkevo-blue-glow text-[11px] font-bold uppercase tracking-wider rounded backdrop-blur-md border border-kkevo-blue/30 shadow-sm">
            {{ story.category_name }}
          </span>
          <span v-if="story.country_flag" class="px-1.5 py-0.5 bg-black/80 text-xs rounded backdrop-blur-md">
            {{ story.country_flag }}
          </span>
        </div>
      </router-link>

      <!-- Content -->
      <div class="p-5 space-y-2.5">
        <router-link :to="`/article/${story.slug}`" class="block">
          <h3 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white leading-snug font-headline group-hover:text-kkevo-green transition-colors">
            {{ story.title }}
          </h3>
        </router-link>

        <p v-if="story.subtitle" class="text-xs text-slate-600 dark:text-slate-400 line-clamp-2 leading-relaxed font-normal">
          {{ story.subtitle }}
        </p>
      </div>
    </div>

    <!-- Metadata Footer -->
    <div class="px-5 pb-4 pt-3 border-t border-slate-100 dark:border-kkevo-navy-800/80 flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 font-mono">
      <span class="font-medium text-slate-700 dark:text-slate-300">{{ story.authors?.[0]?.display_name || 'KKEVO Staff' }}</span>
      <span class="flex items-center gap-1">
        <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        {{ story.reading_time_minutes }}m
      </span>
    </div>
  </article>
</template>

<script setup>
defineProps({
  story: {
    type: Object,
    required: true,
  }
});
</script>
