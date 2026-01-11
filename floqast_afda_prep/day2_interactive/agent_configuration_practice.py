# -*- coding: utf-8 -*-
"""
Day 2: FloQast Agent Configuration Practice
Your Experience + FloQast Interview Prep

Learn to configure FloQast Transform AI Agents by:
1. Understanding configuration concepts (your Salesforce automation translates here!)
2. Working through real customer scenarios
3. Practicing how to explain configurations in interviews

Run: py agent_configuration_practice.py
"""

import json
from datetime import datetime

# ============================================================================
# AGENT CONFIGURATION FRAMEWORK
# ============================================================================

class AgentConfiguration:
    """Represents a FloQast Transform AI Agent configuration"""
    
    def __init__(self, name, customer_type):
        self.name = name
        self.customer_type = customer_type
        self.description = ""
        self.data_source = ""
        self.trigger = ""
        self.materiality = 0
        self.approval_required = True
        self.gl_mapping = {}
        self.filters = []
        
    def set_core_config(self, description, data_source, trigger, materiality, approval):
        self.description = description
        self.data_source = data_source
        self.trigger = trigger
        self.materiality = materiality
        self.approval_required = approval
        
    def add_gl_mapping(self, category, account):
        self.gl_mapping[category] = account
        
    def add_filter(self, field, operator, value):
        self.filters.append({
            "field": field,
            "operator": operator,
            "value": value
        })
        
    def validate(self):
        """Validate configuration completeness"""
        issues = []
        
        if not self.description or len(self.description) < 20:
            issues.append("Description too short - be specific about what agent does")
        
        if not self.data_source:
            issues.append("Data source not specified")
            
        if not self.trigger:
            issues.append("Trigger not specified - when should this run?")
            
        if self.materiality < 100:
            issues.append(f"Materiality ${self.materiality} very low - consider noise vs value")
            
        if not self.approval_required:
            issues.append("No approval required - risky for new agents")
            
        if len(self.gl_mapping) < 2:
            issues.append("GL mapping incomplete - need expense + liability accounts")
            
        return issues
        
    def display(self):
        """Display configuration summary"""
        print("\n" + "=" * 70)
        print(f"AGENT: {self.name}")
        print(f"Customer Type: {self.customer_type}")
        print("=" * 70)
        
        print(f"\nDescription: {self.description}")
        print(f"Data Source: {self.data_source}")
        print(f"Trigger: {self.trigger}")
        print(f"Materiality Threshold: ${self.materiality:,}")
        print(f"Approval Required: {self.approval_required}")
        
        print("\nGL Account Mapping:")
        for category, account in self.gl_mapping.items():
            print(f"  {category:<25} -> {account}")
            
        if self.filters:
            print("\nData Filters:")
            for f in self.filters:
                print(f"  {f['field']} {f['operator']} {f['value']}")
                
        issues = self.validate()
        if issues:
            print("\n[ISSUES FOUND]:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("\n[CONFIGURATION VALID]")
            
        print("=" * 70)
        return len(issues) == 0


def show_interview_connection(scenario_name, your_parallel):
    """Show how this connects to your experience and interviews"""
    print("\n" + "=" * 70)
    print("INTERVIEW CONNECTION")
    print("=" * 70)
    
    print(f"\nScenario: {scenario_name}")
    print(f"\nYour Parallel Experience:\n{your_parallel}")
    
    print("\nHow to Explain This in Interview:")
    print('"I understand agent configuration from my automation experience.')
    print('At Thind Transport, I automated monthly reporting with VBA, which required:')
    print('  1. Defining data sources (what to pull from)')
    print('  2. Setting business rules (filters, thresholds)')
    print('  3. Mapping outputs (where results should go)')
    print('  4. Building in review steps (approval workflow)')
    print('This is exactly what FloQast Transform AI Agents do - just with a')
    print('natural language interface instead of code."')


# ============================================================================
# SCENARIO 1: MANUFACTURING COMPANY (Like Thind Transport)
# ============================================================================

def scenario_manufacturing():
    """Manufacturing company - Coupa PO accruals"""
    print("\n" + "#" * 70)
    print("SCENARIO 1: Manufacturing Company - Coupa Accruals")
    print("(Similar to Thind Transport)")
    print("#" * 70)
    
    print("""
CUSTOMER PROFILE:
- Company: Industrial Parts Manufacturing
- ERP: NetSuite
- Procurement: Coupa
- Problem: 3 hours/month manually creating PO accruals

THE ISSUE:
They receive goods/services before month-end but invoices arrive in the
next month. Need to accrue expenses to match the period.

YOUR TASK: Review and understand this agent configuration.
""")
    
    # Create the configuration
    agent = AgentConfiguration(
        name="Coupa PO Accrual Agent",
        customer_type="Manufacturing"
    )
    
    agent.set_core_config(
        description="Automatically create accrual journal entries for Coupa purchase orders with status 'Received-Not-Invoiced' as of month-end, mapping each expense category to the appropriate GL account",
        data_source="Coupa API",
        trigger="Last business day of month, 6:00 PM",
        materiality=500,  # Don't accrue small items
        approval=True     # Require review before posting
    )
    
    # GL Account mapping
    agent.add_gl_mapping("Maintenance", "6100-Maintenance Expense")
    agent.add_gl_mapping("Raw Materials", "5100-Materials Expense")
    agent.add_gl_mapping("Equipment", "6200-Equipment Expense")
    agent.add_gl_mapping("Professional Fees", "6400-Professional Fees")
    agent.add_gl_mapping("Utilities", "6500-Utilities Expense")
    agent.add_gl_mapping("Accrual Liability", "2100-Accrued Liabilities")
    
    # Filters
    agent.add_filter("Status", "equals", "Received-Not-Invoiced")
    agent.add_filter("Amount", ">=", "$500")
    agent.add_filter("Receipt_Date", "within", "Current Month")
    
    agent.display()
    
    # Sample output
    print("\nSAMPLE AGENT OUTPUT (what it would create):")
    print("-" * 70)
    print(f"{'Account':<40} {'Debit':>12} {'Credit':>12}")
    print("-" * 70)
    print(f"{'6100-Maintenance Expense':<40} ${'12,500':>10} {'':>12}")
    print(f"{'5100-Materials Expense':<40} ${'8,200':>10} {'':>12}")
    print(f"{'6400-Professional Fees':<40} ${'2,500':>10} {'':>12}")
    print(f"{'2100-Accrued Liabilities':<40} {'':>12} ${'23,200':>10}")
    print("-" * 70)
    print(f"{'TOTALS':<40} ${'23,200':>10} ${'23,200':>10}")
    print("\n[AWAITING APPROVAL] - Entry ready for accountant review")
    
    show_interview_connection(
        scenario_name="Manufacturing Coupa Accruals",
        your_parallel="""At Thind Transport, I handled similar accruals manually - fleet maintenance,
fuel charges, and insurance that needed to be recognized before invoices arrived.
I understand the matching principle and why timing matters for accurate financials.
My VBA automation experience (80% time savings) demonstrates I can translate
manual processes into automated workflows - exactly what this agent does."""
    )
    
    return agent


# ============================================================================
# SCENARIO 2: SAAS COMPANY
# ============================================================================

def scenario_saas():
    """SaaS company - Revenue recognition agent"""
    print("\n" + "#" * 70)
    print("SCENARIO 2: SaaS Company - Revenue Recognition")
    print("(Complex ASC 606 compliance)")
    print("#" * 70)
    
    print("""
CUSTOMER PROFILE:
- Company: B2B SaaS Platform
- Revenue Model: Annual subscriptions, billed upfront
- ERP: Intacct
- Problem: Complex rev rec calculations taking 8+ hours/month

THE ISSUE:
Customer pays $120,000 upfront for 12-month subscription.
Must recognize $10,000/month over the contract term (ASC 606).
Tracking hundreds of contracts is error-prone.

YOUR TASK: Understand how an agent would handle this.
""")
    
    agent = AgentConfiguration(
        name="SaaS Revenue Recognition Agent",
        customer_type="SaaS"
    )
    
    agent.set_core_config(
        description="Calculate monthly revenue recognition for all active subscription contracts based on contract start date, term, and total value. Create journal entries to move revenue from Deferred to Earned",
        data_source="Salesforce + Intacct API",
        trigger="First business day of month, 8:00 AM",
        materiality=1000,  # SaaS companies often have many small contracts
        approval=True
    )
    
    agent.add_gl_mapping("Subscription Revenue", "4100-SaaS Revenue")
    agent.add_gl_mapping("Deferred Revenue", "2400-Deferred Revenue")
    agent.add_gl_mapping("Professional Services", "4200-PS Revenue")
    
    agent.add_filter("Contract_Status", "equals", "Active")
    agent.add_filter("Recognition_Type", "equals", "Ratably")
    agent.add_filter("Monthly_Amount", ">=", "$1000")
    
    agent.display()
    
    print("\nSAMPLE AGENT OUTPUT:")
    print("-" * 70)
    print("Processing 150 active contracts...")
    print(f"\n{'Contract':<20} {'Monthly Rev':>15} {'Period':>15}")
    print("-" * 70)
    print(f"{'ACME Corp':<20} ${'10,000':>13} {'Jan 2025':>15}")
    print(f"{'Beta Inc':<20} ${'5,000':>13} {'Jan 2025':>15}")
    print(f"{'Gamma LLC':<20} ${'8,500':>13} {'Jan 2025':>15}")
    print("... (147 more contracts)")
    print("-" * 70)
    print(f"\n{'Account':<40} {'Debit':>12} {'Credit':>12}")
    print("-" * 70)
    print(f"{'2400-Deferred Revenue':<40} ${'485,000':>10} {'':>12}")
    print(f"{'4100-SaaS Revenue':<40} {'':>12} ${'485,000':>10}")
    print("-" * 70)
    
    show_interview_connection(
        scenario_name="SaaS Revenue Recognition",
        your_parallel="""In my consulting work, I dealt with revenue recognition for project-based
billing - recognizing revenue when services were delivered, not when invoiced.
I also automated Salesforce reporting for 2,000+ accounts, which required
understanding data relationships and business rules. This SaaS scenario
is more complex but uses the same principles: rules-based processing of
contract data to generate accurate journal entries."""
    )
    
    return agent


# ============================================================================
# SCENARIO 3: RETAIL COMPANY
# ============================================================================

def scenario_retail():
    """Retail company - Inventory accrual agent"""
    print("\n" + "#" * 70)
    print("SCENARIO 3: Retail Company - Inventory Accruals")
    print("(High volume, seasonal complexity)")
    print("#" * 70)
    
    print("""
CUSTOMER PROFILE:
- Company: Multi-location Retail Chain
- Inventory System: Oracle Retail
- ERP: Oracle Cloud
- Problem: Goods received at stores but not invoiced by month-end

THE ISSUE:
Holiday season means high volume of inventory receipts.
Must accrue for all goods received but not yet invoiced.
Manual process takes entire accounting team 2 days.

YOUR TASK: Understand configuration for high-volume scenarios.
""")
    
    agent = AgentConfiguration(
        name="Inventory Receipt Accrual Agent",
        customer_type="Retail"
    )
    
    agent.set_core_config(
        description="Create accrual entries for inventory received at all store locations where receipt is confirmed but invoice has not been matched. Aggregate by vendor and category for GL posting",
        data_source="Oracle Retail API",
        trigger="Month-end, after inventory cutoff (11:59 PM)",
        materiality=250,  # Lower threshold due to volume
        approval=True
    )
    
    agent.add_gl_mapping("Merchandise Inventory", "1400-Inventory")
    agent.add_gl_mapping("Goods in Transit", "1410-GIT Inventory")
    agent.add_gl_mapping("Vendor Accrual", "2150-Inventory Accrual")
    
    agent.add_filter("Receipt_Status", "equals", "Confirmed")
    agent.add_filter("Invoice_Status", "equals", "Not Matched")
    agent.add_filter("Receipt_Date", "<=", "Month End Cutoff")
    
    agent.display()
    
    print("\nSAMPLE AGENT OUTPUT:")
    print("-" * 70)
    print("Processing receipts from 85 store locations...")
    print("Total unmatched receipts: 1,247")
    print("Aggregated by vendor: 156 vendors")
    print(f"\n{'Account':<40} {'Debit':>12} {'Credit':>12}")
    print("-" * 70)
    print(f"{'1400-Inventory':<40} ${'2,450,000':>10} {'':>12}")
    print(f"{'2150-Inventory Accrual':<40} {'':>12} ${'2,450,000':>10}")
    print("-" * 70)
    print("\nBreakdown by Category:")
    print("  Apparel:        $1,200,000")
    print("  Electronics:      $850,000")
    print("  Home Goods:       $400,000")
    
    show_interview_connection(
        scenario_name="Retail Inventory Accruals",
        your_parallel="""While my direct experience is with smaller operations, I understand
inventory timing issues from Thind Transport's fleet parts inventory.
The key is ensuring cutoff is properly defined and all locations are
captured. My process improvement experience in consulting would help
me identify bottlenecks in a customer's current process and configure
the agent to address their specific pain points."""
    )
    
    return agent


# ============================================================================
# COMPARISON: YOUR AUTOMATION vs FLOQAST AGENTS
# ============================================================================

def compare_automation_approaches():
    """Show how your experience translates to FloQast"""
    print("\n" + "#" * 70)
    print("YOUR AUTOMATION EXPERIENCE vs FLOQAST AGENTS")
    print("#" * 70)
    
    print("""
YOUR VBA AUTOMATION (Thind Transport):
======================================
Data Source:    Excel exports from ERP
Trigger:        Manual run at month-end
Logic:          VBA code with IF statements and lookups
Output:         Formatted Excel report
Time Savings:   80% (8 hours -> 1.5 hours)
Maintenance:    You had to update code when rules changed

FLOQAST TRANSFORM AI AGENTS:
============================
Data Source:    Direct API connections (Coupa, NetSuite, Salesforce)
Trigger:        Automated scheduling (time or event-based)
Logic:          Natural language configuration (no code)
Output:         Journal entries posted to GL
Time Savings:   70-90% typically
Maintenance:    Non-technical users can update in GUI

THE TRANSLATION:
================
Your skills:                 How they apply at FloQast:
- Understanding data flows   -> Configuring data sources
- Business rule logic        -> Setting agent parameters
- Output formatting          -> GL mapping configuration
- Process documentation      -> Customer training
- Troubleshooting errors     -> Agent debugging/support

YOUR SALESFORCE AUTOMATION (2,000+ accounts):
=============================================
This is EXACTLY what FloQast does for accounting:
- You automated CRM workflows
- FloQast automates accounting workflows
- Same concept: rules + data + actions

INTERVIEW ANSWER:
"My automation experience directly translates to FloQast's approach.
At Thind Transport, I automated monthly reporting with VBA - defining
data sources, business rules, and output formats. With Salesforce,
I automated workflows for 2,000+ accounts. FloQast Transform AI Agents
use the same logic but with a natural language interface. I understand
how to translate a manual accounting process into an automated workflow."
""")


# ============================================================================
# CONFIGURATION CHALLENGE
# ============================================================================

def configuration_challenge():
    """Interactive challenge to test understanding"""
    print("\n" + "#" * 70)
    print("CONFIGURATION CHALLENGE")
    print("#" * 70)
    
    print("""
SCENARIO: A customer comes to you with this problem:

"We're a professional services firm. Our consultants submit time entries
in our project management system (Kantata). At month-end, we need to
accrue unbilled revenue for work performed but not yet invoiced.
Currently this takes our team 6 hours because we have 200+ active projects."

Your task: Answer these configuration questions.
""")
    
    questions = [
        {
            "question": "What should be the data source for this agent?",
            "correct": "kantata",
            "answer": "Kantata (project management system) API - that's where the time entries live"
        },
        {
            "question": "What filter condition identifies work needing accrual?",
            "correct": "unbilled",
            "answer": "Time Status = 'Approved' AND Invoice Status = 'Unbilled' AND Period = Current Month"
        },
        {
            "question": "What's a reasonable materiality threshold for professional services?",
            "correct": "500",
            "answer": "$500-$1,000 - professional services typically has higher-value transactions"
        },
        {
            "question": "Should approval be required? Why?",
            "correct": "yes",
            "answer": "Yes - unbilled revenue directly impacts financial statements and should be reviewed"
        },
        {
            "question": "What GL accounts would you map?",
            "correct": "revenue",
            "answer": "Debit: 1300-Unbilled Receivables (asset), Credit: 4100-Service Revenue (or Deferred Revenue depending on rev rec policy)"
        }
    ]
    
    print("Answer these questions (or press Enter to see the answer):\n")
    
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        try:
            user_answer = input("Your answer: ").strip().lower()
            if not user_answer:
                print(f"Answer: {q['answer']}")
            elif q['correct'] in user_answer:
                print(f"Correct! {q['answer']}")
            else:
                print(f"Close! The answer is: {q['answer']}")
        except (EOFError, KeyboardInterrupt):
            print(f"\nAnswer: {q['answer']}")
    
    print("\n" + "=" * 70)
    print("COMPLETE AGENT CONFIGURATION:")
    print("=" * 70)
    
    agent = AgentConfiguration(
        name="Professional Services Unbilled Revenue Agent",
        customer_type="Professional Services"
    )
    
    agent.set_core_config(
        description="Calculate unbilled revenue from approved time entries in Kantata for all active projects. Create accrual entries for work performed but not yet invoiced as of month-end",
        data_source="Kantata API",
        trigger="Last business day of month, after time entry cutoff",
        materiality=500,
        approval=True
    )
    
    agent.add_gl_mapping("Unbilled Revenue", "4100-Service Revenue")
    agent.add_gl_mapping("Unbilled Receivable", "1300-Unbilled A/R")
    
    agent.display()


# ============================================================================
# MAIN MENU
# ============================================================================

def main():
    print("\n" + "=" * 70)
    print("DAY 2: FLOQAST AGENT CONFIGURATION PRACTICE")
    print("Your Experience + FloQast Interview Prep")
    print("=" * 70)
    
    print("""
Your experience sources:
  - Thind Transport: VBA automation (80% time savings)
  - Consulting: Salesforce automation (2,000+ accounts)
  - Both: Process improvement and workflow design

Available Exercises:
  1 - Manufacturing Scenario (Coupa accruals - like Thind Transport)
  2 - SaaS Scenario (Revenue recognition)
  3 - Retail Scenario (Inventory accruals)
  4 - Your Automation vs FloQast Comparison
  5 - Configuration Challenge (Interactive Q&A)
  A - Run ALL exercises
  Q - Quit
""")
    
    exercises = {
        '1': scenario_manufacturing,
        '2': scenario_saas,
        '3': scenario_retail,
        '4': compare_automation_approaches,
        '5': configuration_challenge,
    }
    
    while True:
        try:
            choice = input("\nChoose exercise (1-5, A for all, Q to quit): ").strip().upper()
            
            if choice == 'Q':
                print("\n" + "=" * 70)
                print("DAY 2 SUMMARY")
                print("=" * 70)
                print("""
Key Agent Configuration Concepts:
  1. Data Source - Where does the data come from (Coupa, Salesforce, etc.)
  2. Trigger - When should the agent run (time or event-based)
  3. Filters - What data should be processed (status, date, amount)
  4. Materiality - Minimum threshold to avoid noise
  5. GL Mapping - Which accounts for debit/credit sides
  6. Approval - Should someone review before posting

Your Experience Connection:
  - VBA automation = understanding business rules and data flows
  - Salesforce = experience with API-based data integration
  - Process improvement = ability to identify what should be automated

Interview Answer:
"I understand agent configuration from my automation experience.
At Thind Transport, I automated reporting that required defining
data sources, business rules, and output mapping. This is exactly
what FloQast agents do with a natural language interface."

Next: Continue to Day 3 for customer roleplay scenarios!
""")
                break
            
            elif choice == 'A':
                print("\nRunning all exercises...")
                for key in ['1', '2', '3', '4', '5']:
                    exercises[key]()
                    try:
                        input("\nPress Enter for next exercise...")
                    except (EOFError, KeyboardInterrupt):
                        pass
            
            elif choice in exercises:
                exercises[choice]()
            
            else:
                print("Invalid choice. Enter 1-5, A, or Q.")
                
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except EOFError:
            # Non-interactive mode
            print("\nRunning all exercises (non-interactive)...")
            for key in ['1', '2', '3', '4']:
                exercises[key]()
            break


if __name__ == "__main__":
    main()

