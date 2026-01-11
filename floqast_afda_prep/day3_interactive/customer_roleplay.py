# -*- coding: utf-8 -*-
"""
Day 3: Customer Roleplay & Objection Handling
Your Experience + FloQast Interview Prep

AI plays the skeptical customer. YOU demonstrate:
- Discovery questions (from your consulting experience)
- Value proposition delivery
- Objection handling
- Technical problem-solving

Run: py customer_roleplay.py
"""

import sys

# ============================================================================
# CUSTOMER SCENARIOS
# ============================================================================

class CustomerScenario:
    def __init__(self, scenario_num):
        self.scenario_num = scenario_num
        self.conversation = []
        self.score = {
            'discovery': 0,
            'technical': 0,
            'objection_handling': 0,
            'communication': 0
        }
        self.setup_scenario()
        
    def setup_scenario(self):
        """Configure scenario details"""
        scenarios = {
            1: {
                'title': '"I Don\'t Trust AI With Accounting"',
                'customer': 'Sarah Chen, CFO',
                'company': 'Precision Parts Manufacturing',
                'context': 'Mid-sized manufacturing company, skeptical of AI',
                'your_experience': 'Similar to client presentations in consulting'
            },
            2: {
                'title': '"We Already Have a System That Works"',
                'customer': 'Michael Davis, Controller',
                'company': 'CloudSoft SaaS',
                'context': 'Growing SaaS company, invested in current tools',
                'your_experience': 'Change management from process improvement projects'
            },
            3: {
                'title': '"This Seems Too Expensive"',
                'customer': 'Jennifer Liu, VP Finance',
                'company': 'Urban Retail Group',
                'context': 'Retail chain, tight budgets, needs clear ROI',
                'your_experience': 'ROI modeling from consulting financial analysis'
            },
            4: {
                'title': '"Our Processes Are Too Unique"',
                'customer': 'David Park, Accounting Director',
                'company': 'Professional Services International',
                'context': 'Complex billing, multi-entity, thinks they are special',
                'your_experience': 'Understanding complex client requirements'
            }
        }
        self.scenario = scenarios.get(scenario_num, scenarios[1])
        
    def play(self):
        """Run the roleplay scenario"""
        print("\n" + "=" * 70)
        print(f"SCENARIO {self.scenario_num}: {self.scenario['title']}")
        print("=" * 70)
        print(f"\nCustomer: {self.scenario['customer']}")
        print(f"Company: {self.scenario['company']}")
        print(f"Context: {self.scenario['context']}")
        print(f"\nYour Parallel: {self.scenario['your_experience']}")
        print("=" * 70)
        
        if self.scenario_num == 1:
            return self.scenario_ai_trust()
        elif self.scenario_num == 2:
            return self.scenario_status_quo()
        elif self.scenario_num == 3:
            return self.scenario_price()
        elif self.scenario_num == 4:
            return self.scenario_unique()
        
    def scenario_ai_trust(self):
        """Scenario 1: Customer doesn't trust AI"""
        print(f"\n[{self.scenario['customer']}]:")
        print("I'll be honest with you - I'm skeptical of all this AI stuff.")
        print("Accounting requires precision. One wrong journal entry and we have")
        print("audit issues. How can I trust AI with something so critical?\n")
        
        response = self.get_response("How do you respond to this skepticism?")
        
        # Evaluate response
        good_keywords = ['human', 'review', 'approval', 'control', 'audit', 'validate']
        if any(k in response.lower() for k in good_keywords):
            self.score['objection_handling'] += 4
            self.score['communication'] += 3
            print(f"\n[{self.scenario['customer']}]:")
            print("Okay, so humans still review everything. That's reassuring.")
            print("But what if the AI makes systematic errors we don't catch?")
        else:
            self.score['objection_handling'] += 1
            print(f"\n[{self.scenario['customer']}]:")
            print("That doesn't really address my concern about AI reliability...")
        
        response = self.get_response("How do you address concerns about AI errors?")
        
        if any(k in response.lower() for k in ['same', 'consistent', 'rules', 'transparent', 'log', 'trail']):
            self.score['technical'] += 4
            self.score['objection_handling'] += 3
            print(f"\n[{self.scenario['customer']}]:")
            print("I like that it follows defined rules, not just making things up.")
            print("Can you show me a specific example of what it would do?")
        else:
            self.score['technical'] += 1
            print(f"\n[{self.scenario['customer']}]:")
            print("I'm still not convinced. Give me a concrete example.")
        
        response = self.get_response("Give a specific example of automation with controls")
        
        if 'journal' in response.lower() or 'accrual' in response.lower() or 'entry' in response.lower():
            self.score['technical'] += 3
            self.score['communication'] += 2
            print(f"\n[{self.scenario['customer']}]:")
            print("That makes sense. So it's more like a very smart template than AI magic.")
            print("I think I could get comfortable with that approach.")
        else:
            self.score['communication'] += 1
            print(f"\n[{self.scenario['customer']}]:")
            print("Hmm, I need more details but I appreciate your time.")
        
        self.show_ideal_response(
            objection="I don't trust AI with accounting",
            ideal_approach="""
1. ACKNOWLEDGE the concern (don't dismiss it)
   "Your concern is valid - accounting requires precision. That's exactly why 
   FloQast built Transform AI with accountants, not just engineers."

2. REFRAME the technology
   "Think of it less as 'AI making decisions' and more as 'intelligent automation
   with human oversight.' The AI follows rules YOU define, and every action
   requires human approval before posting."

3. EMPHASIZE controls
   "Every journal entry shows an audit trail - what data was used, what rules
   were applied, and who approved it. Your auditors will have full visibility."

4. GIVE a specific example
   "For example, a Coupa accrual agent would: Pull POs with status 
   'Received-Not-Invoiced', apply your materiality threshold, map to your
   GL accounts, and create a DRAFT entry for your team to review. Nothing
   posts without human approval."
""",
            your_experience="In consulting, you presented recommendations to skeptical stakeholders. The key was showing specific examples and addressing concerns directly, not dismissing them."
        )
        
        return self.evaluate()
    
    def scenario_status_quo(self):
        """Scenario 2: Customer wants to keep current system"""
        print(f"\n[{self.scenario['customer']}]:")
        print("Look, we've spent years building our current processes. We have")
        print("spreadsheets that work. Our team knows how to do this. Why would")
        print("I disrupt everything for a new tool?\n")
        
        response = self.get_response("How do you handle the status quo objection?")
        
        if any(k in response.lower() for k in ['understand', 'tell me', 'current', 'process', 'how long', 'pain']):
            self.score['discovery'] += 4
            self.score['communication'] += 2
            print(f"\n[{self.scenario['customer']}]:")
            print("Well... the spreadsheet reconciliation takes about 2 days per month.")
            print("And honestly, we've had errors that caused restatements before.")
        else:
            self.score['discovery'] += 1
            print(f"\n[{self.scenario['customer']}]:")
            print("That's a pitch, not a question. What about MY specific situation?")
        
        response = self.get_response("Dig deeper into their pain points")
        
        if any(k in response.lower() for k in ['2 days', 'time', 'errors', 'restatement', 'cost']):
            self.score['objection_handling'] += 4
            self.score['technical'] += 2
            print(f"\n[{self.scenario['customer']}]:")
            print("Yeah, those restatements were painful. And we're hiring another")
            print("accountant next quarter because we can't keep up with growth.")
        else:
            self.score['objection_handling'] += 1
            print(f"\n[{self.scenario['customer']}]:")
            print("I'm not sure that applies to us specifically...")
        
        response = self.get_response("Connect their pain to the solution")
        
        if 'scale' in response.lower() or 'grow' in response.lower() or 'automate' in response.lower():
            self.score['technical'] += 3
            self.score['communication'] += 3
            print(f"\n[{self.scenario['customer']}]:")
            print("Hmm, if we could handle more volume without adding headcount...")
            print("That's actually a compelling argument. Tell me more about ROI.")
        else:
            self.score['communication'] += 1
            print(f"\n[{self.scenario['customer']}]:")
            print("I see your point. I'll think about it.")
        
        self.show_ideal_response(
            objection="We already have a system that works",
            ideal_approach="""
1. DON'T attack their current process
   "Your team has clearly built something that functions. Let me understand
   it better so I can see where FloQast might add value."

2. ASK discovery questions to find pain
   "How much time does the reconciliation take?"
   "When was the last error that caused extra work?"
   "What happens when team members are out sick?"

3. CONNECT their pain to the solution
   "So you're spending 2 days per month on reconciliations, and growth means
   you need to hire. What if AutoRec could reduce that 2 days to 2 hours,
   letting your current team handle more volume?"

4. ADDRESS change management
   "I understand change is hard. FloQast implementations are gradual - 
   we'd start with one reconciliation type, prove the value, then expand."
""",
            your_experience="In process improvement consulting, you learned that people resist change when they feel their work is being criticized. Discovery questions reveal pain THEY recognize, making change feel like THEIR idea."
        )
        
        return self.evaluate()
    
    def scenario_price(self):
        """Scenario 3: Customer focused on cost"""
        print(f"\n[{self.scenario['customer']}]:")
        print("We've seen the pricing. It's a significant investment, especially")
        print("given our tight budgets this year. How do you justify the cost?")
        print("We can't just throw money at software and hope for ROI.\n")
        
        response = self.get_response("How do you handle the price objection?")
        
        if any(k in response.lower() for k in ['understand', 'budget', 'tell me', 'current', 'spend', 'cost']):
            self.score['discovery'] += 4
            self.score['objection_handling'] += 2
            print(f"\n[{self.scenario['customer']}]:")
            print("Well, we have 3 accountants working on close activities.")
            print("Combined salary is probably $250K. They spend about 40% of their")
            print("time on tasks that could potentially be automated.")
        else:
            self.score['discovery'] += 1
            print(f"\n[{self.scenario['customer']}]:")
            print("Sure, but I need specifics. What's the actual ROI?")
        
        response = self.get_response("Calculate and present ROI")
        
        if 'roi' in response.lower() or 'save' in response.lower() or '100k' in response.lower() or 'payback' in response.lower():
            self.score['technical'] += 4
            self.score['communication'] += 3
            print(f"\n[{self.scenario['customer']}]:")
            print("A 3-4 month payback period sounds reasonable. But what about")
            print("implementation costs and the time we'd lose during transition?")
        else:
            self.score['technical'] += 1
            print(f"\n[{self.scenario['customer']}]:")
            print("Those are nice numbers, but they feel made up...")
        
        response = self.get_response("Address implementation and hidden costs")
        
        if 'implement' in response.lower() or 'support' in response.lower() or 'included' in response.lower():
            self.score['objection_handling'] += 3
            self.score['communication'] += 2
            print(f"\n[{self.scenario['customer']}]:")
            print("I appreciate the transparency. If the implementation is as smooth")
            print("as you describe, this could work for us. Let's discuss a pilot.")
        else:
            self.score['communication'] += 1
            print(f"\n[{self.scenario['customer']}]:")
            print("I have concerns about hidden costs, but I'll review internally.")
        
        self.show_ideal_response(
            objection="This seems too expensive",
            ideal_approach="""
1. UNDERSTAND their cost context first
   "What does your close process currently cost in terms of time and people?"
   "Have you calculated the cost of errors or delayed closes?"

2. BUILD ROI with their numbers
   "So you have 3 accountants spending 40% on close activities - that's 
   about $100K annually in labor. If FloQast automates half of that,
   you're saving $50K+ per year. Against the software cost, that's a
   payback period of X months."

3. ADDRESS total cost of ownership
   "Implementation is included in the subscription. Your team will be trained
   by AFDAs like myself. Ongoing support is also included. There are no
   hidden costs beyond what you see in the contract."

4. OFFER a pilot
   "Let's start with one high-value use case - maybe your bank reconciliations.
   We can prove ROI on a small scale before expanding."
""",
            your_experience="In consulting, you built financial models and ROI calculations for clients. You know how to translate operational improvements into dollar savings. Use those same skills here."
        )
        
        return self.evaluate()
    
    def scenario_unique(self):
        """Scenario 4: Customer thinks they're too special"""
        print(f"\n[{self.scenario['customer']}]:")
        print("I appreciate you reaching out, but our business is complex.")
        print("We have 6 entities, intercompany transactions, project-based billing,")
        print("and custom revenue recognition rules. I doubt FloQast can handle it.\n")
        
        response = self.get_response("How do you handle 'we're too unique' objection?")
        
        if any(k in response.lower() for k in ['similar', 'customer', 'handle', 'tell me', 'understand', 'specific']):
            self.score['discovery'] += 4
            self.score['communication'] += 2
            print(f"\n[{self.scenario['customer']}]:")
            print("Really? You have customers with multi-entity intercompany?")
            print("What about project-based billing with milestone recognition?")
        else:
            self.score['discovery'] += 1
            print(f"\n[{self.scenario['customer']}]:")
            print("You're just saying that. Give me a specific example.")
        
        response = self.get_response("Show relevant experience")
        
        if 'professional services' in response.lower() or 'similar' in response.lower() or 'configure' in response.lower():
            self.score['technical'] += 4
            self.score['objection_handling'] += 3
            print(f"\n[{self.scenario['customer']}]:")
            print("Okay, that's interesting. But our Chart of Accounts is")
            print("completely custom. Will we have to change it?")
        else:
            self.score['technical'] += 1
            print(f"\n[{self.scenario['customer']}]:")
            print("That's generic. What about OUR specific complexity?")
        
        response = self.get_response("Address their specific concern about customization")
        
        if 'map' in response.lower() or 'adapt' in response.lower() or 'configure' in response.lower():
            self.score['technical'] += 3
            self.score['communication'] += 3
            print(f"\n[{self.scenario['customer']}]:")
            print("I like that you adapt to us, not the other way around.")
            print("Let's schedule a deeper dive into our specific requirements.")
        else:
            self.score['communication'] += 1
            print(f"\n[{self.scenario['customer']}]:")
            print("Hmm, I'm still not sure it will work, but I'll consider it.")
        
        self.show_ideal_response(
            objection="Our processes are too unique",
            ideal_approach="""
1. VALIDATE their complexity (don't dismiss)
   "Multi-entity with intercompany and project-based billing IS complex.
   That's exactly the type of situation where FloQast adds value."

2. SHOW similar customers
   "We work with 50+ professional services firms with similar setups.
   Company X had 8 entities with intercompany, and we helped them
   reduce close time from 12 days to 5."

3. EMPHASIZE configurability
   "FloQast doesn't force you into a template. We map to YOUR Chart of
   Accounts, YOUR workflows, YOUR approval chains. The agent configuration
   is customized to your specific rules."

4. OFFER a discovery session
   "Let's schedule a 30-minute discovery call where you walk me through
   your specific intercompany scenarios. I'll show you exactly how
   FloQast would handle each one."
""",
            your_experience="In consulting, clients often believed their problems were unique. You learned that most 'unique' situations follow common patterns. The key is making clients feel heard while showing you've solved similar problems."
        )
        
        return self.evaluate()
    
    def get_response(self, prompt):
        """Get user input with prompt"""
        try:
            response = input(f"\n[YOU - {prompt}]: ").strip()
            self.conversation.append(response)
            return response
        except (EOFError, KeyboardInterrupt):
            return ""
    
    def show_ideal_response(self, objection, ideal_approach, your_experience):
        """Display the ideal response framework"""
        print("\n" + "=" * 70)
        print("IDEAL RESPONSE FRAMEWORK")
        print("=" * 70)
        print(f"\nObjection: {objection}")
        print(f"\nIdeal Approach:{ideal_approach}")
        print(f"\nYour Experience Connection:\n{your_experience}")
        print("=" * 70)
    
    def evaluate(self):
        """Score the interaction"""
        print("\n" + "=" * 70)
        print("EVALUATION")
        print("=" * 70)
        
        total = sum(self.score.values())
        max_total = 40  # 10 points per category
        
        print(f"\nDiscovery:         {self.score['discovery']}/10")
        print(f"Technical:         {self.score['technical']}/10")
        print(f"Objection Handling: {self.score['objection_handling']}/10")
        print(f"Communication:     {self.score['communication']}/10")
        print("-" * 30)
        print(f"TOTAL: {total}/{max_total} ({int(total/max_total*100)}%)")
        
        if total >= 30:
            print("\nExcellent! You handled this like a pro.")
        elif total >= 20:
            print("\nGood work! Practice the ideal response framework.")
        else:
            print("\nKeep practicing! Focus on discovery and specifics.")
        
        return total >= 25


