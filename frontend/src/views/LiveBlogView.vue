<template>
  <div class="min-h-screen py-8">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <!-- Loading State -->
      <div v-if="loading" class="py-20 text-center">
        <div class="w-10 h-10 border-4 border-red-500 border-t-transparent rounded-full animate-spin mx-auto"></div>
      </div>

      <template v-else-if="liveBlog">
        <!-- Live Blog Header Banner -->
        <header class="bg-white dark:bg-[#0A0E18] border border-red-200 dark:border-red-900/40 rounded-2xl p-6 sm:p-8 space-y-4 shadow-md dark:shadow-xl transition-colors">
          <div class="flex items-center justify-between">
            <span class="inline-flex items-center gap-2 px-3 py-1 rounded bg-red-600 text-white text-xs font-bold uppercase tracking-widest font-mono shadow-sm">
              <span class="w-2 h-2 rounded-full bg-white animate-ping"></span>
              Live Developing Coverage
            </span>
            <span class="text-xs text-slate-500 dark:text-slate-400 font-mono font-bold">
              Started {{ formatDateTime(liveBlog.started_at) }}
            </span>
          </div>

          <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white font-headline">
            {{ liveBlog.title }}
          </h1>

          <p v-if="liveBlog.summary" class="text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
            {{ liveBlog.summary }}
          </p>
        </header>

        <!-- Live Updates Timeline -->
        <div class="space-y-6">
          <div class="flex items-center justify-between border-b border-slate-200 dark:border-white/[0.08] pb-3">
            <h2 class="text-sm uppercase font-mono font-bold tracking-widest text-slate-900 dark:text-slate-200 flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-red-500"></span>
              Timeline of Verified Updates ({{ liveBlog.updates?.length || 0 }})
            </h2>
            <button
              @click="loadLiveBlog"
              class="text-xs text-kkevo-blue dark:text-kkevo-blue-glow hover:underline font-mono font-bold"
            >
              Refresh Timeline &#x21bb;
            </button>
          </div>

          <div v-if="!liveBlog.updates?.length" class="py-12 text-center text-xs text-slate-500 dark:text-slate-400 font-mono">
            No live updates dispatched yet. Monitoring news wires...
          </div>

          <!-- Updates Stream -->
          <div v-else class="space-y-6 relative before:absolute before:inset-0 before:left-3 sm:before:left-4 before:w-0.5 before:bg-slate-200 dark:before:bg-white/[0.08]">
            <article
              v-for="u in liveBlog.updates"
              :key="u.id"
              :class="[
                'relative pl-8 sm:pl-10 p-5 rounded-xl border transition-all duration-200',
                u.is_pinned
                  ? 'bg-red-50/80 dark:bg-red-950/30 border-red-300 dark:border-red-800/60 shadow-md'
                  : 'bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/90 dark:to-[#080D17] border-slate-200 dark:border-white/[0.08] shadow-sm'
              ]"
            >
              <!-- Timeline Marker -->
              <span
                :class="[
                  'absolute left-1.5 sm:left-2.5 top-5 w-3.5 h-3.5 rounded-full border-2 border-white dark:border-[#06090E]',
                  u.is_pinned ? 'bg-red-500 animate-pulse' : 'bg-kkevo-blue'
                ]"
              ></span>

              <!-- Update Meta -->
              <div class="flex items-center justify-between gap-2 mb-2 text-xs font-mono">
                <span class="text-kkevo-green font-bold">{{ formatTime(u.timestamp) }}</span>
                <span v-if="u.is_pinned" class="px-2 py-0.5 rounded bg-red-600 text-white font-bold text-[10px] uppercase shadow-sm">
                  Pinned Key Update
                </span>
              </div>

              <!-- Update Headline & Content -->
              <h3 class="text-base font-bold text-slate-900 dark:text-white font-headline mb-2">{{ u.headline }}</h3>
              <p class="text-sm text-slate-600 dark:text-slate-300 leading-relaxed">{{ u.content }}</p>

              <!-- Author / Source Credit -->
              <div v-if="u.author" class="mt-3 pt-2.5 border-t border-slate-100 dark:border-white/[0.06] text-[11px] text-slate-500 dark:text-slate-400 font-mono">
                Filed by {{ u.author.display_name }} &bull; KKEVO Newsroom
              </div>
            </article>
          </div>
        </div>
      </template>

      <div v-else class="py-16 text-center text-slate-400 text-xs">
        No active live blog currently in session.
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { api } from '../services/api';

const route = useRoute();
const liveBlog = ref(null);
const loading = ref(true);

function formatDateTime(dt) {
  if (!dt) return '';
  return new Date(dt).toLocaleString('en-US', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
}

function formatTime(dt) {
  if (!dt) return '';
  return new Date(dt).toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: false });
}

async function loadLiveBlog() {
  loading.value = true;
  try {
    const slug = route.params.slug;
    if (slug) {
      liveBlog.value = await api.getLiveBlog(slug);
    } else {
      const blogs = await api.getLiveBlogs();
      liveBlog.value = (blogs.results || blogs)?.[0] || null;
    }
    if (liveBlog.value) {
      document.title = `LIVE: ${liveBlog.value.title} | KKEVO STUDIO MEDIA`;
    }
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
}

onMounted(loadLiveBlog);
</script>
