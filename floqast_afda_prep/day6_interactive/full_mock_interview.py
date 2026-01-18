# -*- coding: utf-8 -*-
"""
Day 6: Full Mock Interview Simulation
Your Experience + FloQast Interview Prep

Complete 45-60 minute realistic interview with:
- Opening pitch
- Behavioral questions (STAR)
- Technical scenarios
- Gap-owning
- Your questions

Run: py full_mock_interview.py
"""

import sys
import time

# ============================================================================
# IDEAL ANSWERS REFERENCE (for feedback)
# ============================================================================

IDEAL_ANSWERS = {
    "opening": """
Hi, I'm Ranvir Thind. I graduated from UW with a Business Admin degree 
and have since built a unique background combining finance operations 
and technical automation.

At Thind Transport, our family logistics business, I supported month-end 
close - accruals, reconciliations, variance analysis. The manual work 
frustrated me, so I taught myself VBA and automated our monthly reporting, 
cutting 8 hours of work down to 1.5 hours - an 80% time savings.

In my consulting work, I've done client-facing financial modeling and 
automated Salesforce workflows for 2,000+ accounts. I've learned to 
translate complex technical solutions into business value for stakeholders.

What excites me about FloQast's AFDA role is that it combines everything 
I love: accounting fundamentals, process automation, and client 
partnership. I understand the pain of manual month-end work, and I want 
to help customers solve it with technology.
""",
    
    "automation": """
At Thind Transport, monthly financial reporting took our team about 8 hours.
Someone would pull data from multiple sources, paste into Excel, format 
the reports, and create summaries.

The challenge was both time and errors - manual steps meant occasional 
mistakes that required rework.

I taught myself VBA and built a set of macros that automated the entire 
workflow: data extraction, formatting, calculations, and validation checks.
I also added error-catching logic that flagged unusual values before 
reports were distributed.

The result was reducing 8 hours to 1.5 hours - 80% time savings. Error 
rate dropped to near zero because validation was built in. 

This connects directly to what FloQast Transform Agents do - automate 
repetitive accounting tasks with built-in controls.
""",
    
    "technical_stripe": """
Yes, FloQast AutoRec is perfect for this. With 500 Stripe transactions 
monthly, you need automated matching to save time.

I'd set up AutoRec with matching rules:
- Match by amount - exact match for most transactions
- Date tolerance - maybe +/- 3 days since bank processing varies
- Description matching - to catch transactions with same amount but 
  different purposes

For the FX differences, I'd configure a tolerance threshold - maybe $0.50 
or 0.5% - to auto-match transactions where the difference is due to 
exchange rate rounding, not actual discrepancies.

The result would be most of your 500 transactions auto-matched, with your 
team only reviewing the exceptions - maybe 10-20 per month instead of 500.
""",
    
    "gap_cpa": """
You're right - I don't have a CPA. I want to be honest about that while 
sharing what I do bring.

My path has been different but relevant. At Thind Transport, I worked 
hands-on with month-end close processes - accruals, reconciliations, 
variance analysis. I understand how these workflows work in practice.

What makes me valuable for this role specifically is the combination: 
accounting operations experience PLUS technical automation skills. I'm 
self-taught in VBA, Python, SQL - I can understand what customers need 
and configure solutions.

I'm actively deepening my accounting knowledge. The AFDA role is an 
opportunity to combine my existing strengths with structured learning 
from working with accounting professionals daily.

As for the family business context - yes, I was in a supportive role 
rather than fully independent. But my consulting work was entirely 
independent - client presentations, financial models, stakeholder 
management. I can work autonomously.
"""
}


# ============================================================================
# INTERVIEW CLASS
# ============================================================================

