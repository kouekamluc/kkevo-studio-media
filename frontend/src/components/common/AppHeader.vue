<template>
  <header class="w-full sticky top-0 z-40 transition-colors shadow-sm dark:shadow-none">
    <!-- Top Utility Bar -->
    <div class="border-b border-slate-200 dark:border-kkevo-navy-800/80 bg-slate-100 dark:bg-[#070B12] text-xs text-slate-600 dark:text-slate-300 py-1.5 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto flex items-center justify-between">
        <!-- Date and Edition -->
        <div class="flex items-center gap-4">
          <span class="font-medium text-slate-800 dark:text-slate-200 font-mono">{{ currentDateFormatted }}</span>
          <span class="hidden md:inline text-slate-300 dark:text-slate-700">|</span>
          <span class="hidden md:inline text-slate-600 dark:text-slate-400 font-medium">African-Centred Global Newsroom</span>
        </div>

        <!-- Utility Actions -->
        <div class="flex items-center gap-4">
          <!-- Language Selector -->
          <div class="hidden sm:flex items-center gap-2 text-xs font-mono">
            <span class="text-kkevo-green font-bold">EN</span>
            <span class="text-slate-300 dark:text-slate-700">/</span>
            <span class="text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white cursor-pointer transition">FR</span>
            <span class="text-slate-300 dark:text-slate-700">/</span>
            <span class="text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white cursor-pointer transition">SW</span>
          </div>

          <span class="hidden sm:inline text-slate-300 dark:text-slate-700">|</span>

          <!-- Newsletter Trigger -->
          <button
            @click="newsStore.toggleNewsletterModal(true)"
            class="text-kkevo-blue dark:text-kkevo-blue-glow hover:text-kkevo-blue-dark dark:hover:text-white font-medium flex items-center gap-1.5 transition-colors"
          >
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            <span class="hidden xs:inline font-semibold">Intelligence Briefings</span>
          </button>

          <span class="text-slate-300 dark:text-slate-700">|</span>

          <!-- Search Button -->
          <button
            @click="newsStore.toggleSearchModal(true)"
            class="text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white flex items-center gap-1.5 transition-colors"
            title="Search KKEVO Media"
          >
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
            <span class="hidden md:inline">Search</span>
          </button>

          <span class="text-slate-300 dark:text-slate-700">|</span>

          <!-- Theme Toggle Button (Sun/Moon) -->
          <button
            @click="themeStore.toggleTheme"
            class="px-2 py-1 rounded-md bg-slate-200 dark:bg-kkevo-navy-850 text-slate-800 dark:text-slate-200 hover:bg-slate-300 dark:hover:bg-kkevo-navy-800 transition-colors flex items-center gap-1.5 border border-slate-300 dark:border-white/10"
            :title="themeStore.currentTheme === 'dark' ? 'Switch to Light Theme' : 'Switch to Dark Theme'"
          >
            <!-- Sun icon in dark mode -->
            <svg v-if="themeStore.currentTheme === 'dark'" class="w-3.5 h-3.5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
            </svg>
            <!-- Moon icon in light mode -->
            <svg v-else class="w-3.5 h-3.5 text-slate-700" fill="currentColor" viewBox="0 0 24 24">
              <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z" />
            </svg>
            <span class="text-[11px] font-mono font-bold">{{ themeStore.currentTheme === 'dark' ? 'Light' : 'Dark' }}</span>
          </button>

          <span class="text-slate-300 dark:text-slate-700">|</span>

          <!-- Reader Dossier / Editorial Login -->
          <div v-if="authStore.isAuthenticated" class="flex items-center gap-2">
            <router-link
              to="/profile"
              class="font-medium text-slate-700 dark:text-slate-200 hover:text-kkevo-blue dark:hover:text-white transition-colors flex items-center gap-1"
            >
              <svg class="w-3 h-3 text-kkevo-green" fill="currentColor" viewBox="0 0 24 24">
                <path d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
              </svg>
              <span>Saved ({{ authStore.bookmarks.length }})</span>
            </router-link>
            <router-link
              v-if="authStore.isStaff"
              to="/editorial"
              class="px-2 py-0.5 rounded bg-kkevo-blue/15 text-kkevo-blue dark:text-kkevo-blue-glow border border-kkevo-blue/40 font-bold hover:bg-kkevo-blue/25 transition-colors"
            >
              Newsroom
            </router-link>
            <button
              @click="authStore.logout"
              class="text-slate-500 hover:text-red-500 transition-colors ml-1"
              title="Sign Out"
            >
              &times;
            </button>
          </div>
          <button
            v-else
            @click="authStore.toggleAuthModal(true)"
            class="text-slate-700 dark:text-slate-200 hover:text-slate-900 dark:hover:text-white font-semibold transition-colors"
          >
            Sign In
          </button>
        </div>
      </div>
    </div>

    <!-- Main Brand Bar (Adaptive: Clean crisp white in light mode, deep luminous obsidian in dark mode) -->
    <div class="bg-white dark:bg-[#05080E] border-b border-slate-200 dark:border-white/[0.07] py-3.5 sm:py-4 px-4 sm:px-6 lg:px-8 transition-colors">
      <div class="max-w-7xl mx-auto flex items-center justify-between">
        <!-- Transparent Brand Logo (Adaptive Light & Dark versions with zero background box) -->
        <router-link to="/" class="flex items-center group focus:outline-none">
          <!-- Dark Mode Logo (luminous chrome and vivid emerald) -->
          <img
            src="/assets/logo.png"
            alt="KKEVO STUDIO MEDIA"
            class="hidden dark:block h-12 sm:h-14 md:h-16 w-auto object-contain transition-transform duration-300 group-hover:scale-[1.02]"
          />
          <!-- Light Mode Logo (sharp ink slate and vivid emerald) -->
          <img
            src="/assets/logo-light-theme.png"
            alt="KKEVO STUDIO MEDIA"
            class="block dark:hidden h-12 sm:h-14 md:h-16 w-auto object-contain transition-transform duration-300 group-hover:scale-[1.02]"
          />
        </router-link>

        <!-- Tagline & Strategic Position -->
        <div class="hidden lg:flex flex-col items-end">
          <div class="flex items-center gap-2 text-xs font-mono font-bold tracking-widest text-slate-800 dark:text-slate-200">
            <span class="text-kkevo-green">FACTS.</span>
            <span class="text-kkevo-blue dark:text-kkevo-blue-glow">PERSPECTIVE.</span>
            <span class="text-slate-900 dark:text-white">IMPACT.</span>
          </div>
          <span class="text-[11px] text-slate-500 dark:text-slate-400 mt-1 font-mono">Independent African-Centred Global Newsroom</span>
        </div>

        <!-- Mobile Hamburger Toggle -->
        <button
          @click="mobileMenuOpen = !mobileMenuOpen"
          class="lg:hidden p-2 rounded text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-white/10 focus:outline-none transition-colors"
          aria-label="Toggle Navigation Menu"
        >
          <svg v-if="!mobileMenuOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </div>

    <!-- Primary Navigation Bar (Desktop) -->
    <nav class="hidden lg:block border-b border-slate-200 dark:border-white/[0.08] bg-white/95 dark:bg-[#090E17]/95 backdrop-blur-md">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <ul class="flex items-center justify-between text-xs uppercase tracking-wider font-semibold py-2.5">
          <li>
            <router-link
              to="/"
              class="text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white py-1 transition-colors"
              active-class="text-kkevo-green dark:text-kkevo-green font-bold"
            >
              Home
            </router-link>
          </li>
          <li>
            <router-link
              to="/category/news"
              class="text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white py-1 transition-colors"
              active-class="text-kkevo-green dark:text-kkevo-green font-bold"
            >
              News
            </router-link>
          </li>
          <li>
            <router-link
              to="/category/geopolitics"
              class="text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white py-1 transition-colors"
              active-class="text-kkevo-green dark:text-kkevo-green font-bold"
            >
              Geopolitics
            </router-link>
          </li>
          <li>
            <router-link
              to="/category/economy"
              class="text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white py-1 transition-colors"
              active-class="text-kkevo-green dark:text-kkevo-green font-bold"
            >
              Economy
            </router-link>
          </li>
          <li>
            <router-link
              to="/category/resources"
              class="text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white py-1 transition-colors"
              active-class="text-kkevo-green dark:text-kkevo-green font-bold"
            >
              Resources & Industry
            </router-link>
          </li>
          <li>
            <router-link
              to="/category/technology"
              class="text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white py-1 transition-colors"
              active-class="text-kkevo-green dark:text-kkevo-green font-bold"
            >
              Technology
            </router-link>
          </li>
          <li>
            <router-link
              to="/category/history"
              class="text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white py-1 transition-colors"
              active-class="text-kkevo-green dark:text-kkevo-green font-bold"
            >
              History
            </router-link>
          </li>
          <li>
            <router-link
              to="/category/security"
              class="text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white py-1 transition-colors"
              active-class="text-kkevo-green dark:text-kkevo-green font-bold"
            >
              Security
            </router-link>
          </li>
          <li class="h-4 w-px bg-slate-200 dark:bg-white/10"></li>
          <li>
            <router-link
              to="/analysis"
              class="text-purple-600 dark:text-purple-400 hover:text-purple-700 dark:hover:text-purple-300 py-1 transition-colors flex items-center gap-1 font-bold"
              active-class="underline font-black"
            >
              <span class="w-1.5 h-1.5 rounded-full bg-purple-500"></span>
              Analysis
            </router-link>
          </li>
          <li>
            <router-link
              to="/video"
              class="text-kkevo-blue dark:text-kkevo-blue-glow hover:text-slate-900 dark:hover:text-white py-1 transition-colors flex items-center gap-1 font-bold"
              active-class="underline font-black"
            >
              <span class="w-1.5 h-1.5 rounded-full bg-kkevo-blue"></span>
              Video
            </router-link>
          </li>
          <li>
            <router-link
              to="/live"
              class="text-red-600 dark:text-red-400 hover:text-red-700 dark:hover:text-red-300 py-1 transition-colors flex items-center gap-1.5 font-bold"
              active-class="underline font-black"
            >
              <span class="w-1.5 h-1.5 rounded-full bg-red-600 animate-ping"></span>
              Live
            </router-link>
          </li>
          <li>
            <router-link
              to="/corrections"
              class="text-slate-500 dark:text-slate-400 hover:text-red-500 py-1 transition-colors text-[11px]"
              active-class="text-red-500 font-bold"
            >
              Corrections
            </router-link>
          </li>
        </ul>
      </div>
    </nav>

    <!-- Mobile Navigation Drawer -->
    <div
      v-if="mobileMenuOpen"
      class="lg:hidden border-b border-slate-200 dark:border-white/10 bg-white dark:bg-[#0B111C] px-6 py-5 space-y-4 shadow-xl"
    >
      <div class="grid grid-cols-2 gap-3 text-sm font-semibold">
        <router-link @click="mobileMenuOpen = false" to="/" class="py-1.5 text-slate-800 dark:text-slate-200 hover:text-kkevo-green">Home</router-link>
        <router-link @click="mobileMenuOpen = false" to="/category/news" class="py-1.5 text-slate-800 dark:text-slate-200 hover:text-kkevo-green">News</router-link>
        <router-link @click="mobileMenuOpen = false" to="/category/geopolitics" class="py-1.5 text-slate-800 dark:text-slate-200 hover:text-kkevo-green">Geopolitics</router-link>
        <router-link @click="mobileMenuOpen = false" to="/category/economy" class="py-1.5 text-slate-800 dark:text-slate-200 hover:text-kkevo-green">Economy</router-link>
        <router-link @click="mobileMenuOpen = false" to="/category/resources" class="py-1.5 text-slate-800 dark:text-slate-200 hover:text-kkevo-green">Resources</router-link>
        <router-link @click="mobileMenuOpen = false" to="/category/technology" class="py-1.5 text-slate-800 dark:text-slate-200 hover:text-kkevo-green">Technology</router-link>
        <router-link @click="mobileMenuOpen = false" to="/category/history" class="py-1.5 text-slate-800 dark:text-slate-200 hover:text-kkevo-green">History</router-link>
        <router-link @click="mobileMenuOpen = false" to="/category/security" class="py-1.5 text-slate-800 dark:text-slate-200 hover:text-kkevo-green">Security</router-link>
        <router-link @click="mobileMenuOpen = false" to="/analysis" class="py-1.5 text-purple-600 dark:text-purple-400 font-bold">Analysis</router-link>
        <router-link @click="mobileMenuOpen = false" to="/video" class="py-1.5 text-kkevo-blue dark:text-kkevo-blue-glow font-bold">Video Cinema</router-link>
        <router-link @click="mobileMenuOpen = false" to="/live" class="py-1.5 text-red-600 dark:text-red-400 font-bold">Live Coverage</router-link>
        <router-link @click="mobileMenuOpen = false" to="/profile" class="py-1.5 text-slate-800 dark:text-slate-200">Saved Articles</router-link>
      </div>
      <div class="pt-3 border-t border-slate-200 dark:border-white/10 flex items-center justify-between text-xs text-slate-500 dark:text-slate-400">
        <router-link @click="mobileMenuOpen = false" to="/corrections" class="hover:text-red-500 font-medium">Corrections Ledger</router-link>
        <router-link @click="mobileMenuOpen = false" to="/editorial" class="text-kkevo-blue dark:text-kkevo-blue-glow font-bold">Newsroom Desk &rarr;</router-link>
      </div>
    </div>

    <!-- Breaking News Ticker Bar -->
    <BreakingBar
      v-if="newsStore.breakingAlert"
      :alert="newsStore.breakingAlert"
      @dismiss="newsStore.dismissBreaking"
    />
  </header>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useNewsStore } from '../../stores/newsStore';
import { useAuthStore } from '../../stores/authStore';
import { useThemeStore } from '../../stores/themeStore';
import BreakingBar from './BreakingBar.vue';

const newsStore = useNewsStore();
const authStore = useAuthStore();
const themeStore = useThemeStore();
const mobileMenuOpen = ref(false);

const currentDateFormatted = computed(() => {
  const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  return new Date().toLocaleDateString('en-US', options);
});
</script>
