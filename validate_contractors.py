#!/usr/bin/env python3
"""
Validate contractor/home services startup ideas through V2 skeptical validator.
"""

from validate import run_idea_validation, print_validation_result, Verdict

ideas = [
    {
        "idea": "Contractor Quote Analyzer - Upload quotes, AI tells you if price is fair",
        "target": "Homeowners getting work done (kitchen remodel, roof, etc.)",
        "price": "$19 per analysis OR $9/mo subscription",
        "scores": {
            # HIGH IMPACT (60%)
            "demand_signals": 7.0,       # People DO complain about contractor pricing
            "distribution": 2.0,         # PROBLEM: You're on r/SaaS, not homeowner forums
            "free_alternatives": 6.0,    # Google, Reddit, asking friends
            "customer_asks": 6.0,        # People want this, but scattered demand
            "founder_market_fit": 5.0,   # One-time use, B2C, not your strength

            # MEDIUM IMPACT (30%)
            "competition": 5.0,          # Some exist but not great
            "market_gap": 6.0,           # Gap exists
            "unit_economics": 4.0,       # $19 per analysis, low volume potential
            "churn_risk": 3.0,           # One-time use per project (every 5-10 years)
            "sales_cycle": 7.0,          # Self-serve possible

            # LOWER IMPACT (10%)
            "icp_validation": 4.0,       # Hard to find homeowners mid-project
            "buy_vs_build": 5.0,         # People ask on Reddit/Nextdoor currently
            "price_sensitivity": 5.0,    # $19 is cheap but is it worth it?
            "tam": 6.0,                  # Big market but fragmented
            "payment_friction": 7.0,     # Credit card easy
        },
        "notes": "Distribution killer - you can't reach homeowners through r/SaaS"
    },
    {
        "idea": "Lead Response Automation for Contractors - Auto-respond to leads in <5 min",
        "target": "Small contractors (plumbers, electricians, roofers) getting leads",
        "price": "$99/mo per contractor",
        "scores": {
            # HIGH IMPACT (60%)
            "demand_signals": 7.0,       # Lead response time is proven problem
            "distribution": 2.0,         # PROBLEM: Contractors aren't on r/SaaS
            "free_alternatives": 5.0,    # Manual texting, some CRMs have this
            "customer_asks": 6.0,        # Contractors complain about losing leads
            "founder_market_fit": 3.0,   # B2B local services = sales calls, demos

            # MEDIUM IMPACT (30%)
            "competition": 4.0,          # ServiceTitan, Jobber have this built in
            "market_gap": 5.0,           # Standalone tool vs suite
            "unit_economics": 7.0,       # $99/mo is decent
            "churn_risk": 6.0,           # Monthly need
            "sales_cycle": 3.0,          # Contractors need demos, hand-holding

            # LOWER IMPACT (10%)
            "icp_validation": 3.0,       # Hard to find small contractors
            "buy_vs_build": 6.0,         # They're losing leads to slow response
            "price_sensitivity": 6.0,    # $99 is reasonable for proven ROI
            "tam": 7.0,                  # Millions of contractors
            "payment_friction": 5.0,     # Business purchase, might need invoice
        },
        "notes": "Sales cycle mismatch - contractors need demos and hand-holding"
    },
    {
        "idea": "Home Maintenance Reminder App - Tells you when to service HVAC, clean gutters, etc.",
        "target": "Homeowners who forget maintenance tasks",
        "price": "$4.99/mo OR $39/year",
        "scores": {
            # HIGH IMPACT (60%)
            "demand_signals": 5.0,       # Nice-to-have, not burning pain
            "distribution": 2.0,         # Can't reach homeowners through r/SaaS
            "free_alternatives": 8.0,    # Calendar reminders, free apps exist
            "customer_asks": 4.0,        # Not actively searching for this
            "founder_market_fit": 4.0,   # B2C app, app store distribution

            # MEDIUM IMPACT (30%)
            "competition": 3.0,          # Many apps exist (HomeZada, Centriq)
            "market_gap": 3.0,           # Gap is small
            "unit_economics": 3.0,       # $5/mo, need massive scale
            "churn_risk": 4.0,           # People cancel "reminder" apps
            "sales_cycle": 8.0,          # Self-serve app store

            # LOWER IMPACT (10%)
            "icp_validation": 3.0,       # Generic "homeowners"
            "buy_vs_build": 3.0,         # Most just use calendar or forget
            "price_sensitivity": 3.0,    # $5 competes with free
            "tam": 8.0,                  # Huge market
            "payment_friction": 7.0,     # App store purchase
        },
        "notes": "Free alternatives too strong, low price = bad unit economics"
    },
    {
        "idea": "Contractor Vetting Research Service - Deep background check before you hire",
        "target": "Homeowners about to hire for big projects ($10K+)",
        "price": "$79 per contractor research report",
        "scores": {
            # HIGH IMPACT (60%)
            "demand_signals": 6.0,       # People worry about contractor scams
            "distribution": 2.0,         # Can't reach homeowners through r/SaaS
            "free_alternatives": 6.0,    # Google, BBB, Yelp, Angi reviews
            "customer_asks": 5.0,        # Some want this, not burning demand
            "founder_market_fit": 6.0,   # Research-based, async - fits skills

            # MEDIUM IMPACT (30%)
            "competition": 5.0,          # BBB, Angi have ratings, not deep research
            "market_gap": 6.0,           # Deep research vs surface reviews
            "unit_economics": 5.0,       # $79 / 2-3 hours = $26-40/hr
            "churn_risk": 2.0,           # One project every 5+ years
            "sales_cycle": 6.0,          # Self-serve possible

            # LOWER IMPACT (10%)
            "icp_validation": 4.0,       # Homeowners mid-hiring process
            "buy_vs_build": 5.0,         # People research themselves on Google
            "price_sensitivity": 5.0,    # $79 is small vs $20K project
            "tam": 6.0,                  # Big projects market
            "payment_friction": 7.0,     # Credit card
        },
        "notes": "Research skills fit, but distribution is killer and churn is brutal"
    },
    {
        "idea": "Invoice Dispute Resolver for Contractors - Help contractors get paid by difficult clients",
        "target": "Small contractors with unpaid invoices",
        "price": "20% of recovered amount OR $199 flat fee",
        "scores": {
            # HIGH IMPACT (60%)
            "demand_signals": 7.0,       # Contractors complain about non-payment
            "distribution": 2.0,         # Contractors aren't on r/SaaS
            "free_alternatives": 4.0,    # Lawyers expensive, collections aggressive
            "customer_asks": 7.0,        # Real pain point
            "founder_market_fit": 4.0,   # Requires negotiation skills, confrontation

            # MEDIUM IMPACT (30%)
            "competition": 6.0,          # Collections agencies, lawyers
            "market_gap": 6.0,           # Friendly resolution vs collections
            "unit_economics": 7.0,       # 20% of recovered is good margin
            "churn_risk": 3.0,           # Per-incident, not recurring
            "sales_cycle": 4.0,          # Contractors skeptical, need trust

            # LOWER IMPACT (10%)
            "icp_validation": 4.0,       # Contractors with current disputes
            "buy_vs_build": 6.0,         # Current options suck
            "price_sensitivity": 7.0,    # 20% to get paid vs 0% = easy yes
            "tam": 6.0,                  # Common problem
            "payment_friction": 5.0,     # Outcome-based, some friction
        },
        "notes": "Outcome pricing fits, but distribution mismatch and confrontation doesn't fit personality"
    },
]

