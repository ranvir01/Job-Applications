# -*- coding: utf-8 -*-
"""
Day 1 Afternoon: Bank Reconciliation Practice
Your Experience + FloQast Interview Prep

Based on YOUR real experience from:
- Thind Transport: Cash reconciliations, month-end close
- Consulting: Client financial controls, process improvement

Run this script: py reconciliation_bootcamp.py
"""

import sys
from datetime import datetime

# ============================================================================
# RECONCILIATION GAME
# ============================================================================

class ReconciliationGame:
    def __init__(self, scenario_num):
        self.scenario_num = scenario_num
        self.scenario_name = ""
        self.your_experience = ""
        self.gl_transactions = []
        self.bank_transactions = []
        self.matches = []
        self.deposits_in_transit = []
        self.outstanding_checks = []
        self.expected_matches = []
        self.expected_dit = []
        self.expected_oc = []
        self.setup_scenario()
        
    def setup_scenario(self):
        """Generate scenario data based on your experience"""
        if self.scenario_num == 1:
            self.scenario_name = "Thind Transport - Basic Cash Reconciliation"
            self.your_experience = "Month-end close, matching customer receipts to bank deposits"
            
            self.gl_transactions = [
                {"id": "GL001", "date": "12/05", "desc": "Customer Payment - ABC Freight", "amount": 15000},
                {"id": "GL002", "date": "12/08", "desc": "Fuel Purchase - Express Gas", "amount": -850},
                {"id": "GL003", "date": "12/12", "desc": "Customer Payment - XYZ Logistics", "amount": 22000},
                {"id": "GL004", "date": "12/15", "desc": "Office Supplies - Depot", "amount": -450},
                {"id": "GL005", "date": "12/20", "desc": "Customer Payment - Smith Co", "amount": 18500},
            ]
            self.bank_transactions = [
                {"id": "BNK001", "date": "12/05", "desc": "Deposit", "amount": 15000},
                {"id": "BNK002", "date": "12/08", "desc": "Debit Card", "amount": -850},
                {"id": "BNK003", "date": "12/12", "desc": "Deposit", "amount": 22000},
                {"id": "BNK004", "date": "12/15", "desc": "Debit Card", "amount": -450},
                {"id": "BNK005", "date": "12/20", "desc": "Deposit", "amount": 18500},
            ]
            self.expected_matches = [
                ("GL001", "BNK001"), ("GL002", "BNK002"), ("GL003", "BNK003"),
                ("GL004", "BNK004"), ("GL005", "BNK005")
            ]
            self.expected_dit = []
            self.expected_oc = []
            
        elif self.scenario_num == 2:
            self.scenario_name = "Fuzzy Matching + Outstanding Check"
            self.your_experience = "Date tolerance matching - bank processes 1-2 days after GL entry"
            
            self.gl_transactions = [
                {"id": "GL001", "date": "12/05", "desc": "Customer Payment", "amount": 15000},
                {"id": "GL002", "date": "12/08", "desc": "Fuel Purchase", "amount": -850},
                {"id": "GL003", "date": "12/12", "desc": "Customer Payment", "amount": 22000},
                {"id": "GL004", "date": "12/28", "desc": "Check #1055 - Insurance", "amount": -3200},
            ]
            self.bank_transactions = [
                {"id": "BNK001", "date": "12/05", "desc": "Deposit", "amount": 15000},
                {"id": "BNK002", "date": "12/09", "desc": "Debit", "amount": -850},  # 1 day late
                {"id": "BNK003", "date": "12/13", "desc": "Deposit", "amount": 22000},  # 1 day late
                # Check #1055 not on bank yet = Outstanding Check
            ]
            self.expected_matches = [
                ("GL001", "BNK001"), ("GL002", "BNK002"), ("GL003", "BNK003")
            ]
            self.expected_dit = []
            self.expected_oc = ["GL004"]
            
        elif self.scenario_num == 3:
            self.scenario_name = "Deposits in Transit + Bank Charges"
            self.your_experience = "Month-end timing differences - deposits recorded but not processed"
            
            self.gl_transactions = [
                {"id": "GL001", "date": "12/05", "desc": "Customer Payment", "amount": 15000},
                {"id": "GL002", "date": "12/29", "desc": "Customer Payment - Late Dec", "amount": 8500},
                {"id": "GL003", "date": "12/30", "desc": "Customer Payment - Year End", "amount": 12000},
            ]
            self.bank_transactions = [
                {"id": "BNK001", "date": "12/05", "desc": "Deposit", "amount": 15000},
                {"id": "BNK002", "date": "12/15", "desc": "Service Charge", "amount": -25},
                # 12/29 and 12/30 deposits not on bank yet = DITs
            ]
            self.expected_matches = [("GL001", "BNK001")]
            self.expected_dit = ["GL002", "GL003"]
            self.expected_oc = []
            
        elif self.scenario_num == 4:
            self.scenario_name = "Consulting Client - Complex Reconciliation"
            self.your_experience = "Client process improvement - identified control gaps"
            
            self.gl_transactions = [
                {"id": "GL001", "date": "12/02", "desc": "Client Project Payment", "amount": 25000},
                {"id": "GL002", "date": "12/10", "desc": "Software Subscription", "amount": -1200},
                {"id": "GL003", "date": "12/15", "desc": "Client Retainer", "amount": 10000},
                {"id": "GL004", "date": "12/28", "desc": "Contractor Payment", "amount": -5000},
                {"id": "GL005", "date": "12/30", "desc": "Project Milestone", "amount": 15000},
            ]
            self.bank_transactions = [
                {"id": "BNK001", "date": "12/02", "desc": "Wire Transfer", "amount": 25000},
                {"id": "BNK002", "date": "12/11", "desc": "ACH Debit", "amount": -1200},
                {"id": "BNK003", "date": "12/16", "desc": "Wire Transfer", "amount": 10000},
                {"id": "BNK004", "date": "12/20", "desc": "Service Fee", "amount": -50},
            ]
            self.expected_matches = [
                ("GL001", "BNK001"), ("GL002", "BNK002"), ("GL003", "BNK003")
            ]
            self.expected_dit = ["GL005"]
            self.expected_oc = ["GL004"]
    
    def display_transactions(self):
        """Show GL and Bank transactions"""
        print("\n" + "=" * 80)
        print(f"SCENARIO {self.scenario_num}: {self.scenario_name}")
        print(f"Your Experience: {self.your_experience}")
        print("=" * 80)
        
        print("\nGENERAL LEDGER - Cash Account (Your Books):")
        print(f"{'ID':<8} {'Date':<10} {'Description':<35} {'Amount':>12}")
        print("-" * 80)
        for txn in self.gl_transactions:
            if txn['amount'] >= 0:
                amt_str = f"${txn['amount']:>10,.2f}"
            else:
                amt_str = f"(${abs(txn['amount']):>9,.2f})"
            print(f"{txn['id']:<8} {txn['date']:<10} {txn['desc']:<35} {amt_str:>12}")
        
        print("\nBANK STATEMENT (What the bank shows):")
        print(f"{'ID':<8} {'Date':<10} {'Description':<35} {'Amount':>12}")
        print("-" * 80)
        for txn in self.bank_transactions:
            if txn['amount'] >= 0:
                amt_str = f"${txn['amount']:>10,.2f}"
            else:
                amt_str = f"(${abs(txn['amount']):>9,.2f})"
            print(f"{txn['id']:<8} {txn['date']:<10} {txn['desc']:<35} {amt_str:>12}")
        
        print("\n" + "=" * 80)
        
    def get_transaction(self, txn_id, source):
        txns = self.gl_transactions if source == "GL" else self.bank_transactions
        for txn in txns:
            if txn['id'] == txn_id:
                return txn
        return None
    
    def process_match(self, gl_id, bank_id):
        gl_txn = self.get_transaction(gl_id, "GL")
        bank_txn = self.get_transaction(bank_id, "BANK")
        
        if not gl_txn:
            return f"ERROR: {gl_id} not found in GL"
        if not bank_txn:
            return f"ERROR: {bank_id} not found in Bank Statement"
        
        if abs(gl_txn['amount']) != abs(bank_txn['amount']):
            return f"ERROR: Amounts don't match! GL={gl_txn['amount']}, Bank={bank_txn['amount']}"
        
        if (gl_id, bank_id) in self.matches:
            return "Already matched!"
        
        self.matches.append((gl_id, bank_id))
        
        gl_date = datetime.strptime(f"2024/{gl_txn['date']}", "%Y/%m/%d")
        bank_date = datetime.strptime(f"2024/{bank_txn['date']}", "%Y/%m/%d")
        date_diff = abs((gl_date - bank_date).days)
        
        if date_diff == 0:
            return "CORRECT! Exact match - same amount, same date."
        elif date_diff <= 3:
            return f"GOOD! Fuzzy match ({date_diff} day difference). FloQast AutoRec would configure +/- 3 day tolerance."
        else:
            return f"MATCHED but {date_diff} days apart - verify this is correct."
    
    def evaluate(self):
        print("\n" + "=" * 80)
        print("EVALUATING YOUR RECONCILIATION...")
        print("=" * 80)
        
        score = 0
        max_score = len(self.expected_matches) + len(self.expected_dit) + len(self.expected_oc)
        
        print("\nMATCHED TRANSACTIONS:")
        for expected in self.expected_matches:
            if expected in self.matches:
                print(f"  [OK] {expected[0]} <-> {expected[1]}")
                score += 1
            else:
                print(f"  [MISSED] {expected[0]} <-> {expected[1]}")
        
        if self.expected_dit:
            print("\nDEPOSITS IN TRANSIT (in GL, not yet on bank):")
            for gl_id in self.expected_dit:
                if gl_id in self.deposits_in_transit:
                    print(f"  [OK] {gl_id}")
                    score += 1
                else:
                    print(f"  [MISSED] {gl_id}")
        
        if self.expected_oc:
            print("\nOUTSTANDING CHECKS (in GL, not yet cleared bank):")
            for gl_id in self.expected_oc:
                if gl_id in self.outstanding_checks:
                    print(f"  [OK] {gl_id}")
                    score += 1
                else:
                    print(f"  [MISSED] {gl_id}")
        
        # Check for bank charges not in GL
        bank_only = []
        for btxn in self.bank_transactions:
            matched = any(btxn['id'] == m[1] for m in self.matches)
            if not matched and "Service" in btxn['desc'] or "Fee" in btxn['desc'] or "Charge" in btxn['desc']:
                bank_only.append(btxn)
        
        if bank_only:
            print("\nBANK CHARGES (on bank, not in GL - need journal entry):")
            for txn in bank_only:
                print(f"  [NOTE] {txn['id']}: {txn['desc']} ${txn['amount']}")
        
        print("\n" + "=" * 80)
        pct = int(score / max_score * 100) if max_score > 0 else 0
        print(f"SCORE: {score}/{max_score} ({pct}%)")
        
        if score == max_score:
            print("\nPERFECT! You've mastered this reconciliation.")
            self.show_interview_tip()
            return True
        elif pct >= 70:
            print("\nGood work! Review missed items and try again.")
            return False
        else:
            print("\nKeep practicing! Remember:")
            print("  - DIT: Money recorded in GL but bank hasn't processed yet")
            print("  - OC: Check written in GL but recipient hasn't cashed it")
            return False
    
    def show_interview_tip(self):
        print("\n" + "=" * 80)
        print("INTERVIEW TALKING POINT")
        print("=" * 80)
        
        if self.scenario_num == 1:
            print("""
Question: "Walk me through a bank reconciliation"

Your Answer:
"I start with two columns - GL cash balance and bank statement balance. 
I match each GL transaction to its bank counterpart by amount and date.
For exact matches, I mark them as reconciled. The goal is to identify
and explain any differences between what we recorded and what the bank shows.
At Thind Transport, I did this monthly as part of the close process."

FloQast Connection: This is what AutoRec automates - rule-based matching 
with configurable tolerances. 38% faster reconciliations.""")
            
        elif self.scenario_num == 2:
            print("""
Question: "How do you handle date differences in reconciliations?"

Your Answer:
"Date differences are common - the bank might process a transaction 1-2 days
after we record it. I use a tolerance window, typically +/- 3 days. If amounts
match and dates are within tolerance, it's a valid match. Outstanding checks
are transactions we recorded but the recipient hasn't cashed yet."

FloQast Connection: AutoRec allows configuring date tolerance rules. 
You'd help customers set appropriate windows for their business.""")
            
        elif self.scenario_num == 3:
            print("""
Question: "What are deposits in transit and why do they matter?"

Your Answer:
"Deposits in transit are amounts we recorded in our books but the bank hasn't
processed yet - common at month-end when we deposit on 12/30 but bank doesn't
show it until January. They're reconciling items that explain why GL and bank
balances differ. Not errors - just timing differences."

FloQast Connection: AutoRec identifies DITs automatically based on date 
patterns, reducing manual investigation time.""")
            
        elif self.scenario_num == 4:
            print("""
Question: "Tell me about your consulting experience with reconciliations"

Your Answer:
"In my consulting work, I helped clients improve their reconciliation processes.
I identified gaps like missing bank charges not recorded in GL, timing differences
from outstanding payments, and process bottlenecks. I recommended automation
solutions and documentation improvements - similar to what FloQast delivers."

FloQast Connection: As an AFDA, you'd assess customer processes, configure 
AutoRec rules, and train teams on best practices - exactly this experience.""")
    
    def play(self):
        self.display_transactions()
        
        print("\nYOUR TASK - Reconcile GL to Bank Statement:")
        print("  match GL001 BNK001  - Match transactions by ID")
        print("  dit GL002           - Mark as Deposit In Transit")
        print("  oc GL003            - Mark as Outstanding Check")
        print("  show                - Display transactions again")
        print("  done                - Finish and get scored")
        print("  help                - Show all commands\n")
        
        while True:
            try:
                command = input("YOU: ").strip().lower()
                
                if command == 'done':
                    return self.evaluate()
                
                elif command == 'help':
                    print("\nCOMMANDS:")
                    print("  match GL001 BNK001  - Match GL and Bank transactions")
                    print("  dit GL002           - Mark as Deposit In Transit")
                    print("  oc GL003            - Mark as Outstanding Check")
                    print("  show                - Show transactions again")
                    print("  done                - Finish and check your work")
                    print("\nRECONCILING ITEMS:")
                    print("  DIT = Deposit in Transit (in GL, not yet on bank)")
                    print("  OC  = Outstanding Check (in GL, not yet cleared)")
                    
                elif command == 'show':
                    self.display_transactions()
                    
                elif command.startswith('match '):
                    parts = command.split()
                    if len(parts) != 3:
                        print("Usage: match GL001 BNK001")
                    else:
                        result = self.process_match(parts[1].upper(), parts[2].upper())
                        print(result)
                        
                elif command.startswith('dit '):
                    parts = command.split()
                    if len(parts) != 2:
                        print("Usage: dit GL002")
                    else:
                        gl_id = parts[1].upper()
                        if gl_id in self.deposits_in_transit:
                            print("Already marked as DIT")
                        else:
                            self.deposits_in_transit.append(gl_id)
                            print(f"Marked {gl_id} as Deposit In Transit")
                            print("  -> This means: Money recorded in GL but bank hasn't processed yet")
                            
                elif command.startswith('oc '):
                    parts = command.split()
                    if len(parts) != 2:
                        print("Usage: oc GL003")
                    else:
                        gl_id = parts[1].upper()
                        if gl_id in self.outstanding_checks:
                            print("Already marked as OC")
                        else:
                            self.outstanding_checks.append(gl_id)
                            print(f"Marked {gl_id} as Outstanding Check")
                            print("  -> This means: Check written but recipient hasn't cashed it")
                            
                else:
                    print("Unknown command. Type 'help' for options.")
                    
            except KeyboardInterrupt:
                print("\n\nExiting...")
                sys.exit(0)
            except Exception as e:
                print(f"Error: {e}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("\n" + "=" * 80)
    print("DAY 1: BANK RECONCILIATION PRACTICE")
    print("Your Experience + FloQast Interview Prep")
    print("=" * 80)
    
    print("""
Your experience sources:
  - Thind Transport: Monthly cash reconciliations, month-end close
  - Consulting: Client process improvement, financial controls

Available Scenarios:
  1 - EASY: Thind Transport basic matching (5 transactions)
  2 - MEDIUM: Fuzzy dates + outstanding check
  3 - HARD: Deposits in transit + bank charges
  4 - CONSULTING: Complex client reconciliation
""")
    print("=" * 80)
    
    while True:
        try:
            choice = input("\nChoose scenario (1-4), or 'q' to quit: ").strip()
            
            if choice.lower() == 'q':
                print("\n" + "=" * 80)
                print("RECONCILIATION SUMMARY")
                print("=" * 80)
                print("""
Key Concepts You Practiced:
  - Matching GL to bank by amount and date
  - Fuzzy matching with date tolerances
  - Deposits in Transit (DIT)
  - Outstanding Checks (OC)
  - Bank charges not in GL

Interview Answer Framework:
  "I reconcile by matching GL cash to bank statement, identifying:
   1. Exact matches (same amount, same date)
   2. Fuzzy matches (amount matches, date within tolerance)
   3. DITs - deposits we recorded but bank hasn't processed
   4. OCs - checks we wrote but recipients haven't cashed
   5. Bank charges we need to record in GL
   
   This is exactly what FloQast AutoRec automates with configurable rules."

FloQast Connection:
  - AutoRec: Automated reconciliations with rule-based matching
  - 38% faster reconciliations for customers
  - Your job: Configure matching rules for each customer's needs

Next: Continue to Day 2 for AI Agent configuration practice!
""")
                break
                
            scenario_num = int(choice)
            if scenario_num not in [1, 2, 3, 4]:
                print("Please choose 1, 2, 3, or 4")
                continue
                
            game = ReconciliationGame(scenario_num)
            passed = game.play()
            
            if passed:
                print(f"\nScenario {scenario_num} complete!")
                if scenario_num < 4:
                    print(f"Try scenario {scenario_num + 1} next for more challenge!")
            else:
                print(f"\nTry scenario {scenario_num} again, or move to the next one.")
                
        except ValueError:
            print("Please enter a number 1-4")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break


if __name__ == "__main__":
    main()
