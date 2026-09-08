import uuid
from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.accounts.models import User
from apps.taxonomy.models import Category, Subcategory, Topic, Region, Country
from apps.authors.models import AuthorProfile
from apps.sources.models import SourceType, Source, Citation, Claim, Correction
from apps.articles.models import Article
from apps.live.models import BreakingAlert, LiveBlog, LiveUpdate
from apps.video.models import VideoStory
from apps.newsletter.models import NewsletterSubscriber

class Command(BaseCommand):
    help = 'Seeds database with authoritative African-centred editorial content, taxonomy, sources, and journalists'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("==> Seeding KKEVO STUDIO MEDIA Database..."))

        # 1. USERS & ROLES
        admin_user, _ = User.objects.get_or_create(
            email='admin@kkevostudiomedia.com',
            defaults={
                'username': 'kkevoadmin',
                'first_name': 'KKEVO',
                'last_name': 'Publisher',
                'role': User.Role.ADMIN,
                'is_staff': True,
                'is_superuser': True,
                'is_verified': True,
            }
        )
        admin_user.set_password('kkevoAdmin2026!')
        admin_user.save()

        editor_user, _ = User.objects.get_or_create(
            email='editor@kkevostudiomedia.com',
            defaults={
                'username': 'senior_editor',
                'first_name': 'Amara',
                'last_name': 'Kone',
                'role': User.Role.SENIOR_EDITOR,
                'is_staff': True,
                'is_verified': True,
            }
        )
        editor_user.set_password('editorPass2026!')
        editor_user.save()

        kwame_user, _ = User.objects.get_or_create(
            email='kwame.mensah@kkevostudiomedia.com',
            defaults={
                'username': 'kwamemensah',
                'first_name': 'Kwame',
                'last_name': 'Mensah',
                'role': User.Role.CONTRIBUTOR,
                'is_verified': True,
            }
        )
        kwame_user.set_password('reporterPass2026!')
        kwame_user.save()

        aminata_user, _ = User.objects.get_or_create(
            email='aminata.diallo@kkevostudiomedia.com',
            defaults={
                'username': 'aminatadiallo',
                'first_name': 'Aminata',
                'last_name': 'Diallo',
                'role': User.Role.CONTRIBUTOR,
                'is_verified': True,
            }
        )
        aminata_user.set_password('reporterPass2026!')
        aminata_user.save()

        tariq_user, _ = User.objects.get_or_create(
            email='tariq.zuma@kkevostudiomedia.com',
            defaults={
                'username': 'tariqzuma',
                'first_name': 'Tariq',
                'last_name': 'Zuma',
                'role': User.Role.CONTRIBUTOR,
                'is_verified': True,
            }
        )
        tariq_user.set_password('reporterPass2026!')
        tariq_user.save()

        # 2. AUTHOR PROFILES
        author_amara, _ = AuthorProfile.objects.update_or_create(
            user=editor_user,
            defaults={
                'display_name': 'Amara Koné',
                'slug': 'amara-kone',
                'editorial_title': 'Senior Managing Editor & Geopolitics Lead',
                'bio': 'Specialist in West African security architecture, regional monetary pacts, and bilateral diplomacy. Formerly covering continental trade integration across Abidjan, Bamako, and Addis Ababa.',
                'avatar_url': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80',
                'twitter_handle': '@AmaraKone_KKEVO',
                'location': 'Abidjan / Dakar',
                'is_verified': True,
            }
        )

        author_kwame, _ = AuthorProfile.objects.update_or_create(
            user=kwame_user,
            defaults={
                'display_name': 'Kwame Mensah',
                'slug': 'kwame-mensah',
                'editorial_title': 'Critical Minerals & Industrial Strategy Lead',
                'bio': 'Investigative reporter tracking geological data sovereignty, lithium value retention laws, and domestic mineral refining across the Central and Southern African mineral belts.',
                'avatar_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80',
                'twitter_handle': '@KMensah_Energy',
                'location': 'Kinshasa / Accra',
                'is_verified': True,
            }
        )

        author_aminata, _ = AuthorProfile.objects.update_or_create(
            user=aminata_user,
            defaults={
                'display_name': 'Dr. Aminata Diallo',
                'slug': 'aminata-diallo',
                'editorial_title': 'Economic Sovereignty & Pre-Colonial History Fellow',
                'bio': 'Economic historian and researcher analyzing pre-colonial metallurgical trade corridors and contemporary African financial architecture.',
                'avatar_url': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=400&q=80',
                'twitter_handle': '@DrDiallo_History',
                'location': 'Bamako / Nairobi',
                'is_verified': True,
            }
        )

        # 3. REGIONS & COUNTRIES
        reg_west, _ = Region.objects.get_or_create(name='West Africa', defaults={'code': 'WA', 'description': 'ECOWAS & Alliance of Sahel States'})
        reg_central, _ = Region.objects.get_or_create(name='Central Africa', defaults={'code': 'CA', 'description': 'Congo Basin and Great Lakes'})
        reg_east, _ = Region.objects.get_or_create(name='East Africa', defaults={'code': 'EA', 'description': 'East African Community and Horn of Africa'})
        reg_south, _ = Region.objects.get_or_create(name='Southern Africa', defaults={'code': 'SA', 'description': 'SADC Region'})
        reg_north, _ = Region.objects.get_or_create(name='North Africa', defaults={'code': 'NA', 'description': 'Maghreb & North African Coast'})

        countries_data = [
            {
                'name': 'Democratic Republic of Congo', 'slug': 'drc', 'iso_code': 'COD', 'region': reg_central,
                'capital': 'Kinshasa', 'flag_emoji': '🇨🇩', 'gdp_nominal_usd': '$69.4 Billion', 'population': '102.3 Million',
                'strategic_resources': ['Cobalt (70% global reserves)', 'Copper', 'Coltan (60% global reserves)', 'Lithium', 'Hydroelectric Power (Inga)'],
                'sovereignty_notes': 'Enforcing national subsoil geological data repatriation and local refining quotas to dismantle predatory concession cartels.',
                'latitude': -4.0383, 'longitude': 21.7587, 'is_featured': True
            },
            {
                'name': 'Ghana', 'slug': 'ghana', 'iso_code': 'GHA', 'region': reg_west,
                'capital': 'Accra', 'flag_emoji': '🇬🇭', 'gdp_nominal_usd': '$76.3 Billion', 'population': '34.1 Million',
                'strategic_resources': ['Gold (Africa\'s top producer)', 'Bauxite', 'Cocoa', 'Lithium (Ewoyaa)'],
                'sovereignty_notes': 'Pioneering domestic London Bullion Market Association (LBMA) accredited gold refining and state-backed gold-for-oil barter frameworks.',
                'latitude': 7.9465, 'longitude': -1.0232, 'is_featured': True
            },
            {
                'name': 'Zimbabwe', 'slug': 'zimbabwe', 'iso_code': 'ZWE', 'region': reg_south,
                'capital': 'Harare', 'flag_emoji': '🇿🇼', 'gdp_nominal_usd': '$28.4 Billion', 'population': '16.3 Million',
                'strategic_resources': ['Lithium (Bikita / Arcadia)', 'Platinum Group Metals (PGMs)', 'Chrome', 'Nickel'],
                'sovereignty_notes': 'Instituted historic raw spodumene export bans to compel foreign conglomerates to construct in-country sulphate processing facilities.',
                'latitude': -19.0154, 'longitude': 29.1549, 'is_featured': True
            },
            {
                'name': 'Mali', 'slug': 'mali', 'iso_code': 'MLI', 'region': reg_west,
                'capital': 'Bamako', 'flag_emoji': '🇲🇱', 'gdp_nominal_usd': '$21.2 Billion', 'population': '23.3 Million',
                'strategic_resources': ['Gold (Loulo-Gounkoto)', 'Lithium (Goulamina)', 'Cotton', 'Solar Energy'],
                'sovereignty_notes': 'Core member of the Alliance of Sahel States (AES); overhauled national mining code ensuring 35% state and local ownership stakes.',
                'latitude': 17.5707, 'longitude': -3.9962, 'is_featured': True
            },
            {
                'name': 'Burkina Faso', 'slug': 'burkina-faso', 'iso_code': 'BFA', 'region': reg_west,
                'capital': 'Ouagadougou', 'flag_emoji': '🇧🇫', 'gdp_nominal_usd': '$20.8 Billion', 'population': '22.7 Million',
                'strategic_resources': ['Gold', 'Zinc', 'Cotton', 'Phosphate'],
                'sovereignty_notes': 'Constructed the nation\'s first national gold refinery in Ouagadougou and established a sovereign agricultural self-sufficiency drive.',
                'latitude': 12.2383, 'longitude': -1.5616, 'is_featured': True
            },
            {
                'name': 'Kenya', 'slug': 'kenya', 'iso_code': 'KEN', 'region': reg_east,
                'capital': 'Nairobi', 'flag_emoji': '🇰🇪', 'gdp_nominal_usd': '$112.8 Billion', 'population': '55.1 Million',
                'strategic_resources': ['Geothermal Energy (90% grid clean energy)', 'Titanium', 'Rare Earth Minerals (Mrima Hill)', 'Tea & Tech Corridor'],
                'sovereignty_notes': 'Building East Africa\'s first zero-carbon green smelting industrial park powered entirely by the Great Rift Valley geothermal reservoirs.',
                'latitude': -0.0236, 'longitude': 37.9062, 'is_featured': True
            },
            {
                'name': 'Ethiopia', 'slug': 'ethiopia', 'iso_code': 'ETH', 'region': reg_east,
                'capital': 'Addis Ababa', 'flag_emoji': '🇪🇹', 'gdp_nominal_usd': '$156.0 Billion', 'population': '126.5 Million',
                'strategic_resources': ['GERD Hydroelectric Megaproject (5,150 MW)', 'Potash', 'Gold', 'Coffee'],
                'sovereignty_notes': 'Asserting regional industrial dominance through cheap sovereign hydropower and domestic manufacturing self-reliance.',
                'latitude': 9.1450, 'longitude': 40.4897, 'is_featured': True
            },
            {
                'name': 'Niger', 'slug': 'niger', 'iso_code': 'NER', 'region': reg_west,
                'capital': 'Niamey', 'flag_emoji': '🇳🇪', 'gdp_nominal_usd': '$16.6 Billion', 'population': '27.2 Million',
                'strategic_resources': ['Uranium (Arlit / Imouraren)', 'Crude Oil (Agadem / Niger-Benin Pipeline)', 'Coal', 'Gold'],
                'sovereignty_notes': 'Reclaimed sovereign operational control over northern uranium concessions and inaugurated direct oil exports to global buyers.',
                'latitude': 17.6078, 'longitude': 8.0817, 'is_featured': True
            }
        ]

        country_map = {}
        for c in countries_data:
            obj, _ = Country.objects.update_or_create(slug=c['slug'], defaults=c)
            country_map[c['slug']] = obj

        # 4. CATEGORIES
        cat_data = [
            {'name': 'News', 'slug': 'news', 'order': 1, 'description': 'Fast, rigorously verified African and international developments.'},
            {'name': 'Africa', 'slug': 'africa', 'order': 2, 'description': 'Continental affairs, cross-border integration, and regional dynamics.'},
            {'name': 'Geopolitics', 'slug': 'geopolitics', 'order': 3, 'description': 'Multipolar diplomacy, alliances, state sovereignty, and international relations.'},
            {'name': 'Economy', 'slug': 'economy', 'order': 4, 'description': 'Macroeconomics, central banking, currency architecture, and continental trade.'},
            {'name': 'Resources', 'slug': 'resources', 'order': 5, 'description': 'Critical minerals, energy corridors, geology, and value-chain industrialisation.'},
            {'name': 'Technology', 'slug': 'technology', 'order': 6, 'description': 'Digital sovereignty, infrastructure, AI, renewable tech, and industrial patents.'},
            {'name': 'History', 'slug': 'history', 'order': 7, 'description': 'Pre-colonial institutions, archive scrutiny, anti-colonial struggles, and oral records.'},
            {'name': 'Society', 'slug': 'society', 'order': 8, 'description': 'Demographics, urban transformation, youth, labor, and cultural evolution.'},
            {'name': 'Security', 'slug': 'security', 'order': 9, 'description': 'Defence manufacturing, maritime security, border integrity, and intelligence.'},
            {'name': 'Analysis', 'slug': 'analysis', 'order': 10, 'description': 'Deep strategic interpretation and context-rich foresight.'},
            {'name': 'Video', 'slug': 'video', 'order': 11, 'description': 'Documentary cinema, 60-second context reels, and executive interviews.'},
        ]
        cat_map = {}
        for cat in cat_data:
            obj, _ = Category.objects.update_or_create(slug=cat['slug'], defaults=cat)
            cat_map[cat['slug']] = obj

        # 5. TOPICS
        topics_data = [
            {'name': 'AfCFTA & Free Trade', 'slug': 'afcfta', 'is_featured': True, 'icon_name': 'TrendingUp'},
            {'name': 'Critical Minerals & Value Addition', 'slug': 'critical-minerals', 'is_featured': True, 'icon_name': 'Cpu'},
            {'name': 'Alliance of Sahel States (AES)', 'slug': 'aes', 'is_featured': True, 'icon_name': 'Shield'},
            {'name': 'Geological Data Sovereignty', 'slug': 'geological-data', 'is_featured': True, 'icon_name': 'Database'},
            {'name': 'BRICS+ & Global South Finance', 'slug': 'brics', 'is_featured': True, 'icon_name': 'Globe'},
            {'name': 'Industrial Rail & Transport Corridors', 'slug': 'industrial-rail', 'is_featured': True, 'icon_name': 'Truck'},
            {'name': 'Pre-Colonial Metallurgy & Trade', 'slug': 'pre-colonial-history', 'is_featured': False, 'icon_name': 'BookOpen'},
        ]
        topic_map = {}
        for t in topics_data:
            obj, _ = Topic.objects.update_or_create(slug=t['slug'], defaults=t)
            topic_map[t['slug']] = obj

        # 6. SOURCE TYPES & SOURCES
        st_gov, _ = SourceType.objects.get_or_create(name='Official State / Ministry', defaults={'code': 'GOV_OFFICIAL', 'default_credibility_tier': 1})
        st_wire, _ = SourceType.objects.get_or_create(name='Licensed International Wire', defaults={'code': 'WIRE_AGENCY', 'default_credibility_tier': 2})
        st_acad, _ = SourceType.objects.get_or_create(name='Academic & Scientific Journal', defaults={'code': 'ACADEMIC', 'default_credibility_tier': 1})
        st_intl, _ = SourceType.objects.get_or_create(name='International Multilateral Institution', defaults={'code': 'INSTITUTION', 'default_credibility_tier': 1})

        src_brgm, _ = Source.objects.update_or_create(
            title='Inventory of Mineral Resources and Geophysical Surveys in Katanga and Kivu',
            publisher='Bureau de Recherches Géologiques et Minières (BRGM) & DRC Cadastre Minier',
            defaults={
                'url': 'https://example.org/reports/drc-cadastre-brgm-geophysical',
                'source_type': st_gov,
                'author': 'Dr. Jean-Luc Mbemba & BRGM Research Team',
                'publication_date': '2025-11-14',
                'reliability_notes': 'Primary geological dataset containing airborne magnetic and radiometric surveys across 14 concessions.',
            }
        )

        src_afcfta_sec, _ = Source.objects.update_or_create(
            title='Operationalizing Cross-Border Rules of Origin for Automotive and Steel Corridors',
            publisher='AfCFTA Secretariat, Accra Headquarters',
            defaults={
                'url': 'https://example.org/afcfta/reports/2026-rules-of-origin-industrial',
                'source_type': st_intl,
                'author': 'Trade & Industrial Tariff Committee',
                'publication_date': '2026-02-18',
                'reliability_notes': 'Official treaty implementation directives ratified by 47 state parties.',
            }
        )

        src_bma_ghana, _ = Source.objects.update_or_create(
            title='Royal Gold Ghana Refinery Technical Commissioning and LBMA Pre-Audit Report',
            publisher='Bank of Ghana & Minerals Income Investment Fund (MIIF)',
            defaults={
                'url': 'https://example.org/ghana/miif/royal-gold-refinery-audit',
                'source_type': st_gov,
                'author': 'Chief Assayer & Governor\'s Working Group',
                'publication_date': '2026-01-20',
                'reliability_notes': 'Audit of 400kg/day 99.99% purity gold assaying capabilities in Accra.',
            }
        )

        # 7. ARTICLES & DETAILED EDITORIAL PIECES
        now = timezone.now()

        # Story 1: DRC Geological Data Sovereignty (Dominant Lead Analysis)
        art_drc, _ = Article.objects.update_or_create(
            slug='beyond-raw-extraction-drc-reclaims-geological-data-sovereignty',
            defaults={
                'title': 'Beyond Raw Extraction: Why Kinshasa is Reclaiming Control Over Its Subsoil Mapping Data',
                'short_title': 'DRC Reclaims Geological Data Rights',
                'subtitle': 'For decades, European and Asian mining houses kept proprietary seismic and geological surveys in offshore vaults. A new sovereign directive forces the digital repatriation of all Congolese mineral data.',
                'summary': 'The Democratic Republic of Congo has enacted landmark legislation requiring all mining concessionaires to deposit full-spectrum geophysical, geochemical, and 3D subsoil scans into a sovereign national geological data bank in Kinshasa.',
                'content_type': Article.ContentType.ANALYSIS,
                'status': Article.Status.PUBLISHED,
                'body': """### The Architecture of Informational Asymmetry

For more than seven decades, the most valuable asset in the Congolese mining corridor was not the physical cobalt leaving Kolwezi or the coltan hauled from Rubaya—it was the map.

While public debate consistently focuses on royalty tax rates and export duties, the real leverage in international mining finance has always lived in the **proprietary geophysical surveys** commissioned by multinational mining houses. These airborne electromagnetic surveys, hyperspectral satellite scans, and core-sample assays were routinely exported to servers in Brussels, London, Toronto, and Beijing, without unredacted copies ever residing in the archives of the Congolese Ministry of Mines.

```
THE INFORMATIONAL EXTRACTIVE CYCLE:
Concession Awarded -> Foreign Geological Scan Conducted -> Data Kept Offshore -> Concession Under-Valued at Renegotiation
```

### The New Kinshasa Directive: Sovereign Data Repatriation

Under Ministerial Decree No. 0482 enacted this quarter, the Congolese government has instituted a non-negotiable compliance framework:

1. **Mandatory National Deposit:** Every operational concession holder must transmit complete, uncompressed raw geophysical and seismic datasets to the *Service Géologique National du Congo* (SGNC) within 90 days.
2. **End of Offshore Exclusivity:** Geological data generated within Congolese territorial borders is classified as **sovereign state property**. Concessionaires maintain commercial operating rights, but cannot legally withhold subsoil modeling from state planners.
3. **Establishment of the Kinshasa Supercomputing Cluster:** A state-backed high-performance computing data center is being deployed in Kinshasa to run autonomous AI subsoil inversion models, ending reliance on overseas geological consulting firms.

### Why This Changes Mineral Negotiations

When an African state enters contract negotiations without knowing the true geometry, grade, and boundary of an ore body, it negotiates blind. 

As noted in the 2025 BRGM-Cadastre collaborative audit, prior concession valuations were routinely calculated using outdated 1968 Belgian colonial surveys, even after modern satellite radar had detected multi-billion-dollar cobalt and lithium anomalies deeper in the stratigraphy.

With sovereign access to its own digital subsoil maps, Kinshasa can accurately price auction blocks, forecast state revenues over 30-year horizons, and mandate genuine domestic value addition rather than accepting token royalty checks.
""",
                'structured_blocks': [
                    {
                        'type': 'key_facts',
                        'title': 'Key Facts: The DRC Sovereign Data Law',
                        'items': [
                            'Over 14,000 km² of high-resolution magnetic survey data was previously held outside the African continent.',
                            'Under Decree 0482, non-compliant mining houses face immediate license suspension within 90 days.',
                            'The newly formed SGNC data bank will be open to domestic research universities and African geological institutions.'
                        ]
                    },
                    {
                        'type': 'pull_quote',
                        'quote': 'You cannot have resource sovereignty if a foreign board of directors understands your subsoil better than your own Ministry of Mines.',
                        'author': 'Dr. Jean-Luc Mbemba, Senior Advisor to the Congolese Mining Commission'
                    }
                ],
                'hero_image_url': 'https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=1200&q=80',
                'hero_caption': 'An open-pit cobalt-copper extraction site in the Katanga crescent, where new digital telemetry systems are being integrated with national data banks.',
                'hero_credit': 'KKEVO Studio Media / Field Photo by Kwame Mensah',
                'category': cat_map['resources'],
                'region': reg_central,
                'country': country_map['drc'],
                'published_at': now - timezone.timedelta(hours=4),
                'is_featured': True,
                'is_breaking': False,
                'views_count': 1420,
            }
        )
        art_drc.authors.set([author_kwame])
        art_drc.topics.set([topic_map['critical-minerals'], topic_map['geological-data']])

        # Citations & Claims for Story 1
        Citation.objects.get_or_create(
            article=art_drc,
            citation_number=1,
            defaults={
                'source': src_brgm,
                'quote_excerpt': 'Over 82% of deep-crust radiometric surveys conducted between 2004 and 2022 remained stored on off-site servers with no public registry in Kinshasa.',
                'public_label': 'Section 3.2, BRGM-Cadastre Joint Mineral Audit',
            }
        )

        Claim.objects.get_or_create(
            article=art_drc,
            claim_text='More than 14,000 km² of mineral mapping data was historically retained exclusively in foreign corporate registries.',
            defaults={
                'verification_status': Claim.VerificationStatus.VERIFIED_FACT,
                'verification_notes': 'Audited against public concession registries and ministerial filings in Kolwezi and Kinshasa.',
                'primary_source': src_brgm,
            }
        )

        Claim.objects.get_or_create(
            article=art_drc,
            claim_text='Ministerial Decree 0482 mandates license forfeiture for operators who do not submit raw survey files within 90 days.',
            defaults={
                'verification_status': Claim.VerificationStatus.OFFICIAL_CLAIM,
                'verification_notes': 'Official text published in the Congolese Journal Officiel, March 2026.',
                'primary_source': src_brgm,
            }
        )

        # Story 2: AfCFTA Rail Integration (Secondary Lead)
        art_rail, _ = Article.objects.update_or_create(
            slug='trans-african-rail-corridors-the-real-mechanics-of-continental-free-trade',
            defaults={
                'title': 'Connecting the Atlantic to the Indian Ocean: The Trans-African Rail Corridor and the Real Mechanics of Free Trade',
                'short_title': 'The Trans-African Rail Industrial Corridor',
                'subtitle': 'Tariff reductions under AfCFTA mean little without heavy gauge rail to move containerized goods between regional economic communities. Inside the cross-border logistical integration.',
                'summary': 'An analytical breakdown of the Lobito Corridor expansion, standard gauge rail linkages from Mombasa into Central Africa, and how unified customs protocols are finally bypassing maritime chokepoints.',
                'content_type': Article.ContentType.ANALYSIS,
                'status': Article.Status.PUBLISHED,
                'body': """### Beyond the Tariff Myth

The conventional critique of intra-African trade often cites high border duties. Yet the true structural impediment has always been logistical: it has historically been cheaper and faster to ship a container of manufactured goods from Shanghai to Lagos than from Douala to Tema.

Under the accelerated AfCFTA industrial blueprint ratified in Accra, cross-continental freight is being systematically re-engineered around three primary rail spines:

- **The Atlantic-Indian Transversal:** Linking Angola's Port of Lobito through the DRC copperbelt into Tanzania's Dar es Salaam port.
- **The West African Sahelian Loop:** Bypassing coastal transshipment delays through modernized railheads in Abidjan, Ouagadougou, and Niamey.
- **The Northern Corridor SGR:** Expanding Kenya's high-speed standard gauge line toward Kampala and the Kivu trade nexus.

### The Industrial Multiplier Effect

When heavy mineral trains return from ports toward the continental interior, they create unprecedented freight capacity for intra-African manufactured goods—fertilizers from Morocco, refined steel from South Africa, and electrical transformers from Egypt.
""",
                'hero_image_url': 'https://images.unsplash.com/photo-1541888946425-d0fbb18086f6?auto=format&fit=crop&w=1200&q=80',
                'hero_caption': 'Heavy freight train navigating the Central African mineral logistics corridor.',
                'hero_credit': 'KKEVO Studio Media Archive / African Infrastructure Consortium',
                'category': cat_map['economy'],
                'region': reg_central,
                'country': country_map['drc'],
                'published_at': now - timezone.timedelta(hours=8),
                'is_featured': False,
                'is_breaking': False,
                'views_count': 980,
            }
        )
        art_rail.authors.set([author_amara])
        art_rail.topics.set([topic_map['afcfta'], topic_map['industrial-rail']])

        # Story 3: Ghana Local Gold Refining (Resources & Value Chain)
        art_ghana, _ = Article.objects.update_or_create(
            slug='ending-100-years-of-exporting-dore-inside-ghanas-gold-refining-drive',
            defaults={
                'title': 'Ending 100 Years of Exporting Dore: Inside Ghana’s Drive for LBMA-Accredited Domestic Refineries',
                'short_title': 'Ghana\'s Domestic Gold Refining Revolution',
                'subtitle': 'Africa’s largest gold producer moves from raw bullion exporter to sovereign assayer, demanding 100% in-country refinement of all artisanal and small-scale output.',
                'summary': 'Ghana’s Royal Gold Refinery in Accra undergoes its critical international accreditation audit. How domestic smelting safeguards central bank reserves and curbs illicit bullion flight.',
                'content_type': Article.ContentType.NEWS,
                'status': Article.Status.PUBLISHED,
                'body': """### Breaking Colonial Refinery Monopolies

For over a century, gold mined in the Ashanti and Western regions of Ghana departed Kotoka International Airport in unrefined dore bars—80% to 90% purity—bound for smelters in Switzerland, South Africa, and Dubai.

With the commissioning of state-of-the-art assaying facilities in Accra capable of producing 99.99% 'four nines' certified bullion, the Bank of Ghana has implemented its historic 'Gold Purchase Program', buying directly from local miners in Ghanaian Cedis.

This policy has doubled the central bank's foreign exchange buffer while neutralizing foreign currency volatility during sovereign debt restructuring.""",
                'hero_image_url': 'https://images.unsplash.com/photo-1610375461246-83df859d849d?auto=format&fit=crop&w=1200&q=80',
                'hero_caption': 'High-purity refined gold bullion bars stacked at a state-supervised assay facility in Accra.',
                'hero_credit': 'KKEVO Studio Media / Minerals Commission of Ghana',
                'category': cat_map['resources'],
                'region': reg_west,
                'country': country_map['ghana'],
                'published_at': now - timezone.timedelta(hours=14),
                'is_featured': False,
                'is_breaking': False,
                'views_count': 1120,
            }
        )
        art_ghana.authors.set([author_kwame])
        art_ghana.topics.set([topic_map['critical-minerals'], topic_map['brics']])

        # Story 4: Zimbabwe Lithium Value Chain (Technology & Industrial Policy)
        art_zim, _ = Article.objects.update_or_create(
            slug='from-raw-spodumene-to-cathodes-zimbabwes-lithium-processing-mandate',
            defaults={
                'title': 'From Raw Spodumene to Cathode Precursors: The Reality of Southern Africa’s Lithium Value Chain',
                'short_title': 'Zimbabwe Lithium Retention Mandate',
                'subtitle': 'Two years after outlawing raw mineral exports, Harare’s battery chemical parks are testing whether African resource producers can force global automakers to relocate downstream manufacturing.',
                'summary': 'An on-the-ground investigation into the Bikita, Arcadia, and Zulu lithium projects, assessing environmental governance, domestic beneficiation, and technological transfer.',
                'content_type': Article.ContentType.EXPLAINER,
                'status': Article.Status.PUBLISHED,
                'body': """### The Critical Mineral Ban: Two Years In

In late 2022, Zimbabwe took an audacious step that shocked international battery commodity desks: an outright prohibition on the export of raw lithium ore.

The message to mining conglomerates was unambiguous: **Invest in domestic processing plants or leave the mineral in the ground.**

```
VALUE ADDITION MULTIPLIER:
Raw Spodumene Ore ($150 - $400 / ton) -> Lithium Concentrate 6% ($900 / ton) -> Battery Grade Lithium Carbonate ($14,000 / ton)
```

Today, the Bikita and Arcadia processing plants are operational, churning out petalite and spodumene concentrates on domestic soil. But the next frontier—synthesizing cathode precursor chemicals—requires massive baseload power and precision chemical engineering.""",
                'hero_image_url': 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80',
                'hero_caption': 'Advanced processing equipment at a greenfield mineral beneficiation plant in Goromonzi, Zimbabwe.',
                'hero_credit': 'KKEVO Studio Media / Tariq Zuma',
                'category': cat_map['technology'],
                'region': reg_south,
                'country': country_map['zimbabwe'],
                'published_at': now - timezone.timedelta(hours=22),
                'is_featured': False,
                'is_breaking': False,
                'views_count': 840,
            }
        )
        art_zim.authors.set([author_kwame])
        art_zim.topics.set([topic_map['critical-minerals']])

        # Story 5: Pre-Colonial Sahel History Explainer
        art_hist, _ = Article.objects.update_or_create(
            slug='the-14th-century-currency-unions-of-the-sahel-and-precolonial-metallurgy',
            defaults={
                'title': 'The 14th-Century Currency Unions of the Sahel: Pre-Colonial Metallurgical Industry and Fiscal Networks',
                'short_title': 'Pre-Colonial Sahelian Currency Unions',
                'subtitle': 'Centuries before European central banking, West African kingdoms coordinated complex currency systems based on copper ingots, gold dinars, and standardized iron rods.',
                'summary': 'Historical analysis of the fiscal and technological sovereignty of the Mali and Songhai empires, and what modern African monetary architects can learn from pre-colonial commercial integration.',
                'content_type': Article.ContentType.HISTORY,
                'status': Article.Status.PUBLISHED,
                'body': """### The Industrial Foundation of Sahelian Statehood

Modern accounts of medieval West Africa frequently reduce the Sahelian empires to trade intermediaries exchanging gold for Saharan salt. 

This view obscures the profound **domestic metallurgical industries** that underpinned state authority in Timbuktu, Gao, and Djenné. Archeological excavations at Mema and the Inland Niger Delta demonstrate that sophisticated blast-furnace iron smelting was active continuously from the 4th century BCE through the 16th century CE.

### Standardized Monetary Systems

The Mali Empire did not operate on primitive barter. It maintained a multi-tiered currency system:
- **Mithqal of Gold:** Used for trans-Saharan diplomacy, major real estate transactions, and imperial tributes.
- **Copper Rods and Ingots:** Produced in the Takedda mines (modern-day Niger) and utilized for inter-regional wholesale commodities.
- **Cowrie Currency Units:** Used for high-velocity local retail commerce, strictly regulated in exchange parity by imperial market overseers (*Muhtasib*).
""",
                'hero_image_url': 'https://images.unsplash.com/photo-1599707367072-cd6ada2bc375?auto=format&fit=crop&w=1200&q=80',
                'hero_caption': 'Historical mud-brick architectural arches and manuscripts preservation in Djenné, Mali.',
                'hero_credit': 'Archival Documentation / African Historiography Project',
                'category': cat_map['history'],
                'region': reg_west,
                'country': country_map['mali'],
                'published_at': now - timezone.timedelta(days=2),
                'is_featured': False,
                'is_breaking': False,
                'views_count': 1650,
            }
        )
        art_hist.authors.set([author_aminata])
        art_hist.topics.set([topic_map['pre-colonial-history'], topic_map['aes']])

        # Story 6: Alliance of Sahel States (AES) Economic Architecture
        art_aes, _ = Article.objects.update_or_create(
            slug='inside-the-aes-confederation-sovereign-reserves-and-cross-border-energy',
            defaults={
                'title': 'Sovereign Reserves and Cross-Border Energy: Inside the Mali-Niger-Burkina Faso Confederation',
                'short_title': 'Inside the AES Economic Confederation',
                'subtitle': 'The Alliance of Sahel States moves beyond military coordination to establish joint investment banks, shared satellite communication, and unified gold reserves.',
                'summary': 'How the confederation between Bamako, Niamey, and Ouagadougou is redrawing geopolitical alliances in West Africa and establishing alternative financial clearing structures.',
                'content_type': Article.ContentType.ANALYSIS,
                'status': Article.Status.PUBLISHED,
                'body': """### A Structural Break with Post-Colonial Architecture

When Mali, Niger, and Burkina Faso formed the *Alliance des États du Sahel* (AES), international commentators focused predominantly on mutual defence pacts.

However, the most consequential transformations are occurring across **fiscal and economic domains**:

1. **The AES Investment Bank:** Formally seeded to finance cross-border infrastructure, including a 1,200 km high-voltage transmission line connecting Niger's Kandadji dam to the Malian electrical grid.
2. **Unified Mining Codes:** Harmonized regulations ensuring that all three states require minimum 30% state equity participation in new resource concessions.
3. **Direct Bilateral Energy Swaps:** Niger crude oil refined in Zinder is now piped directly to power generation facilities in Burkina Faso and Mali, bypassing coastal currency surcharges.
""",
                'hero_image_url': 'https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?auto=format&fit=crop&w=1200&q=80',
                'hero_caption': 'High-level ministerial delegation at the Sahelian Regional Economic Council.',
                'hero_credit': 'KKEVO Studio Media / Field Bureau',
                'category': cat_map['geopolitics'],
                'region': reg_west,
                'country': country_map['mali'],
                'published_at': now - timezone.timedelta(hours=36),
                'is_featured': False,
                'is_breaking': False,
                'views_count': 1890,
            }
        )
        art_aes.authors.set([author_amara])
        art_aes.topics.set([topic_map['aes'], topic_map['brics']])

        # Sample Correction for Transparency Demonstration
        Correction.objects.get_or_create(
            article=art_ghana,
            title='Correction: Gold Production Tonnage Estimates in Ashanti Belt',
            defaults={
                'original_claim': 'Ghana produced 145 metric tons of gold in the previous calendar year.',
                'corrected_claim': 'Ghana produced 128.5 metric tons of commercial gold, with artisanal output estimated between 35 and 40 metric tons by the Minerals Commission.',
                'reason_for_correction': 'Official figures updated following reconciled Q4 data from the Bank of Ghana and Ghana Chamber of Mines.',
                'corrected_by': editor_user,
                'is_public_banner_active': True,
            }
        )

        # 8. BREAKING NEWS ALERT
        BreakingAlert.objects.update_or_create(
            headline='DRC and Angola Sign Historic Bilateral Treaty on Joint Maritime Crude & Mineral Exploration Zone',
            defaults={
                'target_url': '/article/beyond-raw-extraction-drc-reclaims-geological-data-sovereignty',
                'priority': 5,
                'is_active': True,
            }
        )

        # 9. VIDEO STORIES
        VideoStory.objects.update_or_create(
            slug='60-seconds-of-context-who-controls-the-katanga-copperbelt',
            defaults={
                'title': '60 Seconds of Context: Who Really Controls the Katanga Mineral Crescent?',
                'summary': 'A fast-paced geopolitical breakdown of concession ownership, sovereign data rights, and export corridors across Central Africa.',
                'video_type': VideoStory.VideoType.SHORT_REEL,
                'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4',
                'thumbnail_url': 'https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?auto=format&fit=crop&w=600&q=80',
                'duration_seconds': 64,
                'transcript': 'Behind the headlines of the clean energy transition lies a single geographic strip spanning southern DRC and northern Zambia. Here is how ownership is shifting from foreign concession cartels to sovereign African control.',
                'is_featured': True,
                'related_article': art_drc,
            }
        )

        VideoStory.objects.update_or_create(
            slug='the-lithium-corridor-inside-zimbabwes-processing-plants',
            defaults={
                'title': 'The Lithium Corridor: Inside Zimbabwe’s In-Country Processing Plants',
                'summary': 'Documentary feature investigating how Southern African miners are adapting to the ban on raw spodumene exports.',
                'video_type': VideoStory.VideoType.EXPLAINER,
                'video_url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4',
                'thumbnail_url': 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=80',
                'duration_seconds': 480,
                'transcript': 'From the pit in Bikita to the chemical kilns in Goromonzi, we track the reality of building a domestic battery supply chain on the African continent.',
                'is_featured': False,
                'related_article': art_zim,
            }
        )

        # 10. NEWSLETTER SUBSCRIBERS
        NewsletterSubscriber.objects.get_or_create(
            email='subscriber.briefing@kkevostudiomedia.com',
            defaults={
                'is_active': True,
                'is_verified': True,
                'preferences': {
                    'daily_briefing': True,
                    'geopolitics': True,
                    'critical_minerals': True,
                }
            }
        )

        self.stdout.write(self.style.SUCCESS("==> KKEVO STUDIO MEDIA Database Successfully Seeded!"))
        self.stdout.write(self.style.SUCCESS(f"    - Articles: {Article.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"    - Countries: {Country.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"    - Categories: {Category.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"    - Sources & Claims: {Source.objects.count()} sources, {Claim.objects.count()} claims"))
        self.stdout.write(self.style.SUCCESS(f"    - Videos: {VideoStory.objects.count()}"))
