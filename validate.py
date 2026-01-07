#!/usr/bin/env python3
"""
Startup Validator CLI - Brutally honest business idea validation tool

Usage:
    python validate.py "Your business idea" "Target customer" "Price point"

Example:
    python validate.py "AI tool that writes cold emails" "B2B SaaS founders" "$29/month"
"""

import sys
import json
import re
from dataclasses import dataclass
from typing import Optional
from enum import Enum

# ============================================================================
# HARDCODED USER CONTEXT - Your specific situation
# ============================================================================

USER_CONTEXT = {
    "distribution": {
        "twitter_followers": 200,
        "reddit_access": ["r/SaaS", "r/indiehackers", "r/startups"],
        "email_list": 0,
        "audience_score": 3,  # 1-10 scale
    },
    "track_record": {
        "projects_started": 5,
        "projects_shipped": 1,
        "projects_with_10_customers": 0,
        "average_quit_weeks": 6,
        "estimation_multiplier": 4,  # Says 2 weeks, takes 8
    },
    "personality": {
        "hates_long_sales_cycles": True,
        "prefers_self_serve": True,
        "prefers_async": True,
        "strengths": ["research", "analysis", "design", "no-code", "AI building"],
        "weaknesses": ["long-term commitment", "sales calls", "enterprise deals"],
    }
}

# ============================================================================
# SCORING CATEGORIES WITH WEIGHTS
# ============================================================================

CATEGORIES = {
    "demand_signals": {
        "name": "Demand Signals",
        "weight": 0.15,
        "description": "Reddit posts, Twitter complaints, Google Trends for the problem",
        "questions": [
            "Can you find 20+ Reddit/Twitter posts complaining about this problem?",
            "Is Google Trends showing growth for related keywords?",
            "Are people actively searching for solutions?",
        ],
    },
    "competition": {
        "name": "Competition",
        "weight": 0.10,
        "description": "Who exists, their pricing, their weaknesses",
        "questions": [
            "Who are the top 3 competitors?",
            "What do their 1-star reviews say?",
            "Is there a clear weakness you can exploit?",
        ],
        "hard_stop_threshold": 3,
    },
    "icp_validation": {
        "name": "ICP Validation",
        "weight": 0.07,
        "description": "How specific and reachable is the target customer",
        "questions": [
            "Can you describe your ideal customer in one sentence?",
            "Do you know where they hang out online?",
            "Can you find 10 of them right now?",
        ],
    },
    "market_gap": {
        "name": "Market Gap",
        "weight": 0.10,
        "description": "What's missing that you can fill",
        "questions": [
            "What specific need is unmet by current solutions?",
            "Why hasn't someone built this already?",
            "Is the gap big enough to matter?",
        ],
    },
    "customer_asks": {
        "name": "Customer Asks",
        "weight": 0.10,
        "description": "Are people asking for this specific solution",
        "questions": [
            "Are people explicitly asking for this solution?",
            "Can you find feature requests for this on competitor forums?",
            "Are there 'I wish X existed' posts?",
        ],
    },
    "churn_risk": {
        "name": "Churn Risk",
        "weight": 0.05,
        "description": "Is this a one-time need or recurring",
        "questions": [
            "Will customers need this monthly or just once?",
            "What keeps them coming back?",
            "Is there a switching cost?",
        ],
    },
    "failed_alternatives": {
        "name": "Failed Alternatives",
        "weight": 0.04,
        "description": "Did similar ideas fail? Why?",
        "questions": [
            "Have similar products failed before?",
            "Why did they fail?",
            "What would you do differently?",
        ],
    },
    "buy_vs_build": {
        "name": "Buy vs Build",
        "weight": 0.07,
        "description": "Are people trying to DIY this and failing",
        "questions": [
            "Are people cobbling together solutions with spreadsheets/Zapier?",
            "How much time are they wasting on DIY?",
            "Would they pay to save that time?",
        ],
    },
    "price_sensitivity": {
        "name": "Price Sensitivity",
        "weight": 0.05,
        "description": "Will they pay your price point",
        "questions": [
            "What are competitors charging?",
            "Does your price fit the customer's budget?",
            "Is this a 'nice to have' or 'must have' purchase?",
        ],
    },
    "sales_cycle": {
        "name": "Sales Cycle",
        "weight": 0.05,
        "description": "Same-day purchase vs months of selling",
        "questions": [
            "Can someone buy in under 10 minutes?",
            "Does it require demos or calls?",
            "Is there a committee approval process?",
        ],
    },
    "tam": {
        "name": "TAM (Total Addressable Market)",
        "weight": 0.05,
        "description": "Total addressable market size",
        "questions": [
            "How many potential customers exist?",
            "What's the realistic revenue ceiling?",
            "Is the market growing?",
        ],
    },
    "trend_backing": {
        "name": "Trend Backing",
        "weight": 0.04,
        "description": "Is this space growing or dying",
        "questions": [
            "Is this industry growing or shrinking?",
            "Are there tailwinds (AI, remote work, etc.)?",
            "Will this be more or less relevant in 2 years?",
        ],
    },
    "integration_complexity": {
        "name": "Integration Complexity",
        "weight": 0.03,
        "description": "How hard to set up",
        "questions": [
            "Can users start in under 5 minutes?",
            "Does it require IT department involvement?",
            "Are there complex integrations needed?",
        ],
    },
    "payment_friction": {
        "name": "Payment Friction",
        "weight": 0.05,
        "description": "Individual credit card vs enterprise procurement",
        "questions": [
            "Can they pay with a personal/corporate card?",
            "Is procurement/legal approval needed?",
            "Is the price under the 'expense report' threshold?",
        ],
    },
    "distribution": {
        "name": "Distribution",
        "weight": 0.12,
        "description": "Can YOU reach these customers (not theoretical)",
        "questions": [
            "Where do your target customers hang out that YOU have access to?",
            "Can you reach 100 of them this week?",
            "Do you have any existing audience overlap?",
        ],
        "hard_stop_threshold": 4,
    },
    "unfair_advantage": {
        "name": "Unfair Advantage",
        "weight": 0.08,
        "description": "Your specific edge",
        "questions": [
            "Why are YOU the right person to build this?",
            "What do you know that others don't?",
            "Do you have unique access to customers/data/skills?",
        ],
    },
    "founder_market_fit": {
        "name": "Founder-Market Fit",
        "weight": 0.08,
        "description": "Does this match your personality/skills",
        "questions": [
            "Does this match your strengths?",
            "Will you still care about this in 6 months?",
            "Is the sales motion compatible with your personality?",
        ],
    },
}

