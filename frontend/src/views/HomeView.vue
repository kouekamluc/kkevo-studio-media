<template>
  <div class="min-h-screen">
    <!-- Main Content Container -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-12">
      <!-- Loading State -->
      <div v-if="newsStore.loading && !newsStore.homepageData" class="py-20 text-center space-y-4">
        <div class="w-12 h-12 border-4 border-kkevo-blue border-t-transparent rounded-full animate-spin mx-auto"></div>
        <p class="text-xs uppercase font-mono tracking-widest text-slate-400">Loading KKEVO Newsroom Feed...</p>
      </div>

      <template v-else>
        <!-- 1. Dominant Lead & Secondary Grid Section -->
        <section class="space-y-6">
          <HeroStory
            v-if="newsStore.heroStory"
            :story="newsStore.heroStory"
          />

          <!-- Secondary Leads Grid -->
          <div v-if="newsStore.secondaryLeads.length" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <SecondaryLeadCard
              v-for="story in newsStore.secondaryLeads"
              :key="story.id"
              :story="story"
            />
          </div>
        </section>

        <!-- 2. Split Stream: Latest Verified News & Resources / Africa Today -->
        <section class="grid grid-cols-1 lg:grid-cols-12 gap-8 pt-4">
          <!-- Left Column: Chronological Verified Feed -->
          <div class="lg:col-span-4">
            <LatestNewsFeed :news-items="newsStore.latestNews" />
          </div>

          <!-- Right Column: Continental Economy & Deep Resources -->
          <div class="lg:col-span-8 space-y-6">
            <div class="flex items-center justify-between border-b border-kkevo-navy-800 pb-3">
              <h3 class="text-xs uppercase font-bold tracking-widest text-white font-mono flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-kkevo-green"></span>
                Africa Today: Economic & Strategic Developments
              </h3>
              <router-link to="/category/africa" class="text-xs text-kkevo-green hover:underline font-mono">
                View All &rarr;
              </router-link>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <SecondaryLeadCard
                v-for="story in newsStore.resourceStories"
                :key="story.id"
                :story="story"
              />
            </div>
          </div>
        </section>

        <!-- 3. KKEVO STUDIO MEDIA | In-Depth Perspective & Analysis -->
        <AnalysisSection :stories="newsStore.analysisStories" />

        <!-- 4. Interactive Africa Continental Map Explorer -->
        <AfricaMapExplorer :countries="newsStore.countries" />

        <!-- 5. Who Owns Africa's Resources? -->
        <ResourceTracker />

        <!-- 6. History Spotlight: The Africa They Never Taught You -->
        <section v-if="newsStore.historyStories.length" class="mt-16 bg-kkevo-navy-900 border border-kkevo-navy-800 rounded-lg p-6 sm:p-8">
          <div class="flex items-end justify-between mb-6 pb-3 border-b border-kkevo-navy-800">
            <div>
              <span class="text-xs font-mono font-bold tracking-widest text-amber-400 uppercase block">
                Archival & Pre-Colonial Scrutiny
              </span>
              <h2 class="text-2xl font-extrabold text-white font-headline mt-1">
                The Africa They Never Taught You
              </h2>
            </div>
            <router-link to="/category/history" class="text-xs uppercase font-mono tracking-wider text-amber-400 hover:underline">
              Historical Archives &rarr;
            </router-link>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <article
              v-for="hist in newsStore.historyStories"
              :key="hist.id"
              class="bg-kkevo-navy-950 border border-kkevo-navy-800 rounded-lg p-5 flex flex-col justify-between group hover:border-amber-500/40 transition"
            >
              <div class="space-y-3">
                <span class="text-[10px] font-mono uppercase tracking-widest text-amber-400 font-bold">Historical Record</span>
                <router-link :to="`/article/${hist.slug}`" class="block">
                  <h3 class="text-base font-bold text-white leading-snug group-hover:text-amber-300 transition font-headline">
                    {{ hist.title }}
                  </h3>
                </router-link>
                <p v-if="hist.subtitle" class="text-xs text-slate-400 line-clamp-3 leading-relaxed">
                  {{ hist.subtitle }}
                </p>
              </div>
              <div class="pt-3 mt-4 border-t border-kkevo-navy-800 text-xs text-slate-400 font-mono">
                {{ hist.authors?.[0]?.display_name || 'KKEVO Historian' }} &bull; {{ hist.reading_time_minutes }}m read
              </div>
            </article>
          </div>
        </section>

        <!-- 7. Video & 60 Seconds of Context -->
        <VideoReelsSection :videos="videoItems" />
      </template>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useNewsStore } from '../stores/newsStore';
import { api } from '../services/api';
import HeroStory from '../components/editorial/HeroStory.vue';
import SecondaryLeadCard from '../components/editorial/SecondaryLeadCard.vue';
import LatestNewsFeed from '../components/editorial/LatestNewsFeed.vue';
import AnalysisSection from '../components/editorial/AnalysisSection.vue';
import AfricaMapExplorer from '../components/editorial/AfricaMapExplorer.vue';
import ResourceTracker from '../components/editorial/ResourceTracker.vue';
import VideoReelsSection from '../components/editorial/VideoReelsSection.vue';

const newsStore = useNewsStore();
const videoItems = ref([]);

onMounted(async () => {
  await Promise.all([
    newsStore.fetchHomepage(),
    newsStore.fetchTaxonomy(),
    api.getVideos().then(res => {
      videoItems.value = res.results || res;
    }).catch(console.error)
  ]);
});
</script>
