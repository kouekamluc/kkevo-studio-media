<template>
  <section class="mt-16 space-y-8">
    <div class="flex items-end justify-between pb-3 border-b border-slate-200 dark:border-kkevo-navy-800">
      <div>
        <div class="flex items-center gap-2 text-xs font-mono font-bold tracking-widest text-kkevo-green uppercase">
          <span class="w-2 h-2 rounded-full bg-kkevo-green"></span>
          KKEVO Special Investigation
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white font-headline mt-1">
          Who Owns Africa’s Resources?
        </h2>
      </div>
      <router-link to="/category/resources" class="text-xs uppercase font-mono tracking-wider text-kkevo-green hover:underline font-bold">
        Track Value Chains &rarr;
      </router-link>
    </div>

    <!-- Value-Chain Visualizer Chart -->
    <ValueChainChart />

    <!-- Value Chain Comparison Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/90 dark:to-[#080D17] border border-slate-200 dark:border-white/[0.08] rounded-xl p-6 space-y-4 hover:border-kkevo-green/60 dark:hover:border-kkevo-green/50 transition-all duration-300 shadow-sm hover:shadow-lg dark:shadow-[0_4px_20px_-4px_rgba(0,0,0,0.6)] dark:hover:shadow-[0_12px_30px_-5px_rgba(0,210,106,0.18)] hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <span class="text-xs uppercase font-mono font-bold text-kkevo-green">Cobalt & Copper</span>
          <span class="text-xs text-slate-500 dark:text-slate-400 font-mono">DRC Belt</span>
        </div>
        <h3 class="text-lg font-bold text-slate-900 dark:text-white font-headline">Subsoil Mapping Data Sovereignty</h3>
        <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
          Transitioning from foreign concession monopolies to state-owned seismic data banks. Forcing European and Asian smelters to bid on transparent, verified sovereign assays.
        </p>
        <div class="pt-3 border-t border-slate-100 dark:border-white/[0.06] flex items-center justify-between text-xs font-mono">
          <span class="text-slate-500 dark:text-slate-400">Global Supply: <strong class="text-slate-800 dark:text-white">70%</strong></span>
          <span class="text-kkevo-green font-bold">Decree 0482 Active</span>
        </div>
      </div>

      <div class="bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/90 dark:to-[#080D17] border border-slate-200 dark:border-white/[0.08] rounded-xl p-6 space-y-4 hover:border-kkevo-blue/60 dark:hover:border-kkevo-blue/50 transition-all duration-300 shadow-sm hover:shadow-lg dark:shadow-[0_4px_20px_-4px_rgba(0,0,0,0.6)] dark:hover:shadow-[0_12px_30px_-5px_rgba(56,139,253,0.18)] hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <span class="text-xs uppercase font-mono font-bold text-kkevo-blue dark:text-kkevo-blue-glow">Lithium Retention</span>
          <span class="text-xs text-slate-500 dark:text-slate-400 font-mono">Zimbabwe / Mali</span>
        </div>
        <h3 class="text-lg font-bold text-slate-900 dark:text-white font-headline">Raw Spodumene Export Prohibitions</h3>
        <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
          Mandating local sulphate conversion before export. Foreign mining companies are forced to construct in-country processing kilns or forfeit exploratory permits.
        </p>
        <div class="pt-3 border-t border-slate-100 dark:border-white/[0.06] flex items-center justify-between text-xs font-mono">
          <span class="text-slate-500 dark:text-slate-400">Value Multiplier: <strong class="text-slate-800 dark:text-white">10x - 40x</strong></span>
          <span class="text-kkevo-blue dark:text-kkevo-blue-glow font-bold">Harare Ban Enforced</span>
        </div>
      </div>

      <div class="bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/90 dark:to-[#080D17] border border-slate-200 dark:border-white/[0.08] rounded-xl p-6 space-y-4 hover:border-amber-500/60 dark:hover:border-amber-400/50 transition-all duration-300 shadow-sm hover:shadow-lg dark:shadow-[0_4px_20px_-4px_rgba(0,0,0,0.6)] dark:hover:shadow-[0_12px_30px_-5px_rgba(245,158,11,0.18)] hover:-translate-y-1">
        <div class="flex items-center justify-between">
          <span class="text-xs uppercase font-mono font-bold text-amber-600 dark:text-amber-400">Sovereign Bullion</span>
          <span class="text-xs text-slate-500 dark:text-slate-400 font-mono">Ghana / Burkina Faso</span>
        </div>
        <h3 class="text-lg font-bold text-slate-900 dark:text-white font-headline">LBMA Domestic Gold Assaying</h3>
        <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
          Ending a century of raw bullion flight. Central banks directly purchase artisanal and commercial output in local currency, stabilizing foreign exchange reserves.
        </p>
        <div class="pt-3 border-t border-slate-100 dark:border-white/[0.06] flex items-center justify-between text-xs font-mono">
          <span class="text-slate-500 dark:text-slate-400">Purity Standard: <strong class="text-slate-800 dark:text-white">99.99%</strong></span>
          <span class="text-amber-600 dark:text-amber-400 font-bold">Accra Refinery Active</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import ValueChainChart from '../data/ValueChainChart.vue';
</script>
