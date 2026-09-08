<template>
  <div
    class="fixed bottom-5 right-5 z-50 flex flex-col gap-3 max-w-sm w-full pointer-events-none px-4 sm:px-0"
    aria-live="assertive"
  >
    <transition-group
      enter-active-class="transform ease-out duration-300 transition"
      enter-from-class="translate-y-4 opacity-0 sm:translate-y-0 sm:translate-x-4"
      enter-to-class="translate-y-0 opacity-100 sm:translate-x-0"
      leave-active-class="transition ease-in duration-200"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0 translate-x-4"
    >
      <div
        v-for="alert in alertStore.alerts"
        :key="alert.id"
        class="pointer-events-auto w-full bg-white dark:bg-[#0C121E] border border-slate-200 dark:border-white/10 rounded-xl p-4 shadow-xl dark:shadow-[0_12px_35px_-5px_rgba(0,0,0,0.9)] flex items-start gap-3.5 transition-colors overflow-hidden relative"
      >
        <!-- Accent indicator stripe -->
        <div
          :class="[
            'absolute left-0 top-0 bottom-0 w-1.5',
            stripeColor(alert.type)
          ]"
        ></div>

        <!-- Alert Icon -->
        <div :class="['shrink-0 p-1 rounded-lg', iconBg(alert.type)]">
          <!-- Success check -->
          <svg v-if="alert.type === 'success'" class="w-5 h-5 text-emerald-600 dark:text-kkevo-green" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
          </svg>
          <!-- Info / News alert -->
          <svg v-else-if="alert.type === 'info'" class="w-5 h-5 text-kkevo-blue dark:text-kkevo-blue-glow" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <!-- Warning -->
          <svg v-else-if="alert.type === 'warning'" class="w-5 h-5 text-amber-600 dark:text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
          </svg>
          <!-- Error -->
          <svg v-else class="w-5 h-5 text-red-600 dark:text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>

        <!-- Text Content -->
        <div class="flex-grow min-w-0 pr-2">
          <h5 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-white font-headline leading-tight">
            {{ alert.title }}
          </h5>
          <p v-if="alert.message" class="text-xs text-slate-600 dark:text-slate-300 mt-0.5 leading-relaxed">
            {{ alert.message }}
          </p>
        </div>

        <!-- Dismiss button -->
        <button
          @click="alertStore.dismiss(alert.id)"
          class="text-slate-400 hover:text-slate-700 dark:hover:text-white p-1 rounded transition shrink-0"
          title="Dismiss notification"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </transition-group>
  </div>
</template>

<script setup>
import { useAlertStore } from '../../stores/alertStore';

const alertStore = useAlertStore();

function stripeColor(type) {
  switch (type) {
    case 'success':
      return 'bg-emerald-500 dark:bg-kkevo-green';
    case 'info':
      return 'bg-kkevo-blue dark:bg-kkevo-blue-glow';
    case 'warning':
      return 'bg-amber-500 dark:bg-amber-400';
    case 'error':
      return 'bg-red-500 dark:bg-red-400';
    default:
      return 'bg-slate-400';
  }
}

function iconBg(type) {
  switch (type) {
    case 'success':
      return 'bg-emerald-50 dark:bg-emerald-950/60';
    case 'info':
      return 'bg-blue-50 dark:bg-blue-950/60';
    case 'warning':
      return 'bg-amber-50 dark:bg-amber-950/60';
    case 'error':
      return 'bg-red-50 dark:bg-red-950/60';
    default:
      return 'bg-slate-100 dark:bg-slate-800';
  }
}
</script>