# ============================================================================
# HARD STOP RULES
# ============================================================================

HARD_STOP_RULES = [
    {
        "id": "no_specific_customers",
        "name": "Can't Name 10 Specific People",
        "description": "You must be able to name 10 specific people (not types) who have this problem",
        "question": "Can you name 10 specific people (real names, not personas) who have this problem?",
    },
    {
        "id": "validation_time",
        "name": "Validation Takes >2 Weeks",
        "description": "Core assumption must be testable in under 2 weeks",
        "question": "Can you validate the core assumption in under 2 weeks?",
    },
    {
        "id": "validation_cost",
        "name": "Requires >$1K to Test",
        "description": "You shouldn't need more than $1K to test the idea",
        "question": "Can you test this idea for under $1,000?",
    },
    {
        "id": "only_customer",
        "name": "You're the Only Customer",
        "description": "Being your own only known customer is a red flag",
        "question": "Do you know customers OTHER than yourself?",
    },
    {
        "id": "low_pain",
        "name": "Pain Score <7",
        "description": "After talking to real customers, pain must be 7+/10",
        "question": "After customer conversations, is the pain score 7+/10?",
    },
    {
        "id": "competition_dominated",
        "name": "Market Dominated (Competition <3)",
        "description": "If competition score is below 3, market is too dominated",
        "category_link": "competition",
    },
    {
        "id": "no_distribution",
        "name": "Can't Reach Customers (Distribution <4)",
        "description": "If you can't reach customers, nothing else matters",
        "category_link": "distribution",
    },
]

