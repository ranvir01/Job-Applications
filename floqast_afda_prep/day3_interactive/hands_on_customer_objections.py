# -*- coding: utf-8 -*-
"""
Day 3: Hands-On Customer Objection Handling
Real practice - Handle actual customer objections
"""

import sys

def get_input(prompt=""):
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return ""

def objection_ai_skeptic():
    """Handle: 'I don't trust AI with accounting'"""
    
    print("\n" + "="*70)
    print("OBJECTION 1: 'I Don't Trust AI'")
    print("="*70)
    
    print("""
CUSTOMER: Sarah, CFO of Precision Manufacturing

"Look, I appreciate you taking the time, but I'm really skeptical about
AI in accounting. One wrong journal entry and we have audit issues.
How can I trust a machine with something this critical?"

YOUR TASK: Handle this objection. Type your response.
""")
    
    response = get_input("\nYOU: ")
    
    score = 0
    feedback = []
    
    # Check response quality
    if 'human' in response.lower() or 'review' in response.lower() or 'approval' in response.lower():
        score += 25
        feedback.append("✓ Emphasized human-in-the-loop")
    else:
        feedback.append("✗ Missed opportunity to mention human review/approval")
    
    if 'rule' in response.lower() or 'logic' in response.lower() or 'transparent' in response.lower():
        score += 20
        feedback.append("✓ Explained AI follows defined rules")
    else:
        feedback.append("~ Could explain that AI follows YOUR rules, not making decisions")
    
    if 'audit' in response.lower() or 'trail' in response.lower():
        score += 20
        feedback.append("✓ Addressed audit trail/visibility")
    else:
        feedback.append("~ Could mention complete audit trail for auditors")
    
    if 'example' in response.lower() or 'specific' in response.lower() or 'coupa' in response.lower():
        score += 20
        feedback.append("✓ Used specific example")
    else:
        feedback.append("~ Could give concrete example (e.g., Coupa accruals)")
    
    if any(word in response.lower() for word in ['understand', 'hear', 'valid', 'appreciate']):
        score += 15
        feedback.append("✓ Acknowledged their concern empathetically")
    else:
        feedback.append("~ Should acknowledge concern before addressing it")
    
    # Show results
    print("\n" + "-"*70)
    print("FEEDBACK:")
    for fb in feedback:
        print(f"  {fb}")
    
    print(f"\nSCORE: {score}/100")
    
    print("\n" + "-"*70)
    print("IDEAL RESPONSE:")
    print("-"*70)
    print("""
"I completely understand your concern - accounting requires precision,
and that's exactly why FloQast built Transform AI with accountants,
not just engineers.

Here's how it actually works: The AI doesn't make decisions on its own.
It follows rules YOU define. For example, for Coupa accruals, you tell
it: pull POs with status 'Received-Not-Invoiced', map Maintenance to
GL 6100, set threshold at $500. The AI executes those rules consistently.

Every entry the agent creates goes to your team for approval before
posting. Nothing touches your books without human sign-off. It's not
replacing judgment - it's replacing repetitive data entry.

And for audit purposes, there's a complete trail showing what data was
used, what rules were applied, and who approved it. Actually MORE
transparent than manual processes.

Would it help if I showed you a specific example with your actual data?"
""")
    
    return score >= 60


