# StockTwits official MCP server / AI integration check (as of 2026-10-21)

**Bottom line:** The first note is correct. StockTwits runs an official, live, hosted MCP server at `https://mcp.stocktwits.com/mcp`, marketed at ai.stocktwits.com. The second note ("no official server, only an unhealthy third-party connector") most likely came from checking MCP registries. Those registries list only Pipeworx's third-party `io.github.pipeworx-io/stocktwits` server. Glama marks it "Unhealthy", and PulseMCP confusingly labels it "official". The StockTwits-run server is not listed in the official MCP registry.

## Do ai.stocktwits.com and mcp.stocktwits.com exist, are they run by StockTwits, and what do they offer?

### Takeaway
Both are live and operated by StockTwits. ai.stocktwits.com markets "Stocktwits MCP", a remote MCP server at mcp.stocktwits.com/mcp. You sign in with a StockTwits account through standard MCP OAuth. It works with Claude, ChatGPT, Codex, Cursor, OpenClaw, Hermes and any other MCP client. It serves trending tickers, per-ticker bull/bear sentiment, message volume, sentiment shifts and individual messages. The page states no pricing and no launch date.

### Cited Findings
- **Operator:** the page footer reads "© 2026 Stocktwits, Inc. All rights reserved." The product is "Stocktwits MCP", tagline "Stocktwits intelligence, built for AI". The page says that with this "new MCP, everyone can use AI to tap into what investors are watching, saying, and feeling." — [ai.stocktwits.com](https://ai.stocktwits.com/)
- **Server:** listed as "Remote MCP server · Platform agnostic", URL `https://mcp.stocktwits.com/mcp`. Setup: paste the URL, then authorize with your StockTwits account. "No client ID, secret, or custom credentials needed." — [ai.stocktwits.com](https://ai.stocktwits.com/)
- **Supported clients:**
  - Claude, through a connector in Claude's directory. The page links to `claude.ai/directory/connectors/stocktwits`.
  - ChatGPT, with a one-click add. The page links to `chatgpt.com/plugins/plugin_asdk_app_6a427a19b1f481919c5db13838af00c2`.
  - Codex, Cursor, OpenClaw and Hermes (Nous).
  - Any other MCP-compatible agent, by manual setup.
  - Source: [ai.stocktwits.com](https://ai.stocktwits.com/) (page text plus link targets in its HTML)
- **Data shown:**
  - "Trending on Stocktwits" board: price, change, market status, sparklines, watchers and volume.
  - "Symbol Pulse": per-ticker watchers, message volume, price action and bull/bear sentiment.
  - Example prompts: sentiment shifts over a month, message volume over two weeks, whether current chatter is a spike, "Quote the best bull and the best bear", and sweeps of a watchlist for unusual conversation.
  - The page publishes no list of tool names.
  - Source: [ai.stocktwits.com](https://ai.stocktwits.com/)
- **Pricing and launch date:** the page gives neither. It calls the product a "new MCP" and has a 2026 copyright. — [ai.stocktwits.com](https://ai.stocktwits.com/)
- **Disclaimer:** "Stocktwits provides social, sentiment, and market data for informational purposes only." The page also says the content is not investment advice. — [ai.stocktwits.com](https://ai.stocktwits.com/)
- **Live endpoint probe** (curl, 2026-10-21):
  - `https://mcp.stocktwits.com/` returns HTTP 404, which is expected at the root.
  - `https://mcp.stocktwits.com/mcp` returns HTTP 401 with `WWW-Authenticate: Bearer error="invalid_request", error_description="Bearer token required", resource_metadata="https://mcp.stocktwits.com/.well-known/oauth-protected-resource/mcp"`.
  - The server sits behind Cloudflare and sets cookies scoped to `Domain=stocktwits.com`.
  - Source: [mcp.stocktwits.com/mcp](https://mcp.stocktwits.com/mcp)
- **OAuth protected-resource metadata:** `{"resource":"https://mcp.stocktwits.com/mcp","authorization_servers":["https://mcp.stocktwits.com"],"scopes_supported":["read","watch_lists"]}` — [oauth-protected-resource](https://mcp.stocktwits.com/.well-known/oauth-protected-resource)
- **OAuth authorization-server metadata:**
  - Dynamic client registration at `/register`.
  - Endpoints at `/authorize` and `/token`.
  - Grant types `authorization_code` and `refresh_token`.
  - PKCE `S256`.
  - `token_endpoint_auth_methods_supported: ["none"]`.
  - Source: [oauth-authorization-server](https://mcp.stocktwits.com/.well-known/oauth-authorization-server)

### Inferences
- This is the standard MCP OAuth 2.1 flow with dynamic client registration. That explains the "no client ID or secret needed" claim. The `watch_lists` scope suggests the server can read the signed-in user's StockTwits watchlists, which fits the "watchlist sweep" example prompts.
- The live 401/OAuth responses on a stocktwits.com subdomain, plus the Stocktwits, Inc. copyright, make operation by StockTwits very likely. This does not rest only on the marketing page.

### Gaps
- The actual tool names and schemas could not be listed, because `tools/list` needs an authenticated StockTwits session. I did not sign in.
- Pricing, free versus premium gating, and rate limits are not stated anywhere I found.
- Launch date unknown.

## Is there a press release, blog post, X post, or registry/directory listing confirming it?

### Takeaway
I found no press release, blog post or X post. The official MCP registry, Glama and PulseMCP list only Pipeworx's third-party server. The StockTwits page links to Claude and ChatGPT directory entries, but I could not open them from this environment.

### Cited Findings
- Searches for a StockTwits MCP launch or announcement found no press release or dated announcement. The only first-party source was ai.stocktwits.com. A FinTech Studios "MCP connector for Claude & ChatGPT" press release is about a different company. — [natlawreview.com (FinTech Studios, unrelated)](https://natlawreview.com/press-releases/fintech-studios-launches-mcp-connector-claude-chatgpt-brings-market)
- **Official MCP registry:** a search for "stocktwits" returns only `io.github.pipeworx-io/stocktwits` ("StockTwits MCP (keyless public read)"). Versions run from 0.1.0, published 2026-06-26, to 0.1.3, published 2026-10-07. Its remote is `gateway.pipeworx.io/stocktwits/mcp`. There is no stocktwits.com-namespaced entry. — [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io/v0/servers?search=stocktwits)
- **Glama:** the Pipeworx StockTwits connector shows status **"Unhealthy"**, with 28.8% uptime over 65 days and the last two health checks failed. It exposes 49 tools, many unrelated to StockTwits (Polymarket, Kalshi, memory). — [Glama](https://glama.ai/mcp/connectors/io.github.pipeworx-io/stocktwits)
  - This matches the "unofficial third-party connector listed as unhealthy" in the second note.
- **PulseMCP:** the "StockTwits" listing labels the server "official", but its provider and maintainer are Pipeworx (pipeworx-io). It lists a release date of May 24, 2026, needs no authentication, and has a free tier. — [PulseMCP](https://www.pulsemcp.com/servers/stocktwits)
  - This mislabeling is a likely source of confusion.
- **Claude directory:**
  - ai.stocktwits.com links to `claude.ai/directory/connectors/stocktwits`. Fetching it returned a Cloudflare challenge (403), so I could not verify it.
  - The public URL `claude.com/connectors/stocktwits` redirects (308) to `claude.com/marketplace/connectors/stocktwits`, which returned 404.
  - A web search of claude.com connector pages found no StockTwits mention.
  - Sources: [ai.stocktwits.com](https://ai.stocktwits.com/); [claude.com/connectors/stocktwits](https://claude.com/connectors/stocktwits)
- **ChatGPT directory:** ai.stocktwits.com links to a ChatGPT app ID (`plugin_asdk_app_6a427a19…`). The page returned 403 from this environment, so I could not verify it. — [ai.stocktwits.com](https://ai.stocktwits.com/)
- **GitHub repo `stocktwits/stocktwits-mcp`:** this is a separate, local (npx) server.
  - Repo tagline: "MCP server for StockTwits — stock prices, social sentiment, trending symbols, and user profiles".
  - It has 9 tools, needs no API key, and "All data comes from public, unauthenticated StockTwits endpoints" (200 requests per hour per IP).
  - It has 4 stars and 4 commits, and nowhere describes itself as official.
  - Source: [github.com/stocktwits/stocktwits-mcp](https://github.com/stocktwits/stocktwits-mcp)

### Inferences
- The official server is distributed through StockTwits' own landing page and, per that page, the Claude and ChatGPT app directories. It is not in the open MCP registries, which explains why a registry-first search missed it.
- The `stocktwits/stocktwits-mcp` GitHub repo is a different product from the hosted mcp.stocktwits.com server. It is unauthenticated and local, with different tools. Do not treat it as the official integration.

### Gaps
- Whether the Claude and ChatGPT directory listings are actually live and approved could not be confirmed. Both directories block unauthenticated fetches.
- Whether the `stocktwits` GitHub org belongs to StockTwits, Inc. could not be verified, because GitHub API access to the org was blocked in this session.
- No dated announcement exists, so the launch date cannot be pinned down. The only signal is "new MCP" in 2026.

## Does it expose per-user track-record / "who's been right" data?

### Takeaway
No evidence of it. The official server is marketed only on aggregate symbol data (trending, sentiment, volume, watchers, price) and on message content. Its OAuth scopes are just `read` and `watch_lists`. No source mentions accuracy, track records or leaderboards.

### Cited Findings
- ai.stocktwits.com does not mention per-user accuracy, track records or "who's been right" data. The features it describes are symbol- and watchlist-level, plus quoting individual bull and bear messages. — [ai.stocktwits.com](https://ai.stocktwits.com/)
- The only OAuth scopes advertised are `read` and `watch_lists`. — [oauth-protected-resource](https://mcp.stocktwits.com/.well-known/oauth-protected-resource)
- The separate GitHub server has `get_user_profile`, `get_user_messages` and `get_user_sentiment`.
  - The profile returns followers, following, posts, watchlist count and like count.
  - `get_user_sentiment` only counts a user's recent bullish and bearish tags per symbol.
  - Nothing checks whether calls were correct.
  - Source: [github.com/stocktwits/stocktwits-mcp](https://github.com/stocktwits/stocktwits-mcp)
- PulseMCP's Pipeworx listing mentions no accuracy or track-record data. — [PulseMCP](https://www.pulsemcp.com/servers/stocktwits)

### Inferences
- As of October 2026, scoring "who's been right" (scored per-user prediction accuracy) appears to be white space. Neither StockTwits' official MCP nor the third-party servers offer it publicly. At most they offer per-user sentiment tagging and social stats.

### Gaps
- Without an authenticated `tools/list` call, I cannot rule out that the official server has an unadvertised user-level tool. Nothing public suggests one exists.
