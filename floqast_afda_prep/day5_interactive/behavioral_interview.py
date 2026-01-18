# -*- coding: utf-8 -*-
"""
Day 5: Behavioral Interview Practice
Your Experience + FloQast Interview Prep

AI interviews YOU with real FloQast AFDA questions.
Covers BOTH your Thind Transport AND consulting experience.

Run: py behavioral_interview.py
"""

import sys
import random

# ============================================================================
# YOUR EXPERIENCE STORIES (Reference for practice)
# ============================================================================

YOUR_STORIES = {
    "automation": {
        "thind": "VBA automation of monthly reporting - reduced 8 hours to 1.5 hours (80% savings)",
        "consulting": "Salesforce automation for 2,000+ customer accounts, streamlined workflows"
    },
    "learning": {
        "thind": "Self-taught VBA, SQL, Python to solve business problems",
        "consulting": "Learned financial modeling, CRM systems, AI tools on the job"
    },
    "customer": {
        "thind": "Working with different departments (ops, finance) on reporting needs",
        "consulting": "Client presentations, stakeholder management, discovery sessions"
    },
    "mistake": {
        "thind": "Formula error in report caught before distribution - added validation steps",
        "consulting": "Underestimated project timeline - learned to build in buffer"
    },
    "process_improvement": {
        "thind": "Redesigned budget variance workflow to highlight key drivers",
        "consulting": "Mapped client processes, identified bottlenecks, recommended solutions"
    }
}


# ============================================================================
# INTERVIEW QUESTIONS
# ============================================================================