class MockInterview:
    def __init__(self, difficulty='neutral'):
        self.difficulty = difficulty
        self.start_time = None
        self.scores = {
            'opening': 0,
            'behavioral': 0,
            'technical': 0,
            'gaps': 0,
            'questions': 0,
            'presence': 0
        }
        self.feedback = []
        
    def run(self):
        """Execute full interview"""
        print("\n" + "=" * 70)
        print("FULL MOCK INTERVIEW - FloQast AFDA")
        print("=" * 70)
        print(f"\nMode: {self.difficulty.upper()}")
        print("Duration: 45-60 minutes")
        print("\nSections:")
        print("  1. Opening (5 min)")
        print("  2. Behavioral Questions (15-20 min)")
        print("  3. Technical Scenarios (10-15 min)")
        print("  4. Gap Handling (5-10 min)")
        print("  5. Your Questions (5 min)")
        print("\nTreat this like a real interview!")
        print("=" * 70)
        
        try:
            input("\nPress Enter when ready to begin...")
        except EOFError:
            return
        
        self.start_time = time.time()
        
        # Interview sections
        self.section_opening()
        self.section_behavioral()
        self.section_technical()
        self.section_gaps()
        self.section_questions()
        
        # Debrief
        self.debrief()
        
    def get_answer(self, prompt=""):
        """Get multiline answer"""
        if prompt:
            print(prompt)
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
        
        return "\n".join(lines).strip()
    
    def section_opening(self):
        """Opening pitch"""
        print("\n" + "=" * 70)
        print("SECTION 1: OPENING")
        print("=" * 70)
        
        if self.difficulty == 'friendly':
            print("\n[INTERVIEWER]: Hi Ranvir! Thanks for being here. Tell me about")
            print("yourself and what brings you to FloQast.")
        else:
            print("\n[INTERVIEWER]: Let's start. Tell me about yourself.")
        
        answer = self.get_answer()
        
        # Score
        score = 0
        lower = answer.lower()
        
        if 'thind transport' in lower:
            score += 2
        if 'consulting' in lower or 'client' in lower:
            score += 2
        if any(k in lower for k in ['automation', 'vba', 'automated']):
            score += 2
        if any(k in lower for k in ['floqast', 'afda', 'role']):
            score += 2
        if len(answer.split()) >= 100:
            score += 2
        
        self.scores['opening'] = min(score, 10)
        
        if score >= 7:
            self.feedback.append("Opening: Strong pitch covering background and motivation")
        elif score >= 4:
            self.feedback.append("Opening: Decent but could add more about motivation for FloQast")
        else:
            self.feedback.append("Opening: Too brief - aim for 1-2 minutes covering background AND FloQast interest")
        
        # Interviewer response
        if self.difficulty == 'friendly':
            print("\n[INTERVIEWER]: Great background! I love that you taught yourself automation.")
        else:
            print("\n[INTERVIEWER]: Okay.")
    
    def section_behavioral(self):
        """Behavioral questions"""
        print("\n" + "=" * 70)
        print("SECTION 2: BEHAVIORAL QUESTIONS")
        print("=" * 70)
        
        questions = [
            {
                "q": "Tell me about a time you automated a process. What was your approach and what impact did it have?",
                "follow": "What was the exact time savings? How did you validate it worked?",
                "keywords": ["vba", "automated", "hours", "percent", "%", "saved"]
            },
            {
                "q": "Describe a situation where you had to explain something technical to a non-technical audience.",
                "follow": "How did you confirm they actually understood?",
                "keywords": ["explain", "analogy", "example", "visual", "asked"]
            },
            {
                "q": "Tell me about a time you made a mistake. What happened and how did you handle it?",
                "follow": "What did you learn? How has your approach changed?",
                "keywords": ["mistake", "error", "caught", "learned", "changed", "validation"]
            }
        ]
        
        total_score = 0
        
        for i, q in enumerate(questions, 1):
            print(f"\n--- Question {i}/3 ---")
            print(f"\n[INTERVIEWER]: {q['q']}")
            
            answer = self.get_answer()
            
            # Score STAR
            score = 0
            lower = answer.lower()
            
            # Structure
            if 'thind' in lower or 'consulting' in lower or 'when' in lower:
                score += 2  # Situation
            if 'needed' in lower or 'had to' in lower or 'challenge' in lower:
                score += 2  # Task
            if 'i ' in lower and any(v in lower for v in ['created', 'built', 'designed', 'automated']):
                score += 2  # Action
            if any(char.isdigit() for char in answer):
                score += 2  # Result with numbers
            
            # Keywords
            if any(k in lower for k in q['keywords']):
                score += 2
            
            total_score += min(score, 10)
            
            # Follow-up if challenging or weak answer
            if self.difficulty != 'friendly' or score < 6:
                print(f"\n[INTERVIEWER]: {q['follow']}")
                try:
                    followup = input("\n[YOU]: ").strip()
                    if len(followup) > 30:
                        total_score += 1
                except EOFError:
                    pass
        
        self.scores['behavioral'] = min(total_score, 30)
        
        avg = self.scores['behavioral'] / 3
        if avg >= 8:
            self.feedback.append("Behavioral: Strong STAR stories with quantified results")
        elif avg >= 5:
            self.feedback.append("Behavioral: Good stories but add more specific metrics")
        else:
            self.feedback.append("Behavioral: Need clearer STAR structure and specific outcomes")
    
    def section_technical(self):
        """Technical scenarios"""
        print("\n" + "=" * 70)
        print("SECTION 3: TECHNICAL SCENARIOS")
        print("=" * 70)
        
        questions = [
            {
                "q": "A customer has 500 Stripe transactions monthly that need to reconcile with their GL. They're spending 2 days per month on this. How would you use FloQast to help?",
                "follow": "They mention some transactions are off by a few cents due to FX. How would you handle that?",
                "keywords": ["autorec", "match", "rule", "tolerance", "automat"]
            },
            {
                "q": "Walk me through how you'd configure a FloQast Transform Agent for month-end Coupa accruals. What decisions would you make?",
                "follow": "What materiality threshold would you recommend and why?",
                "keywords": ["agent", "accrual", "coupa", "threshold", "material", "gl", "account"]
            }
        ]
        
        total_score = 0
        
        for i, q in enumerate(questions, 1):
            print(f"\n--- Scenario {i}/2 ---")
            print(f"\n[INTERVIEWER]: {q['q']}")
            
            answer = self.get_answer()
            
            score = 0
            lower = answer.lower()
            
            # Keywords
            keyword_matches = sum(1 for k in q['keywords'] if k in lower)
            score += min(keyword_matches * 3, 9)
            
            # Detail
            if len(answer.split()) >= 80:
                score += 3
            elif len(answer.split()) >= 40:
                score += 2
            
            # Specific recommendations
            if any(char.isdigit() for char in answer):
                score += 3
            
            total_score += min(score, 15)
            
            # Follow-up
            print(f"\n[INTERVIEWER]: {q['follow']}")
            try:
                followup = input("\n[YOU]: ").strip()
                if len(followup) > 20:
                    total_score += 2
            except EOFError:
                pass
        
        self.scores['technical'] = min(total_score, 30)
        
        if self.scores['technical'] >= 22:
            self.feedback.append("Technical: Strong FloQast product knowledge")
        elif self.scores['technical'] >= 14:
            self.feedback.append("Technical: Decent but review AutoRec, Transform, Flux specifics")
        else:
            self.feedback.append("Technical: Need to study FloQast products more")
    
    def section_gaps(self):
        """Gap-owning"""
        print("\n" + "=" * 70)
        print("SECTION 4: GAP HANDLING")
        print("=" * 70)
        
        if self.difficulty == 'friendly':
            print("\n[INTERVIEWER]: I see you're developing your accounting expertise.")
            print("Tell me about your hands-on experience and how you're growing.")
        else:
            print("\n[INTERVIEWER]: I notice you don't have a CPA, and your main")
            print("accounting experience is in a family business. Our customers are")
            print("enterprise CFOs with Big 4 backgrounds. How do you think about that?")
        
        answer = self.get_answer()
        
        score = 0
        lower = answer.lower()
        
        # Owns it (doesn't deflect or apologize)
        if 'sorry' not in lower and 'unfortunately' not in lower:
            score += 2
        
        # Acknowledges honestly
        if any(k in lower for k in ['honest', 'right', 'true', 'support', 'learning']):
            score += 2
        
        # Pivots to strengths
        if any(k in lower for k in ['automation', 'vba', 'technical', 'process', 'consulting']):
            score += 3
        
        # Growth mindset
        if any(k in lower for k in ['eager', 'learning', 'growing', 'studying', 'opportunity']):
            score += 3
        
        self.scores['gaps'] = min(score, 10)
        
        if self.difficulty != 'friendly':
            print("\n[INTERVIEWER]: But our other candidates have CPAs and enterprise experience.")
            print("Why should we take a chance on you?")
            try:
                followup = input("\n[YOU]: ").strip()
                if len(followup) > 40:
                    self.scores['gaps'] = min(self.scores['gaps'] + 2, 10)
            except EOFError:
                pass
        
        if self.scores['gaps'] >= 8:
            self.feedback.append("Gap handling: Confident, authentic, with strong pivot to strengths")
        elif self.scores['gaps'] >= 5:
            self.feedback.append("Gap handling: Decent but strengthen the pivot to your unique value")
        else:
            self.feedback.append("Gap handling: Need to own gaps more confidently, less defensively")
    
    def section_questions(self):
        """Candidate questions"""
        print("\n" + "=" * 70)
        print("SECTION 5: YOUR QUESTIONS")
        print("=" * 70)
        
        print("\n[INTERVIEWER]: We have a few minutes left. What questions do you have?")
        
        questions_asked = 0
        score = 0
        
        good_topics = ['team', 'success', 'onboard', 'train', 'customer', 'day', 'challenge', 'grow', 'culture']
        
        while questions_asked < 3:
            try:
                q = input(f"\n[YOU - Question {questions_asked + 1}]: ").strip()
            except EOFError:
                break
            
            if q.lower() in ['none', 'no', 'no questions', '']:
                break
            
            questions_asked += 1
            
            if any(t in q.lower() for t in good_topics):
                score += 4
            else:
                score += 2
            
            # Generic response
            print("\n[INTERVIEWER]: Great question. [Provides thoughtful answer]")
            
            if questions_asked < 3:
                try:
                    cont = input("\nMore questions? (y/n): ").strip().lower()
                    if cont != 'y':
                        break
                except EOFError:
                    break
        
        if questions_asked == 0:
            score = 0
            self.feedback.append("Questions: Did not ask any questions - missed opportunity!")
        else:
            self.feedback.append(f"Questions: Asked {questions_asked} thoughtful question(s)")
        
        self.scores['questions'] = min(score, 10)
    
    def debrief(self):
        """Comprehensive debrief"""
        elapsed = int((time.time() - self.start_time) / 60)
        
        print("\n" + "=" * 70)
        print("INTERVIEW COMPLETE")
        print("=" * 70)
        
        print(f"\n[INTERVIEWER]: Thank you for your time today.")
        print(f"\nElapsed: ~{elapsed} minutes")
        
        try:
            input("\nPress Enter for your debrief...")
        except EOFError:
            pass
        
        # Scoring
        print("\n" + "=" * 70)
        print("COMPREHENSIVE DEBRIEF")
        print("=" * 70)
        
        total = sum(self.scores.values())
        max_total = 100
        pct = int(total / max_total * 100)
        
        print(f"\nOVERALL: {total}/{max_total} ({pct}%)")
        print("-" * 30)
        print(f"Opening:    {self.scores['opening']}/10")
        print(f"Behavioral: {self.scores['behavioral']}/30")
        print(f"Technical:  {self.scores['technical']}/30")
        print(f"Gaps:       {self.scores['gaps']}/10")
        print(f"Questions:  {self.scores['questions']}/10")
        
        print("\n" + "-" * 70)
        print("DETAILED FEEDBACK:")
        for fb in self.feedback:
            print(f"  - {fb}")
        
        # Decision
        print("\n" + "=" * 70)
        if pct >= 80:
            print("DECISION: STRONG YES - Ready for final round!")
            print("\nYou demonstrated strong STAR stories, technical knowledge,")
            print("and authentic gap-owning. Well prepared!")
        elif pct >= 65:
            print("DECISION: YES WITH RESERVATIONS")
            print("\nSolid interview but polish these areas before the real thing:")
            self.show_improvement_areas()
        elif pct >= 50:
            print("DECISION: MAYBE - Needs work")
            print("\nPotential is there but significant improvement needed:")
            self.show_improvement_areas()
        else:
            print("DECISION: NOT READY")
            print("\nFocus on:")
            self.show_improvement_areas()
        
        # Reference answers
        print("\n" + "=" * 70)
        print("REFERENCE: IDEAL OPENING PITCH")
        print("=" * 70)
        print(IDEAL_ANSWERS['opening'])
        
        print("\n" + "=" * 70)
        print("REFERENCE: IDEAL GAP RESPONSE")
        print("=" * 70)
        print(IDEAL_ANSWERS['gap_cpa'])
        
        print("\n" + "=" * 70)
        print("YOU COMPLETED ALL 6 DAYS!")
        print("=" * 70)
        print("""
Your Preparation Arsenal:
  - Day 1: Journal entries + Bank reconciliation practice
  - Day 2: Agent configuration understanding
  - Day 3: Customer objection handling
  - Day 4: Teaching/training practice
  - Day 5: Behavioral interview (STAR stories)
  - Day 6: Full mock interview

Key Strengths to Emphasize:
  - VBA automation (80% time savings)
  - Salesforce automation (2,000+ accounts)
  - Month-end close experience
  - Self-taught technical skills
  - Hybrid accounting + tech background

Gap-Owning Strategy:
  - Own it confidently (not defensively)
  - Pivot to unique strengths
  - Show growth mindset
  - Connect to the AFDA role

GOOD LUCK WITH YOUR REAL INTERVIEW!
""")
    
    def show_improvement_areas(self):
        """Show areas needing improvement"""
        if self.scores['opening'] < 6:
            print("  - Opening: Practice your 1-2 minute pitch (see reference)")
        if self.scores['behavioral'] < 18:
            print("  - Behavioral: Add specific metrics to STAR stories")
        if self.scores['technical'] < 18:
            print("  - Technical: Study FloQast products (AutoRec, Transform, Flux)")
        if self.scores['gaps'] < 6:
            print("  - Gaps: Practice confident, authentic gap-owning (see reference)")
        if self.scores['questions'] < 5:
            print("  - Questions: Prepare 3-4 thoughtful questions for interviewer")


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("\n" + "=" * 70)
    print("DAY 6: FULL MOCK INTERVIEW")
    print("Your Experience + FloQast Interview Prep")
    print("=" * 70)
    
    print("""
Your final test - a complete interview simulation.

Modes:
  1 - FRIENDLY: Warm, encouraging interviewer
  2 - NEUTRAL: Standard professional interview
  3 - CHALLENGING: Tough, probing follow-ups

Recommendation: Try NEUTRAL first, then CHALLENGING.

Set aside 60-75 minutes for full immersion.
""")
    
    while True:
        try:
            choice = input("\nChoose mode (1-3, Q to quit): ").strip().upper()
            
            if choice == 'Q':
                print("\nGood luck with your interview!")
                break
            
            if choice in ['1', '2', '3']:
                modes = {'1': 'friendly', '2': 'neutral', '3': 'challenging'}
                interview = MockInterview(difficulty=modes[choice])
                interview.run()
                
                try:
                    again = input("\nTry again? (y/n): ").strip().lower()
                    if again != 'y':
                        break
                except EOFError:
                    break
            else:
                print("Invalid choice. Enter 1-3 or Q.")
                
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except EOFError:
            print("\nRunning in non-interactive mode not supported for full mock.")
            break


if __name__ == "__main__":
    main()
