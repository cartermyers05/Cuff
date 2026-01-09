#!/usr/bin/env python3
"""
Med Spa Ideas Validation - Using Ralph Framework + V2 Validator

KEY ADVANTAGE: Direct access to $2M/year med spa operator (mom)
- Can validate instantly
- Has industry connections
- Can intro to other owners
- THIS IS YOUR UNFAIR ADVANTAGE
"""

from validate import run_idea_validation, print_validation_result, Verdict

# Update distribution context for med spa
# You have DIRECT ACCESS here, unlike contractor/home services

ideas = [
    {
        "idea": "Package Breakage Recovery Tool - Auto-remind clients before unused sessions expire",
        "target": "Med spa owners losing money on expired packages",
        "price": "$199/mo OR 15% of recovered revenue",
        "scores": {
            # HIGH IMPACT (60%)
            "demand_signals": 8.0,       # Owners HATE losing package revenue
            "distribution": 8.0,         # MOM CAN INTRO YOU TO OTHER OWNERS
            "free_alternatives": 4.0,    # Manual tracking in spreadsheets (painful)
            "customer_asks": 8.0,        # "I wish I knew before packages expired"
            "founder_market_fit": 8.0,   # No-code, async, self-serve possible

            # MEDIUM IMPACT (30%)
            "competition": 6.0,          # Boulevard/Zenoti have some features, not focused
            "market_gap": 7.0,           # Standalone recovery tool vs bloated suite
            "unit_economics": 8.0,       # $199/mo or % of recovered = great margins
            "churn_risk": 7.0,           # Monthly recurring, ongoing need
            "sales_cycle": 7.0,          # Can demo to mom, get referrals

            # LOWER IMPACT (10%)
            "icp_validation": 9.0,       # Mom IS the ICP, knows dozens more
            "buy_vs_build": 8.0,         # Currently losing money, manual tracking fails
            "price_sensitivity": 7.0,    # $199 is nothing vs thousands in lost revenue
            "tam": 6.0,                  # ~30K med spas in US
            "payment_friction": 7.0,     # Business expense, credit card
        },
        "ralph_score": {
            "revenue_leak": 10,
            "med_spa_specific": 8,
            "moat_potential": 7,
            "instant_value": 8,
            "outcome_pricing": 9,
            "mission_critical": 7,
        },
        "validation_question": "How much revenue did you lose last year from expired packages? What do you do to prevent it?",
    },
    {
        "idea": "No-Show Recovery System - Auto-text/call when client misses, offer rebooking + deposit",
        "target": "Med spas losing $200-500 per no-show",
        "price": "$149/mo OR $20 per recovered appointment",
        "scores": {
            # HIGH IMPACT (60%)
            "demand_signals": 9.0,       # No-shows are UNIVERSAL pain
            "distribution": 8.0,         # Mom connection
            "free_alternatives": 5.0,    # Manual texting, some PMS have basic reminders
            "customer_asks": 9.0,        # Every owner complains about no-shows
            "founder_market_fit": 8.0,   # Automated, async, no calls needed

            # MEDIUM IMPACT (30%)
            "competition": 5.0,          # Some tools exist but not med-spa focused
            "market_gap": 6.0,           # Recovery vs just reminders
            "unit_economics": 8.0,       # $149/mo or per-recovery = solid
            "churn_risk": 8.0,           # Ongoing monthly need
            "sales_cycle": 7.0,          # Demo to mom, referrals

            # LOWER IMPACT (10%)
            "icp_validation": 9.0,       # Mom
            "buy_vs_build": 8.0,         # Currently losing money
            "price_sensitivity": 8.0,    # Pays for itself in 1 recovered appointment
            "tam": 6.0,                  # 30K med spas
            "payment_friction": 7.0,     # Business expense
        },
        "ralph_score": {
            "revenue_leak": 10,
            "med_spa_specific": 7,
            "moat_potential": 6,
            "instant_value": 9,
            "outcome_pricing": 10,
            "mission_critical": 8,
        },
        "validation_question": "How many no-shows do you get per week? What's your current recovery process?",
    },
    {
        "idea": "Rebooking Gap Automator - Detects clients who haven't scheduled next appointment, auto-outreach",
        "target": "Med spas losing clients who 'forget' to rebook",
        "price": "$179/mo",
        "scores": {
            # HIGH IMPACT (60%)
            "demand_signals": 7.0,       # Less acute than no-shows but real
            "distribution": 8.0,         # Mom connection
            "free_alternatives": 5.0,    # Manual review of client list
            "customer_asks": 7.0,        # Owners know they lose clients this way
            "founder_market_fit": 8.0,   # Automated, async

            # MEDIUM IMPACT (30%)
            "competition": 5.0,          # Some CRMs have this, not focused
            "market_gap": 6.0,           # Proactive vs reactive
            "unit_economics": 7.0,       # $179/mo, good margins
            "churn_risk": 7.0,           # Monthly need
            "sales_cycle": 7.0,          # Mom demo

            # LOWER IMPACT (10%)
            "icp_validation": 9.0,       # Mom
            "buy_vs_build": 7.0,         # Currently manual or ignored
            "price_sensitivity": 7.0,    # One recovered client pays for months
            "tam": 6.0,                  # 30K med spas
            "payment_friction": 7.0,     # Business expense
        },
        "ralph_score": {
            "revenue_leak": 8,
            "med_spa_specific": 7,
            "moat_potential": 6,
            "instant_value": 7,
            "outcome_pricing": 7,
            "mission_critical": 6,
        },
        "validation_question": "What percentage of clients don't schedule their next appointment before leaving? What do you do about it?",
    },
    {
        "idea": "Lead Response Speed Tool - Auto-respond to inquiries in <5 min, qualify, book consultation",
        "target": "Med spas losing leads to slow response",
        "price": "$249/mo OR $25 per booked consultation",
        "scores": {
            # HIGH IMPACT (60%)
            "demand_signals": 8.0,       # Speed to lead is proven crucial
            "distribution": 8.0,         # Mom connection
            "free_alternatives": 4.0,    # Manual response, often slow
            "customer_asks": 8.0,        # Owners know they lose leads
            "founder_market_fit": 7.0,   # Needs some setup but automated after

            # MEDIUM IMPACT (30%)
            "competition": 5.0,          # Generic lead response tools exist
            "market_gap": 7.0,           # Med-spa specific qualification
            "unit_economics": 8.0,       # $249/mo or per-booking = solid
            "churn_risk": 8.0,           # Monthly need
            "sales_cycle": 6.0,          # Slightly more complex to explain

            # LOWER IMPACT (10%)
            "icp_validation": 9.0,       # Mom
            "buy_vs_build": 7.0,         # Currently slow manual response
            "price_sensitivity": 8.0,    # One consultation = $200+ revenue
            "tam": 6.0,                  # 30K med spas
            "payment_friction": 7.0,     # Business expense
        },
        "ralph_score": {
            "revenue_leak": 9,
            "med_spa_specific": 7,
            "moat_potential": 6,
            "instant_value": 9,
            "outcome_pricing": 9,
            "mission_critical": 7,
        },
        "validation_question": "What's your average response time to new inquiries? How many leads do you think you lose to slow response?",
    },
    {
        "idea": "Treatment Plan Adherence Tracker - Remind clients to complete their treatment series",
        "target": "Med spas with clients who drop off mid-treatment plan",
        "price": "$129/mo",
        "scores": {
            # HIGH IMPACT (60%)
            "demand_signals": 6.0,       # Real but less acute than no-shows
            "distribution": 8.0,         # Mom connection
            "free_alternatives": 5.0,    # Manual tracking
            "customer_asks": 6.0,        # Less top-of-mind
            "founder_market_fit": 8.0,   # Automated, async

            # MEDIUM IMPACT (30%)
            "competition": 5.0,          # Some PMS have this
            "market_gap": 5.0,           # Smaller gap
            "unit_economics": 6.0,       # $129/mo, lower price point
            "churn_risk": 6.0,           # Monthly but less sticky
            "sales_cycle": 7.0,          # Easy to demo

            # LOWER IMPACT (10%)
            "icp_validation": 9.0,       # Mom
            "buy_vs_build": 6.0,         # Nice to have vs must have
            "price_sensitivity": 6.0,    # Value less obvious
            "tam": 6.0,                  # 30K med spas
            "payment_friction": 7.0,     # Business expense
        },
        "ralph_score": {
            "revenue_leak": 7,
            "med_spa_specific": 8,
            "moat_potential": 5,
            "instant_value": 6,
            "outcome_pricing": 6,
            "mission_critical": 5,
        },
        "validation_question": "What percentage of clients complete their full treatment plan? What happens to the ones who don't?",
    },
]

