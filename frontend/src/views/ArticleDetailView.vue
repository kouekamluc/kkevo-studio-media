<template>
  <div class="min-h-screen py-8 transition-colors">
    <!-- Loading Spinner -->
    <div v-if="loading" class="py-24 text-center space-y-4">
      <div class="w-12 h-12 border-4 border-kkevo-blue border-t-transparent rounded-full animate-spin mx-auto"></div>
      <p class="text-xs uppercase font-mono tracking-widest text-slate-500 dark:text-slate-400">Retrieving Verified Article & Sourcing...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error || !article" class="max-w-3xl mx-auto px-4 py-16 text-center space-y-4">
      <h2 class="text-2xl font-bold text-slate-900 dark:text-white font-headline">Article Not Found</h2>
      <p class="text-xs text-slate-500">{{ error || 'The requested story could not be retrieved from the archives.' }}</p>
      <router-link to="/" class="inline-block px-4 py-2 bg-kkevo-blue text-white rounded text-xs uppercase tracking-wider font-semibold">
        Return to Newsroom
      </router-link>
    </div>

    <!-- Main Article Layout -->
    <article v-else class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <!-- Breadcrumbs & Category Bar -->
      <div class="flex flex-wrap items-center gap-2 text-xs font-mono text-slate-500 dark:text-slate-400 border-b border-slate-200 dark:border-kkevo-navy-800 pb-3">
        <router-link to="/" class="hover:text-slate-900 dark:hover:text-white transition">Home</router-link>
        <span>&rsaquo;</span>
        <router-link :to="`/category/${article.category?.slug}`" class="text-kkevo-green font-bold hover:underline uppercase">
          {{ article.category?.name }}
        </router-link>
        <template v-if="article.country">
          <span>&rsaquo;</span>
          <router-link :to="`/country/${article.country.slug}`" class="text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white flex items-center gap-1 font-medium">
            <span>{{ article.country.flag_emoji }}</span>
            <span>{{ article.country.name }}</span>
          </router-link>
        </template>
        <span>&rsaquo;</span>
        <span class="text-purple-600 dark:text-purple-400 uppercase font-bold">{{ article.content_type_display }}</span>
      </div>

      <!-- Article Header & Headline -->
      <header class="space-y-4">
        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-slate-900 dark:text-white leading-[1.15] font-headline text-balance">
          {{ article.title }}
        </h1>

        <p v-if="article.subtitle" class="text-lg sm:text-xl text-slate-600 dark:text-slate-300 font-light leading-relaxed">
          {{ article.subtitle }}
        </p>

        <!-- Author Byline & Sharing Tools -->
        <div class="pt-4 border-t border-slate-200 dark:border-kkevo-navy-800/80 flex flex-wrap items-center justify-between gap-4 text-xs text-slate-500 dark:text-slate-400">
          <!-- Author Info -->
          <div class="flex items-center gap-3">
            <img
              v-if="primaryAuthor?.effective_avatar"
              :src="primaryAuthor.effective_avatar"
              :alt="primaryAuthor.display_name"
              class="w-11 h-11 rounded-full object-cover border border-slate-300 dark:border-kkevo-navy-700 shadow-sm"
            />
            <div>
              <div class="flex items-center gap-1.5">
                <span class="font-bold text-slate-900 dark:text-slate-100 text-sm">{{ primaryAuthor?.display_name || 'KKEVO Staff' }}</span>
                <span v-if="primaryAuthor?.is_verified" class="text-kkevo-green text-[11px]" title="Verified KKEVO Journalist">✓</span>
              </div>
              <span class="text-[11px] text-slate-500 dark:text-slate-400 block">{{ primaryAuthor?.editorial_title }}</span>
              <span class="text-[10px] text-slate-500 dark:text-slate-400 font-mono">Published {{ formattedDate }} &bull; {{ article.reading_time_minutes }} min read</span>
            </div>
          </div>

          <!-- Share & Bookmark Actions -->
          <div class="flex items-center gap-2">
            <button
              @click="authStore.toggleBookmark(article.id)"
              :class="[
                'px-3.5 py-1.5 rounded-lg border text-xs font-semibold flex items-center gap-1.5 transition',
                authStore.isBookmarked(article.id)
                  ? 'bg-kkevo-green/20 border-kkevo-green text-kkevo-green'
                  : 'bg-slate-100 dark:bg-kkevo-navy-900 border-slate-300 dark:border-kkevo-navy-700 text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white'
              ]"
            >
              <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
              </svg>
              <span>{{ authStore.isBookmarked(article.id) ? 'Saved' : 'Save Story' }}</span>
            </button>

            <button
              @click="shareStory"
              class="px-3.5 py-1.5 rounded-lg bg-slate-100 dark:bg-kkevo-navy-900 border border-slate-300 dark:border-kkevo-navy-700 text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white text-xs font-semibold flex items-center gap-1.5 transition shadow-sm"
            >
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z" />
              </svg>
              <span>{{ copied ? 'Link Copied!' : 'Share' }}</span>
            </button>
          </div>
        </div>
      </header>

      <!-- Active Editorial Correction Banner -->
      <div v-if="article.active_correction || article.status === 'CORRECTED'" class="p-4 sm:p-5 bg-rose-50/90 dark:bg-[#1A0A0E] border-y border-r border-rose-200 dark:border-red-900/50 border-l-4 border-l-red-600 dark:border-l-red-500 rounded-r-xl text-xs space-y-2 shadow-sm transition-colors">
        <div class="flex items-center justify-between gap-2">
          <div class="flex items-center gap-2 text-red-700 dark:text-red-400 font-bold uppercase tracking-wider font-mono text-xs">
            <span class="w-2 h-2 rounded-full bg-red-600 dark:bg-red-500 animate-ping"></span>
            Institutional Correction Notice
          </div>
          <span v-if="article.active_correction?.corrected_at" class="text-[11px] font-mono text-slate-500 dark:text-slate-400">
            Updated {{ formatCorrectionDate(article.active_correction.corrected_at) }}
          </span>
        </div>
        <p class="text-sm font-bold text-slate-900 dark:text-white">
          {{ article.active_correction?.title || 'This article has been updated to correct factual context in accordance with KKEVO verification standards.' }}
        </p>
        <p class="text-slate-700 dark:text-slate-300 leading-relaxed">
          {{ article.active_correction?.reason_for_correction || 'KKEVO STUDIO MEDIA maintains a publicly accountable transparency ledger. All edits affecting factual assertions are timestamped and preserved.' }}
        </p>
        <div class="pt-1">
          <router-link to="/corrections" class="text-red-700 dark:text-red-400 hover:underline font-mono font-bold text-[11px] inline-flex items-center gap-1">
            <span>Review Full Institutional Corrections Ledger</span> &rarr;
          </router-link>
        </div>
      </div>

      <!-- Hero Media -->
      <figure class="space-y-2">
        <div class="aspect-[16/10] bg-slate-900 rounded-xl overflow-hidden border border-slate-200 dark:border-kkevo-navy-800 shadow-md">
          <img
            :src="article.effective_hero_image || 'https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=1200&q=80'"
            :alt="article.title"
            class="w-full h-full object-cover"
          />
        </div>
        <figcaption class="flex flex-col sm:flex-row sm:items-center justify-between text-xs text-slate-500 dark:text-slate-400 gap-1 px-1">
          <span>{{ article.hero_caption }}</span>
          <span v-if="article.hero_credit" class="font-mono text-slate-500">Photo: {{ article.hero_credit }}</span>
        </figcaption>
      </figure>

      <!-- Credibility & Scrutiny Bar -->
      <div v-if="article.claims?.length" class="bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/90 dark:to-[#080D17] border border-slate-200 dark:border-white/[0.08] rounded-xl p-5 sm:p-6 space-y-4 shadow-sm dark:shadow-[0_4px_20px_-4px_rgba(0,0,0,0.6)]">
        <div class="flex items-center justify-between border-b border-slate-200 dark:border-white/[0.08] pb-3">
          <span class="text-xs uppercase font-mono font-bold tracking-widest text-slate-800 dark:text-white">
            KKEVO Credibility & Fact Audit
          </span>
          <span class="text-[11px] font-mono text-slate-500 dark:text-slate-400 font-bold">{{ article.claims.length }} Scrutinized Claims</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div
            v-for="claim in article.claims"
            :key="claim.id"
            class="p-3.5 bg-slate-50 dark:bg-[#060910] rounded-lg border border-slate-200 dark:border-white/[0.06] space-y-1.5"
          >
            <div class="flex items-center justify-between">
              <VerificationBadge :status="claim.verification_status" :label="claim.status_display" />
            </div>
            <p class="text-xs text-slate-900 dark:text-white font-semibold leading-snug">{{ claim.claim_text }}</p>
            <p v-if="claim.verification_notes" class="text-[11px] text-slate-600 dark:text-slate-300 leading-tight">{{ claim.verification_notes }}</p>
          </div>
        </div>
      </div>

      <!-- Structured Interactive Blocks (Pull Quotes, Key Facts) -->
      <div v-if="article.structured_blocks?.length" class="space-y-4">
        <div
          v-for="(block, idx) in article.structured_blocks"
          :key="idx"
        >
          <!-- Pull Quote Block -->
          <blockquote v-if="block.type === 'pull_quote'" class="p-6 bg-blue-50 dark:bg-blue-950/20 border-l-4 border-kkevo-blue dark:border-kkevo-blue-glow rounded-r-xl my-6 space-y-2">
            <p class="text-lg sm:text-xl font-bold text-slate-900 dark:text-white font-headline italic leading-relaxed">
              &ldquo;{{ block.quote }}&rdquo;
            </p>
            <cite v-if="block.author" class="text-xs font-mono text-kkevo-blue dark:text-kkevo-blue-glow block not-italic font-bold">
              &mdash; {{ block.author }}
            </cite>
          </blockquote>

          <!-- Key Facts Box -->
          <div v-else-if="block.type === 'key_facts'" class="p-5 bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/90 dark:to-[#080D17] border border-emerald-300 dark:border-kkevo-green/40 rounded-xl space-y-2.5 my-6 shadow-sm">
            <h4 class="text-xs uppercase font-bold font-mono tracking-widest text-kkevo-green flex items-center gap-1.5">
              <span class="w-1.5 h-1.5 rounded-full bg-kkevo-green"></span>
              {{ block.title || 'Key Facts' }}
            </h4>
            <ul class="space-y-1.5 text-xs text-slate-700 dark:text-slate-200 list-disc list-inside">
              <li v-for="(fact, fIdx) in block.items" :key="fIdx">{{ fact }}</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Article Rich Body -->
      <div class="prose prose-slate dark:prose-invert max-w-none text-slate-800 dark:text-slate-200 text-base sm:text-lg leading-relaxed space-y-6 pt-2 font-sans">
        <div v-html="renderedBody"></div>
      </div>

      <!-- Citations & Footnotes Drawer -->
      <section v-if="article.citations?.length" class="mt-12 bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/90 dark:to-[#080D17] border border-slate-200 dark:border-white/[0.08] rounded-xl p-6 space-y-4 shadow-sm">
        <div class="flex items-center justify-between border-b border-slate-200 dark:border-white/[0.08] pb-3">
          <h3 class="text-xs uppercase font-bold tracking-widest text-slate-900 dark:text-white font-mono flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-kkevo-blue"></span>
            Primary Source Citations & References
          </h3>
          <span class="text-xs text-slate-500 dark:text-slate-400 font-mono font-bold">{{ article.citations.length }} Sources Documented</span>
        </div>

        <ol class="space-y-3 text-xs">
          <li
            v-for="cite in article.citations"
            :key="cite.id"
            class="flex items-start gap-3 p-3.5 bg-slate-50 dark:bg-[#060910] rounded-lg border border-slate-200 dark:border-white/[0.06]"
          >
            <span class="px-1.5 py-0.5 rounded bg-blue-100 dark:bg-kkevo-blue/20 text-kkevo-blue dark:text-kkevo-blue-glow font-mono font-bold text-[11px] shrink-0">
              [{{ cite.citation_number }}]
            </span>
            <div class="space-y-1 min-w-0">
              <div class="font-bold text-slate-900 dark:text-white flex items-center gap-2">
                <span>{{ cite.source?.title }}</span>
                <span v-if="cite.source?.publisher" class="text-slate-500 dark:text-slate-400 font-normal">({{ cite.source.publisher }})</span>
              </div>
              <p v-if="cite.quote_excerpt" class="text-slate-700 dark:text-slate-300 italic">
                &ldquo;{{ cite.quote_excerpt }}&rdquo;
              </p>
              <div class="flex items-center gap-3 text-[11px] text-slate-500 dark:text-slate-400 font-mono">
                <span v-if="cite.public_label">{{ cite.public_label }}</span>
                <a
                  v-if="cite.source?.url"
                  :href="cite.source.url"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="text-kkevo-blue dark:text-kkevo-blue-glow hover:underline flex items-center gap-1 font-bold"
                >
                  Verify Source &nearr;
                </a>
              </div>
            </div>
          </li>
        </ol>
      </section>

      <!-- Author Dossier Box -->
      <div v-if="primaryAuthor" class="mt-12 p-6 bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/90 dark:to-[#080D17] border border-slate-200 dark:border-white/[0.08] rounded-xl flex flex-col sm:flex-row items-start gap-5 shadow-sm">
        <img
          v-if="primaryAuthor.effective_avatar"
          :src="primaryAuthor.effective_avatar"
          :alt="primaryAuthor.display_name"
          class="w-16 h-16 rounded-full object-cover border-2 border-kkevo-green/40 shadow-sm shrink-0"
        />
        <div class="space-y-2">
          <div class="flex items-center gap-2">
            <h4 class="text-base font-bold text-slate-900 dark:text-white font-headline">{{ primaryAuthor.display_name }}</h4>
            <span class="text-xs text-kkevo-green font-mono font-bold">({{ primaryAuthor.editorial_title }})</span>
          </div>
          <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">{{ primaryAuthor.bio }}</p>
          <div class="text-[11px] text-slate-500 dark:text-slate-400 font-mono flex items-center gap-4 pt-1">
            <span v-if="primaryAuthor.location">📍 {{ primaryAuthor.location }}</span>
            <span v-if="primaryAuthor.twitter_handle">{{ primaryAuthor.twitter_handle }}</span>
          </div>
        </div>
      </div>

      <!-- Civil Discussion & Community Comment Section -->
      <CommentSection :article-id="article.id" />
    </article>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import { api } from '../services/api';