print("\n" + "="*70)
print("CONTRACTOR / HOME SERVICES IDEAS - V2 SKEPTICAL VALIDATION")
print("="*70)

print("""
⚠️  DISTRIBUTION WARNING:
Your audience is r/SaaS, r/indiehackers, r/startups (tech founders).
Contractor/home services targets:
- Homeowners (B2C consumers, not on your subs)
- Contractors (local B2B, not on your subs)

This is a DISTRIBUTION MISMATCH for almost every idea in this space.
""")

results = []
for i, idea_data in enumerate(ideas, 1):
    print(f"\n{'='*70}")
    print(f"IDEA {i}: {idea_data['idea'][:50]}...")
    print(f"{'='*70}")

    result = run_idea_validation(
        idea_data["idea"],
        idea_data["target"],
        idea_data["price"],
        idea_data["scores"]
    )
    results.append((idea_data, result))

    # Print summary
    verdict_symbol = {
        Verdict.BUILD_NOW: "✅",
        Verdict.VALIDATE_FIRST: "⚠️",
        Verdict.STOP: "❌"
    }

    print(f"\n  {verdict_symbol[result.verdict]} {result.verdict.value}")
    print(f"  Raw: {result.final_score:.1f} → Adjusted: {result.adjusted_score:.1f}")
    print(f"  Distribution Score: {idea_data['scores']['distribution']}/10 ← THE KILLER")
    print(f"  Note: {idea_data['notes']}")

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70)

print("\n| Idea | Raw | Adjusted | Verdict | Distribution |")
print("|------|-----|----------|---------|--------------|")
for idea_data, result in results:
    short_name = idea_data['idea'].split(' - ')[0][:30]
    print(f"| {short_name:30} | {result.final_score:.1f} | {result.adjusted_score:.1f} | {result.verdict.value:15} | {idea_data['scores']['distribution']}/10 |")

print("""

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
THE HONEST TRUTH ABOUT CONTRACTOR/HOME SERVICES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Every idea in this space fails on DISTRIBUTION for YOU because:

1. YOUR AUDIENCE: r/SaaS, r/indiehackers, r/startups
   - Tech founders
   - Indie hackers
   - SaaS builders

2. CONTRACTOR/HOME SERVICES AUDIENCE:
   - Homeowners (B2C consumers) → Facebook, Nextdoor, local forums
   - Contractors (local B2B) → Trade associations, Facebook groups, referrals

3. THE MISMATCH:
   - You can't reach homeowners through r/SaaS
   - You can't reach contractors through r/indiehackers
   - You'd need to build entirely new distribution channels

4. ADDITIONAL PROBLEMS:
   - Contractors often need demos/calls (you hate calls)
   - Homeowner tools are often one-time use (bad churn)
   - Many ideas compete with free alternatives (Yelp, Google, BBB)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT WOULD WORK IN THIS SPACE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

If you REALLY want to do contractor/home services, you need:

1. A DISTRIBUTION HACK:
   - Partner with someone who HAS contractor audience
   - Buy a small contractor-focused newsletter/community
   - Spend 6+ months building audience in contractor spaces

2. OR PIVOT TO YOUR ACTUAL AUDIENCE:
   - "Contractor hiring guide for founders building offices"
   - "Home office setup service for remote workers"
   - Something that targets YOUR existing audience

3. THE MED SPA ANGLE (from your Ralph doc):
   - You have direct access to a $2M/year med spa operator
   - THAT is your distribution advantage
   - Med spa > contractor for YOUR situation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECOMMENDATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ SKIP contractor/home services - distribution mismatch

✅ INSTEAD: Explore med spa with your Ralph framework
   - You have DIRECT ACCESS to validator (mom)
   - You have INDUSTRY CONNECTIONS through her
   - She can introduce you to other med spa owners
   - THAT is your unfair advantage, not contractor/home services

The best startup ideas leverage YOUR specific advantages.
Contractor/home services doesn't leverage yours.
Med spa does.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
