<template>
  <div class="min-h-screen py-8">
    <!-- Loading Spinner -->
    <div v-if="loading" class="py-24 text-center space-y-4">
      <div class="w-12 h-12 border-4 border-kkevo-blue border-t-transparent rounded-full animate-spin mx-auto"></div>
      <p class="text-xs uppercase font-mono tracking-widest text-slate-400">Retrieving Verified Article & Sourcing...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error || !article" class="max-w-3xl mx-auto px-4 py-16 text-center space-y-4">
      <h2 class="text-2xl font-bold text-white font-headline">Article Not Found</h2>
      <p class="text-xs text-slate-400">{{ error || 'The requested story could not be retrieved from the archives.' }}</p>
      <router-link to="/" class="inline-block px-4 py-2 bg-kkevo-blue text-white rounded text-xs uppercase tracking-wider font-semibold">
        Return to Newsroom
      </router-link>
    </div>

    <!-- Main Article Layout -->
    <article v-else class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <!-- Breadcrumbs & Category Bar -->
      <div class="flex flex-wrap items-center gap-2 text-xs font-mono text-slate-400 border-b border-kkevo-navy-800 pb-3">
        <router-link to="/" class="hover:text-white transition">Home</router-link>
        <span>&rsaquo;</span>
        <router-link :to="`/category/${article.category?.slug}`" class="text-kkevo-green font-bold hover:underline uppercase">
          {{ article.category?.name }}
        </router-link>
        <template v-if="article.country">
          <span>&rsaquo;</span>
          <router-link :to="`/country/${article.country.slug}`" class="text-slate-300 hover:text-white flex items-center gap-1">
            <span>{{ article.country.flag_emoji }}</span>
            <span>{{ article.country.name }}</span>
          </router-link>
        </template>
        <span>&rsaquo;</span>
        <span class="text-purple-400 uppercase">{{ article.content_type_display }}</span>
      </div>

      <!-- Article Header & Headline -->
      <header class="space-y-4">
        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white leading-tight font-headline text-balance">
          {{ article.title }}
        </h1>

        <p v-if="article.subtitle" class="text-lg sm:text-xl text-slate-300 font-light leading-relaxed">
          {{ article.subtitle }}
        </p>

        <!-- Author Byline & Sharing Tools -->
        <div class="pt-4 border-t border-kkevo-navy-800/80 flex flex-wrap items-center justify-between gap-4 text-xs text-slate-400">
          <!-- Author Info -->
          <div class="flex items-center gap-3">
            <img
              v-if="primaryAuthor?.effective_avatar"
              :src="primaryAuthor.effective_avatar"
              :alt="primaryAuthor.display_name"
              class="w-11 h-11 rounded-full object-cover border border-kkevo-navy-700"
            />
            <div>
              <div class="flex items-center gap-1.5">
                <span class="font-bold text-slate-100">{{ primaryAuthor?.display_name || 'KKEVO Staff' }}</span>
                <span v-if="primaryAuthor?.is_verified" class="text-kkevo-green text-[11px]" title="Verified KKEVO Journalist">✓</span>
              </div>
              <span class="text-[11px] text-slate-400 block">{{ primaryAuthor?.editorial_title }}</span>
              <span class="text-[10px] text-slate-400 font-mono">Published {{ formattedDate }} &bull; {{ article.reading_time_minutes }} min read</span>
            </div>
          </div>

          <!-- Share & Bookmark Actions -->
          <div class="flex items-center gap-2">
            <button
              @click="authStore.toggleBookmark(article.id)"
              :class="['px-3 py-1.5 rounded border text-xs font-semibold flex items-center gap-1.5 transition', authStore.isBookmarked(article.id) ? 'bg-kkevo-green/20 border-kkevo-green text-kkevo-green' : 'bg-kkevo-navy-900 border-kkevo-navy-700 text-slate-300 hover:text-white']"
            >
              <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
              </svg>
              <span>{{ authStore.isBookmarked(article.id) ? 'Saved' : 'Save Story' }}</span>
            </button>

            <button
              @click="shareStory"
              class="px-3 py-1.5 rounded bg-kkevo-navy-900 border border-kkevo-navy-700 text-slate-300 hover:text-white text-xs font-semibold flex items-center gap-1.5 transition"
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
      <div v-if="article.active_correction" class="p-4 bg-red-950/80 border-l-4 border-red-500 rounded-r text-xs space-y-2">
        <div class="flex items-center gap-2 text-red-400 font-bold uppercase tracking-wider font-mono">
          <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
          Editorial Correction Notice &bull; {{ formatCorrectionDate(article.active_correction.corrected_at) }}
        </div>
        <p class="text-slate-200 font-medium">{{ article.active_correction.title }}</p>
        <p class="text-slate-400 leading-relaxed">{{ article.active_correction.reason_for_correction }}</p>
      </div>

      <!-- Hero Media -->
      <figure class="space-y-2">
        <div class="aspect-[16/10] bg-black rounded-lg overflow-hidden border border-kkevo-navy-800">
          <img
            :src="article.effective_hero_image || 'https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=1200&q=80'"
            :alt="article.title"
            class="w-full h-full object-cover"
          />
        </div>
        <figcaption class="flex flex-col sm:flex-row sm:items-center justify-between text-xs text-slate-400 gap-1 px-1">
          <span>{{ article.hero_caption }}</span>
          <span v-if="article.hero_credit" class="font-mono text-slate-400">Photo: {{ article.hero_credit }}</span>
        </figcaption>
      </figure>

      <!-- Credibility & Scrutiny Bar -->
      <div v-if="article.claims?.length" class="bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg p-4 space-y-3">
        <div class="flex items-center justify-between border-b border-kkevo-navy-800 pb-2">
          <span class="text-xs uppercase font-mono font-bold tracking-widest text-slate-300">
            KKEVO Credibility & Fact Audit
          </span>
          <span class="text-[11px] font-mono text-slate-400">{{ article.claims.length }} Scrutinized Claims</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div
            v-for="claim in article.claims"
            :key="claim.id"
            class="p-3 bg-kkevo-navy-950 rounded border border-kkevo-navy-800 space-y-1.5"
          >
            <div class="flex items-center justify-between">
              <VerificationBadge :status="claim.verification_status" :label="claim.status_display" />
            </div>
            <p class="text-xs text-slate-200 font-medium leading-snug">{{ claim.claim_text }}</p>
            <p v-if="claim.verification_notes" class="text-[11px] text-slate-400 leading-tight">{{ claim.verification_notes }}</p>
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
          <blockquote v-if="block.type === 'pull_quote'" class="p-6 bg-blue-950/20 border-l-4 border-kkevo-blue rounded-r my-6 space-y-2">
            <p class="text-lg sm:text-xl font-bold text-white font-headline italic leading-relaxed">
              &ldquo;{{ block.quote }}&rdquo;
            </p>
            <cite v-if="block.author" class="text-xs font-mono text-kkevo-blue-glow block not-italic">
              &mdash; {{ block.author }}
            </cite>
          </blockquote>

          <!-- Key Facts Box -->
          <div v-else-if="block.type === 'key_facts'" class="p-5 bg-kkevo-navy-900 border border-kkevo-green/40 rounded-lg space-y-2 my-6">
            <h4 class="text-xs uppercase font-bold font-mono tracking-widest text-kkevo-green flex items-center gap-1.5">
              <span class="w-1.5 h-1.5 rounded-full bg-kkevo-green"></span>
              {{ block.title || 'Key Facts' }}
            </h4>
            <ul class="space-y-1.5 text-xs text-slate-300 list-disc list-inside">
              <li v-for="(fact, fIdx) in block.items" :key="fIdx">{{ fact }}</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Article Rich Body -->
      <div class="prose prose-invert max-w-none text-slate-200 text-base sm:text-lg leading-relaxed space-y-6 pt-2 font-sans">
        <div v-html="renderedBody"></div>
      </div>

      <!-- Citations & Footnotes Drawer -->
      <section v-if="article.citations?.length" class="mt-12 bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg p-6 space-y-4">
        <div class="flex items-center justify-between border-b border-kkevo-navy-800 pb-3">
          <h3 class="text-xs uppercase font-bold tracking-widest text-white font-mono flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-kkevo-blue"></span>
            Primary Source Citations & References
          </h3>
          <span class="text-xs text-slate-400 font-mono">{{ article.citations.length }} Sources Documented</span>
        </div>

        <ol class="space-y-3 text-xs">
          <li
            v-for="cite in article.citations"
            :key="cite.id"
            class="flex items-start gap-3 p-3 bg-kkevo-navy-950 rounded border border-kkevo-navy-800/80"
          >
            <span class="px-1.5 py-0.5 rounded bg-kkevo-blue/20 text-kkevo-blue-glow font-mono font-bold text-[11px] shrink-0">
              [{{ cite.citation_number }}]
            </span>
            <div class="space-y-1 min-w-0">
              <div class="font-bold text-white flex items-center gap-2">
                <span>{{ cite.source?.title }}</span>
                <span v-if="cite.source?.publisher" class="text-slate-400 font-normal">({{ cite.source.publisher }})</span>
              </div>
              <p v-if="cite.quote_excerpt" class="text-slate-300 italic">
                &ldquo;{{ cite.quote_excerpt }}&rdquo;
              </p>
              <div class="flex items-center gap-3 text-[11px] text-slate-400 font-mono">
                <span v-if="cite.public_label">{{ cite.public_label }}</span>
                <a
                  v-if="cite.source?.url"
                  :href="cite.source.url"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="text-kkevo-blue-glow hover:underline flex items-center gap-1"
                >
                  Verify Source &nearr;
                </a>
              </div>
            </div>
          </li>
        </ol>
      </section>

      <!-- Author Dossier Box -->
      <div v-if="primaryAuthor" class="mt-12 p-6 bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg flex flex-col sm:flex-row items-start gap-5">
        <img
          v-if="primaryAuthor.effective_avatar"
          :src="primaryAuthor.effective_avatar"
          :alt="primaryAuthor.display_name"
          class="w-16 h-16 rounded-full object-cover border-2 border-kkevo-navy-700 shrink-0"
        />
        <div class="space-y-2">
          <div class="flex items-center gap-2">
            <h4 class="text-base font-bold text-white font-headline">{{ primaryAuthor.display_name }}</h4>
            <span class="text-xs text-kkevo-green font-mono">({{ primaryAuthor.editorial_title }})</span>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed">{{ primaryAuthor.bio }}</p>
          <div class="text-[11px] text-slate-400 font-mono flex items-center gap-4 pt-1">
            <span v-if="primaryAuthor.location">📍 {{ primaryAuthor.location }}</span>
            <span v-if="primaryAuthor.twitter_handle">{{ primaryAuthor.twitter_handle }}</span>
          </div>
        </div>
      </div>
    </article>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import { api } from '../services/api';
