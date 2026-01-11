# -*- coding: utf-8 -*-
"""
Day 1: Journal Entry Practice Lab
Your Experience + FloQast Interview Prep

Based on YOUR real experience from:
- Thind Transport: Month-end close, accruals, reconciliations
- Consulting Work: Client financial modeling, process improvement, Salesforce automation

Run this script: py journal_entry_practice.py
"""

from datetime import datetime
import sys

# ============================================================================
# SETUP
# ============================================================================

class JournalEntry:
    def __init__(self, entry_id, date, description, context=""):
        self.entry_id = entry_id
        self.date = date
        self.description = description
        self.context = context
        self.lines = []
    
    def add_line(self, account, debit=0.0, credit=0.0):
        self.lines.append({'account': account, 'debit': debit, 'credit': credit})
    
    def validate(self):
        total_debits = sum(line['debit'] for line in self.lines)
        total_credits = sum(line['credit'] for line in self.lines)
        return abs(total_debits - total_credits) < 0.01
    
    def display(self):
        print("=" * 70)
        print(f"Entry: {self.entry_id} | {self.description}")
        print(f"Date: {self.date.strftime('%Y-%m-%d')}")
        if self.context:
            print(f"Your Experience: {self.context}")
        print("=" * 70)
        print(f"{'Account':<40} {'Debit':>12} {'Credit':>12}")
        print("-" * 70)
        
        total_dr, total_cr = 0, 0
        for line in self.lines:
            dr = f"${line['debit']:,.2f}" if line['debit'] else ""
            cr = f"${line['credit']:,.2f}" if line['credit'] else ""
            print(f"{line['account']:<40} {dr:>12} {cr:>12}")
            total_dr += line['debit']
            total_cr += line['credit']
        
        print("-" * 70)
        print(f"{'TOTALS':<40} ${total_dr:>10,.2f} ${total_cr:>10,.2f}")
        print("=" * 70)
        
        if self.validate():
            print("[BALANCED] Entry is correct!")
            return True
        else:
            print(f"[UNBALANCED] Debits ${total_dr:,.2f} != Credits ${total_cr:,.2f}")
            return False


def show_interview_tip(question, answer, floqast_connection):
    """Display interview talking point"""
    print("\n" + "=" * 70)
    print("INTERVIEW TALKING POINT")
    print("=" * 70)
    print(f"\nQ: {question}\n")
    print(f"Your Answer:\n{answer}\n")
    print(f"FloQast Connection: {floqast_connection}")
    print("=" * 70)


# ============================================================================
# EXERCISES
# ============================================================================

def exercise_1_maintenance_accrual():
    """Thind Transport: Fleet Maintenance Accrual"""
    print("\n" + "#" * 70)
    print("EXERCISE 1: Fleet Maintenance Accrual (Thind Transport)")
    print("#" * 70)
    
    print("""
SCENARIO: December 31st at Thind Transport. Fleet maintenance was completed 
for $12,500, but the invoice won't arrive until January.

ACCOUNTING LOGIC:
- Expense happened in December (matching principle)
- We owe the vendor but haven't been billed
- Must accrue to show accurate December financials

ENTRY STRUCTURE:
- Debit: Expense account (increases expense)
- Credit: Liability account (we owe money)
""")
    
    je = JournalEntry(
        entry_id="JE-MAINT-001",
        date=datetime(2024, 12, 31),
        description="Fleet maintenance accrual - December services",
        context="Thind Transport month-end close"
    )
    
    je.add_line(account="Maintenance Expense", debit=12500, credit=0)
    je.add_line(account="Accrued Liabilities", debit=0, credit=12500)
    
    result = je.display()
    
    show_interview_tip(
        question="Walk me through a journal entry you've created",
        answer='"At Thind Transport, I handled month-end accruals. For example, when we had fleet maintenance done in December for $12,500 but the invoice came in January, I created an accrual entry: Debit Maintenance Expense to recognize the December expense, Credit Accrued Liabilities to record what we owe. This ensures our December financials match the services received that month."',
        floqast_connection="Transform AI Agents can automate these accrual entries by pulling from procurement systems like Coupa."
    )
    
    return result


