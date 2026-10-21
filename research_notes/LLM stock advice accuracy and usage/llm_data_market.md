# Selling finance data directly into end users' LLMs (consumer/prosumer MCP, ChatGPT apps, Claude connectors, Perplexity/Gemini)

Research date: 2026-10-21. Builds on prior notes (StockTwits official MCP at mcp.stocktwits.com with no pricing shown; Stockpulse MCP ~EUR 249–599/mo; self-serve sentiment APIs ~$0–300/mo); those findings are not repeated here. "Fetched 2026-10-21" means the live page was read on that date. Estimates and third-party figures are labeled.

## 1. Distribution: how third parties get into ChatGPT, Claude, Perplexity and Gemini, and whether they can charge users there

### Takeaway
Getting listed is now cheap and fast on both ChatGPT and Claude. Directory review is mostly automated, and Claude now lists about 1,000 connectors. Neither platform lets a data vendor sell a subscription inside the assistant. OpenAI explicitly bans selling digital goods or subscriptions in plugins, and there is no revenue share because there is no in-assistant billing for data. The working model on both platforms is to sell the subscription on your own site, then let the user sign in to the paid account with OAuth inside the assistant. Trade execution is barred from both directories unless a platform grants an exception.

### Cited Findings
**OpenAI / ChatGPT**
- OpenAI launched apps in ChatGPT and the Apps SDK, which is built on MCP, at DevDay on Oct 6, 2025. Launch partners were Booking.com, Canva, Coursera, Figma, Expedia, Spotify and Zillow. Altman cited 800M+ weekly ChatGPT users. — [SiliconANGLE, Oct 6 2025](https://siliconangle.com/2025/10/06/openai-announces-chatgpt-apps-embedded-codex-coding-agent-devday/); [Simon Willison live blog](https://simonwillison.net/2025/Oct/6/openai-devday-live-blog/)
- Third-party app submissions and the App Directory opened Dec 17, 2025. OpenAI reviews every submission before listing it, and approved apps began rolling out in early 2026. Users find apps in the sidebar directory or at chatgpt.com/apps and invoke them with @mention or from the tools menu. At launch, apps could link out to complete purchases "for physical goods only." Digital goods and subscriptions were not allowed, with OpenAI "exploring more options over time." — [VentureBeat, Dec 18 2025](https://venturebeat.com/technology/openai-now-accepting-chatgpt-app-submissions-from-third-party-devs-launches)
- OpenAI renamed the App Directory to the Plugin Directory on Jul 9, 2026. A plugin bundles apps, skills and app templates, and existing app connections were unaffected. — [OpenAI Help Center art. 20001256](https://help-lb.openai.com/en/articles/20001256)
- The current submission guidelines (fetched 2026-10-21) say:
  - "Currently, plugins may conduct commerce only for physical goods."
  - "Selling digital products or services—including subscriptions, digital content, tokens, or credits—is not allowed."
  - "Plugins must not display subscription plans, initiate new subscriptions, or promote upgrades." Plugins also may not "Link directly to a checkout or other transactional page."
  - "Plugins must not apply ChatGPT-specific fees, surcharges, or other pricing that penalizes users."
  - Plugins "must not serve advertisements."

  Users can still sign in to a subscription they already have. — [OpenAI Apps SDK app submission guidelines](https://developers.openai.com/apps-sdk/app-submission-guidelines)
- On financial services, the same guidelines prohibit "Execution of money transfers, crypto transfers, or investment trades" and "Unregulated, deceptive, or abusive financial services." They say nothing about financial advice or informational market data, so read-only data apps are allowed. — [OpenAI app submission guidelines](https://developers.openai.com/apps-sdk/app-submission-guidelines)
- On discovery, plugins with strong performance "may be eligible for enhanced distribution opportunities." Screenshots no longer appear in directory listings, and plugins must not "manipulate how the model selects or uses other plugins." Demo or trial plugins are rejected. — [OpenAI app submission guidelines](https://developers.openai.com/apps-sdk/app-submission-guidelines)
- The monetization docs (fetched 2026-10-21) say the "recommended and generally available approach is to use external checkout." They describe an in-ChatGPT payment sheet as a private beta "limited to select marketplaces." Merchants certified to PCI DSS Level 1 can use the Agentic Commerce Protocol's Delegate Payment endpoint. "Current approval is limited to plugins for physical goods purchases." The docs list no revenue share or fee for apps. — [OpenAI Apps SDK monetization](https://developers.openai.com/apps-sdk/build/monetization)
- OpenAI and Stripe co-developed the Agentic Commerce Protocol and launched it with Instant Checkout ("Buy it in ChatGPT") in Sept 2025 for physical-goods merchants. — [OpenAI](https://openai.com/index/buy-it-in-chatgpt/); [Stripe newsroom](https://stripe.com/newsroom/news/stripe-openai-instant-checkout)
- A retailer guide reports a 4% OpenAI transaction fee for Instant Checkout, citing PYMNTS from Jan 2026. It also reports that OpenAI moved in Mar 2026 toward sending purchases to merchants' own storefronts. Both claims are secondary and unverified against OpenAI. — [Ekamoira guide](https://www.ekamoira.com/blog/chatgpt-instant-checkout-agentic-commerce-protocol-2026)
- **Inside-ChatGPT freemium in practice:** Unusual Whales' ChatGPT app "works on any ChatGPT plan" with a free or paid UW login. Free UW accounts get data delayed by two trading sessions, and "some tools need an upgrade." That fits the rule that plugins may explain plan limits but not sell upgrades in-chat. — [Unusual Whales AI apps page](https://unusualwhales.com/ai-apps)

**Anthropic / Claude**
- On Jul 28, 2026, Anthropic said Claude's connectors directory lists "over 950 MCP servers" and is "used by millions of people every day." — [Claude blog, Jul 28 2026](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)
- The public directory page showed **993 connectors** when fetched on 2026-10-21. — [claude.com/connectors](https://claude.com/connectors)
- A third-party snapshot counted 369 connectors on Jun 19, 2026. It likely used a narrower definition, so it conflicts with Anthropic's figure. — [dirjournal](https://www.dirjournal.com/blogs/claude-connectors-list)
- Anthropic opened a self-serve directory submission portal (claude.ai/directory/manage) on Sep 25, 2026. Anyone on a paid Claude plan can submit. Developers get review tracking and post-launch usage analytics. — [Claude resources article](https://claude.com/resources/articles/build-plugins-for-claude); [Unite.AI](https://www.unite.ai/anthropic-opens-directory-submission-portal-for-claude-plugins/)
- Submission requirements (fetched 2026-10-21):
  - A remote HTTPS server.
  - OAuth 2.0 for authenticated services, or no auth for public data.
  - Every tool annotated with a title and readOnlyHint or destructiveHint.
  - A privacy policy and a test account for reviewers.
  - Seven compliance acknowledgments, including "financial transactions" and "first-party API usage."
  - A data-handling step asking whether the API is the developer's own, proxied with a partner's permission, or a third party's.

  After an automated scan, a submission is "by default" listed as a Community connector. Some get human review, and Verified status is a separate step. — [Claude docs: Submit a connector](https://claude.com/docs/connectors/building/submission)
- The Anthropic Software Directory Policy (updated Apr 15, 2026) bars software that "executes financial transactions on behalf of users" or "transfers money, cryptocurrency, or other financial assets," "Unless otherwise expressly permitted by us in writing." It also bars software that "serves advertisements, sponsored content, paid product placements." It contains no rules on selling subscriptions, paid accounts or financial advice. — [Anthropic Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)
- Claude has no in-chat checkout or payment rail for connectors in any source found. Monetization works through the vendor's own OAuth account. Unusual Whales' Claude app, for example, requires Claude Pro/Max/Team/Enterprise plus a UW login. — [Unusual Whales AI apps](https://unusualwhales.com/ai-apps)
- Anthropic launched interactive connectors (MCP Apps, meaning UI inside Claude) on Jan 26, 2026. — [Claude blog: Interactive connectors and MCP Apps](https://claude.com/blog/interactive-tools-in-claude)

**MCP ecosystem scale**
- On Dec 9, 2025, Anthropic donated MCP to the Linux Foundation's new Agentic AI Foundation, co-founded with Block and OpenAI. It said there were "more than 10,000 active public MCP servers" and listed ChatGPT, Cursor, Gemini, Microsoft Copilot and VS Code as adopters. — [Anthropic, Dec 9 2025](https://anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
- The figure of 97M+ monthly SDK downloads appears only in secondary sources and is unverified against Anthropic. — [FourWeekMBA](https://fourweekmba.com/model-context-protocol-donated-to-linux-foundation-the-tcp-ip-of-agentic-ai/); [Gyld](https://gyld.ai/blog/mcp-adoption-statistics-2026-growth-servers-and-agent-tool-use)
- Third-party counts of the official MCP registry (estimates):
  - 43,298 servers as of Oct 14, 2026, about 64% of them remote, up 36% in 30 days. — [Gravity census](https://gravity.fast/data/mcp-adoption-statistics/)
  - 43,012 active servers in Oct 2026. — [LocalCan](https://www.localcan.com/blog/state-of-mcp-server-development)
  - 30,375 unique servers in Sept 2026. — [DevToolHub](https://devtoolhub.com/mcp-registry-by-the-numbers/)
- **Paid MCP is still tiny:** A vendor-published snapshot from Aug 2026 reported that x402 per-call payments settled $197,149 across 523 services in 30 days, with 86% going to one service. A June 2026 observation found "almost all MCP servers are free." Both are low-authority or vendor sources. — [summarized in search results from usagebox / godberrystudios / WorkOS](https://workos.com/blog/x402-vs-stripe-mpp-how-to-choose-payment-infrastructure-for-ai-agents-and-mcp-tools-in-2026); [Godberry Studios](https://godberrystudios.com/posts/how-to-monetize-mcp-servers-2026/)

**Perplexity / Gemini**
- Perplexity takes in finance data through its own licensing deals and through bring-your-own-license connectors rather than an open paid app store. Examples are Benzinga (announced Dec 11, 2025) and Daloopa BYOL (Apr 30, 2026). — see Q4 for sources.
- Google Finance's AI features (Deep Search, Kalshi/Polymarket data, announced Nov 6, 2025) are first-party Google products. Google AI Pro/Ultra subscribers get higher Deep Search limits. — [Search Engine Journal](https://www.searchenginejournal.com/google-finance-gets-ai-deep-search-prediction-market-data/560157/); [Android Authority](https://www.androidauthority.com/google-finance-deep-search-kalshi-polymarket-support-3613620/)
- No third-party paid data marketplace for Gemini or Perplexity consumers was found. Both platforms are clients for MCP: Gemini CLI, and Perplexity via Robinhood/Public/Morningstar MCP support (see Q2).

### Inferences
- A startup gets distribution almost for free: a Community listing in Claude's directory and, after review, a ChatGPT plugin listing. It gets **no billing, no revenue share and no paid placement**. Every dollar has to come from a subscription sold outside the assistant and checked through OAuth. This is the "bring your own entitlement" model.
- OpenAI's ban on in-chat upsells ("must not display subscription plans... or promote upgrades") makes the free-to-paid funnel *inside* ChatGPT weak. Free tiers in ChatGPT must be good enough, or limits explained plainly enough, that users go to the vendor's site on their own.
- Being discovered in a directory of about 1,000 Claude connectors and a large ChatGPT plugin directory is a real problem. The OpenAI guidelines tie "enhanced distribution" to performance, which favors brands users already ask for by name.
- Both platforms bar trade execution in their directories by default. A data-and-scoring product, such as sentiment or trader track records, sits in the allowed read-only lane. Brokerage-integrated trading agents need a custom connector or a written exception.

### Gaps
- No official count of ChatGPT plugins/apps or install/MAU figures for any directory app was found. OpenAI has not published directory usage stats.
- No official per-connector usage numbers for Claude. Anthropic gives only "millions of people every day" across the directory, and per-connector analytics go privately to developers.
- The Anthropic Software Directory **Terms**, separate from the Policy, were not read. They may contain monetization clauses.
- No documented plan from OpenAI or Anthropic to allow digital-goods or subscription sales in-chat was found as of Oct 2026, beyond OpenAI's Dec 2025 "exploring more options" language.

## 2. Finance-data vendors selling into LLMs: offerings, pricing, traction

### Takeaway
Many retail and prosumer finance-data brands already ship official MCP servers or ChatGPT/Claude apps. Examples include Unusual Whales, TipRanks, Morningstar/PitchBook (for entitled users), Financial Datasets, Fiscal.ai, Quiver, Alpha Vantage, Massive/Polygon, SentiSense, Robinhood, Public and Alpaca. Almost all of them charge through their existing API or subscription plans and give the AI connector away as a perk or a metered feature. None disclosed user counts or revenue from the AI channel.

### Cited Findings
**Unusual Whales (options flow, dark pool, congress trades)**
- **Apps and access:**
  - Official apps exist for ChatGPT, Claude and Grok. Users sign in with a UW account and need no API key.
  - The ChatGPT version has interactive widgets (flow tape, GEX heatmap, screener). Claude and Grok return text and tables. All tools are read-only.
  - Free UW accounts get data delayed by two trading sessions.

  — [UW AI apps page, fetched 2026-10-21](https://unusualwhales.com/ai-apps)
- **Hosted MCP server and pricing:**
  - The hosted MCP server at api.unusualwhales.com/api/mcp has "100+ tools," and "API access, including MCP, is part of the API plans." — [UW AI agents page](https://unusualwhales.com/ai-agents)
  - API plans (fetched 2026-10-21): Options Starter $99/mo (25,000 requests/mo), Basic $150/mo ("Most Popular," unlimited daily requests), Advanced $375/mo. All three list "MCP Support" and "Custom Skills for your agents." — [UW public API](https://unusualwhales.com/public-api)
  - Structured data on the same page showed $125/$350, which conflicts with the plan prices above. — [search summary of UW public API](https://unusualwhales.com/public-api)
- **Consumer plan:** Basic is $50/mo, about $42/mo billed annually. — [UW pricing](https://unusualwhales.com/pricing)
- **Traction:** No user, subscriber or AI-channel figures are disclosed. A third-party review claims "tens of thousands of subscribers" without sourcing. — [Bullish Bears review](https://bullishbears.com/unusual-whales-review/)

**TipRanks (analyst ratings, Smart Score, insider/hedge-fund/politician signals, sentiment)**
- **Listing and auth:** TipRanks is listed in ChatGPT's plugin directory under TipRanks Ltd and connects over OAuth. It also supports Claude.ai, Claude Desktop, Claude Code, Cursor, VS Code, Codex and Gemini CLI. — [mcp.tipranks.com, updated 2026-05-19](https://mcp.tipranks.com/); [ChatGPT plugin listing](https://chatgpt.com/plugins/plugin_asdk_app_6a216a0ba8488191998cb0adb5fc79e5)
- **Metered quota by subscription:**
  - OAuth connector calls per month are tiered by TipRanks plan: Free/Basic 10, Premium 100, Ultimate 200.
  - Separate paid MCP API-key plans allow 1,000, 2,500 or 6,000 calls/mo. Dollar prices are not shown publicly.
  - Portfolio data requires the OAuth `tipranks:portfolio` scope.

  — [mcp.tipranks.com](https://mcp.tipranks.com/)
- **Traction:** TipRanks claims "10M+ monthly users" on tipranks.com and "100+ banks, brokers, and exchanges" for the company overall. It gives no connector-specific numbers. — [mcp.tipranks.com](https://mcp.tipranks.com/)
- **Launch:** An announcement post exists: "Bring TipRanks into Every Investment Conversation – Introducing MCP." — [TipRanks Labs](https://www.tipranks.com/news/labs/bring-tipranks-into-every-investment-conversation-introducing-mcp)

**SentiSense (multi-source stock sentiment; closest analog to the user's thesis)**
- **Connector:** One URL (app.sentisense.ai/mcp) provides 11 read-only tools with OAuth sign-in. It works with Claude (directory listing or custom connector), ChatGPT, Grok, Codex and Claude Code.
- **Data:** Sentiment, analyst ratings, insider and 13F filings, options positioning, news and a "Market Mood" score. The page does not mention track records or backtested accuracy.
- **Pricing:** The free tier gives preview data and 1,000 calls/mo. PRO is **$6.75/mo**, a promo price shown as 55% off for life with code FALL26, with unlimited calls.
- **Traction:** No user counts are given.

— [SentiSense connect page, fetched 2026-10-21](https://sentisense.ai/connect)

**Financial Datasets (developer/agent-first fundamentals and prices)**
- Hosted MCP at mcp.financialdatasets.ai works with Claude, Cursor and other clients.
- Pricing: Credits $20 one-time for 1,000 requests; Personal $200/mo for 100k requests; Professional $2,000/mo for 2M requests with a redistribution license; Enterprise custom. Overages run $10 or $5 per 1,000 requests.
- No traction claims.

— [Financial Datasets pricing, fetched 2026-10-21](https://www.financialdatasets.ai/pricing)

**Fiscal.ai (formerly FinChat)**
- **Pricing:** Terminal plans are Pro at $39/mo billed yearly ($49 monthly) and Max at $79/mo billed yearly. MCP is sold separately. One review cites $780/yr and another cites a $199/mo Enterprise tier; these conflict. — [Ryan O'Connell review](https://ryanoconnellfinance.com/fiscal-ai-review/); [Stock Simplifier review](https://stocksimplifier.com/reviews/fiscal-ai)
- **Funding and users:** Fiscal.ai raised a $10M Series A in June 2025 led by Portage, with Social Leverage and VanEck participating, and was described as serving "over 350,000 registered users." It received a C$1.5M FedDev Ontario grant on Jun 26, 2026. — [Lawson Lundell / LW law announcement](https://www.lwlaw.com/fiscal-ai-a-canadian-based-ai-driven-financial-data-platform-raised-a-usd-10-million-series-a-funding-round-led-by-portage-with-continued-participation-from-social-leverage-among-others/); [TinySeed](https://tinyseed.com/latest/fiscal-ai-10m-future-ai-finance)

**Quiver Quantitative (congress trades, alt-data)**
- Hobbyist is $30/mo monthly or $25/mo annually and includes 10 of 18 Quiver MCP tools. Trader is $75/mo. — [Quiver API pricing](https://api.quiverquant.com/pricing/)
- The search tool labeled this page as old, but it lists MCP tools, which suggests it is current. The date is unverified.

**Alpha Vantage**
- The free key allows 25 requests/day. Paid tiers start at $49.99/mo per one source or $99.99/mo for real-time US data per another; these conflict. — [MarketXLS comparison](https://marketxls.com/blog/best-financial-data-mcp-servers-ai-market-data); [Shibui Finance guide](https://shibui.finance/guide-best-mcp-server-stock-data)

**Massive (formerly Polygon.io)**
- The official MCP server (GitHub massive-com/mcp_massive) is labeled experimental and requires a Massive API key, so access follows the API plan. — [Glama listing](https://glama.ai/mcp/servers/polygon-io/mcp_massive)
- No MCP-specific pricing was found.

**Financial Modeling Prep**
- Only community-maintained FMP MCP servers were found, for example imbenrabi's on npm/Glama. They require the user's own FMP key. — [Glama](https://glama.ai/mcp/servers/@imbenrabi/Financial-Modeling-Prep-MCP-Server/tree/0b8da2879b20ebd7410fca3c14baf0d5febbdbe7); [jsDelivr README](https://cdn.jsdelivr.net/npm/financial-modeling-prep-mcp-server@2.6.12/README.md)
- The FMP docs page returned 403, so an official server could not be confirmed.
- FMP is reported, via secondary 2024 sources, as a data source for Perplexity Finance. — [wwwhatsnew, Oct 2024](https://wwwhatsnew.com/2024/10/22/perplexity-finance-el-nuevo-aliado-de-la-ia-para-investigar-el-mercado-de-valores/)

**Koyfin**
- One comparison says Koyfin has no public API or MCP server. Plans: Plus $39/mo, Premium $79/mo. — [claudecodehq comparison](https://www.claudecodehq.com/blog/koyfin-vs-fiscal-ai)

**Morningstar / PitchBook**
- Apps in ChatGPT were announced Dec 17, 2025, for "entitled or licensed" Morningstar and PitchBook users. They build on earlier integrations with Claude, Perplexity Finance, Microsoft Foundry and Copilot Studio. — [Morningstar newsroom](https://newsroom.morningstar.com/news/news-details/2025/Morningstar-and-PitchBook-Bring-Trusted-Investing-Intelligence-to-Apps-in-ChatGPT/default.aspx); [BusinessWire](https://www.businesswire.com/news/home/20251216478652/en/morningstar-and-pitchbook-bring-trusted-investing-intelligence-to-apps-in-chatgpt)
- No consumer price or usage numbers were found.

**Institutional connectors**
- Claude for Financial Services launched Jul 2025 with connectors including FactSet, S&P Capital IQ, Daloopa, Morningstar and PitchBook. Later additions were LSEG, Moody's, MT Newswires, Aiera, Chronograph and Egnyte. Using them requires a Claude for Financial Services subscription plus the user's own data licenses. — [Anthropic: Claude for Financial Services](https://anthropic.com/news/claude-for-financial-services); [Anthropic: Advancing Claude for FS](https://anthropic.com/news/advancing-claude-for-financial-services); [Claude support](https://support.claude.com/en/articles/11771619-get-started-with-claude-for-financial-services)
- **Daloopa:** Its Perplexity integration on Apr 30, 2026 is BYOL. It is also a bundled dataset in ChatGPT for Financial Services (Sep 2026). — [Tullahoma News / press release](https://www.tullahomanews.com/?p=103680); [VentureBeat](https://venturebeat.com/data/openai-launches-chatgpt-for-financial-services-with-integrated-data-sources-it-pulls-research-cites-it-and-builds-decks-in-minutes)

**Brokerage MCPs**
- **Robinhood:**
  - Agentic trading MCP in beta. Supported clients: Claude Code and Desktop, ChatGPT, Codex, Cursor and Grok, plus Perplexity, Replit, AWS Quick and others.
  - The agent can read all accounts but trades only in a dedicated "Agentic" MCP account. Users can require approval before trades.
  - Robinhood warns that agents "can make errors."

  — [Robinhood support: agentic trading overview](https://robinhood.com/us/en/support/articles/agentic-trading-overview/)
  - The beta launch date of May 27, 2026 and the "27M customers" figure come from secondary sources. — [Bitsminds](https://www.bitsminds.com/news/robinhood-agentic-trading-claude-chatgpt-mcp-2026); [Vorp Labs](https://vorplabs.com/agent-tools/robinhood-cli)
  - A critical hands-on review was published Jul 2026. — [NexusTrade](https://nexustrade.io/blog/robinhood-agentic-trading-mcp-review-20260708)
- **Public.com:** The MCP server supports Claude, ChatGPT, Perplexity, Grok, Muse and Codex. It covers US stocks, ETFs, options, crypto and bonds. It is included with a Public account at no extra cost, though standard trading fees apply, and Public offers dedicated MCP accounts. — [Public MCP page, fetched 2026-10-21](https://public.com/mcp-trading)
- **Alpaca:** The official open-source MCP server works with Claude, ChatGPT, VS Code, Cursor and Gemini CLI, and a free paper-trading account is enough to start. — [Alpaca docs](https://docs.alpaca.markets/us/docs/alpaca-mcp-server)
- Because of the OpenAI and Anthropic directory rules in Q1, trade-executing brokerage MCPs mostly run as custom connectors or in developer mode rather than as directory listings.

**Others observed**
- Claude's directory front page showed "TEXT TO QUANT," a Verified and Trending connector for plain-English strategy backtests. It also showed Etherscan. — [claude.com/connectors, fetched 2026-10-21](https://claude.com/connectors)
- A Stocktwits page advertises a ChatGPT connector for sentiment, trending, watcher and news data. No pricing is shown. — [Stocktwits page](https://stocktwits.com/coins/claude)
- Improvado resells Stocktwits data for querying via MCP. — [Improvado](https://improvado.io/integrations/stocktwits)
- Trendlyne (India) publishes a Claude MCP setup guide. — [Trendlyne help](https://help.trendlyne.com/support/solutions/articles/84000399335-trendlyne-mcp-setup-guide-claude)

**Yahoo Finance, Seeking Alpha, Benzinga Pro**
- No official Yahoo Finance or Seeking Alpha app in ChatGPT or Claude was found, only third-party sync connectors such as Windsor.ai. — [Windsor.ai](https://windsor.ai/connect/yahoo-finance-to-chatgpt-integration/)
- Benzinga's route into LLMs is a platform licensing deal with Perplexity (Q4), not a consumer app.

### Inferences
- The dominant pricing pattern is **"the connector is a channel for the existing subscription."** Examples:
  - UW: free account gets delayed data; consumer plan is $50/mo; API/MCP is $99–375/mo.
  - TipRanks: connector calls metered by Premium/Ultimate tier.
  - Morningstar: entitled users only.
  - Public: included with the account.

  Pure "pay for my LLM data feed" pricing exists mainly for developers: Financial Datasets credits, the Stockpulse and UW API tiers. SentiSense is the one consumer sentiment connector found, priced as low as $6.75/mo on promo.
- Market pricing for a retail sentiment connector sits at roughly **$0–$50/mo**, set by SentiSense ($0 / $6.75 promo), TipRanks (bundled with Premium/Ultimate) and UW Basic ($50). That is well below Stockpulse's EUR 249–599 and the $99–375 developer/API tiers. This is an inference from listed prices.
- Scored trader track records were **not** found as a productized LLM data feed from any vendor. TipRanks scores analysts and insiders, which is the closest analog, but not social traders. This is a possible white space, but see the Q4 caveats.
- Vendors are racing to be the brand a user names when calling a tool ("@Unusual Whales"), because the directory rules give them no other way to make money in-chat.

### Gaps
- None of these vendors disclosed AI-channel users, installs, MAU or revenue. The only scale claims are company-wide: TipRanks 10M+ monthly users and Fiscal.ai 350K registered users (2025).
- TipRanks MCP dollar prices are behind the developer portal, and Fiscal.ai's MCP price conflicts across reviews.
- Official FMP MCP status could not be confirmed (403). Massive/Polygon MCP pricing was not found.
- Unusual Whales' subscriber count and revenue were not found; there is no Sacra profile in search results.
- The date and pricing of the Stocktwits ChatGPT connector are unknown.

## 3. Willingness to pay: do retail/prosumer traders pay for data add-ons, and for data inside an AI assistant?

### Takeaway
Retail traders demonstrably pay for data and research subscriptions in the $25–$80/mo band: Unusual Whales, TipRanks, Seeking Alpha, Fiscal.ai, Koyfin, Quiver and TradingView. Hard, audited subscriber numbers are scarce because these companies are private. No vendor or platform has published evidence that consumers pay *specifically* for data delivered inside an AI assistant. The money observed so far comes from existing subscribers who get AI access as a bundled perk. Per-call paid MCP revenue across the whole ecosystem is negligible.

### Cited Findings
**AI usage for finance**
- In May 2026, OpenAI said "more than 200 million users already ask financial questions to ChatGPT every month." — [TechCrunch, May 15 2026](https://techcrunch.com/2026/05/15/openai-launches-chatgpt-for-personal-finance-will-let-you-connect-bank-accounts/)
- An Investing.com survey of 938 US investors (Apr 2026) found:
  - 62% have used AI tools to help with investment decisions.
  - 24% use them regularly.
  - 53.5% trust AI analysis only after verifying it elsewhere.
  - 17% do not plan to use AI for investing.

  The survey was run by a company that sells investing products. — [Traders Magazine](https://www.tradersmagazine.com/xtra/nearly-two-thirds-of-retail-investors-use-ai-to-inform-investment-decisions/); [InvestorIdeas release](https://www.investorideas.com/news/2026/technology/04061-ai-retail-investing-survey.asp)
- An eToro survey of 1,000 US retail investors found 55% use or are open to AI picking or altering their investments. The figure rises to 77% for Gen Z and 79% for Millennials. — [eToro press release](https://www.etoro.com/en-us/news-and-analysis/latest-news/press-release/gen-z-embraces-ai-as-investing-tool-even-as-ai-stock-enthusiasm-cools/)
- A secondary commentary says 54% of investors use AI chatbots like ChatGPT for research "not a $49-a-month stock-scoring subscription." This substitution threat is unverified. — [Investing.com analysis](https://www.investing.com/analysis/hedge-fund-at-home-how-ai-is-rewiring-retail-trading-and-testing-its-limits-200685595)

**Paid retail data and research subscriptions (mostly estimates)**
- **Unusual Whales:** Consumer Basic is $50/mo, about $504/yr. — [UW pricing](https://unusualwhales.com/pricing)
- **TradingView** (private, no official 2025–26 figures):
  - Estimates of paid subscribers range from 1.5M+ to 6.5M, and 2025 revenue estimates range from ~$300M to $420M. The sources conflict and come from template and SEO sites. — [canvasbusinessmodel](https://canvasbusinessmodel.com/products/tradingview-marketing-mix); [productmint](https://productmint.com/?p=3318)
  - The last widely reported hard figure is 1M+ paying subscribers in Dec 2021. — [productmint](https://productmint.com/?p=3318)
- **Seeking Alpha:** "250,000+ Premium members," unsourced and dated Aug 2026. Premium costs $239–299/yr and Pro $2,400/yr. — [Financer review](https://financer.com/invest/seeking-alpha-premium-review/)
- **Fiscal.ai:** 350K+ registered users (paid share unknown, June 2025) and $39–79/mo plans. — see Q2 sources.
- **TipRanks:** Paid plan about $29.95/mo per a comparison site. — [findmymoat](https://www.findmymoat.com/vs/seeking-alpha-vs-tipranks)
- **Koyfin:** $39–79/mo. — [claudecodehq](https://www.claudecodehq.com/blog/koyfin-vs-fiscal-ai)
- **Quiver:** $25–75/mo. — [Quiver pricing](https://api.quiverquant.com/pricing/)

**Evidence specific to paying inside an AI assistant**
- TipRanks gates connector volume by paid tier: free gets 10 calls/mo, Premium 100, Ultimate 200. This is the clearest live experiment in using the LLM channel as an upsell lever. — [mcp.tipranks.com](https://mcp.tipranks.com/)
- UW gives free accounts two-session-delayed data in ChatGPT and live data to paid accounts. — [UW AI apps](https://unusualwhales.com/ai-apps)
- SentiSense is cutting its PRO connector price to $6.75/mo with a "55% off for life" promo, which suggests price sensitivity or a land-grab. — [SentiSense](https://sentisense.ai/connect)
- **Ecosystem-wide per-call payments are tiny.** x402 settled about $197K across 523 services in 30 days (Aug 2026, vendor source, 86% to one service). One guide observes that "almost all MCP servers are free." — [Godberry Studios](https://godberrystudios.com/posts/how-to-monetize-mcp-servers-2026/); [WorkOS](https://workos.com/blog/x402-vs-stripe-mpp-how-to-choose-payment-infrastructure-for-ai-agents-and-mcp-tools-in-2026)
- ChatGPT's own personal-finance feature, which connects bank and brokerage accounts via Plaid across 12,000+ institutions, launched first for **Pro** subscribers in the US. That shows OpenAI is willing to put finance features behind its own highest consumer tier. — [TechCrunch](https://techcrunch.com/2026/05/15/openai-launches-chatgpt-for-personal-finance-will-let-you-connect-bank-accounts/)

### Inferences
- Willingness to pay for *trader data* is proven; willingness to pay for *the AI delivery channel itself* is not. The realistic consumer motion today is that a trader already pays, or upgrades, on the vendor's website, and the LLM connector raises retention and perceived value. A standalone "data for your LLM" SKU sold to consumers is still unproven.
- The audience is large: 200M+ monthly finance askers in ChatGPT alone. But users mostly treat AI output as something to verify, with 53.5% verifying elsewhere. That may favor *sourced, scored* data such as track records with citations over raw sentiment. This is an inference.
- Usage-metered connector quotas, like TipRanks', suggest vendors worry about the cost of LLM-driven API calls. An agent can make dozens of calls per question. That pushes consumer pricing toward call caps rather than all-you-can-eat plans.

### Gaps
- No published conversion rate, ARPU or churn data for any finance AI connector.
- No audited subscriber numbers for Unusual Whales, TradingView, Seeking Alpha or Benzinga Pro. All figures found are third-party estimates or unsourced.
- No survey was found that measures willingness to pay *for data inside an AI assistant*, as opposed to AI tool use generally.
- Benzinga Pro subscriber counts were not found.

## 4. Who wins this slot: are LLM platforms licensing data themselves and squeezing third parties? Platform policies on financial apps

### Takeaway
The platforms are moving into finance data directly, but so far with **institutional or bundled licensed data and first-party features**, not by blocking third parties:
- OpenAI launched ChatGPT for Financial Services (Sep 10, 2026) with OpenAI-hosted Daloopa, PitchBook and LSEG News data, and a Pro-tier personal-finance product (May 2026).
- Google built Gemini-powered Google Finance with Kalshi/Polymarket data.
- Perplexity licenses Benzinga and others.
- Anthropic relies on partner connectors for institutions.

Commodity data (quotes, fundamentals, news, analyst ratings) is being absorbed into the platforms for free. Third parties keep the space for proprietary or derived data and brand-name pull. Platform policies restrict trade execution and in-chat selling, not financial information or advice.

### Cited Findings
**OpenAI**
- ChatGPT for Financial Services launched Sep 10, 2026 for eligible institutions, with investment banking and equity research as the first focus and Morgan Stanley and Evercore as design partners.
  - **Bundled datasets** (Daloopa, PitchBook, LSEG News) are "indexed and hosted on OpenAI's infrastructure," so customers need no separate data contracts.
  - **Entitlement integrations** under development (S&P Capital IQ, LSEG, MSCI, Factiva, Moody's) recognize the user's existing licenses.
  - There are MCP connections to S&P Global and FactSet and 50+ other integrations.
  - Pricing was not disclosed, and the product is not for retail.

  — [VentureBeat](https://venturebeat.com/data/openai-launches-chatgpt-for-financial-services-with-integrated-data-sources-it-pulls-research-cites-it-and-builds-decks-in-minutes); [The Next Web](https://thenextweb.com/news/openai-chatgpt-financial-services-dora-data-residency); [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/openai-launches-chatgpt-financial-services-204024031.html)
- ChatGPT personal finance launched May 15, 2026 as a preview for US Pro users. It connects 12,000+ institutions via Plaid, including Schwab, Fidelity and Robinhood brokerages, and shows a portfolio-performance dashboard. Intuit support is planned. — [TechCrunch](https://techcrunch.com/2026/05/15/openai-launches-chatgpt-for-personal-finance-will-let-you-connect-bank-accounts/)
- OpenAI policy bars plugins that execute investment trades or money transfers, sell digital goods or subscriptions in-chat, or serve ads. It does not restrict financial information or advice content. — [OpenAI app submission guidelines](https://developers.openai.com/apps-sdk/app-submission-guidelines)

**Google**
- Google Finance AI was announced Nov 6, 2025. It added Gemini Deep Search with cited multi-step reports (higher limits for AI Pro/Ultra), Kalshi and Polymarket prediction-market data, and live earnings features, and expanded to India. — [Search Engine Journal](https://www.searchenginejournal.com/google-finance-gets-ai-deep-search-prediction-market-data/560157/); [Android Authority](https://www.androidauthority.com/google-finance-deep-search-kalshi-polymarket-support-3613620/); [CoinTelegraph](https://cointelegraph.com/news/google-finance-prediction-markets-kalshi-polymarket-ai)
- A report says the redesigned AI Google Finance rolled out to 100+ countries from Apr 8, 2026. A lower-quality blog reported it officially out of beta with an Android app in Jul 2026. — [SBBIT (Japanese), Apr 2026](https://www.sbbit.jp/article/fj/184257); [ai2.work](https://ai2.work/blog/google-finance-launches-ai-research-tools-for-retail-investors)
- Reviews say Google Finance AI is free for basic use and does not trade or give personalized advice. — [macmyths](https://macmyths.com/google-finance-adds-gemini-powered-research-tools-but-it-still-doesnt-place-trades/)

**Perplexity**
- Benzinga partnership announced Dec 11, 2025, covering news, analyst ratings, earnings, insider transactions and price movements. — [StreetInsider press release](https://www.streetinsider.com/Press+Releases/Benzinga+and+Perplexity+Announce+Strategic+Partnership+to+Power+AI-Driven+Financial+Research/25726565.html); [DBusiness](https://www.dbusiness.com/daily-news/benzinga-in-detroit-adds-partnership-to-advance-ai-driven-financial-research/)
- Daloopa BYOL integration on Apr 30, 2026. — [press release via Tullahoma News](https://www.tullahomanews.com/?p=103680)
- Crunchbase and FactSet were 2025 partners, initially for Enterprise Pro.
- Perplexity Computer reportedly connects to 20+ licensed data sources (Dun & Bradstreet, Guidepoint, IBISWorld) for users who already subscribe. Perplexity is "not reselling these datasets" (Aug 2026, single source). — [GadgetBond](https://gadgetbond.com/perplexity-computer-finance-data-sources-update-aug-2026/)
- Secondary sources list FMP (prices and fundamentals), Unusual Whales (options), Quartr (transcripts) and EDGAR as Perplexity Finance inputs. None of this is confirmed by Perplexity. — [wwwhatsnew 2024](https://wwwhatsnew.com/2024/10/22/perplexity-finance-el-nuevo-aliado-de-la-ia-para-investigar-el-mercado-de-valores/); [Encyclopedia Autonomica Substack](https://jdsemrau.substack.com/p/how-to-use-perplexity-for-finance)
- UW's API page names Perplexity AI and Public.com as platforms it "Empower[s]," consistent with UW selling B2B to platforms. — [UW public API](https://unusualwhales.com/public-api)

**Anthropic**
- Anthropic uses a partner-connector model, Claude for Financial Services, for institutions with their own licenses. No consumer data bundle was found. — [Anthropic](https://anthropic.com/news/advancing-claude-for-financial-services)
- The directory policy bars executing financial transactions and serving sponsored content unless Anthropic permits it in writing. — [Anthropic Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)

### Inferences
- There are three ways a finance-data company gets into a trader's LLM:
  - **(a) B2B license to the platform:** Benzinga→Perplexity; Daloopa/PitchBook/LSEG→OpenAI; Kalshi/Polymarket→Google; reportedly UW and FMP→Perplexity. This is the biggest-revenue, least-brand route, and the platforms seem to prefer it for commodity data.
  - **(b) BYO-entitlement connector:** Morningstar, TipRanks, UW, Daloopa BYOL. The vendor keeps the customer and the platform takes no cut.
  - **(c) Developer/API MCP:** Financial Datasets, Massive, Alpha Vantage, the UW API, Stockpulse.

  A consumer sentiment or track-record startup would probably need (b) for brand-building and (a) for revenue scale.
- The squeeze risk is real for **commodity** data such as prices, fundamentals, headlines and consensus ratings. ChatGPT, Google Finance and Perplexity already show these for free or bundled. It is weaker for **proprietary, derived signals**: StockTwits-style crowd sentiment, scored trader track records, options flow. Those signals are exactly what the platforms are *licensing in*, which validates their value but pushes the economics toward B2B deals.
- A platform that licenses a dataset (Benzinga in Perplexity) reduces the need for a user to install a separate connector for that data. First-to-license deals may matter more than consumer connector listings for capturing the "data in the trader's LLM" slot at scale.
- Neither OpenAI nor Anthropic restricts informational, read-only investment-data apps. Regulatory or advice risk falls on the vendor, as shown by Robinhood's and Public's own risk disclaimers, not on platform rules.

### Gaps
- No terms (price, exclusivity, revenue share) were disclosed for any platform–data vendor license: Benzinga–Perplexity, Daloopa–OpenAI, Kalshi/Polymarket–Google.
- Where ChatGPT's consumer stock charts and quotes come from could not be confirmed.
- No evidence was found of a platform removing or demoting a third-party finance app in favor of first-party data. The squeeze is inferred, not observed.
- The Google Blog primary post and an official Google Finance AI pricing page were not retrieved; tier limits come from secondary coverage.

## 5. Synthesis: does the "marketing data to a person's LLM" gap exist, and how is it monetized?

### Takeaway
The *distribution* gap is closing fast. Getting into Claude and ChatGPT is now self-serve and nearly free, and many finance-data brands are already there. The *monetization* gap is real and structural. Neither ChatGPT nor Claude lets vendors sell subscriptions in-chat, there is no revenue share, and no vendor has disclosed meaningful AI-channel revenue. A new entrant would compete on the uniqueness of the dataset (track records, sentiment) and on brand pull. The revenue would come from subscriptions sold off-platform, consumer prices would land around $0–$50/mo, and B2B licensing to the platforms would likely be the bigger revenue pool.

### Cited Findings
- **Distribution:** Claude shows 993 connectors (fetched 2026-10-21) with self-serve submission since Sep 25, 2026; ChatGPT's directory has accepted reviewed submissions since Dec 17, 2025. — [claude.com/connectors](https://claude.com/connectors); [Claude docs](https://claude.com/docs/connectors/building/submission); [VentureBeat](https://venturebeat.com/technology/openai-now-accepting-chatgpt-app-submissions-from-third-party-devs-launches)
- **Monetization constraint:** OpenAI bars in-chat digital-goods and subscription sales and upgrade prompts. — [OpenAI guidelines](https://developers.openai.com/apps-sdk/app-submission-guidelines)
- **Existing consumer-facing finance connectors:**
  - Unusual Whales: ChatGPT, Claude and Grok apps, freemium. — [UW](https://unusualwhales.com/ai-apps)
  - TipRanks: ChatGPT plugin and Claude, quota tied to tier. — [TipRanks MCP](https://mcp.tipranks.com/)
  - SentiSense: sentiment, $0 or $6.75/mo promo. — [SentiSense](https://sentisense.ai/connect)
  - Stocktwits: ChatGPT connector. — [Stocktwits](https://stocktwits.com/coins/claude)
  - Morningstar: entitled users only. — [Morningstar](https://newsroom.morningstar.com/news/news-details/2025/Morningstar-and-PitchBook-Bring-Trusted-Investing-Intelligence-to-Apps-in-ChatGPT/default.aspx)
- **Platforms licensing data:** OpenAI (Daloopa, PitchBook, LSEG News), Perplexity (Benzinga), Google (Kalshi, Polymarket). — see Q4 sources.

### Inferences
- The user's thesis is directionally right that traders want data inside their assistant. Large volumes of finance questions and fast connector proliferation support it. But "selling data to a person's LLM" as a *consumer* business is not yet proven anywhere. The defensible angle is proprietary scored data, such as trader track records, which no vendor sells as an LLM feed in what was found. It should be paired with a B2B licensing path to the platforms and brokers. Precedents for that path are UW→Perplexity/Public and Stocktwits→Alpaca. — [Howard Lindzon on Stocktwits/Alpaca](https://www.howardlindzon.com/p/stocktwits-everywhere-as-the-web-disappears-bloomberg-terminals-for-everyone-and-the-trump-stock-mar)
- Likely consumer pricing benchmark: free tier with delayed or limited calls, $5–$50/mo paid tier, metered call quotas. Developer/agent API at $99–$375/mo. Institutional or platform licenses priced by negotiation. This is an inference from the listed prices above.

### Gaps
- No public AI-channel traction data (installs, MAU, revenue) for any finance connector, so market size for this channel cannot be estimated from disclosed figures.
- It is unknown whether OpenAI or Anthropic will open in-chat subscriptions or revenue share in 2027. That would change the economics materially.
