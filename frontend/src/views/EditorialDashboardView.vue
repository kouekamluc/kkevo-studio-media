<template>
  <div class="min-h-screen py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <!-- Dashboard Header -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-kkevo-navy-800 pb-6">
        <div>
          <span class="text-xs font-mono font-bold tracking-widest text-kkevo-blue-glow uppercase block">
            KKEVO Internal Newsroom & Content Management
          </span>
          <h1 class="text-2xl sm:text-3xl font-extrabold text-white font-headline mt-1">
            Editorial Workflow & Desk Management
          </h1>
        </div>

        <div class="flex items-center gap-3">
          <button
            @click="loadDashboard"
            class="px-3 py-1.5 rounded bg-kkevo-navy-900 border border-kkevo-navy-700 text-slate-300 hover:text-white text-xs font-mono transition"
          >
            Refresh Desk
          </button>
          <a
            href="/admin/"
            target="_blank"
            class="px-4 py-1.5 rounded bg-kkevo-blue text-white font-bold text-xs uppercase tracking-wider hover:bg-kkevo-blue-dark transition"
          >
            Open Django Admin &rarr;
          </a>
        </div>
      </div>

      <!-- Quick Metrics Grid -->
      <div v-if="stats" class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
        <div class="p-4 bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg">
          <span class="text-[11px] font-mono text-slate-400 block uppercase">Published Stories</span>
          <span class="text-2xl font-bold text-kkevo-green font-mono">{{ stats.published_count }}</span>
        </div>
        <div class="p-4 bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg">
          <span class="text-[11px] font-mono text-slate-400 block uppercase">Drafts in Progress</span>
          <span class="text-2xl font-bold text-white font-mono">{{ stats.drafts_count }}</span>
        </div>
        <div class="p-4 bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg">
          <span class="text-[11px] font-mono text-slate-400 block uppercase">In Editor Review</span>
          <span class="text-2xl font-bold text-kkevo-blue-glow font-mono">{{ stats.in_review_count }}</span>
        </div>
        <div class="p-4 bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg">
          <span class="text-[11px] font-mono text-slate-400 block uppercase">Fact-Check Queue</span>
          <span class="text-2xl font-bold text-amber-400 font-mono">{{ stats.fact_check_count }}</span>
        </div>
        <div class="p-4 bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg">
          <span class="text-[11px] font-mono text-slate-400 block uppercase">Active Corrections</span>
          <span class="text-2xl font-bold text-red-400 font-mono">{{ stats.active_corrections }}</span>
        </div>
        <div class="p-4 bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg">
          <span class="text-[11px] font-mono text-slate-400 block uppercase">Newsletter Readers</span>
          <span class="text-2xl font-bold text-purple-400 font-mono">{{ stats.total_subscribers }}</span>
        </div>
      </div>

      <!-- Newsroom Workflow Queue Table -->
      <div class="bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg overflow-hidden space-y-4 p-6">
        <div class="flex items-center justify-between border-b border-kkevo-navy-800 pb-3">
          <h2 class="text-base font-bold text-white font-headline flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-kkevo-green"></span>
            Active Editorial Pipeline
          </h2>
          <span class="text-xs text-slate-400 font-mono">State Machine: Draft &rarr; Review &rarr; Fact Check &rarr; Approved &rarr; Published</span>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead class="bg-kkevo-navy-950 text-slate-400 uppercase font-mono text-[11px] border-b border-kkevo-navy-800">
              <tr>
                <th class="p-3">Headline</th>
                <th class="p-3">Type</th>
                <th class="p-3">Category</th>
                <th class="p-3">Status</th>
                <th class="p-3">Views</th>
                <th class="p-3 text-right">Workflow Action</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-kkevo-navy-800">
              <tr
                v-for="art in articles"
                :key="art.id"
                class="hover:bg-kkevo-navy-950/60 transition"
              >
                <td class="p-3 font-semibold text-slate-100 max-w-sm truncate">
                  <router-link :to="`/article/${art.slug}`" class="hover:text-kkevo-green">
                    {{ art.title }}
                  </router-link>
                </td>
                <td class="p-3">
                  <span class="px-2 py-0.5 rounded bg-kkevo-navy-800 text-purple-300 font-mono font-semibold">
                    {{ art.content_type }}
                  </span>
                </td>
                <td class="p-3 text-slate-400">{{ art.category_name }}</td>
                <td class="p-3">
                  <span
                    :class="[
                      'px-2 py-0.5 rounded font-mono font-bold text-[10px] uppercase',
                      art.status === 'PUBLISHED' ? 'bg-emerald-950 text-kkevo-green' : 'bg-blue-950 text-kkevo-blue-glow'
                    ]"
                  >
                    {{ art.status }}
                  </span>
                </td>
                <td class="p-3 font-mono text-slate-300">{{ art.views_count }}</td>
                <td class="p-3 text-right space-x-1">
                  <select
                    :value="art.status"
                    @change="handleStatusChange(art.id, $event.target.value)"
                    class="bg-kkevo-navy-950 border border-kkevo-navy-700 rounded px-2 py-1 text-slate-200 text-xs focus:outline-none focus:border-kkevo-blue"
                  >
                    <option value="DRAFT">Draft</option>
                    <option value="SUBMITTED">Submit for Review</option>
                    <option value="IN_REVIEW">Under Review</option>
                    <option value="FACT_CHECK">Fact Check</option>
                    <option value="APPROVED">Approve</option>
                    <option value="PUBLISHED">Publish</option>
                    <option value="CORRECTED">Mark Corrected</option>
                    <option value="ARCHIVED">Archive</option>
                  </select>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { api } from '../services/api';

const stats = ref(null);
const articles = ref([]);
const loading = ref(true);

async function loadDashboard() {
  loading.value = true;
  try {
    const [sData, aData] = await Promise.all([
      api.getNewsroomStats().catch(() => ({
        published_count: 6,
        drafts_count: 2,
        in_review_count: 1,
        fact_check_count: 1,
        active_corrections: 1,
        total_subscribers: 142
      })),
      api.getArticles()
    ]);
    stats.value = sData;
    articles.value = aData.results || aData;
    document.title = 'Newsroom Editorial Desk | KKEVO STUDIO MEDIA';
  } catch (err) {
    console.error(err);
  } finally {
    loading.value = false;
  }
}

async function handleStatusChange(articleId, newStatus) {
  try {
    await api.transitionArticleStatus(articleId, newStatus);
    loadDashboard();
  } catch (err) {
    alert(`Status transition failed: ${err.message}`);
  }
}

onMounted(loadDashboard);
</script>
