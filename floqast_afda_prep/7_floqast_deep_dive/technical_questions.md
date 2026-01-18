# FloQast AFDA: Technical Interview Questions

## Accounting Workflow Questions

### 1. "Walk me through how you'd configure a Coupa accrual agent for a customer"

**Answer**:
> "First, I'd understand their current manual process:
> - How do they identify items to accrue? (Received but not invoiced in Coupa)
> - What's their materiality threshold? (e.g., only items >$500)
> - Which GL accounts do they use for different expense categories?
> 
> Then I'd configure the agent:
> 1. **Connect data source**: Authenticate Coupa API in FloQast
> 2. **Map accounts**: Maintenance → GL 6020, Fuel → GL 6010, etc.
> 3. **Set threshold**: Materiality filter at $500
> 4. **Configure trigger**: Run on last business day of month
> 5. **Set approval workflow**: Generate draft JE, route to accountant for review
> 
> Before go-live, I'd test on 2-3 months of historical data to validate output matches their manual entries.
> 
> Finally, I'd train them on reviewing agent output and approving entries in their ERP."

---

### 2. "A customer's bank reconciliation agent is matching incorrectly. How do you troubleshoot?"

**Answer**:
> "Systematic approach:
> 
> 1. **Understand the symptom**: What specifically is wrong? Matching transactions that shouldn't match? Missing valid matches?
> 
> 2. **Check the data**: 
>    - Is GL data pulling correctly from ERP?
>    - Is bank feed connected and syncing?
>    - Are there data format issues (dates, amounts)?
> 
> 3. **Review matching rules**:
>    - Is the date tolerance too wide or too narrow? (e.g., currently ±3 days, should be ±1 day?)
>    - Is the amount tolerance correct? (±$0.01?)
>    - Are there custom matching rules that need adjustment?
> 
> 4. **Test with specific examples**:
>    - Take a transaction that matched incorrectly
>    - Walk through why the agent matched it
>    - Adjust the rule and retest
> 
> 5. **Document and train**:
>    - Document what was wrong and how we fixed it
>    - Train customer on monitoring match quality
> 
> I'd work closely with the customer's accountant (who knows what SHOULD match) and potentially FloQast support if it's a platform issue."

---

### 3. "Customer asks: Can FloQast automate our revenue recognition process?"

**Answer**:
> "Great question. Let me explain what FloQast can and can't do:
> 
> **What FloQast CAN do**:
> - Automate data pulls from CRM/billing systems
> - Apply rules-based revenue allocation (e.g., straight-line over contract term)
> - Generate draft journal entries for review
> - Track deferred revenue balance
> - Create reconciliations between billing and recognized revenue
> 
> **What FloQast CANNOT do** (yet):
> - Complex ASC 606 judgment calls (performance obligations, variable consideration)
> - Multi-element arrangements requiring significant judgment
> - Replace your rev rec specialist for complex SaaS contracts
> 
> **My recommendation**:
> - If your revenue is straightforward (e.g., SaaS subscriptions with monthly recognition), FloQast agents can automate 70-80% of the manual work
> - If you have complex contracts requiring judgment, FloQast can assist but not fully automate
> - Let's schedule a deeper discovery call to understand your specific contracts
> 
> I'd never overpromise. It's better to under-promise and over-deliver."

---

### 4. "Explain how FloQast integrates with NetSuite"

**Answer**:
> "FloQast connects to NetSuite via API (REST or SOAP):
> 
> **Setup process**:
> 1. Customer creates an Integration user in NetSuite with read permissions
> 2. Customer provides OAuth credentials to FloQast (secure)
> 3. FloQast authenticates and tests the connection
> 
> **What FloQast pulls**:
> - Chart of Accounts (account structure)
> - Trial Balance (account balances by period)
> - GL Detail (transaction-level data for reconciliations)
> - Subsidiary Ledgers (cash transactions, AR aging, etc.)
> 
> **Sync frequency**:
> - Typically daily or on-demand
> - Can be scheduled or manual trigger
> 
> **Data flow** (read-only in most cases):
> NetSuite → FloQast API pull → FloQast normalizes data → Displayed in FloQast UI
> 
> **Common issues**:
> - Permission errors (user needs full access to accounting records)
> - Subsidiary filtering (need to include all relevant entities)
> - Custom fields (need to map NetSuite custom segments)
> 
> I'd work with the customer's NetSuite admin to handle the technical setup."

