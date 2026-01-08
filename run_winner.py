#!/usr/bin/env python3
"""Run validation on the BUILD NOW idea."""

from validate import run_idea_validation, print_validation_result

# THE WINNING IDEA
idea = "Startup Idea Validation Reports - async research service"
target = "Indie hackers on r/SaaS, r/indiehackers, r/startups thinking about building something"
price = "$49 per report OR $29/mo subscription (1 idea/month)"

# Scores with reasoning
scores = {
    "demand_signals": 9.0,       # "Should I build this?" asked daily on Reddit
    "competition": 7.0,          # Some exist but most are expensive agencies or garbage
    "icp_validation": 9.0,       # Target customers ARE on Reddit, findable in 5 min
    "market_gap": 8.0,           # Quality + affordable + fast + indie-focused
    "customer_asks": 9.0,        # People literally pay for idea validation
    "churn_risk": 7.0,           # Subscription model for serial ideators
    "failed_alternatives": 7.0,  # Some work, some don't - execution matters
    "buy_vs_build": 8.0,         # People spend weeks doing bad research themselves
    "price_sensitivity": 8.0,    # $49 to save weeks of research = easy yes
    "sales_cycle": 9.0,          # Self-serve, instant purchase, no calls
    "tam": 6.0,                  # Hundreds of thousands of indie hackers globally
    "trend_backing": 8.0,        # More people starting side projects than ever
    "integration_complexity": 9.0,   # No tech needed, just research + delivery
    "payment_friction": 9.0,     # Credit card, Gumroad, instant
    "distribution": 9.0,         # YOU ARE ON THESE SUBREDDITS DAILY
    "unfair_advantage": 8.0,     # Research + analysis is YOUR CORE STRENGTH
    "founder_market_fit": 9.0,   # Async, no calls, pure research - PERFECT FIT
}

print("\n" + "="*70)
print("IDEA BRAINSTORM → VALIDATION RESULTS")
print("="*70)

print("""
IDEAS TESTED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ IDEA 1: Reddit Keyword Monitor for SaaS founders
   Score: 7.6 → VALIDATE FIRST
   Problem: Competition (F5Bot, Syften, GummySearch), unfair advantage weak

❌ IDEA 2: Landing Page Roast Service
   Score: 7.3 → VALIDATE FIRST
   Problem: One-time purchase = no MRR, you'll quit when income is lumpy

❌ IDEA 3: Competitor Intel Reports (automated)
   Score: 6.7 → VALIDATE FIRST
   Problem: "Nice to have" not "must have", weaker demand signals

❌ IDEA 4: Notion Templates for Indie Hackers
   Score: N/A → STOP (saturated market, no differentiation)

✅ IDEA 5: Startup Idea Validation Reports ← WINNER
   Score: 8.2 → BUILD NOW
   Why it wins: Perfect founder-market fit + you're IN the distribution channel

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

result = run_idea_validation(idea, target, price, scores)
print_validation_result(result)

print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHY THIS IDEA WINS FOR *YOU* SPECIFICALLY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. DISTRIBUTION MATCH
   You have access to r/SaaS, r/indiehackers, r/startups
   → Your customers post "should I build X?" there DAILY
   → You can find 10 potential customers in 10 minutes

2. SKILLS MATCH
   Your strengths: Research, analysis, design
   → This is LITERALLY a research business
   → No coding needed for MVP

3. PERSONALITY MATCH
   You hate: Sales calls, long cycles, enterprise
   → This is: Self-serve, async, credit card purchase
   → Zero calls required

4. UNFAIR ADVANTAGE
   You already built a validation framework (this tool!)
   → Productize your own process
   → You understand the problem firsthand

5. ANTI-QUIT DESIGN
   Deliver manually first = revenue from day 1
   → No "build for 6 weeks then quit" pattern
   → Get paid before you build anything

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT TO DO RIGHT NOW:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TODAY:
  1. Go to r/SaaS or r/indiehackers
  2. Find 3 "should I build this?" posts from the last week
  3. Comment offering a FREE validation report
  4. Deliver manually using your framework

THIS WEEK:
  1. Get 3 testimonials from free reports
  2. Set up Gumroad payment link ($49)
  3. Post: "I'll validate your startup idea for $49 - here's what you get"

SUCCESS = First paying customer within 7 days

If you can't get 1 paying customer in 7 days, the idea is a STOP.
If you can, scale to 10 customers before automating ANYTHING.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
