<div align="center">

# Web Scrapers

<strong>366 ready-to-run web scrapers, each with a Python example, a cURL call and sample output.</strong>

![Scrapers](https://img.shields.io/badge/scrapers-366-blue?style=flat-square) ![Examples](https://img.shields.io/badge/examples-MIT-lightgrey?style=flat-square)

</div>

Every folder in [`actors/`](actors) is one scraper: what it does, how to call it, its inputs, and the shape of its output.
All of them run on [Apify](https://apify.com/abotapi?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo), so there are no servers or proxies to manage.
Sample files are mock data with the real field structure.

## Quick start

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>
python actors/coupang-scraper/example.py
```

## Scrapers by category

[Real Estate](#real-estate) (76) · [Jobs](#jobs) (42) · [Travel](#travel) (12) · [Social Media](#social-media) (19) · [Video](#video) (1) · [News & Sports](#news--sports) (2) · [AI & LLM](#ai--llm) (4) · [SEO & Search](#seo--search) (3) · [Leads & Directories](#leads--directories) (19) · [E-commerce](#e-commerce) (97) · [More](#more) (91)

### Real Estate

| Scraper | What it does |
| --- | --- |
| [Avito.ru Scraper](actors/avito-ru-scraper) | Scrape structured listings from Avito.ru by region, category, filters, or direct URL. Automatically paginate through… |
| [BizBuySell Scraper](actors/bizbuysell-scraper) | Extract business-for-sale and franchise listings from bizbuysell.com with financials, full descriptions, photos, and… |
| [Real Estate AU Scraper](actors/realestate-au-scraper) | Extract detailed Australian real estate property listings with 30+ structured fields, including price, description,… |
| [SeLoger Scraper](actors/seloger-france-scraper) | Scrape SeLoger.com properties for sale and rent. Search by location with price, room and property type filters.… |
| [Bayut.com Scraper](actors/bayut-com-scraper) | Scrape Bayut.com property listings with prices, beds, baths, area, GPS, agent and agency details, phone, WhatsApp,… |
| [Commercial Property AU Scraper](actors/realcommercial-au-scraper) | Scrape Australian commercial property listings with full detail data. Extract descriptions, highlights, property… |
| [PropertyGuru SG Scraper](actors/propertyguru-sg-scraper) | Scrape PropertyGuru.com.sg sale and rental listings with 30+ structured fields, including price, PSF, floor area,… |
| [Housing.com Scraper](actors/housing-com-scraper) | Scrape residential property listings from Housing.com across 750+ cities. Extract structured data for properties… |
| [Cian RU Scraper](actors/cian-ru-scraper) | Collect property listings from Cian.ru by search filters or direct URLs. Returns structured rows with listing URL,… |
| [Domain.com.au Scraper](actors/domain-com-au-scraper) | Extract enriched Domain.com.au property listings across buy, rent, and sold, with AI-enhanced content and deep… |
| [Trade Me NZ Scraper](actors/trademe-co-nz-scraper) | Scrape trademe.co.nz across all five sections: Marketplace goods and auctions, Property, Motors, Jobs and Services.… |
| [2GIS Scraper](actors/2gis-places-scraper) | Extract business and place data from 2GIS.com at scale. Get names, addresses, phones, emails, websites, social… |
| [StreetEasy Scraper](actors/streeteasy-scraper) | Scrape StreetEasy sales, rentals and in-contract listings across NYC and Jersey City. Search with filters or URLs… |
| [Real Estate AU Agents Scraper](actors/au-property-agents-scraper) | Scrape Australian real estate agent and agency profiles by suburb or profile URLs. Returns names, roles, agencies,… |
| [DDproperty Thailand Scraper](actors/ddproperty-scraper) | Scrape DDproperty.com Thailand listings at scale. Extract prices, property features, images, agent contacts, GPS… |
| [Batdongsan.com.vn Scraper](actors/batdongsan-com-vn-scraper) | Scrape Batdongsan.com.vn property listings into clean JSON. Search by listing type, property category, city, or… |
| [Housesigma Scraper](actors/housesigma-com) | Scrape housesigma.com listings across Ontario, BC, and Alberta. Search by city or paste URLs to extract prices,… |
| [Houzz Pro Scraper](actors/houzz-scraper) | Pull Houzz pro listings across global sites. Search by category and location, keyword, or URL, plus review mode for… |
| [LoopNet Scraper](actors/loopnet-scraper) | Scrape LoopNet commercial listings across the US, including office, retail, industrial, multifamily, land and… |
| [Rumah123 Scraper](actors/rumah123-indonesia-property-scraper) | Pull structured property listings from Rumah123.com, Indonesia’s largest property portal. Search by location with… |
| [Crexi Scraper](actors/crexi-commercial-listings-scraper) | Scrape crexi.com commercial listings: asking price, cap rate, square footage, units, year built, lot size, APN,… |
| [Dubizzle.com Scraper](actors/dubizzle-com-scraper) | Scrape dubizzle.com across the UAE for property, motors, and agent listings. Search by filters or URLs with auto… |
| [Homes.co.nz Scraper](actors/homes-co-nz-scraper) | Scrape Homes.co.nz listings by location or URL with pagination. Extract property details, valuations, agents, branch… |
| [NewHomeSource Scraper](actors/newhomesource-scraper) | Scrape new homes, floor plans, builders and communities from NewHomeSource.com. Search by US state or city, or paste… |
| [Pap.fr Scraper](actors/pap-fr-scraper) | Extract property listings from pap.fr. Get fully-detailed listings with price, address, rooms, area, photo gallery,… |
| [Realtor.ca Scraper](actors/realtor-ca-scraper) | Scrape Realtor.ca property listings with prices, descriptions, images, agent and brokerage details, coordinates,… |
| [Zap Imóveis Scraper](actors/zapimoveis-scraper) | Scrape Zap Imóveis sale, rental and new-development listings by city, filters or URL. Extract 80+ fields including… |
| [Auction.com Scraper](actors/auction-com-scraper) | Extract foreclosure, REO, short-sale, and auction listings from Auction.com in minutes. Search by location and… |
| [CommercialGuru SG Property Listings & Agent Contacts Scraper](actors/commercialguru-sg-scraper) | Scrape commercialguru.com.sg Singapore listings at scale. Extract prices, PSF, floor area, tenure, property type,… |
| [Hipflat Scraper](actors/hipflat-scraper) | Scrape hipflat.co.th property listings and new-project data across Thailand: price, price per m², beds, baths, area,… |
| [ImmobilienScout24.de Scraper](actors/immoscout24-scraper) | $0.9💰/1K for Gold discount. Extract property listings from immobilienscout24.de, Germany's #1 real estate platform… |
| [Otodom.pl Scraper](actors/otodom-pl-scraper) | Scrape Otodom.pl properties for sale and rent, including apartments, houses, plots, commercial spaces, garages,… |
| [Subito.it Scraper](actors/subito-it-scraper) | Scrape Subito.it listings across cars, real estate, marketplace, jobs, and more. Search by keyword and filters or… |
| [591.com.tw Scraper](actors/591-com-tw-scraper) | Extract property listings from 591房屋交易網 591.com.tw, Taiwan’s largest real estate marketplace. Search by city or use… |
| [Funda in Business Scraper](actors/fundainbusiness-nl-commercial-property-scraper) | Scrape Funda in Business commercial listings: offices, retail, industrial, catering and more. Full detail pages,… |
| [Google Maps Scraper](actors/google-maps-scraper) | Extract business data from Google Maps at scale. Get names, addresses, phone numbers, websites, ratings, reviews,… |
| [Immoweb.be Scraper](actors/immoweb-scraper) | Extract property listings from immoweb.be. Get price, location, coordinates, images, and 27 structured fields per… |
| [Immowelt.de Scraper](actors/immowelt-de-scraper) | Scrape detailed property listings from Immowelt.de into clean structured data. Extract prices, GPS coordinates,… |
| [Lennar Homes Scraper](actors/lennar-scraper) | Scrape Lennar new-home communities, move-in-ready homes and floor plans. Extract prices, monthly payment breakdowns,… |
| [Mudah.my Cars Scraper](actors/mudah-my-scraper) | Scrape Mudah.my listings across every category: cars, motorcycles, property, mobiles, electronics, home, hobbies,… |
| [Property Finder UAE Scraper](actors/propertyfinder-ae-scraper) | Scrape PropertyFinder.ae listings at scale. Extract prices, property details, images, amenities, coordinates, agent… |
| [Tutti.ch Scraper](actors/tutti-ch-scraper) | Scrape listings from tutti.ch across all 23 categories, including vehicles, property, electronics, furniture,… |
| [Apartments.com Scraper](actors/apartments-com-scraper) | Scrape Apartments.com rentals by city, ZIP, neighborhood, address or URL. Extract rent, floorplans, available units,… |
| [BizQuest Scraper](actors/bizquest-scraper) | Extract business-for-sale, franchise, and asset listings from BizQuest. Search by category, US state, asking price,… |
| [BusinessesForSale.com Scraper](actors/businessesforsale-com-scraper) | Extract businesses and franchises listed for sale on BusinessesForSale.com. Search by keywords, country, price,… |
| [Domclick RU Property Scraper](actors/domclick-scraper) | Extract property listings from domclick.ru, one of Russia’s largest real estate portals. Search by city or use… |
| [Dot Property Scraper](actors/dotproperty-com-ph-scraper) | Scrape Philippines property listings from dotproperty.com.ph and lamudi.com.ph with exact map-pin coordinates,… |
| [DR Horton Scraper](actors/drhorton-scraper) | Extract new-home data from drhorton.com, America’s largest homebuilder. Pull communities and quick move-in homes by… |
| [Fuel Prices AU Scraper](actors/fuel-prices-anz-scraper) | Scrapes petrol and fuel prices data across Australia and New Zealand. Search by address or coordinates to find… |
| [Gumtree UK Scraper](actors/gumtree-uk-scraper) | Scrape gumtree.com classifieds across motors, property, jobs, services, pets and goods for sale. Extract titles,… |
| [Homely.com.au Scraper](actors/homely-com-au-scraper) | Scrape Homely.com.au properties for sale, rent, and sold, plus agent finder, suburb reviews, ratings, and Q&A.… |
| [iProperty MY Scraper](actors/iproperty-com-my-scraper) | Scrape property listings from iProperty.com.my for sale or rent: price, PSF, bedrooms, bathrooms, floor area,… |
| [Kijiji.ca Scraper](actors/kijiji-scraper) | Scrape Kijiji.ca listings across property, vehicles, jobs, electronics, furniture, services, and more. Search by… |
| [OnTheMarket Scraper](actors/onthemarket-scraper) | Scrape onthemarket.com for-sale, to-rent and new-homes listings with 85+ fields: price, address & geo,… |
| [AU Residential Property Scraper](actors/property-au-scraper) | Scrape Australian property listings with rich detail-page enrichment. Each listing record comes back with far more… |
| [RealestateCo NZ Scraper](actors/realestate-co-nz-scraper) | Search and extract all real estate properties for sale, rent, and sold across New Zealand from realestate.co.nz. |
| [Realtor.com Scraper](actors/realtor-com-scraper) | Extract property listings from realtor.com. Get comprehensive data, including prices, property details, agent… |
| [Redfin Scraper](actors/redfin-scraper) | Scrape redfin.com home listings: price, beds, baths, sqft, lot, year built, coordinates, address, MLS, status, days… |
| [Rent.com Scraper](actors/rent-com-scraper) | Extract rental listings from rent.com. Get comprehensive data including monthly rent ranges, full address with GPS,… |
| [Rightmove Scraper](actors/rightmove-scraper) | Fast, reliable Rightmove.co.uk scraper for sale, rent, and sold-price listings. Search by location or direct URL and… |
| [Willhaben.at Scraper](actors/willhaben-at-scraper) | Scrape Willhaben.at listings into clean JSON with 40+ structured fields, including prices, GPS coordinates, photos,… |
| [Fotocasa.es Scraper](actors/fotocasa-es-scraper) | Scrape Spain property listings from fotocasa.es. Get price, surface, rooms, baths, address, GPS, agency, phone,… |
| [Idealista Scraper](actors/idealista-scraper) | Scrape Idealista properties across Spain, Italy, and Portugal. Extract 35+ fields including prices, sizes, rooms,… |
| [Immobiliare.it Scraper](actors/immobiliare-it-scraper) | Extract property listings from Immobiliare.it with clean structured data including prices, descriptions, GPS… |
| [Jitty Scraper](actors/jitty-uk-scraper) | Scrape residential property listings from Jitty.com across the UK. Search with 20+ property filters, including AI… |
| [LandWatch Scraper](actors/landwatch-scraper) | Scrape land, farm, ranch, and rural property listings from LandWatch.com. Search by location, price, acreage… |
| [Leboncoin FR Scraper](actors/leboncoin-fr-scraper) | Pull public leboncoin.fr listings across cars, property, jobs, electronics, furniture, and 35+ categories. Returns… |
| [Properstar Scraper](actors/properstar-scraper) | Extract property listings from Properstar across global domains like .com, .co.uk, .ch, and .fr. Use search pages,… |
| [Property24 Scraper](actors/property24-scraper) | Extract structured property listings from Property24, South Africa’s largest property portal. Search by location or… |
| [PropertyGuru MY Scraper](actors/propertyguru-my-scraper) | Scrape PropertyGuru.com.my sale and rental listings with 30+ structured fields, including MYR price, built-up area,… |
| [QuintoAndar Scraper](actors/quintoandar-scraper) | Scrape QuintoAndar property listings across Brazil with 80+ fields, including rent, sale price, condo fees, IPTU,… |
| [REIWA Scraper](actors/reiwa-com-au-scraper) | Scrape REIWA.com.au across sale, rental, sold, commercial, business and rural properties. Search with filters or… |
| [Trulia Scraper](actors/trulia-scraper) | Scrape Trulia.com property listings by location, filters, or URL. Extract prices, beds, baths, square footage,… |
| [View.com.au Scraper](actors/view-com-au-scraper) | Scrape View.com.au properties for sale, rent and recently sold across Australia. Search by suburb, city, state or… |
| [Zonaprop Argentina Scraper](actors/zonaprop-scraper) | Scrape Zonaprop.com.ar property listings across Argentina. Extract 140+ fields including USD/ARS prices, price per… |
| [Zumper Scraper](actors/zumper-scraper) | Scrape Zumper.com rental listings: apartments, houses, condos and rooms. Pulls 60+ fields per listing, including… |

### Jobs

| Scraper | What it does |
| --- | --- |
| [HH.ru Jobs Scraper](actors/hh-ru-jobs-scraper) | Scrape HH.ru job listings with 50+ structured fields. Search by filters or URLs and extract salary, experience,… |
| [SEEK Jobs Scraper](actors/seek-scraper) | Scrape SEEK.com.au and SEEK.co.nz jobs by keyword, location, or filters. Extract full descriptions, companies,… |
| [Bayt.com Scraper](actors/bayt-com-jobs-scraper) | Scrape Bayt.com job listings by keyword, country, or URL. Extract structured data including job title, company,… |
| [JobStreet Scraper](actors/jobstreet-scraper) | Scrape JobStreet listings across Malaysia, Singapore, Indonesia, and the Philippines. Extract titles, companies,… |
| [Hiring.Cafe Jobs Scraper](actors/hiring-cafe-scraper) | Unlock powerful Hiring.Cafe job data extraction. Use advanced filters or URLs to get 100+ fields per job, including… |
| [CareerBuilder Scraper](actors/careerbuilder-scraper) | Scrape CareerBuilder.com job listings by search or URL. Returns title, company profile, location with coordinates,… |
| [NHS UK Scraper](actors/jobs-nhs-uk-scraper) | Scrape nhs.uk Jobs listings into a flat dataset. Extract 50+ fields, including pay band, salary, full description,… |
| [F6S Scraper](actors/f6s-directory-scraper) | Extract structured data from F6S.com. Scrape funding programs, startup accelerators, events, and jobs from a single… |
| [Gupy Jobs Scraper](actors/gupy-io-scraper) | Scrape public jobs from Gupy.io by keyword, state, city, workplace type, job type, company, PWD, and feedback badge.… |
| [JobTeaser Scraper](actors/jobteaser-scraper) | Scrape early-career jobs and internships from JobTeaser across Europe. Search with 15 filters or use JobTeaser URLs.… |
| [Workday Jobs Scraper](actors/myworkdayjobs-scraper) | Scrape job postings from any Workday-hosted careers site on Myworkdayjobs.com. Paste careers-page or job URLs and… |
| [Wellfound Jobs Scraper](actors/wellfound-jobs-scraper) | Scrape startup jobs from Wellfound.com by keyword, location, role, or remote status. Extract job details,… |
| [Caterer.com Scraper](actors/caterer-com-scraper) | Scrape UK hospitality jobs from Caterer.com, including chef, hotel, restaurant, bar, and events roles. Search by… |
| [Comparably Scraper](actors/comparably-scraper) | Extract rich company data from comparably.com using company names or profile URLs. Get ratings, culture scores, CEO… |
| [EdJoin.org Scraper](actors/edjoin-scraper) | Scrape EdJoin.org K-12 and higher-ed jobs by keyword, location, filters or URL. Extract districts, locations,… |
| [France Travail Scraper](actors/francetravail-fr-scraper) | Scrape job offers from France Travail with titles, companies, locations, salaries, contracts, descriptions, skills,… |
| [HiJobs.net Scraper](actors/hijobs-net-jobs-scraper) | Scrape hijobs.net job listings via the official mobile API: title, employer, salary range, location, hours, sector,… |
| [IrishJobs.ie Scraper](actors/irishjobs-ie) | Scrape job listings from IrishJobs.ie by keyword, location, job type, salary, recency, or search URL. Extract… |
| [Jobs.cz Scraper](actors/jobs-cz-scraper) | Scrape Czech job listings from Jobs.cz. Search builder (keyword, location, field, salary, employment type) or paste… |
| [JobStreet Scraper](actors/jobstreet-companies-reviews-scraper) | Pull JobStreet company profiles and employee reviews across Malaysia, Singapore, Indonesia, and the Philippines.… |
| [Monster Jobs Scraper](actors/monster-com) | Scrape Monster.com job listings from search and direct job URLs. Extract full descriptions, salaries, companies,… |
| [NoFluffJobs Scraper](actors/nofluffjobs-scraper) | Scrape NoFluffJobs IT jobs across Poland, Czechia, Slovakia, Hungary and the Netherlands. Search with filters or… |
| [Reed.co.uk Scraper](actors/reed-co-uk-scraper) | Scrape Reed.co.uk jobs, companies, courses and reviews by keyword, location, filters or URL. Extract 80+ fields… |
| [s1jobs Scraper](actors/s1jobs-com-scraper) | Scrape jobs from s1jobs.com across Scotland and the UK. Search by keyword, location, or URLs. Returns title, parsed… |
| [SEEK Company Reviews Scraper](actors/seek-companies-reviews-scraper) | Scrape SEEK Australia and New Zealand company profiles and employee reviews. Choose aggregated company data with top… |
| [SimplyHired Scraper](actors/simplyhired-com-scraper) | Pull active SimplyHired jobs across the US, UK, Canada, Australia, Ireland, and India. Search via builder or URL.… |
| [Superprof Scraper](actors/superprof-tutor-scraper) | Scrape Superprof tutors by subject and location, or paste tutor URLs. One rich record per tutor: name, photo, price,… |
| [Totaljobs Scraper](actors/totaljobs-com-scraper) | Scrape UK job listings from Totaljobs.com by keyword, location, filters, or URL. Extract 40+ fields including title,… |
| [Werk.nl Scraper](actors/werk-nl-scraper) | Scrape job vacancies from werk.nl, the official Dutch government job board by UWV. Uses werk.nl’s vacancy data… |
| [ZipRecruiter Scraper](actors/ziprecruiter-com-scraper) | Scrape ZipRecruiter jobs with titles, companies, salaries, locations, benefits, apply URLs and full descriptions.… |
| [BetaList Scraper](actors/betalist-com-scraper) | Scrape BetaList.com startup profiles with founder and contact enrichment. Extract startup names, taglines,… |
| [Cwjobs UK Scraper](actors/cwjobs-scraper) | Scrape tech and IT jobs from CWJobs.co.uk into clean, structured data. Search by keyword, location, salary, work… |
| [Dice.com Scraper](actors/dice-com-scraper) | Scrape tech job listings from Dice.com by keyword, filters, or URL. Extract job titles, companies, recruiter types,… |
| [FINN.no Jobs Scraper](actors/finn-no-jobs-scraper) | Scrape active FINN.no job listings by search filters or URL. Extract 30+ fields including full descriptions,… |
| [Jobsite UK Scraper](actors/jobsite-co-uk-scraper) | Collect UK job listings from Jobsite.co.uk at scale. Search by keyword, location, filters, or paste search URLs.… |
| [Jora Jobs Scraper](actors/jora-jobs-scraper) | Scrape Jora.com job listings across supported countries by keyword, filters, or URL. Extract full job descriptions,… |
| [NIJobs Scraper](actors/nijobs-scraper) | Scrape NIJobs.com listings across Northern Ireland by keyword, location, salary, posted date, or URL. Extract 60+… |
| [RemoteOK Jobs Scraper](actors/remoteok-com-scraper) | Scrape RemoteOK jobs by keyword or job URL. Extract title, company, location, remote details, tags, salary when… |
| [RepVue Scraper](actors/repvue-scraper) | Scrape RepVue company profiles, RepVue Score, sales-rep reviews, and compensation by role (OTE, base, percentiles)… |
| [StepStone.de Scraper](actors/stepstone-de) | Scrape StepStone.de jobs by keyword, location, filters, or URL. Extract 35+ fields including employer, logo,… |
| [ThomasNet Scraper](actors/thomasnet-supplier-scraper) | Scrape ThomasNet suppliers and manufacturers by keyword, category, location, certification or company type, or paste… |
| [We Work Remotely Scraper](actors/we-work-remotely-jobs-scraper) | Extract current remote job listings from weworkremotely.com. Use keyword search or WWR feed, category, and… |

### Travel

| Scraper | What it does |
| --- | --- |
| [Expedia Hotels Scraper](actors/expedia-universal-scraper) | Scrape Expedia.com hotel listings and reviews for any destination. Extract prices, ratings, review text, photos,… |
| [FurnishedFinder Scraper](actors/furnishedfinder-scraper) | Scrape furnishedfinder.com listings by city or URL. Extract structured data including price, beds, baths, occupancy,… |
| [Autotrader US Scraper](actors/autotrader-com-scraper) | Scrape US car listings from Autotrader by make, model, ZIP, price, year, body style, filters, or listing URLs.… |
| [Flightpoints & Roame Award Flight Scraper](actors/flightpoints-award-scraper) | Multi-source award flight availability from Flightpoints.com + Roame.travel. Search any route and date for miles,… |
| [Viator Scraper](actors/viator-com-scraper) | Collect Viator.com tour and activity results from destinations, categories, search pages, or pasted URLs. Returns… |
| [Concert Archives Scraper](actors/concert-archives-scraper) | Scrape Concert Archives concert and tour history: past and upcoming dates, venues, cities, line-ups, tours, genres,… |
| [Naver Map Scraper](actors/naver-map-scraper) | Scrape Naver Map places by keyword or URL: names, categories, ratings, phones, addresses, GPS, menus, opening hours,… |
| [Vrbo Scraper](actors/vrbo-vacation-rentals-scraper) | Extract vacation rental data from Vrbo.com by location, region, coordinates, property URL, or property ID. Returns… |
| [Booking.com Hotels Scraper](actors/booking-com-scraper) | Scrape booking.com hotels, apartments, villas and hostels. Search any destination with the site's own filters (type,… |
| [EasyAuto123 Scraper](actors/easyauto123-cars-scraper) | Scrape EasyAuto123 vehicle listings into clean structured data. Extract prices, VINs, odometer readings, make,… |
| [Pollstar Scraper](actors/pollstar-concert-tour-scraper) | Scrape Pollstar upcoming concerts and tour dates: play date, venue with full address and coordinates, artist… |
| [AutoTrader UK Scraper](actors/autotrader) | Pull structured vehicle listings from autotrader.co.uk at scale. Search by filters or use AutoTrader URLs. Returns… |

### Social Media

| Scraper | What it does |
| --- | --- |
| [TikTok Profile Scraper](actors/tiktok-scraper) | Scrape TikTok without login. Extract profiles, bios, follower stats and videos; search by hashtag or keyword; scrape… |
| [Lemon8 Search Scraper](actors/lemon8-discover-scraper) | Scrape Lemon8 posts by keyword across multiple regions. Extract posts, images, videos, comments, engagement metrics,… |
| [Lemon8 Profile Scraper](actors/lemon8-profile-scraper) | Scrape Lemon8 user profiles with automated multi-profile discovery. Extract profile data, detailed posts, engagement… |
| [Tiktok Live Recorder Scraper](actors/tiktok-live-recorder) | Record TikTok live streams to MP4 with full metadata, all stream quality URLs, and crash-resilient segmented… |
| [ViewStats Scraper](actors/viewstats-channel-analytics) | Scrape YouTube channel analytics from ViewStats. Look up channels by handle, URL, or keyword search. Returns… |
| [Twitch ALL IN ONE URL Scraper](actors/twitch-scraper) | Scrape Twitch data at scale, including channels, live streams, clips, VODs, and top games. Extract HLS m3u8 stream… |
| [Clutch Scraper](actors/clutch-directory-scraper) | Scrape Clutch company directories and profiles. Get names, ratings, review counts, hourly rate, min project size,… |
| [Suno Scraper](actors/suno-music-scraper) | Collect public Suno music data: songs with lyrics, style tags, model version, play and like counts, audio, video and… |
| [Truth Social Scraper](actors/truthsocial-com-scraper) | Scrape public Truth Social profiles, posts, media, metrics, author data, and complete source objects using profile… |
| [Mastodon Scraper](actors/mastodon-social-scraper) | Scrape trending Mastodon profiles and related posts from any Mastodon instance. Returns rich profile data, follower… |
| [Reddit Scraper](actors/reddit-scraper) | Scrape Reddit posts, comments, and media from any subreddit or user profile — no login or API keys required. Search… |
| [TrustMate.io Scraper](actors/trustmate-io-reviews-scraper) | Scrape complete company review histories from TrustMate.io. Paste company profile URLs, slugs, or domains, with… |
| [Udio Scraper](actors/udio-com-scraper) | Collect public Udio tracks with the complete generation prompt, full lyrics, style tags, like and play counts,… |
| [Universal Media Extractor Scraper](actors/universal-media-extractor) | Extract videos, audio, and metadata from 1000+ websites including YouTube, TikTok, Twitter/X, Instagram, Vimeo,… |
| [Apple App Store Reviews Scraper](actors/app-store-reviews-scraper) | Scrape Apple App Store reviews across 150+ country storefronts. Search by app name or URL and extract ratings,… |
| [Google Play Reviews Scraper](actors/google-play-reviews-scraper) | Collect Google Play reviews and ratings for any app across country storefronts. Search by app name or use a Google… |
| [Lemon8 Feed Scraper](actors/lemon8-feeds-scraper) | Scrape Lemon8 feeds across 22 categories and 10+ regions. Extract posts, images, videos, comments, engagement… |
| [Lemon8 Media Scraper](actors/lemon8-media-scraper) | Lightweight Lemon8 scraper for extracting image and video URLs from posts, with optional media downloads. Built for… |
| [Wattpad Scraper](actors/wattpad-scraper) | Scrape Wattpad stories by keyword, tag, category, language or URL. Extract authors, reads, votes, tags, completion… |

### Video

| Scraper | What it does |
| --- | --- |
| [YouTube Transcript & Subtitle Scraper](actors/youtube-transcript-scraper) | Extract transcripts and subtitles from YouTube videos in bulk using video, playlist, channel URLs, or keyword… |

### News & Sports

| Scraper | What it does |
| --- | --- |
| [SofaScore Scraper](actors/sofascore-scraper) | Pull structured sports data from SofaScore across football, basketball, tennis, and 20+ sports. Search by keyword,… |
| [AI Search Tool Scraper](actors/ai-web-search-tool) | Give your AI agents real-world knowledge. This Actor provides high-quality web, news, image, video, and book search… |

### AI & LLM

| Scraper | What it does |
| --- | --- |
| [ProductReview.com.au Scraper](actors/product-reviews-australia-scraper) | Scrape ProductReview.com.au products, businesses and customer reviews. Search by location, category or custom query… |
| [AI Agent Web Fetcher Scraper](actors/ai-fetch-python) | An advanced web fetcher that can fetch almost all websites and convert them to LLM-friendly Markdown format. Perfect… |
| [Web Scraper For Llms](actors/web-scraper-for-llms) | Stealth web scraping engine built for LLMs. Converts any web page to clean markdown or HTML |
| [Doc To Markdown Scraper](actors/doc-to-markdown) | Convert documents (PDF, Word, PowerPoint, Excel, HTML, images) to clean Markdown. Supports batch processing,… |

### SEO & Search

| Scraper | What it does |
| --- | --- |
| [Yellow Pages AU Scraper](actors/yellow-pages-au-scraper) | Scrape business listings from Yellow Pages Australia by type and location. Get names, contacts, websites, ratings,… |
| [Dealroom Startup & Market Map Scraper](actors/dealroom-co-scraper) | Scrape Dealroom.net market maps, company lookup results, live signals, and newly founded startup records. Supports… |
| [Ip Location Check Scraper](actors/ip-location-check) | Look up geographic locations for IP addresses. Supports batch lookups with country, city, subdivision, coordinates,… |

### Leads & Directories

| Scraper | What it does |
| --- | --- |
| [OLX Scraper](actors/olx-scraper) | Fast OLX scraper across 9 countries, including Poland, Romania, Portugal, Ukraine, Bulgaria, Kazakhstan, Uzbekistan,… |
| [BBB Scraper](actors/bbb-org-scraper) | Scrape bbb.org (Better Business Bureau, USA & Canada) business profiles: BBB rating, accreditation, contact and… |
| [AutoScout24 Scraper](actors/autoscout24-scraper) | A lean, production-grade scraper for autoscout24.com. Point it at a search, get back clean JSON with 30+ fields per… |
| [Herold.at Scraper](actors/herold-at-scraper) | Scrape Herold.at business listings across Austria into clean JSON. Extract names, addresses, GPS, phone numbers,… |
| [Ycombinator Scraper](actors/ycombinator-com-scraper) | Pull every ycombinator.com company across every batch, with founders, social URLs, application Q&A, demo-day video,… |
| [Craigslist Scraper](actors/craigslist-classifieds-scraper) | Scrape Craigslist postings in any of 700+ cities worldwide: price, title, posting text, attributes, photos,… |
| [Yellow Pages NZ Scraper](actors/yellow-nz-scraper) | Scrapes business listings from Yellow.co.nz (New Zealand Yellow Pages). Extract comprehensive business information,… |
| [Childcare AU Scraper](actors/careforkids-com-au-scraper) | Scrape Australia’s largest childcare directory careforkids.com.au with long day care, preschool, family day care,… |
| [Flippa Scraper](actors/flippa-com-scraper) | Scrape Flippa listings with full enrichment, including revenue, profit, valuation multiples, traffic, business age,… |
| [GoWork FR & DE Company Reviews and Profile Scraper](actors/gowork-eu-scraper) | Extract company profiles from GoWork France and Germany, including contact details, review threads with replies,… |
| [HiPages Scraper](actors/hipages-business-scraper) | Scrape business listings from HiPages Australia by category, location, or URL. Extract business names, contact… |
| [Justia Lawyer Profiles Scraper](actors/justia-lawyer-scraper) | Scrape attorney profiles from the Justia Lawyer Directory. Extract names, contacts, office locations, practice… |
| [Local.ch Scraper](actors/local-ch-scraper) | Pull structured company data from local.ch, including name, address, GPS, phone, email, website, hours, ratings,… |
| [Product Hunt Scraper](actors/product-hunt-launches-scraper) | Extract producthunt.com data including products, launches, keyword search results, maker profiles, reviews,… |
| [TrueLocal AU Directory Listings & Reviews Scraper](actors/truelocal-com-au-scraper) | Scrape TrueLocal.com.au business listings by keyword, location, or URL. Extract names, addresses, GPS coordinates,… |
| [2dehands & 2ememain Scraper](actors/2dehands-2ememain-scraper) | Scrape classifieds from 2dehands.be and 2ememain.be by keyword, filters, or URLs. Returns title, price, location,… |
| [Kleinanzeigen.de Scraper](actors/kleinanzeigen-de-scraper) | Scrape Kleinanzeigen.de ads by keyword, category, location, price, seller type, or search URL. Extract descriptions,… |
| [Marktplaats.nl Scraper](actors/marktplaats-nl-scraper) | Scrape Marktplaats.nl listings by keyword or URL. Extract title, price, condition, location and coordinates, photos,… |
| [PagesJaunes FR Scraper](actors/pagesjaunes-fr-scraper) | Scrapes business listings from PagesJaunes.fr (French Yellow Pages). Extract comprehensive business information,… |

### E-commerce

| Scraper | What it does |
| --- | --- |
| [Ozon.ru Scraper](actors/ozon-ru-scraper) | Extract structured product data from Ozon.ru, Russia’s largest marketplace. Search by keyword or use product,… |
| [Coupang Scraper](actors/coupang-scraper) | Scrape Coupang.com products by keyword, category or URL. Extract 20+ fields including title, brand, price, discount,… |
| [bol.com Scraper](actors/bol-com-scraper) | Scrape bol.com products: title, price, list price and discount, EAN, brand, images, condition, delivery, full… |
| [Woolworths AU Scraper](actors/woolworths-au-scraper) | Scrape Woolworths Australia (woolworths.com.au) grocery products and reviews. Search by keyword or paste product /… |
| [GrabFood Restaurant Scraper](actors/grabfood-restaurants-scraper) | Scrape GrabFood restaurants across Southeast Asia, including SG, MY, TH, VN, PH, ID, KH, and MM. Search by keyword… |
| [Coles AU Scraper](actors/coles-au-scraper) | Scrape Coles.com.au grocery products and customer reviews. Search by keyword, browse categories, or use… |
| [Tokopedia Scraper](actors/tokopedia-scraper) | Extract product data from Tokopedia, Indonesia’s largest marketplace. Search by keyword with sorting and filters, or… |
| [Trendyol Scraper](actors/trendyol-scraper) | Scrape Trendyol products, prices, ratings, badges, sellers, full reviews and Q&A. Search by keyword with filters,… |
| [Depop Scraper](actors/depop-scraper) | Scrape Depop search results, listings, shops, and reviews to JSON, CSV, or Excel. Extract titles, prices, shipping,… |
| [Cars.com Scraper](actors/cars-com-scraper) | Scrape cars.com listings by make, ZIP and radius. 90+ fields per car: price, MSRP, monthly payment, mileage, VIN,… |
| [Cdiscount Scraper](actors/cdiscount-scraper) | Scrape product data from Cdiscount.com by keyword, category, or URL. Apply filters and sorting, then enrich results… |
| [DoorDash Scraper](actors/doordash-scraper) | Extract structured doordash.com data at scale. Search by keyword or paste store URLs to get store details, ratings,… |
| [Lazada Scraper](actors/lazada-scraper) | Scrape Lazada products and reviews across SEA markets, including Malaysia, Singapore, Indonesia, Philippines,… |
| [Mercari Japan Scraper](actors/mercari-jp-scraper) | Scrape Mercari Japan listings, sellers and reviews at scale. Extract names, prices, conditions, photos, shipping… |
| [Wine-Searcher Scraper](actors/wine-searcher-scraper) | Look up wines on wine-searcher.com by name, URL, or LWIN code. Returns 30+ fields, including critic scores, prices,… |
| [ALDI AU Scraper](actors/aldi-com-au-scraper) | Scrape ALDI Australia (aldi.com.au) products: name, brand, price, was-price, savings, unit price, size, category,… |
| [Naver Shopping Scraper](actors/naver-brand-store-scraper) | Scrape Naver Shopping products by Korean or English keyword, or by URL. Returns 190+ fields per product, including… |
| [Carrefour Spain Scraper](actors/carrefour-es-scraper) | Scrape Carrefour Spain (carrefour.es) products. Search by keyword, browse a category, or paste product/category… |
| [Gumtree AU Scraper](actors/gumtree-au-scraper) | Scrape gumtree.com.au classifieds across every vertical: for-sale goods, motors, real estate, jobs and services. Get… |
| [KREAM Korea Scraper](actors/kream-scraper) | Scrape KREAM (kream.co.kr) sneaker and fashion resale data by keyword search, filters, sorts, or product URLs.… |
| [E.Leclerc Scraper](actors/leclerc-fr-scraper) | Scrape E.Leclerc France (e.leclerc) grocery and retail products. Search by keyword or category, or paste product and… |
| [OTTO.de Scraper](actors/otto-de-scraper) | Scrape OTTO.de products by search or URL. Extract prices, discounts, variants, availability, brand, seller,… |
| [Darty Scraper](actors/darty-com-scraper) | Scrape Darty (darty.com) products: current price plus strike-through reference price and discount, brand, category… |
| [Instacart Scraper](actors/instacart-grocery-price-scraper) | Scrape Instacart grocery catalogs with per-store prices. Run keywords across several stores at once to compare what… |
| [Kmart Scraper](actors/kmart-au-scraper) | Scrape products and customer reviews from Kmart.com.au. Search by keyword or use product/category URLs with sorting… |
| [Mango Scraper](actors/mango-com-scraper) | Scrape Mango (shop.mango.com) fashion products: current price plus strike-through Rebajas (sale) discount, full… |
| [REWE.de Scraper](actors/rewe-de-scraper) | Scrape REWE Germany (rewe.de) grocery products: current price, was-price and discount when genuinely on offer,… |
| [UNIQLO Scraper](actors/uniqlo-com-scraper) | Scrape UNIQLO products across 21 country storefronts in local currency. Price with pre discount original price, per… |
| [Wolt.com Scraper](actors/wolt-restaurants-scraper) | Scrape Wolt restaurants and full menus at the city scale. Extract 60+ fields, including name, address, GPS, hours,… |
| [Zalando Scraper](actors/zalando-scraper) | Scrape Zalando products: name, brand, current and original price, discount, sizes, images, deal flags and rating,… |
| [Boulanger.com Scraper](actors/boulanger-com-scraper) | Scrape Boulanger (boulanger.com) electronics and home-appliance products: current price plus strike-through… |
| [Bunnings Scraper](actors/bunnings-com-au-scraper) | Scrape bunnings.com.au products with full specifications, price, brand, stock, image gallery, warranty, customer… |
| [Carsales.com.au Scraper](actors/carsales-au-scraper) | Scrape structured vehicle listings from Carsales.com.au from $1 per 1K results. Built to bypass the 20-page /… |
| [Castorama.fr Scraper](actors/castorama-fr-scraper) | Scrape Castorama.fr DIY and home-improvement products by keyword, category, or URL. Extract prices, original prices,… |
| [Chrono24 Scraper](actors/chrono24-scraper) | Scrape Chrono24 luxury watch listings by keyword, filters or URL. Extract 50+ fields including brand, model,… |
| [Dienmayxanh Scraper](actors/dienmayxanh-scraper) | Scrape dienmayxanh.com home appliances and electronics with full specifications, current & original price, discount,… |
| [dm.de Scraper](actors/dm-de-scraper) | Scrape dm-drogerie markt (dm.de) products: current + strike-through Ausverkauf price with discount, per-unit pricing… |
| [Douglas Germany Scraper](actors/douglas-de) | Scrape Douglas.de beauty and fragrance products by keyword, category, brand, or URL. Extract brands, current and… |
| [IKEA Products & Reviews Scraper](actors/ikea-scraper) | Scrape IKEA products across 50+ markets. Extract names, prices, currencies, ratings, full reviews, colours,… |
| [Kaufland.de Scraper](actors/kaufland-de-scraper) | Scrape Kaufland.de, Germany's hypermarket and online marketplace: keyword/category/brand search or paste links.… |
| [LeroyMerlin.es Scraper](actors/leroymerlin-es-scraper) | Scrape Leroy Merlin Spain (leroymerlin.es) DIY and home-improvement products: price, strike-through original price… |
| [Officeworks Scraper](actors/officeworks-scraper) | Scrape Officeworks products by keyword, category, or URL. Extract names, brands, prices, GST, stock by state,… |
| [SHEIN Scraper](actors/shein-product-scraper) | Scrape SHEIN product listings by keyword or from any category, sale or search link. Returns product ID, SKU, title,… |
| [StockX Scraper](actors/stockx-market-data-scraper) | Scrape StockX market data by keyword, category or URL. Every row carries lowest ask, highest bid, last sale, bid ask… |
| [Thalia.de Scraper](actors/thalia-de-scraper) | Scrape Thalia.de books, eBooks, audiobooks, toys and stationery. Search by keyword or category, browse Schnäppchen… |
| [The RealReal Scraper](actors/therealreal-scraper) | Scrape luxury consignment listings from therealreal.com. Browse by designer, category or keyword and get designer,… |
| [Vivino Wine Scraper](actors/vivino-wine-data-scraper) | Scrape Vivino.com for wine ratings, prices, taste profiles, food pairings, grapes, and reviews. Search by wine names… |
| [Zara Scraper](actors/zara-com-scraper) | Scrape Zara (zara.com) products: current price plus strike-through Rebajas (sale) discount, full colour variant… |
| [Zomato Scraper](actors/zomato-scraper) | Scrape restaurants and reviews from zomato.com. Get names, cuisines, ratings and votes, cost for two, address and… |
| [24S Scraper](actors/24s-com-scraper) | Scrape 24S luxury fashion by category, filters, or URL. Extract brand, name, price, discounts, size stock, colors,… |
| [Auchan France Scraper](actors/auchan-fr-scraper) | Scrape Auchan.fr products: grocery, drinks, household and general merchandise. Real price scoped to your… |
| [Chemist Warehouse AU Scraper](actors/chemistwarehouse-com-au-scraper) | Scrape chemistwarehouse.com.au products with prices, RRP, discounts, stock, images, ingredients, directions,… |
| [Costco Australia Scraper](actors/costco-au-scraper) | Scrape Costco.com.au products by keyword or product, search and category URLs. Extract prices, brands, ratings,… |
| [Decathlon.es Scraper](actors/decathlon-es-scraper) | Scrape Decathlon Spain (decathlon.es) sporting goods: current price plus strike-through discount, brand, seller,… |
| [Discogs Scraper](actors/discogs-scraper) | Scrape the Discogs catalogue by keyword, filter or link: releases, masters, artists and labels with tracklists,… |
| [druni.es Scraper](actors/druni-es-scraper) | Scrape Druni beauty, cosmetics and perfume products. Search by keyword, category, Ofertas Flash deals or paste… |
| [El Corte Inglés Scraper](actors/elcorteingles-es-scraper) | Scrape El Corte Inglés elcorteingles.es products across fashion, electronics, home, beauty, jewellery, toys and… |
| [Etsy Scraper](actors/etsy-marketplace-scraper) | Scrape Etsy listings by keyword, category, or URL. Extract titles, shops, prices, discounts, availability, images,… |
| [Fnac Scraper](actors/fnac-com-scraper) | Scrape Fnac (fnac.com) products: current price plus strike-through discount, colour/model variant matrix, brand,… |
| [FoodHero Scraper](actors/foodhero-surplus-grocery-scraper) | Scrape FoodHero surplus grocery deals across Canada by area, store or offer ID. Extract products, brands, regular… |
| [HORNBACH Products Scraper](actors/hornbach-de-scraper) | Scrape HORNBACH (hornbach.de) DIY, building & garden products: current + strike-through price with discount,… |
| [Idealo.de Scraper](actors/idealo-de-price-comparison-scraper) | Scrape Idealo.de products with identity details, GTIN, price ranges, specifications, images, rating breakdowns and… |
| [itch.io Game Scraper](actors/itch-io-scraper) | Scrape itch.io games by genre, tag, platform, price band or keyword, plus creator catalogues and game jam results.… |
| [Kogan.com Scraper](actors/kogan-com-scraper) | Scrape Kogan.com products with full details and customer reviews. Search by keyword or paste category/search URLs… |
| [MediaMarkt Germany Scraper](actors/mediamarkt-de-scraper) | Scrape MediaMarkt.de products by keyword or URL. Extract current and original prices, discounts, brands, EANs,… |
| [Mercadona Scraper](actors/mercadona-es-scraper) | Scrape Mercadona products by delivery-area postal code. Search by keyword or category, or paste product and category… |
| [MUJI Scraper](actors/muji-scraper) | Scrape MUJI products from the United States, Canada and Australia storefronts. Search by keyword or paste product,… |
| [Myer Scraper](actors/myer-au-scraper) | Scrape Myer (myer.com.au) department-store products: name, brand, price, was-price, saving, availability, category,… |
| [Netshoes Brazil Scraper](actors/netshoes-scraper) | Scrape sportswear and footwear from netshoes.com.br. Search by keyword with the store's own brand, size, colour and… |
| [Nitori Japan Furniture & Home Goods Scraper](actors/nitori-net-jp-scraper) | Scrape Nitori Japan (nitori-net.jp) furniture and home goods by keyword, category or pasted link. Filter by… |
| [OfferUp Scraper](actors/offerup-scraper) | Scrape OfferUp listings by keyword, location and radius. Returns 40+ fields per item: price, condition, GPS, full… |
| [ResQ Club Scraper](actors/resq-club-surplus-food-scraper) | Scrape ResQ Club surplus food offers in Finland, Sweden and Estonia: name, price, current price, discount, portions… |
| [Reverb Music Gear and Sold Price Guide Scraper](actors/reverb-scraper) | Scrape reverb.com music gear: guitars, amps, synths, pedals, drums and pro audio. Search live listings by brand,… |
| [Sephora Scraper](actors/sephora-product-scraper) | Scrape Sephora products across 21+ storefronts (US, AU, NZ, SG, MY, ID, TH, PH, MX, DE, RO, SE, GR, DK) with a… |
| [Target AU Scraper](actors/target-au-scraper) | Scrape products and customer reviews from Target.com.au. Search by keyword or use product/category URLs with sorting… |
| [Thegioididong Scraper](actors/thegioididong-scraper) | Scrape thegioididong.com products with full specifications, current & original price, discount, brand, category,… |
| [The Warehouse NZ Scraper](actors/thewarehouse-co-nz-scraper) | Scrape The Warehouse New Zealand search results, category pages, and direct product URLs. Extract prices,… |
| [ThredUp Scraper](actors/thredup-scraper) | Scrape ThredUp resale listings by keyword, department, brand, size, condition, price or URL. Extract 35+ fields… |
| [A101 Turkey Scraper](actors/a101-product-scraper) | Scrape A101.com.tr products across A101 Ekstra and A101 Kapıda. Extract 80+ fields including prices, discounts,… |
| [Amazon Australia Product & Reviews Scraper](actors/amazon-au-scraper) | Scrape Amazon Australia (amazon.com.au) products and customer reviews. Search by keyword or paste product, search… |
| [Americanas Brazil Scraper](actors/americanas-com-br-scraper) | Scrape Americanas Brazil (americanas.com.br) by keyword, department or pasted link. Returns SKU, title, brand,… |
| [Bic Camera Scraper](actors/biccamera-com-scraper) | Scrape Bic Camera (biccamera.com) products: JPY price, list price and discount, Bic Point amount and rate, stock and… |
| [BIG W Marketplace Scraper](actors/bigw-marketplace-scraper) | Scrape BIG W Marketplace seller listings from bigw.com.au: name, brand, price, was-price, saving, condition,… |
| [Daangn Scraper](actors/daangn-scraper) | Scrape Daangn (당근) marketplace listings by keyword and region. Returns 35+ fields per item including price, status,… |
| [Drogasil Brazil Pharmacy Scraper](actors/drogasil-com-br-scraper) | Scrape Drogasil (drogasil.com.br) medicines, health and beauty products by keyword, catalogue section or pasted… |
| [Gmarket.co.kr Scraper](actors/gmarket-global-scraper) | Scrape Gmarket.co.kr product listings and customer reviews into clean JSON. Search by keyword, paste product URLs,… |
| [GOAT Scraper](actors/goat-sneaker-scraper) | Scrape GOAT (goat.com), the sneaker and streetwear resale marketplace. Search or paste product, brand, collection… |
| [Harvey Norman Scraper](actors/harvey-norman-scraper) | Scrape Harvey Norman Australia products: name, brand, price, was-price / discount, specifications, image gallery,… |
| [Lidl.es Products Scraper](actors/lidl-es-scraper) | Scrape Lidl.es grocery and non-food products across weekly offers, tools, home, garden, kitchen, fashion, kids,… |
| [MediaMarkt.es Scraper](actors/mediamarkt-es-scraper) | Scrape MediaMarkt Spain (mediamarkt.es) products: current price, strike-through original price + discount on offers,… |
| [mobile.de Scraper](actors/mobile-de-scraper) | Scrape mobile.de vehicle listings with 30+ fields, including price, registration, mileage, power, fuel,… |
| [OBI.de Scraper](actors/obi-de-scraper) | Scrape OBI (obi.de) DIY/home-improvement products: current + strike-through original price with discount, per-unit… |
| [PB Tech Scraper](actors/pbtech-co-nz-scraper) | Scrape pbtech.co.nz products with full specifications, price, brand, condition, per-store stock, image gallery,… |
| [PcComponentes Scraper](actors/pccomponentes-com-scraper) | Scrape PcComponentes (pccomponentes.com) products: current price plus strike-through reference-price discount,… |
| [ROSSMANN.de Scraper](actors/rossmann-de-scraper) | Scrape ROSSMANN (rossmann.de) drugstore products: current + original strike-through price with discount, per-unit… |
| [SeatGeek Scraper](actors/seatgeek-events-scraper) | Scrape SeatGeek events with ticket price ranges (lowest, highest, average, median), venues, performers, dates and… |
| [Whatnot Scraper](actors/whatnot-scraper) | Scrape Whatnot live and upcoming shows, queued items and lots, and seller profiles. Search by keyword or URL, then… |

### More

| Scraper | What it does |
| --- | --- |
| [Mercado Livre Brazil Scraper](actors/mercadolivre-com-br-scraper) | Scrape Mercado Livre Brazil by keyword or URL. Filter by category, brand, price, condition, shipping, official… |
| [Turo Scraper](actors/turo-scraper) | Collect Turo vehicles by location and trip dates or listing URLs. Get make, model, year, ratings, photos, dated… |
| [TikTok Comments Scraper](actors/tiktok-comments-scraper) | Scrape comments from TikTok videos using one or more video URLs or IDs. Extract comment text, author, likes, reply… |
| [eBay Scraper](actors/ebay-com-scraper) | Scrape eBay by keyword, category, seller or pasted link across 16 country storefronts. Returns id, title, condition,… |
| [Jumia Marketplace Scraper](actors/jumia-marketplace-scraper) | Scrape Jumia, Africa's largest marketplace: products with local prices, discounts, ratings, official-store badges… |
| [Songkick Scraper](actors/songkick-concert-calendar-scraper) | Scrape Songkick concert and event calendars: upcoming and past dates, venues, cities, artists, ticket availability… |
| [Too Good To Go Scraper](actors/toogoodtogo-surprise-bag-scraper) | Scrape Too Good To Go (TGTG) stores and surprise bags by location or item: price, value, savings, quantity, pickup… |
| [Untappd Beer Scraper](actors/untappd-scraper) | Scrape Untappd beers, breweries, venues and check-ins by keyword, brewery, Top Rated chart or pasted link. Returns… |
| [Allegro Scraper](actors/allegro-pl-scraper) | Scrape Allegro by keyword or URL. Extract offers, prices, delivery, seller details, and product reviews. Includes… |
| [CrazyGames Scraper](actors/crazygames-scraper) | Scrape CrazyGames games with ratings, upvotes and downvotes, total plays and likes, developer, category and tags,… |
| [Hipcamp Scraper](actors/hipcamp-camping-glamping-scraper) | Scrape Hipcamp campgrounds, RV parks, glamping and unique stays by US or AU region or listing link: price per night,… |
| [Klook Scraper](actors/klook-activities-scraper) | Scrape Klook activities, tours, attractions and travel experiences from search pages or activity URLs. Extract… |
| [Marks & Spencer Scraper](actors/marksandspencer-scraper) | Collect marksandspencer.com (M&S) products and individual reviews from keyword searches, categories or product… |
| [Naver Land Scraper](actors/naver-land-listings) | Scrape structured property listings from Naver Land map URLs. Extract listing titles, prices, areas, addresses, GPS… |
| [OpenTable Reviews Scraper](actors/opentable-reviews-scraper) | Scrape full OpenTable.com restaurant reviews by keyword, area, or restaurant profile URLs. Collect every available… |
| [Rakuten Scraper](actors/rakuten-ichiba-scraper) | Scrape Rakuten Ichiba (rakuten.co.jp): name, JPY price, reference price and discount, Rakuten points, shipping,… |
| [Sportsbook Odds Scraper (1xBet, Melbet, Linebet, Paripulse)](actors/sportsbook-odds-scraper) | Collect live and prematch betting odds from 1xBet, Melbet, Linebet and Paripulse. Give it the brands and feeds you… |
| [Trustpilot Scraper](actors/trustpilot-reviews-scraper) | Scrape Trustpilot business profiles and reviews on any country domain: TrustScore, the exact 1-5 star distribution… |
| [Wildberries Scraper](actors/wildberries-marketplace-scraper) | Scrape Wildberries marketplace: product search with prices (wallet vs retail), discounts, stock, ratings and seller… |
| [Zigbang Scraper](actors/zigbang-property-scraper) | Scrape Zigbang property listings across Seoul and South Korea, including one-room, villa and officetel rentals and… |
| [ZOZOTOWN Scraper](actors/zozotown-scraper) | Scrape ZOZOTOWN (zozo.jp), Japan's largest fashion marketplace: name, brand, JPY price with was-price and discount,… |
| [Airbnb Scraper](actors/airbnb-stays-reviews-scraper) | Scrape Airbnb stays by destination or link: nightly and total price, rating breakdown, host stats, amenities, house… |
| [AliExpress Scraper](actors/aliexpress-scraper) | Scrape AliExpress products: search by keyword or category, or process pasted search, category and product URLs page… |
| [AllTrails Hiking Scraper](actors/alltrails-hiking-scraper) | Scrape AllTrails, the world's largest hiking platform: trails with difficulty, length, elevation gain, route type,… |
| [Anghami Scraper](actors/anghami-catalog-scraper) | Scrape Anghami's public catalog by keyword or player URL. Rows carry their kind (song, album, artist, playlist, tag)… |
| [AniList Anime & Manga Scraper](actors/anilist-anime-manga-scraper) | Scrape AniList anime and manga: titles (romaji/English/native), scores, popularity, favourites, genres, studios,… |
| [Appliances Online Scraper](actors/appliancesonline-com-au-scraper) | Scrape appliancesonline.com.au by category, keyword, or URL. Extract title, brand, AUD price, was-price, stock, key… |
| [ASOS Scraper](actors/asos-com-scraper) | Scrape ASOS by keyword, category or URL. Every row carries the selling price and the original price, the discount,… |
| [Bandsintown Scraper](actors/bandsintown-concert-event-scraper) | Scrape Bandsintown concert and festival dates: artist tour calendars, venue profiles, ticket links, lineups, RSVP… |
| [Casas Bahia Brazil Electronics & Home Goods Scraper](actors/casasbahia-com-br-scraper) | Scrape products from Casas Bahia Brazil by keyword, department, or URL. Filter by brand, price, discount, rating,… |
| [Dan Murphy’s Scraper](actors/danmurphys-scraper) | Scrape Dan Murphy’s products by category, keyword, or specials. Extract 45+ fields, including regular, sale and… |
| [Deezer Scraper](actors/deezer-com-scraper) | Scrape Deezer by keyword or URL. Extract tracks, albums, artists, playlists, lyrics, radios, charts and public… |
| [Duolingo Scraper](actors/duolingo-learner-scraper) | Scrape public Duolingo data without login. Extract learner profiles with streaks, XP and achievements, weekly league… |
| [Dzen.ru Scraper](actors/dzen-ru-scraper) | Scrape Dzen.ru (ex Yandex.Zen): articles, videos and channels. Full article text with likes and comment counts,… |
| [Eventim Scraper](actors/eventim-de-event-scraper) | Scrape CTS Eventim Germany and EU event catalogue: concerts, festivals, comedy, sports, dates, venues, prices and… |
| [Falabella Scraper](actors/falabella-marketplace-scraper) | Scrape Falabella, Latin America's leading retail marketplace: products with local prices, discounts, ratings and… |
| [Fever Scraper](actors/fever-com-scraper) | Scrape Fever events by city, category, keyword or URL. Extract from-prices, venues, dates and ratings, with optional… |
| [Digitec Galaxus Scraper](actors/galaxus-marketplace-scraper) | Scrape Digitec Galaxus, Switzerland's largest online retailer: products with local prices, discounts, ratings, stock… |
| [Globo Esporte Scraper](actors/globo-ge) | Scrape public sports content from ge.globo.com, including news, videos, matches and feed records. Extract clean,… |
| [Grailed Scraper](actors/grailed-marketplace-scraper) | Scrape Grailed by keyword, category, designer, condition, size or URL. Extract prices and price history,… |
| [Hepsiemlak Scraper](actors/hepsiemlak-com-scraper) | Scrape hepsiemlak.com sale and rental listings by city or district, or paste listing links. Every row carries price,… |
| [Homes.com Scraper](actors/homes-com-scraper) | Scrape US property records from Homes.com. Pick a city, state or ZIP and a channel (for sale, for rent, recently… |
| [KKday Scraper](actors/kkday-com-scraper) | Scrape KKday travel activities by keyword, city or URL. Every row carries prices, discount, ratings, booking counts,… |
| [KLEKT Sneaker & Apparel Resale Scraper](actors/klekt-com-scraper) | Scrape sneaker and streetwear listings from KLEKT (klekt.com). Browse the catalog with filters and extract product… |
| [Isetan Mitsukoshi Scraper](actors/mistore-jp-scraper) | Scrape the Isetan Mitsukoshi department store online shop (mistore.jp). Search by keyword or department, or paste… |
| [MyAnimeList Scraper](actors/myanimelist-scraper) | Scrape MyAnimeList anime and manga by keyword, ranking chart or URL. Extract titles, scores, ranks, members, genres,… |
| [Naukri.com Scraper](actors/naukri-com-scraper) | Scrape Naukri.com jobs by keyword or URL. Extract job title, company, skills, experience, salary, location and… |
| [Next.co.uk Scraper](actors/next-uk-product-scraper) | Scrape Next.co.uk: keyword search, category and product-listing walks, full product details (price, was-price,… |
| [OK.ru Scraper](actors/ok-ru-scraper) | Scrape public OK.ru users, groups, topics, posts, videos, games and greetings by keyword or URL. Extract profiles,… |
| [OneFootball Scraper](actors/onefootball-com-scraper) | Scrape public OneFootball data including football news, upcoming fixtures, match results and league tables. Get… |
| [Padmapper Scraper](actors/padmapper-rental-listings-scraper) | Scrape Padmapper apartment rentals across US/CA cities: rent, beds, baths, sqft, location, photos, source-site… |
| [Pikabu Scraper](actors/pikabu-scraper) | Scrape Pikabu (Пикабу): keyword search, hot/new/best feeds, communities, tags, full story details with media, all… |
| [Pocket Casts Podcast Scraper](actors/pocketcasts-podcast-scraper) | Scrape Pocket Casts podcast data, including listener ratings, full episode archives, publishing cadence, seasons,… |
| [Poshmark Scraper](actors/poshmark-scraper) | Scrape Poshmark fashion-resale listings: keyword search, brand and category browse, sold listings with sold dates,… |
| [Rakuten Travel Scraper](actors/rakuten-travel-scraper) | Scrape Rakuten Travel, Japan's largest domestic hotel-booking site, by prefecture, keyword or URL. Every row carries… |
| [Resy Scraper](actors/resy-restaurant-availability-scraper) | Scrape Resy restaurants and live reservation availability by city or URL. Get bookable times by date and party size,… |
| [Roblox Scraper](actors/roblox-scraper) | Scrape Roblox experiences, marketplace items, users and communities. Player counts, visits, likes, genre, creator,… |
| [Rover Pet Care Scraper](actors/rover-pet-care-scraper) | Scrape Rover.com pet-care providers: sitter search by city, rates per stay type, ratings and review history,… |
| [Shopee Cambodia Scraper](actors/shopee-collection-products) | Scrape public Shopee Cambodia collections and campaign products without signing in. Extract prices, ratings, images,… |
| [SpaceX Launches Scraper](actors/spacex-com) | Pull the full SpaceX launch catalog from spacex.com in clean JSON. Filter by vehicle, mission type, status, launch… |
| [SSENSE Scraper](actors/ssense-product-scraper) | Scrape SSENSE by keyword, category, designer or URL. Every row carries the selling price and the regular price, the… |
| [Stocktwits Scraper](actors/stocktwits-com-scraper) | Scrape Stocktwits message streams with bull/bear sentiment labels, bodies, likes, replies, cashtags and author stats… |
| [Suumo.jp Scraper](actors/suumo-jp-scraper) | Scrape Suumo, Japan's largest property portal: rental rooms with rent, management fees, deposits, layout, floor… |
| [Willhaben.at Scraper](actors/takealot-com-scraper) | Scrape Willhaben.at listings into clean JSON with 40+ structured fields, including prices, GPS coordinates, photos,… |
| [TaskRabbit Scraper](actors/taskrabbit-tasker-scraper) | Scrape TaskRabbit taskers by US city and service. Extract hourly rates, ratings, reviews, completed tasks, elite… |
| [Ticketmaster Scraper](actors/ticketmaster-event-discovery) | Discover and scrape Ticketmaster events across the US, UK, Australia and Canada. Search by keyword, artist or venue,… |
| [TIDAL Scraper](actors/tidal-catalog-scraper) | Scrape TIDAL tracks, albums, artists, playlists and public mixes by search phrase or URL. Extract structured… |
| [Traveloka Hotel Scraper](actors/traveloka-com-scraper) | Scrape Traveloka hotels across Singapore, Malaysia, Indonesia, Thailand, Vietnam and the Philippines: nightly… |
| [Trip.com Hotels Scraper](actors/trip-com-scraper) | Pull structured hotel listings from trip.com with prices, room types, amenities, policies, nearby places, and full… |
| [Vinted Multi-Country Scraper](actors/vinted-marketplace-scraper) | Scrape Vinted across 27 country marketplaces: keyword search with brand, price and condition filters, item and… |
| [Walgreens Products & Reviews Scraper](actors/walgreens-com) | Scrape Walgreens products by keyword, category or product URL. Extract prices, promotions, availability,… |
| [Walmart Scraper](actors/walmart-scraper) | Scrape Walmart.com by keyword, URL, or item ID. Extract prices, was-prices, sellers, marketplace offers, stock,… |
| [WEBTOON Scraper](actors/webtoons-com-scraper) | Scrape the WEBTOON catalog into structured data. Extract series, genres, rankings and complete episode lists,… |
| [Wego Scraper](actors/wego-com-scraper) | Scrape Wego hotels by city or search URL. Get rates, providers, booking links, coordinates, scores, images and… |
| [Yandex Maps Scraper](actors/yandex-maps-scraper) | Scrape businesses and places from Yandex Maps by search term or URL for research, leads and market analysis. Парсер… |
| [Yandex SERP Scraper](actors/yandex-serp-scraper) | Scrape Yandex web, image and video results with URLs, snippets and organic rankings for SEO and competitor research.… |
| [Yanolja Scraper](actors/yanolja-com-scraper) | Scrape Yanolja (NOL), Korea's largest accommodations marketplace, by region or URL. Every row carries name, address,… |
| [Yodobashi Scraper](actors/yodobashi-com-scraper) | Scrape yodobashi.com electronics and appliances: JPY price, list price and discount, reward points, stock and… |
| [Zillow Scraper](actors/zillow-scraper) | Scrape zillow.com properties for sale, for rent and recently sold across the US: price, beds, baths, area, address,… |
| [Zoopla Scraper](actors/zoopla-co-uk-scraper) | Scrape UK property from Zoopla: for sale, to rent and Land Registry sold prices. Search by place with filters or… |
| [BookMyShow Scraper](actors/bookmyshow-scraper) | Scrape BookMyShow movies and live events by city, category or URL. Extract genres, languages, posters, synopsis,… |
| [Doc To Markdown MCP Server Scraper](actors/doc-to-markdown-mcp) | An MCP server that converts documents to clean Markdown. Convert PDFs, Word docs, Excel spreadsheets, PowerPoints,… |
| [Flashfood Scraper](actors/flashfood-grocery-deals-scraper) | Scrape Flashfood discounted groceries and stores by location or store. Extract current and original prices, savings,… |
| [Flightradar24 Scraper](actors/flightradar24-live-flight-tracker) | Live aircraft positions by map area (callsign, lat/lng, altitude, speed, vertical speed, heading, squawk,… |
| [GasBuddy Scraper](actors/gasbuddy-com-scraper) | Scrape GasBuddy station by station across the US and Canada. Returns brand, address, coordinates, phone, amenities,… |
| [Gopuff Scraper](actors/gopuff-prices-assortment-scraper) | Scrape Gopuff, the US quick-commerce delivery store, by location or product: prices, promotions, stock and… |
| [JioHotstar Scraper](actors/hotstar-com-scraper) | Scrape the JioHotstar catalog by content type or URL. Extract shows, movies, episodes, sports, clips and live… |
| [Letterboxd Scraper](actors/letterboxd-film-reviews-scraper) | Scrape Letterboxd films and reviews by search phrase, popular or genre lists, or film URL. Extract ratings,… |
| [Propwire Scraper](actors/propwire-property-leads-scraper) | Scrape Propwire.com: 157M+ US MLS & off-market properties with owner names, mailing addresses, equity, foreclosure… |
| [TuneIn Scraper](actors/tunein-radio-podcast-scraper) | Scrape TuneIn by keyword, category, genre, location or URL. Extract stations and podcasts with artwork, genre,… |
| [Viagogo Scraper](actors/viagogo-events-scraper) | Scrape Viagogo events by artist, production, venue, city, category, or URL. Extract event names, dates, venues,… |

---

<sub>These scrapers are built and maintained by [abotapi](https://abotapi.com/?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo). This repo is regenerated automatically from the public Apify Store. The examples are MIT licensed.</sub>