print("\n" + "="*70)
print("MED SPA IDEAS - V2 VALIDATION + RALPH FRAMEWORK")
print("="*70)

print("""
✅ DISTRIBUTION ADVANTAGE:
- Direct access to $2M/year med spa operator (mom)
- She can validate instantly
- She can intro you to other owners
- THIS CHANGES EVERYTHING vs contractor/home services

Scoring with distribution = 8/10 (vs 2/10 for contractors)
""")

results = []
for i, idea_data in enumerate(ideas, 1):
    print(f"\n{'='*70}")
    print(f"IDEA {i}: {idea_data['idea'][:55]}...")
    print(f"{'='*70}")

    result = run_idea_validation(
        idea_data["idea"],
        idea_data["target"],
        idea_data["price"],
        idea_data["scores"]
    )
    results.append((idea_data, result))

    # Calculate Ralph score
    ralph_total = sum(idea_data["ralph_score"].values())

    verdict_symbol = {
        Verdict.BUILD_NOW: "✅",
        Verdict.VALIDATE_FIRST: "⚠️",
        Verdict.STOP: "❌"
    }

    print(f"\n  {verdict_symbol[result.verdict]} {result.verdict.value}")
    print(f"  V2 Score: Raw {result.final_score:.1f} → Adjusted {result.adjusted_score:.1f}")
    print(f"  Ralph Score: {ralph_total}/60")
    print(f"\n  📋 Validation Question for Mom:")
    print(f"     \"{idea_data['validation_question']}\"")

