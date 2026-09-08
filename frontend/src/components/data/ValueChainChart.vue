<template>
  <div class="bg-kkevo-navy-950 border border-kkevo-navy-800 rounded-lg p-6 space-y-4 shadow-xl">
    <div class="flex items-center justify-between border-b border-kkevo-navy-800 pb-3">
      <div>
        <span class="text-xs font-mono font-bold tracking-widest text-kkevo-green uppercase block">
          KKEVO Data Journalism & Economics
        </span>
        <h4 class="text-base font-bold text-white font-headline mt-0.5">
          African Mineral Value-Addition Multiplier ($ / Metric Ton)
        </h4>
      </div>
      <span class="text-xs text-slate-400 font-mono">Source: USGS & KKEVO Research</span>
    </div>

    <p class="text-xs text-slate-300 leading-relaxed">
      Why African states are outlawing raw ore exports: in-country refining yields between <strong>5x to 40x higher revenue</strong> retained within the domestic banking system.
    </p>

    <!-- Visual Chart Bars -->
    <div class="space-y-4 pt-2">
      <!-- Lithium Value Chain -->
      <div class="space-y-1.5">
        <div class="flex justify-between text-xs font-mono">
          <span class="text-slate-200 font-bold">Lithium (Zimbabwe / Mali)</span>
          <span class="text-kkevo-green font-bold">Raw Ore: $350 &rarr; Battery Hydroxide: $14,200</span>
        </div>
        <div class="h-5 bg-kkevo-navy-900 rounded overflow-hidden flex items-center p-0.5">
          <div class="bg-slate-500 h-full rounded-l text-[10px] text-white flex items-center px-1.5" style="width: 8%">
            Raw
          </div>
          <div class="bg-kkevo-blue h-full text-[10px] text-white flex items-center px-1.5" style="width: 25%">
            Conc 6%
          </div>
          <div class="bg-kkevo-green h-full rounded-r text-[10px] text-black font-bold flex items-center px-2 flex-grow">
            Refined Hydroxide (40x Multiplier)
          </div>
        </div>
      </div>

      <!-- Cobalt & Copper Chain -->
      <div class="space-y-1.5">
        <div class="flex justify-between text-xs font-mono">
          <span class="text-slate-200 font-bold">Cobalt & Copper (DRC / Zambia)</span>
          <span class="text-kkevo-blue-glow font-bold">Raw Concentrate: $1,200 &rarr; Refined Cathode: $8,900</span>
        </div>
        <div class="h-5 bg-kkevo-navy-900 rounded overflow-hidden flex items-center p-0.5">
          <div class="bg-slate-500 h-full rounded-l text-[10px] text-white flex items-center px-1.5" style="width: 14%">
            Concentrate
          </div>
          <div class="bg-kkevo-blue-glow h-full rounded-r text-[10px] text-black font-bold flex items-center px-2 flex-grow">
            Electro-Refined LME Grade Cathode (7.4x)
          </div>
        </div>
      </div>

      <!-- Gold Assaying Chain -->
      <div class="space-y-1.5">
        <div class="flex justify-between text-xs font-mono">
          <span class="text-slate-200 font-bold">Gold Smelting (Ghana / Burkina Faso)</span>
          <span class="text-amber-400 font-bold">Unrefined Dore &rarr; LBMA 99.99% Good Delivery Bullion</span>
        </div>
        <div class="h-5 bg-kkevo-navy-900 rounded overflow-hidden flex items-center p-0.5">
          <div class="bg-amber-700 h-full rounded-l text-[10px] text-white flex items-center px-1.5" style="width: 30%">
            Exported Dore (Foreign Margin Retained Offshore)
          </div>
          <div class="bg-amber-400 h-full rounded-r text-[10px] text-black font-bold flex items-center px-2 flex-grow">
            Domestic Central Bank Reserve Purity (100% Retained)
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
