<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 dark:bg-black/80 backdrop-blur-sm">
    <div class="bg-white dark:bg-[#0B101B] border border-slate-200 dark:border-white/[0.08] rounded-2xl max-w-lg w-full p-6 sm:p-8 shadow-2xl relative space-y-5 transition-colors">
      <button @click="$emit('close')" class="absolute top-4 right-4 text-slate-400 hover:text-slate-800 dark:hover:text-white transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <div class="space-y-2">
        <span class="inline-flex items-center gap-1.5 text-xs font-mono font-bold tracking-widest text-kkevo-green uppercase">
          <span class="w-2 h-2 rounded-full bg-kkevo-green"></span>
          KKEVO Intelligence Briefing
        </span>
        <h3 class="text-xl font-bold text-slate-900 dark:text-white font-headline">
          Independent African Geopolitical & Economic Intelligence
        </h3>
        <p class="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
          Rigorous daily and weekly briefings delivered directly to senior analysts, industrial leaders, diplomats, and informed readers globally.
        </p>
      </div>

      <form @submit.prevent="handleSubmit" class="space-y-4">
        <div>
          <label class="block text-xs uppercase font-mono text-slate-500 dark:text-slate-400 mb-1 font-bold">Corporate or Personal Email</label>
          <input
            v-model="email"
            type="email"
            required
            placeholder="analyst@institution.org"
            class="w-full bg-slate-50 dark:bg-[#06090E] border border-slate-300 dark:border-white/[0.1] rounded-lg px-4 py-2.5 text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:border-kkevo-green text-sm"
          />
        </div>

        <div class="space-y-2 pt-1">
          <span class="text-xs uppercase font-mono text-slate-500 dark:text-slate-400 block font-bold">Briefing Streams:</span>
          <label class="flex items-center gap-2 text-xs text-slate-700 dark:text-slate-300 cursor-pointer">
            <input v-model="prefs.daily_briefing" type="checkbox" class="rounded bg-slate-100 dark:bg-kkevo-navy-950 border-slate-300 dark:border-kkevo-navy-700 text-kkevo-green focus:ring-0" />
            <span>Daily African Headline & Verification Digest</span>
          </label>
          <label class="flex items-center gap-2 text-xs text-slate-700 dark:text-slate-300 cursor-pointer">
            <input v-model="prefs.geopolitics" type="checkbox" class="rounded bg-slate-100 dark:bg-kkevo-navy-950 border-slate-300 dark:border-kkevo-navy-700 text-kkevo-green focus:ring-0" />
            <span>Geopolitics, Sovereignty & Multipolar Alliances</span>
          </label>
          <label class="flex items-center gap-2 text-xs text-slate-700 dark:text-slate-300 cursor-pointer">
            <input v-model="prefs.critical_minerals" type="checkbox" class="rounded bg-slate-100 dark:bg-kkevo-navy-950 border-slate-300 dark:border-kkevo-navy-700 text-kkevo-green focus:ring-0" />
            <span>Who Owns Africa's Resources? (Mineral & Value Chain Tracker)</span>
          </label>
        </div>

        <div v-if="successMsg" class="p-3 bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-300 dark:border-kkevo-green/40 rounded-lg text-xs text-emerald-800 dark:text-kkevo-green font-semibold">
          {{ successMsg }}
        </div>
        <div v-if="errorMsg" class="p-3 bg-red-50 dark:bg-red-950/60 border border-red-300 dark:border-red-500/40 rounded-lg text-xs text-red-800 dark:text-red-400 font-semibold">
          {{ errorMsg }}
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full py-3 bg-kkevo-green text-slate-950 font-bold rounded-lg text-xs uppercase tracking-widest hover:bg-kkevo-green-glow transition flex items-center justify-center gap-2 shadow-sm"
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
import { useAlertStore } from '../../stores/alertStore';

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
    const alertStore = useAlertStore();
    alertStore.success('Intelligence Briefing Activated', 'You are now subscribed to verified African daily briefs.');
    setTimeout(() => {
      emit('close');
      email.value = '';
      successMsg.value = '';
    }, 2500);
  } catch (err) {
    errorMsg.value = err.data?.email?.[0] || err.message || 'Subscription failed.';
    const alertStore = useAlertStore();
    alertStore.error('Subscription Error', errorMsg.value);
  } finally {
    loading.value = false;
  }
}
</script>