import { useAuthStore } from '../stores/authStore';
import { useAlertStore } from '../stores/alertStore';
import VerificationBadge from '../components/common/VerificationBadge.vue';
import CommentSection from '../components/editorial/CommentSection.vue';

const route = useRoute();
const authStore = useAuthStore();
const alertStore = useAlertStore();

const article = ref(null);
const loading = ref(true);
const error = ref(null);
const copied = ref(false);

const primaryAuthor = computed(() => article.value?.authors?.[0] || null);

const formattedDate = computed(() => {
  if (!article.value?.published_at) return '';
  return new Date(article.value.published_at).toLocaleDateString('en-US', {
    month: 'long',
    day: 'numeric',
    year: 'numeric'
  });
});

const renderedBody = computed(() => {
  if (!article.value?.body) return '';
  let html = article.value.body
    .replace(/^### (.*$)/gim, '<h3 class="text-xl font-bold text-slate-900 dark:text-white font-headline mt-8 mb-4">$1</h3>')
    .replace(/^## (.*$)/gim, '<h2 class="text-2xl font-extrabold text-slate-900 dark:text-white font-headline mt-10 mb-4 pb-2 border-b border-slate-200 dark:border-white/10">$1</h2>')
    .replace(/\*\*(.*?)\*\*/gim, '<strong class="text-slate-900 dark:text-white font-semibold">$1</strong>')
    .replace(/\n\n/g, '</p><p class="mb-5 leading-relaxed">')
    .replace(/```([\s\S]*?)```/gim, '<pre class="bg-slate-900 dark:bg-[#060910] text-emerald-400 dark:text-kkevo-green p-4 rounded-xl font-mono text-xs border border-slate-800 dark:border-white/10 my-4 overflow-x-auto"><code>$1</code></pre>');

  return `<p class="editorial-dropcap mb-5 leading-relaxed">${html}</p>`;
});

async function loadArticle() {
  loading.value = true;
  error.value = null;
  try {
    const data = await api.getArticle(route.params.slug);
    article.value = data;
    document.title = `${data.title} | KKEVO STUDIO MEDIA`;
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
}

function shareStory() {
  if (navigator.clipboard) {
    navigator.clipboard.writeText(window.location.href);
    copied.value = true;
    alertStore.info('Story Link Copied', 'Article link copied to clipboard.');
    setTimeout(() => { copied.value = false; }, 2000);
  } else {
    alertStore.info('Story URL', window.location.href);
  }
}

function formatCorrectionDate(d) {
  if (!d) return '';
  return new Date(d).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
}

onMounted(loadArticle);
watch(() => route.params.slug, loadArticle);
</script>
