# Day 1: Excel-Based Accounting Practice

**Welcome to REAL accounting work!** Today you'll use Excel - the tool accountants actually use - not Python notebooks.

---

## What You'll Do Today

### Morning (2-3 hours): Journal Entries
Work in **`journal_entry_workbook.xlsx`**

### Afternoon (2-3 hours): Bank Reconciliation  
Work in **`bank_reconciliation.xlsx`**

### Optional: Variance Analysis
Work in **`variance_analysis.xlsx`**

---

## Morning Session: Journal Entry Workbook

### Step 1: Open the Workbook
```powershell
cd "d:\Job Applications\floqast_afda_prep\day1_excel"
start journal_entry_workbook.xlsx
```

### Step 2: Review the Chart of Accounts
- Open the **"Chart of Accounts"** sheet
- Familiarize yourself with account numbers and types
- This is your reference - keep it open in a second window

### Step 3: Complete Exercises

#### Exercise 1: Maintenance Accrual (GUIDED)
- Open sheet **"Exercise 1 - Maintenance"**
- Read the scenario: Fleet maintenance $12,500, invoice comes next month
- **Your task**: Fill in the journal entry form
  - Line 1: Pick the expense account number (Hint: 6100)
  - Enter debit amount: 12500
  - Line 2: Pick the liability account (Hint: 2100)
  - Enter credit amount: 12500
- Watch the Status field - it should say "✓ BALANCED"

#### Exercise 2: Prepaid Insurance
- Sheet **"Exercise 2 - Prepaid"**
- Scenario: Paid $6,000 for 6 months insurance, only 1 month used
- Calculate: $5,000 is prepaid (5 months remaining)
- Create the adjustment entry

#### Exercise 3: Debug Depreciation
- Sheet **"Exercise 3 - Debug"**
- This entry is BROKEN - find and fix it!
- Hint: Check if accounts have correct debit/credit sides

#### Exercise 4: Payroll
- Sheet **"Exercise 4 - Payroll"**
- Gross: $45,000, Taxes: $6,800, Benefits: $2,200, Net: $36,000
- Create 4-line compound entry

#### Exercise 5: Full Month-End
- Sheet **"Exercise 5 - Month End"**
- Create FOUR separate entries:
  1. Fuel accrual $8,200
  2. Depreciation $4,500
  3. Insurance expense $1,000
  4. Interest accrual $750

### Step 4: Validate Your Work
```powershell
py validate_journal_entries.py journal_entry_workbook.xlsx
```

You'll get:
- ✓ or ✗ for each exercise
- Specific feedback on errors
- Interview tips on how to explain your work

---

## Afternoon Session: Bank Reconciliation

### Step 1: Open the Workbook
```powershell
start bank_reconciliation.xlsx
```

### Step 2: Review the Data
- **Sheet: "GL Cash Transactions"** - Your book entries (9 transactions)
- **Sheet: "Bank Statement"** - What the bank shows (7 transactions)
- Notice: Some are missing! That's what you'll reconcile.

### Step 3: Complete Reconciliation
- Go to **"Reconciliation Worksheet"** sheet
- Your task:
  1. For each GL transaction, find matching bank transaction
  2. Fill in columns E (Bank ID), F (Bank Date), G (Match Status)
  3. Mark status as:
     - **MATCHED** - Found on both GL and bank
     - **DIT** - Deposit in Transit (in GL, not on bank yet)
     - **OC** - Outstanding Check (in GL, not cleared bank)
  
### Example:
```
GL-1001 (12/02, $15,000 receipt) → BNK-A001 (12/02, $15,000) → MATCHED
GL-1008 (12/29, $8,500 receipt) → Not on bank statement → DIT
```

### Step 4: Complete Reconciliation Summary
- Calculate total DITs
- Calculate total OCs  
- Calculate bank charges not recorded
- Verify adjusted bank balance matches GL

### Step 5: Validate
```powershell
py validate_reconciliation.py bank_reconciliation.xlsx
```

---

## Optional: Variance Analysis

### Step 1: Open the Workbook
```powershell
start variance_analysis.xlsx
```

### Step 2: Review P&L
- **Sheet: "Monthly P&L Data"** - December vs November
- Notice the formulas calculate variances automatically
- Identify material variances (>10% or >$5,000)

### Step 3: Explain Variances
- **Sheet: "Variance Analysis"** - Your workspace
- For each material variance, write explanation in column G
- Think about: Why did this change? Business reasons?

### Step 4: Compare to AI
- **Sheet: "Flux AI Simulation"** - See what FloQast's AI would generate
- This is what the Flux agent automates!

---

## Why This Matters for Your Interview

### When interviewer asks: "Walk me through a journal entry"

**You can say**:
> "At Thind Transport, I handled month-end accruals. For example, when we had fleet maintenance done in December for $12,500 but the invoice came in January, I'd create an accrual entry. I'd debit Maintenance Expense (6100) for $12,500 to recognize the December expense, and credit Accrued Liabilities (2100) for $12,500 to record what we owe. This ensures our December financials are accurate for the close."

### When interviewer asks: "How do you ensure accuracy?"

**You can say**:
> "First, I verify the entry is balanced - debits equal credits. Second, I check account classifications make sense - expenses are debits, liabilities are credits. Third, I validate against source documents. For example, in a bank rec, I match GL transactions to bank statements using both amounts and dates, identifying any deposits in transit or outstanding checks."

### When interviewer asks: "Have you used accounting software?"

**You can say**:
> "I've worked extensively in Excel for journal entries and reconciliations, which translates well to ERP systems since the underlying accounting logic is the same. I understand GL account structures, debit/credit mechanics, and reconciliation workflows. The interfaces differ, but the principles are universal."

---

## Tips for Success

1. **Take your time** - This is practice, not a race
2. **Use the Chart of Accounts** - Real accountants reference this constantly
3. **Check your balance** - Always verify debits = credits before moving on
4. **Think about the business** - Why does this transaction make sense?
5. **Run validation often** - Get feedback as you go, don't wait until the end

---

## Common Mistakes to Avoid

❌ **Wrong**: Crediting an expense account (expenses should be debits)  
✓ **Right**: Debit expense, credit liability for accruals

❌ **Wrong**: Forgetting to reverse accruals next month  
✓ **Right**: Accruals are temporary - they reverse when invoice arrives

❌ **Wrong**: Matching transactions with different amounts  
✓ **Right**: Amounts must match exactly (or within pennies for rounding)

---

## Next Steps

After completing Day 1:
1. ✓ You understand journal entry mechanics
2. ✓ You can perform reconciliations
3. ✓ You can explain variance analysis
4. → Ready for Day 2: Web-based ERP simulators

---

## Need Help?

- Check the **"Chart of Accounts"** sheet for account numbers
- Review **"JE Template"** sheet to see proper format
- Look at **"Flux AI Simulation"** for variance analysis examples
- Run validation scripts for immediate feedback

**Remember**: Real accountants use Excel like this every day. You're building transferable skills!



