# -*- coding: utf-8 -*-
"""
Day 4: Teaching & Enablement Practice
Your Experience + FloQast Interview Prep

Practice explaining technical concepts clearly - a core AFDA skill.
Based on YOUR experience:
- Client presentations in consulting
- Training stakeholders at Thind Transport
- Explaining complex topics simply

Run: py teach_the_ai.py
"""

import sys

# ============================================================================
# TEACHING SCENARIOS
# ============================================================================

class TeachingScenario:
    def __init__(self, scenario_num):
        self.scenario_num = scenario_num
        self.student_understanding = 0
        self.teaching_score = {'clarity': 0, 'patience': 0, 'completeness': 0}
        self.setup_scenario()
        
    def setup_scenario(self):
        """Configure scenario"""
        scenarios = {
            1: {
                'title': 'Explain: What is an Accrual?',
                'student': 'New staff accountant, 6 months experience',
                'context': 'Customer training session on FloQast accrual agents',
                'your_experience': 'Explaining financial concepts at Thind Transport'
            },
            2: {
                'title': 'Explain: Bank Reconciliation Process',
                'student': 'Finance manager, non-accounting background',
                'context': 'Onboarding session for new AutoRec user',
                'your_experience': 'Teaching spreadsheet processes to colleagues'
            },
            3: {
                'title': 'Explain: How FloQast Agents Work',
                'student': 'CFO evaluating the product',
                'context': 'Executive demo - needs high-level understanding',
                'your_experience': 'Executive presentations in consulting'
            },
            4: {
                'title': 'Troubleshoot: Agent Not Working',
                'student': 'Frustrated power user',
                'context': 'Support call for agent failure',
                'your_experience': 'Debugging VBA automation issues'
            }
        }
        self.scenario = scenarios.get(scenario_num, scenarios[1])
        
    def run(self):
        """Execute the teaching scenario"""
        print("\n" + "=" * 70)
        print(f"SCENARIO {self.scenario_num}: {self.scenario['title']}")
        print("=" * 70)
        print(f"\nStudent: {self.scenario['student']}")
        print(f"Context: {self.scenario['context']}")
        print(f"Your Experience: {self.scenario['your_experience']}")
        print("=" * 70)
        
        if self.scenario_num == 1:
            return self.teach_accruals()
        elif self.scenario_num == 2:
            return self.teach_bank_rec()
        elif self.scenario_num == 3:
            return self.teach_agents_to_cfo()
        elif self.scenario_num == 4:
            return self.troubleshoot_support()
    
    def get_response(self, prompt):
        """Get teaching response"""
        try:
            return input(f"\n[YOU]: ").strip()
        except (EOFError, KeyboardInterrupt):
            return ""
    
    def teach_accruals(self):
        """Teach accrual accounting basics"""
        print("\n[STUDENT - New Staff Accountant]:")
        print("I'm looking at this accrual entry the agent created, but I don't")
        print("really understand why we're recording an expense when we haven't")
        print("received an invoice yet. Isn't that premature?")
        
        response = self.get_response("")
        
        # Check for good teaching approach
        if any(k in response.lower() for k in ['matching', 'period', 'timing', 'when the expense happened']):
            self.teaching_score['clarity'] += 5
            self.student_understanding += 25
            print("\n[STUDENT]: Oh, so it's about recording expenses in the period")
            print("they actually happened, not when we get the paperwork?")
        elif 'expense' in response.lower() or 'debit' in response.lower():
            self.teaching_score['clarity'] += 2
            self.student_understanding += 10
            print("\n[STUDENT]: I understand expenses are debits, but WHY record")
            print("them before we have the invoice?")
        else:
            self.teaching_score['clarity'] += 1
            print("\n[STUDENT]: I'm still not sure I understand the purpose...")
        
        response = self.get_response("")
        
        if 'matching principle' in response.lower() or 'accurate' in response.lower() or 'close' in response.lower():
            self.teaching_score['clarity'] += 4
            self.teaching_score['completeness'] += 3
            self.student_understanding += 25
            print("\n[STUDENT]: So if we received $10,000 of maintenance in December,")
            print("we need to show that as a December expense even if the bill comes")
            print("in January. Otherwise December looks too profitable!")
        else:
            self.student_understanding += 10
            print("\n[STUDENT]: I think I'm starting to understand...")
        
        response = self.get_response("")
        
        if 'reverse' in response.lower() or 'next month' in response.lower() or 'invoice arrives' in response.lower():
            self.teaching_score['completeness'] += 4
            self.student_understanding += 20
            print("\n[STUDENT]: Got it! So we accrue now, then reverse when the")
            print("invoice comes and record the actual payment. That makes sense!")
        else:
            self.student_understanding += 5
            print("\n[STUDENT]: Okay, thanks for explaining.")
        
        self.show_teaching_tip(
            topic="Explaining Accruals",
            ideal_explanation="""
1. START with the WHY (business purpose)
   "Financial statements need to show what ACTUALLY happened in a period.
   If we got $10,000 of maintenance done in December, December should
   show that expense - even if the bill doesn't come until January."

2. USE a simple analogy
   "Think of it like a credit card. You made the purchase in December,
   so that's when the expense really happened, even though you pay the
   bill in January."

3. WALK through the mechanics
   "The entry is: Debit Maintenance Expense $10,000 (recording the expense),
   Credit Accrued Liabilities $10,000 (we owe this but haven't been billed).
   In January, we reverse it when the invoice arrives."

4. CONNECT to their work
   "The FloQast agent does this automatically by looking at Coupa POs that
   show goods were received but not yet invoiced."
""",
            your_experience="At Thind Transport, you explained month-end entries to non-accounting colleagues. The key was using real examples they could relate to."
        )
        
        return self.evaluate()
    
    def teach_bank_rec(self):
        """Teach bank reconciliation process"""
        print("\n[STUDENT - Finance Manager]:")
        print("I came from operations and I'm not clear on what bank reconciliation")
        print("actually accomplishes. We have the bank statement, we have our books -")
        print("why do we need to reconcile them? Shouldn't they just match?")
        
        response = self.get_response("")
        
        if any(k in response.lower() for k in ['timing', 'different', 'not always', 'delay']):
            self.teaching_score['clarity'] += 4
            self.student_understanding += 20
            print("\n[STUDENT]: So the bank and our books might show different numbers")
            print("because of timing? Like if we write a check on the 30th but it")
            print("doesn't clear until the 3rd?")
        else:
            self.teaching_score['clarity'] += 1
            print("\n[STUDENT]: I'm not following why they wouldn't match...")
        
        response = self.get_response("")
        
        if 'outstanding check' in response.lower() or 'deposit in transit' in response.lower():
            self.teaching_score['clarity'] += 4
            self.teaching_score['patience'] += 3
            self.student_understanding += 25
            print("\n[STUDENT]: Outstanding checks and deposits in transit - got it!")
            print("What about things on the bank statement we didn't record?")
        else:
            self.student_understanding += 10
            print("\n[STUDENT]: Can you give me specific examples?")
        
        response = self.get_response("")
        
        if any(k in response.lower() for k in ['bank charge', 'fee', 'service charge', 'interest']):
            self.teaching_score['completeness'] += 4
            self.student_understanding += 25
            print("\n[STUDENT]: So bank charges and interest we might not know about")
            print("until we see the statement. We need to record those!")
        else:
            self.student_understanding += 10
            print("\n[STUDENT]: Okay, I think I understand the concept...")
        
        response = self.get_response("")
        
        if 'autorec' in response.lower() or 'automate' in response.lower() or 'match' in response.lower():
            self.teaching_score['completeness'] += 4
            self.student_understanding += 20
            print("\n[STUDENT]: So FloQast AutoRec does this matching automatically,")
            print("and I just review the exceptions? That sounds way faster!")
        else:
            self.student_understanding += 10
            print("\n[STUDENT]: Thanks for the explanation!")
        
        self.show_teaching_tip(
            topic="Explaining Bank Reconciliation",
            ideal_explanation="""
1. START with a simple truth
   "Your books and the bank often show different numbers - and that's normal.
   Reconciliation figures out WHY they're different and ensures nothing is
   wrong or missing."

2. GIVE concrete examples of differences
   "Outstanding checks - you wrote a check on 12/30, but the recipient
   hasn't cashed it yet, so the bank doesn't show it.
   
   Deposits in transit - you deposited cash on 12/31, but the bank
   didn't process it until 1/2.
   
   Bank charges - the bank charged you $25 for a service fee, but you
   didn't know about it until you saw the statement."

3. EXPLAIN the purpose
   "Reconciliation ensures we catch everything - mistakes, fraud, missing
   entries. It's a key internal control."

4. CONNECT to FloQast
   "AutoRec does the matching automatically - it looks for transactions
   with matching amounts and dates, and flags the exceptions for human
   review. Most customers see 38% faster reconciliations."
""",
            your_experience="You've done bank reconciliations at Thind Transport. Use that hands-on experience to make explanations concrete."
        )
        
        return self.evaluate()
    
    def teach_agents_to_cfo(self):
        """Executive-level explanation of FloQast agents"""
        print("\n[STUDENT - CFO]:")
        print("I've heard about 'AI agents' but I need to understand what they")
        print("actually do before I approve this purchase. No buzzwords please -")
        print("just tell me in plain English what this means for my team.")
        
        response = self.get_response("")
        
        if any(k in response.lower() for k in ['automate', 'repetitive', 'manual', 'time']):
            self.teaching_score['clarity'] += 4
            self.student_understanding += 20
            print("\n[CFO]: So it takes over the repetitive tasks. Give me a specific")
            print("example - what's one thing my team does today that this would handle?")
        else:
            self.teaching_score['clarity'] += 1
            print("\n[CFO]: That's too abstract. Give me a concrete example.")
        
        response = self.get_response("")
        
        if any(k in response.lower() for k in ['accrual', 'coupa', 'journal entry', 'month-end']):
            self.teaching_score['clarity'] += 5
            self.teaching_score['completeness'] += 3
            self.student_understanding += 30
            print("\n[CFO]: So instead of someone pulling data from Coupa, looking up")
            print("the right accounts, and creating an entry manually... the agent")
            print("does all that and presents a draft for approval?")
        else:
            self.student_understanding += 10
            print("\n[CFO]: I need a specific example, not generalities.")
        
        response = self.get_response("")
        
        if 'review' in response.lower() or 'approve' in response.lower() or 'human' in response.lower():
            self.teaching_score['completeness'] += 4
            self.teaching_score['patience'] += 3
            self.student_understanding += 25
            print("\n[CFO]: Good - humans still approve everything. What's the ROI?")
            print("How much time does this actually save?")
        else:
            self.student_understanding += 10
            print("\n[CFO]: And my team still reviews it?")
        
        response = self.get_response("")
        
        if any(k in response.lower() for k in ['hour', 'day', 'percent', 'time', 'faster']):
            self.teaching_score['completeness'] += 4
            self.student_understanding += 20
            print("\n[CFO]: 2-3 hours saved per month on just one process? And there")
            print("are multiple processes we could automate? That adds up.")
            print("Let's move forward with a pilot.")
        else:
            self.student_understanding += 10
            print("\n[CFO]: I need to see numbers before I can make a decision.")
        
        self.show_teaching_tip(
            topic="Executive-Level Explanation",
            ideal_explanation="""
1. NO JARGON - business language only
   "FloQast agents automate the manual, repetitive tasks your accounting
   team does every month - pulling data, creating entries, matching
   transactions."

2. ONE CONCRETE EXAMPLE
   "Right now, someone on your team spends 3 hours each month pulling
   Coupa purchase orders, looking up the right GL accounts, and creating
   accrual entries. An agent does that in minutes and presents a draft
   for your team to review and approve."

3. ADDRESS THE CONCERN (control)
   "Your team still reviews and approves everything. The agent doesn't
   post anything without human sign-off. It's not replacing judgment -
   it's replacing data entry."

4. ROI IN THEIR TERMS
   "If we automate 5 processes that each take 3 hours, that's 15 hours
   per month your team gets back. They can focus on analysis and
   strategic work instead of manual tasks."
""",
            your_experience="In consulting, you presented to executives who wanted bottom-line impact, not technical details. Lead with business value."
        )
        
        return self.evaluate()
    
    def troubleshoot_support(self):
        """Handle a frustrated customer support call"""
        print("\n[STUDENT - Frustrated User]:")
        print("Look, I've been using FloQast for 6 months and this agent has")
        print("been working fine. Now it just says 'failed' and I have month-end")
        print("tomorrow. I don't have time for this. Fix it!")
        
        response = self.get_response("")
        
        if any(k in response.lower() for k in ['understand', 'frustrating', 'help you', 'let me']):
            self.teaching_score['patience'] += 4
            self.student_understanding += 15
            print("\n[USER]: *sighs* Okay, thank you. The error says 'API connection")
            print("failed - authentication error'. I don't know what that means.")
        else:
            self.teaching_score['patience'] += 1
            print("\n[USER]: Can you just fix it? I don't have time for questions.")
        
        response = self.get_response("")
        
        if any(k in response.lower() for k in ['credential', 'password', 'api key', 'expired', 'changed']):
            self.teaching_score['clarity'] += 4
            self.teaching_score['completeness'] += 3
            self.student_understanding += 25
            print("\n[USER]: Oh, we did change our Coupa password last week for")
            print("security. Could that be it?")
        else:
            self.student_understanding += 10
            print("\n[USER]: I don't understand what you're asking...")
        
        response = self.get_response("")
        
        if 'update' in response.lower() or 'new password' in response.lower() or 'settings' in response.lower():
            self.teaching_score['clarity'] += 4
            self.teaching_score['completeness'] += 4
            self.student_understanding += 30
            print("\n[USER]: I see it - there's a Coupa connection settings page.")
            print("I'll update the password here. Then what?")
        else:
            self.student_understanding += 10
            print("\n[USER]: Where do I update it?")
        
        response = self.get_response("")
        
        if 'test' in response.lower() or 'rerun' in response.lower() or 'try again' in response.lower():
            self.teaching_score['patience'] += 4
            self.student_understanding += 25
            print("\n[USER]: Okay, I updated it and tested the connection - it works!")
            print("I'll rerun the agent now. Thank you so much for your patience!")
        else:
            self.student_understanding += 10
            print("\n[USER]: Is that all? How do I know it's fixed?")
        
        self.show_teaching_tip(
            topic="Support Call with Frustrated User",
            ideal_explanation="""
1. ACKNOWLEDGE their frustration first
   "I completely understand - month-end pressure is real, and having a
   tool fail at this moment is frustrating. Let me help you get this
   working right away."

2. ASK clarifying questions calmly
   "What's the exact error message you're seeing?"
   "Has anything changed recently - passwords, system updates?"

3. EXPLAIN the issue simply
   "An 'authentication error' means FloQast tried to connect to Coupa
   but the credentials didn't work. It's like a password being rejected."

4. WALK them through the fix
   "Let's update the Coupa credentials in FloQast settings. Go to
   Settings > Connections > Coupa. Enter the new password. Click 'Test
   Connection' to verify it works. Then rerun the agent."

5. CONFIRM resolution
   "Great, the connection test passed! You can rerun the agent now.
   I'll stay on until you confirm it completes successfully."
""",
            your_experience="When your VBA automation broke at Thind Transport, you had to troubleshoot under pressure. That experience makes you calm in support situations."
        )
        
        return self.evaluate()
    
    def show_teaching_tip(self, topic, ideal_explanation, your_experience):
        """Show teaching guidance"""
        print("\n" + "=" * 70)
        print(f"TEACHING TIP: {topic}")
        print("=" * 70)
        print(f"\nIdeal Approach:{ideal_explanation}")
        print(f"\nYour Experience Connection:\n{your_experience}")
        print("=" * 70)
    
    def evaluate(self):
        """Score teaching effectiveness"""
        print("\n" + "=" * 70)
        print("TEACHING EVALUATION")
        print("=" * 70)
        
        print(f"\nStudent Understanding: {self.student_understanding}/100")
        
        total_teaching = sum(self.teaching_score.values())
        max_teaching = 30  # 10 per category
        
        print(f"\nYour Teaching Scores:")
        print(f"  Clarity:      {self.teaching_score['clarity']}/10")
        print(f"  Patience:     {self.teaching_score['patience']}/10")
        print(f"  Completeness: {self.teaching_score['completeness']}/10")
        print(f"  TOTAL:        {total_teaching}/{max_teaching}")
        
        combined = (self.student_understanding + (total_teaching/max_teaching*100)) / 2
        
        print("\n" + "-" * 30)
        print(f"COMBINED SCORE: {int(combined)}/100")
        
        if combined >= 80:
            print("\nExcellent! You'd be a great trainer.")
        elif combined >= 60:
            print("\nGood teaching - focus on structure and patience.")
        else:
            print("\nPractice more - use the ideal approach as a guide.")
        
        return combined >= 70


