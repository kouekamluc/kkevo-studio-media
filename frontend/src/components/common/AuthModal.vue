<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 dark:bg-black/80 backdrop-blur-sm">
    <div class="bg-white dark:bg-[#0B101B] border border-slate-200 dark:border-white/[0.08] rounded-2xl max-w-md w-full p-6 sm:p-7 shadow-2xl relative space-y-4 transition-colors">
      <button @click="$emit('close')" class="absolute top-4 right-4 text-slate-400 hover:text-slate-800 dark:hover:text-white transition-colors">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <div class="space-y-1">
        <h3 class="text-lg font-bold text-slate-900 dark:text-white font-headline">Reader & Newsroom Access</h3>
        <p class="text-xs text-slate-600 dark:text-slate-400">Sign in to save articles, manage intelligence alerts, or access editorial desks.</p>
      </div>

      <!-- Quick Demo Credentials Selector for Easy Review -->
      <div class="p-3 bg-slate-50 dark:bg-[#06090E] border border-slate-200 dark:border-white/[0.08] rounded-lg text-xs space-y-1.5">
        <span class="text-slate-500 dark:text-slate-400 font-mono font-bold block">Instant Demo Access:</span>
        <div class="flex gap-2">
          <button
            @click="fillCredentials('editor@kkevostudiomedia.com', 'editorPass2026!')"
            class="px-2.5 py-1 bg-blue-50 dark:bg-kkevo-blue/20 text-kkevo-blue dark:text-kkevo-blue-glow border border-blue-200 dark:border-kkevo-blue/40 rounded hover:bg-blue-100 dark:hover:bg-kkevo-blue/30 transition text-[11px] font-semibold"
          >
            Senior Editor
          </button>
          <button
            @click="fillCredentials('admin@kkevostudiomedia.com', 'kkevoAdmin2026!')"
            class="px-2.5 py-1 bg-emerald-50 dark:bg-emerald-950/60 text-emerald-800 dark:text-kkevo-green border border-emerald-200 dark:border-kkevo-green/40 rounded hover:bg-emerald-100 dark:hover:bg-emerald-900/60 transition text-[11px] font-semibold"
          >
            Publisher Admin
          </button>
        </div>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-3">
        <div>
          <label class="block text-xs uppercase font-mono text-slate-500 dark:text-slate-400 mb-1 font-bold">Email</label>
          <input
            v-model="email"
            type="email"
            required
            class="w-full bg-slate-50 dark:bg-[#06090E] border border-slate-300 dark:border-white/[0.1] rounded-lg px-3 py-2 text-slate-900 dark:text-white text-sm focus:outline-none focus:border-kkevo-blue"
          />
        </div>
        <div>
          <label class="block text-xs uppercase font-mono text-slate-500 dark:text-slate-400 mb-1 font-bold">Password</label>
          <input
            v-model="password"
            type="password"
            required
            class="w-full bg-slate-50 dark:bg-[#06090E] border border-slate-300 dark:border-white/[0.1] rounded-lg px-3 py-2 text-slate-900 dark:text-white text-sm focus:outline-none focus:border-kkevo-blue"
          />
        </div>

        <div v-if="errorMsg" class="p-2.5 bg-red-50 dark:bg-red-950/60 border border-red-300 dark:border-red-500/40 rounded-lg text-xs text-red-800 dark:text-red-400 font-semibold">
          {{ errorMsg }}
        </div>

        <button
          type="submit"
          :disabled="authStore.loading"
          class="w-full py-2.5 bg-kkevo-blue text-white font-bold rounded-lg text-xs uppercase tracking-widest hover:bg-kkevo-blue-dark transition shadow-sm"
        >
          <span v-if="authStore.loading">Authenticating...</span>
          <span v-else>Sign In</span>
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../../stores/authStore';

defineProps({
  isOpen: Boolean
});

const emit = defineEmits(['close']);
const authStore = useAuthStore();

const email = ref('');
const password = ref('');
const errorMsg = ref('');

function fillCredentials(e, p) {
  email.value = e;
  password.value = p;
}

async function handleLogin() {
  errorMsg.value = '';
  try {
    await authStore.login(email.value, password.value);
    emit('close');
  } catch (err) {
    errorMsg.value = err.message || 'Invalid credentials.';
  }
}
</script>
