# Alaska Airlines Treasury Financial Analyst - Practice Guide

**Purpose:** This guide helps you complete the Excel practice simulation and understand Treasury terminology for your Alaska Airlines interview.

---

## Table of Contents

1. [Exercise Solutions & Hints](#exercise-solutions--hints)
2. [Treasury Terminology Glossary](#treasury-terminology-glossary)
3. [Key Excel Functions for Treasury](#key-excel-functions-for-treasury)
4. [How to Talk About This in Interviews](#how-to-talk-about-this-in-interviews)
5. [Common Treasury Metrics](#common-treasury-metrics)
6. [Month-End Close Process](#month-end-close-process)

---

## Exercise Solutions & Hints

### Tab 1: Fleet & Lease Portfolio

**Goal:** Build a summary of monthly aircraft obligations

**Solution Approach:**

1. **Total Monthly Obligation (Column G):**
   ```excel
   =IF(E15<>"-", E15, F15)
   ```
   This formula says: "If there's a lease payment, use it; otherwise use the debt payment"

2. **Total Portfolio Payment:**
   ```excel
   =SUM(G15:G19)
   ```
   Should equal: $1,913,000/month

3. **Highest Cost Aircraft:**
   ```excel
   =MAX(G15:G19)
   ```
   Answer: AA-002 at $425,000/month

**Key Insight:** Operating leases and finance leases are treated differently accounting-wise, but both represent monthly cash obligations that Treasury must plan for.

---

### Tab 2: Debt Amortization Schedule

**Goal:** Build a complete 144-month amortization schedule

**Solution Approach:**

1. **Monthly Payment Calculation (Cell B21):**
   ```excel
   =PMT(B19, B18, -B15)
   ```
   - B19 = monthly interest rate (0.458%)
   - B18 = number of payments (144)
   - B15 = loan amount ($50,000,000) - use negative because it's money borrowed
   
   **Result:** $465,068.34/month

2. **Amortization Schedule (Starting Row 26):**

   **Payment # (A26):** 1, 2, 3... (just sequential numbers)
   
   **Payment Date (B26):** 
   ```excel
   =DATE(2021,7,1)  [First payment]
   =EDATE(B26, 1)   [Subsequent payments - adds 1 month]
   ```
   
   **Beginning Balance (C26):**
   ```excel
   =$B$15           [First row]
   =G26             [Subsequent rows - previous ending balance]
   ```
   
   **Monthly Payment (D26):**
   ```excel
   =$B$21           [Lock to calculated payment]
   ```
   
   **Interest Paid (E26):**
   ```excel
   =IPMT($B$19, A26, $B$18, -$B$15)
   ```
   Or simpler:
   ```excel
   =C26 * $B$19     [Beginning Balance times monthly rate]
   ```
   
   **Principal Paid (F26):**
   ```excel
   =PPMT($B$19, A26, $B$18, -$B$15)
   ```
   Or simpler:
   ```excel
   =D26 - E26       [Payment minus interest]
   ```
   
   **Ending Balance (G26):**
   ```excel
   =C26 - F26       [Beginning balance minus principal paid]
   ```

3. **Copy Down:** Select row 26, copy formulas down to row 169 (144 payments total)

4. **Verification:**
   - Final ending balance (G169) should be $0 or very close
   - Total interest paid over life of loan: ~$16.8M
   - First payment: ~$229K interest, ~$236K principal
   - Last payment: ~$2K interest, ~$463K principal

**Key Insight:** Early payments are mostly interest; later payments are mostly principal. This is how amortization works.

---

### Tab 3: Monthly Cash Flow Forecast

**Goal:** Build 12-month rolling forecast of all debt and lease obligations

**Solution Approach:**

1. **Operating Lease Payments (Column C):**
   ```excel
   ='1_Fleet_Portfolio'!B28
   ```
   This pulls the total monthly portfolio payment you calculated in Tab 1

2. **Debt Service Payments (Column D):**
   ```excel
   ='2_Debt_Amortization'!$B$21
   ```
   This pulls the monthly debt payment from Tab 2

3. **Total Monthly Outflow (Column E):**
   ```excel
   =C16+D16
   ```
   Should be approximately: $1,913,000 + $465,068 = $2,378,068/month

4. **Cumulative Outflow (Column F):**
   ```excel
   =E16             [First row]
   =F16+E17         [Subsequent rows - running total]
   ```

5. **Alert Flag (Column G):**
   ```excel
   =IF(E16>2000000, "HIGH", "")
   ```
   Flags months with over $2M in payments

6. **Conditional Formatting:**
   - Select column E
   - Home > Conditional Formatting > Highlight Cells Rules > Greater Than
   - Enter 2000000, choose red fill

**Summary Metrics:**
- Total 12-Month Cash Outflow: ~$28.5M
- Average Monthly Payment: ~$2.38M
- Peak Month: All months are roughly equal

**Key Insight:** Treasury uses rolling forecasts to ensure sufficient liquidity for upcoming obligations.

---

### Tab 4: Payment Tracking & Reconciliation

**Goal:** Reconcile bank statement against scheduled payments

**Solution Approach:**

1. **Build the Reconciliation Worksheet (Rows 27-32):**

   Start by listing all Payment IDs (PAY-001 through PAY-005) in column A

2. **Scheduled Amount (Column B):**
   ```excel
   =VLOOKUP(A27, A18:D22, 4, FALSE)
   ```
   Looks up the scheduled amount for each Payment ID

3. **Actual Amount (Column C):**
   ```excel
   =IFERROR(VLOOKUP(A27, OFFSET(E18,0,0,6,1):OFFSET(J18,0,0,6,1), 6, FALSE), 0)
   ```
   Or use INDEX/MATCH:
   ```excel
   =IFERROR(INDEX(J18:J23, MATCH("*"&A27&"*", L18:L23, 0)), 0)
   ```
   This searches the bank statement Reference Note for the Payment ID

4. **Variance (Column D):**
   ```excel
   =C27-B27
   ```

5. **Variance % (Column E):**
   ```excel
   =IF(B27=0, 0, D27/B27)
   ```
   Format as percentage

6. **Status (Column F):**
   ```excel
   =IF(D27=0, "Match", "Variance")
   ```

7. **Variance Category (Column G):**
   ```excel
   =IF(D27=0, "Match", 
      IF(C27=0, "Missing Payment",
         IF(D27>0, "Overpayment",
            "Underpayment")))
   ```

**Expected Variances:**
- PAY-001: Match ($0 variance)
- PAY-002: Match ($0 variance)
- PAY-003: Match ($0 variance) - Note: paid 1 day early but amount correct
- PAY-004: Overpayment (+$2,000) - paid $400K instead of $398K
- PAY-005: Match ($0 variance)

**Also Note:**
- WIRE-3896 is an extra payment not in scheduled payments (new aircraft deposit)
- This needs to be flagged and investigated

**Summary:**
- Total Scheduled: $1,913,000
- Total Actual: $2,040,000
- Net Variance: +$127,000 (we paid more than scheduled)

**Key Insight:** Daily reconciliation catches errors before they compound. The $2K overpayment and $125K extra payment need investigation.

---

### Tab 5: Variance Report & Analysis

**Goal:** Analyze forecast vs. actual and create pivot table summary

**Solution Approach:**

1. **Variance ($) Column D:**
   ```excel
   =C16-B16
   ```
   Actual minus Forecast

2. **Variance (%) Column E:**
   ```excel
   =IF(B16=0, 0, D16/B16)
   ```
   Format as percentage (0.00%)

3. **Investigation Required? (Column F):**
   ```excel
   =IF(ABS(E16)>0.05, "YES", "NO")
   ```
   Flags variances greater than 5% in either direction

4. **Summary Metrics:**
   ```excel
   Total Forecasted:     =SUM(B16:B23)
   Total Actual:         =SUM(C16:C23)
   Total Variance:       =SUM(D16:D23)
   Forecast Accuracy:    =1-ABS(B28/B26)
   Items for Investigation: =COUNTIF(F16:F23,"YES")
   ```

5. **Create Pivot Table:**
   - Select data range A15:G23
   - Insert > PivotTable
   - Place in cell H15
   - Rows: Payment Category (or create a category field grouping)
   - Values: Sum of Variance ($)
   - This shows where variances are concentrated

6. **Create Chart:**
   - Select columns A, B, C (categories, forecast, actual)
   - Insert > Column Chart > Clustered Column
   - Format with two series (blue for forecast, orange for actual)

**Key Findings:**
- Total variance: +$179,300 (7.6% over forecast)
- Major variances:
  - New aircraft deposit: $125K (not in forecast)
  - Credit facility interest: $2,800 higher (rate increase)
  - Wells Fargo overpayment: $2,000
  - FX benefit: $8,500 (favorable)

**Key Insight:** Variance analysis explains differences to leadership and identifies areas for forecast improvement.

---

### Tab 6: Month-End Close Package

**Goal:** Prepare complete accounting close package with journal entries

**Solution Approach:**

1. **Debt Portfolio Summary:**
   ```excel
   Beginning Debt Balance:    ='2_Debt_Amortization'!C26
   Principal Payments Made:   ='2_Debt_Amortization'!F26
   Ending Debt Balance:       =B16-B17
   
   Interest Expense:          ='2_Debt_Amortization'!E26
   Operating Lease Expense:   ='1_Fleet_Portfolio'!B28
   ```

2. **Journal Entries:**
   
   **Interest Expense Entry:**
   ```
   Debit:  Interest Expense     $229,166
   Credit: Cash                         $229,166
   ```
   
   **Lease Expense Entry:**
   ```
   Debit:  Lease Expense        $1,685,000
   Credit: Cash                         $1,685,000
   ```
   
   **Principal Payment Entry:**
   ```
   Debit:  Debt - Long Term     $235,902
   Credit: Cash                         $235,902
   ```

3. **Executive Dashboard Metrics:**
   ```excel
   Total Debt Outstanding:    =B18
   Debt-to-Assets Ratio:      =B18/500000000  (assuming $500M assets)
   
   Monthly Cash Outflow:      =B20+B21+B17
   Annual Run Rate:           =B35*12
   
   Interest Coverage:         =Operating_Income/B20  (need OpIncome data)
   Average Interest Rate:     =B20/(B16+B18)/2
   ```

4. **Reconciliation Checklist:**
   Go through each item and verify:
   - Check debt balance matches amortization schedule
   - Verify interest expense calculation
   - Confirm lease expense totals
   - Ensure cash flow forecast alignment
   - Review payment reconciliation (Tab 4)
   - Document variance explanations (Tab 5)
   - Verify journal entries balance (debits = credits)

**Key Insight:** Month-end close package synthesizes all Treasury activity for Accounting. Accuracy is critical for financial reporting and audits.

---

## Treasury Terminology Glossary

### Core Treasury Terms

**Amortization Schedule**
- Detailed payment schedule showing principal and interest breakdown over the life of a loan
- Used to track remaining balance and forecast future payments

**Debt Service**
- The cash required to pay back principal and interest on debt
- Includes both regularly scheduled payments and balloon payments

**Operating Lease**
- A lease where the airline doesn't own the aircraft
- Treated as rental expense, not a balance sheet liability (under old GAAP)
- Monthly payments go directly to expense

**Finance Lease / Capital Lease**
- A lease that's essentially a financed purchase
- Aircraft and debt appear on balance sheet
- Payments split between principal (balance sheet) and interest (income statement)

**Liquidity**
- The company's ability to meet short-term cash obligations
- Treasury's primary job is ensuring sufficient liquidity

**Credit Facility**
- A pre-arranged line of credit the company can draw on when needed
- Like a corporate credit card with large limit
- Provides liquidity buffer for unexpected needs

**Debt Covenant**
- Requirements and restrictions in debt agreements
- Examples: maintain certain debt ratios, provide quarterly reports
- Treasury monitors compliance to avoid default

**SOX Compliance (Sarbanes-Oxley)**
- Federal law requiring accurate financial reporting and internal controls
- Treasury must document all payments, maintain audit trails
- Reconciliations are key control activities

**Reconciliation**
- Process of comparing two sets of records to ensure they match
- Treasury reconciles: scheduled vs. actual payments, bank statements, system balances
- Critical for catching errors and fraud

**Variance Analysis**
- Comparing actual results to forecasted/budgeted amounts
- Explaining why differences occurred
- Used to improve future forecasts

### Aircraft Financing Terms

**Aircraft Delivery**
- When manufacturer hands over a new plane to the airline
- Major cash outflow event (down payment, first payments)
- Treasury must plan liquidity months in advance

**Pre-Delivery Payment (PDP)**
- Deposits paid to manufacturer before aircraft is delivered
- Can be 5-30% of purchase price paid over 2-3 years
- Must be tracked and forecasted

**Enhanced Equipment Trust Certificate (EETC)**
- Common way airlines finance aircraft
- Secured by the aircraft itself
- Typically lower interest rates due to strong collateral

**Sale-Leaseback**
- Airline sells aircraft it owns, then leases it back
- Converts asset to cash while keeping the plane
- Treasury strategy for improving liquidity

### Financial Metrics

**Debt-to-Equity Ratio**
- Total Debt / Shareholders' Equity
- Measures financial leverage
- Rating agencies watch this closely

**Interest Coverage Ratio**
- EBIT / Interest Expense
- Measures ability to pay interest from operations
- Higher is better (>3x is healthy)

**Liquidity Ratio / Current Ratio**
- Current Assets / Current Liabilities
- Measures ability to pay short-term obligations
- >1.0 means you can cover obligations

**Free Cash Flow (FCF)**
- Operating Cash Flow - Capital Expenditures
- Cash available after maintaining operations
- Used to pay debt, dividends, or build reserves

---

## Key Excel Functions for Treasury

### Financial Functions

**PMT(rate, nper, pv, [fv], [type])**
- Calculates periodic payment for a loan
- rate = interest rate per period
- nper = total number of payments
- pv = present value (loan amount)
- Example: `=PMT(0.05/12, 144, -50000000)` → $465,068.34/month

**IPMT(rate, per, nper, pv)**
- Calculates interest portion of a specific payment
- per = which payment period (1, 2, 3...)
- Example: `=IPMT(0.05/12, 1, 144, -50000000)` → $229,166.67 (first payment interest)

**PPMT(rate, per, nper, pv)**
- Calculates principal portion of a specific payment
- Example: `=PPMT(0.05/12, 1, 144, -50000000)` → $235,901.67 (first payment principal)

**FV(rate, nper, pmt, [pv], [type])**
- Future value of investment or loan
- Used for savings projections

**RATE(nper, pmt, pv, [fv], [type])**
- Calculates interest rate of a loan
- Useful when rate isn't known but payments are

### Lookup Functions

**VLOOKUP(lookup_value, table_array, col_index, [range_lookup])**
- Searches for value in first column, returns value from specified column
- Example: `=VLOOKUP("PAY-001", A18:D22, 4, FALSE)`
- FALSE = exact match (always use for IDs)

**INDEX(array, row_num, [col_num])**
**MATCH(lookup_value, lookup_array, [match_type])**
- INDEX/MATCH combination is more flexible than VLOOKUP
- Can look left, handles inserted columns better
- Example: `=INDEX(D18:D22, MATCH("PAY-001", A18:A22, 0))`

**XLOOKUP(lookup_value, lookup_array, return_array)** (Excel 365)
- Modern replacement for VLOOKUP
- Simpler syntax, more powerful
- Example: `=XLOOKUP("PAY-001", A18:A22, D18:D22)`

### Date Functions

**EDATE(start_date, months)**
- Returns date that is X months before/after start date
- Perfect for payment schedules
- Example: `=EDATE(DATE(2021,7,1), 1)` → 2021-08-01

**EOMONTH(start_date, months)**
- Returns last day of month X months away
- Useful for month-end close dates

**DATEDIF(start_date, end_date, unit)**
- Calculates difference between dates
- Units: "M" for months, "Y" for years
- Example: `=DATEDIF(DATE(2021,7,1), DATE(2026,1,31), "M")` → 54 months

### Logic & Error Handling

**IF(logical_test, value_if_true, value_if_false)**
- Basic conditional logic
- Example: `=IF(E15<>"-", E15, F15)`

**IFERROR(value, value_if_error)**
- Returns alternative value if formula errors
- Essential for VLOOKUP formulas
- Example: `=IFERROR(VLOOKUP(...), 0)`

**IFS(logical_test1, value1, [logical_test2, value2]...)**
- Multiple conditions without nesting
- Example: `=IFS(D27=0, "Match", C27=0, "Missing", D27>0, "Over")`

### Aggregation Functions

**SUM, SUMIF, SUMIFS**
- Basic summation and conditional summation
- Example: `=SUMIF(A:A, "Debt Service", C:C)`

**AVERAGE, AVERAGEIF**
- Calculate means

**COUNT, COUNTA, COUNTIF, COUNTIFS**
- Count cells meeting criteria
- Example: `=COUNTIF(F16:F23, "YES")`

**MAX, MIN**
- Find largest/smallest values
- Example: `=MAX(G15:G19)`

### Text Functions

**CONCATENATE or &**
- Join text strings
- Example: `="Payment for "&A27`

**TEXT(value, format)**
- Convert numbers to formatted text
- Example: `=TEXT(B27, "$#,##0")`

---

## How to Talk About This in Interviews

### When Discussing Your Excel Skills

**Instead of:** "I'm good at Excel"

**Say:** 
> "I'm advanced in Excel, particularly with financial functions like PMT, IPMT, and PPMT for debt analysis. To prepare for this Treasury role, I actually built a practice workbook where I created amortization schedules, payment reconciliations, and cash flow forecasts for aircraft financing scenarios. I'm comfortable with VBA automation, INDEX/MATCH for reconciliations, and building dashboards that consolidate data across multiple sources."

### When Asked About Treasury Experience

**Instead of:** "I don't have Treasury experience"

**Say:**
> "While I haven't worked in a formal Treasury role, I have directly applicable experience. At Thind Transport, I managed a $1M+ budget including forecasting cash flow obligations, processing payments, and reconciling accounts - all core Treasury functions. I supported month-end close by preparing journal entries and variance analysis. I also automated our payment tracking system using VBA, which improved accuracy and controls. To understand Treasury operations specifically, I researched aircraft financing and built practice amortization schedules and cash flow forecasts to ensure I hit the ground running."

### When Discussing Attention to Detail

**Give Specific Examples:**
> "Attention to detail is critical in Treasury work. In my simulation practice, I built reconciliation worksheets to match bank wire transfers against scheduled payments - I had to catch a $2,000 overpayment and identify a missing payment that wasn't on the bank statement. At Thind Transport, I built automated reconciliation controls that flagged variances before month-end close, which improved our accuracy and caught several potential issues. I understand that in Treasury, these controls prevent default risk and catch fraud."

### When Asked "What Do You Know About This Role?"

**Show You've Done Research:**
> "From researching the role and speaking with Treasury professionals, I understand the Financial Analyst supports Alaska's aircraft debt portfolio, operating leases, and credit facilities. Day-to-day, that includes maintaining amortization schedules, forecasting monthly cash obligations, processing wire payments with fraud controls, reconciling to bank statements, and preparing month-end close packages for Accounting. There's also cross-functional work with Fleet on aircraft deliveries, with Legal on debt agreements, and with credit rating agencies. The Bloomberg terminal access suggests there's also market monitoring for interest rates and credit conditions. The SOX compliance aspect means documentation and audit trails are critical."

### When Asked About Learning & Initiative

**Highlight Preparation:**
> "When I learned about the Treasury role, I wanted to understand it beyond just the job description. I researched what Treasury analysts actually do day-to-day, learned about debt amortization calculations and aircraft financing, and built a practice Excel workbook simulating Treasury workflows. I created amortization schedules using PMT functions, reconciliation worksheets with VLOOKUP, rolling cash flow forecasts, and month-end close packages. It gave me hands-on practice with the work and confidence that I can handle the technical requirements. It also helped me understand why certain controls matter - like catching payment variances before they compound."

### Questions to Ask the Interviewer

**Show Understanding of the Role:**

1. "What does a typical month-end close look like for the Treasury team? How does Treasury's close package feed into Accounting's process?"

2. "How does the team balance routine obligations like debt payments with more strategic work like analyzing new aircraft financing structures?"

3. "When there's a variance between scheduled and actual payments, what's the typical process for investigation and resolution?"

4. "How does Treasury work with the Fleet team on delivery schedules? How far in advance do you typically forecast cash needs for new aircraft?"

5. "What systems does Treasury use beyond Excel and Bloomberg? How integrated are they with Accounting's systems?"

6. "What does success look like for a Financial Analyst in the first 90 days?"

---

## Common Treasury Metrics

### Metrics You Should Know

**Average Debt Balance**
```excel
=(Beginning Balance + Ending Balance) / 2
```
Used for calculating average interest rates

**Effective Interest Rate**
```excel
=Total Interest Paid / Average Debt Balance
```
Actual rate paid including fees

**Debt Service Coverage Ratio (DSCR)**
```excel
=Operating Income / Total Debt Service
```
Measures ability to service debt from operations
- >1.5x is healthy
- <1.0x means struggling to cover debt

**Days Cash on Hand**
```excel
=(Cash + Short-term Investments) / (Operating Expenses / 365)
```
How many days company can operate with current cash
- Airlines target 30-60 days
- Higher during uncertainty

**Fleet Financing Ratio**
```excel
=Total Aircraft Debt / Total Fleet Value
```
Leverage on aircraft assets

### Why These Matter

**For Credit Rating Agencies:**
- They review these metrics quarterly
- Downgrades increase borrowing costs
- Treasury prepares packages showing strong metrics

**For Leadership:**
- Dashboard showing liquidity, leverage, debt service
- Trend analysis month-over-month
- Early warning if metrics deteriorating

**For You in Interviews:**
- Shows you think beyond just processing payments
- Understand the "why" behind Treasury work
- Can contribute to strategic analysis

---

## Month-End Close Process

### Treasury's Role in Close

**Week 1-3 of Month:**
- Process routine debt and lease payments
- Track actual vs. forecast
- Note any variances or unusual items
- Maintain documentation for audit

**Week 4 (Days 25-30):**
- Prepare preliminary close estimates
- Calculate accrued interest to date
- Forecast any payments before month-end
- Flag variances to Accounting team

**Day 1-3 of New Month:**
- Finalize all payments made (check bank statements)
- Complete debt balance reconciliation
- Calculate total interest expense for the month
- Calculate total lease expense for the month
- Prepare variance explanations
- Draft journal entries for Accounting

**Day 4-5:**
- Submit close package to Accounting
- Review and support Accounting questions
- Provide backup documentation if needed
- Update forecasts for new month

**Day 6-10:**
- Respond to any audit questions
- Update executive dashboards
- Conduct variance analysis meeting
- Document lessons learned
- Adjust future forecasts based on actuals

### Close Package Contents

**Core Documents:**
1. Debt portfolio summary (beginning/ending balances)
2. Interest expense calculation by debt instrument
3. Lease expense summary by aircraft
4. Payment activity detail (all wires, checks)
5. Reconciliation worksheet (scheduled vs. actual)
6. Variance analysis report
7. Journal entry proposals
8. Supporting documentation (agreements, statements)

**For Management:**
1. Executive dashboard (key metrics)
2. Liquidity report
3. Covenant compliance certification
4. Forecast vs. actual analysis
5. Next month outlook

### Controls & SOX Compliance

**Key Controls Treasury Maintains:**
- Dual approval on wire transfers (prevents fraud)
- Reconciliation of all payments to schedules
- Documentation of all variances >$X threshold
- Segregation of duties (preparer vs. reviewer)
- Monthly balance confirmations from lenders
- Audit trail of all system changes

**Why This Matters:**
- External auditors test these controls
- SOX violations can result in personal liability
- Strong controls protect company and employees
- Documentation proves compliance

---

## Practice Interview Scenarios

### Scenario 1: Payment Variance

**Interviewer:** "You notice a $50,000 difference between what we scheduled to pay on a lease and what actually went out the door. What do you do?"

**Good Answer:**
> "First, I'd pull the scheduled payment details from our system and the actual wire confirmation from the bank to verify the variance is real. Then I'd check if it's a timing issue - maybe we paid early or late. If the amount is genuinely different, I'd review the lease agreement to confirm the scheduled amount is correct - rates could have adjusted. I'd also check with our payment processing team to see if there was a known issue. While investigating, I'd flag this to my manager since $50K is material, and document everything for audit trail. If it's an overpayment, we'd need to request refund from the lessor. If underpayment, we need to cure it quickly to avoid default. Finally, I'd update our forecast if the scheduled amount was wrong."

### Scenario 2: Cash Crunch

**Interviewer:** "You're forecasting cash flow and realize next month we have $150M in obligations but only $100M in projected cash. What do you do?"

**Good Answer:**
> "This is a liquidity issue that needs immediate attention. I'd first verify my forecast is accurate - check all scheduled debt payments, leases, and any other known obligations. Then I'd look at our available liquidity sources: undrawn credit facilities, short-term investment maturities, operational cash generation. I'd prepare a summary showing the gap and potential solutions - like drawing on our revolver credit facility or timing certain payments differently if agreements allow. I'd escalate this to Treasury leadership immediately with the analysis and options. This isn't something I'd try to solve alone - leadership and potentially CFO need to be involved. Time is critical because if we miss payments, that's default risk."

### Scenario 3: System Error

**Interviewer:** "It's the 5th business day of the month and Accounting says our debt balance doesn't match theirs by $5M. Month-end close is due today. What's your approach?"

**Good Answer:**
> "First, I'd stay calm - reconciliation differences happen and there's a systematic way to resolve them. I'd pull our debt schedule showing the ending balance we calculated and ask Accounting for their detailed schedule. Then I'd compare line by line to identify where the difference is. Common causes: they might have a payment we didn't record, we might have a payment they didn't get, principal vs. interest classification difference, or timing on month-end cutoff. I'd also check if we had any unusual activity in the month - early payments, refinancing, new debt. Since close is due today, I'd communicate the issue to my manager immediately and propose working with Accounting to identify the difference. Even if we don't resolve by end of day, documenting what we know and committing to resolution is better than forcing wrong numbers. The worst thing would be to adjust one side to match without understanding why."

---

## Next Steps

### After Completing the Simulation

1. **Time Yourself** - Track how long each exercise takes. You'll get faster with practice.

2. **Review Your Work** - Use the hints in this guide to check your formulas. Make sure you understand the logic, not just copying.

3. **Practice Explaining** - Talk through your approach out loud. Pretend you're explaining to a manager or interview. This builds confidence.

4. **Customize Your Resume** - Update your Excel skills bullet to mention specific functions you practiced (PMT, IPMT, VLOOKUP, reconciliation).

5. **Prepare Interview Stories** - Write down 2-3 specific examples from the simulation you can reference in interviews.

### In Your Alaska Airlines Interview

**When to Mention the Simulation:**
- "To prepare for this role, I built a Treasury practice workbook..."
- "I wanted to understand Treasury operations, so I created amortization schedules and reconciliation workflows..."
- "I practiced the specific Excel functions Treasury uses like PMT, IPMT, and payment matching..."

**When NOT to Overdo It:**
- Don't claim you have Treasury experience
- Don't say this replaces real experience
- Don't spend 10 minutes on it - brief mention shows initiative

**The Right Balance:**
> "While my direct experience is in FP&A and budget management, I researched Treasury operations and built practice exercises to understand the workflows. That showed me how my payment processing and reconciliation experience at Thind Transport translates to Treasury's debt portfolio management."

---

## Additional Resources

### To Learn More

**Books:**
- "Treasury Management: The Practitioner's Guide" - Steven Bragg
- "Corporate Treasury and Cash Management" - Luca Bucalossi

**Websites:**
- Association for Financial Professionals (AFP) - treasury resources
- Treasury Today - industry news and trends
- IATA Economics - airline industry financial data

**Excel Practice:**
- Microsoft Excel Financial Functions documentation
- Corporate Finance Institute (CFI) Excel courses

### Aircraft Financing Specific

**Terms to Research:**
- EETC (Enhanced Equipment Trust Certificate)
- ACMI Lease (Aircraft, Crew, Maintenance, Insurance)
- 12-year depreciation schedule for aircraft
- Residual value risk in aircraft leasing

**Alaska Airlines Context:**
- Alaska's fleet: Boeing 737 MAX, Airbus A320 family
- Hawaiian acquisition: integration of Hawaiian's A330 widebody fleet
- Alaska's credit rating and debt structure (check investor relations)

---

## Summary Checklist

Before your interview, you should be able to:

- [ ] Explain what an amortization schedule is and build one in Excel
- [ ] Calculate monthly payment using PMT function
- [ ] Describe the difference between operating lease and finance lease
- [ ] Explain how Treasury supports month-end close
- [ ] Walk through a payment reconciliation process
- [ ] Define key metrics like debt-to-equity, interest coverage
- [ ] Discuss why reconciliation and controls matter (SOX, fraud prevention)
- [ ] Give specific examples of your attention to detail
- [ ] Explain how this role differs from FP&A (focus on cash vs. profitability)
- [ ] Ask intelligent questions about Treasury processes

---

**Good luck with your Alaska Airlines application! You've got this! 🛫**

*This simulation and guide show genuine interest in learning Treasury operations. Combined with your finance background, Excel skills, and attention to detail, you're well-positioned for this role.*
