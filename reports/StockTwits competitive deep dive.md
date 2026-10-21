# Build the Scoreboard, Not Another Chatroom

StockTwits is not a bad product, and it does not lack competition. It is a sticky niche incumbent that is slowly shrinking, its real weakness is trust, and in 2026 it faces more direct competition than at any point in its 18-year history. Its active users rate it **4.8/5 across ~167K iOS ratings**. It owns **17 years of ticker-tagged bull/bear data**, and it already runs an **official MCP server for Claude and ChatGPT** ([App Store](https://apps.apple.com/us/app/stocktwits/id389157776?see-all=reviews&platform=iphone); [ai.stocktwits.com](https://ai.stocktwits.com/)). Against that, third-party traffic estimates are 20–43% below their late-2024 and early-2025 levels, its "10M users" headline has not changed since January 2025, and revenue is estimated at only **$5–25M a year**. It also sells more and more paid presence to leveraged-ETF issuers, crypto exchanges, prediction markets and microcap investor-relations buyers ([Semrush](https://www.semrush.com/website/stocktwits.com/overview/); [Owler](https://www.owler.com/company/stocktwits)). The "nothing really competes" half of the claim is wrong. X added cashtag charts and a Trade button. Robinhood opened KYC-verified Social to all eligible US customers in mid-October. Reddit's chatter is now an ICE data product. Paid Discords hold the highest-value traders, and AI assistants answer "why is it moving" for free. One opening is still unclaimed: a **complete, neutral public record, scored the same way for everyone, of who called what and whether they were right**. Robinhood lets users pick which trades to show and hide their stats ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/robinhood-expands-social-trading-push-000800407.html)), and StockTwits' MCP exposes no track records. TickerHall's quickest credible route has four parts. Lead with Calls on the record as a scoreboard that is useful to a single caller, with verified call cards that travel on X, Reddit and Discord. Measure weekly active callers, not members. Refuse every form of paid visibility. Charge readers first and sell track-record data second. The base rates are harsh. Standalone social-investing apps were mostly absorbed, pivoted or shut down, and the best outcomes for companies that only do this cluster around **$200M valuations after a decade**. So run TickerHall as a capped option, gated by milestones, on 8 of your ~30 weekly hours, and keep PostDose, with the other 22, as your source of cash.

## StockTwits is sticky and shrinking, not broken

StockTwits' strength starts with habit. About **70% of its desktop traffic arrives direct**, the average visit lasts **~6:50**, and the audience is a loyal US-centred core: 68.5% American, ~74% male, with 25–34 the largest age group (third-party estimates) ([Similarweb](https://www.similarweb.com/website/stocktwits.com/)). Users stay for one live stream per cashtag, watchlists and earnings tools. On many small caps and biotechs, StockTwits is still the only place with dense live chatter. The iOS app's **4.8 stars from ~167K ratings** show that its engaged users are not suffering ([App Store](https://apps.apple.com/us/app/stocktwits/id389157776?see-all=reviews&platform=iphone)). Underneath sits the asset hardest to copy: **17 years of first-party history** of follows, conversation and self-labeled bull/bear sentiment ([Stocktwits](https://stocktwits.com/news-articles/business/others/stocktwits-acquires-ai-startup-thematic/ch8KVxsR5pd)). StockTwits licenses it through an enterprise API and a Databricks Marketplace listing ([Databricks](https://marketplace.databricks.com/details/1b5033c7-1709-4367-9a9b-3f33a54facb4/Stocktwits_Stocktwits-Messages-API)). Howard Lindzon, CEO again since early 2024, has pitched it explicitly as LLM training data ([Lindzon](https://www.howardlindzon.com/p/data-new-gold-stocktwits-cashtag-gold)).

The company also ships faster than its reputation suggests. A June 2026 relaunch of its ticker ("symbol") pages added "Top Voices", ranked on analysis quality rather than follower count. It also added "Watchers Data Insights", which charts how many distinct people watch a ticker against its price ([BriefGlance](https://briefglance.com/articles/stocktwits-doubles-down-on-social-overhauling-its-core-experience)). It also shipped AI "Why It's Trending" summaries ([Stocktwits Help](https://help.stocktwits.com/c/key-features/features/why-it-s-trending)), Polymarket earnings odds on ticker pages ([Barchart](https://www.barchart.com/story/news/34813550/stocktwits-and-polymarket-join-forces-the-worlds-largest-prediction-market-and-the-worlds-largest-social-platform-for-finance-launch-new-earnings-markets)), and CME futures and single-stock futures data ([Stocktwits](https://stocktwits.com/news-articles/business/others/stocktwits-expands-cme-group-alliance-with-the-integration-of-single-stock-futures-data/cZY86PbRJp6)).

The most important release for TickerHall is a live, sign-in-protected **official MCP server at mcp.stocktwits.com**. It feeds trending tickers, bull/bear sentiment per ticker, message volume and individual posts into Claude, ChatGPT, Codex, Cursor and any other MCP client ([ai.stocktwits.com](https://ai.stocktwits.com/)). Searches of the open MCP registries miss it, because they list only a third-party wrapper that Glama marks "Unhealthy" ([Glama](https://glama.ai/mcp/connectors/io.github.pipeworx-io/stocktwits)). A direct check of the endpoint's sign-in settings confirms StockTwits runs it, with access limited to reading data and the user's watchlists ([OAuth metadata](https://mcp.stocktwits.com/.well-known/oauth-protected-resource)). StockTwits' October 2026 Stocktoberfest conference named "agentic trading and social relative strength" as its themes ([Stocktwits](https://stocktwits.com/news-articles/business/others/stocktwits-announces-stocktoberfest-2026-with-tradr-et-fs-as-title-partner/cZoJNHSRJet)). StockTwits means to be the social data source for AI agents, which is the slot TickerHall's MCP plan was aiming at.

Behind the brand, the business is small. StockTwits has disclosed monthly active users only once: **~1M MAU on 6M registered users in December 2021**. That was when it raised $30M at a reported $210M valuation, in a round led by Alameda Research Ventures; it is the last priced round on record ([Bloomberg Law](https://news.bloomberglaw.com/private-equity/social-media-platform-stocktwits-nabs-210-million-valuation)). Third-party estimates put revenue at **$5–25M** ([Owler](https://www.owler.com/company/stocktwits)) and headcount at **~84** ([Tracxn](https://tracxn.com/d/companies/stocktwits/__IRMWBki8_c7cPCRwRUA80P47BYrIgyEKf_OWgw4nH8Q)). Its move into running a brokerage ended with the accounts sold to Public for **under $10M (~15K accounts)** ([FinTech Collective](https://news.fintech.io/post/102j5jj/public-acquires-stocktwits-trading-accounts)). Every press release from January 2025 to August 2026 gives the same "10M+ users", labeled sometimes "registered" and sometimes "active". Over that period Semrush's estimate of web visits fell from **26.5M in January 2025 to ~15M in December 2025** ([Semrush](https://tr.semrush.com/website/stocktwits.com/overview); [Semrush](https://www.semrush.com/website/stocktwits.com/overview/)). Similarweb shows **~11M in September 2026, down 12.9% from August**, though its period label is ambiguous ([Similarweb](https://www.similarweb.com/website/stocktwits.com/)). The company says MAU grew 20% after Lindzon's return; that is a company claim relayed by Forbes ([Forbes](https://www.forbes.com/sites/digital-assets/2025/05/12/stocktwits-jumps-on-the-crypto-bandwagon/)). App usage, which the web trackers miss, could be holding up better, and nobody outside the company knows. What is documented is that usage follows retail manias: StockTwits attributed its 50% user growth in 2021 directly to meme stocks.

The trust problem is real and well evidenced. Trustpilot rates StockTwits **1.3/5**, and every review on the first page is one star. The most common complaint is mutes and bans that are never explained and are triggered by mass-reporting. Bots, pumpers and the stream failing at peak moments come next ([Trustpilot](https://www.trustpilot.com/review/www.stocktwits.com)). Independent research backs up the anecdotes:

- **Bots and manipulation.** A December 2025 working paper matched ~80M StockTwits posts to 56,000+ NASDAQ manipulation alerts. Isolating the posts made by bots **nearly doubled their measured effect on manipulators' profits**. This comes from a secondary summary, not the paper itself ([Swedroe](https://larryswedroe.substack.com/p/social-media-noise-and-stock-manipulation)).
- **Echo chambers.** A peer-reviewed study of ~400,000 users found that bulls were **~5x more likely** than bears to follow a bullish user. Users inside these echo chambers earned lower returns afterwards ([Cookson et al.](https://rady.ucsd.edu/faculty/directory/engelberg/pub/portfolios/ECHO_CHAMBERS.pdf)).
- **Detection left to users.** StockTwits' own help center tells users to spot pump-and-dumps by watching for "many new or low-activity accounts" posting the same bullish message ([Stocktwits Help](https://help.stocktwits.com/c/best-practices/community-guidelines/spotting-scams)).
- **A live SEC case.** The SEC alleges that a 60K-follower StockTwits account touted a Nasdaq-listed biotech while secretly selling it ([SEC](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26187)).

The structural problem is money. A business of roughly $10M that has stopped raising capital and dropped trading revenue has to sell attention. Its buyers are exactly the parties who want to be seen on hot tickers:

- Tradr ETFs, an issuer of leveraged and inverse ETFs, was the title partner of Stocktoberfest 2026, alongside microcap sponsors.
- The Gemini exchange is built into StockTwits' crypto coin pages ([FinanceFeeds](https://financefeeds.com/stocktwits-launches-cryptotwits-to-serve-10-million-users/)).
- Lindzon has pitched public companies "premium message placement" on their own ticker pages ([Howie Town](https://www.howardlindzon.com/p/stocktwits-investor-relations-claim-ticker-today)).

Fixing the integrity problem completely would mean turning that revenue away.

| Part of the claim | Verdict | Evidence |
|---|---|---|
| "StockTwits is a shit product" | **Wrong for its core users, right about trust.** | 4.8 on iOS from ~167K ratings vs 1.3 on Trustpilot from 82 reviews; complaints concentrate on moderation, bots and pumpers ([Trustpilot](https://www.trustpilot.com/review/www.stocktwits.com)) |
| "StockTwits is weak" | **Partly true.** It is small, flat, swings with the market and depends on sponsors, but it owns the habit and the archive | Revenue estimated at $5–25M; traffic estimates falling; no priced round since 2021 |
| "Nothing really competes" | **Wrong.** At least six venues compete, and two shipped StockTwits' core loop in 2026 | X cashtags plus Trade button; Robinhood Social open to all eligible US customers; Reddit/ICE; paid Discords |
| "TickerHall's features are new" | **Mostly wrong, with one exception.** People-based attention counts (Watchers), quality ranking (Top Voices), bull/bear tags, published House Rules, earnings tools and an MCP already exist. A complete scored record of calls does not | [BriefGlance](https://briefglance.com/articles/stocktwits-doubles-down-on-social-overhauling-its-core-experience); [ai.stocktwits.com](https://ai.stocktwits.com/) |

In one line: StockTwits is a mediocre product that people use out of habit. It has an integrity problem that its revenue model discourages it from fixing, and its real competition is now X and Robinhood.

## X and Robinhood rebuilt StockTwits' core loop in 2026

StockTwits invented the ticker page with live chatter in 2008, and this year that loop became standard. On **April 14, 2026** X launched Smart Cashtags in the US and Canada: tapping a $ticker opens a live chart and related posts ([Tech Times](https://www.techtimes.com/articles/315918/20260416/x-launches-cashtags-live-stock-crypto-charts-turns-social-feed-real-time-trading-hub.htm)). On **September 16** it added a Trade button that sends US users to Interactive Brokers, Moomoo, Gemini, Kraken or Coinbase, and Webull joined on October 2 ([TechCrunch](https://techcrunch.com/2026/09/16/x-will-now-let-u-s-users-trade-via-cashtags/); [Finance Magnates](https://www.financemagnates.com/forex/brokers/webull-joins-x-cashtag-program-as-social-feed-adds-broker-links/)).

Robinhood went further on credibility. Robinhood Social gives every profile a KYC-verified identity, posts trades as they are verified, and shows P&L and profit rate. It went from a 1,000-user beta in March to **all eligible US customers between September 29 and October 13, 2026**, inside an app with **28.4M funded customers**. Posts carry a "Quick trade" button, and there is a live earnings-call experience ([Robinhood Newsroom](https://robinhood.com/newsroom/robinhood-social-beta/); [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/robinhood-expands-social-trading-push-000800407.html); [CoinSpectator](https://coinspectator.com/mainstream/2026/10/14/robinhood-lets-all-eligible-us-customers-share-their-trades-and-portfolios/)). Robinhood pitches it explicitly against fake trades, wash trading and "Telegram-style signal scams" ([Investing.com](https://www.investing.com/news/transcripts/robinhood-at-hood-summit-26-pushes-trading-into-living-hours-93CH-4923894)). That is TickerHall's trust language, backed by tens of millions of customers.

| Venue | Scale (label) | 2025–26 move | Where it beats StockTwits | Threat to TickerHall |
|---|---|---|---|---|
| X / FinTwit | Largest open audience; no official finance figure | Smart Cashtags (Apr 2026); Trade button with 6 brokers (Sep–Oct 2026); creator revenue sharing ended Sep 7, 2026 ([TechCrunch](https://techcrunch.com/2026/09/16/x-will-now-let-u-s-users-trade-via-cashtags/)) | Reach, creators, breaking news | Very high for attention, low for trust |
| Robinhood Social | 28.4M funded customers; how many use Social is undisclosed ([CoinSpectator](https://coinspectator.com/mainstream/2026/10/14/robinhood-lets-all-eligible-us-customers-share-their-trades-and-portfolios/)) | Beta Mar 2026; all eligible US customers Sep 29–Oct 13, 2026 | KYC identity, trades and P&L verified live, one-tap trading | Very high |
| Reddit | r/wallstreetbets ~19.9M subscribers (third-party count) ([Wikipedia](https://en.wikipedia.org/wiki/R/wallstreetbets)) | ICE "Reddit Signals and Sentiment" (Jan 2026); Reddit Answers at 15M weekly users | Long-form research posts (DD), meme rallies, scale | High, on both audience and data |
| Paid Discord / Whop | Groups of ~5K–14K members at ~$60–$280/month (Whop's own promotional figures) ([Whop](https://whop.com/blog/trading-discord-servers/)) | Whop building its own chat and livestreams | Real-time chat, trade alerts, mentorship, creator income | Medium-high for active traders; also a channel to partner with |
| eToro | 4.28M funded accounts, Q2 2026 ([eToro](https://www.etoro.com/news-and-analysis/press-releases/etoro-reports-second-quarter-2026-results/)) | US copy trading in a phased rollout; buying TradeZero | Social that pays: traders others copy earn up to 1.5% a year of the assets copying them ([eToro](https://www.etoro.com/copytrader/popular-investor/)) | Medium; small in the US today |
| Webull / Moomoo | 28.2M / 31.25M registered users ([Finance Magnates](https://www.financemagnates.com/forex/brokers/webull-joins-x-cashtag-program-as-social-feed-adds-broker-links/); [Futu](https://www.moomoo.com/community/feed/futu-announces-q2-2026-results-strong-results-across-global-markets-117126789726214)) | Joined X's cashtag program instead of building their own | A community inside the broker | Low-medium; more likely buyers than rivals |
| Blossom Social | 750K+ members, ~$6.5M annualized revenue (company claims) ([BetaKit](https://betakit.com/blossom-social-raises-more-than-2-million-through-frontfundr-campaign/)) | Raised ~$2M in two hours by crowdfunding, Jun 2026 | Verified portfolios, education, free-plus-paid tiers | Medium; the closest independent rival |
| TradingView | 40M+ monthly users (company figure, 2022) ([TradingView](https://www.tradingview.com/chart/AMZN/EAksOtab-Help-us-build-a-better-social-network/)) | Public trade ideas fell from 771,813 (2024) to 383,555 (2025) | Charts as content, user-written scripts | Medium for technical traders |
| Public | — | Shut its social feed Jun 5, 2025, citing AI ([Finance Magnates](https://www.financemagnates.com/forex/publiccom-terminates-social-trading/)) | — | A warning, not a rival |
| AI assistants | ChatGPT's Finances feature opened to US free users Oct 2, 2026 ([OpenAI](https://openai.com/index/personal-finance-chatgpt/)); Robinhood's Cortex 1M+ users ([Motley Fool](https://www.fool.com/investing/2026/01/03/here-are-3-financial-stocks-making-big-ai-moves-in/)) | Google Finance AI available globally from ~Jun 2026 ([Yahoo Tech](https://tech.yahoo.com/article/google-finance-gets-an-ai-powered-overhaul-160005769.html)) | "Why is it moving", recaps, screening | High for information jobs; none score crowd calls |
| Sentiment-data vendors | ICE/Reddit, LSEG MarketPsych, Stockpulse; developer APIs ~$0–$600/month ([Adanos](https://adanos.com/insights/blog/best-stock-sentiment-apis-2026/)) | ICE's Reddit product live Jan 2026 | Distribution to institutions, long history | High for raw sentiment; none sell scored retail calls |

Three of these deserve more than a table row.

**Reddit and ICE.** Reddit's finance subreddits far outnumber StockTwits on membership. In February 2025, ICE (which owns the NYSE) licensed Reddit's data API to build products for capital markets ([Business Wire](https://www.businesswire.com/news/home/20250211782623/en/Intercontinental-Exchange-and-Reddit-Collaborate-to-Create-and-Distribute-Data-Products-for-Capital-Markets)). On **January 28, 2026** ICE launched "Reddit Signals and Sentiment". It provides live and historical sentiment scores, a daily map of which stocks are mentioned together, and mapping to individual securities, all on ICE's institutional data feed ([ICE](https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-Launches-Reddit-Signals-and-Sentiment-Tool-Providing-Actionable-Market-Indicators-for-Investors/default.aspx)). LSEG MarketPsych, owned by the London Stock Exchange Group, scores "tens of millions of authors" ([LSEG](https://www.lseg.com/en/data-analytics/financial-data/analytics/marketpsych-analytics)). Between them, exchange and market-data operators now own "retail sentiment" as an institutional product.

**Paid Discords.** These groups hold the traders worth the most, people paying $60–$280 a month, and they sell track records nobody can audit. Separately, X ended Creator Revenue Sharing in September ([tech-ish](https://tech-ish.com/2026/08/08/x-is-scrapping-creator-revenue-sharing-on-7-september-everyone-has-to-apply-again/)), which left finance creators looking for both credibility and income.

**AI assistants.** They have taken over the commodity half of stock chat. Public shut its social feed because recaps and market updates were now "created by AI—faster, more accurate" ([Finance Magnates](https://www.financemagnates.com/forex/publiccom-terminates-social-trading/)). None of the major assistants shows crowd sentiment on its own. It reaches them through MCP connectors, led by StockTwits' own and by Stockpulse's ([Stockpulse](https://stockpulse.ai/mcp-server/)).

Further out, Seeking Alpha, Yahoo Finance's per-ticker "Conversations" boards and Bluesky's new cashtags compete less directly.

| Threat | Live since | What it takes from TickerHall | How fast it could copy TickerHall's openings | Response |
|---|---|---|---|---|
| Robinhood Social | Sep 29–Oct 13, 2026 | The "verified track record" claim for 28.4M funded customers; social around earnings week | Forcing complete, unhideable records is a settings change it could make in weeks, but it would cut posting. It can never verify other brokers' customers | Position on "complete and open to anyone": record forecasts rather than positions, and show % returns only |
| X Smart Cashtags + Trade | Apr 14 / Sep 16, 2026 | The ticker page, chatter and trade button together; creators' audiences | Could add call scoring within a quarter, but its incentives favor engagement and broker links | Use X for distribution: every card carries its $cashtag |
| StockTwits' official MCP | 2026, exact date undisclosed | The "first stock-chat MCP" press story; the sentiment-to-AI slot | Adding a per-user accuracy tool takes weeks, and it could score 17 years of tagged posts after the fact (inference) | Launch an MCP only as a track-record product, once ≥90 days of scored calls exist |
| Reddit/ICE (+LSEG) | Deal Feb 2025; product Jan 28, 2026 | Any B2B plan built on "retail sentiment" | Already far ahead on raw sentiment | Sell calls weighted by accuracy, not sentiment |
| AI assistants | ChatGPT Finances free to US users Oct 2, 2026 | Recaps, "why it's moving", summaries | Not applicable | Don't build summaries; become the source they cite |

## Only a complete, neutral record of who was right is unclaimed

A real opening has to pass two tests: nobody serves it today, and the incumbents' business models make copying it costly. Features alone fail the second test, because StockTwits could build any TickerHall mechanic in weeks. What incumbents cannot adopt cheaply is completeness and neutrality, because each of them earns money from the opposite. StockTwits earns from sponsors who want to be seen. Robinhood earns from trades, and from users relaxed enough to keep posting. X earns from engagement and broker links. The table below ranks openings by size, by durability, and by fit with what TickerHall has already designed.

| Rank | Opening | Evidence it is open | Who could copy, how fast | Durability |
|---|---|---|---|---|
| 1 | **A complete ledger of scored calls**: every call stamped with the price at posting, scored against a benchmark after a fixed period, and never deletable or hideable | Robinhood users "choose which eligible transactions to share" and "can turn off profile trading statistics" ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/robinhood-expands-social-trading-push-000800407.html)); StockTwits' MCP exposes no accuracy data ([ai.stocktwits.com](https://ai.stocktwits.com/)); the closest MCPs found rank prediction-market or crypto traders, not stock pickers ([mcp.so](https://mcp.so/servers/polymarket-mcp-server-mrlarryjohnson111)) | **StockTwits:** weeks to a quarter, and it could score 17 years of tagged posts after the fact (inference). **Robinhood:** weeks technically, but forced completeness would cut posting. **X:** a quarter or more, with little sign of interest | Medium. The feature can be copied; a neutral ledger several years deep cannot |
| 2 | **Zero paid visibility**, with a published money policy and enforcement users can see (rule cited, appeal offered, protection from mass-reporting) | StockTwits' sponsor roster and its pitch of "premium message placement" to companies ([Howie Town](https://www.howardlindzon.com/p/stocktwits-investor-relations-claim-ticker-today)); Trustpilot complaints center on unexplained bans ([Trustpilot](https://www.trustpilot.com/review/www.stocktwits.com)) | Technically days; economically very unlikely for StockTwits or X | High, as long as TickerHall never takes money from listed companies or brokers |
| 3 | **Credibility that works across brokers and is based on forecasts**: anyone can make a call, including a bearish one without shorting, scored on % moves with no dollar P&L shown | Robinhood Social is for its customers only, bars licensed professionals, and cannot post futures or multi-leg options trades ([CoinSpectator](https://coinspectator.com/mainstream/2026/10/14/robinhood-lets-all-eligible-us-customers-share-their-trades-and-portfolios/)); eToro now lets users copy only its approved "Popular Investors" ([FX News Group](https://fxnewsgroup.com/forex-news/retail-forex/etoro-updates-copytrader-to-permit-copying-of-popular-investors-only/)) | **Robinhood:** structurally never. **Blossom or StockTwits:** about a quarter | High against brokers, medium against independents |
| 4 | **A proof layer for creators and paid communities**: cards, embeds and a Discord bot that record calls made elsewhere | Whop groups charge $60–$280/month on claims nobody can audit ([Whop](https://whop.com/blog/trading-discord-servers/)); X ended creator revenue sharing ([tech-ish](https://tech-ish.com/2026/08/08/x-is-scrapping-creator-revenue-sharing-on-7-september-everyone-has-to-apply-again/)) | **Whop or X:** about a quarter | Medium; being first into these communities matters |
| 5 | **Track-record data for AI agents and fintechs** (API, MCP, or a feed other companies run under their own brand) | TipRanks, which ranks experts by accuracy, reaches ~50M users through partners ([Yahoo Finance](https://finance.yahoo.com/news/fintech-firm-tipranks-majority-stake-172211344.html)); Estimize sells crowd earnings forecasts through IBKR, WRDS and QuantConnect ([ExtractAlpha](https://extractalpha.com/2024/12/03/extractalpha-collaborates-with-interactive-brokers-to-integrate-estimize-data-into-trading-platforms/)) | **StockTwits:** weeks to add an MCP tool | Low as a feature; it is only as durable as opening #1 |
| 6 | **Sentiment that resists gaming**: The Floor, one Lean per person, the 7-day rule | StockTwits tells users to watch for new accounts posting identical bullish messages ([Stocktwits Help](https://help.stocktwits.com/c/best-practices/community-guidelines/spotting-scams)); bot posts amplify manipulators' profits ([Swedroe](https://larryswedroe.substack.com/p/social-media-noise-and-stock-manipulation)) | **StockTwits:** weeks; its Watchers metrics already count people | Low; basic hygiene, not a moat |

**Why the ledger comes first.** The evidence says the useful signal in crowd sentiment comes from weighting people by their accuracy, and nobody publishes that for retail investors. A study of ~30M StockTwits messages found that sentiment predicted returns, but less so from users who spread themselves across many stocks ([Institutional Investor](https://www.institutionalinvestor.com/article/2bsx05fv46nw5bkj7bu2o/portfolio/the-power-of-social-media-in-predicting-stock-returns)). WallStreetBets research posts predicted returns before GameStop and stopped doing so afterwards, as posts chased attention ([EBSCO](https://www.ebsco.com/articles/business-and-management/cf6a3620-b1a9-5907-94b9-b492bd0db320/place-your-bets-the-value-of-investment-research-on-reddit-s-wallstreetbets)). Unweighted crowd sentiment decays; knowing who has been right is the signal that lasts.

The main danger is StockTwits itself. It holds timestamped, self-tagged bull/bear posts going back years. It could compute each user's hit rate after the fact and launch a deeper track-record database than TickerHall can build for years. This is inference: there is no public record of whether StockTwits' tags and deletion policies would allow clean scoring. TickerHall's answer has three parts: speed, a stricter method (no deletes, a fixed scoring period, returns measured against a benchmark, published rules), and a neutrality StockTwits cannot claim while it sells sponsored placement.

**Neutrality is the most durable opening, because copying it costs incumbents revenue.** StockTwits' 2026 sponsors run from a leveraged-ETF title partner to microcap companies. X's Trade button was presented by its global advertising head ([TechCrunch](https://techcrunch.com/2026/09/16/x-will-now-let-u-s-users-trade-via-cashtags/)). A public money policy (no sponsored posts, no paid trending, no paid placement for listed companies, no broker buttons) can be checked by anyone in a way StockTwits' House Rules cannot. Pair it with enforcement users can see: cite the rule that was broken, offer an appeal, and stop mutes triggered by mass-reporting, which is the angriest complaint in StockTwits' reviews.

**Broker neutrality is the opening against Robinhood.** Robinhood's verified trades are a stronger signal than free calls, because money on the line beats talk. But they cover one broker's customers, exclude licensed professionals, reveal P&L per position when shared, and record positions rather than forecasts. TickerHall can score anyone's view on percentage moves alone, including a bearish call from someone who never shorts.

**The creator layer and the data layer are how the ledger spreads and earns money.** Paid Discord operators and FinTwit creators sell on claims nobody can audit. A neutral record they can embed in a Whop page or an X bio is worth most to the honest ones. A /call bot inside their servers turns their communities into TickerHall's supply of calls. Data comes last because buyers want years of history. StockTwits and Estimize each sell more than a decade of it. An MCP is a way to reach users, not a source of revenue.

**What is not an opening.** Several parts of the current TickerHall pitch should stop being treated as differentiators:

- **Cashtag pages with charts and chatter.** These are free on X.
- **"Why it's moving" summaries.** Cortex, Google Finance and StockTwits itself already provide them.
- **Earnings threads.** They compete with StockTwits' earnings tools, Polymarket's earnings markets, and Robinhood's live earnings-call feed with one-tap trading.
- **A bull/bear meter.** It is a commodity that developer APIs sell for $0–$600 a month.
- **Published rules.** StockTwits already publishes House Rules; enforcement users can see is what would set TickerHall apart.
- **An MCP that serves sentiment.** It would copy StockTwits' official server.

Keep all of these as hygiene, but spend no build time competing on them.

## Lead with call cards, count callers, sell data last

### A receipt beats a room on day one

StockTwits' moat is density per ticker. When news hits a small cap, the live conversation is already there, and a new room with better rules loses that race until it fills up. A scored call does not need a full room. The first caller gets value on day one because the record travels.

The unit is a card showing the ticker, the direction, the price at posting and the timestamp. A week later, a result card shows the return against the S&P 500 (SPY) and the caller's running hit rate. Callers post these where their audience already is. On X, a post carrying the $cashtag now opens a live chart and joins that ticker's related-posts stream ([Tech Times](https://www.techtimes.com/articles/315918/20260416/x-launches-cashtags-live-stock-crypto-charts-turns-social-feed-real-time-trading-hub.htm)), so a TickerHall card would ride X's own cashtag product (inference).

The first customer to win is the caller who has an audience to prove something to: mid-size FinTwit accounts, people who write research posts on Reddit, and Discord operators. Passive readers come later, through the cards. Chat, The Floor and Lean still launch, but as the room around the scoreboard, not the reason to come.

Two changes to the launch list follow:

- **Don't lead with $SLS.** Lead the public Floor with liquid, high-attention names that report earnings that week. Small caps are where the manipulation evidence concentrates. The working paper on bots studied stocks under $2B, and the SEC's case involved a StockTwits account touting a Nasdaq-listed biotech ([SEC](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26187)). A pre-launch stock-chat app led by one small-cap biotech will look like a promotion vehicle to the skeptical traders it needs.
- **Disclose founder positions.** Every founder should publicly disclose positions in launch-list tickers. That disclosure is itself proof of "no one pays to be seen".

### Build the ledger now, the room later

| Horizon | Build | Why |
|---|---|---|
| Now, before launch (~12 weeks) | Calls that can't be edited, priced by a published rule from a feed you have rights to display; one-week scoring with hit rate and return vs SPY; a full public record with no delete or hide; rankings only after ≥10 scored calls; auto-generated call and result cards; weekly leaderboards per ticker and overall; one account per person plus the 7-day rule; Lean and The Floor; public ticker pages ("who's been right on $X"); published moderation and money policies, with every enforcement action citing a rule and allowing appeal | This is the scoreboard plus the trust layer, and everything else depends on it |
| Next (months 3–9) | A Discord /call bot; an embeddable record widget for bios and newsletters; alerts when top-scored callers act on a ticker in your watchlist (the hook for the paid tier); 1-month and 3-month scoring periods; a track-record MCP/API once ≥90 days of scored calls exist | Reaches creator communities, creates the first paid feature, and gives the AI press moment real data behind it |
| Later (year 2+) | A feed other companies run under their own brand; a historical dataset sold through quant-data distributors; an optional read-only brokerage link for a "verified holder" badge (untested; cost and regulatory treatment not researched) | Needs history, legal review and sales capacity |
| Never | Sponsored posts, paid trending, paid placement for listed companies, broker Trade buttons or affiliate links, AI recap feeds | Each one breaks neutrality, or competes where AI and X already win |

This changes one piece of the existing plan. An MCP launch is no longer a first: StockTwits' page says its official server is already in Claude's and ChatGPT's app directories, though those listings could not be checked independently ([ai.stocktwits.com](https://ai.stocktwits.com/)). The press story works only as "the first MCP that tells an AI agent who has actually been right on $X". It also needs 90+ days of scored calls before the answer means anything. Expect StockTwits to respond within a quarter; the launch is a way to get attention, not a moat.

The same logic makes public ticker pages the better way to get into AI answers. ChatGPT Finances, Google Finance's Deep Search and Reddit Answers all need sources to cite. A ranked, dated list of who called $X correctly is content no assistant can generate for itself (inference).

### Weekly active callers is the only number that matters

Make **weekly active callers (WAC)** the core metric: distinct accounts at least seven days old that made at least one call that week. In a scoreboard business, callers are the supply. Every leaderboard, result card, "who was right" post, AI citation and future dataset comes from them. Members and sign-ups don't count until they make calls.

Track three guardrails next to WAC:

- **Four-week caller retention:** how many callers are still calling four weeks later.
- **Share rate:** cards posted off-platform per call made.
- **Retention of below-median callers.** A complete record will make most callers look average or worse. Robinhood's decision to let users hide their stats hints that full exposure discourages posting (inference).

To counter that, rank callers only after a minimum number of calls, add per-ticker and "most improved" boards that create many winners, and show percentiles rather than raw losses on profiles.

### Money comes from readers and data buyers, never from the people being seen

"No one pays to be seen" leaves room for three revenue sources: readers paying to see better, platforms paying to integrate, and data buyers paying for history.

- **Year one:** charge nothing.
- **Months 9–15: TickerHall Pro at roughly $9–12/month** (my estimate). It would offer real-time alerts when top-scored callers act on your watchlist, full stats, filters and exports. Callers' records stay free forever. Price anchors:
  - Blossom PRO costs $8.99/month, with ~10% of its monthly active users subscribing (company claim, unaudited) ([FrontFundr](https://www.frontfundr.com/blossomsocial2026)).
  - StockTwits charges $7.99 for Plus and $22.95–$29.99 for Edge ([WallStreetZen](https://www.wallstreetzen.com/blog/stocktwits-review/)).
  - Quiver Premium costs $25 ([Quiver](https://www.quiverquant.com/premium-vs-api/)).
- **Year two onward: sell to businesses.** Three lines:
  - A "verified retail track records" feed that brokers and fintechs without their own social network run under their own brand. This is the TipRanks model.
  - Commercial API/MCP tiers in the market's ~$0–$600/month range ([Adanos](https://adanos.com/insights/blog/best-stock-sentiment-apis-2026/)).
  - Once there are 2+ years of history, a dataset sold to quant funds through distributors, as Estimize does through WRDS, QuantConnect and IBKR ([QuantConnect](https://www.quantconnect.com/data/extractalpha-estimize)).

Run the numbers before believing in subscriptions alone. At $10/month, **$1M in annual recurring revenue needs ~8,300 subscribers, or ~83K–167K monthly active users** at 5–10% conversion. **$10M a year needs ~0.8–1.7M monthly active users**, about the 1M StockTwits reported at its 2021 peak, its only disclosed MAU figure ([Bloomberg Law](https://news.bloomberglaw.com/private-equity/social-media-platform-stocktwits-nabs-210-million-valuation)). These are my estimates.

Data alone has a ceiling too:

- The average alternative dataset sold to investment firms has **~20 clients** ([Neudata](https://www.neudata.co/blog/state-of-the-alternative-data-market-2026)).
- Buyers spend roughly **$80K per dataset** ([Hedgeweek](https://www.hedgeweek.com/hedge-funds-gear-up-for-a-2025-alternative-dataset-budget-boom/)).
- The average dataset earns about **$1.1M a year** ([Neudata](https://www.neudata.co/education/how-big-is-the-alternative-data-market-for-investment-managers)).

The path to scale therefore runs through other companies distributing the ledger. TipRanks reaches **~50M users through bank and broker partners, against ~6M directly** ([Yahoo Finance](https://finance.yahoo.com/news/fintech-firm-tipranks-majority-stake-172211344.html)). The natural buyers are brokers that chose to rent X's cashtag traffic rather than build social, and that now face Robinhood Social (inference).

### Milestones run from a private beta to a 2028 data business

All dates and thresholds below are my targets, not forecasts.

| Target date | Milestone | Gate |
|---|---|---|
| Now–Nov 2026 | Equity and vesting signed; scoring engine, cards and profiles built; recruiting starts | — |
| Dec 2026–mid-Jan 2027 | Private beta: ~100 recruited callers make real calls, so leaderboards have weeks of scored history on launch day | Gate 0 |
| Late Jan–Feb 2027 | Public launch into the Q4 earnings season; weekly "who was right" content running | — |
| ~May 2027 (day 90) | ≥100 WAC, ≥1,000 members, ≥30% four-week caller retention, ≥10% share rate | Gate 1 |
| Q3 2027 | Discord bot and embeds live; track-record MCP/API launched as the press moment; ~500 WAC; a pre-seed round or community crowdfund closed; one founder full-time | Gate 2 |
| Q1 2028 | Pro launched; 2,000+ WAC; first business pilot with a broker or fintech | Gate 3 |
| 2029+ | 2+ years of scored history; data and white-label revenue; acquisition conversations | — |

The private beta is the most important change to the launch plan. Launching an empty scoreboard wastes the earnings-week moment. Launching with eight weeks of real records gives the first press coverage and the first carousels actual winners and losers.

For the Gate 2 raise, community crowdfunding has worked in this category. Blossom raised $2.89M from 1,207 investments ([FrontFundr](https://www.frontfundr.com/case-studies/blossom-social)), and Prospero.ai ran a campaign on Republic ([Business Wire](https://www.businesswire.com/news/home/20251030313761/en/Prospero.ai-Nears-Close-of-Equity-Crowdfunding-Campaign-on-Republic-Final-Day-to-Join-the-AI-Investing-Revolution)). The first 1,000 Founder members are the natural first investors.

### Base rates say acquisition, and that is a fine outcome

The category's record is sobering:

- **Commonstock**, the social network built on verified portfolios, was folded into Yahoo Finance in 2023 ([Axios](https://www.axios.com/2023/08/23/commonstock-yahoo-social-investing-platform)).
- **Atom Finance** was bought by Toggle in 2024, and its site is gone ([PYMNTS](https://www.pymnts.com/acquisitions/2024/toggle-ai-acquires-atom-finance-to-bolster-investment-platform/)).
- **Shares** pulled out of the UK in 2024 ([BusinessCloud](https://businesscloud.co.uk/news/social-investing-app-shares-shutters-uk-business/)).
- **Public**, once "the social investing app", shut its feed in 2025.

The ceiling for companies that only do this is modest:

- **TipRanks** reached a **~$200M valuation after more than a decade** ([Finance Magnates](https://www.financemagnates.com/forex/tech-firm-prytek-completes-200m-buyout-of-investment-platform-tipranks/)).
- **Estimize** ended up inside a small quant-signals vendor.
- **StockTwits'** last valuation was $210M, in 2021.
- **Blossom** is at ~$6.5M in annualized revenue.
- **eToro**, with **$868M of FY2025 net contribution**, is the exception, and it is a broker: it makes money from social through brokerage and copy trading ([eToro](https://investors.etoro.com/news-releases/news-release-details/etoro-reports-fourth-quarter-and-full-year-2025-results)). TickerHall will not do that.

What could make TickerHall different is the combination, not any one feature:

- It is useful to a single caller, so it does not need a dense room to start.
- Its main asset, a scored history, grows more valuable with time.
- Its neutrality is something incumbents cannot adopt without losing revenue.
- It reaches people through X, Reddit and Discord instead of fighting them.

Even then, the most likely good outcome is an acquisition in years three to five, by a broker without its own social product, by a ratings or data firm, or by StockTwits itself. So build to be acquirable: a clean scoring method, clear rights to the data, clean compliance.

For your stake, illustratively and not as a forecast: a $20–50M sale, with your 10% diluted to ~7%, returns about $1.4–3.5M. A TickerHall-sized version of the TipRanks outcome ($200M) returns about $14M. Either would arrive four to seven years out. That is real money, but it is not "millions per year", and it is why PostDose cannot be the thing that gives.

### Two legal checks before launch

The research did not cover how US securities rules treat scored public calls, leaderboards of "top callers", or paid alerts that tell subscribers when a top caller acts. Get a securities lawyer's view before Pro ships.

Paid stock promotion on these boards must disclose who paid and how much, and the SEC has acted against undisclosed paid touting ([SEC](https://www.sec.gov/enforce/33-10953-s)). Regulators are watching the category: FINRA reported in December 2025 that 24% of investors, and 35% of those under 30, get investing information from social media ([FINRA](https://www.finra.org/sites/default/files/2025-12/2025-social-media-influenced-investing.pdf)). A strict ban on paid promotion, disclosed founder positions and enforcement users can see are both the product promise and the compliance stance.

## PostDose gets 22 of your 30 hours; TickerHall gets 8

The economics favor PostDose. TickerHall will produce no cash for at least a year, your 10% will be diluted, and the best case pays out years from now. PostDose is the business that can make millions a year.

You have about **30 hours a week for both companies combined**. The recommended default is **22 hours on PostDose and 8 on TickerHall**, roughly a 73/27 split. TickerHall rises to 12 only during a launch sprint of three weeks or less. Over the ~28 weeks to Gate 1, that gives TickerHall about **230 hours**. That is enough for you to recruit the first callers, run the launch content and write the specs for the shareable features, while your co-founder carries the build. PostDose can hold its output on 22 hours only if a VA takes over production and posting, so hiring one is part of the plan, not an option.

| Company | Block | Hours/week | What goes in it |
|---|---|---|---|
| **PostDose (22)** | Revenue and growth | 9 | Offers, funnel and copy, partnerships: whatever directly produces income |
| | Content system | 8 | One ~6-hour batch session producing a week of carousels through the locked pipeline; a 1-hour weekly trend scan; 1 hour approving the VA's output |
| | Operations and analytics | 3 | Managing the VA, weekly metrics review |
| | Buffer | 2 | Absorbs a bad week without eating TickerHall's hours |
| **TickerHall (8)** | Recruiting callers | 3 | DMs and calls to the first 100 callers, then creators and Discord operators |
| | Content batch | 2.5 | Weekly leaderboard and "who was right" carousels, made right after the PostDose batch while the workflow is fresh, under a separate brand |
| | Product specs and metrics | 1.5 | Specs for cards, profiles, leaderboards and ticker pages; the weekly WAC report |
| | Co-founder sync | 1 | The weekly 45-minute priorities meeting plus follow-ups |

PostDose has to hold its output on 22 hours, and its locked carousel system makes that possible:

- **Batch and schedule.** Produce a full week of carousels in one session through the existing prompt pipeline, and schedule them a week ahead in each platform's own scheduler.
- **Scan weekly.** Move trend scanning from daily to a weekly routine that feeds the batch.
- **Hire a part-time VA (10–15 hours a week).** The VA assembles slides and checks them against the brand system, posts, sorts comments and DMs, and compiles a one-page weekly metrics sheet. Write a two-page set of instructions before handing over.
- **Keep the four things that drive money and risk:** the offer and funnel, final approval of hooks, review of every health claim, and partnerships.

If PostDose's margins cannot pay for a VA, that alone tells you PostDose needs your hours more than TickerHall does. Reuse the same content machine for TickerHall's weekly leaderboard and "who was right" carousels, but keep the two brands, their accounts and their audiences completely separate.

| Area | Owner | Why |
|---|---|---|
| Recruiting callers (the first 100, then creators and Discord operators) | You | Distribution is your edge; it runs on DMs and relationships |
| Content engine: weekly leaderboards, "who was right" carousels and short videos | You, run as a system like PostDose | It is the machine you already operate |
| Specs for the shareable surfaces: call cards, profiles, leaderboards, ticker pages written for AI search | You | These are the product features you were brought in for |
| Weekly metrics report (WAC, retention, share rate) | You | Keeps the gates honest |
| Engineering, infrastructure, price data, scoring accuracy | Co-founder | The ledger's integrity is the product |
| Moderation, enforcement and appeals | Co-founder, working from the published rules | Needs a daily presence you won't have |
| Legal, compliance, entity and equity paperwork (Mobilize Cloud LLC) | Co-founder, with outside counsel | It is the owner's entity |
| Fundraising and partnerships with businesses and data buyers | Co-founder leads; you supply the metrics story | Later-stage work |
| Launch timing, gate reviews, pricing | Joint | Decided in a weekly 45-minute sync |

Settle equity before your hours ramp up. Ten percent is defensible for a part-timer with capped hours, so instead of arguing about hours, tie the upside to the gates. Illustrative terms: 10% vesting over four years with a one-year cliff, plus kickers of about 5% at Gate 1 and Gate 2. Make sure the grant sits in the entity that owns TickerHall, whether that is Mobilize Cloud LLC or a separate TickerHall company. Record it in an amendment to the operating agreement, with an assignment of your intellectual property, not a verbal promise. If Gate 2 arrives and neither founder will go full-time, TickerHall is a side project and should be sized and valued as one.

All thresholds below are my targets.

| Checkpoint | Continue if | Iterate (one 60-day cycle) if | Stop or drop to maintenance if |
|---|---|---|---|
| Gate 0: launch readiness (mid-Jan 2027) | Equity signed; ≥100 beta callers with ≥3 scored calls each; cards and scoring live | 50–99 callers: move launch to the next heavy earnings week | <50 callers or equity unsigned: don't launch and don't add hours |
| Gate 1: day 90 (~May 2027) | ≥100 WAC; ≥1,000 members; ≥30% of callers active in week 4; ≥10% of calls shared off-platform | 50–99 WAC, or share rate of 3–10% | <50 WAC or share rate <3%: leave the operating role and keep vested equity |
| Gate 2: months 6–9 (Q3 2027) | ≥500 WAC growing ≥10% a month with no paid ads; raise closed; one founder full-time | Growth positive but under 10% a month | WAC flat or falling two months running |
| Gate 3: months 12–15 (Q1 2028) | Pro converts ≥3% of monthly active users, or a business pilot is signed | Only one of the two | Neither |
| PostDose tripwire (checked weekly) | Revenue within 15% of the baseline set before TickerHall ramped; posting cadence on target | — | Revenue down >15% over the trailing 4 weeks, cadence missed 2 weeks running, or TickerHall above 12 hours for 3 weeks: cut TickerHall to 4 hours until PostDose has 2 good weeks in a row |

Your 30 hours should move between the companies only at these checkpoints, and only in the direction the evidence points.

| Phase or checkpoint result | PostDose hours | TickerHall hours | Condition |
|---|---|---|---|
| Now to Gate 0 (build and private beta, through mid-Jan 2027) | 22 | 8 | The default |
| Launch sprint (3 weeks at most, late Jan–Feb 2027) | 18 | 12 | Gate 0 passed, and three weeks of PostDose content scheduled in advance |
| Launch to Gate 1 (Feb–May 2027) | 22 | 8 | Back to the default after the sprint |
| Gate 0 missed, or equity unsigned | 26 | 4 | Recruiting and specs only, until both are fixed |
| Gate 1 passed | 20 | 10 | PostDose revenue within 15% of baseline |
| Gate 1 "iterate" (one 60-day cycle) | 22 | 8 | No extra hours for a product that hasn't proven itself |
| Gate 1 failed | 28–30 | 0–2 | Leave the operating role, keep vested equity, advise occasionally |
| Gate 2 passed (raise closed, one founder full-time) | 16 | 14 | Only if PostDose holds revenue on 16 hours for a month, **and** a matching equity kicker or salary is signed |
| Gate 3 passed | 12–16 | 14–18 | Only if TickerHall pays you; at this point the real decision is whether to go full-time on it |
| PostDose tripwire hit (any phase) | 26 | 4 | Until PostDose has two good weeks in a row |

## Conclusion

TickerHall is not really racing StockTwits' 10M accounts. It is racing the moment an incumbent adds scoring. StockTwits could score years of tagged posts after the fact, and Robinhood could make records complete with a settings change. What protects TickerHall is the one combination incumbents cannot adopt without hurting their own revenue: complete records (which costs Robinhood posting volume), no paid visibility (which costs StockTwits and X their sponsors and broker partners), and neutrality across brokers (which no broker can offer). That makes "no one pays to be seen" the moat itself, not a slogan. The first sponsored placement or broker button would turn TickerHall into a smaller StockTwits. The cold-start problem that killed earlier "better StockTwits" attempts also eases if the product starts as a portable receipt rather than a room: callers bring their own audiences, and the room fills behind them.

For you personally, the biggest realistic win is TickerHall becoming the neutral record of who was right that a broker without social, or a ratings company, eventually buys. That is a multi-year equity outcome, not income. PostDose is still the path to millions a year. TickerHall is worth about 230 capped hours, 8 of your 30 a week, to test. It should get more of your time only when Gate 1 and Gate 2 show the evidence.
