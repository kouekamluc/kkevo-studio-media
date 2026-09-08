<template>
  <div class="min-h-screen py-8">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <!-- Profile Header -->
      <div class="bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/90 dark:to-[#080D17] border border-slate-200 dark:border-white/[0.08] rounded-2xl p-6 sm:p-8 space-y-4 shadow-sm dark:shadow-xl transition-colors">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-white/[0.08] pb-4">
          <div class="flex items-center gap-4">
            <div class="w-14 h-14 rounded-full bg-blue-50 dark:bg-kkevo-blue/20 border-2 border-kkevo-blue text-kkevo-blue dark:text-white flex items-center justify-center text-xl font-bold font-mono">
              {{ authStore.displayName.charAt(0).toUpperCase() }}
            </div>
            <div>
              <span class="text-xs font-mono font-bold tracking-widest text-kkevo-green uppercase block">
                KKEVO Registered Reader Dossier
              </span>
              <h1 class="text-2xl font-bold text-slate-900 dark:text-white font-headline">{{ authStore.displayName }}</h1>
              <span class="text-xs text-slate-500 dark:text-slate-400 font-mono">{{ authStore.user?.email }} &bull; Role: {{ authStore.role }}</span>
            </div>
          </div>

          <button
            @click="authStore.logout"
            class="px-3 py-1.5 rounded-lg bg-red-50 dark:bg-red-950/40 border border-red-200 dark:border-red-800/60 text-red-600 dark:text-red-400 hover:bg-red-100 dark:hover:bg-red-950 text-xs font-mono transition"
          >
            Sign Out
          </button>
        </div>

        <div class="flex items-center gap-6 text-xs font-mono text-slate-600 dark:text-slate-400">
          <span>Saved Articles: <strong class="text-slate-900 dark:text-white">{{ authStore.bookmarks.length }}</strong></span>
          <span>Verified Account: <strong class="text-kkevo-green font-bold">Active</strong></span>
        </div>
      </div>

      <!-- Bookmarked Stories Section -->
      <div class="space-y-4">
        <div class="flex items-center justify-between border-b border-slate-200 dark:border-white/[0.08] pb-3">
          <h2 class="text-lg font-bold text-slate-900 dark:text-white font-headline flex items-center gap-2">
            <svg class="w-4 h-4 text-kkevo-green" fill="currentColor" viewBox="0 0 24 24">
              <path d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
            </svg>
            Saved Reading List ({{ authStore.bookmarks.length }})
          </h2>
          <span class="text-xs text-slate-500 dark:text-slate-400 font-mono">Stored on your sovereign profile</span>
        </div>

        <div v-if="!authStore.bookmarks.length" class="py-12 text-center text-xs text-slate-500 dark:text-slate-400 font-mono">
          No saved articles yet. Click &ldquo;Save Story&rdquo; on any article to store it here for offline reference.
        </div>

        <div v-else class="space-y-3">
          <article
            v-for="b in authStore.bookmarks"
            :key="b.id"
            class="p-4 bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/90 dark:to-[#080D17] border border-slate-200 dark:border-white/[0.08] rounded-xl flex flex-col sm:flex-row sm:items-center justify-between gap-4 hover:border-slate-300 dark:hover:border-kkevo-blue/40 transition shadow-sm"
          >
            <div class="space-y-1 min-w-0">
              <span class="text-[10px] uppercase font-mono text-kkevo-green font-bold">
                {{ b.article_data?.category_name || 'Investigation' }}
              </span>
              <router-link
                :to="`/article/${b.article_data?.slug}`"
                class="block text-sm font-bold text-slate-900 dark:text-white hover:text-kkevo-blue dark:hover:text-kkevo-blue-glow transition truncate"
              >
                {{ b.article_data?.title }}
              </router-link>
              <span class="text-[11px] text-slate-400 font-mono">
                {{ b.article_data?.reading_time_minutes }} min read
              </span>
            </div>

            <div class="flex items-center gap-2 shrink-0">
              <router-link
                :to="`/article/${b.article_data?.slug}`"
                class="px-3 py-1 bg-kkevo-blue/20 text-kkevo-blue-glow rounded text-xs font-semibold hover:bg-kkevo-blue/30 transition"
              >
                Read Story &rarr;
              </router-link>
              <button
                @click="authStore.toggleBookmark(b.article_data?.id || b.article)"
                class="p-1.5 text-slate-400 hover:text-red-400 transition"
                title="Remove Bookmark"
              >
                &times;
              </button>
            </div>
          </article>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useAuthStore } from '../stores/authStore';

const authStore = useAuthStore();

onMounted(() => {
  authStore.fetchBookmarks();
  document.title = 'Reader Profile & Saved Stories | KKEVO STUDIO MEDIA';
});
</script>