BEHAVIORAL_QUESTIONS = [
    {
        "category": "Automation",
        "question": "Tell me about a time you automated a process. Walk me through what you did and the impact.",
        "value": "Empowered to Grow",
        "follow_up": "What was the measurable impact? How did you validate it worked correctly?",
        "answer_template": """
SITUATION: At Thind Transport, monthly reporting was taking 8 hours of 
manual work - pulling data, formatting Excel, creating summaries.

TASK: Needed to reduce this time and eliminate manual errors that were 
causing rework.

ACTION: I taught myself VBA and built macros to automate data extraction, 
formatting, and summary calculations. I also added validation checks to 
catch errors before reports were distributed.

RESULT: Reduced process from 8 hours to 1.5 hours - 80% time savings. 
Error rate dropped to near zero because validation was built in.

CONSULTING PARALLEL: Similarly, I automated Salesforce workflows for 
2,000+ accounts, creating consistent processes where there was manual 
inconsistency before.

FLOQAST CONNECTION: This is exactly what Transform AI Agents do - 
automate repetitive accounting tasks with built-in validation.
"""
    },
    {
        "category": "Learning",
        "question": "Tell me about a time you had to learn something technical quickly. What was your approach?",
        "value": "Empowered to Grow",
        "follow_up": "What resources did you use? How did you know you'd mastered it?",
        "answer_template": """
SITUATION: At Thind Transport, I saw an opportunity to automate reporting 
but didn't know VBA. The business need was immediate.

TASK: Needed to learn VBA well enough to build production-ready automation 
within a few weeks.

ACTION: I took a structured approach: started with online courses for 
fundamentals, then immediately applied concepts to our actual reports. 
When I hit problems, I searched forums and documentation. I built 
iteratively - small wins first, then more complex features.

RESULT: Within 3 weeks, I had a working automation. Within 2 months, it 
was production-ready with error handling. I've since applied the same 
approach to learn Python and SQL.

CONSULTING PARALLEL: Same pattern with financial modeling tools and 
Salesforce - learn fundamentals, apply immediately, iterate.

FLOQAST CONNECTION: AFDA role requires learning customer systems quickly. 
I have a proven pattern for rapid technical learning.
"""
    },
    {
        "category": "Customer/Communication",
        "question": "Describe a time you explained a complex technical concept to a non-technical person.",
        "value": "Customer Obsessed",
        "follow_up": "How did you confirm they actually understood?",
        "answer_template": """
SITUATION: In consulting, I needed to present a financial model to 
stakeholders who didn't have finance backgrounds.

TASK: Help them understand the model's assumptions and outputs so they 
could make informed decisions.

ACTION: I avoided jargon, used analogies (e.g., "Think of NPV like 
comparing the value of getting $100 today vs $110 next year"). I showed 
simple visuals instead of complex spreadsheets. Most importantly, I 
asked them to explain it back to me in their own words.

RESULT: They asked thoughtful follow-up questions about specific 
assumptions - showing they understood the core concepts. They made a 
decision based on the analysis.

THIND PARALLEL: Explained month-end accounting to operations managers 
using concrete examples from our actual business.

FLOQAST CONNECTION: Training customers on agent configuration requires 
the same skill - translating technical to business language.
"""
    },
    {
        "category": "Mistake",
        "question": "Tell me about a time you made a mistake. What happened and how did you handle it?",
        "value": "Unwaveringly Authentic",
        "follow_up": "What did you learn? How has your approach changed?",
        "answer_template": """
SITUATION: At Thind Transport, I had a formula error in a monthly report 
that showed incorrect variance numbers.

TASK: The report was about to be distributed. I needed to decide whether 
to delay or catch the error.

ACTION: I noticed the numbers looked off during my final review. Instead 
of assuming it was fine, I traced back through the formulas and found 
the error. I delayed the report by 2 hours to fix it, then proactively 
told my supervisor what happened and what I did to prevent it.

RESULT: The correct report went out. I added validation checks to all 
my spreadsheets - totals that must balance, reasonableness flags for 
unusual values. Haven't had a similar error since.

WHAT I LEARNED: Always build in validation, and trust your instincts 
when something looks wrong.

FLOQAST CONNECTION: I understand why FloQast agents require approval 
before posting - human review catches what automation might miss.
"""
    },
    {
        "category": "Collaboration",
        "question": "Give me an example of when you worked with people from different teams to solve a problem.",
        "value": "Collaboration",
        "follow_up": "How did you handle differing priorities?",
        "answer_template": """
SITUATION: At Thind Transport, operations and finance had different 
reporting needs. Operations wanted detailed route performance; finance 
wanted summary P&L impact.

TASK: Create a reporting solution that served both teams without 
doubling the work.

ACTION: I met with both teams separately to understand their specific 
needs. I identified common data elements and created a single data 
pull with different views - operations got their detail, finance got 
their summary, all from one source of truth.

RESULT: Both teams got what they needed. Maintenance time dropped because 
we only had one process to update. Cross-team trust improved because 
numbers were always consistent.

CONSULTING PARALLEL: Client projects always involved multiple 
stakeholders with different priorities. Discovery questions helped 
find common ground.

FLOQAST CONNECTION: AFDA role involves working across customer teams - 
same skill of understanding different needs and finding solutions.
"""
    },
    {
        "category": "Above and Beyond",
        "question": "Tell me about a time you went above and beyond for a customer or client.",
        "value": "Customer Obsessed",
        "follow_up": "What was the outcome? Was there any recognition?",
        "answer_template": """
SITUATION: A consulting client was struggling with a presentation to 
their board the next day. The model we built wasn't telling the story 
they needed.

TASK: They needed a revised presentation that highlighted the key 
insights in a way their board would understand.

ACTION: I stayed late (past 10 PM) to restructure the model outputs 
into a clear narrative. I created executive-friendly visuals and wrote 
speaking notes for each slide. I also did a quick rehearsal call with 
them early the next morning.

RESULT: The presentation went well. The client specifically mentioned 
my support to my manager, which led to additional project work.

THIND PARALLEL: Stayed late during month-end to ensure reports were 
accurate before a bank meeting.

FLOQAST CONNECTION: Customer success in this role means going the 
extra mile to ensure customers succeed with the product.
"""
    }
]


# ============================================================================
# GAP-OWNING QUESTIONS
# ============================================================================