---

## Agent Configuration Scenarios

### 5. "A manufacturing customer wants to automate their inventory accrual. How would you approach this?"

**Answer**:
> "Discovery questions first:
> - What's the current manual process?
> - Where is inventory data stored? (ERP? Separate system?)
> - What's the accrual methodology? (Actual vs. standard costing?)
> - What GL accounts are involved?
> - How often do they need to accrue? (Monthly? Quarterly?)
> 
> **Configuration approach**:
> 1. **Data source**: Connect to inventory management system
> 2. **Business logic**:
>    - Pull items received but not invoiced
>    - Calculate accrual (quantity × standard cost)
>    - Apply materiality threshold
> 3. **Account mapping**: Inventory account (debit), Accrued Liabilities (credit)
> 4. **Validation rules**: Flag items with cost > 10% of average
> 5. **Output**: Draft journal entry for review
> 
> **Testing**: Run on 3 months historical data, compare to manual accruals
> 
> **Training**: Show them how to review agent output and handle exceptions (e.g., unusual costs)
> 
> Timeline: 2-3 weeks from discovery to go-live"

---

### 6. "Customer has 5 legal entities. How do you set up FloQast to handle multi-entity?"

**Answer**:
> "Multi-entity is common. Here's the approach:
> 
> **Setup**:
> 1. **Create entities in FloQast**: Map to ERP subsidiaries/entities
> 2. **Configure permissions**: Who can see which entities?
> 3. **Separate close checklists**: Each entity has own close workflow (unless consolidated)
> 4. **ERP integration**: Pull data for each entity separately
> 
> **Considerations**:
> - **Intercompany eliminations**: Do they need consolidated close? FloQast can track intercompany reconciliations
> - **Different close timelines**: Entity A closes on day 5, Entity B on day 3?
> - **Shared vs. separate teams**: Same accountants for all entities or dedicated teams?
> 
> **Agent implications**:
> - Agents can run per entity (e.g., separate bank recon for each entity's cash account)
> - Or consolidated (e.g., one variance explainer for consolidated P&L)
> 
> I'd map out their organizational structure and close process before configuring."

---

## Process & Troubleshooting

### 7. "Walk me through your first 30 days with a new customer"

**Answer**:
> **Week 1: Discovery & Setup**
> - Kickoff call: Understand their pain points, goals, and timeline
> - Technical setup: ERP integration credentials, test connection
> - Identify quick wins (what can we automate first?)
> 
> **Week 2: Configuration**
> - Configure close checklist (map their current process to FloQast)
> - Set up first agent (usually simplest one - e.g., monthly depreciation)
> - Configure reconciliation templates
> 
> **Week 3: Testing & Training**
> - Test agent on historical data (validate output)
> - Train customer team (hands-on workshop)
> - Create documentation (step-by-step guides)
> 
> **Week 4: Go-Live & Support**
> - Run first live close with FloQast
> - I'm available for real-time support (office hours)
> - Collect feedback and iterate
> 
> **Week 5+: Expand**
> - Configure additional agents
> - Optimize based on usage patterns
> - Check in regularly
> 
> Goal: Deliver value within 30 days (not just set up software)"

---

### 8. "How do you handle a customer who is resistant to change?"

**Answer**:
> "Change management is key. My approach:
> 
> **Understand the resistance**:
> - What's the fear? (Job security? Learning curve? Trust in AI?)
> - Address it directly and empathetically
> 
> **Show, don't tell**:
> - Run agent on their historical data
> - Show side-by-side: manual entry vs. agent output
> - Prove it works before asking them to trust it
> 
> **Start small**:
> - Pick the most painful, repetitive task (e.g., monthly depreciation)
> - Automate that one thing first
> - Build trust with small wins
> 
> **Human-in-the-loop**:
> - Emphasize: Agent generates draft, you approve
> - You're still in control, just more efficient
> 
> **Identify champions**:
> - Find one team member who's excited
> - They become the advocate to their peers
> 
> Example: At Thind Transport, the team was skeptical of my VBA automation. I showed them it would save them hours. After one month, they couldn't imagine going back."

---

## FloQast Product Knowledge

### 9. "What's the difference between FloQast Close, AutoRec, and Transform AI Agents?"

**Answer**:
> **FloQast Close** (Core Product):
> - Month-end close workflow management
> - Checklists, task dependencies, documentation storage
> - Email reminders, progress dashboards
> - Think: Project management for accounting close
> 
> **FloQast AutoRec** (Automation Layer):
> - Automated account reconciliations
> - Rule-based matching (GL to bank, GL to subledger)
> - Flags exceptions for review
> - 38% reduction in reconciliation time (FloQast stat)
> - Think: Intelligent matching engine
> 
> **FloQast Transform AI Agents** (NEW - AI Layer):
> - Custom AI agents built using natural language
> - Automates complex, recurring workflows
> - Examples: Coupa accruals, variance explanations, data transformation
> - 20% reduction in close time (FloQast stat)
> - Think: AI-powered workflow automation
> 
> **How they work together**:
> 1. Close management coordinates the overall process
> 2. AutoRec handles standard reconciliations
> 3. AI Agents handle custom workflows
> 
> All three integrate with customer's ERP"

---

### 10. "What are FloQast's key differentiators vs. competitors?"

**Answer**:
> "Main competitors: BlackLine, Trintech, Workiva
> 
> **FloQast's differentiators**:
> 
> 1. **Built by accountants for accountants**:
>    - Founders were accountants who felt the pain
>    - Product is intuitive for accounting teams (not IT-driven)
> 
> 2. **AI-first innovation**:
>    - Transform AI Agents (2025) - natural language agent builder
>    - Competitors are adding AI as bolt-on; FloQast built it natively
> 
> 3. **ERP-agnostic**:
>    - Works with NetSuite, Intacct, Dynamics, SAP, etc.
>    - Competitors often favor specific ERPs
> 
> 4. **Ease of use**:
>    - Accountants can configure agents themselves (no IT required)
>    - Quick time-to-value (30 days to first automation)
> 
> 5. **Company culture**:
>    - Inc. Best Workplaces 4 years running
>    - Customer-obsessed approach
> 
> **Best fit for**: Mid-market to enterprise companies that want cutting-edge AI automation without complex IT projects
> 
> I'd position FloQast based on customer's pain points, not generic competitor bashing."

---

## Scenario-Based Questions

### 11. "Customer says: 'FloQast sounds great but we're mid-implementation of NetSuite and don't have bandwidth.' How do you respond?"

**Answer**:
> "I completely understand. NetSuite implementations are resource-intensive.
> 
> Here's what I'd suggest:
> 
> **Option 1: Wait until NetSuite stabilizes** (3-6 months post go-live)
> - Once your NetSuite close process is stable, we can layer FloQast on top
> - Benefit: We automate your new NetSuite workflows right away
> 
> **Option 2: Start FloQast planning now, implement later**
> - We document your target state close process in NetSuite
> - Design FloQast configuration in parallel
> - Go live with FloQast right after NetSuite stabilizes
> - Benefit: Faster time-to-value after NetSuite is live
> 
> **Option 3: Pilot with one entity or workflow**
> - If you have multiple entities, pilot FloQast with one that's NOT migrating to NetSuite yet
> - Build internal knowledge before full rollout
> 
> **What I wouldn't do**: Force them to take on FloQast during NetSuite chaos. That's a recipe for failure.
> 
> I'd stay engaged, provide value where possible (e.g., best practices for close process design), and be ready when they are."

---

### 12. "Customer deployed an agent and it's generating incorrect journal entries. Walk me through debugging."

**Answer**:
> "High-priority issue. Here's the systematic approach:
> 
> **Immediate action** (stop the bleeding):
> - Disable the agent temporarily (don't post incorrect entries)
> - Communicate to customer: We're investigating, manual process for now
> 
> **Root cause analysis**:
> 1. **Isolate the error**: Which entries are wrong? All of them or specific scenarios?
> 2. **Check the data**: Is the source data correct? (e.g., Coupa export accurate?)
> 3. **Check the business rules**:
>    - Is the account mapping correct? (Did they change their chart of accounts?)
>    - Is the calculation logic correct? (e.g., materiality threshold, accrual formula)
> 4. **Check the timing**: Did something change recently? (New vendor, new expense type?)
> 
> **Testing**:
> - Recreate the error with sample data
> - Fix the configuration
> - Test on historical data (validate fix)
> 
> **Communication**:
> - Explain to customer what was wrong and why
> - Show them the fix
> - Document for future reference
> 
> **Prevention**:
> - Add validation rules (e.g., flag entries >$50K for review)
> - Schedule monthly check-ins to review agent performance
> 
> I'd also loop in FloQast support if it's a platform bug vs. configuration issue."

---

## Metrics & Value Demonstration

### 13. "How do you measure success as an AFDA?"

**Answer**:
> "Success has multiple dimensions:
> 
> **Customer metrics**:
> - **Time savings**: Did we reduce close time? (Target: 20% reduction)
> - **Agent adoption**: Are they using the agents we configured? (Weekly/monthly runs)
> - **Accuracy**: Are agent outputs high quality? (Approval rate >95%)
> - **User satisfaction**: Do they find FloQast valuable? (NPS score)
> 
> **My performance metrics**:
> - **Time to value**: How fast did I deliver first working agent? (Target: <30 days)
> - **Implementation quality**: Are configurations correct? (Minimal rework)
> - **Customer retention**: Do customers renew and expand? (Upsell opportunities)
> - **Responsiveness**: How quickly do I resolve issues? (24-hour response time)
> 
> **Qualitative indicators**:
> - Customer asks for help configuring additional agents (they're empowered)
> - Customer refers FloQast to other companies (advocacy)
> - Customer provides product feedback (engaged partnership)
> 
> I'd track these in a dashboard and review monthly with my manager."

---

### 14. "Customer asks for ROI justification to their CFO. How do you build the business case?"

**Answer**:
> "CFOs care about dollars and risk. Here's the ROI framework:
> 
> **Cost Savings (Quantitative)**:
> - Current state: 5 accountants × 40 hours/month on close = 200 hours
> - Fully loaded cost: $50/hour = $10,000/month
> - FloQast reduction: 20-40% = 40-80 hours saved
> - Annual savings: $24K-$48K
> - FloQast cost: ~$30K/year (example)
> - Net savings: Break even to $18K/year
> 
> **Risk Reduction** (Qualitative but critical):
> - Reduced manual errors (audit findings cost $$)
> - Better SOX compliance (audit trail of all agent actions)
> - Reduced key person risk (process documented in FloQast)
> 
> **Strategic Benefits**:
> - Accountants spend time on analysis, not data entry
> - Faster close = faster decision-making for business
> - Scalability (grow revenue without adding accounting headcount)
> 
> **Case study**: Show example of similar company
> 
> I'd customize this based on their pain points. If they have audit findings, emphasize risk reduction. If they're growing fast, emphasize scalability."

---

### 15. "What's your 90-day plan as a new AFDA?"

**Answer**:
> **Days 1-30: Learn & Observe**
> - Shadow experienced AFDAs on customer calls
> - Learn FloQast platform deeply (Close, AutoRec, Transform)
> - Study common customer scenarios and troubleshooting
> - Get certified on FloQast products
> 
> **Days 31-60: Deploy (with support)**
> - Take ownership of 2-3 customer deployments (with mentor backup)
> - Configure agents, run workshops, train customers
> - Build internal knowledge base (document learnings)
> - Start building customer relationships
> 
> **Days 61-90: Own & Optimize**
> - Fully own customer deployments independently
> - Identify patterns (which agents work best for which industries?)
> - Contribute to AFDA team best practices
> - Seek feedback and iterate on my approach
> 
> **Key milestone**: By day 90, deliver measurable value for 5+ customers (time savings, successful agent deployments)
> 
> I'm a fast learner and will lean on the team heavily in the first 30 days."

---

## Follow-Up Questions to Ask

1. "What does a typical AFDA's customer portfolio look like? (Number of customers, industries, size)"
2. "How does FloQast support AFDAs when we encounter a technical issue we can't solve?"
3. "What's the most common mistake new AFDAs make?"
4. "How do AFDAs collaborate with Account Executives and Customer Success?"
5. "What training and onboarding does FloQast provide for new AFDAs?"

---

## Key Reminders

- **Don't overpromise**: Be honest about what FloQast can/can't do
- **Show systematic thinking**: Troubleshooting, implementation, customer management
- **Connect to experience**: Relate every answer back to Thind Transport or consulting examples
- **Emphasize learning**: "I don't know X yet, but here's how I'd learn it"
- **Customer-first**: Every technical answer should include customer impact