def exercise_2_revenue_recognition():
    """Consulting: Revenue Recognition"""
    print("\n" + "#" * 70)
    print("EXERCISE 2: Consulting Revenue Recognition (Your Consulting Work)")
    print("#" * 70)
    
    print("""
SCENARIO: Your consulting network delivered Phase 1 of a client project 
worth $25,000 in December. Client will be invoiced in January, but revenue 
should be recognized when earned.

ACCOUNTING LOGIC:
- Revenue is earned when service is delivered (not when billed)
- We have a right to receive payment = Asset (Accounts Receivable)
- Revenue increases with credits

THIS CONNECTS TO: Your financial modeling and client project work
""")
    
    je = JournalEntry(
        entry_id="JE-REV-001",
        date=datetime(2024, 12, 31),
        description="Consulting revenue - Phase 1 delivered",
        context="Consulting network client project"
    )
    
    je.add_line(account="Accounts Receivable", debit=25000, credit=0)
    je.add_line(account="Consulting Revenue", debit=0, credit=25000)
    
    result = je.display()
    
    show_interview_tip(
        question="Do you have experience with revenue recognition?",
        answer='"Yes, in my consulting work, I dealt with recognizing revenue when services were delivered versus when billed. For a $25,000 project phase completed in December but invoiced in January, I recognized the revenue in December by debiting Accounts Receivable and crediting Revenue. This aligns with ASC 606 principles."',
        floqast_connection="SaaS companies struggle with complex revenue recognition. FloQast helps companies get this right every close."
    )
    
    return result


def exercise_3_prepaid_software():
    """Prepaid Software Subscription"""
    print("\n" + "#" * 70)
    print("EXERCISE 3: Prepaid Software (CRM like Salesforce)")
    print("#" * 70)
    
    print("""
SCENARIO: Paid $12,000 for annual CRM software subscription. Now it's 
month-end - need to recognize 1 month of expense.

ACCOUNTING LOGIC:
- $12,000 / 12 months = $1,000/month
- Move $1,000 from Prepaid Asset to Expense
- Assets decrease with credits, expenses increase with debits

THIS CONNECTS TO: Your Salesforce automation experience (2,000+ accounts)
""")
    
    je = JournalEntry(
        entry_id="JE-PREP-001",
        date=datetime(2024, 12, 31),
        description="Monthly CRM subscription expense",
        context="Similar to Salesforce you automated"
    )
    
    je.add_line(account="Software Expense", debit=1000, credit=0)
    je.add_line(account="Prepaid Software", debit=0, credit=1000)
    
    result = je.display()
    
    show_interview_tip(
        question="How do you handle prepaid expenses?",
        answer='"I create monthly amortization schedules. For a $12,000 annual software subscription, that\'s $1,000 per month. Each month-end, I debit Software Expense and credit Prepaid Software. This ensures we recognize expense in the period consumed, not when cash was paid."',
        floqast_connection="These recurring entries are perfect for automation - same entry every month."
    )
    
    return result


def exercise_4_payroll():
    """Compound Payroll Entry"""
    print("\n" + "#" * 70)
    print("EXERCISE 4: Compound Payroll Entry (Thind Transport)")
    print("#" * 70)
    
    print("""
SCENARIO: December payroll at Thind Transport:
- Gross wages: $45,000
- Tax withholdings: $6,800
- Benefits: $2,200  
- Net pay to employees: $36,000

ACCOUNTING LOGIC:
- Gross wages = total expense (debit)
- Withholdings = liabilities we owe to IRS, insurance (credits)
- Net pay = cash paid to employees (credit)
- One debit, multiple credits - MUST balance!

CHECK: $45,000 = $6,800 + $2,200 + $36,000
""")
    
    je = JournalEntry(
        entry_id="JE-PAY-001",
        date=datetime(2024, 12, 31),
        description="December payroll",
        context="Thind Transport payroll processing"
    )
    
    je.add_line(account="Payroll Expense", debit=45000, credit=0)
    je.add_line(account="Payroll Taxes Payable", debit=0, credit=6800)
    je.add_line(account="Benefits Payable", debit=0, credit=2200)
    je.add_line(account="Cash", debit=0, credit=36000)
    
    result = je.display()
    
    show_interview_tip(
        question="Have you worked with compound journal entries?",
        answer='"Yes, payroll is a great example. At Thind Transport, our December payroll had $45,000 gross wages, but we withheld $6,800 for taxes and $2,200 for benefits, paying employees $36,000 net. The entry was: Debit Payroll Expense $45,000, Credit Taxes Payable $6,800, Credit Benefits Payable $2,200, Credit Cash $36,000. It balances because gross expense equals all credits combined."',
        floqast_connection="Complex entries with multiple lines are where automation really shines."
    )
    
    return result


