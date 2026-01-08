#!/usr/bin/env python3
"""Re-run validation on the 'Idea Validation Reports' idea with V2 skeptical scoring."""

from validate import run_idea_validation, print_validation_result

# THE IDEA (with skeptical scoring this time)
idea = "Startup Idea Validation Reports - async research service"
target = "Indie hackers on r/SaaS, r/indiehackers, r/startups thinking about building something"
price = "$49 per report OR $29/mo subscription (1 idea/month)"

# V2 SKEPTICAL SCORES - Being honest this time
scores = {
    # HIGH IMPACT (60%)
    "demand_signals": 6.0,       # People want FREE feedback, not paid. Be honest.
    "distribution": 7.0,         # You're on the subreddits, but haven't sold to them before
    "free_alternatives": 7.0,    # ChatGPT, Reddit comments, friends = strong free options (HIGH = BAD)
    "customer_asks": 5.0,        # People ask for feedback, rarely PAY for it
    "founder_market_fit": 8.0,   # Async, research-based, no calls = good fit

    # MEDIUM IMPACT (30%)
    "competition": 6.0,          # Some paid services exist, validates market but crowded
    "market_gap": 5.0,           # Gap between free garbage and expensive agencies, but small
    "unit_economics": 5.0,       # $49 / 2-3 hours = $16-25/hr. Not great.
    "churn_risk": 4.0,           # One-time purchase mostly, low repeat
    "sales_cycle": 8.0,          # Self-serve, instant purchase

    # LOWER IMPACT (10%)
    "icp_validation": 7.0,       # Can find them easily
    "buy_vs_build": 6.0,         # People DIY with ChatGPT, might not pay
    "price_sensitivity": 6.0,    # $49 is reasonable but cheap market
    "tam": 5.0,                  # Limited by your time if manual
    "payment_friction": 8.0,     # Credit card, easy
}

print("\n" + "="*70)
print("V2 SKEPTICAL VALIDATION: Startup Idea Validation Reports")
print("="*70)

print("""
KEY CHANGES IN V2:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Weights now sum to exactly 100% (was 123% - inflating scores)
2. Added "Free Alternatives" category (ChatGPT/Reddit compete with you)
3. Added "Unit Economics" category ($49 ÷ hours = $/hr)
4. Execution Risk Penalty based on YOUR track record (-15% to -50%)
5. Founder-Market Fit weighted higher (13% vs 8%)
6. Distribution weighted higher (15% vs 12%)

SKEPTICAL SCORING ADJUSTMENTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Demand Signals: 9 → 6 (people want FREE feedback, not paid)
• Customer Asks: 9 → 5 (asking ≠ paying)
• Free Alternatives: NEW at 7 (ChatGPT is strong competition)
• Unit Economics: NEW at 5 ($49/3hr = $16/hr is bad)
• Churn Risk: 7 → 4 (one-time purchase, low LTV)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

result = run_idea_validation(idea, target, price, scores)
print_validation_result(result)

print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HONEST ASSESSMENT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The V1 validator was too optimistic. Here's the reality:

PROBLEMS WITH THIS IDEA:
1. Free alternatives are strong (ChatGPT, Reddit, friends)
2. Unit economics are bad ($16-25/hr is a job, not a business)
3. One-time purchase = constant customer acquisition
4. "Asking for feedback" ≠ "willing to pay for feedback"

WHAT WOULD MAKE THIS A BUILD NOW?
1. Higher price point ($149-299) with clear 10x value over free
2. Recurring model that actually works (cohort-based?)
3. Automation to improve unit economics
4. Proof that people PAY (not just "cool idea")

NEXT STEP:
Before doing ANYTHING, answer this:
→ Can you find 5 people who ALREADY PAID for idea validation?
→ Not "would pay" - actually paid. For anything similar.

If no, this is a STOP.
If yes, talk to them about what they paid for and why.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
