<template>
  <section class="mt-16">
    <div class="flex items-end justify-between mb-8 pb-3 border-b border-kkevo-navy-800">
      <div>
        <div class="flex items-center gap-2 text-xs font-mono font-bold tracking-widest text-kkevo-green uppercase">
          <span class="w-2 h-2 rounded-full bg-kkevo-green"></span>
          KKEVO Special Investigation
        </div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-white font-headline mt-1">
          Who Owns Africa’s Resources?
        </h2>
      </div>
      <router-link to="/category/resources" class="text-xs uppercase font-mono tracking-wider text-kkevo-green hover:underline">
        Track Value Chains &rarr;
      </router-link>
    </div>

    <!-- Value Chain Comparison Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg p-6 space-y-4 hover:border-kkevo-navy-700 transition">
        <div class="flex items-center justify-between">
          <span class="text-xs uppercase font-mono font-bold text-kkevo-green">Cobalt & Copper</span>
          <span class="text-xs text-slate-400 font-mono">DRC Belt</span>
        </div>
        <h3 class="text-lg font-bold text-white font-headline">Subsoil Mapping Data Sovereignty</h3>
        <p class="text-xs text-slate-400 leading-relaxed">
          Transitioning from foreign concession monopolies to state-owned seismic data banks. Forcing European and Asian smelters to bid on transparent, verified sovereign assays.
        </p>
        <div class="pt-3 border-t border-kkevo-navy-800 flex items-center justify-between text-xs font-mono">
          <span class="text-slate-400">Global Supply: <strong class="text-white">70%</strong></span>
          <span class="text-kkevo-green font-bold">Decree 0482 Active</span>
        </div>
      </div>

      <div class="bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg p-6 space-y-4 hover:border-kkevo-navy-700 transition">
        <div class="flex items-center justify-between">
          <span class="text-xs uppercase font-mono font-bold text-kkevo-blue-glow">Lithium Retention</span>
          <span class="text-xs text-slate-400 font-mono">Zimbabwe / Mali</span>
        </div>
        <h3 class="text-lg font-bold text-white font-headline">Raw Spodumene Export Prohibitions</h3>
        <p class="text-xs text-slate-400 leading-relaxed">
          Mandating local sulphate conversion before export. Foreign mining companies are forced to construct in-country processing kilns or forfeit exploratory permits.
        </p>
        <div class="pt-3 border-t border-kkevo-navy-800 flex items-center justify-between text-xs font-mono">
          <span class="text-slate-400">Value Multiplier: <strong class="text-white">10x</strong></span>
          <span class="text-kkevo-blue-glow font-bold">Harare Ban Enforced</span>
        </div>
      </div>

      <div class="bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg p-6 space-y-4 hover:border-kkevo-navy-700 transition">
        <div class="flex items-center justify-between">
          <span class="text-xs uppercase font-mono font-bold text-amber-400">Sovereign Bullion</span>
          <span class="text-xs text-slate-400 font-mono">Ghana / Burkina Faso</span>
        </div>
        <h3 class="text-lg font-bold text-white font-headline">LBMA Domestic Gold Assaying</h3>
        <p class="text-xs text-slate-400 leading-relaxed">
          Ending a century of raw bullion flight. Central banks directly purchase artisanal and commercial output in local currency, stabilizing foreign exchange reserves.
        </p>
        <div class="pt-3 border-t border-kkevo-navy-800 flex items-center justify-between text-xs font-mono">
          <span class="text-slate-400">Purity Standard: <strong class="text-white">99.99%</strong></span>
          <span class="text-amber-400 font-bold">Accra Refinery Active</span>
        </div>
      </div>
    </div>
  </section>
</template>
