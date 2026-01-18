# FloQast Product Knowledge Deep Dive

## Company Overview

**Founded**: 2013  
**Founders**: Mike Whitmire (CPA), Chris Sluty (CPA), Cullen Zandstra (Engineer)  
**Headquarters**: Los Angeles, CA  
**Employees**: 300+ (as of 2025)  
**Customers**: 3,500+ accounting teams globally  
**Valuation**: $1.6 billion (Series E, April 2024)  
**Funding**: $200M+ total raised

**Mission**: Elevate the accounting profession through innovative technology

**Why It Matters**: Founded by accountants who experienced close pain firsthand

---

## Product Suite (3 Layers)

### 1. FloQast Close (Core - 2013)

**What It Is**: Month-end close workflow management platform

**Key Features**:
- Close checklist management (task tracking, dependencies, due dates)
- Centralized documentation storage (support workpapers in one place)
- Email reminders and notifications
- Real-time progress dashboards
- Period-over-period comparison
- Tie-outs to Excel workbooks

**Customer Pain It Solves**:
- Manual Excel checklists hard to track
- Supporting documents scattered across email/shared drives
- No visibility into close progress
- Task dependencies unclear

**Impact**: Standardizes and accelerates close process

---

### 2. FloQast AutoRec (2019)

**What It Is**: Automated account reconciliation engine

**Key Features**:
- Rule-based transaction matching (exact match, fuzzy date, one-to-many)
- Auto-import GL data from ERP
- Exception flagging for manual review
- Reconciliation templates (reusable configurations)
- Workflow approval routing
- Historical recon storage

**Common Use Cases**:
- Bank reconciliations (GL Cash vs. Bank Statement)
- Intercompany reconciliations (Entity A vs. Entity B)
- Subledger reconciliations (GL AR vs. AR aging)

**Impact**: **38% reduction in reconciliation time** (FloQast stat)

**How It Works**:
1. Pull GL transactions from ERP
2. Pull external data (bank statement, subledger)
3. Apply matching rules (amount + date + description logic)
4. Auto-match what it can
5. Flag exceptions for accountant review
6. Generate reconciliation report

---

### 3. FloQast Transform AI Agents (2025)

**What It Is**: Natural language agent builder for custom accounting workflows

**The Game-Changer**: No-code/low-code - accountants build agents themselves

**Key Features**:
- **Agent Builder**: Describe task in natural language, system creates agent
- **Pre-built agents**: Coupa accruals, variance explainer, data transformation
- **Custom agents**: Build any recurring workflow
- **Auditability**: Full log of agent actions for compliance (ISO 42001 certified)
- **Human-in-the-loop**: Agent generates draft, accountant approves

**Example Agents**:
1. **Journal Entry Agent**: Auto-create recurring entries (depreciation, accruals)
2. **Flux (Variance Explainer)**: AI-generated variance narratives
3. **Data Transformation Agent**: Standardize messy data (invoices from PDFs)
4. **Reconciliation Agent**: Custom recon matching beyond AutoRec

**Impact**: **20% reduction in overall close time** (FloQast stat)

**Why Transform Is Different from Competitors**:
- Natural language (vs. complex scripting)
- Built for accountants (not IT teams)
- Auditable by design (SOX/ISO compliance)
- Fast time-to-value (days, not months)

---

## Technical Architecture

### ERP Integrations

**Supported ERPs**:
- NetSuite (REST/SOAP API)
- Sage Intacct (Web Services API)
- Microsoft Dynamics 365 (OData API)
- SAP (OData/RFC)
- Oracle EBS
- QuickBooks Online
- Workday Financials
- Custom ERPs (via API or file upload)

**What FloQast Pulls**:
- Chart of Accounts
- Trial Balance (by period)
- GL Transaction Detail
- Subsidiary Ledgers (Cash, AR, AP, Fixed Assets)

**Integration Methods**:
1. API (most common - automated, real-time)
2. File Upload (CSV/Excel - manual, less desirable)
3. Direct Database Connection (on-premise ERPs only)

**Sync Frequency**: Daily, weekly, on-demand, or real-time