# Summary
print("\n" + "="*70)
print("SUMMARY - RANKED BY ADJUSTED SCORE")
print("="*70)

# Sort by adjusted score
sorted_results = sorted(results, key=lambda x: x[1].adjusted_score, reverse=True)

print("\n| Rank | Idea | Adjusted | Verdict | Ralph |")
print("|------|------|----------|---------|-------|")
for i, (idea_data, result) in enumerate(sorted_results, 1):
    short_name = idea_data['idea'].split(' - ')[0][:25]
    ralph_total = sum(idea_data["ralph_score"].values())
    verdict_short = "BUILD" if result.verdict == Verdict.BUILD_NOW else "VALIDATE" if result.verdict == Verdict.VALIDATE_FIRST else "STOP"
    print(f"| {i} | {short_name:25} | {result.adjusted_score:.1f}/10 | {verdict_short:8} | {ralph_total}/60 |")

# Find best candidate
best_idea, best_result = sorted_results[0]

print(f"""

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 TOP CANDIDATE: {best_idea['idea'].split(' - ')[0]}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Adjusted Score: {best_result.adjusted_score:.1f}/10
Verdict: {best_result.verdict.value}
Price: {best_idea['price']}

RALPH FRAMEWORK BREAKDOWN:
""")

for key, val in best_idea["ralph_score"].items():
    bar = "█" * val + "░" * (10 - val)
    print(f"  {key.replace('_', ' ').title():.<25} {bar} {val}/10")

print(f"""
VALIDATION QUESTION FOR MOM:
"{best_idea['validation_question']}"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NEXT STEPS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ASK MOM THE VALIDATION QUESTIONS (today):
""")

for idea_data, _ in sorted_results[:3]:
    print(f"   • \"{idea_data['validation_question']}\"")

print("""
2. BASED ON HER ANSWERS:
   - Which problem makes her say "Oh my god, yes"?
   - Can she name 3+ other owners with the same pain?
   - What would she pay to solve it?

3. IF VALIDATED:
   - Build MVP in Lovable (2 weeks)
   - Mom is first customer
   - She intros you to other owners
   - Aim: 5 paying customers in 4 weeks

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHY MED SPA > CONTRACTOR/HOME SERVICES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Factor | Contractor | Med Spa |
|--------|------------|---------|
| Distribution | 2/10 (no access) | 8/10 (mom) |
| Validation | Can't test | Instant via mom |
| Referrals | None | Mom's network |
| Industry knowledge | None | Direct access |
| First customer | ??? | Mom |

Your unfair advantage is the med spa connection.
USE IT.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
