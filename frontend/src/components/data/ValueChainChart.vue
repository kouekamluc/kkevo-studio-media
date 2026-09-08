<template>
  <div class="bg-white dark:bg-gradient-to-b dark:from-[#0E1726]/90 dark:to-[#080D17] border border-slate-200 dark:border-white/[0.08] rounded-xl p-6 space-y-4 shadow-sm dark:shadow-xl transition-colors">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-200 dark:border-white/[0.08] pb-3 gap-2">
      <div>
        <span class="text-xs font-mono font-bold tracking-widest text-kkevo-green uppercase block">
          KKEVO Data Journalism & Economics
        </span>
        <h4 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white font-headline mt-0.5">
          African Mineral Value-Addition Multiplier ($ / Metric Ton)
        </h4>
      </div>
      <span class="text-xs text-slate-500 dark:text-slate-400 font-mono">Source: USGS & KKEVO Research</span>
    </div>

    <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
      Why African states are outlawing raw ore exports: in-country refining yields between <strong class="text-slate-900 dark:text-white font-semibold">5x to 40x higher revenue</strong> retained within the domestic banking system.
    </p>

    <!-- Visual Chart Bars -->
    <div class="space-y-4 pt-2">
      <!-- Lithium Value Chain -->
      <div class="space-y-1.5">
        <div class="flex justify-between text-xs font-mono">
          <span class="text-slate-800 dark:text-slate-200 font-bold">Lithium (Zimbabwe / Mali)</span>
          <span class="text-emerald-700 dark:text-kkevo-green font-bold">Raw Ore: $350 &rarr; Battery Hydroxide: $14,200</span>
        </div>
        <div class="h-6 bg-slate-100 dark:bg-[#060910] border border-slate-200 dark:border-white/[0.06] rounded-md overflow-hidden flex items-center p-0.5">
          <div class="bg-slate-400 dark:bg-slate-600 h-full rounded-l text-[10px] text-white flex items-center px-2 font-medium" style="width: 8%">
            Raw
          </div>
          <div class="bg-kkevo-blue h-full text-[10px] text-white flex items-center px-2 font-medium" style="width: 25%">
            Conc 6%
          </div>
          <div class="bg-emerald-500 dark:bg-kkevo-green h-full rounded-r text-[10px] text-slate-900 font-bold flex items-center px-2.5 flex-grow">
            Refined Hydroxide (40x Multiplier)
          </div>
        </div>
      </div>

      <!-- Cobalt & Copper Chain -->
      <div class="space-y-1.5">
        <div class="flex justify-between text-xs font-mono">
          <span class="text-slate-800 dark:text-slate-200 font-bold">Cobalt & Copper (DRC / Zambia)</span>
          <span class="text-blue-700 dark:text-kkevo-blue-glow font-bold">Raw Concentrate: $1,200 &rarr; Refined Cathode: $8,900</span>
        </div>
        <div class="h-6 bg-slate-100 dark:bg-[#060910] border border-slate-200 dark:border-white/[0.06] rounded-md overflow-hidden flex items-center p-0.5">
          <div class="bg-slate-400 dark:bg-slate-600 h-full rounded-l text-[10px] text-white flex items-center px-2 font-medium" style="width: 14%">
            Concentrate
          </div>
          <div class="bg-blue-600 dark:bg-kkevo-blue-glow h-full rounded-r text-[10px] text-white dark:text-black font-bold flex items-center px-2.5 flex-grow">
            Electro-Refined LME Grade Cathode (7.4x)
          </div>
        </div>
      </div>

      <!-- Gold Assaying Chain -->
      <div class="space-y-1.5">
        <div class="flex justify-between text-xs font-mono">
          <span class="text-slate-800 dark:text-slate-200 font-bold">Gold Smelting (Ghana / Burkina Faso)</span>
          <span class="text-amber-700 dark:text-amber-400 font-bold">Unrefined Dore &rarr; LBMA 99.99% Good Delivery Bullion</span>
        </div>
        <div class="h-6 bg-slate-100 dark:bg-[#060910] border border-slate-200 dark:border-white/[0.06] rounded-md overflow-hidden flex items-center p-0.5">
          <div class="bg-amber-600 h-full rounded-l text-[10px] text-white flex items-center px-2 font-medium" style="width: 30%">
            Exported Dore
          </div>
          <div class="bg-amber-400 dark:bg-amber-400 h-full rounded-r text-[10px] text-slate-900 font-bold flex items-center px-2.5 flex-grow">
            Domestic Central Bank Reserve Purity (100% Retained)
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
