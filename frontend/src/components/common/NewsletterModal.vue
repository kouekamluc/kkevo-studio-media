<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm">
    <div class="bg-kkevo-navy-900 border border-kkevo-navy-700 rounded-lg max-w-lg w-full p-6 sm:p-8 shadow-2xl relative space-y-5">
      <button @click="$emit('close')" class="absolute top-4 right-4 text-slate-400 hover:text-white">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <div class="space-y-2">
        <span class="inline-flex items-center gap-1.5 text-xs font-mono font-bold tracking-widest text-kkevo-green uppercase">
          <span class="w-2 h-2 rounded-full bg-kkevo-green"></span>
          KKEVO Intelligence Briefing
        </span>
        <h3 class="text-xl font-bold text-white font-headline">
          Independent African Geopolitical & Economic Intelligence
        </h3>
        <p class="text-xs text-slate-400 leading-relaxed">
          Rigorous daily and weekly briefings delivered directly to senior analysts, industrial leaders, diplomats, and informed readers globally.
        </p>
      </div>

      <form @submit.prevent="handleSubmit" class="space-y-4">
        <div>
          <label class="block text-xs uppercase font-mono text-slate-400 mb-1">Corporate or Personal Email</label>
          <input
            v-model="email"
            type="email"
            required
            placeholder="analyst@institution.org"
            class="w-full bg-kkevo-navy-950 border border-kkevo-navy-700 rounded px-4 py-2.5 text-white placeholder-slate-500 focus:outline-none focus:border-kkevo-green text-sm"
          />
        </div>

        <div class="space-y-2 pt-1">
          <span class="text-xs uppercase font-mono text-slate-400 block">Briefing Streams:</span>
          <label class="flex items-center gap-2 text-xs text-slate-300">
            <input v-model="prefs.daily_briefing" type="checkbox" class="rounded bg-kkevo-navy-950 border-kkevo-navy-700 text-kkevo-green focus:ring-0" />
            <span>Daily African Headline & Verification Digest</span>
          </label>
          <label class="flex items-center gap-2 text-xs text-slate-300">
            <input v-model="prefs.geopolitics" type="checkbox" class="rounded bg-kkevo-navy-950 border-kkevo-navy-700 text-kkevo-green focus:ring-0" />
            <span>Geopolitics, Sovereignty & Multipolar Alliances</span>
          </label>
          <label class="flex items-center gap-2 text-xs text-slate-300">
            <input v-model="prefs.critical_minerals" type="checkbox" class="rounded bg-kkevo-navy-950 border-kkevo-navy-700 text-kkevo-green focus:ring-0" />
            <span>Who Owns Africa's Resources? (Mineral & Value Chain Tracker)</span>
          </label>
        </div>

        <div v-if="successMsg" class="p-3 bg-emerald-950/60 border border-kkevo-green/40 rounded text-xs text-kkevo-green">
          {{ successMsg }}
        </div>
        <div v-if="errorMsg" class="p-3 bg-red-950/60 border border-red-500/40 rounded text-xs text-red-400">
          {{ errorMsg }}
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full py-3 bg-kkevo-green text-kkevo-navy-950 font-bold rounded text-xs uppercase tracking-widest hover:bg-kkevo-green-glow transition flex items-center justify-center gap-2"
        >
          <span v-if="loading">Subscribing...</span>
          <span v-else>Receive Intelligence Briefings &rarr;</span>
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { api } from '../../services/api';

defineProps({
  isOpen: Boolean
});

const emit = defineEmits(['close']);
const email = ref('');
const loading = ref(false);
const successMsg = ref('');
const errorMsg = ref('');

const prefs = ref({
  daily_briefing: true,
  geopolitics: true,
  critical_minerals: true,
});

async function handleSubmit() {
  loading.value = true;
  successMsg.value = '';
  errorMsg.value = '';
  try {
    const res = await api.subscribeNewsletter(email.value, prefs.value);
    successMsg.value = res.message || 'Subscription confirmed.';
    setTimeout(() => {
      emit('close');
      email.value = '';
      successMsg.value = '';
    }, 2500);
  } catch (err) {
    errorMsg.value = err.data?.email?.[0] || err.message || 'Subscription failed.';
  } finally {
    loading.value = false;
  }
}
</script>
