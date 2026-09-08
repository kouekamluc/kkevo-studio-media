<template>
  <section class="mt-16 bg-black/60 border-y border-kkevo-navy-800 py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-end justify-between mb-8 pb-3 border-b border-kkevo-navy-800">
        <div>
          <div class="flex items-center gap-2 text-xs font-mono font-bold tracking-widest text-kkevo-blue-glow uppercase">
            <span class="w-2 h-2 rounded-full bg-kkevo-blue"></span>
            KKEVO Visual & Broadcast Journalism
          </div>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-white font-headline mt-1">
            60 Seconds of Context & Documentaries
          </h2>
        </div>
        <router-link to="/video" class="text-xs uppercase font-mono tracking-wider text-kkevo-blue-glow hover:text-white transition">
          Browse Video Archive &rarr;
        </router-link>
      </div>

      <!-- Video Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="v in videos"
          :key="v.id"
          class="bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg overflow-hidden group cursor-pointer hover:border-kkevo-blue/50 transition"
          @click="activeVideo = v"
        >
          <!-- Video Thumbnail with Play Button -->
          <div class="relative aspect-video bg-black overflow-hidden">
            <img
              :src="v.thumbnail_url || 'https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=600&q=80'"
              :alt="v.title"
              class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 opacity-80 group-hover:opacity-100"
            />
            <div class="absolute inset-0 flex items-center justify-center">
              <div class="w-12 h-12 rounded-full bg-kkevo-blue/90 text-white flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform">
                <svg class="w-5 h-5 ml-0.5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M8 5v14l11-7z" />
                </svg>
              </div>
            </div>
            <!-- Duration Badge -->
            <div class="absolute bottom-2 right-2 px-2 py-0.5 rounded bg-black/80 text-[11px] font-mono text-white backdrop-blur">
              {{ v.formatted_duration || '1:04' }}
            </div>
          </div>

          <!-- Video Title & Details -->
          <div class="p-4 space-y-2">
            <span class="text-[10px] font-mono uppercase tracking-widest text-kkevo-blue-glow font-bold">
              {{ v.type_display || 'Short Reel' }}
            </span>
            <h3 class="text-sm font-bold text-white leading-snug group-hover:text-kkevo-blue-glow transition line-clamp-2">
              {{ v.title }}
            </h3>
            <p v-if="v.summary" class="text-xs text-slate-400 line-clamp-2 leading-relaxed">
              {{ v.summary }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Interactive Video Lightbox Modal -->
    <div v-if="activeVideo" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/90 backdrop-blur-md">
      <div class="bg-kkevo-navy-950 border border-kkevo-navy-700 rounded-lg max-w-4xl w-full p-6 shadow-2xl relative space-y-4">
        <button @click="activeVideo = null" class="absolute top-4 right-4 text-slate-400 hover:text-white z-10">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>

        <h3 class="text-lg font-bold text-white font-headline pr-8">{{ activeVideo.title }}</h3>

        <div class="aspect-video bg-black rounded overflow-hidden">
          <video
            controls
            autoplay
            :src="activeVideo.video_url"
            class="w-full h-full"
          >
            Your browser does not support video playback.
          </video>
        </div>

        <div v-if="activeVideo.transcript" class="p-3 bg-kkevo-navy-900 rounded border border-kkevo-navy-800 text-xs text-slate-300 leading-relaxed max-h-32 overflow-y-auto">
          <span class="font-bold text-kkevo-green block mb-1 font-mono uppercase text-[11px]">Transcript:</span>
          {{ activeVideo.transcript }}
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

defineProps({
  videos: {
    type: Array,
    default: () => [],
  }
});

const activeVideo = ref(null);
</script>