def objection_expensive():
    """Handle: 'This seems too expensive'"""
    
    print("\n" + "="*70)
    print("OBJECTION 2: 'Too Expensive'")
    print("="*70)
    
    print("""
CUSTOMER: Jennifer, VP Finance at Retail Chain

"We've seen the pricing. It's $35K annually. That's a significant
investment given our tight budgets. How do you justify the cost?"

YOUR TASK: Build ROI case. Answer these questions.
""")
    
    score = 0
    feedback = []
    
    # Q1: Discovery
    print("\n--- What do you ask FIRST? ---")
    discovery_q = get_input("YOU: ")
    
    if any(word in discovery_q.lower() for word in ['cost', 'time', 'hours', 'people', 'spend', 'current']):
        score += 30
        feedback.append("✓ Asked discovery question about current costs/time")
    else:
        score += 5
        feedback.append("✗ Should ask about current costs BEFORE building ROI case")
    
    # Give them data
    print("\n[CUSTOMER]: 'We have 3 accountants spending about 40% of their")
    print("time on close activities. Fully loaded cost is about $200K annually.'")
    
    # Q2: Calculate savings
    print("\n--- Calculate potential savings ---")
    print("If FloQast reduces close time by 25%, what's annual savings?")
    savings = get_input("Your calculation: $")
    
    try:
        sav_val = float(savings.replace('$', '').replace(',', '').replace('k', '000').replace('K', '000'))
        expected = 200000 * 0.40 * 0.25  # $20,000
        
        if 15000 <= sav_val <= 25000:
            score += 30
            feedback.append(f"✓ Savings calculation: ${sav_val:,.0f} is correct")
        else:
            score += 10
            feedback.append(f"~ Savings: Close, but math is: $200K × 40% × 25% = $20K")
    except:
        feedback.append("✗ Calculation: $200K × 40% × 25% = $20K annual savings")
    
    # Q3: ROI pitch
    print("\n--- How do you position the $35K cost vs $20K savings? ---")
    print("(Hint: There's more to ROI than just time savings)")
    roi_pitch = get_input("YOU: ")
    
    if 'risk' in roi_pitch.lower() or 'error' in roi_pitch.lower() or 'audit' in roi_pitch.lower():
        score += 20
        feedback.append("✓ Mentioned risk reduction value")
    else:
        feedback.append("~ Could mention risk reduction (errors, audit findings)")
    
    if 'scale' in roi_pitch.lower() or 'grow' in roi_pitch.lower():
        score += 20
        feedback.append("✓ Mentioned scalability benefit")
    else:
        feedback.append("~ Could mention scalability (handle growth without adding headcount)")
    
    # Show results
    print("\n" + "-"*70)
    print("FEEDBACK:")
    for fb in feedback:
        print(f"  {fb}")
    
    print(f"\nSCORE: {score}/100")
    
    print("\n" + "-"*70)
    print("IDEAL ROI APPROACH:")
    print("-"*70)
    print("""
1. DISCOVER current costs:
   "What does your close process currently cost in time and people?"
   
2. QUANTIFY savings:
   Current: 3 accountants × 40% time × $200K = $80K on close
   FloQast reduction: 25% = $20K saved
   
3. ADDRESS the gap ($35K cost vs $20K savings):
   "The direct time savings are $20K, which covers more than half the cost.
   But there's additional value:
   
   - Risk reduction: Fewer manual errors means fewer audit findings
   - Scalability: Handle revenue growth without adding accounting headcount  
   - Strategic value: Your team spends time on analysis, not data entry
   - Faster close: Make business decisions earlier in the month"
   
4. OFFER pilot:
   "Let's start with one high-value use case - your bank reconciliations.
   We can prove ROI on a small scale before full deployment."
""")
    
    return score >= 50


def main():
    print("\n" + "="*70)
    print("DAY 3: HANDS-ON OBJECTION HANDLING")
    print("="*70)
    
    print("""
Real customer objections - YOU handle them.

Available Scenarios:
  1 - "I don't trust AI with accounting"
  2 - "This seems too expensive"
  Q - Quit
""")
    
    while True:
        try:
            choice = input("\nChoose scenario (1-2, Q to quit): ").strip()
            
            if choice.lower() == 'q':
                break
            
            elif choice == '1':
                objection_ai_skeptic()
                input("\nPress Enter to continue...")
            
            elif choice == '2':
                objection_expensive()
                input("\nPress Enter to continue...")
            
            else:
                print("Invalid choice.")
                
        except KeyboardInterrupt:
            break
        except EOFError:
            objection_ai_skeptic()
            objection_expensive()
            break


if __name__ == "__main__":
    main()