# ============================================================================
# ANTI-RATIONALIZATION PATTERNS
# ============================================================================

RATIONALIZATION_PATTERNS = [
    {
        "pattern": r"but (my|i have|i've got).*(twitter|audience|followers)",
        "condition": lambda scores: scores.get("distribution", 10) < 5,
        "warning": "Your distribution score is {score}/10. 200 Twitter followers ≠ distribution.",
        "past_project": "this is exactly what you said before your last 5 projects that got 0 customers",
    },
    {
        "pattern": r"(research is wrong|data is wrong|numbers are off)",
        "condition": lambda scores: scores.get("demand_signals", 10) < 5,
        "warning": "The research shows low demand. You're pattern-matching to 'I want this to work'.",
        "past_project": "Project #3 where you ignored market research",
    },
    {
        "pattern": r"competitors (are bad|suck|aren't good)",
        "condition": lambda scores: scores.get("competition", 10) < 5,
        "warning": "If competitors are so bad, why do they have customers and you don't?",
        "past_project": "the 'I can do it better' projects that never shipped",
    },
    {
        "pattern": r"(build|ship|launch|finish).*(week|days|weekend|quickly)",
        "condition": lambda _: True,  # Always flag time estimates
        "warning": "Your historical accuracy is 4x off. '2 weeks' means 8 weeks. Plan accordingly.",
        "past_project": "every project you've ever estimated",
    },
    {
        "pattern": r"(just need|only need).*(one|1|few|some).*customer",
        "condition": lambda _: True,
        "warning": "You've shipped 1 project and gotten 0 to 10 customers. 'Just need' is cope.",
        "past_project": "the project you shipped that got <10 customers",
    },
    {
        "pattern": r"(different|unique|special|unlike)",
        "condition": lambda scores: scores.get("unfair_advantage", 10) < 5,
        "warning": "Everyone thinks they're different. Your unfair advantage score says otherwise.",
        "past_project": "every 'this time is different' moment",
    },
    {
        "pattern": r"(once|when|after).*(build|launch|ship)",
        "condition": lambda _: True,
        "warning": "You're planning for post-launch when 4/5 of your projects never shipped.",
        "past_project": "the 4 projects that never made it to launch",
    },
    {
        "pattern": r"(growth|scale|viral|organic)",
        "condition": lambda scores: scores.get("distribution", 10) < 5,
        "warning": "Organic growth requires an audience. You have 200 Twitter followers.",
        "past_project": "hoping for virality instead of doing distribution",
    },
]

# ============================================================================
# VERDICT ENUM
# ============================================================================

class Verdict(Enum):
    BUILD_NOW = "BUILD NOW"
    VALIDATE_FIRST = "VALIDATE FIRST"
    STOP = "STOP"

# ============================================================================
# CORE VALIDATION LOGIC
# ============================================================================

@dataclass
class ValidationResult:
    idea: str
    target_customer: str
    price_point: str
    category_scores: dict
    hard_stops_triggered: list
    rationalizations_detected: list
    final_score: float
    verdict: Verdict
    action_items: list

def get_color(score: float) -> str:
    """Return ANSI color code based on score."""
    if score >= 8:
        return "\033[92m"  # Green
    elif score >= 6:
        return "\033[93m"  # Yellow
    else:
        return "\033[91m"  # Red

def reset_color() -> str:
    return "\033[0m"

def bold() -> str:
    return "\033[1m"

def print_header(text: str):
    """Print a section header."""
    print(f"\n{bold()}{'='*60}{reset_color()}")
    print(f"{bold()}{text}{reset_color()}")
    print(f"{bold()}{'='*60}{reset_color()}")

def print_category_score(name: str, score: float, weight: float, description: str):
    """Print a single category score line."""
    color = get_color(score)
    weighted = score * weight
    bar = "█" * int(score) + "░" * (10 - int(score))
    print(f"  {name:.<30} {color}{bar} {score:.1f}/10{reset_color()} (×{weight:.0%} = {weighted:.2f})")

