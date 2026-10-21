# How accurate are LLMs (ChatGPT, Claude, Gemini, Grok, DeepSeek, Qwen, Perplexity) at stock-market tasks? (as of Oct 21, 2026)

Source-type legend used below: **[PEER]** = peer-reviewed journal or conference; **[PRE]** = preprint or working paper (arXiv/SSRN/NBER); **[CO]** = company-run live experiment or commercial benchmark; **[JOUR]** = journalism or newsroom audit; **[MKT]** = marketing or vendor content, or an anecdotal test.

## Key Question 1: Live and real-money LLM trading or stock-picking experiments, and how they did vs. the S&P 500

### Takeaway
Live, head-to-head LLM trading contests (nof1 Alpha Arena) show most frontier models **losing money**. In Season 1 (crypto, Oct–Nov 2025), 4 of 6 models lost 30–63%. In Season 1.5 (tokenized US stocks, Nov–Dec 2025), only one model, an unreleased Grok 4.20, was profitable in a mid-run snapshot. The most rigorous forward-looking study of chatbot stock picks (NBER, Aug 2025–Apr 2026) found that the portfolios beat the S&P 500 on raw returns. That edge disappeared once the analysis adjusted for size, growth, and momentum tilts: no abnormal returns. "ChatGPT beat the funds" headlines come from short, hypothetical, 2023-era marketing tests.