GAP_QUESTIONS = [
    {
        "question": "I notice you don't have a CPA. Our customers are accounting professionals. How do you think about that gap?",
        "challenge": "But CPAs have years of training in accounting standards. Why would a customer trust your guidance?",
        "framework": """
OWN IT: "You're right - I don't have a CPA. I've chosen a different path 
that I believe is valuable for this specific role."

PIVOT: "What I bring is the combination of practical accounting experience 
from Thind Transport - accruals, reconciliations, month-end close - 
combined with technical automation skills. I understand accounting 
workflows from the inside, and I can automate them."

GROWTH: "I'm actively deepening my accounting knowledge. I've been 
studying for CPA exams and applying concepts in my work. The AFDA role 
is a perfect opportunity to combine accounting fundamentals with 
technical implementation."

FLOQAST FIT: "FloQast needs people who understand accounting AND 
technology. I bring both, plus the ability to explain technical 
solutions to accounting professionals in their language."
"""
    },
    {
        "question": "Your resume mentions Thind Transport, but that's a family business. How independent was your work really?",
        "challenge": "So you had a lot of help. How do I know you can work independently with customers?",
        "framework": """
OWN IT HONESTLY: "It is a family business, and I want to be honest about 
the context. I supported the month-end close working alongside our 
accountant, not as the sole accountant."

SPECIFY YOUR CONTRIBUTIONS: "What was entirely mine: the VBA automation 
that saved 80% of reporting time, the variance analysis presentations, 
the process improvements I designed. The accountant handled the 
technical accounting decisions; I handled the execution and automation."

CONSULTING INDEPENDENCE: "In my consulting work, I operated much more 
independently - client presentations, financial models, Salesforce 
automation for 2,000+ accounts. That was my work with minimal supervision."

GROWTH FRAMING: "I see the AFDA role as the next step - taking the skills 
I've built in both contexts and applying them in a professional 
environment where I'm fully accountable."
"""
    },
    {
        "question": "You don't have direct ERP experience - our clients use NetSuite, SAP, Intacct. How would you help them?",
        "challenge": "They're paying for expertise. Is on-the-job learning fair to them?",
        "framework": """
ACKNOWLEDGE: "You're right that I haven't worked directly in enterprise 
ERPs like NetSuite or SAP. I want to be honest about that."

TRANSFERABLE SKILLS: "What I do have is experience with system 
integrations - understanding how data flows between systems, how APIs 
work, how to map data from one format to another. That's what I did 
with Salesforce automation."

RAPID LEARNING TRACK RECORD: "I've demonstrated I can learn technical 
systems quickly. VBA from zero to production in 3 weeks. SQL, Python, 
AI tools - all self-taught and applied. I'll apply the same approach 
to ERPs."

AFDA CONTEXT: "The AFDA role isn't about being an ERP expert - it's 
about understanding accounting workflows and configuring FloQast to 
solve customer problems. The ERP-specific details I'll learn through 
training and customer exposure."
"""
    }
]


# ============================================================================
# INTERVIEWER CLASS
# ============================================================================