# ============================================================================
# INTERVIEW CONNECTION
# ============================================================================

def show_interview_tips():
    """Display interview tips for customer-facing questions"""
    print("\n" + "=" * 70)
    print("INTERVIEW TIPS: CUSTOMER-FACING QUESTIONS")
    print("=" * 70)
    
    print("""
Common Interview Questions About Customer Work:

1. "How would you handle a skeptical customer?"
   YOUR ANSWER: "In my consulting work, I presented to skeptical stakeholders
   regularly. My approach: acknowledge their concern, ask discovery questions
   to understand the root cause, then show a specific example that addresses
   it. I never dismiss objections - I address them directly with evidence."

2. "Describe a time you overcame resistance to change"
   YOUR ANSWER: "When automating Salesforce workflows for 2,000+ accounts,
   users were concerned about losing control. I involved key stakeholders
   in the design, showed them how the new process gave them MORE visibility
   not less, and started with a pilot to prove value before full rollout."

3. "How do you build relationships with customers?"
   YOUR ANSWER: "I focus on understanding their problems before proposing
   solutions. At Thind Transport, I learned that each department had different
   priorities. I scheduled time with stakeholders individually to understand
   their needs, then presented solutions that addressed everyone's concerns."

4. "How do you explain technical concepts to non-technical users?"
   YOUR ANSWER: "I use analogies and specific examples. For journal entries,
   I might say 'Think of it like a ledger where every dollar in has to be
   matched by a dollar out.' Then I show a concrete example with their actual
   data. I check for understanding and adjust my explanation as needed."

Your Experience Connection:
- Consulting: Client presentations, stakeholder management, process improvement
- Thind Transport: Working with different departments, explaining financial concepts
- Both: Building trust through transparency and delivering results
""")


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("\n" + "=" * 70)
    print("DAY 3: CUSTOMER ROLEPLAY & OBJECTION HANDLING")
    print("Your Experience + FloQast Interview Prep")
    print("=" * 70)
    
    print("""
Your experience sources:
  - Consulting: Client presentations, stakeholder management
  - Thind Transport: Cross-functional collaboration
  - Both: Handling skepticism, proving value

Available Scenarios:
  1 - "I Don't Trust AI" (Tech skepticism)
  2 - "We Already Have a System" (Status quo)
  3 - "This Seems Expensive" (Price objection)
  4 - "We're Too Unique" (Special snowflake)
  T - Show Interview Tips
  Q - Quit
""")
    
    while True:
        try:
            choice = input("\nChoose scenario (1-4, T for tips, Q to quit): ").strip().upper()
            
            if choice == 'Q':
                print("\n" + "=" * 70)
                print("DAY 3 SUMMARY")
                print("=" * 70)
                print("""
Key Objection Handling Skills:
  1. Acknowledge - Don't dismiss concerns
  2. Discover - Ask questions to understand root cause
  3. Reframe - Show the solution addresses their specific concern
  4. Evidence - Use examples from similar customers
  5. Pilot - Offer a low-risk way to prove value

Your Consulting Experience = Your Advantage:
  - You've presented to skeptical stakeholders before
  - You know how to build ROI models
  - You understand change management
  - You can translate technical to business value

Next: Continue to Day 4 for teaching/training scenarios!
""")
                break
            
            elif choice == 'T':
                show_interview_tips()
            
            elif choice in ['1', '2', '3', '4']:
                scenario = CustomerScenario(int(choice))
                scenario.play()
            
            else:
                print("Invalid choice. Enter 1-4, T, or Q.")
                
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except EOFError:
            # Non-interactive mode
            print("\nRunning in demo mode (non-interactive)...")
            show_interview_tips()
            break


if __name__ == "__main__":
    main()
