<template>
  <div class="min-h-screen py-8">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
      <div class="border-b border-slate-200 dark:border-white/[0.08] pb-6 space-y-2">
        <span class="text-xs font-mono font-bold tracking-widest text-kkevo-green uppercase">
          Institutional Governance & Transparency
        </span>
        <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white font-headline">
          Editorial Standards & AI Media Policy
        </h1>
        <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
          KKEVO STUDIO MEDIA is committed to uncompromising independence, rigorous empirical verification, and structural depth.
        </p>
      </div>

      <!-- Navigation Tabs -->
      <div class="flex flex-wrap gap-2 border-b border-slate-200 dark:border-white/[0.08] pb-3 text-xs font-mono">
        <button
          v-for="t in tabs"
          :key="t.id"
          @click="activeTab = t.id"
          :class="[
            'px-3.5 py-1.5 rounded-lg transition font-medium',
            activeTab === t.id
              ? 'bg-kkevo-blue text-white font-bold shadow-sm'
              : 'bg-slate-100 dark:bg-white/[0.05] border border-slate-200 dark:border-white/[0.08] text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-white/[0.1]'
          ]"
        >
          {{ t.label }}
        </button>
      </div>

      <!-- Content Sections -->
      <div class="bg-white dark:bg-[#0A0F1A] border border-slate-200 dark:border-white/[0.08] rounded-2xl p-6 sm:p-8 space-y-6 text-sm text-slate-700 dark:text-slate-300 leading-relaxed shadow-sm transition-colors">
        <!-- Tab 1: Editorial Standards -->
        <div v-if="activeTab === 'standards'" class="space-y-4">
          <h2 class="text-xl font-bold text-slate-900 dark:text-white font-headline">Editorial Philosophy & African Sovereignty</h2>
          <p>
            KKEVO STUDIO MEDIA operates as an African-centred, fiercely independent global newsroom. We reject sensationalism, clickbait, and ideological subservience. We scrutinise African governments, foreign powers, transnational corporations, and civil society with the exact same unyielding standard of empirical evidence.
          </p>
          <div class="p-4 bg-slate-50 dark:bg-[#06090E] rounded-xl border border-slate-200 dark:border-white/[0.08] space-y-2 text-xs">
            <strong class="text-kkevo-green font-mono uppercase block font-bold">Core Scrutiny Questions Applied to Every Story:</strong>
            <ul class="list-disc list-inside space-y-1 text-slate-700 dark:text-slate-300">
              <li>What happened? (Verified facts separated from claims)</li>
              <li>Why does it matter? (Structural impact on African citizens and industry)</li>
              <li>What is the historical and economic lineage?</li>
              <li>What are the competing sovereign perspectives?</li>
              <li>What are the concrete second-order and scenario outcomes?</li>
            </ul>
          </div>
        </div>

        <!-- Tab 2: AI & Synthetic Media Policy -->
        <div v-else-if="activeTab === 'ai'" class="space-y-4">
          <h2 class="text-xl font-bold text-slate-900 dark:text-white font-headline">AI & Synthetic Media Policy</h2>
          <p>
            As artificial intelligence technologies transform publishing, KKEVO STUDIO MEDIA maintains a definitive boundary between illustrative technological tools and documentary evidence.
          </p>
          <div class="space-y-3 text-xs">
            <div class="p-3.5 bg-red-50 dark:bg-red-950/40 border border-red-200 dark:border-red-900/40 rounded-xl text-slate-800 dark:text-slate-200">
              <strong class="text-red-600 dark:text-red-400 font-mono uppercase block mb-1 font-bold">Documentary Evidence Integrity:</strong>
              AI-generated imagery, deepfake synthesis, or simulated video is strictly prohibited from being presented as documentary reality. Authentic on-the-ground photojournalism and verified archival records are mandatory for news reporting.
            </div>
            <div class="p-3.5 bg-blue-50 dark:bg-blue-950/40 border border-blue-200 dark:border-blue-900/40 rounded-xl text-slate-800 dark:text-slate-200">
              <strong class="text-kkevo-blue dark:text-kkevo-blue-glow font-mono uppercase block mb-1 font-bold">Assistive & Research Utility:</strong>
              AI tools may assist reporters with large-scale document parsing, dataset cross-referencing, multi-language translation between African languages, and clearly-labelled conceptual diagrams.
            </div>
            <div class="p-3.5 bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-900/40 rounded-xl text-slate-800 dark:text-slate-200">
              <strong class="text-emerald-700 dark:text-kkevo-green font-mono uppercase block mb-1 font-bold">Human Editorial Responsibility:</strong>
              Every published word, claim classification, and citation undergoes human editor review. Algorithms do not have bylines, nor do they possess legal editorial accountability.
            </div>
          </div>
        </div>

        <!-- Tab 3: Sourcing & Credibility -->
        <div v-else-if="activeTab === 'sourcing'" class="space-y-4">
          <h2 class="text-xl font-bold text-slate-900 dark:text-white font-headline">Sources & Verification Architecture</h2>
          <p>
            Credibility is an engineering problem as much as an editorial standard. Our newsroom categorizes every critical assertion:
          </p>
          <ul class="space-y-2 text-xs">
            <li><strong class="text-emerald-700 dark:text-kkevo-green font-mono">VERIFIED FACT:</strong> Corroborated by dual primary documents, raw telemetry, court filings, or eyewitness accounts.</li>
            <li><strong class="text-blue-700 dark:text-kkevo-blue-glow font-mono">OFFICIAL CLAIM:</strong> Statements issued by heads of state, ministries, or military commands, presented with context.</li>
            <li><strong class="text-amber-600 dark:text-amber-400 font-mono">ALLEGATION:</strong> Unsubstantiated third-party reports under active investigation.</li>
            <li><strong class="text-purple-600 dark:text-purple-300 font-mono">ANALYSIS:</strong> Interpretive foresight by accredited KKEVO fellows and analysts based on established economic models.</li>
          </ul>
        </div>

        <!-- Tab 4: Ethics & Whistleblowers -->
        <div v-else-if="activeTab === 'ethics'" class="space-y-4">
          <h2 class="text-xl font-bold text-slate-900 dark:text-white font-headline">Whistleblower Protection & Ethics</h2>
          <p>
            KKEVO STUDIO MEDIA safeguards confidential sources, whistleblowers in extractive industries, and investigative researchers across the continent. We do not surrender source identities to state authorities or corporate litigation cartels.
          </p>
          <div class="p-4 bg-slate-50 dark:bg-[#06090E] rounded-xl border border-slate-200 dark:border-white/[0.08] text-xs font-mono space-y-1">
            <span class="text-slate-500 dark:text-slate-400 block font-bold">Secure Newsroom Cryptographic Ingestion:</span>
            <span class="text-kkevo-green font-bold">desk@kkevostudiomedia.com (PGP Key Available on Request)</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const activeTab = ref('standards');

const tabs = [
  { id: 'standards', label: 'Editorial Standards' },
  { id: 'ai', label: 'AI & Synthetic Media Policy' },
  { id: 'sourcing', label: 'Sources & Credibility' },
  { id: 'ethics', label: 'Ethics & Whistleblowers' },
];
</script>