def prompt_score(category_key: str, category: dict) -> float:
    """Prompt user to score a category."""
    print(f"\n{bold()}📊 {category['name']}{reset_color()}")
    print(f"   {category['description']}")
    print(f"   {'-'*50}")

    for i, q in enumerate(category.get('questions', []), 1):
        print(f"   {i}. {q}")

    while True:
        try:
            score_input = input(f"\n   Score (0-10): ").strip()
            if score_input.lower() in ('q', 'quit', 'exit'):
                sys.exit(0)
            score = float(score_input)
            if 0 <= score <= 10:
                return score
            print("   ⚠️  Score must be between 0 and 10")
        except ValueError:
            print("   ⚠️  Please enter a number between 0 and 10")

def prompt_hard_stop(rule: dict) -> bool:
    """Prompt user for a hard stop rule. Returns True if it's a STOP."""
    print(f"\n{bold()}🚨 HARD STOP CHECK: {rule['name']}{reset_color()}")
    print(f"   {rule['description']}")

    if 'question' in rule:
        print(f"\n   ❓ {rule['question']}")
        while True:
            answer = input("   (y/n): ").strip().lower()
            if answer in ('y', 'yes'):
                return False  # Not a stop
            elif answer in ('n', 'no'):
                return True   # This IS a stop
            print("   ⚠️  Please answer y or n")

    return False  # Category-linked rules are checked separately

def check_rationalizations(user_input: str, scores: dict) -> list:
    """Check for rationalization patterns in user input."""
    detected = []

    for pattern_def in RATIONALIZATION_PATTERNS:
        if re.search(pattern_def["pattern"], user_input.lower()):
            if pattern_def["condition"](scores):
                score_val = None
                # Try to find relevant score for the warning message
                for key, val in scores.items():
                    if key in pattern_def.get("warning", ""):
                        score_val = val
                        break

                warning = pattern_def["warning"]
                if score_val is not None:
                    warning = warning.format(score=score_val)

                detected.append({
                    "warning": warning,
                    "past_project": pattern_def["past_project"],
                })

    return detected

def calculate_final_score(scores: dict) -> float:
    """Calculate weighted final score."""
    total = 0.0
    for key, score in scores.items():
        weight = CATEGORIES[key]["weight"]
        total += score * weight
    return total

def get_verdict(score: float, hard_stops: list) -> Verdict:
    """Determine verdict based on score and hard stops."""
    if hard_stops:
        return Verdict.STOP
    if score >= 8.0:
        return Verdict.BUILD_NOW
    if score >= 6.0:
        return Verdict.VALIDATE_FIRST
    return Verdict.STOP

def generate_action_items(scores: dict, verdict: Verdict) -> list:
    """Generate specific action items based on scores and verdict."""
    items = []

    if verdict == Verdict.STOP:
        items.append("🛑 Do NOT proceed with this idea as-is")
        items.append("📋 Document what you learned and move on")
        items.append("⏰ Set a 48-hour cooling off period before considering pivots")
        return items

    # Find lowest scoring categories
    sorted_scores = sorted(scores.items(), key=lambda x: x[1])
    weak_categories = sorted_scores[:3]

    items.append(f"📅 2-WEEK VALIDATION SPRINT:")

    for key, score in weak_categories:
        cat = CATEGORIES[key]
        if key == "demand_signals" and score < 7:
            items.append(f"  • Week 1: Find 20 Reddit/Twitter posts about this problem")
            items.append(f"  • Week 1: Set up Google Alerts for related keywords")
        elif key == "distribution" and score < 7:
            items.append(f"  • Week 1: DM 20 potential customers on Twitter/Reddit")
            items.append(f"  • Week 1: Post in r/SaaS, r/indiehackers asking for feedback")
        elif key == "customer_asks" and score < 7:
            items.append(f"  • Week 1: Find 10 feature requests on competitor forums")
            items.append(f"  • Week 1: Search 'I wish [X] existed' posts")
        elif key == "icp_validation" and score < 7:
            items.append(f"  • Week 1: Write down 10 SPECIFIC people (names) who need this")
            items.append(f"  • Week 1: DM all 10 and ask about their current solution")
        elif key == "competition" and score < 7:
            items.append(f"  • Week 1: Sign up for top 3 competitors")
            items.append(f"  • Week 1: Document every weakness and complaint")

    items.append(f"\n📊 VALIDATION CRITERIA:")
    items.append(f"  • Get 5 'I would pay for this' responses (not 'cool idea')")
    items.append(f"  • Confirm pain score 7+/10 from real conversations")
    items.append(f"  • Identify your distribution channel (where you'll get first 10 customers)")

    items.append(f"\n⏱️ TIME BOX:")
    items.append(f"  • Maximum 2 weeks of validation")
    items.append(f"  • If you can't validate in 2 weeks, it's a STOP")
    items.append(f"  • Remember: You estimate 4x too optimistically")

    return items

