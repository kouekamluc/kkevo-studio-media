<template>
  <footer class="bg-slate-100 dark:bg-kkevo-navy-950 border-t border-slate-200 dark:border-kkevo-navy-800 text-slate-600 dark:text-slate-400 text-sm mt-20 transition-colors">
    <!-- Top Footer Segment -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8">
        <!-- Brand Identity Column -->
        <div class="lg:col-span-2 space-y-4">
          <router-link to="/" class="inline-block">
            <div class="p-1 rounded bg-black dark:bg-transparent shadow-sm dark:shadow-none inline-block">
              <img
                src="/assets/logo.png"
                alt="KKEVO STUDIO MEDIA"
                class="h-14 w-auto object-contain"
              />
            </div>
          </router-link>
          <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed max-w-sm">
            KKEVO STUDIO MEDIA is an independent, African-centred global digital media institution. Delivering verified facts, geopolitical perspective, and in-depth structural analysis.
          </p>
          <div class="flex items-center gap-4 text-xs font-mono text-slate-700 dark:text-slate-300">
            <span class="text-kkevo-green font-bold">FACTS.</span>
            <span class="text-kkevo-blue dark:text-kkevo-blue-glow font-bold">PERSPECTIVE.</span>
            <span class="text-slate-900 dark:text-white font-bold">IMPACT.</span>
          </div>
        </div>

        <!-- Newsroom Sections -->
        <div>
          <h4 class="text-xs uppercase font-bold tracking-widest text-slate-900 dark:text-slate-200 mb-3 font-mono">Sections</h4>
          <ul class="space-y-2 text-xs">
            <li><router-link to="/category/news" class="hover:text-slate-900 dark:hover:text-white transition">Fast News & Developments</router-link></li>
            <li><router-link to="/category/geopolitics" class="hover:text-slate-900 dark:hover:text-white transition">African Geopolitics</router-link></li>
            <li><router-link to="/category/economy" class="hover:text-slate-900 dark:hover:text-white transition">Continental Economy</router-link></li>
            <li><router-link to="/category/resources" class="hover:text-slate-900 dark:hover:text-white transition">Resources & Industrialisation</router-link></li>
            <li><router-link to="/category/technology" class="hover:text-slate-900 dark:hover:text-white transition">Technology & Patents</router-link></li>
            <li><router-link to="/category/history" class="hover:text-slate-900 dark:hover:text-white transition">The Africa They Never Taught You</router-link></li>
            <li><router-link to="/analysis" class="text-purple-600 dark:text-purple-400 hover:underline font-semibold transition">KKEVO Analysis</router-link></li>
          </ul>
        </div>

        <!-- Editorial & Trust Standards -->
        <div>
          <h4 class="text-xs uppercase font-bold tracking-widest text-slate-900 dark:text-slate-200 mb-3 font-mono">Trust & Standards</h4>
          <ul class="space-y-2 text-xs">
            <li><router-link to="/legal/editorial-standards" class="hover:text-slate-900 dark:hover:text-white transition">Editorial Standards</router-link></li>
            <li><router-link to="/corrections" class="text-red-600 dark:text-red-400 hover:underline font-semibold transition">Corrections Ledger</router-link></li>
            <li><router-link to="/legal/sources-policy" class="hover:text-slate-900 dark:hover:text-white transition">Source & Citation Policy</router-link></li>
            <li><router-link to="/legal/ai-policy" class="hover:text-slate-900 dark:hover:text-white transition">AI & Synthetic Media Policy</router-link></li>
            <li><router-link to="/legal/ethics" class="hover:text-slate-900 dark:hover:text-white transition">Journalistic Ethics</router-link></li>
            <li><router-link to="/editorial" class="text-kkevo-blue dark:text-kkevo-blue-glow hover:underline transition font-semibold">Newsroom Staff Portal</router-link></li>
          </ul>
        </div>

        <!-- Intelligence Briefings & Feeds -->
        <div>
          <h4 class="text-xs uppercase font-bold tracking-widest text-slate-900 dark:text-slate-200 mb-3 font-mono">Syndication</h4>
          <ul class="space-y-2 text-xs">
            <li>
              <button @click="newsStore.toggleNewsletterModal(true)" class="text-kkevo-green hover:underline flex items-center gap-1 font-bold">
                <span>Daily Intelligence Briefing</span> &rarr;
              </button>
            </li>
            <li><a href="/feeds/rss/" target="_blank" class="hover:text-slate-900 dark:hover:text-white transition">RSS 2.0 Feed</a></li>
            <li><a href="/feeds/rss/analysis/" target="_blank" class="hover:text-slate-900 dark:hover:text-white transition">RSS Analysis Feed</a></li>
            <li><a href="/feeds/sitemap.xml" target="_blank" class="hover:text-slate-900 dark:hover:text-white transition">XML News Sitemap</a></li>
            <li><router-link to="/legal/contact" class="hover:text-slate-900 dark:hover:text-white transition">Newsroom Contact & Whistleblowers</router-link></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Bottom Legal Bar -->
    <div class="border-t border-slate-200 dark:border-kkevo-navy-900 bg-slate-200/50 dark:bg-black/40 py-6 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-slate-500 dark:text-slate-400">
        <p>&copy; {{ new Date().getFullYear() }} KKEVO STUDIO MEDIA. All Rights Reserved. Not government or corporate propaganda.</p>
        <div class="flex items-center gap-6">
          <router-link to="/legal/privacy" class="hover:text-slate-800 dark:hover:text-slate-300">Privacy Policy</router-link>
          <router-link to="/legal/terms" class="hover:text-slate-800 dark:hover:text-slate-300">Terms of Use</router-link>
          <router-link to="/legal/cookies" class="hover:text-slate-800 dark:hover:text-slate-300">Cookie Settings</router-link>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { useNewsStore } from '../../stores/newsStore';

const newsStore = useNewsStore();
</script>
