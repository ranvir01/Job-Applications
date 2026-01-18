# -*- coding: utf-8 -*-
"""
Day 4: Hands-On Teaching Practice
Explain concepts - YOU teach, AI scores clarity
"""

import sys

def get_input(prompt=""):
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return ""

def teach_accruals():
    """Teach: What is an accrual?"""
    
    print("\n" + "="*70)
    print("TEACHING EXERCISE: Explain Accruals")
    print("="*70)
    
    print("""
STUDENT: New staff accountant (6 months experience)

"I'm looking at this accrual entry the agent created. We're debiting
Maintenance Expense for $12,500 even though we haven't received an
invoice yet. Why are we recording an expense before we're billed?"

YOUR TASK: Explain accrual accounting. Type your explanation.
""")
    
    explanation = get_input("\nYOU: ")
    
    score = 0
    feedback = []
    
    # Check explanation quality
    if 'matching' in explanation.lower() or 'period' in explanation.lower():
        score += 25
        feedback.append("✓ Explained matching principle")
    else:
        feedback.append("✗ Should explain matching principle (expense in period it happened)")
    
    if 'invoice' in explanation.lower() and 'when' in explanation.lower():
        score += 20
        feedback.append("✓ Addressed timing vs billing")
    else:
        feedback.append("~ Could clarify timing: when expense happened vs when billed")
    
    if 'accurate' in explanation.lower() or 'correct' in explanation.lower() or 'true' in explanation.lower():
        score += 20
        feedback.append("✓ Explained why it matters (accurate financials)")
    else:
        feedback.append("~ Could explain business purpose (accurate financial statements)")
    
    if any(word in explanation.lower() for word in ['example', 'like', 'think of', 'imagine']):
        score += 20
        feedback.append("✓ Used analogy or example")
    else:
        feedback.append("~ Using analogy makes it more relatable")
    
    if 'reverse' in explanation.lower() or 'next month' in explanation.lower() or 'january' in explanation.lower():
        score += 15
        feedback.append("✓ Explained what happens when invoice arrives")
    else:
        feedback.append("~ Could complete the cycle (what happens in January)")
    
    # Results
    print("\n" + "-"*70)
    print("TEACHING SCORE:")
    for fb in feedback:
        print(f"  {fb}")
    
    print(f"\nTOTAL: {score}/100")
    
    if score >= 80:
        print("\nExcellent teaching! Clear and complete.")
    elif score >= 60:
        print("\nGood explanation. Add more context.")
    else:
        print("\nNeeds work. Use simpler language and examples.")
    
    print("\n" + "-"*70)
    print("IDEAL EXPLANATION:")
    print("-"*70)
    print("""
"Financial statements need to show what ACTUALLY happened in a period.
If we received $12,500 of maintenance in December, December should
show that expense - even if the bill doesn't come until January.

Think of it like a credit card. You made a purchase in December, so
that's when the expense really happened, even though you pay the bill
in January.

The entry is: Debit Maintenance Expense $12,500 (recording December expense),
Credit Accrued Liabilities $12,500 (we owe this but haven't been billed).

In January when the invoice arrives, we reverse the accrual and record
the actual payment. This ensures December financials are accurate."
""")
    
    return score >= 60


def teach_bank_rec():
    """Teach: Bank reconciliation process"""
    
    print("\n" + "="*70)
    print("TEACHING EXERCISE: Bank Reconciliation")
    print("="*70)
    
    print("""
STUDENT: Finance manager (non-accounting background)

"I came from operations. Can you explain what bank reconciliation
actually accomplishes? We have the bank statement, we have our books -
why do they need to be reconciled? Shouldn't they just match?"

YOUR TASK: Explain bank reconciliation. Type your explanation.
""")
    
    explanation = get_input("\nYOU: ")
    
    score = 0
    feedback = []
    
    # Check explanation
    if 'timing' in explanation.lower() or 'different' in explanation.lower() or 'delay' in explanation.lower():
        score += 25
        feedback.append("✓ Explained timing differences")
    else:
        feedback.append("✗ Should explain timing causes differences")
    
    if 'outstanding' in explanation.lower() or 'check' in explanation.lower():
        score += 20
        feedback.append("✓ Gave example of outstanding checks")
    else:
        feedback.append("~ Should give concrete example (outstanding checks)")
    
    if 'deposit' in explanation.lower() and 'transit' in explanation.lower():
        score += 20
        feedback.append("✓ Mentioned deposits in transit")
    else:
        feedback.append("~ Could mention deposits in transit")
    
    if 'bank charge' in explanation.lower() or 'fee' in explanation.lower():
        score += 20
        feedback.append("✓ Mentioned bank charges")
    else:
        feedback.append("~ Could mention bank charges we didn't know about")
    
    if 'why' in explanation.lower() or 'purpose' in explanation.lower() or 'catch' in explanation.lower():
        score += 15
        feedback.append("✓ Explained purpose (catch errors/fraud)")
    else:
        feedback.append("~ Could explain WHY we do this (internal control)")
    
    # Results
    print("\n" + "-"*70)
    print("TEACHING SCORE:")
    for fb in feedback:
        print(f"  {fb}")
    
    print(f"\nTOTAL: {score}/100")
    
    print("\n" + "-"*70)
    print("IDEAL EXPLANATION:")
    print("-"*70)
    print("""
"Your books and the bank often show different numbers - and that's normal.
Reconciliation figures out WHY they're different.

Outstanding checks - you wrote a check on 12/30, but the recipient
hasn't cashed it yet, so the bank doesn't show it.

Deposits in transit - you deposited cash on 12/31, but the bank
didn't process it until 1/2.

Bank charges - the bank charged you $25 for a service fee, but you
didn't know about it until you saw the statement.

The purpose is ensuring we catch everything - mistakes, fraud, missing
entries. It's a key internal control."
""")
    
    return score >= 60


def main():
    print("\n" + "="*70)
    print("DAY 4: HANDS-ON TEACHING PRACTICE")
    print("="*70)
    
    print("""
YOU explain concepts - AI scores your clarity.

Available Exercises:
  1 - Explain: What is an accrual?
  2 - Explain: Bank reconciliation
  Q - Quit
""")
    
    while True:
        try:
            choice = input("\nChoose exercise (1-2, Q to quit): ").strip()
            
            if choice.lower() == 'q':
                break
            
            elif choice == '1':
                teach_accruals()
                input("\nPress Enter to continue...")
            
            elif choice == '2':
                teach_bank_rec()
                input("\nPress Enter to continue...")
            
            else:
                print("Invalid choice.")
                
        except KeyboardInterrupt:
            break
        except EOFError:
            teach_accruals()
            teach_bank_rec()
            break


if __name__ == "__main__":
    main()



