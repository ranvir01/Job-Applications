# -*- coding: utf-8 -*-
"""
Day 2: Hands-On Agent Configuration
Real practice - YOU make the decisions, AI scores your choices
"""

import sys

def get_input(prompt):
    """Get user input"""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return ""

def scenario_manufacturing():
    """Hands-on: Configure Coupa accrual agent"""
    
    print("\n" + "="*70)
    print("HANDS-ON EXERCISE: Configure Coupa Accrual Agent")
    print("="*70)
    
    print("""
CUSTOMER CONTEXT:
- Company: TechManufacturing Inc
- ERP: NetSuite
- Procurement: Coupa
- Problem: 40 POs per month, 3 hours manual accrual work
- Current: Accountant exports "Goods Received" POs, creates JEs manually

YOUR TASK: Configure the agent by answering each question.
""")
    
    score = 0
    feedback = []
    
    # Question 1: Data Source
    print("\n--- QUESTION 1: DATA SOURCE ---")
    print("Where should the agent pull data from?")
    data_source = get_input("Your answer: ")
    
    if 'coupa' in data_source.lower() and 'api' in data_source.lower():
        score += 10
        feedback.append("✓ Data Source: Correct - Coupa API")
    elif 'coupa' in data_source.lower():
        score += 7
        feedback.append("~ Data Source: Mostly correct, but specify 'API' for clarity")
    else:
        feedback.append("✗ Data Source: Should be 'Coupa API'")
    
    # Question 2: Trigger
    print("\n--- QUESTION 2: TRIGGER TIMING ---")
    print("When should this agent run?")
    print("a) Daily at midnight")
    print("b) Last business day of month")
    print("c) First business day of month")
    print("d) Manual trigger only")
    trigger = get_input("Your answer (a/b/c/d): ").lower()
    
    if trigger == 'b':
        score += 15
        feedback.append("✓ Trigger: Perfect - Last business day captures month-end accruals")
    elif trigger == 'c':
        score += 10
        feedback.append("~ Trigger: First day works but you'd miss some December items")
    else:
        feedback.append("✗ Trigger: Should be last business day of month for accurate cutoff")
    
    # Question 3: Filter Status
    print("\n--- QUESTION 3: FILTER RULES ---")
    print("What Coupa status should the agent filter for?")
    print("(Hint: Customer said 'Goods Received' but not invoiced)")
    status = get_input("Your answer: ")
    
    if 'received' in status.lower() and ('not' in status.lower() or 'uninvoiced' in status.lower()):
        score += 15
        feedback.append("✓ Filter: Excellent - 'Received-Not-Invoiced' is correct")
    elif 'received' in status.lower():
        score += 10
        feedback.append("~ Filter: Close, but need to specify 'Not Invoiced' to avoid duplicates")
    else:
        feedback.append("✗ Filter: Should filter for 'Received-Not-Invoiced' status")
    
    # Question 4: Materiality
    print("\n--- QUESTION 4: MATERIALITY THRESHOLD ---")
    print("What's the minimum $ amount to accrue?")
    print("(Too low = noise, too high = miss important items)")
    materiality = get_input("Your answer: $")
    
    try:
        mat_value = float(materiality.replace('$', '').replace(',', ''))
        if 500 <= mat_value <= 1000:
            score += 15
            feedback.append(f"✓ Materiality: ${mat_value:,.0f} is perfect - avoids noise without missing material items")
        elif 100 <= mat_value < 500:
            score += 10
            feedback.append(f"~ Materiality: ${mat_value:,.0f} might create noise with small items")
        elif mat_value > 2000:
            score += 5
            feedback.append(f"~ Materiality: ${mat_value:,.0f} is high - you might miss important accruals")
        else:
            feedback.append(f"✗ Materiality: ${mat_value:,.0f} is too extreme")
    except:
        feedback.append("✗ Materiality: Enter a number (e.g., 500)")
    
    # Question 5: GL Mapping
    print("\n--- QUESTION 5: GL ACCOUNT MAPPING ---")
    print("Map this category to a GL account:")
    print("Category: Maintenance Expenses")
    print("What GL account? (format: ####-Account Name)")
    gl_account = get_input("Your answer: ")
    
    if any(x in gl_account for x in ['6', '5']) and ('maintenance' in gl_account.lower() or 'expense' in gl_account.lower()):
        score += 10
        feedback.append(f"✓ GL Mapping: {gl_account} - Good expense account structure")
    else:
        feedback.append("✗ GL Mapping: Expense accounts typically 5xxx or 6xxx series")
    
    # Question 6: Credit Account
    print("\n--- QUESTION 6: LIABILITY ACCOUNT ---")
    print("What GL account for the CREDIT side (what you owe)?")
    credit_account = get_input("Your answer: ")
    
    if '2' in credit_account and ('accrued' in credit_account.lower() or 'liability' in credit_account.lower() or 'payable' in credit_account.lower()):
        score += 15
        feedback.append(f"✓ Credit Account: {credit_account} - Correct liability account")
    else:
        feedback.append("✗ Credit Account: Should be 2xxx (liability) - Accrued Liabilities or AP")
    
    # Question 7: Approval
    print("\n--- QUESTION 7: APPROVAL WORKFLOW ---")
    print("Should this agent:")
    print("a) Auto-post entries (no approval)")
    print("b) Create draft for accountant review")
    print("c) Route to CFO for approval")
    approval = get_input("Your answer (a/b/c): ").lower()
    
    if approval == 'b':
        score += 20
        feedback.append("✓ Approval: Perfect - draft for review is best practice for new agents")
    elif approval == 'c':
        score += 10
        feedback.append("~ Approval: CFO approval is overkill - accountant review is sufficient")
    else:
        feedback.append("✗ Approval: Auto-posting without review is risky for new automations")
    
    # Results
    print("\n" + "="*70)
    print("YOUR CONFIGURATION SCORE")
    print("="*70)
    
    for fb in feedback:
        print(f"{fb}")
    
    print(f"\nTOTAL SCORE: {score}/100")
    
    if score >= 85:
        print("\n🎉 EXCELLENT! You'd configure this correctly in the field.")
        print("Your decisions show good judgment on timing, filters, and controls.")
    elif score >= 70:
        print("\n✓ GOOD! Minor tweaks needed but you understand the concepts.")
    else:
        print("\n📚 NEEDS WORK. Review agent configuration fundamentals.")
    
    print("\n" + "="*70)
    print("WHAT A REAL AFDA WOULD CONFIGURE:")
    print("="*70)
    print("""
✓ Data Source: Coupa API
✓ Trigger: Last business day of month, 6 PM (after close of business)
✓ Filter: Status = 'Received-Not-Invoiced' AND Receipt_Date <= Month End
✓ Materiality: $500 (avoids noise, captures material items)
✓ GL Mapping: Maintenance -> 6100-Maintenance Expense
✓ Credit Account: 2100-Accrued Liabilities
✓ Approval: Draft for accountant review (human-in-the-loop)
✓ Validation: Flag items >$10K for extra scrutiny

Expected Result: 40 POs automated, 3 hours -> 30 minutes (83% savings)
""")
    
    return score >= 70


