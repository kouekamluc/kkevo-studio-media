<template>
  <article v-if="story" class="group bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg overflow-hidden hover:border-kkevo-navy-700 transition flex flex-col justify-between">
    <div>
      <!-- Thumbnail -->
      <router-link :to="`/article/${story.slug}`" class="block relative aspect-[16/9] overflow-hidden bg-black">
        <img
          :src="story.effective_hero_image || 'https://images.unsplash.com/photo-1541888946425-d0fbb18086f6?auto=format&fit=crop&w=600&q=80'"
          :alt="story.title"
          class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 opacity-90 group-hover:opacity-100"
          loading="lazy"
        />
        <div class="absolute top-2.5 left-2.5 flex items-center gap-1.5">
          <span class="px-2 py-0.5 bg-black/80 text-kkevo-blue-glow text-[11px] font-bold uppercase tracking-wider rounded backdrop-blur border border-kkevo-blue/30">
            {{ story.category_name }}
          </span>
          <span v-if="story.country_flag" class="px-1.5 py-0.5 bg-black/80 text-xs rounded backdrop-blur">
            {{ story.country_flag }}
          </span>
        </div>
      </router-link>

      <!-- Content -->
      <div class="p-5 space-y-2.5">
        <router-link :to="`/article/${story.slug}`" class="block">
          <h3 class="text-base sm:text-lg font-bold text-white leading-snug font-headline group-hover:text-kkevo-green transition-colors">
            {{ story.title }}
          </h3>
        </router-link>

        <p v-if="story.subtitle" class="text-xs text-slate-400 line-clamp-2 leading-relaxed">
          {{ story.subtitle }}
        </p>
      </div>
    </div>

    <!-- Metadata Footer -->
    <div class="px-5 pb-4 pt-2 border-t border-kkevo-navy-800/60 flex items-center justify-between text-xs text-slate-400 font-mono">
      <span>{{ story.authors?.[0]?.display_name || 'KKEVO Staff' }}</span>
      <span>{{ story.reading_time_minutes }} min read</span>
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
