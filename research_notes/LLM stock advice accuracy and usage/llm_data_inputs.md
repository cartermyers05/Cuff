# LLM Data Inputs for Stock Answers: What LLMs Use Today vs. What Better Data Adds (as of Oct 21, 2026)

Labels used below:
- **[VENDOR]** means a claim from the company selling the product.
- **[INDEPENDENT]** means an academic paper, an independent benchmark or journalism.
- **[SECONDARY]** means a third-party blog or aggregator that I could not check against the primary source.

All dates are publication or measurement dates.

---

## Q1. Default inputs: training cutoffs, answers without search (stale data), and the sources cited when search is on

### Takeaway
Without retrieval, a frontier model answers stock questions from training data that was 4 to 21 months old as of Oct 2026, so any price, valuation or news it gives is stale by construction. With search on, finance answers mostly cite three kinds of source:
- consumer personal-finance publishers: NerdWallet, Investopedia, Bankrate, CNBC, Yahoo
- unscored crowd content: Reddit, YouTube
- general authority sites: Wikipedia, Forbes

They rarely draw on structured market data, professional research (Morningstar ranks #84; Seeking Alpha and Bloomberg are outside the top 100 in AI Overviews), or any trader-level data. I found no citation study that isolates stock-ticker or "should I buy X" prompts.

### Cited Findings

**Training cutoffs** [SECONDARY]. These come from third-party compilations, not vendor model cards, and the sources disagree on some model-to-date pairings.
- **OpenAI:** GPT-5.5 has a Dec 1, 2025 cutoff and was released in Apr 2026 — [FixAEO](https://fixaeo.com/ai-knowledge-cutoff/); [Metehan.ai](https://metehan.ai/articles/llm-knowledge-cutoff-dates/)
- **OpenAI:** GPT-5.6 has a Feb 16, 2026 cutoff and GPT-6 has an Apr 30, 2026 cutoff — [RankScope](https://rankscope.ai/blog/chatgpt-knowledge-cutoff)
- **Anthropic:** the newest models (Opus 5.5 / Sonnet 5.5) are listed at June 2026, Opus 5 at May 2026, and Opus 4.7/4.8 at Jan 2026 — [Metehan.ai](https://metehan.ai/articles/llm-knowledge-cutoff-dates/); [Temso](https://www.temso.ai/blog/ai-knowledge-cutoff-dates-every-major-llm-updated-for-2026)
- **Google:** Gemini 3.1 Pro is listed at Jan 2025. Gemini 3.8 Flash is "reported" at Mar 2026, and Google notes that knowledge in some domains is still limited to Jan 2025 — [Temso](https://www.temso.ai/blog/ai-knowledge-cutoff-dates-every-major-llm-updated-for-2026); [Allmo](https://allmo.ai/articles/list-of-large-language-model-cut-off-dates)
- **xAI:** Grok 4.7 is listed at May 2026, Grok 4.6 at Feb 1, 2026, and Grok 4 at Nov 2024 — [FixAEO](https://fixaeo.com/ai-knowledge-cutoff/)

**What happens without fresh data**
- **Alpha Arena (nof1), a live trading contest [INDEPENDENT, reported via SECONDARY press].** Models received only numeric price data. nof1's Jay Zhang said "LLMs do not handle numerical time series data well, but that was the entire context we provided them." — [Forklog](https://forklog.com/en/four-out-of-six-ai-models-suffer-losses-in-trading-tournament/amp); [AIbase](https://www.aibase.com/news/23442)
- **Lopez-Lira & Tang avoid look-ahead [INDEPENDENT].** The researchers measure real predictive skill only on headlines dated after each model's knowledge cutoff, which shows that anything inside the training window is contaminated. — [arXiv 2304.07619 v6, Oct 2025](https://arxiv.org/html/2304.07619v6)
- **Same prompt, different answer [INDEPENDENT, journalism].** In Apr 2023, The Register re-ran the paper's prompt in free ChatGPT and got a different answer than the paper reported, an early sign that answers are inconsistent. — [The Register](https://www.theregister.com/2023/04/18/large_language_models_like_chatgpt/)

**When search is on: how ChatGPT search was built**
- ChatGPT search launched on Oct 31, 2024. OpenAI says it "partnered with news and data providers" to cover weather, stocks, sports, news and maps, and stock queries return a chart. Named publishing partners include AP, Axel Springer, Condé Nast, Dotdash Meredith, Financial Times, Hearst, News Corp, Reuters and others. OpenAI did not name the vendor behind the stock-price data. [VENDOR] — [OpenAI](https://openai.com/index/introducing-chatgpt-search/); [BetaNews](https://betanews.com/2024/10/31/chatgpt-launches-upgraded-search-feature-with-links-to-web-sources)

**When search is on: all-topic citation studies** [INDEPENDENT / SEO vendor]
- **Profound** (published Jun 2025, updated Aug 2025): 680M citations collected Aug 2024 to Jun 2025, measured as share of all citations.

  | Platform | Top cited domains | NerdWallet |
  |---|---|---|
  | ChatGPT | Wikipedia 7.8%, Reddit 1.8%, Forbes 1.1%; Reuters 0.6% (#10) | 0.8% (#6) |
  | Google AI Overviews | Reddit 2.2%, YouTube 1.9%, Quora 1.5% | 0.6% (#6) |
  | Perplexity | Reddit 6.6%, YouTube 2.0% | 0.6% (#7) |

  Yahoo Finance and Investopedia are absent from every all-topic top 10. — [Profound](https://www.tryprofound.com/blog/ai-platform-citation-patterns)
- **Peec AI** (30M sources, reported by Search Engine Land): Reddit is the most-cited domain across ChatGPT, Google AI Mode, Gemini, Perplexity and AI Overviews. — [Search Engine Land](https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138)

**When search is on: finance-specific citation studies** [SEO vendor / PR studies]
- **Goodie AI** (Aug 13, 2025; Feb to Jun 2025 data):
  - Sample: 109,000+ finance citations isolated from 5.7M.
  - Prompts: banking, payments, checkout and money transfer.
  - Models: GPT-4o, Gemini 1.5, Claude 3.7 Sonnet and Perplexity Pro.
  - Results: NerdWallet is the "universal constant" leader across models. Bankrate, PCMag, CNBC, Forbes, Business Insider, Bloomberg, Reddit, Wikipedia and Investopedia are also named.
  - Platform tendencies: ChatGPT favors traditional publishers and structured explainers, Gemini leans toward affiliate and review content, and Perplexity "leans harder into UGC and affiliate content than any other model."

  — [Goodie](https://higoodie.com/blog/most-cited-finance-domains-ai-search/)
- **LLM Authority Index** (Google AI Overviews; updated Oct 10, 2026; Jul to Sep 2026 data):
  - Sample: 4,129 responses, 18,378 citation events and 1,759 domains.
  - Verticals: 11, including Online Stock Brokers, Robo-Advisors and Crypto Exchanges.
  - Metric: response coverage, the share of responses that cite a domain at least once.

  | Rank | Domain | Response coverage |
  |---|---|---|
  | 1 | NerdWallet | 17.8% |
  | 2 | YouTube | 17.2% |
  | 3 | Reddit | 16.3% |
  | 4 | Investopedia | 15.4% |
  | 5 | CNBC | 14.9% |
  | 6 | Money.com | 10.3% |
  | 7 | Yahoo | 8.7% |
  | 8 | Fidelity | 8.2% |
  | 9 | Forbes | 7.8% |
  | 10 | Bankrate | 7.3% |
  | 15 | WSJ | 3.3% |
  | 20 | Motley Fool (fool.com) | 2.8% |
  | 22 | Robinhood | 2.8% |
  | 84 | Morningstar | 0.7% |
  | n/a | Seeking Alpha, Bloomberg | not in top 100 |

  — [LLM Authority Index](https://llmauthorityindex.com/resources/research/top-100-google-ai-overviews-citations-investing-retirement-mortgage-financial-high-stakes-consumer-decisions)
- **Wealth-management study** (Mar 2026; press release): 201,233 citations. NerdWallet appeared in 38% of national-prompt responses and Bankrate in 35.3%. — [Yahoo Finance press release](https://finance.yahoo.com/news/study-200-000-ai-citations-120000960.html)

### Inferences
- **Where answers come from.** The default "evidence base" for an LLM stock answer is:
  - (a) stale parametric memory, or
  - (b) a handful of consumer explainer, affiliate and news sites, plus unweighted crowd chatter from Reddit and YouTube.

  None of these sources scores who is right. Reddit and YouTube make up roughly 16 to 17% coverage each in AI Overviews finance answers. They supply crowd opinion with no accuracy weighting, which is exactly the gap a scored-sentiment product would fill.
- **Product-comparison bias.** The heavily cited sources (NerdWallet, Bankrate, Investopedia) are built for product comparisons and definitions, not for ticker-level, time-sensitive signals. The verticals studied (brokers, robo-advisors, mortgages) suggest AI search is tuned to "which product" questions more than "which stock" questions.
- **Ownership links.** Some publishing partners own finance brands, for example News Corp (WSJ, Barron's, MarketWatch) and Dotdash Meredith (Investopedia). That likely biases ChatGPT toward those outlets for stock news. This is my inference from known ownership; the OpenAI page does not say it.
- **Size of the staleness gap.** The gap runs from about 4 months (Claude, cutoff Jun 2026) to about 21 months (Gemini 3.1 Pro, cutoff Jan 2025) as of Oct 21, 2026. Without a tool call, no model can know current prices, the latest earnings or recent sentiment.

### Gaps
- **No ticker-level citation study.** I found no study of which domains are cited for stock-ticker or stock-pick prompts (e.g., "Is NVDA a buy?"), so the shares of Seeking Alpha, Motley Fool, MarketBeat, Investing.com and Yahoo Finance quote pages for those prompts are unknown. Ahrefs, Semrush, BrightEdge and Similarweb finance-vertical breakdowns did not surface in my searches.
- **Cutoffs unconfirmed.** Training cutoffs come from secondary compilations, and I did not confirm them against vendor model cards.
- **ChatGPT's quote vendor and delay are unknown.** OpenAI has not publicly named the vendor behind its built-in stock charts or said whether quotes are delayed.

---

## Q2. Built-in finance data in the major assistants, and which include social sentiment or trader track records

### Takeaway
Every major assistant added licensed finance data in 2025 and 2026, but it is mostly institutional data: fundamentals, filings, transcripts, news, private-company data and estimates. The licensors include S&P, FactSet, LSEG, Morningstar, PitchBook, Daloopa, Moody's and Quartr. Crowd data reaches these assistants in only three ways:
- **Grok** reads raw X posts natively.
- **Perplexity** offers a bring-your-own Stocktwits connector for "bullish/bearish signals."
- **Google Finance** shows Kalshi and Polymarket prediction-market odds.

None of the assistants ships scored retail-trader track records. The closest is TipRanks' third-party MCP, which exposes analyst rankings and average returns.

### Cited Findings

**ChatGPT (OpenAI)**
- **Search with stock charts** (Oct 31, 2024): built with unnamed "data providers" for stocks. [VENDOR] — [OpenAI](https://openai.com/index/introducing-chatgpt-search/)
- **"Finances" in ChatGPT** (May 15, 2026) [INDEPENDENT, journalism]:
  - Access: preview for US Pro subscribers on web and iOS.
  - Data: read-only Plaid connections to "over 12,000 financial institutions" (Schwab, Fidelity, Robinhood, etc.).
  - Features: a dashboard of "portfolio performance, spending, subscriptions, and upcoming payments," running on GPT-5.5.
  - Plans: OpenAI plans Intuit support for tax analysis, such as "the impact of a stock sale on taxes."
  - The article describes no market-data feed and no sentiment data.

  — [TechCrunch](https://techcrunch.com/2026/05/15/openai-launches-chatgpt-for-personal-finance-will-let-you-connect-bank-accounts/)
- **ChatGPT for Financial Services** (Sep 10, 2026):
  - Audience: investment bankers and equity researchers, sold through enterprise sales.
  - Built-in premium data: Daloopa, PitchBook and LSEG News, with some reports adding Crunchbase and Quartr.
  - Uses: drafting research, building models and producing decks.

  — [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-10/openai-debuts-chatgpt-for-financial-services-an-investment-banker-tool); [VentureBeat](https://venturebeat.com/data/openai-launches-chatgpt-for-financial-services-with-integrated-data-sources-it-pulls-research-cites-it-and-builds-decks-in-minutes); [FinanceFeeds](https://financefeeds.com/openai-launches-chatgpt-for-financial-services-with-lseg-and-pitchbook-data/)
- **S&P Global** says its data portal is available through ChatGPT for Financial Services. [VENDOR] — [S&P Global Marketplace](https://www.marketplace.spglobal.com/en/solutions/chatgpt-(594c80a5-b40c-49ae-9f9c-c9f304590399))
- **OpenAI's own page** for this product returned HTTP 403, so the partner list relies on press coverage. Reports name the model "GPT-6 Astra," but I could not verify that name.

**Perplexity**
- **Core quote and fundamentals data:** Financial Modeling Prep (FMP), as described at the 2024 launch. — [Wikipedia: Perplexity AI](https://en.wikipedia.org/wiki/Perplexity_AI); [CO/AI](https://getcoai.com/news/perplexitys-new-finance-tool-makes-stock-research-a-breeze)
- **Third-party partner list:** FMP, Unusual Whales (options data), Quartr (live transcripts), Fiscal.ai, S&P Global Market Intelligence and Morningstar. [SECONDARY] — [FindMyMoat](https://www.findmymoat.com/vs/perplexity-finance-vs-sec-api-sec-api-io); [Techpoint Africa](https://techpoint.africa/guide/perplexity-finance-review/)
- **Official Help Center, "Premium Data Sources"** (undated; fetched Oct 2026) [VENDOR]:
  - **Included for all users:** Wiley, PitchBook Essentials, CB Insights, Statista and Midpage.
  - **Licensed bring-your-own connectors** (Pro, Max and Enterprise users with an eligible partner license):
    - FactSet, Morningstar, Daloopa, Zacks and Wisesheets (fundamentals)
    - Carbon Arc (alternative data)
    - AlphaCreek (SEC filings)
    - **Canary Data** ("accounting red flags, insider-trading signals")
    - MT Newswires (news) and Quartr (earnings calls and transcripts)
    - **Stocktwits** ("market sentiment, including trending tickers and bullish/bearish signals")
    - IBISWorld (industry research)
    - Interactive Brokers (drafts trades, never submits them)
  - **No options-flow provider** is named on this page.

  — [Perplexity Help Center](https://www.perplexity.ai/help-center/en/articles/12870803-premium-data-sources)

**Google (Gemini / Google Finance)**
- **Google Finance Deep Search** (Nov 2025): Gemini "will issue up to hundreds of simultaneous searches" and cites its sources. Google Finance also added prediction-market data from **Kalshi and Polymarket**. Google does not name a stock-price vendor. [VENDOR] — [Google Blog](https://blog.google/products-and-platforms/products/search/new-google-finance-ai-deep-search/); [PYMNTS](https://www.pymnts.com/google/2025/google-finance-rolls-out-ai-driven-deep-search-prediction-market-data/)

**Claude (Anthropic)**
- **Claude for Financial Services** launched in July 2025 with connectors for S&P Capital IQ, Daloopa, Morningstar and PitchBook. [VENDOR]
- **The Oct 27, 2025 expansion** [VENDOR] added:
  - **Aiera:** real-time earnings calls, with Third Bridge expert interviews through Aiera's connector.
  - **Chronograph:** private-equity data.
  - **Egnyte:** internal data rooms.
  - **LSEG:** "live market data" covering equities, fixed income, FX, macro indicators and analyst estimates.
  - **Moody's:** credit ratings and data on 600M+ companies.
  - **MT Newswires:** markets news.
- **No social or crowd sentiment connector** is listed.
- **Benchmark claim:** Anthropic says Sonnet 4.5 topped the Vals AI Finance Agent benchmark at 55.3%.

  — [Anthropic](https://www.anthropic.com/news/advancing-claude-for-financial-services)
- **Claude solutions page:** also lists FactSet among the pre-built integrations. [VENDOR] — [Claude Financial Services](https://claude.com/solutions/financial-services?m=1)

**Grok (xAI)**
- **Real-time X access** is Grok's distinguishing input. xAI's official cookbook shows Grok ingesting X posts through the Filtered Stream API and scoring market sentiment, with bitcoin as the worked example. [VENDOR] — [xAI Cookbook](https://docs.x.ai/cookbook/examples/sentiment_analysis_on_x); [xAI market monitoring](https://x.ai/grok/use-cases/market-monitoring) (that page returned 403; the description comes from search snippets)
- **Competitors lack this:** ChatGPT, Claude and Gemini do not have direct real-time X access. [SECONDARY] — [AI-Toolbox](https://www.ai-toolbox.co/advantages-use-cases-grok-toolbox/grok-for-traders-real-time-x-2026)

**Track-record data in LLM channels**
- **TipRanks MCP** (Jun 3, 2026) [VENDOR]:
  - Clients: Claude, ChatGPT (as an app), Cursor and Codex.
  - Data: analyst consensus, Smart Score screens and alerts, Smart Portfolio data via OAuth, earnings history and "trade-idea validation."

  — [TipRanks](https://www.tipranks.com/news/labs/bring-tipranks-into-every-investment-conversation-introducing-mcp); [TipRanks MCP](https://mcp.tipranks.com/)
- **TipRanks' analyst tool:** a third-party directory shows a `get_analysts_by_firm` tool that returns each analyst's `rank` and `avg_return_1y_pct`. These are sell-side analyst track records, not retail traders. [SECONDARY] — [Glama](https://glama.ai/mcp/connectors/com.tipranks/tipranks)
- **Stocktwits' own MCP:** CEO Howard Lindzon wrote that a Stocktwits MCP is being tested internally. The post is undated, and I could not confirm a launch. — [Howard Lindzon](https://www.howardlindzon.com/p/stocktwits-everywhere-as-the-web-disappears-bloomberg-terminals-for-everyone-and-the-trump-stock-mar)
- **Other sentiment MCPs:** StockPulse sells an "AI-ready social sentiment" MCP. Improvado offers a third-party StockTwits integration for Claude and ChatGPT. [VENDOR] — [StockPulse](https://stockpulse.ai/mcp-server-offering/); [Improvado](https://improvado.io/integrations/stocktwits)

### Inferences
- **The professional/retail split.** Institutional fundamentals and news are now commoditized inside the assistants: Claude and ChatGPT for FS, plus Perplexity's bring-your-own connectors. Crowd sentiment comes in only two forms:
  - raw and unscored: Grok over X, and Perplexity over the Stocktwits connector
  - market-priced: Google Finance with Kalshi and Polymarket
- **The whitespace.** No assistant was found to expose retail or social-trader track records, meaning who has been right on which tickers. That gap appears to be real whitespace. TipRanks covers it only for sell-side analysts and its own scores.
- **Competitive exposure.** Perplexity's Stocktwits connector and a pending Stocktwits MCP are the closest competitive threats to a "human sentiment into LLMs" product. Neither is documented as weighting users by accuracy.

### Gaps
- **"ChatGPT Finances Oct 2026" is unconfirmed.** One secondary result claimed an Oct 2, 2026 rollout of Finances to Free and Go users in the US, but I could not tie it to a verifiable source.
- **Unconfirmed vendors.** I could not confirm the real-time quote vendors behind ChatGPT's stock charts, Google Finance/Gemini, or Perplexity's current default feed, beyond FMP as of 2024.
- **Gemini outside Google Finance.** I could not confirm whether Gemini's app (as opposed to Google Finance) has dedicated finance connectors.
- **Grok's X sentiment is unmeasured.** I found no independent accuracy measurement of Grok's X-sentiment answers.

---

## Q3. Evidence that better inputs help: quantified deltas from retrieval, tools, news, sentiment and track-record data

### Takeaway
**For factual finance questions, retrieval and tools are clearly necessary but not enough:**
- GPT-4-Turbo with a naive retrieval system failed or refused 81% of FinanceBench questions, but reached about 85% accuracy when given the right passage.
- On Vals AI's Finance Agent benchmark, the best tool-using agents score only 60 to 64%, and higher scores track with more tool calls.

**For trading and prediction, the evidence is mixed:**
- Adding news, memory, reflection and multi-source analysts produces large backtest gains (FinAgent, TradingAgents).
- Richer news context adds about +8% accuracy (FinGPT).
- Rigorous 20-year tests (FINSABER) and live contests (Alpha Arena) show that most LLM trading "alpha" shrinks or disappears.

**The track-record result is the most striking number for this thesis.** Naive StockTwits crowd sentiment was 47.6% accurate (no better than chance). Sentiment from users filtered by their past accuracy was 72.8% accurate. That result has not yet been tested inside an LLM.

### Cited Findings

**Factual Q&A: with vs. without retrieval and tools**
- **FinanceBench** (Patronus AI, Nov 2023) [INDEPENDENT]: GPT-4-Turbo "used with a retrieval system incorrectly answered or refused to answer 81% of questions." — [arXiv 2311.11944](https://arxiv.org/abs/2311.11944v1)
- **FinanceBench breakdown** [SECONDARY]:
  - Shared vector store: 19% correct.
  - Per-document store: 50% correct.
  - Oracle passage given: 85% correct.
  - Long-context prompting: 79% correct.

  — [Beancount research log](https://beancount.io/bean-labs/research-logs/2026/05/12/financebench-open-book-financial-qa-benchmark)
- **Vals AI Finance Agent v1.1** (leaderboard as of Jun 4, 2026; 537 analyst-style questions; tools include Google web search and an HTML parser) [INDEPENDENT]:

  | Model | Accuracy |
  |---|---|
  | Claude Opus 4.7 | 64.37% |
  | Claude Sonnet 4.6 | 63.33% |
  | GPT 5.5 | 59.96% |
  | Gemini 3.1 Pro Preview | 59.72% |

  Vals says "the top performers on this benchmark also register relatively high numbers of tool calls," and "performance can be improved by allowing the model more tool calls and more tokens used, but this comes at a cost." — [Vals AI](https://www.vals.ai/benchmarks/finance_agent)
- **Vals Finance Agent v2** (Sep 23, 2026) [SECONDARY]: Gemini 3.8 Flash leads at 61.4%, and GLM 5.3 Flash is the best open-weight model at 57.9%. — [AllMind](https://allmind.ai/research/ai-financial-research-benchmarks-explained); [KuCoin blog](https://kucoin.com/blog/can-ai-replace-financial-analysts-in-2026-vals-ai-finance-agent-v2-reveals-gpt-5-5-hits-just-52-percent-accuracy)
- **FinSearchComp** (ByteDance; arXiv Sep 2025; ICLR 2026) [INDEPENDENT]:
  - Scope: 635 expert-annotated questions on time-sensitive data fetching and historical lookups, across 21 models and products.
  - The authors say web search plus financial plugins "substantially improves" results.
  - Grok 4 (web) tops the global subset, approaching expert level. A secondary leaderboard puts it at 68.9% against a 75.0% human-expert baseline.

  — [arXiv 2509.13160](https://arxiv.org/abs/2509.13160); [ICLR 2026](https://iclr.cc/virtual/2026/poster/10011221); [BenchmarkList](https://benchmarklist.com/benchmarks/finsearchcomp/)

**Trading and prediction: news, memory and multi-source inputs**
- **Lopez-Lira & Tang** (v6, Oct 2025) [INDEPENDENT]:
  - Data: GPT-4 sentiment scores on news headlines dated after the model's cutoff.
  - Result: about 90% portfolio-day hit rates on the initial (non-tradable) price reaction.
  - Scores also "significantly predict the subsequent drift," especially for small stocks and negative news.
  - Strategy returns decline as LLM adoption rises.

  — [arXiv 2304.07619 v6](https://arxiv.org/html/2304.07619v6)
- **FinAgent** (KDD 2024) [INDEPENDENT]:
  - Inputs: daily prices, K-line and trading charts, news (about 8k to 10k articles per stock from Bloomberg Technology, Seeking Alpha and CNBC) and "expert guidance."
  - Period: trained Jun 2022 to Jun 2023; tested Jun 2023 to Jan 2024 on AAPL, AMZN, GOOGL, MSFT, TSLA and ETH.
  - Result: ">36% average improvement on profit" over 12 baselines, and a 92.27% return on one dataset.
  - **Ablation results:**

  | Configuration | TSLA ARR | TSLA Sharpe | TSLA MDD | ETH ARR |
  |---|---|---|---|---|
  | News and price intelligence only | 39.27% | 0.77 | 30.15% | 25.97% |
  | + low-level reflection | 57.16% (+45.6%) | | | 52.33% (+101%) |
  | + high-level reflection | 89.25% | | | |
  | + rule-based tools | 92.27% | 2.01 | 12.14% | -21% vs. previous row |

  The stock-only tools hurt ETH, cutting its ARR by 21%. — [FinAgent paper (KDD '24)](https://personal.ntu.edu.sg/boan/papers/KDD24_FinAgent.pdf)
- **TradingAgents** (arXiv Dec 2024, v5) [INDEPENDENT]:
  - Inputs: prices; news from Bloomberg, Yahoo, EODHD, FinnHub and Reddit; **social media posts and sentiment from Reddit and X**; insider transactions; financials; and 60 technical indicators.
  - Period: Jan 1 to Mar 29, 2024, only 3 months "due to intensive LLM and tool use."

  | Ticker | TradingAgents cumulative return | Buy-and-hold | TradingAgents Sharpe |
  |---|---|---|---|
  | AAPL | 26.62% | -5.23% | 8.21 |
  | GOOGL | 24.36% | 7.78% | |
  | AMZN | 23.21% | 17.1% | |

  The authors say the AAPL Sharpe "exceeds our expected empirical range." In the portion of the paper I read, I found no ablation that isolates the social-media analyst. — [arXiv 2412.20138](https://arxiv.org/html/2412.20138v5)
- **FinGPT dissemination-aware model** (Dec 2024; AAAI 2025 workshop) [INDEPENDENT]: adding news dissemination breadth (clustering related news to estimate reach) and richer context "improves prediction accuracy by 8%" over existing methods. — [arXiv 2412.10823](https://arxiv.org/abs/2412.10823)

**Social sentiment and track-record weighting**
- **"Unleashing Expert Opinion from Social Media for Stock Prediction"** (Zhou et al., HKUST and IDEA Research; arXiv v2 Nov 10, 2025) [INDEPENDENT]:
  - **Naive crowd:** aggregated StockTwits sentiment predicted the next-day trend 47.63% of the time, "not better than random guessing."
  - **Expert definition:** users at ≥80% accuracy over their last 20 posts (spanning ≥5 trading days) **and** ≥65% accuracy over 2 years.
  - **Expert signals:** 72.8% T+1 accuracy, 13 and 15 points above the next-best user-centric models.
  - **Coverage tradeoff:** expert signals cover only about 4% of stock-days. Propagating them over industry and correlation graphs extends coverage to about 90%.
  - **NASDAQ-100 results:** accuracy 57.83% vs. 50.75% for the best baseline. A long-short top/bottom-decile strategy with 4bp costs returned 32.91% annualized at a Sharpe of 2.69.
  - **LLMs not tested:** the paper does not feed expert signals into an LLM. The authors propose using expert tracing to pick posts for LLM processing as future work.

  — [arXiv 2504.10078](https://arxiv.org/html/2504.10078)
- **User-centric StockTwits/Twitter study** (ACM) [INDEPENDENT]: StockTwits is more predictive than Twitter. Self-labeled sentiment is "only slightly predictive in aggregate over the short-term," and individual users show distinct predictive behaviors over a 144-day horizon. — [ACM 10.1145/3532856](https://dl.acm.org/doi/10.1145/3532856)
- **Leung, Wong & Wong** (SSRN) [INDEPENDENT]: social-media sentiment predicts returns less well when users follow more stocks, and the predictability is tied to users' ability to forecast earnings. — [SSRN 3492722](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3492722)
- **LLM-enhanced tweet emotion analysis** (arXiv Oct 2025) [INDEPENDENT; figure from search summary]: Llama 3.1-8B preprocessing of tweets raised the best model's accuracy from 23.6% to 38.5% on a multi-class task. — [arXiv 2510.03633](https://arxiv.org/pdf/2510.03633)

**Counter-evidence: gains shrink under rigorous or live testing**
- **FINSABER** (arXiv 2505.07078; KDD 2026) [INDEPENDENT]:
  - Scope: two decades and 100+ symbols.
  - Finding: "previously reported LLM advantages deteriorate significantly under broader cross-section and over a longer-term evaluation."
  - Behavior: LLM strategies are "overly conservative in bull markets... overly aggressive in bear markets."

  — [arXiv 2505.07078](https://arxiv.org/html/2505.07078v3)
- **Press coverage of FINSABER** (Jun 30, 2026) [INDEPENDENT, journalism]:
  - Buy-and-hold returned about 7.9% a year with the best risk-adjusted result in a low-volatility screen.
  - One AI agent hit about 14% a year but with steep drawdowns.
  - A 55-year-old ARIMA model beat the AI tools on a risk-adjusted basis.
  - Larger models did not reliably outperform smaller ones.

  — [Moneywise via Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/think-outsmart-market-letting-ai-130000111.html)
- **Alpha Arena Season 1** (live crypto perpetuals on Hyperliquid; $10k per model; ended Nov 3, 2025; price data only) [INDEPENDENT event; SECONDARY reporting]. Season 1.5 was won by "Grok 4.20" at +12.11% over 14 days, and by Dec 8 it was reportedly the only profitable model.

  | Model | Final balance from $10,000 |
  |---|---|
  | Qwen3 Max | $12,231 (+22.3%) |
  | DeepSeek | $10,489 |
  | Claude Sonnet 4.5 | $5,799 |
  | Gemini 2.5 Pro | $5,445 |
  | Grok 4 | $4,208 |
  | GPT-5 | $4,126 |

  — [Forklog](https://forklog.com/en/four-out-of-six-ai-models-suffer-losses-in-trading-tournament/amp); [Forklog S1.5](https://forklog.com/en/ai-model-grok-4-2-triumphs-in-trading-tournament/amp)

### Inferences
- **The strongest pitch is factual accuracy.** The most defensible quantified case for "better data" is accuracy on factual or analytical questions. FinanceBench shows the swing from 19% to 85% correct depends on what data reaches the model and how. Vals shows tool use drives the leaderboard.
- **"LLM + data = alpha" is not established.** Backtest gains from news and multi-source agents are large but fragile: short windows, mega-cap tickers and possible look-ahead.
- **The track-record result fits this business directly.** Unfiltered crowd sentiment is roughly a coin flip (47.6%), while accuracy-filtered experts reach 72.8%. That supports selling scored track records rather than raw sentiment, which Grok and the Stocktwits connector already provide. The catch is sparse coverage (about 4% of stock-days), so propagation or aggregation is needed.
- **There is no published LLM test yet.** I found no study that feeds accuracy-weighted crowd signals into an LLM and measures the change. A business could run and publish that experiment itself, as a white paper or benchmark, to prove the gap.
- **The edge decays with adoption.** Lopez-Lira & Tang find returns fall as LLM adoption rises. Any edge from data that everyone's LLM can reach will decay, so value accrues to proprietary or differentiated signals.

### Gaps
- **No published delta for social or track-record data.** I found no study reporting the change in an LLM agent's accuracy or returns from adding social sentiment or track-record data in a controlled ablation. TradingAgents uses social data but reports no ablation in the portion I read.
- **FinMem not extracted.** FinMem's quantified results (backbone, memory and character ablations on TSLA) were not pulled in detail.
- **FinGPT +8% baseline unverified.** A search summary claimed 63% vs. 55% for the FinGPT result, but I could not verify the underlying baseline and metric.
- **FinSearchComp search delta missing.** I did not find the exact with- vs. without-search numbers in the paper's tables.
- **Vals v2 not primary-confirmed.** Vals Finance Agent v2 figures come from secondary sources, and they conflict with each other (52% vs. 60.6% vs. 61.4%).

---

## Q4. Known failure modes tied to data

### Takeaway
The documented failure modes are:
- stale knowledge
- wrong or hallucinated figures (43% average accuracy on money questions in one Sep 2026 test; 15% wrong even with the correct passage on FinanceBench)
- fabricated citations
- concentration on popular sources and large-cap, prominent stocks
- inconsistent answers to identical prompts
- look-ahead and survivorship bias that inflates published backtests
- weakness with numeric time series
- regime-blind behavior

I found herding discussed only as a risk, with no empirical measurement.

### Cited Findings

**Wrong or hallucinated numbers**
- **Saturn "Artificial Authority"** (Sep 2026; commercial firm) [INDEPENDENT-ish]:
  - Scope: 18 models, 121 money questions, each run 5 times.
  - Result: 43% average accuracy across 17 current models, falling to 12% on multi-step questions involving tax rules and precise figures.

  — [Yahoo Tech](https://tech.yahoo.com/ai/chatgpt/articles/ai-could-costing-money-study-161730747.html); [InvestmentNews](https://www.investmentnews.com/fintech/ai-chatbots-give-wrong-financial-answers-most-of-the-time-study-finds/268267)
- **Vanguard survey:** 37% of respondents reported getting incorrect or misleading information from AI. MIT researchers (Lo and Ross) found chatbots overlooking key financial details. — [TheStreet](https://www.thestreet.com/personal-finance/vanguard-mit-chatbot-financial-advice-risks)
- **Fabricated finance citations** (2024 study): chatbots hallucinated about 20% to 77% of the finance citations they produced. — [arXiv 2411.07031](https://arxiv.org/pdf/2411.07031)
- **FinanceBench:** even with the oracle passage, GPT-4-Turbo reached only about 85% accuracy. [SECONDARY breakdown] — [Beancount](https://beancount.io/bean-labs/research-logs/2026/05/12/financebench-open-book-financial-qa-benchmark)

**Over-reliance on popular sources and popular stocks**
- **Citation concentration:** AI Overviews finance answers are concentrated in NerdWallet (17.8% coverage), YouTube (17.2%) and Reddit (16.3%). — [LLM Authority Index](https://llmauthorityindex.com/resources/research/top-100-google-ai-overviews-citations-investing-retirement-mortgage-financial-high-stakes-consumer-decisions)
- **"Your AI, Not Your View"** (Lee et al.) [INDEPENDENT]:
  - Scope: 427 S&P 500 stocks.
  - Result: bias scores decline as company size decreases, which indicates a preference for large caps.
  - Cause: the authors attribute this to a popularity effect, since prominent firms appear more often in training data.
  - Models also show a contrarian-strategy preference.

  — [arXiv 2507.20957](https://arxiv.org/pdf/2507.20957); [ACM](https://dl.acm.org/doi/10.1145/3768292.3770375)
- **"Multifaceted variability in LLM-driven stock recommendations"** (ScienceDirect) [INDEPENDENT]: LLMs show a "structural bias toward recommending large-cap stocks." Portfolios built from their picks underperform the S&P 500 risk-adjusted, and identical prompts produce substantially different recommendations. — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1544612325021762)
- **Product-bias study** (7 LLMs) [SECONDARY summary]: stock recommendations showed the highest concentration of any category, with an average Gini index of 0.95. — [Lacuna](https://lacuna.tiptreesystems.com/work/exposing-product-bias-in-llm-investment-recommendation/wrk_275d4271c80fcd83e468de938fb0211a)

**Herding and crowding**
- **CFA Institute commentary (2026):** AI investment advice may increase concentration by overweighting dominant sectors and assets, and could amplify herding. This is commentary, not a measurement. — [CFA Institute Enterprising Investor](https://rpc.cfainstitute.org/blogs/enterprising-investor/2026/attention-bias-in-ai-driven-investing)
- **Lopez-Lira & Tang:** strategy returns decline as LLM adoption rises, consistent with crowding into the same signal. — [arXiv 2304.07619 v6](https://arxiv.org/html/2304.07619v6)

**Look-ahead, survivorship and data snooping**
- **Glasserman & Lin** (Sep 2023) [INDEPENDENT]:
  - Look-ahead bias overstates the performance of LLM-based strategies.
  - A separate "distraction effect" (from knowing company identity) can cut either way.
  - Anonymizing headlines *improved* in-sample performance of a GPT-3.5 sentiment long-short strategy, especially for large companies.

  — [arXiv 2309.17322](https://arxiv.org/abs/2309.17322)
- **Dec 2025 follow-up:** masking or anonymizing identifiers only partly helps, because subtler memorization channels remain. — [Hugging Face paper page 2512.23847](https://huggingface.co/papers/2512.23847.md)
- **Look-Ahead-Bench** (Jan 2026): a standardized benchmark for look-ahead bias in point-in-time finance LLMs. — [arXiv 2601.13770](https://arxiv.org/pdf/2601.13770)
- **FINSABER:** short windows and narrow stock universes overstate LLM strategies "due to survivorship and data-snooping biases." — [arXiv 2505.07078](https://arxiv.org/html/2505.07078v3)

**Numeric and time-series weakness, and regime blindness**
- **Alpha Arena:** "LLMs do not handle numerical time series data well." — [AIbase](https://www.aibase.com/news/23442)
- **FINSABER:** LLM strategies are too conservative in bull markets and too aggressive in bear markets. — [arXiv 2505.07078](https://arxiv.org/html/2505.07078v3)

### Inferences
- **Most failure modes are input problems.** Several of these failures (stale knowledge, wrong figures, popularity and large-cap bias, crowding) are at least partly input problems. Point-in-time, structured, fresh and differentiated data addresses them more directly than a bigger model does. The FINSABER finding that larger models did not reliably beat smaller ones supports this.
- **Scored sentiment counters popularity bias.** Accuracy-weighted crowd data could counter the popularity bias, because it weights who has been right rather than who is loudest or most-cited. No study I found tests this inside an LLM.
- **Point-in-time stamps are a selling point.** Look-ahead risk means any data vendor claiming that its data "improves LLM returns" must show point-in-time, post-cutoff, out-of-sample tests, or sophisticated buyers will discount the claim. Timestamped track-record data that cannot be revised later is a selling point here.

### Gaps
- **No systematic stale-price audit.** I found no systematic audit of how often ChatGPT, Gemini, Claude or Perplexity give wrong or stale stock prices. The only evidence was an anecdotal vendor-blog mention of wrong Perplexity quotes for QBTS, CLSK and IONQ, which I could not verify.
- **No herding study.** I found no empirical study of herding among investors induced by LLMs.
- **Sentiment-specific failure rates.** I found no measurement of how sentiment-driven LLM answers fail, for example amplifying pump-and-dump chatter from Reddit or X.