def print_validation_result(result: ValidationResult):
    """Print the full validation result."""

    # Header
    print("\n" + "🎯" * 30)
    print_header("STARTUP VALIDATION REPORT")

    print(f"\n{bold()}IDEA:{reset_color()} {result.idea}")
    print(f"{bold()}TARGET:{reset_color()} {result.target_customer}")
    print(f"{bold()}PRICE:{reset_color()} {result.price_point}")

    # Verdict
    print_header("VERDICT")

    verdict_colors = {
        Verdict.BUILD_NOW: "\033[92m",      # Green
        Verdict.VALIDATE_FIRST: "\033[93m", # Yellow
        Verdict.STOP: "\033[91m",           # Red
    }

    color = verdict_colors[result.verdict]
    score_color = get_color(result.final_score)

    print(f"\n  {bold()}{score_color}SCORE: {result.final_score:.1f}/10{reset_color()}")
    print(f"  {bold()}{color}VERDICT: {result.verdict.value}{reset_color()}")

    if result.verdict == Verdict.BUILD_NOW:
        print(f"\n  ✅ Green light to build. But remember:")
        print(f"     • Your estimation is 4x off. Plan for that.")
        print(f"     • You've shipped 1/5 projects. Commit to finishing.")
        print(f"     • Distribution is still your weakest link.")
    elif result.verdict == Verdict.VALIDATE_FIRST:
        print(f"\n  ⚠️  Promising but needs validation before building")
        print(f"     • Do NOT write code yet")
        print(f"     • 2-week validation sprint first")
        print(f"     • See action items below")
    else:
        print(f"\n  🛑 Do not proceed with this idea")
        print(f"     • This is not a 'try harder' situation")
        print(f"     • Move on to the next idea")

    # Hard Stops
    if result.hard_stops_triggered:
        print_header("🚨 HARD STOPS TRIGGERED")
        for stop in result.hard_stops_triggered:
            print(f"\n  ❌ {stop['name']}")
            print(f"     {stop['description']}")

    # Category Breakdown
    print_header("CATEGORY BREAKDOWN")

    sorted_categories = sorted(
        result.category_scores.items(),
        key=lambda x: CATEGORIES[x[0]]["weight"],
        reverse=True
    )

    for key, score in sorted_categories:
        cat = CATEGORIES[key]
        print_category_score(cat["name"], score, cat["weight"], cat["description"])

    print(f"\n  {'-'*50}")
    print(f"  {'WEIGHTED TOTAL':.<30} {bold()}{get_color(result.final_score)}{result.final_score:.2f}/10{reset_color()}")

    # Anti-Rationalization Warnings
    if result.rationalizations_detected:
        print_header("⚠️  RATIONALIZATION DETECTED")
        for r in result.rationalizations_detected:
            print(f"\n  🧠 {r['warning']}")
            print(f"     ↳ This is the same thinking that killed: {r['past_project']}")

    # Action Items
    print_header("📋 ACTION ITEMS")
    for item in result.action_items:
        print(f"  {item}")

    # Context Reminder
    print_header("🪞 YOUR CONTEXT (reality check)")
    print(f"""
  Distribution Reality:
    • Twitter: {USER_CONTEXT['distribution']['twitter_followers']} followers (not a distribution channel)
    • Reddit: Access to {', '.join(USER_CONTEXT['distribution']['reddit_access'])}
    • Email list: {USER_CONTEXT['distribution']['email_list']} subscribers

  Track Record:
    • Projects started: {USER_CONTEXT['track_record']['projects_started']}
    • Projects shipped: {USER_CONTEXT['track_record']['projects_shipped']}
    • Projects with 10+ customers: {USER_CONTEXT['track_record']['projects_with_10_customers']}
    • Average quit time: {USER_CONTEXT['track_record']['average_quit_weeks']} weeks
    • Estimation accuracy: {USER_CONTEXT['track_record']['estimation_multiplier']}x off

  Personality Fit Check:
    • ✓ Self-serve product? {result.category_scores.get('payment_friction', 5) >= 7}
    • ✓ Short sales cycle? {result.category_scores.get('sales_cycle', 5) >= 7}
    • ✓ Async-friendly? {result.category_scores.get('integration_complexity', 5) >= 6}
""")

    print("\n" + "🎯" * 30 + "\n")

