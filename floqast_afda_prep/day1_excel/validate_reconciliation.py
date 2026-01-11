"""
Bank Reconciliation Validator - AI-Style Feedback
Checks if you correctly matched transactions and identified reconciling items
"""

import openpyxl
import sys
from datetime import datetime

class ReconciliationValidator:
    def __init__(self, workbook_path):
        try:
            self.wb = openpyxl.load_workbook(workbook_path)
        except FileNotFoundError:
            print(f"❌ Error: Could not find {workbook_path}")
            sys.exit(1)
        
        self.score = 0
        self.max_score = 0
    
    def validate(self):
        print("\n" + "="*80)
        print("BANK RECONCILIATION VALIDATION")
        print("="*80)
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        try:
            ws_recon = self.wb["Reconciliation Worksheet"]
        except KeyError:
            print("❌ Could not find 'Reconciliation Worksheet' sheet")
            return
        
        # Expected correct matches
        expected_matches = {
            'GL-1001': ('BNK-A001', 'MATCHED'),
            'GL-1002': ('BNK-A002', 'MATCHED'),  # Date differs by 1 day but amounts match
            'GL-1003': ('BNK-A003', 'MATCHED'),
            'GL-1004': ('BNK-A004', 'MATCHED'),
            'GL-1005': ('BNK-A005', 'MATCHED'),
            'GL-1006': ('BNK-A006', 'MATCHED'),  # Date differs but amounts match
            'GL-1007': (None, 'OC'),  # Outstanding check (not on bank statement)
            'GL-1008': (None, 'DIT'),  # Deposit in transit
            'GL-1009': (None, 'DIT'),  # Deposit in transit
        }
        
        print("Checking your reconciliation...\n")
        print(f"{'GL ID':<12} {'Your Match':<12} {'Status':<15} {'Correct?':<10}")
        print("-"*60)
        
        correct_matches = 0
        total_items = len(expected_matches)
        
        # Check each GL transaction (rows 14-22)
        for row in range(14, 23):
            gl_id = ws_recon[f'A{row}'].value
            if not gl_id:
                continue
            
            bank_id = ws_recon[f'E{row}'].value
            status = ws_recon[f'G{row}'].value
            
            # Clean up values
            if bank_id and isinstance(bank_id, str):
                bank_id = bank_id.strip().replace('[Fill bank ID]', '').strip()
                if not bank_id:
                    bank_id = None
            
            if status and isinstance(status, str):
                status = status.strip().replace('[MATCHED/DIT/OC]', '').strip().upper()
                if not status:
                    status = None
            
            expected_bank, expected_status = expected_matches.get(gl_id, (None, None))
            
            # Check if correct
            is_correct = False
            if expected_status == 'MATCHED':
                if bank_id == expected_bank and status == 'MATCHED':
                    is_correct = True
            else:  # DIT or OC
                if status == expected_status:
                    is_correct = True
            
            check_mark = "CORRECT" if is_correct else "INCORRECT"
            if is_correct:
                correct_matches += 1
            
            bank_display = bank_id if bank_id else "---"
            status_display = status if status else "NOT FILLED"
            
            print(f"{gl_id:<12} {bank_display:<12} {status_display:<15} {check_mark:<10}")
        
        print("-"*60)
        score = int(correct_matches / total_items * 100)
        print(f"MATCHES CORRECT: {correct_matches}/{total_items} ({score}%)\n")
        
        # Detailed feedback
        print("="*80)
        print("DETAILED FEEDBACK")
        print("="*80)
        
        # Expected results
        print("\nEXPECTED RESULTS:")
        print("  - GL-1001 -> BNK-A001: MATCHED (exact match)")
        print("  - GL-1002 -> BNK-A002: MATCHED (1-day date difference, but amount matches)")
        print("  - GL-1003 -> BNK-A003: MATCHED (exact match)")
        print("  - GL-1004 -> BNK-A004: MATCHED (exact match)")
        print("  - GL-1005 -> BNK-A005: MATCHED (exact match)")
        print("  - GL-1006 -> BNK-A006: MATCHED (date differs but amount matches)")
        print("  - GL-1007: OC (Outstanding Check - $5,000 insurance, not cleared bank yet)")
        print("  - GL-1008: DIT (Deposit in Transit - $8,500, deposited 12/29, not on bank yet)")
        print("  - GL-1009: DIT (Deposit in Transit - $12,000, deposited 12/30, not on bank yet)")
        
        print("\nKEY CONCEPTS:")
        print("  - MATCHED: Transaction appears on both GL and bank statement")
        print("  - DIT (Deposit in Transit): In GL but not on bank yet (end-of-month timing)")
        print("  - OC (Outstanding Check): Written but not cashed yet")
        print("  - Fuzzy matching: Dates may differ by 1-2 days due to processing time")
        
        # Bank charge
        print("\nBANK CHARGES:")
        print("  - BNK-A007: Bank service charge $25 on 12/15")
        print("  - This appears on bank statement but NOT in GL")
        print("  - You'd need to record a journal entry to account for this")
        
        # Interview tips
        print("\n" + "="*80)
        print("INTERVIEW TIP - How to explain reconciliation:")
        print("="*80)
        print('"I perform bank reconciliations by matching GL cash transactions to bank')
        print('statements. I look for exact matches first, then fuzzy matches where dates')
        print('differ by 1-2 days due to processing time. I identify deposits in transit')
        print('(recorded in GL but not on bank yet) and outstanding checks (issued but')
        print('not cashed). I also look for bank charges not recorded in the GL, which')
        print('require a journal entry. This is similar to how FloQast\'s AutoRec product')
        print('automates matching using configurable rules."')
        
        print("\n" + "="*80)
        if score >= 80:
            print("EXCELLENT! You understand reconciliation mechanics.")
            print("   Next: Open variance_analysis.xlsx for P&L variance practice")
        elif score >= 60:
            print("GOOD WORK! Review any incorrect items and try again.")
        else:
            print("KEEP PRACTICING! Review reconciliation concepts.")
        print("="*80)

def main():
    if len(sys.argv) < 2:
        print("Usage: py validate_reconciliation.py bank_reconciliation.xlsx")
        sys.exit(1)
    
    workbook_path = sys.argv[1]
    validator = ReconciliationValidator(workbook_path)
    validator.validate()

if __name__ == "__main__":
    main()