class AIInterviewer:
    def __init__(self, difficulty='neutral'):
        self.difficulty = difficulty
        self.scores = {
            'situation': 0,
            'task': 0,
            'action': 0,
            'result': 0,
            'authenticity': 0,
            'floqast_connection': 0
        }
        
    def ask_question(self, question_data):
        """Ask a behavioral question"""
        print("\n" + "=" * 70)
        print(f"[INTERVIEWER]: {question_data['question']}")
        print("=" * 70)
        
        if self.difficulty == 'friendly':
            print(f"\nHINT: Maps to FloQast value '{question_data.get('value', 'N/A')}'")
            print("STRUCTURE: Use STAR format (Situation, Task, Action, Result)")
        
        print("\n(Type your answer. Press Enter twice when done)")
        
        lines = []
        try:
            while True:
                line = input()
                if line == "" and lines and lines[-1] == "":
                    break
                lines.append(line)
        except EOFError:
            pass
        
        answer = "\n".join(lines).strip()
        self.evaluate_answer(answer, question_data)
        
        # Follow-up for non-friendly modes
        if self.difficulty != 'friendly' and question_data.get('follow_up'):
            print(f"\n[INTERVIEWER]: {question_data['follow_up']}")
            try:
                follow_up = input("\n[YOU]: ").strip()
                if follow_up:
                    self.evaluate_follow_up(follow_up)
            except EOFError:
                pass
        
        self.show_feedback(question_data)
        
    def evaluate_answer(self, answer, question_data):
        """Score the answer"""
        answer_lower = answer.lower()
        
        # Situation
        if any(k in answer_lower for k in ['at thind', 'in consulting', 'when i', 'situation', 'context']):
            self.scores['situation'] += 3
        
        # Task
        if any(k in answer_lower for k in ['needed to', 'had to', 'goal', 'task', 'challenge']):
            self.scores['task'] += 3
        
        # Action - look for first person
        if 'i ' in answer_lower:
            action_verbs = ['created', 'built', 'automated', 'learned', 'designed', 'implemented', 'analyzed']
            action_count = sum(1 for v in action_verbs if v in answer_lower)
            self.scores['action'] += min(action_count * 2, 8)
        
        # Result - look for quantification
        if any(char.isdigit() for char in answer):
            self.scores['result'] += 3
        if '%' in answer or 'percent' in answer_lower:
            self.scores['result'] += 2
        if any(k in answer_lower for k in ['saved', 'reduced', 'improved', 'increased']):
            self.scores['result'] += 2
        
        # Authenticity
        if any(k in answer_lower for k in ['honest', 'admit', 'learn', 'support', 'help']):
            self.scores['authenticity'] += 3
        
        # FloQast connection
        if any(k in answer_lower for k in ['floqast', 'agent', 'autorec', 'automation', 'afda']):
            self.scores['floqast_connection'] += 3
            
    def evaluate_follow_up(self, answer):
        """Score follow-up response"""
        if len(answer) > 50:
            self.scores['action'] += 2
            self.scores['result'] += 1
            
    def show_feedback(self, question_data):
        """Show feedback and template"""
        print("\n" + "-" * 70)
        print("FEEDBACK")
        print("-" * 70)
        
        total = sum(self.scores.values())
        
        if total >= 20:
            print("\nStrong answer! Good STAR structure and specifics.")
        elif total >= 12:
            print("\nDecent answer. Add more specific metrics and actions.")
        else:
            print("\nNeeds work. Focus on concrete examples with numbers.")
        
        if self.difficulty == 'friendly' and 'answer_template' in question_data:
            print("\n" + "-" * 70)
            print("REFERENCE ANSWER:")
            print(question_data['answer_template'])
    
    def final_score(self):
        """Show final interview score"""
        print("\n" + "=" * 70)
        print("INTERVIEW SUMMARY")
        print("=" * 70)
        
        total = sum(self.scores.values())
        max_score = 50  # Rough max
        
        print(f"\nSituation Setup: {self.scores['situation']}/8")
        print(f"Task Clarity: {self.scores['task']}/8")
        print(f"Action Detail: {self.scores['action']}/10")
        print(f"Result Metrics: {self.scores['result']}/10")
        print(f"Authenticity: {self.scores['authenticity']}/8")
        print(f"FloQast Connection: {self.scores['floqast_connection']}/6")
        print("-" * 30)
        print(f"TOTAL: {total}/{max_score}")
        
        if total >= 35:
            print("\nReady for the real interview!")
        elif total >= 20:
            print("\nGood progress - practice the templates.")
        else:
            print("\nReview the answer templates and try again.")


def run_gap_practice():
    """Practice gap-owning questions"""
    print("\n" + "=" * 70)
    print("GAP-OWNING PRACTICE")
    print("=" * 70)
    print("""
These are the HARD questions about your resume gaps.

Strategy:
  1. OWN it honestly (don't be defensive)
  2. PIVOT to transferable skills
  3. Show GROWTH mindset
  4. Connect to FLOQAST role
""")
    
    for i, q in enumerate(GAP_QUESTIONS, 1):
        print("\n" + "=" * 70)
        print(f"GAP QUESTION {i}/{len(GAP_QUESTIONS)}")
        print(f"\n[INTERVIEWER]: {q['question']}")
        print("=" * 70)
        
        try:
            answer = input("\n[YOU]: ").strip()
            
            print(f"\n[INTERVIEWER - PUSHING BACK]: {q['challenge']}")
            followup = input("\n[YOU]: ").strip()
            
            print("\n" + "-" * 70)
            print("IDEAL RESPONSE FRAMEWORK:")
            print(q['framework'])
            
            input("\nPress Enter to continue...")
        except (EOFError, KeyboardInterrupt):
            print("\n" + q['framework'])
            break


