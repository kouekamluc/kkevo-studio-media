<template>
  <article v-if="story" class="relative group bg-white dark:bg-kkevo-navy-900 border border-slate-200 dark:border-kkevo-navy-800 rounded-xl overflow-hidden hover:border-slate-300 dark:hover:border-kkevo-navy-700 transition-all duration-300 shadow-md hover:shadow-xl dark:shadow-2xl">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-0">
      <!-- Media Column -->
      <div class="lg:col-span-7 relative overflow-hidden bg-slate-900 aspect-[16/10] lg:aspect-auto min-h-[300px] lg:min-h-[460px]">
        <img
          :src="story.effective_hero_image || 'https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=1200&q=80'"
          :alt="story.title"
          class="w-full h-full object-cover group-hover:scale-[1.03] transition-transform duration-700 opacity-95 group-hover:opacity-100"
          loading="eager"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent lg:opacity-60"></div>
        
        <!-- Category & Country Tags Overlay -->
        <div class="absolute top-4 left-4 flex flex-wrap gap-2 z-10">
          <span class="px-3 py-1 bg-black/85 text-kkevo-green text-xs font-bold uppercase tracking-wider rounded-md border border-kkevo-green/40 backdrop-blur-md shadow-sm">
            {{ story.category_name }}
          </span>
          <span v-if="story.country_name" class="px-3 py-1 bg-black/85 text-slate-100 text-xs font-semibold rounded-md border border-slate-700 backdrop-blur-md flex items-center gap-1.5 shadow-sm">
            <span>{{ story.country_flag }}</span>
            <span>{{ story.country_name }}</span>
          </span>
        </div>

        <!-- Image Caption (Desktop) -->
        <div v-if="story.hero_caption" class="absolute bottom-3 left-4 right-4 hidden sm:block text-[11px] text-slate-300 bg-black/75 px-3 py-1.5 rounded-md backdrop-blur-md max-w-xl border border-white/10">
          {{ story.hero_caption }} <span v-if="story.hero_credit" class="text-slate-400 font-mono">({{ story.hero_credit }})</span>
        </div>
      </div>

      <!-- Content Column -->
      <div class="lg:col-span-5 p-6 sm:p-8 flex flex-col justify-between space-y-6">
        <div class="space-y-4">
          <!-- Kicker / Content Type Badge -->
          <div class="flex items-center gap-2">
            <span class="text-xs uppercase font-mono tracking-widest text-kkevo-blue dark:text-kkevo-blue-glow font-bold">
              KKEVO STUDIO MEDIA &bull; {{ story.content_type_display }}
            </span>
          </div>

          <!-- Main Dominant Headline -->
          <router-link :to="`/article/${story.slug}`" class="block group/title">
            <h1 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-slate-900 dark:text-white leading-[1.2] font-headline group-hover/title:text-kkevo-green transition-colors">
              {{ story.title }}
            </h1>
          </router-link>

          <!-- Dek / Subtitle -->
          <p v-if="story.subtitle" class="text-sm sm:text-base text-slate-600 dark:text-slate-300 leading-relaxed font-normal">
            {{ story.subtitle }}
          </p>
        </div>

        <!-- Metadata & Author Byline -->
        <div class="pt-4 border-t border-slate-200 dark:border-kkevo-navy-800 flex items-center justify-between text-xs text-slate-500 dark:text-slate-400">
          <div class="flex items-center gap-3">
            <img
              v-if="story.authors?.[0]?.effective_avatar"
              :src="story.authors[0].effective_avatar"
              :alt="story.authors[0].display_name"
              class="w-10 h-10 rounded-full object-cover border-2 border-kkevo-green/40 shadow-sm"
            />
            <div>
              <span class="font-bold text-slate-900 dark:text-slate-200 block text-sm">{{ story.authors?.[0]?.display_name || 'KKEVO Newsroom' }}</span>
              <span class="text-[11px] text-slate-500 dark:text-slate-400 font-mono">{{ story.reading_time_minutes }} min read &bull; {{ formattedDate }}</span>
            </div>
          </div>

          <button
            @click.stop="authStore.toggleBookmark(story.id)"
            :class="[
              'p-2.5 rounded-lg border transition-all',
              authStore.isBookmarked(story.id)
                ? 'bg-kkevo-green/20 border-kkevo-green text-kkevo-green'
                : 'bg-slate-100 dark:bg-kkevo-navy-800 border-slate-200 dark:border-kkevo-navy-700 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
            ]"
            title="Save Story"
          >
            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
              <path d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </article>
</template>

<script setup>
import { computed } from 'vue';
import { useAuthStore } from '../../stores/authStore';

const props = defineProps({
  story: {
    type: Object,
    required: true,
  }
});

const authStore = useAuthStore();

const formattedDate = computed(() => {
  if (!props.story?.published_at) return '';
  const date = new Date(props.story.published_at);
  return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
});
</script>