def exercise_5_automation_parallel():
    """Your VBA Automation Story"""
    print("\n" + "#" * 70)
    print("EXERCISE 5: Automation Parallel (Your VBA Experience)")
    print("#" * 70)
    
    print("""
YOUR STORY: At Thind Transport, you automated monthly reporting with VBA,
reducing the process from 8 hours to 1.5 hours - 80% time savings!

This is the SAME concept as FloQast Transform AI Agents:
- Identify repetitive manual process
- Define the rules/logic
- Automate execution
- Human reviews output

Let's see what entries you automated:
""")
    
    # Create multiple recurring entries that would be automated
    entries = []
    
    # Monthly depreciation
    depr = JournalEntry("JE-DEPR-001", datetime(2024,12,31), 
                        "Monthly depreciation", "Automated with VBA")
    depr.add_line("Depreciation Expense", debit=4500, credit=0)
    depr.add_line("Accumulated Depreciation", debit=0, credit=4500)
    entries.append(depr)
    
    # Monthly insurance
    ins = JournalEntry("JE-INS-001", datetime(2024,12,31), 
                       "Monthly insurance from prepaid", "Automated with VBA")
    ins.add_line("Insurance Expense", debit=1200, credit=0)
    ins.add_line("Prepaid Insurance", debit=0, credit=1200)
    entries.append(ins)
    
    # Monthly loan interest
    interest = JournalEntry("JE-INT-001", datetime(2024,12,31), 
                            "Monthly interest accrual", "Automated with VBA")
    interest.add_line("Interest Expense", debit=750, credit=0)
    interest.add_line("Interest Payable", debit=0, credit=750)
    entries.append(interest)
    
    passed = 0
    for entry in entries:
        if entry.display():
            passed += 1
        print()
    
    print(f"\nAutomated Entries: {passed}/{len(entries)} validated")
    print(f"Manual time before: 8 hours")
    print(f"Automated time: 1.5 hours")
    print(f"Time savings: 80%")
    
    show_interview_tip(
        question="Tell me about your automation experience",
        answer='"At Thind Transport, I automated monthly reporting with VBA, reducing the process from 8 hours to 1.5 hours - 80% time savings. I identified recurring entries like depreciation, prepaid amortization, and interest accruals that followed the same pattern every month. I built macros that generated these entries automatically, then I reviewed them before posting. This is exactly the approach FloQast uses with Transform AI Agents - automate the repetitive parts, human reviews the output."',
        floqast_connection="Your VBA automation experience directly translates to configuring Transform AI Agents for customers."
    )
    
    return passed == len(entries)