def run_values_practice():
    """Practice FloQast values stories"""
    print("\n" + "=" * 70)
    print("FLOQAST VALUES PRACTICE")
    print("=" * 70)
    
    values = [
        {
            "value": "Unwaveringly Authentic",
            "question": "Tell me about a time you had to be honest about a mistake or limitation.",
            "your_story": "Thind: Caught formula error, owned it, added validation. Consulting: Acknowledged timeline underestimate, adjusted plan."
        },
        {
            "value": "Ambitious with Integrity",
            "question": "Tell me about a time you pushed for excellence while doing things the right way.",
            "your_story": "Thind: Automation could have been quick/dirty, but I added validation and documentation for maintainability."
        },
        {
            "value": "Empowered to Grow",
            "question": "Tell me about a time you taught yourself something new.",
            "your_story": "Self-taught VBA, SQL, Python. Pattern: fundamentals -> immediate application -> iterate."
        },
        {
            "value": "Collaboration",
            "question": "Tell me about working with people who had different priorities.",
            "your_story": "Thind: Ops vs Finance reporting needs - found common data source. Consulting: Multiple stakeholder management."
        },
        {
            "value": "Customer Obsessed",
            "question": "Tell me about going above and beyond for someone.",
            "your_story": "Consulting: Late night model revision for client board presentation. Thind: Month-end support before bank meeting."
        }
    ]
    
    for v in values:
        print("\n" + "=" * 70)
        print(f"VALUE: {v['value']}")
        print(f"\nQuestion: {v['question']}")
        print(f"\nYour Story Options: {v['your_story']}")
        print("=" * 70)
        
        try:
            input("\n[Practice out loud, then press Enter...]")
        except (EOFError, KeyboardInterrupt):
            break


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("\n" + "=" * 70)
    print("DAY 5: BEHAVIORAL INTERVIEW PRACTICE")
    print("Your Experience + FloQast Interview Prep")
    print("=" * 70)
    
    print("""
Your experience sources:
  - Thind Transport: Automation, month-end, process improvement
  - Consulting: Client work, presentations, financial modeling

Available Modes:
  1 - FRIENDLY: Hints + answer templates shown
  2 - NEUTRAL: Standard interview (recommended)
  3 - CHALLENGING: Tough follow-ups
  4 - GAP-OWNING: Practice handling your resume gaps
  5 - VALUES PRACTICE: One story per FloQast value
  Q - Quit
""")
    
    while True:
        try:
            choice = input("\nChoose mode (1-5, Q to quit): ").strip().upper()
            
            if choice == 'Q':
                print("\n" + "=" * 70)
                print("DAY 5 SUMMARY")
                print("=" * 70)
                print("""
Key Interview Skills:
  - STAR format: Situation, Task, Action, Result
  - Quantify results (80%, 8 hours to 1.5, 2,000 accounts)
  - Include BOTH Thind Transport AND consulting experience
  - Own gaps honestly, pivot to strengths
  - Connect to FloQast role

Your Story Arsenal:
  - Automation: VBA (80% savings), Salesforce (2,000 accounts)
  - Learning: Self-taught VBA, SQL, Python in weeks
  - Customer: Executive presentations, stakeholder management
  - Mistake: Caught errors, added validation
  - Collaboration: Cross-team reporting solutions

Gap-Owning Strategy:
  1. Own it (don't be defensive)
  2. Pivot to transferable skills
  3. Show growth mindset
  4. Connect to the role

Next: Day 6 for full mock interview!
""")
                break
            
            elif choice == '4':
                run_gap_practice()
            
            elif choice == '5':
                run_values_practice()
            
            elif choice in ['1', '2', '3']:
                difficulties = {'1': 'friendly', '2': 'neutral', '3': 'challenging'}
                interviewer = AIInterviewer(difficulty=difficulties[choice])
                
                # Pick 3 random questions
                questions = random.sample(BEHAVIORAL_QUESTIONS, 3)
                
                for i, q in enumerate(questions, 1):
                    print(f"\n\nQUESTION {i}/3")
                    interviewer.ask_question(q)
                    try:
                        input("\nPress Enter for next question...")
                    except (EOFError, KeyboardInterrupt):
                        break
                
                interviewer.final_score()
            
            else:
                print("Invalid choice. Enter 1-5 or Q.")
                
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except EOFError:
            run_values_practice()
            break


if __name__ == "__main__":
    main()