def scenario_troubleshooting():
    """Hands-on: Troubleshoot broken agent"""
    
    print("\n" + "="*70)
    print("HANDS-ON EXERCISE: Troubleshoot Agent Failure")
    print("="*70)
    
    print("""
CUSTOMER ISSUE:
"The Coupa accrual agent ran last night but it created WRONG entries!
It accrued $50,000 for a single PO that should have been $5,000.
And it accrued items that were already invoiced. Help!"

YOUR TASK: Diagnose what's wrong and how to fix it.
""")
    
    score = 0
    feedback = []
    
    # Question 1: First step
    print("\n--- QUESTION 1: FIRST DIAGNOSTIC STEP ---")
    print("What's the FIRST thing you check?")
    print("a) Look at the agent configuration")
    print("b) Check the Coupa source data")
    print("c) Review the generated journal entries")
    print("d) Restart the agent")
    first_step = get_input("Your answer (a/b/c/d): ").lower()
    
    if first_step == 'c':
        score += 15
        feedback.append("✓ First Step: Correct - Review output to understand what went wrong")
    elif first_step == 'b':
        score += 10
        feedback.append("~ First Step: Data check is good, but review output first to see the symptom")
    else:
        feedback.append("✗ First Step: Always review the output first to understand the problem")
    
    # Question 2: $50K vs $5K issue
    print("\n--- QUESTION 2: AMOUNT ERROR DIAGNOSIS ---")
    print("The agent accrued $50,000 instead of $5,000 (10x error).")
    print("What could cause this?")
    amount_cause = get_input("Your answer: ")
    
    if 'quantity' in amount_cause.lower() or 'multiplied' in amount_cause.lower() or 'decimal' in amount_cause.lower():
        score += 20
        feedback.append("✓ Diagnosis: Yes! Likely quantity field being read as dollar amount")
    else:
        score += 5
        feedback.append("~ Diagnosis: Consider if quantity is being confused with amount in data mapping")
    
    # Question 3: Already invoiced issue
    print("\n--- QUESTION 3: FILTER ERROR DIAGNOSIS ---")
    print("The agent accrued items that were already invoiced.")
    print("What configuration issue would cause this?")
    filter_cause = get_input("Your answer: ")
    
    if 'filter' in filter_cause.lower() or 'status' in filter_cause.lower():
        score += 20
        feedback.append("✓ Diagnosis: Correct - filter isn't excluding 'Invoiced' status")
    else:
        score += 5
        feedback.append("~ Diagnosis: The filter rules aren't properly excluding invoiced items")
    
    # Question 4: Fix approach
    print("\n--- QUESTION 4: HOW TO FIX ---")
    print("What's your action plan?")
    print("a) Delete bad entries, disable agent, investigate, fix config, test, re-enable")
    print("b) Just fix the config and run again")
    print("c) Call FloQast support immediately")
    fix_approach = get_input("Your answer (a/b/c): ").lower()
    
    if fix_approach == 'a':
        score += 25
        feedback.append("✓ Fix Approach: Perfect systematic approach - stop, fix, test, validate")
    elif fix_approach == 'c':
        score += 10
        feedback.append("~ Fix Approach: Support can help but you should diagnose first")
    else:
        feedback.append("✗ Fix Approach: Need systematic approach - disable, diagnose, fix, test")
    
    # Question 5: Prevention
    print("\n--- QUESTION 5: HOW TO PREVENT ---")
    print("How do you prevent this from happening again?")
    prevention = get_input("Your answer: ")
    
    if 'test' in prevention.lower() or 'validation' in prevention.lower() or 'alert' in prevention.lower():
        score += 20
        feedback.append("✓ Prevention: Good! Testing + validation rules catch issues early")
    else:
        score += 5
        feedback.append("~ Prevention: Add validation rules (e.g., flag entries >$10K for review)")
    
    # Results
    print("\n" + "="*70)
    print("TROUBLESHOOTING SCORE")
    print("="*70)
    
    for fb in feedback:
        print(f"{fb}")
    
    print(f"\nTOTAL SCORE: {score}/100")
    
    if score >= 80:
        print("\n🎉 EXCELLENT troubleshooting! You'd handle customer issues well.")
    elif score >= 60:
        print("\n✓ DECENT troubleshooting. Build more systematic approach.")
    else:
        print("\n📚 NEEDS WORK. Practice systematic debugging.")
    
    print("\n" + "="*70)
    print("IDEAL TROUBLESHOOTING APPROACH:")
    print("="*70)
    print("""
1. STOP THE BLEEDING:
   - Disable agent immediately (prevent more bad entries)
   - Reverse incorrect entries already posted

2. DIAGNOSE ROOT CAUSE:
   - Review agent config (filter rules, data mapping)
   - Check source data (is Coupa data correct?)
   - Test with sample: Run agent on single PO manually

3. FIX THE ISSUE:
   - Amount error: Field mapping wrong (quantity vs amount)
   - Filter error: Status filter not excluding "Invoiced"
   
4. TEST THE FIX:
   - Run on historical data (last 2 months)
   - Compare to manual entries (should match)
   
5. PREVENT RECURRENCE:
   - Add validation: Flag entries >$10K for review
   - Add validation: Check if already invoiced before accruing
   - Schedule monthly check-in with customer

6. COMMUNICATE:
   - Explain to customer what happened and why
   - Show them the fix and validation steps
   - Document for future reference
""")
    
    return score >= 60


def main():
    print("\n" + "="*70)
    print("DAY 2: HANDS-ON AGENT CONFIGURATION PRACTICE")
    print("="*70)
    
    print("""
Real practice - YOU make decisions, AI scores your choices.

Available Exercises:
  1 - Configure Coupa Accrual Agent (Manufacturing)
  2 - Troubleshoot Broken Agent
  Q - Quit
""")
    
    while True:
        try:
            choice = input("\nChoose exercise (1-2, Q to quit): ").strip()
            
            if choice.lower() == 'q':
                print("\nGreat practice! You're learning by doing.")
                break
            
            elif choice == '1':
                scenario_manufacturing()
                input("\nPress Enter to continue...")
            
            elif choice == '2':
                scenario_troubleshooting()
                input("\nPress Enter to continue...")
            
            else:
                print("Invalid choice. Enter 1, 2, or Q.")
                
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except EOFError:
            # Non-interactive demo mode
            print("\nRunning Exercise 1 in demo mode...")
            scenario_manufacturing()
            print("\n\nRunning Exercise 2 in demo mode...")
            scenario_troubleshooting()
            break


if __name__ == "__main__":
    main()