# ============================================================================
# INTERVIEW TIPS
# ============================================================================

def show_interview_tips():
    """Show interview talking points for teaching questions"""
    print("\n" + "=" * 70)
    print("INTERVIEW TIPS: TEACHING/TRAINING QUESTIONS")
    print("=" * 70)
    
    print("""
Q: "How would you explain a complex concept to someone non-technical?"

YOUR ANSWER:
"I start with the WHY - what business problem does this solve? Then I use
a relatable analogy. For example, explaining accruals to a non-accountant:
'Think of it like a credit card - the purchase happens in December even
though you pay in January.' Then I walk through a specific example with
real numbers. I check for understanding and adjust my explanation based
on their questions."

---

Q: "How do you handle a frustrated customer?"

YOUR ANSWER:
"First, I acknowledge their frustration - don't dismiss it. At Thind
Transport, when our VBA automation broke during month-end, I felt that
same pressure. So I say: 'I understand this is frustrating, especially
with month-end tomorrow. Let me help you fix this right now.' Then I ask
clarifying questions, explain what's happening in simple terms, and walk
them through the solution step by step."

---

Q: "Describe your training or presentation experience"

YOUR ANSWER:
"In consulting, I presented financial models and recommendations to
stakeholders at various levels - from analysts to executives. I learned
to adjust my communication style: executives want bottom-line impact and
ROI; analysts want the methodology details. I also trained colleagues on
spreadsheet processes at Thind Transport, creating step-by-step
documentation and conducting hands-on sessions. The key is meeting
people where they are, not where you think they should be."

---

Your Experience Connections:
- Consulting: Client presentations, explaining complex analysis
- Thind Transport: Training colleagues on automated processes
- Both: Patience with different learning styles
""")


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("\n" + "=" * 70)
    print("DAY 4: TEACHING & ENABLEMENT PRACTICE")
    print("Your Experience + FloQast Interview Prep")
    print("=" * 70)
    
    print("""
Your experience sources:
  - Consulting: Client presentations, executive communication
  - Thind Transport: Training colleagues, explaining processes
  - Both: Translating technical to business language

Available Scenarios:
  1 - Explain: What is an Accrual? (New accountant)
  2 - Explain: Bank Reconciliation (Non-accounting manager)
  3 - Explain: FloQast Agents (CFO)
  4 - Troubleshoot: Support Call (Frustrated user)
  T - Show Interview Tips
  Q - Quit
""")
    
    scenarios = {
        '1': 1, '2': 2, '3': 3, '4': 4
    }
    
    while True:
        try:
            choice = input("\nChoose scenario (1-4, T for tips, Q to quit): ").strip().upper()
            
            if choice == 'Q':
                print("\n" + "=" * 70)
                print("DAY 4 SUMMARY")
                print("=" * 70)
                print("""
Key Teaching Skills:
  1. Start with WHY (business purpose)
  2. Use analogies (credit card for accruals)
  3. Give specific examples (real numbers)
  4. Check understanding (ask questions)
  5. Adapt to audience (CFO vs analyst)
  6. Be patient with confusion

Your Experience = Your Advantage:
  - Client presentations taught you executive communication
  - Training colleagues taught you patience
  - Troubleshooting taught you calm under pressure

Interview Connection:
  "I've trained stakeholders at various levels - from presenting
  financial models to executives in consulting, to teaching spreadsheet
  processes to colleagues at Thind Transport. I adapt my communication
  to the audience: executives want ROI, analysts want methodology."

Next: Continue to Day 5 for behavioral interview practice!
""")
                break
            
            elif choice == 'T':
                show_interview_tips()
            
            elif choice in scenarios:
                scenario = TeachingScenario(scenarios[choice])
                scenario.run()
            
            else:
                print("Invalid choice. Enter 1-4, T, or Q.")
                
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except EOFError:
            # Non-interactive
            show_interview_tips()
            break


if __name__ == "__main__":
    main()
