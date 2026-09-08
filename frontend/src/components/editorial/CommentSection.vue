<template>
  <section class="mt-12 bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/90 dark:to-[#080D17] border border-slate-200 dark:border-white/[0.08] rounded-xl p-6 sm:p-8 space-y-6 shadow-sm dark:shadow-[0_4px_20px_-4px_rgba(0,0,0,0.6)] transition-colors">
    <div class="flex items-center justify-between border-b border-slate-200 dark:border-white/[0.08] pb-3">
      <div>
        <span class="text-xs font-mono font-bold tracking-widest text-kkevo-green uppercase block">
          Reader Perspectives & Scrutiny
        </span>
        <h3 class="text-lg font-bold text-slate-900 dark:text-white font-headline mt-0.5">
          Civil Discussion ({{ comments.length }})
        </h3>
      </div>
      <span class="text-[11px] text-slate-500 dark:text-slate-400 font-mono">Pre-Moderated Newsroom Forum</span>
    </div>

    <!-- Submit Comment Form -->
    <div v-if="authStore.isAuthenticated" class="space-y-3">
      <label class="block text-xs uppercase font-mono text-slate-700 dark:text-slate-300 font-semibold">
        Leave an evidence-led perspective as <strong class="text-slate-900 dark:text-white">{{ authStore.displayName }}</strong>:
      </label>
      <textarea
        v-model="commentText"
        rows="3"
        placeholder="Add empirical context, historical clarification, or constructive scrutiny..."
        class="w-full bg-slate-50 dark:bg-[#060910] border border-slate-200 dark:border-white/10 rounded-lg p-3 text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:border-kkevo-blue text-sm leading-relaxed"
      ></textarea>

      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 pt-1">
        <span class="text-[11px] text-slate-500 dark:text-slate-400">Comments are audited against KKEVO community guidelines.</span>
        <button
          @click="submitComment"
          :disabled="submitting || !commentText.trim()"
          class="px-4 py-2 bg-kkevo-blue text-white rounded-lg text-xs font-bold uppercase tracking-wider hover:bg-kkevo-blue-dark transition disabled:opacity-50 shadow-sm"
        >
          <span v-if="submitting">Submitting...</span>
          <span v-else>Post Comment &rarr;</span>
        </button>
      </div>

      <div v-if="feedbackMsg" class="p-3 bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-300 dark:border-kkevo-green/40 rounded-lg text-xs text-emerald-800 dark:text-kkevo-green font-medium">
        {{ feedbackMsg }}
      </div>
    </div>

    <div v-else class="p-4 bg-slate-50 dark:bg-[#060910] border border-slate-200 dark:border-white/10 rounded-lg text-xs text-slate-600 dark:text-slate-300 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
      <span>Join the discussion and contribute verified perspectives.</span>
      <button
        @click="authStore.toggleAuthModal(true)"
        class="px-3.5 py-1.5 bg-kkevo-blue text-white rounded-lg font-semibold hover:bg-kkevo-blue-dark transition shadow-sm"
      >
        Sign In to Comment
      </button>
    </div>

    <!-- Comments List -->
    <div class="space-y-4 pt-2">
      <div v-if="!comments.length" class="text-center py-6 text-xs text-slate-500 dark:text-slate-400 font-mono">
        No comments approved on this story yet. Be the first to provide verified perspective.
      </div>

      <div
        v-for="c in comments"
        :key="c.id"
        class="p-4 bg-slate-50 dark:bg-[#060910] rounded-xl border border-slate-200 dark:border-white/10 space-y-2"
      >
        <div class="flex items-center justify-between text-xs">
          <div class="flex items-center gap-2">
            <span class="font-bold text-slate-900 dark:text-slate-100">{{ c.user_name || 'Registered Reader' }}</span>
            <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-50 dark:bg-emerald-950/80 text-emerald-800 dark:text-kkevo-green font-mono border border-emerald-200 dark:border-emerald-500/30 font-bold">
              Verified Reader
            </span>
          </div>
          <span class="text-slate-500 dark:text-slate-400 font-mono text-[11px]">{{ formatDate(c.created_at) }}</span>
        </div>
        <p class="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed">{{ c.content }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useAuthStore } from '../../stores/authStore';

const props = defineProps({
  articleId: {
    type: String,
    required: true,
  }
});

const authStore = useAuthStore();
const comments = ref([]);
const commentText = ref('');
const submitting = ref(false);
const feedbackMsg = ref('');

function formatDate(d) {
  if (!d) return '';
  return new Date(d).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
}

async function loadComments() {
  if (!props.articleId) return;
  try {
    const res = await fetch(`/api/v1/community/comments/?article=${props.articleId}`);
    if (res.ok) {
      const data = await res.json();
      comments.value = data.results || data;
    }
  } catch (err) {
    console.error(err);
  }
}

async function submitComment() {
  if (!commentText.value.trim()) return;
  submitting.value = true;
  feedbackMsg.value = '';
  try {
    const res = await fetch('/api/v1/community/comments/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        article: props.articleId,
        content: commentText.value.trim(),
      })
    });
    if (res.ok) {
      feedbackMsg.value = 'Perspective submitted successfully. Thank you for maintaining civil discourse.';
      commentText.value = '';
      loadComments();
    } else {
      feedbackMsg.value = 'Perspective submitted for editorial moderation queue.';
    }
  } catch (err) {
    feedbackMsg.value = 'Failed to submit comment.';
  } finally {
    submitting.value = false;
  }
}

onMounted(loadComments);
watch(() => props.articleId, loadComments);
</script>
