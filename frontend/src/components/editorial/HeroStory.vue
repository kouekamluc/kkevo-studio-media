<template>
  <article v-if="story" class="relative group bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg overflow-hidden hover:border-kkevo-navy-700 transition shadow-2xl">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-0">
      <!-- Media Column -->
      <div class="lg:col-span-7 relative overflow-hidden bg-black aspect-[16/10] lg:aspect-auto min-h-[300px] lg:min-h-[460px]">
        <img
          :src="story.effective_hero_image || 'https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=1200&q=80'"
          :alt="story.title"
          class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-90 group-hover:opacity-100"
          loading="eager"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-kkevo-navy-950 via-transparent to-transparent opacity-80 lg:opacity-40"></div>
        
        <!-- Category & Country Tags Overlay -->
        <div class="absolute top-4 left-4 flex flex-wrap gap-2 z-10">
          <span class="px-2.5 py-1 bg-kkevo-navy-950/90 text-kkevo-green text-xs font-bold uppercase tracking-wider rounded border border-kkevo-green/30 backdrop-blur">
            {{ story.category_name }}
          </span>
          <span v-if="story.country_name" class="px-2.5 py-1 bg-kkevo-navy-950/90 text-slate-200 text-xs font-semibold rounded border border-slate-700 backdrop-blur flex items-center gap-1">
            <span>{{ story.country_flag }}</span>
            <span>{{ story.country_name }}</span>
          </span>
        </div>

        <!-- Image Caption (Desktop) -->
        <div v-if="story.hero_caption" class="absolute bottom-3 left-4 right-4 hidden sm:block text-[11px] text-slate-400 bg-black/60 px-3 py-1.5 rounded backdrop-blur max-w-xl">
          {{ story.hero_caption }} <span v-if="story.hero_credit" class="text-slate-400">({{ story.hero_credit }})</span>
        </div>
      </div>

      <!-- Content Column -->
      <div class="lg:col-span-5 p-6 sm:p-8 flex flex-col justify-between space-y-6">
        <div class="space-y-4">
          <!-- Kicker / Content Type Badge -->
          <div class="flex items-center gap-2">
            <span class="text-xs uppercase font-mono tracking-widest text-kkevo-blue-glow font-bold">
              KKEVO STUDIO MEDIA &bull; {{ story.content_type_display }}
            </span>
          </div>

          <!-- Main Dominant Headline -->
          <router-link :to="`/article/${story.slug}`" class="block">
            <h1 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-white leading-tight font-headline hover:text-kkevo-green transition-colors">
              {{ story.title }}
            </h1>
          </router-link>

          <!-- Dek / Subtitle -->
          <p v-if="story.subtitle" class="text-sm sm:text-base text-slate-300 leading-relaxed font-light">
            {{ story.subtitle }}
          </p>
        </div>

        <!-- Metadata & Author Byline -->
        <div class="pt-4 border-t border-kkevo-navy-800 flex items-center justify-between text-xs text-slate-400">
          <div class="flex items-center gap-3">
            <img
              v-if="story.authors?.[0]?.effective_avatar"
              :src="story.authors[0].effective_avatar"
              :alt="story.authors[0].display_name"
              class="w-9 h-9 rounded-full object-cover border border-kkevo-navy-700"
            />
            <div>
              <span class="font-medium text-slate-200 block">{{ story.authors?.[0]?.display_name || 'KKEVO Newsroom' }}</span>
              <span class="text-[11px] text-slate-400 font-mono">{{ story.reading_time_minutes }} min read &bull; {{ formattedDate }}</span>
            </div>
          </div>

          <button
            @click.stop="authStore.toggleBookmark(story.id)"
            :class="['p-2 rounded hover:bg-kkevo-navy-800 transition', authStore.isBookmarked(story.id) ? 'text-kkevo-green' : 'text-slate-400']"
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