def run_interactive_validation(idea: str, target: str, price: str) -> ValidationResult:
    """Run the full interactive validation flow."""

    print("\n" + "="*60)
    print(f"{bold()}🔍 STARTUP VALIDATOR - Brutally Honest Edition{reset_color()}")
    print("="*60)
    print(f"\nValidating: {idea}")
    print(f"Target: {target}")
    print(f"Price: {price}")
    print("\nAnswer honestly. Lying only hurts you.")
    print("Type 'q' to quit at any time.\n")

    # Collect category scores
    scores = {}
    for key, category in CATEGORIES.items():
        scores[key] = prompt_score(key, category)

    # Check hard stops
    hard_stops = []

    # Category-linked hard stops
    if scores.get("competition", 10) < 3:
        hard_stops.append(next(r for r in HARD_STOP_RULES if r["id"] == "competition_dominated"))

    if scores.get("distribution", 10) < 4:
        hard_stops.append(next(r for r in HARD_STOP_RULES if r["id"] == "no_distribution"))

    # Prompted hard stops
    print_header("HARD STOP CHECKS")
    for rule in HARD_STOP_RULES:
        if "category_link" not in rule:
            if prompt_hard_stop(rule):
                hard_stops.append(rule)

    # Check for rationalizations in original input
    combined_input = f"{idea} {target} {price}"
    rationalizations = check_rationalizations(combined_input, scores)

    # Calculate final score
    final_score = calculate_final_score(scores)

    # Get verdict
    verdict = get_verdict(final_score, hard_stops)

    # Generate action items
    action_items = generate_action_items(scores, verdict)

    return ValidationResult(
        idea=idea,
        target_customer=target,
        price_point=price,
        category_scores=scores,
        hard_stops_triggered=hard_stops,
        rationalizations_detected=rationalizations,
        final_score=final_score,
        verdict=verdict,
        action_items=action_items,
    )

