# FloQast Terminology & Accounting Concepts

## FloQast Product Terms

### Core Products
- **FloQast Close** - Month-end close management platform
- **FloQast AutoRec** - Automated reconciliation matching engine
- **FloQast Transform** - AI-powered workflow automation platform
- **Agent Builder** - Natural language interface to create custom AI agents

### Transform AI Agents
- **Agent** - Automated workflow that performs accounting tasks
- **Journal Entry Agent** - Auto-generates journal entries (e.g., accruals, depreciation)
- **Flux** - AI variance explainer agent that generates narrative commentary
- **Data Transformation Agent** - Standardizes unstructured data
- **Custom Agent** - User-defined agent built via Agent Builder

### Automation Concepts
- **Trigger** - Event that starts an agent (e.g., last day of month)
- **Business Rules** - Logic the agent applies (e.g., materiality threshold >$500)
- **Audit Trail** - Complete log of agent actions for compliance
- **Human-in-the-Loop** - Agent generates draft, human reviews/approves
- **Exception Handling** - Flagging items that need manual review

## Accounting Workflow Terms

### Month-End Close
- **Close Process** - Series of tasks to finalize monthly financials
- **Close Checklist** - Task list for month-end (who, what, when, status)
- **Period-End Close** - Closing accounting period (month, quarter, year)
- **Hard Close** - No entries allowed after close date
- **Soft Close** - Preliminary close allowing adjustments

### Journal Entries
- **Journal Entry (JE)** - Record of debits and credits
- **Accrual** - Recording expense/revenue before cash transaction
- **Reversal** - Reversing an accrual in next period
- **Adjustment** - Correcting entry for errors or estimates
- **Recurring Entry** - Entry that repeats each period (e.g., depreciation)
- **Standard Journal Entry (SJE)** - Pre-defined recurring entry

### Reconciliations
- **Account Reconciliation** - Matching GL balance to supporting documentation
- **Bank Reconciliation** - GL Cash vs. Bank Statement
- **Deposits in Transit** - Deposits recorded in GL but not yet on bank statement
- **Outstanding Checks** - Checks recorded in GL but not yet cleared bank
- **Subledger Reconciliation** - GL account vs. detailed ledger (AR, AP, Fixed Assets)
- **Intercompany Reconciliation** - Matching balances between legal entities

### Variance Analysis
- **Variance** - Difference between actual and budget/prior period
- **Favorable Variance** - Revenue > budget or Expense < budget
- **Unfavorable Variance** - Revenue < budget or Expense > budget
- **Material Variance** - Variance exceeding threshold (%, $)
- **Variance Driver** - Root cause explanation for variance
- **Rolling Forecast** - Continuously updated forecast

## ERP & Integration Terms

### ERP Systems
- **ERP** - Enterprise Resource Planning (system of record)
- **NetSuite** - Cloud ERP by Oracle, popular with tech companies
- **Sage Intacct** - Cloud ERP, strong multi-entity support
- **Microsoft Dynamics 365** - Microsoft's ERP platform
- **SAP** - Large enterprise ERP (on-premise and cloud)

### Data Structures
- **Chart of Accounts (COA)** - List of all GL accounts
- **General Ledger (GL)** - Core accounting system with all transactions
- **Trial Balance (TB)** - List of all accounts with debit/credit balances
- **Subsidiary Ledger** - Detailed transactions for a specific account
- **GL Detail** - Transaction-level data from GL

### Integration Concepts
- **API Integration** - Programmatic connection between systems
- **OAuth** - Secure authentication method for APIs
- **Data Sync** - Automated data transfer between systems
- **Mapping** - Linking ERP fields to FloQast fields
- **Subsidiary/Entity** - Legal entity within multi-entity structure
- **Dimension/Segment** - Additional tagging (Department, Location, Project)

## Financial Accounting Basics

### Financial Statements
- **P&L (Profit & Loss)** - Revenue minus expenses = net income
- **Income Statement** - Same as P&L
- **Balance Sheet** - Assets = Liabilities + Equity (point in time)
- **Cash Flow Statement** - Sources and uses of cash

### Accounting Principles
- **Accrual Basis** - Record when earned/incurred (vs. cash basis)
- **Matching Principle** - Match expenses to revenues in same period
- **Materiality** - Threshold for what matters to financial statement users
- **Double Entry** - Every transaction has debit(s) and credit(s) that balance

### Key Accounts
- **Assets** - What company owns (Cash, AR, Inventory, PP&E)
- **Liabilities** - What company owes (AP, Accrued Expenses, Debt)
- **Equity** - Owners' stake (Capital, Retained Earnings)
- **Revenue** - Income from operations
- **COGS** - Cost of Goods Sold
- **OPEX** - Operating Expenses (SG&A, R&D)

## Forward Deployed Accountant Terms

### Implementation
- **Deployment** - Process of setting up FloQast for a customer
- **Configuration** - Setting parameters for agents, reconciliations, close checklist
- **Testing** - Validating that setup works correctly
- **Go-Live** - Launch date when customer starts using FloQast
- **Post-Implementation Support** - Ongoing help after go-live

### Customer Success
- **Enablement** - Training customers to use FloQast independently
- **Workshop** - Hands-on training session
- **Office Hours** - Open Q&A session for customer questions
- **Adoption** - Extent to which customer uses FloQast features
- **Time-to-Value** - How quickly customer realizes benefits

### Troubleshooting
- **Root Cause Analysis** - Identifying why something isn't working
- **Data Quality Issue** - Incorrect or missing data causing problems
- **Configuration Error** - Incorrect settings in FloQast
- **Integration Failure** - ERP connection not working
- **Exception** - Item that doesn't match/requires manual review

## Industry-Specific Terms

### SaaS Accounting
- **ARR** - Annual Recurring Revenue
- **MRR** - Monthly Recurring Revenue
- **Deferred Revenue** - Cash received for services not yet delivered
- **Revenue Recognition (ASC 606)** - Standard for when to recognize revenue
- **Churn** - Customer cancellations

### Manufacturing
- **WIP** - Work in Process Inventory
- **BOM** - Bill of Materials
- **Standard Cost** - Pre-determined cost for inventory
- **Variance** - Difference between standard and actual cost
- **Overhead Absorption** - Allocating indirect costs to products

## FloQast Statistics (Memorize These)

- **38%** reduction in reconciliation time (AutoRec)
- **20%** reduction in overall close time (FloQast platform)
- **27 hours/month** saved on variance analysis (Flux agent)
- **3,500+** customers globally
- **2025 Awards**: CODiE Fintech, Deloitte Fast 500, FinTech Breakthrough

## Interview Usage Examples

**Demonstrate Knowledge**:
> "FloQast's AutoRec automates the matching logic I used to do manually with vlookup. For bank reconciliations, it applies exact match and fuzzy date match rules to identify deposits in transit and outstanding checks. That's a 38% time savings."

**Show Technical Understanding**:
> "The agent pulls trial balance data from NetSuite via API, applies materiality thresholds based on our configuration, and generates draft journal entries. The full audit trail ensures SOX compliance."

**Connect to Experience**:
> "At Thind Transport, I performed accrual entries manually. With FloQast's Journal Entry Agent, I'd configure it to pull received-not-invoiced items from Coupa and auto-generate the accrual entry. That's the 'human-in-the-loop' model - agent does heavy lifting, I review and approve."



