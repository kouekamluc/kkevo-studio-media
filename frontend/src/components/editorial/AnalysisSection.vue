<template>
  <section class="mt-16 bg-slate-100/90 dark:bg-gradient-to-b dark:from-[#0B0D17] dark:via-[#0E0C1B] dark:to-[#070912] border-y border-slate-200 dark:border-purple-500/20 py-12 transition-colors">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Section Header -->
      <div class="flex items-end justify-between mb-8 pb-3 border-b border-slate-300 dark:border-white/[0.08]">
        <div>
          <div class="flex items-center gap-2 text-xs font-mono font-bold tracking-widest text-purple-600 dark:text-purple-400 uppercase">
            <span class="w-2 h-2 rounded-full bg-purple-500"></span>
            KKEVO STUDIO MEDIA | In-Depth Perspective
          </div>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white font-headline mt-1">
            Geopolitical & Economic Analysis
          </h2>
        </div>
        <router-link to="/analysis" class="text-xs uppercase font-mono tracking-wider text-purple-600 dark:text-purple-400 hover:text-purple-700 dark:hover:text-purple-300 font-bold transition">
          View All Analysis &rarr;
        </router-link>
      </div>

      <!-- Analysis Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <article
          v-for="story in stories"
          :key="story.id"
          class="bg-white dark:bg-gradient-to-b dark:from-[#110F24]/80 dark:to-[#0A0B14] border border-slate-200 dark:border-white/[0.08] rounded-xl p-5 flex flex-col justify-between hover:border-purple-400 dark:hover:border-purple-400/60 transition-all duration-300 group shadow-sm hover:shadow-lg dark:shadow-[0_4px_20px_-4px_rgba(0,0,0,0.6)] dark:hover:shadow-[0_12px_30px_-5px_rgba(168,85,247,0.2)] hover:-translate-y-1"
        >
          <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
              <span class="px-2.5 py-0.5 rounded bg-purple-100 dark:bg-purple-950/80 text-purple-700 dark:text-purple-300 font-bold border border-purple-300 dark:border-purple-500/30 text-[11px]">
                ANALYSIS
              </span>
              <span v-if="story.country_flag" class="text-xs text-slate-600 dark:text-slate-300 font-medium">{{ story.country_flag }} {{ story.country_name }}</span>
            </div>

            <router-link :to="`/article/${story.slug}`" class="block">
              <h3 class="text-base font-bold text-slate-900 dark:text-white leading-snug group-hover:text-purple-600 dark:group-hover:text-purple-300 transition font-headline">
                {{ story.title }}
              </h3>
            </router-link>

            <p v-if="story.subtitle" class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed line-clamp-3">
              {{ story.subtitle }}
            </p>
          </div>

          <div class="pt-4 mt-4 border-t border-slate-100 dark:border-white/[0.06] flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 font-mono">
            <span class="text-slate-700 dark:text-slate-200">{{ story.authors?.[0]?.display_name || 'KKEVO Analyst' }}</span>
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