def run_demo_validation() -> ValidationResult:
    """Run a demo validation with sample scores to show output format."""

    # Sample idea
    idea = "AI tool that writes personalized cold emails for B2B sales"
    target = "B2B SaaS founders doing outbound sales"
    price = "$49/month"

    # Sample scores (realistic mixed bag)
    scores = {
        "demand_signals": 7.0,      # Lots of cold email complaints
        "competition": 5.0,         # Lemlist, Instantly exist
        "icp_validation": 6.0,      # Can find them on Twitter
        "market_gap": 6.0,          # Personalization is weak in existing tools
        "customer_asks": 7.0,       # People complain about generic emails
        "churn_risk": 5.0,          # Monthly need but might churn
        "failed_alternatives": 7.0, # Some failed but for different reasons
        "buy_vs_build": 8.0,        # People use templates + ChatGPT
        "price_sensitivity": 7.0,   # $49 is reasonable
        "sales_cycle": 8.0,         # Self-serve possible
        "tam": 7.0,                 # Decent market
        "trend_backing": 8.0,       # AI is hot
        "integration_complexity": 7.0,  # Can be simple
        "payment_friction": 8.0,    # Credit card OK
        "distribution": 4.0,        # Weak - your bottleneck
        "unfair_advantage": 4.0,    # Nothing special
        "founder_market_fit": 6.0,  # Research/AI matches, sales doesn't
    }

    # Sample hard stops (distribution triggers one)
    hard_stops = []
    if scores.get("distribution", 10) < 4:
        hard_stops.append(next(r for r in HARD_STOP_RULES if r["id"] == "no_distribution"))

    # Sample rationalization (simulate user saying they can build it in 2 weeks)
    rationalizations = [{
        "warning": "Your historical accuracy is 4x off. '2 weeks' means 8 weeks. Plan accordingly.",
        "past_project": "every project you've ever estimated",
    }]

    final_score = calculate_final_score(scores)
    verdict = get_verdict(final_score, hard_stops)
    action_items = generate_action_items(scores, verdict)

    return ValidationResult(
        idea=idea,
        target_customer=target,
        price_point=price,
        category_scores=scores,
        hard_stops_triggered=hard_stops,
        rationalizations_detected=rationalizations,
        final_score=final_score,
        verdict=verdict,
        action_items=action_items,
    )

def print_usage():
    """Print usage information."""
    print("""
╔══════════════════════════════════════════════════════════════╗
║              STARTUP VALIDATOR CLI                           ║
║         Brutally Honest Business Idea Validation             ║
╚══════════════════════════════════════════════════════════════╝

USAGE:
    python validate.py "<idea>" "<target customer>" "<price>"
    python validate.py --demo    # See example output
    python validate.py --quick "<idea>" "<target>" "<price>"  # Fast mode (5 key questions)

EXAMPLES:
    python validate.py "AI cold email writer" "B2B SaaS founders" "$29/mo"
    python validate.py "Notion template marketplace" "productivity enthusiasts" "$19 one-time"
    python validate.py "Discord bot for DAOs" "Web3 community managers" "$99/mo"

WHAT IT DOES:
    1. Scores your idea across 17 weighted categories
    2. Checks for hard-stop deal-breakers
    3. Detects rationalization patterns
    4. Gives you a BUILD NOW / VALIDATE FIRST / STOP verdict
    5. Provides specific action items

MODES:
    (default)  Full validation - all 17 categories + hard stop checks
    --demo     Show example output without answering questions
    --quick    Fast mode - only 5 key questions for rapid screening

SCORING:
    8.0+ = BUILD NOW (with caveats)
    6.0-7.9 = VALIDATE FIRST (2-week sprint)
    <6.0 = STOP (move on)

HARD STOPS (any = automatic STOP):
    • Can't name 10 specific people with the problem
    • Takes >2 weeks to validate core assumption
    • Requires >$1K to test
    • You're the only customer you know
    • Pain score <7 after customer conversations
    • Competition score <3 (market dominated)
    • Distribution score <4 (can't reach customers)

Remember: You've started 5 projects, shipped 1, gotten 0 to 10 customers.
This tool exists to break that pattern.
""")