### Cited Findings
**nof1 Alpha Arena, Season 1 (crypto perpetuals, real money) [CO]**
- Setup: each model got $10,000 in real capital and traded crypto perpetual contracts autonomously on the decentralized exchange Hyperliquid, with identical prompts and no human intervention. — [iWeaver recap](https://www.iweaver.ai/blog/alpha-arena-ai-trading-season-1-results/); [Jiemian](https://en.jiemian.com/article/13592098.html)
- Dates: launched Oct 18, 2025 and ran 17 days. One report gives the end date as Nov 3, 2025. — [Jiemian](https://en.jiemian.com/article/13592098.html); [TechNews.tw](https://technews.tw/2025/11/04/ai-large-model-trading-contest-qwen-winner/)
- Final returns as reported by iWeaver: Qwen3 Max **+22.3%**, DeepSeek Chat V3.1 **+4.89%**, Claude Sonnet 4.5 **−30.81%**, Grok 4 **−45.3%**, Gemini 2.5 Pro **−56.71%**, GPT-5 **−62.66%**. Qwen made only about 43 trades (fewer than 3 a day). — [iWeaver](https://www.iweaver.ai/blog/alpha-arena-ai-trading-season-1-results/)
- Conflicting final balances from other coverage: Qwen ~$12,231, DeepSeek ~$10,489, Claude ~$5,799, Gemini ~$5,445, Grok ~$4,208, GPT-5 ~$4,126. A $4,126 balance implies about −59% for GPT-5, not −62%. The two Chinese models were the only profitable ones, and all four US models ended in the red. — [search summary of Jiemian, TechNews, iWeaver coverage](https://en.jiemian.com/article/13592098.html); contradicted in detail by [iWeaver](https://www.iweaver.ai/blog/alpha-arena-ai-trading-season-1-results/)
- Mid-run leaders were different. Decrypt reported Grok, DeepSeek, and Claude leading early and Gemini "imploding", which shows high path dependence and volatility. — [Decrypt](https://decrypt.co/345006/ai-crypto-trading-showdown-deepseek-grok-winning-gemini-implodes)
- Bitcoin Magazine headline: "Western models lose 80% capital in one week" (a mid-run drawdown). — [Bitcoin Magazine](https://bitcoinmagazine.com/business/alpha-arena-reveals-ai-trading-flaws-western-models-lose-80-capital-in-one-week)
- Caveat: one 2026 source says the official Season 1 pages on nof1's site are no longer available, so the figures rely on founder posts and press. — [search summary citing traderank/onedayadvisor](https://www.traderank.ai/blog/alpha-arena-alternatives-2026)

**nof1 Alpha Arena, Season 1.5 ("US stocks") [CO]**
- Launched Nov 20, 2025. Models "live-trad[ed] U.S. stock tokens on trade.xyz", which are tokenized equities on a crypto venue, not shares at a broker. All models in a match received identical inputs. — [Lookonchain, Dec 6, 2025](https://m.lookonchain.com/feeds/39476)
- Competition modes: New Baseline, Monk Mode, Situational Awareness, Max Leverage. — [ForkLog, Dec 8, 2025](https://forklog.com/en/ai-model-grok-4-2-triumphs-in-trading-tournament/)
- Snapshot as of Dec 6, 2025 (not final): Grok 4.20 **+22.38%**, GPT-5.1 **−2.29%**, Gemini 3 Pro **−25.74%**, DeepSeek 3.1 **−29.16%**, Kimi 2 **−29.93%**, Qwen3-Max **−31.9%**, Claude Sonnet 4.5 **−35.08%**, Grok 4 **−53.39%**. Only 1 of 8 models was profitable. — [Lookonchain](https://m.lookonchain.com/feeds/39476)
- Winner: the "Mystery Model", later revealed as Grok 4.20, with a **+12.11% aggregate return over about 2 weeks**. nof1 framed this as an aggregate across the competitions, worth $4,844 in total. It was reportedly profitable in all 4 competitions. — [ForkLog](https://forklog.com/en/ai-model-grok-4-2-triumphs-in-trading-tournament/); [Powerdrill/Polymarket summary](https://powerdrill.ai/bloom/polymarket/alpha-arena-season)
- Sources disagree on the end date: one says the season ended Dec 3, 2025, while Lookonchain's "as of Dec 6" snapshot implies trading was still live. — [Powerdrill](https://powerdrill.ai/bloom/polymarket/alpha-arena-season); [Lookonchain](https://m.lookonchain.com/feeds/39476)
- Later seasons: nof1 raised $15M and said Season 2 would add web search, extended reasoning, and multi-step execution. — [AI Weekly](https://aiweekly.co/alerts/nof1-raises-15m-to-run-ai-models-in-live-trading). A third-party check in Aug 2026 said the homepage still showed Season 1.5 (closed Dec 2025) as the latest season. — [search summary of traderank.ai](https://www.traderank.ai/blog/alpha-arena-alternatives-2026). nof1.ai now describes itself as an "AI research lab for financial markets" and links out to alphaarena.ai, which returned HTTP 403 to my fetch. — [nof1.ai](https://nof1.ai/)

**Other arenas [CO/MKT]**
- Rallies.ai "AI Trading Arena" (hypothetical $100k portfolios in US stocks, benchmarked to the S&P 500): as of early Jan 2026, DeepSeek-v3 ranked #1 with about **+4.6% over one month**. GPT-5, Claude, Gemini, and Grok were also entered, with no figures given. — [OneDayAdvisor](https://www.onedayadvisor.com/2026/01/AI-stock-trading.html)

**Forward-looking academic test of chatbot stock picks [PRE, NBER working paper]**
- Carlin, Israelsen & Wazzan, NBER w35153. Models: ChatGPT 5.0 and 5.2, Claude Sonnet 4.5, Gemini 2.5 Flash, Grok 4.1 Fast. Daily prompts ran from Aug 2025 to Apr 2026, giving >1,200 portfolio-day observations across 7 actively managed variants and 5 buy-and-hold prompts. — [NBER w35153](https://www.nber.org/papers/w35153); [Science of Money summary, Jun 5, 2026](https://www.scienceofmoney.org/when-chatbots-play-stock-picker-what-ai-actually-recommends-for-your-portfolio-559/)
- All 7 active portfolios beat the S&P 500 on cumulative return, and Sharpe ratios beat the benchmark in all but one specification. After Daniel-Grinblatt-Titman-Wermers characteristic adjustment (size, book-to-market, momentum), **outperformance largely disappeared**. Daily adjusted returns were not statistically different from zero, and buy-and-hold excess returns were mostly insignificant from 1 day to 6 months. — [Science of Money](https://www.scienceofmoney.org/when-chatbots-play-stock-picker-what-ai-actually-recommends-for-your-portfolio-559/)
- Caveat: the Claude, Gemini, and Grok samples cover only about 1 month of unusually strong markets. The Gemini result rests on 18 trading days. — [Science of Money](https://www.scienceofmoney.org/when-chatbots-play-stock-picker-what-ai-actually-recommends-for-your-portfolio-559/)

**2023-era "ChatGPT fund" marketing tests [MKT]**
- Finder.com (UK): ChatGPT (GPT-3.5 era) picked a 38-stock dummy portfolio. It gained **+4.9% from Mar 6 to Apr 28, 2023**, against **−0.8%** for the average of the 10 most popular UK funds on Interactive Investor. No real money was invested. — [AI Business](https://aibusiness.com/nlp/chatgpt-picked-stocks-outperform-top-u-k-mutual-funds); [Business Standard](https://www.business-standard.com/amp/technology/tech-news/portfolio-created-by-chatgpt-reports-better-returns-than-top-funds-in-uk-123050500240_1.html)
- Finder update: **+9.4% from Mar 6 to Aug 18, 2023** vs **+1.67%** for the equal-weighted 10-fund composite, reportedly also ahead of the S&P 500. Finder's CEO cautioned that it was "too early" to trust AI with finance. — [AI Business](https://aibusiness.com/nlp/chatgpt-picked-stocks-outperform-top-u-k-mutual-funds); [Daily Wire](https://www.dailywire.com/news/chatgpt-built-a-stock-portfolio-outperforming-several-popular-funds)

### Inferences
- In live contests, the losses come largely from **position sizing, leverage, and over-trading**, not just bad information. The best Season 1 performer traded least. Better data alone may not fix this. Data that includes risk context, such as crowding and sentiment extremes, is a plausible differentiator but is untested.
- Raw "beat the S&P" results for chatbot portfolios are mostly **factor exposure**: large-cap, semiconductors, momentum, and high beta during a tech rally. That is beta, not skill.
- Every live sample is tiny (6–8 models, 2–3 weeks, one market regime). None is statistically conclusive in either direction.

### Gaps
- I could not reach alphaarena.ai (HTTP 403). Final, official per-model Season 1.5 numbers for each competition mode remain unverified, and I found no Season 2 results by Oct 2026.
- I found no Bloomberg, CNBC, or Fortune primary coverage in my searches. Season 1 numbers come from secondary outlets that disagree by a few percentage points.
- I did not verify the Motley Fool UK GPT-4 test (reported second-hand as +17.4% vs +13.0% S&P over 9 months), a WSJ ChatGPT-allocation test (reported as lagging an ~8% S&P gain), or Reddit and Substack $100 to $5,000 experiments. These appear only in search summaries. Leads: [scienceofmoney.org](https://www.scienceofmoney.org/when-chatbots-play-stock-picker-what-ai-actually-recommends-for-your-portfolio-559/), [vocal.media](https://vocal.media/trader/i-handed-chat-gpt-100-to-trade-stocks-here-s-what-happened-in-2-months), [wadeswatch.com](https://www.wadeswatch.com/chatgpt-picked-my-stocks-vs-wall-street-i-let-ai-invest-against-the-s-p-500/), [edgen.tech "$1M portfolio trails S&P"](https://edgen.beta.edgen.tech/news/post/chatgpt-manages-a-1-million-portfolio-and-trails-the-sp-500).
- I did not research the Autopilot app or other commercial "AI-picked" funds.

## Key Question 2: Academic studies on forecasting, trading benchmarks, look-ahead bias, recommendation biases, and LLM-as-advisor

### Takeaway
The flagship positive result (Lopez-Lira & Tang) is real but **decaying fast**: the Sharpe ratio fell from 6.5 in late 2021 to 1.2 in 2024, and the strategy is unprofitable above about 20 bps in trading costs. Contamination-free trading benchmarks (StockBench, 2025) show frontier agents earning 0–2.5% over 4 months on DJIA stocks, roughly matching buy-and-hold. Much of the apparent LLM forecasting "alpha" in backtests is **memorization** (look-ahead bias). Several independent studies find that LLM recommendations are systematically tilted toward large-cap, tech, high-attention, momentum, and high-beta names. As advisors, LLMs give plausible but poorly personalized advice.

### Cited Findings
**Forecasting from news (Lopez-Lira & Tang, "Can ChatGPT Forecast Stock Price Movements?") [PRE, arXiv 2304.07619 v6, Oct 2025]**
- v6 sample: Oct 2021 to May 2024 (after GPT-4's Sept 2021 training cutoff). It covers 159,137 firm-headline-date observations for 4,123 firms, about 85% of CRSP. — [arXiv v6](https://arxiv.org/html/2304.07619v6)
- Initial-reaction hit rate is **93.3%** for overnight news and **88.8%** for intraday news, but the paper calls this non-tradable without early access. — [arXiv v6](https://arxiv.org/html/2304.07619v6)
- Tradable next-day "drift" using GPT-4 (before costs): overnight hit rate 58%, 0.34% a day, Sharpe 2.97; intraday hit rate 55%, 0.50% a day, Sharpe 2.63. Predictability is concentrated in negative news: the short leg earns 26 bps a day (Sharpe 2.01) vs 8 bps for the long leg. — [arXiv v6](https://arxiv.org/html/2304.07619v6)
- Model ranking by drift Sharpe: GPT-4 2.97 > GPT-3.5 1.66 > DistilBart 1.26 > BART-large 1.05 > Llama2-70b 0.97. GPT-1, GPT-2, and BERT had negative drift Sharpe ratios. — [arXiv v6](https://arxiv.org/html/2304.07619v6)
- **Decay:** annualized long-short Sharpe was **6.54 (2021Q4) → 3.68 (2022) → 2.33 (2023) → 1.22 (Jan–May 2024)**. The authors link this to rising LLM adoption and call it "suggestive" evidence. — [arXiv v6](https://arxiv.org/html/2304.07619v6)
- **Costs:** gross cumulative return was about 700% (Oct 2021 to May 2024) with turnover around 190% a day. It falls to >300% at 5 bps, >100% at 10 bps, and the strategy is **unprofitable at 20 bps** round-trip. — [arXiv v6](https://arxiv.org/html/2304.07619v6)
- The first version (Apr 2023) covered Oct 2021 to Dec 2022 headlines and reported that GPT-4-based long-short strategies had the highest Sharpe ratio. — [arXiv v1](https://arxiv.org/abs/2304.07619v1); [InvestorDaily](https://www.investordaily.com.au/chatgpt-can-forecast-stock-price-movements-study-finds)

**Trading-agent benchmarks**
- **StockBench** [PRE, arXiv 2510.02209, Oct 2025]. Contamination-free test window: Mar 3 to Jun 30, 2025 (82 trading days). Top 20 DJIA stocks, $100k starting cash, daily prices, fundamentals, and news. Results are averages of 3 runs:

  | Model | Return | Max drawdown | Sortino |
  |---|---|---|---|
  | Kimi-K2 | +1.9% | −11.8% | 0.042 (rank 1) |
  | Qwen3-235B-Ins | +2.4% | −11.2% | — |
  | GLM-4.5 | +2.3% | — | — |
  | Qwen3-235B-Think | +2.5% | — | — |
  | OpenAI o3 | +1.9% | — | — |
  | Claude-4-Sonnet | +2.2% | — | — |
  | DeepSeek-V3.1 | +1.1% | — | — |
  | GPT-5 | +0.3% | — | — |
  | DeepSeek-V3 | +0.2% | — | — |
  | **Passive buy-and-hold** | **+0.4%** | **−15.2%** | — |
  | GPT-OSS-120B | −0.9% | — | — |
  | GPT-OSS-20B | −2.8% | — | — |

  — [arXiv 2510.02209](https://arxiv.org/html/2510.02209v1)
- The StockBench abstract says "most LLM agents struggle to outperform the simple buy-and-hold baseline", yet the body says "most tested models outperform" it. The paper is internally inconsistent. In practice, returns were within ±2.5 percentage points of the baseline with drawdowns of 11–15%. — [arXiv 2510.02209](https://arxiv.org/html/2510.02209v1)
- StockBench also concludes that "excelling at static financial knowledge tasks does not necessarily translate into successful trading strategies", and that reasoning-tuned models did not consistently beat instruction-tuned ones. — [arXiv 2510.02209](https://arxiv.org/html/2510.02209v1)
- **FinBen** [PEER, NeurIPS 2024 Datasets & Benchmarks]. Older work: 15 to 21 LLMs across 35 to 42 datasets (the count varies by version). On the FinTrade task (10 stocks, 1 year), GPT-4 had a Sharpe >1, and "all LLMs show better performance than Buy & Hold." This period likely overlaps training data, so look-ahead bias is a risk. — [NeurIPS slides](https://nips.cc/media/neurips-2024/Slides/97525.pdf); [arXiv 2402.12659](https://www.arxiv.org/pdf/2402.12659v1)
- **InvestorBench** [PRE, arXiv 2412.18174, Dec 2024]. 13 LLMs on stock, crypto, and ETF trading. Proprietary and larger models generally did better, but "all models struggle in highly volatile market conditions." — [alphaXiv](https://www.alphaxiv.org/overview/2412.18174v1)

**Look-ahead and memorization bias**
- "A Test of Lookahead Bias in LLM Forecasts" [PRE, arXiv 2512.23847, Dec 2025]. Introduces "Lookahead Propensity" (LAP). On Llama-3.3, memorization "substantially amplifies" the apparent predictive power of LLM return forecasts, and the effect loses significance on post-cutoff samples. — [arXiv 2512.23847](https://arxiv.org/html/2512.23847v1)
- "The Memorization Problem" [PRE, arXiv 2504.14765]. Forecasting skill is non-identified when the model has seen the outcomes. Instructions to "respect historical boundaries" fail to prevent recall-level accuracy. — [arXiv 2504.14765](https://arxiv.org/html/2504.14765v2)
- Somoza, Didisheim & Fraschini, "AI's predictable memory in financial analysis" [PEER, *Economics Letters*, 2025]. Prompts LLMs to recall historical returns as a memorization proxy. Smaller models and finer data granularity show negligible bias. — [ESSEC](https://faculty.essec.edu/research/16148-ais-predictable-memory-in-financial-analysis)
- Look-Ahead-Bench (Benhenda, 2026) [PRE, reported second-hand by a vendor, vBase/validityBase, Apr 21, 2026]. Matched 6-month windows with ~25% buy-and-hold return each: in-sample Apr–Sep 2021 vs out-of-sample Jul–Dec 2024. DeepSeek 3.2's annualized alpha went from **+20.73% in-sample to −1.04% out-of-sample**. Llama 3.1 8B went from +13.81% to −3.42%. A point-in-time model ("Pitinf-Large") went from +6.02% to +7.32%. — [HedgeFundAlpha](https://hedgefundalpha.com/education/your-llms-alpha-might-be-mere-memorization/). Caveat: the source sells point-in-time tooling, and I did not read the original paper.

**Recommendation biases**
- Lee, Seo, Park, Lee, Ahn, Choi, Lopez-Lira & Lee, "Your AI, Not Your View" [PRE, arXiv 2507.20957, Jul 2025]. Covered 427 S&P 500 stocks, 3,416 generated evidence items, and 10 repeats per stock. Models: Llama4-Scout, DeepSeek-V3, Qwen3-235B, Gemini-2.5-flash, GPT-4.1, Mistral-24B. — [arXiv](https://arxiv.org/html/2507.20957v1)
  - **Large-cap preference.** DeepSeek-V3 had a top-quartile vs bottom-quartile cap gap of 0.187 (p<0.001), and Qwen3 a gap of 0.118 (p=0.004). For GPT-4.1 the gap was 0.032 (not significant). — [arXiv](https://arxiv.org/html/2507.20957v1)
  - **Technology preference** scores: Llama4-Scout 0.90, DeepSeek-V3 0.84, Qwen3 0.61, Gemini 0.50, Mistral 0.44, GPT-4.1 0.39. Sector preferences varied across models with "no overall trend." — [arXiv](https://arxiv.org/html/2507.20957v1)
  - **Contrarian over momentum** in balanced-prompt tests, which is the opposite of what the NBER live portfolios showed. — [arXiv](https://arxiv.org/html/2507.20957v1)
  - **Confirmation bias.** At the strongest counter-evidence setting, most models flipped their view less than 60% of the time. — [arXiv](https://arxiv.org/html/2507.20957v1)
- Carlin, Israelsen & Wazzan (NBER w35153), live picks: **semiconductors averaged 41%** of AI portfolios vs ~20% of the S&P 500. ChatGPT 5.0 put **18–20% in Nvidia**. Picked stocks had **~10× the news coverage** of the average Compustat firm and an **average beta of ~1.6**, with a momentum and growth tilt. Gemini's median portfolio held 4.5 names, and concentration rose over time. Models visited about 16 websites per query, about two-thirds of them corporate sites. Prompt wording did not meaningfully change picks. — [Science of Money](https://www.scienceofmoney.org/when-chatbots-play-stock-picker-what-ai-actually-recommends-for-your-portfolio-559/)
- A CFA Institute Enterprising Investor piece (Feb 18, 2026) cites Choi et al. (2025) on size and sector bias, Aghbabali, Chung & Huh (2025) on investors trading "in the same direction" after ChatGPT's release (herding), Cao, Wang & Xiang (2025) on foreign bias, and Winder et al. (2024) on increased concentration. The article itself gives no figures. — [CFA Institute](https://rpc.cfainstitute.org/blogs/enterprising-investor/2026/attention-bias-in-ai-driven-investing)

**LLMs as financial advisors**
- Baeckström & Matkovskyy, "Financial advice behaviour: humans versus AI" [PEER, *Journal of Corporate Finance*; KCL release Jul 29, 2026]. Compared 9 LLMs (GPT incl. a GPT-5.2 configuration, Gemini, Claude) with 190 human advisers on 10 fictional clients. The most conservative AI configuration reached about £189,100 in terminal wealth after 20 years vs about £230,700 for the average human recommendation, an **18% shortfall, or up to £42k per £100k**. The extra caution brought "little reduction in long-term volatility." Break-even is a human fee of 1.03%. — [King's College London](https://www.kcl.ac.uk/news/ai-investment-advice-may-sacrifice-returns-without-reducing-risk)
- "Biased echoes" (St. Gallen/TUM) [PEER, *PLOS ONE*, Jun 2025]. LLMs favored stock-picking and active funds over index funds, and recommended portfolios with higher expense ratios. Simple de-biasing prompts had limited effect. — [PLOS ONE](https://journals.plos.org/plosone/article%3Fid=10.1371/journal.pone.0325459); [Univ. St. Gallen](https://www.unisg.ch/en/newsroom/be-careful-financial-advice-from-ai-comes-with-risks/)
- Takayanagi et al., "Are Generative AI Agents Effective Personalized Financial Advisors?" [PRE, arXiv 2504.05862, 2025]. A 64-participant user study. Personalization helped only when preference elicitation was accurate. With complex or contradictory profiles, elicitation accuracy fell "to random levels", and users could not tell good advice from bad. — [arXiv 2504.05862](https://arxiv.org/pdf/2504.05862)
- "One Size Fits None: Heuristic Collapse in LLM Investment Advice" [PRE, arXiv 2604.23837, Apr 2026]. Allocations were driven mostly by stated risk tolerance, with age, income, horizon, and liquidity contributing little. Web search improved diversification but made advice **more uniform** across clients. — [arXiv 2604.23837](https://arxiv.org/pdf/2604.23837)

### Inferences
- Positive academic results cluster in **(a) older, likely contaminated backtests** (FinBen, early Lopez-Lira) or **(b) non-tradable or tiny edges**. Once a test is post-cutoff and trades with costs, the edge shrinks toward zero.
- LLMs converge on the same high-attention megacaps. This homogeneity is a crowding risk and an opening for a product that brings in information about non-consensus names or crowd-positioning data.
- Biases differ by model (contrarian in controlled tests, momentum in live picks). LLM stock opinions are unstable artifacts of training text and retrieval, not consistent strategies.

### Gaps
- I did not find a published, peer-reviewed version of Lopez-Lira & Tang. It is still cited here as an arXiv/SSRN working paper (v6).
- InvestorBench per-model return numbers and BizFinBench results were not retrieved.
- I found no 2026 contamination-free trading benchmark covering the newest frontier models (e.g., GPT-5.5, Claude Opus 5, Gemini 4).
- The MIT/Stanford study reporting that ChatGPT-5.2 recommended lower equity allocations for women was seen only in a secondary summary and is unverified.

## Key Question 3: Factual accuracy, meaning wrong or stale prices, wrong financial figures, and fabricated news or citations

### Takeaway
On grounded financial Q&A over SEC filings, even tool-using frontier agents get only about 59–65% right on analyst-level tasks (Vals AI, Oct 2026). Earlier retrieval setups failed on up to 81% of questions (FinanceBench, 2023). Independent newsroom audits find AI search tools mis-cite or misreport news a large share of the time: >60% wrong citations across 8 engines (Tow Center, Mar 2025), and 45% of answers with a significant issue (EBU/BBC, Oct 2025). I found no rigorous, independent audit of stock-price or quote accuracy specifically.

### Cited Findings
- **FinanceBench** (Patronus AI et al.) [PRE, arXiv 2311.11944, Nov 2023]. 150 open-source cases and 2,400 human-reviewed responses. GPT-4-Turbo with a shared vector store got **19% correct with 68% refusals, so 81% wrong or declined**. A per-document vector store reached about 50% correct, long-context with the full relevant filing reached 79%, and even the "oracle" evidence page reached only **85%**. Llama 2 hallucinated heavily, while GPT-4-Turbo mostly refused. About 66% of questions require numerical reasoning. — [alphaXiv](https://www.alphaxiv.org/abs/2311.11944v1); [Beancount research log, May 2026](https://beancount.io/bean-labs/research-logs/2026/05/12/financebench-open-book-financial-qa-benchmark)
- **Vals AI Finance Agent v2** [CO]. 927 expert-reviewed questions on public-company filings at entry-level analyst difficulty. Results as of Oct 18, 2026: Gemini 4 Argon **65.40%** ($4.38 per test), Gemini 3.8 Flash 61.44%, Muse Spark Open 61.34%, Claude Fable 5.1 58.88%, Claude Opus 5 58.63%. The page notes v2 has been superseded by v2.1. — [Vals AI](https://www.vals.ai/benchmarks/fabv2). A vendor summary of a June 2026 run said "no model clears 58%." — [Barebone AI](https://barebone.ai/resources/how-accurate-is-ai-stock-analysis). This probably reflects a different date or version; I did not verify it.
- **Columbia Tow Center** [JOUR, Mar 2025]. 8 AI search engines, 1,600 queries: each was given a news quote and asked for headline, publisher, date, and URL. Engines answered incorrectly **>60%** of the time. **Perplexity was best at 37% wrong; Grok-3 Search was worst at 94% wrong.** Gemini and Grok 3 gave more fabricated links than correct ones, and premium tiers were more "confidently incorrect" than free tiers. — [CJR/Tow Center](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php); [Nieman Lab](https://www.niemanlab.org/2025/03/ai-search-engines-fail-to-produce-accurate-citations-in-over-60-of-tests-according-to-new-tow-center-study/); [Fortune](https://fortune.com/2025/03/18/ai-search-engines-confidently-wrong-citing-sources-columbia-study)
- **EBU/BBC news-integrity study** [JOUR, Oct 2025]. 22 public broadcasters in 18 countries reviewed >3,000 answers from ChatGPT, Copilot, Gemini, and Perplexity. **45%** had at least one significant issue and **81%** had some issue. **31%** had serious sourcing problems, and about **20%** had major accuracy issues "including hallucinated details and outdated information." Gemini had significant issues in **76%** of answers and sourcing issues in 72%. Sourcing-issue rates were 24% for ChatGPT and 15% each for Perplexity and Copilot. — [The Register](https://www.theregister.com/2025/10/24/bbc_probe_ai_news/)
- **Investing in the Web** [MKT, affiliate/finance site; tested Nov 2024, published Apr 2025]. 100 finance questions to ChatGPT Search, graded by professionals: **65% correct, 29% incomplete or misleading, 6% wrong**. The site advises checking original sources for fast-changing data such as stock performance. — [Investing in the Web](https://investingintheweb.com/blog/chatgpt-search-fails-in-35-of-finance-related-queries/); [Entrepreneur](https://www.entrepreneur.com/business-news/dont-ask-chatgpt-for-financial-advice-study/489792)
- **Which?** UK consumer test [JOUR/consumer group]. ChatGPT scored 64%, 5th of 6 tools (ChatGPT, Gemini, Copilot, Meta AI, Perplexity, and one other). ChatGPT and Copilot missed a planted false premise, a "£25,000 ISA allowance" when the real figure is £20,000. — [Which?](https://www.which.co.uk/news/article/can-you-trust-ai-chatgpt-and-other-ai-chatbots-put-to-the-test-aetjt5e0RnPB) (details via the [Barebone AI summary](https://barebone.ai/resources/how-accurate-is-ai-stock-analysis))
- **Fabricated citations, general** [PEER, *Scientific Reports*, 2023, older]. 55% of ChatGPT-3.5 citations and 18% of GPT-4 citations were fabricated. — [Nature Sci Rep](https://www.nature.com/articles/s41598-023-41032-5)
- **Vectara hallucination leaderboard** (general summarization faithfulness; last updated Oct 16, 2026) [CO]. Hallucination rates: GPT-5.4 7.0%, GPT-5.5 9.3%, GPT-5-high 15.1%, Claude Opus 4.7 12.0%, Claude Sonnet 4.6 10.6%, Gemini 3 Pro preview 13.6%, Gemini 4 Argon 12.1%, Grok 4.1 Fast (reasoning) 19.2%, DeepSeek-V3.2 6.3%, DeepSeek-V4-Pro 8.6%. Best overall was antgroup finix_s1_32b at 1.8%. Note that newer "reasoning" models often hallucinate more on this test. — [Vectara GitHub](https://github.com/vectara/hallucination-leaderboard)

### Inferences
- The failure modes that matter for a market-data product are **staleness** (no live data without tools), **retrieval misses** (wrong document or period), **numerical-reasoning errors**, and **mis-attribution of news**. Tool access fixes the first, partly fixes the second, and does little for the last two.
- Even the best agent misses about 1 in 3 analyst-level filing questions (Oct 2026). Answers that LLMs already get right are a weak selling point; verified, structured, timestamped data is the stronger one.

### Gaps
- I found **no independent, systematic audit of stock-price or quote accuracy** (e.g., "what is NVDA trading at?") across ChatGPT, Gemini, Grok, and Perplexity. One vendor blog claimed in Dec 2025 that "ChatGPT-5" returned a balance sheet one quarter stale and other models up to six quarters stale. I could not retrieve the primary source, so it is unverified.
- I did not retrieve NewsGuard's AI False Claims Monitor figures, so no finance-specific misinformation rate is cited.
- BizFinBench results were not retrieved.

## Key Question 4: Do newer models with web search or tools do measurably better? (head-to-head with vs. without retrieval)

### Takeaway
Yes, dramatically for **current-data lookups**. In FinSearchComp (ICLR 2026), models without search scored **0%** on time-sensitive financial data. Search added an average of 41 points there, 29 points on simple historical lookups, but only 8 points on complex investigations. Even the best search-enabled product (Grok 4 web, 68.9%) trailed human experts (75.0%) on the global subset. Better retrieval does **not** translate into trading alpha. NBER chatbot portfolios browsed about 16 websites per query and still produced no risk-adjusted outperformance. In advice tasks, web search made recommendations more uniform.

### Cited Findings
- **FinSearchComp** (ByteDance Seed with Columbia Business School) [PEER, ICLR 2026 poster; arXiv 2509.13160, Sep 16, 2025]. 635 expert-annotated questions (70 financial experts) covering global and Greater China markets, with 3 tasks: T1 time-sensitive data fetching, T2 simple historical lookup, T3 complex historical investigation. 21 models/products were tested. — [arXiv abs](https://arxiv.org/abs/2509.13160); [ICLR](https://iclr.cc/virtual/2026/poster/10011221)
  - "Models without search uniformly score 0 on T1." Average gains from search were **+40.8 pts (T1), +29.0 (T2), +8.1 (T3)**. — [arXiv HTML](https://arxiv.org/html/2509.13160)
  - Like-for-like test of Gemini 2.5 Pro via API: **with Google Search, 34.8% overall** (global average 38.2, T1-global 42.5). **Without search, 10.0% overall** (global average 11.9, T1 0.0). — [arXiv HTML](https://arxiv.org/html/2509.13160). Caveat: the scraped table headers were garbled. The column mapping was inferred and checked against the paper's stated Grok 4 = 68.9 and human = 75.0.
  - Global subset: **human experts 75.0**; Grok 4 (web) 68.9; GPT-5-Thinking (web) 63.9; Gemini 2.5 Pro (web) 42.6; DouBao (web) 39.1; Kimi k2 (web) 29.5; DeepSeek-R1 (web) 17.2. On complex historical questions (T3-global), the best model scored 51.2 vs 51.4 for humans. Greater China subset: human 88.3, best model DouBao (web) 54.2. — [arXiv HTML](https://arxiv.org/html/2509.13160)
  - Country of origin of both model and tool significantly affected performance. — [arXiv abs](https://arxiv.org/abs/2509.13160)
- **FinanceBench retrieval configuration** [PRE, 2023]. Correctness ranged from 19% (shared vector store) to ~50% (per-document store) to 79% (long context) to 85% (oracle page). Retrieval quality was the dominant variable, and a ~15% error rate remained even with perfect evidence. — [Beancount](https://beancount.io/bean-labs/research-logs/2026/05/12/financebench-open-book-financial-qa-benchmark)
- **StockBench news and fundamentals ablation** [PRE, 2025]. Kimi-K2's return fell from 1.9% with full inputs to 1.4% without news and 0.6% without news or fundamentals. GPT-OSS-120B fell from −1.2% (full) to −3.4% (no news or fundamentals). Richer information inputs helped modestly. — [arXiv 2510.02209](https://arxiv.org/html/2510.02209v1)
- **Search-enabled tools still mis-cite news.** In the Tow Center test, all 8 engines had live search and still erred >60% of the time (Perplexity 37%, Grok-3 Search 94%). — [CJR](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php)
- **Browsing does not create alpha.** NBER chatbot portfolios visited about 16 websites per query yet showed no characteristic-adjusted abnormal returns. — [Science of Money / NBER w35153](https://www.scienceofmoney.org/when-chatbots-play-stock-picker-what-ai-actually-recommends-for-your-portfolio-559/)
- **Search homogenizes advice.** Web search improved diversification but made allocations more uniform across clients. — [arXiv 2604.23837](https://arxiv.org/pdf/2604.23837)
- **Newer models score higher on grounded analyst tasks, but the ceiling is low.** Vals Finance Agent v2 top score was 65.4% (Gemini 4 Argon, Oct 2026). — [Vals AI](https://www.vals.ai/benchmarks/fabv2)
- **Newer is not uniformly better at trading.** In Alpha Arena S1, GPT-5 finished last. In StockBench, GPT-5 (+0.3%) trailed Kimi-K2 and Qwen3, and reasoning models did not reliably beat instruction-tuned ones. — [iWeaver](https://www.iweaver.ai/blog/alpha-arena-ai-trading-season-1-results/); [arXiv 2510.02209](https://arxiv.org/html/2510.02209v1)

### Inferences
- The gap a data vendor can close is largest and most measurable on **time-sensitive and structured lookups**: going from 0% to about 40–87% on T1-type questions with good retrieval. It is smallest on multi-step investigation, where reasoning, not data, is the bottleneck.
- A natural evaluation for an MCP product is FinSearchComp-style: the same model with vs. without the connector, on time-sensitive questions plus questions about sentiment and track records.
- Retrieval quality, meaning which source and how fresh, drives accuracy more than model version. Generic web search pulls heavily from corporate sites and mainstream news (NBER: about two-thirds of visited sites were corporate), so retail sentiment and trader track records are a data category LLMs currently barely see.

### Gaps
- I found no published head-to-head that adds **sentiment or social data** to an LLM and measures forecasting or trading lift on a post-cutoff period.
- Alpha Arena Season 2, which reportedly adds web search, had no results I could find by Oct 2026. So there is no live trading result with vs. without search.
- FinSearchComp's full results for proprietary consumer products in non-search mode (e.g., ChatGPT without browsing) were not separately reported in what I retrieved.
