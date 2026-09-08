<template>
  <section class="mt-16 bg-gradient-to-b from-kkevo-navy-900/90 to-kkevo-navy-950 border-y border-kkevo-navy-800 py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Section Header -->
      <div class="flex items-end justify-between mb-8 pb-3 border-b border-kkevo-navy-800">
        <div>
          <div class="flex items-center gap-2 text-xs font-mono font-bold tracking-widest text-purple-400 uppercase">
            <span class="w-2 h-2 rounded-full bg-purple-500"></span>
            KKEVO STUDIO MEDIA | In-Depth Perspective
          </div>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-white font-headline mt-1">
            Geopolitical & Economic Analysis
          </h2>
        </div>
        <router-link to="/analysis" class="text-xs uppercase font-mono tracking-wider text-purple-400 hover:text-purple-300 transition">
          View All Analysis &rarr;
        </router-link>
      </div>

      <!-- Analysis Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <article
          v-for="story in stories"
          :key="story.id"
          class="bg-kkevo-navy-950/80 border border-kkevo-navy-800/80 rounded-lg p-5 flex flex-col justify-between hover:border-purple-500/40 transition group shadow-lg"
        >
          <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
              <span class="px-2 py-0.5 rounded bg-purple-950/60 text-purple-300 font-semibold border border-purple-500/30 text-[11px]">
                ANALYSIS
              </span>
              <span v-if="story.country_flag" class="text-sm">{{ story.country_flag }} {{ story.country_name }}</span>
            </div>

            <router-link :to="`/article/${story.slug}`" class="block">
              <h3 class="text-base font-bold text-white leading-snug group-hover:text-purple-300 transition font-headline">
                {{ story.title }}
              </h3>
            </router-link>

            <p v-if="story.subtitle" class="text-xs text-slate-400 leading-relaxed line-clamp-3">
              {{ story.subtitle }}
            </p>
          </div>

          <div class="pt-4 mt-4 border-t border-kkevo-navy-800/60 flex items-center justify-between text-xs text-slate-400 font-mono">
            <span>{{ story.authors?.[0]?.display_name || 'Staff' }}</span>
            <span>{{ story.reading_time_minutes }}m read</span>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({
  stories: {
    type: Array,
    default: () => [],
  }
});
</script>