def run_quick_validation(idea: str, target: str, price: str) -> ValidationResult:
    """Run a quick validation with only 5 key questions."""

    print("\n" + "="*60)
    print(f"{bold()}⚡ QUICK VALIDATION MODE{reset_color()}")
    print("="*60)
    print(f"\nValidating: {idea}")
    print(f"Target: {target}")
    print(f"Price: {price}")
    print("\n5 critical questions only. Full validation recommended for BUILD decisions.\n")

    # Key categories for quick screening
    quick_categories = ["demand_signals", "distribution", "competition", "customer_asks", "founder_market_fit"]

    scores = {}

    # Score only key categories
    for key in quick_categories:
        scores[key] = prompt_score(key, CATEGORIES[key])

    # Fill remaining categories with estimates based on quick scores
    avg_score = sum(scores.values()) / len(scores)
    for key in CATEGORIES:
        if key not in scores:
            # Conservative estimate
            scores[key] = max(5.0, avg_score - 1)

    # Check hard stops
    hard_stops = []
    if scores.get("competition", 10) < 3:
        hard_stops.append(next(r for r in HARD_STOP_RULES if r["id"] == "competition_dominated"))
    if scores.get("distribution", 10) < 4:
        hard_stops.append(next(r for r in HARD_STOP_RULES if r["id"] == "no_distribution"))

    # Quick hard stop check
    print_header("⚡ QUICK HARD STOP CHECK")
    print("\n  Answer these 2 critical questions:")

    # Most important hard stops
    key_stops = [r for r in HARD_STOP_RULES if r["id"] in ("no_specific_customers", "only_customer")]
    for rule in key_stops:
        if prompt_hard_stop(rule):
            hard_stops.append(rule)

    combined_input = f"{idea} {target} {price}"
    rationalizations = check_rationalizations(combined_input, scores)

    final_score = calculate_final_score(scores)
    verdict = get_verdict(final_score, hard_stops)
    action_items = generate_action_items(scores, verdict)

    # Add note about quick mode
    if verdict != Verdict.STOP:
        action_items.insert(0, "⚡ This was a QUICK validation. Run full validation before committing.")

    return ValidationResult(
        idea=idea,
        target_customer=target,
        price_point=price,
        category_scores=scores,
        hard_stops_triggered=hard_stops,
        rationalizations_detected=rationalizations,
        final_score=final_score,
        verdict=verdict,
        action_items=action_items,
    )

def main():
    """Main entry point."""

    # Handle --demo flag
    if len(sys.argv) == 2 and sys.argv[1] == "--demo":
        print("\n" + "="*60)
        print(f"{bold()}📋 DEMO MODE - Sample Validation Output{reset_color()}")
        print("="*60)
        result = run_demo_validation()
        print_validation_result(result)
        sys.exit(0)

    # Handle --quick flag
    if len(sys.argv) >= 2 and sys.argv[1] == "--quick":
        if len(sys.argv) == 5:
            idea = sys.argv[2]
            target = sys.argv[3]
            price = sys.argv[4]
        else:
            print("\n⚡ QUICK VALIDATION MODE\n")
            idea = input("💡 Business idea:\n> ").strip()
            target = input("\n👤 Target customer:\n> ").strip()
            price = input("\n💰 Price point:\n> ").strip()

        if not idea or not target or not price:
            print("Error: All fields are required")
            sys.exit(1)

        result = run_quick_validation(idea, target, price)
        print_validation_result(result)

        if result.verdict == Verdict.STOP:
            sys.exit(2)
        elif result.verdict == Verdict.VALIDATE_FIRST:
            sys.exit(1)
        sys.exit(0)

    # Handle no arguments - interactive mode
    if len(sys.argv) == 1:
        print_usage()
        print("\n" + "-"*60)
        print("No arguments provided. Starting interactive mode...\n")

        idea = input("💡 Describe your business idea (1-2 sentences):\n> ").strip()
        if not idea:
            print("Error: Idea cannot be empty")
            sys.exit(1)

        target = input("\n👤 Who is your target customer?\n> ").strip()
        if not target:
            print("Error: Target customer cannot be empty")
            sys.exit(1)

        price = input("\n💰 What's your price point?\n> ").strip()
        if not price:
            print("Error: Price point cannot be empty")
            sys.exit(1)

    elif len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help", "help"):
        print_usage()
        sys.exit(0)

    elif len(sys.argv) == 4:
        idea = sys.argv[1]
        target = sys.argv[2]
        price = sys.argv[3]

    else:
        print("Error: Invalid arguments")
        print_usage()
        sys.exit(1)

    # Run validation
    result = run_interactive_validation(idea, target, price)

    # Print results
    print_validation_result(result)

    # Exit with appropriate code
    if result.verdict == Verdict.STOP:
        sys.exit(2)
    elif result.verdict == Verdict.VALIDATE_FIRST:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