**Data Flow** (Read-Only):
```
ERP → FloQast API → FloQast Database → FloQast UI
```
(FloQast typically doesn't write back to ERP)

---

## Use Cases by Company Size

### Small (<$50M Revenue)
- Close management (standardize process)
- Basic reconciliations (bank, key accounts)
- 1-2 simple agents (depreciation, basic accruals)

### Mid-Market ($50M-$500M)
- Full close automation
- AutoRec for all balance sheet accounts
- 3-5 agents (accruals, variance, custom workflows)
- Multi-entity support

### Enterprise (>$500M)
- Complex close orchestration across entities
- Advanced agents for complex workflows
- Integration with multiple ERPs
- Custom compliance reporting

---

## Competitive Landscape

### Main Competitors

**1. BlackLine** (Market Leader)
- Established player (founded 2001)
- Strong in large enterprise
- More IT-centric (less intuitive for accountants)
- FloQast differentiator: Ease of use, AI-first

**2. Trintech** (Cadency Platform)
- Strong in reconciliations
- Complex to implement
- FloQast differentiator: Faster time-to-value

**3. Workiva** (Wdesk)
- Focus on reporting and compliance (10-K, 10-Q)
- Less focused on close automation
- FloQast differentiator: Close process vs. reporting

**4. Adra by Trintech**
- Mid-market focus
- Similar to FloQast
- FloQast differentiator: Transform AI Agents

### FloQast's Competitive Advantages
1. Built by accountants for accountants (intuitive UX)
2. AI-first innovation (Transform launched 2025)
3. Fast time-to-value (30-90 days vs. 6-12 months)
4. ERP-agnostic (works with any ERP)
5. Strong customer support and enablement

---

## Awards & Recognition (2025)

- **CODiE Award**: Best Fintech Solution
- **Deloitte Technology Fast 500**: Rapid growth
- **FinTech Breakthrough Awards**: Accounting Automation Innovation
- **CNBC Disruptor 50**: Disrupting accounting tech
- **Inc. Best Workplaces**: 2021-2024 (4 consecutive years)
- **Built In Best Places to Work**: Los Angeles (6 consecutive years)

---

## Pricing (General)

**Note**: FloQast doesn't publish pricing publicly. Based on industry research:

- **Typical Range**: $30,000-$150,000/year
- **Based On**: Number of entities, users, accounts, modules
- **Implementation**: Additional services fee (varies)

**ROI Calculation**:
- Accountant fully loaded cost: ~$50-$75/hour
- 20% close time savings × 5 accountants × 160 hours/year each = 160 hours saved
- Savings: $8,000-$12,000/year (easily justifies investment)

---

## Customer Examples (Public)

- **Snowflake**: SaaS company, rapid growth
- **Twilio**: Cloud communications
- **Instacart**: Grocery delivery
- **Golden State Warriors**: Sports/entertainment
- **Los Angeles Lakers**: Sports/entertainment
- **Zoom**: Video communications

**Common Profile**: High-growth tech companies, SaaS businesses, multi-entity structures

---

## ISO 42001 Certification

**What It Is**: International standard for AI management systems

**Why It Matters**: FloQast's AI agents are auditable and compliant with emerging AI regulations

**Key Points**:
- Full audit trail of agent decisions
- Transparency in AI logic
- Human oversight requirements
- Data privacy and security

**Interview Talking Point**:
> "FloQast is ISO 42001 certified, which means our AI agents meet international standards for auditability and compliance. Every agent action is logged - who, what, when, why. This is critical for SOX compliance and external audits."

---

## Product Roadmap Insights (Public)

**Current Focus**:
- Expanding Transform AI Agent library
- Deeper ERP integrations
- Enhanced analytics and insights
- Global expansion (EMEA, APAC)

**Future Vision**: Fully automated close where AI handles 80% of work, accountants focus on judgment and analysis

---

## Sales & Implementation Process

### Typical Customer Journey

**Month 1-2: Sales & Demo**
- AE (Account Executive) demos FloQast
- Customer evaluates vs. alternatives
- ROI calculation and business case

**Month 3-4: Implementation**
- AFDA leads deployment
- ERP integration setup
- Close checklist configuration
- Agent configuration
- User training

**Month 5+: Expansion**
- Add more agents
- Expand to additional entities
- Optimize based on usage

**AFDA's Role**: Months 3-4 (implementation) and ongoing support

---

## Interview Usage

### Demonstrate Deep Product Knowledge

**Question**: "What do you know about FloQast's products?"

**Strong Answer**:
> "FloQast has three product layers:
>
> 1. **Close** - The core workflow management platform for month-end close, with checklists, documentation, and progress tracking
>
> 2. **AutoRec** - Automated reconciliation matching launched in 2019, which reduced recon time by 38% through rule-based matching
>
> 3. **Transform AI Agents** - The newest product launched in 2025, which lets accountants build custom AI agents using natural language. This includes pre-built agents like Flux for variance explanations and custom agents for workflows like Coupa accruals
>
> What's unique is that FloQast was founded by CPAs who experienced close pain firsthand. The product is built for accountants, not IT teams. And the Transform AI Agents are ISO 42001 certified, which means they're auditable and compliant - critical for SOX and external audits.
>
> FloQast competes with BlackLine and Trintech, but differentiates through ease of use, AI-first innovation, and faster time-to-value."

---

## Key Statistics to Memorize

- **3,500+** customers
- **$1.6B** valuation (Series E, 2024)
- **38%** reduction in recon time (AutoRec)
- **20%** reduction in close time (overall platform)
- **27 hours/month** saved on variance analysis (Flux)
- **2013** founded
- **2025** Transform AI Agents launched
- **ISO 42001** certified for AI management

---

**Use this knowledge to demonstrate you've done your homework and understand not just what FloQast does, but WHY it matters to customers.**