import { useAuthStore } from '../stores/authStore';
import VerificationBadge from '../components/common/VerificationBadge.vue';

const route = useRoute();
const authStore = useAuthStore();

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
  // Basic markdown conversion for paragraphs, headings, bold
  let html = article.value.body
    .replace(/^### (.*$)/gim, '<h3 class="text-xl font-bold text-white font-headline mt-8 mb-4">$1</h3>')
    .replace(/^## (.*$)/gim, '<h2 class="text-2xl font-extrabold text-white font-headline mt-10 mb-4 pb-2 border-b border-kkevo-navy-800">$1</h2>')
    .replace(/\*\*(.*?)\*\*/gim, '<strong class="text-white font-semibold">$1</strong>')
    .replace(/\n\n/g, '</p><p class="mb-5 leading-relaxed">')
    .replace(/```([\s\S]*?)```/gim, '<pre class="bg-kkevo-navy-950 p-4 rounded font-mono text-xs text-kkevo-green border border-kkevo-navy-800 my-4 overflow-x-auto"><code>$1</code></pre>');

  return `<p class="editorial-dropcap mb-5 leading-relaxed">${html}</p>`;
});

async function loadArticle() {
  loading.value = true;
  error.value = null;
  try {
    const data = await api.getArticle(route.params.slug);
    article.value = data;
    // Update document title for SEO
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
    setTimeout(() => { copied.value = false; }, 2000);
  }
}

function formatCorrectionDate(d) {
  if (!d) return '';
  return new Date(d).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
}

onMounted(loadArticle);
watch(() => route.params.slug, loadArticle);
</script>