def exercise_6_full_month_close():
    """Complete Month-End Close"""
    print("\n" + "#" * 70)
    print("EXERCISE 6: Full Month-End Close (Thind Transport)")
    print("#" * 70)
    
    print("""
SCENARIO: You're closing December at Thind Transport.
Complete all month-end entries:

1. Fuel accrual: $8,200 (services received, invoice pending)
2. Depreciation: $4,500 (monthly fleet depreciation)
3. Insurance: $1,000 (from prepaid to expense)
4. Interest accrual: $750 (loan interest for December)

This is your complete month-end close simulation!
""")
    
    entries = []
    
    # Fuel accrual
    fuel = JournalEntry("JE-FUEL-001", datetime(2024,12,31), 
                        "Fuel accrual", "Thind Transport")
    fuel.add_line("Fuel Expense", debit=8200, credit=0)
    fuel.add_line("Accrued Liabilities", debit=0, credit=8200)
    entries.append(("Fuel Accrual", fuel))
    
    # Depreciation
    depr = JournalEntry("JE-DEPR-001", datetime(2024,12,31), 
                        "Monthly depreciation", "Thind Transport")
    depr.add_line("Depreciation Expense", debit=4500, credit=0)
    depr.add_line("Accumulated Depreciation", debit=0, credit=4500)
    entries.append(("Depreciation", depr))
    
    # Insurance
    ins = JournalEntry("JE-INS-001", datetime(2024,12,31), 
                       "Monthly insurance", "Thind Transport")
    ins.add_line("Insurance Expense", debit=1000, credit=0)
    ins.add_line("Prepaid Insurance", debit=0, credit=1000)
    entries.append(("Insurance", ins))
    
    # Interest
    interest = JournalEntry("JE-INT-001", datetime(2024,12,31), 
                            "Interest accrual", "Thind Transport")
    interest.add_line("Interest Expense", debit=750, credit=0)
    interest.add_line("Interest Payable", debit=0, credit=750)
    entries.append(("Interest", interest))
    
    passed = 0
    for name, entry in entries:
        print(f"\n--- {name} ---")
        if entry.display():
            passed += 1
    
    print("\n" + "=" * 70)
    print(f"MONTH-END CLOSE RESULT: {passed}/4 entries correct")
    print("=" * 70)
    
    if passed == 4:
        print("\nExcellent! Your December close is complete!")
        print("Total adjustments made:")
        print(f"  - Fuel Expense:        $8,200")
        print(f"  - Depreciation:        $4,500")
        print(f"  - Insurance Expense:   $1,000")
        print(f"  - Interest Expense:      $750")
        print(f"  - TOTAL ADJUSTMENTS:  $14,450")
    
    show_interview_tip(
        question="Walk me through your month-end close process",
        answer='"At Thind Transport, I supported the close with several key steps. Days 1-3 were accruals - fuel expenses, maintenance, anything we\'d received but not been billed for. Day 4-5 were standard entries like depreciation, which I automated with VBA saving 80% of time. Day 6 was prepaid amortization. Day 7 was variance analysis - comparing actuals to budget. Days 8-10 were review and adjustments. I also automated Salesforce reporting for 2,000+ customer accounts, so I understand how automation transforms accounting workflows."',
        floqast_connection="FloQast's Close product manages this entire workflow. Transform AI automates recurring entries. AutoRec handles reconciliations. Flux does variance analysis."
    )
    
    return passed == 4


# ============================================================================
# MAIN MENU
# ============================================================================

def main():
    print("\n" + "=" * 70)
    print("DAY 1: JOURNAL ENTRY PRACTICE LAB")
    print("Your Experience + FloQast Interview Prep")
    print("=" * 70)
    
    print("""
Your experience sources:
  - Thind Transport: Month-end close, accruals, 80% VBA automation
  - Consulting: Financial modeling, client projects, Salesforce (2,000+ accounts)
  - Technical: VBA, Python, SQL, AI tools

Available Exercises:
  1 - Fleet Maintenance Accrual (Thind Transport)
  2 - Revenue Recognition (Consulting Experience)
  3 - Prepaid Software (CRM like Salesforce)
  4 - Compound Payroll Entry (Thind Transport)
  5 - Your VBA Automation Story
  6 - Full Month-End Close Simulation
  A - Run ALL exercises
  Q - Quit
""")
    
    exercises = {
        '1': exercise_1_maintenance_accrual,
        '2': exercise_2_revenue_recognition,
        '3': exercise_3_prepaid_software,
        '4': exercise_4_payroll,
        '5': exercise_5_automation_parallel,
        '6': exercise_6_full_month_close,
    }
    
    while True:
        try:
            choice = input("\nChoose exercise (1-6, A for all, Q to quit): ").strip().upper()
            
            if choice == 'Q':
                print("\nGreat practice! Remember:")
                print("- You can explain any of these entries in your interview")
                print("- Connect each to your Thind Transport or consulting experience")
                print("- Tie to FloQast products: Transform AI, Close, AutoRec, Flux")
                print("\nNext: Run reconciliation_bootcamp.py for bank reconciliation practice!")
                break
            
            elif choice == 'A':
                print("\nRunning all exercises...")
                passed = 0
                for key in ['1', '2', '3', '4', '5', '6']:
                    if exercises[key]():
                        passed += 1
                    input("\nPress Enter to continue to next exercise...")
                
                print("\n" + "=" * 70)
                print(f"FINAL SCORE: {passed}/6 exercises completed successfully")
                print("=" * 70)
                
                if passed == 6:
                    print("\nPERFECT! You're ready to explain journal entries in any interview!")
            
            elif choice in exercises:
                exercises[choice]()
            
            else:
                print("Invalid choice. Enter 1-6, A, or Q.")
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except EOFError:
            # Non-interactive mode - run all exercises
            print("\nRunning all exercises (non-interactive mode)...")
            for key in ['1', '2', '3', '4', '5', '6']:
                exercises[key]()
            break


if __name__ == "__main__":
    main()



