# -*- coding: utf-8 -*-
"""
Day 5: Hands-On Behavioral Interview
Real interview questions - YOU answer, AI scores STAR format
"""

import sys

def get_input(prompt=""):
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return ""

def question_automation():
    """Tell me about your automation project"""
    
    print("\n" + "="*70)
    print("BEHAVIORAL QUESTION 1")
    print("="*70)
    
    print("""
INTERVIEWER:
"Tell me about a time you automated a process. Walk me through what
you did and what the impact was."

YOUR TASK: Answer using STAR format.
Type your answer below.
""")
    
    answer = get_input("\nYOU: ")
    
    score = 0
    feedback = []
    
    # Check STAR components
    if any(word in answer.lower() for word in ['thind', 'transport', 'when', 'at']):
        score += 15
        feedback.append("✓ Situation: Set context")
    else:
        feedback.append("✗ Situation: Missing context (where/when)")
    
    if any(word in answer.lower() for word in ['needed', 'had to', 'goal', 'challenge']):
        score += 15
        feedback.append("✓ Task: Defined what needed to be done")
    else:
        feedback.append("✗ Task: Didn't clarify the goal/challenge")
    
    if 'i ' in answer.lower() and any(word in answer.lower() for word in ['built', 'created', 'automated', 'taught', 'learned']):
        score += 20
        feedback.append("✓ Action: Described your specific actions (I did...)")
    else:
        feedback.append("✗ Action: Need specific actions YOU took (not 'we')")
    
    if any(char.isdigit() for char in answer):
        score += 25
        feedback.append("✓ Result: Included numbers/metrics")
    else:
        feedback.append("✗ Result: Missing quantifiable outcomes")
    
    if '80' in answer and '%' in answer:
        score += 15
        feedback.append("✓ Excellent: Mentioned 80% time savings")
    elif '8' in answer and '1.5' in answer:
        score += 15
        feedback.append("✓ Excellent: Mentioned 8 hours -> 1.5 hours")
    
    if 'floqast' in answer.lower() or 'agent' in answer.lower() or 'role' in answer.lower():
        score += 10
        feedback.append("✓ Connected to FloQast role")
    else:
        feedback.append("~ Could connect to FloQast agents")
    
    # Results
    print("\n" + "-"*70)
    print("STAR SCORE:")
    for fb in feedback:
        print(f"  {fb}")
    
    print(f"\nTOTAL: {score}/100")
    
    if score >= 80:
        print("\nExcellent STAR answer!")
    elif score >= 60:
        print("\nGood structure. Add more specifics.")
    else:
        print("\nNeeds work. Follow STAR format closely.")
    
    print("\n" + "-"*70)
    print("IDEAL STAR ANSWER:")
    print("-"*70)
    print("""
SITUATION: At Thind Transport, monthly financial reporting was taking
8 hours of manual work - pulling data, formatting Excel, creating summaries.

TASK: I needed to reduce this time and eliminate errors that were
causing rework.

ACTION: I taught myself VBA and built macros to automate data extraction,
formatting, and calculations. I added validation checks to catch errors
before reports were distributed.

RESULT: Reduced process from 8 hours to 1.5 hours - 80% time savings.
Error rate dropped to near zero because validation was built in.

This is exactly what FloQast Transform AI Agents do - automate
repetitive accounting tasks with built-in validation.
""")
    
    return score >= 60


def question_gap_cpa():
    """Gap owning: No CPA"""
    
    print("\n" + "="*70)
    print("GAP-OWNING QUESTION")
    print("="*70)
    
    print("""
INTERVIEWER:
"I notice you don't have a CPA. For this role, we need strong
accounting knowledge. How do you think about that gap?"

YOUR TASK: Own the gap confidently. Type your answer.
""")
    
    answer = get_input("\nYOU: ")
    
    score = 0
    feedback = []
    
    # Check gap-owning approach
    if any(word in answer.lower() for word in ['right', 'correct', 'true', 'honest']):
        score += 20
        feedback.append("✓ Owned it directly (not defensive)")
    else:
        feedback.append("✗ Should own it upfront ('You're right, I don't')")
    
    if 'sorry' in answer.lower() or 'unfortunately' in answer.lower():
        score -= 10
        feedback.append("✗ Too apologetic - own it confidently")
    
    if any(word in answer.lower() for word in ['automation', 'vba', 'technical', 'process']):
        score += 25
        feedback.append("✓ Pivoted to technical strengths")
    else:
        feedback.append("✗ Didn't pivot to your unique strengths")
    
    if any(word in answer.lower() for word in ['hands-on', 'experience', 'thind', 'close']):
        score += 20
        feedback.append("✓ Mentioned practical experience")
    else:
        feedback.append("~ Could mention hands-on experience")
    
    if any(word in answer.lower() for word in ['eager', 'learning', 'grow', 'opportunity']):
        score += 20
        feedback.append("✓ Showed growth mindset")
    else:
        feedback.append("~ Could show eagerness to learn")
    
    if 'afda' in answer.lower() or 'role' in answer.lower() or 'floqast' in answer.lower():
        score += 15
        feedback.append("✓ Connected to the AFDA role")
    else:
        feedback.append("~ Should connect to what AFDA needs")
    
    # Results
    print("\n" + "-"*70)
    print("GAP-OWNING SCORE:")
    for fb in feedback:
        print(f"  {fb}")
    
    print(f"\nTOTAL: {score}/100")
    
    print("\n" + "-"*70)
    print("IDEAL GAP-OWNING RESPONSE:")
    print("-"*70)
    print("""
"You're right - I don't have a CPA. Here's what I do have:

- Finance degree with accounting coursework from UW
- Hands-on experience: month-end close, journal entries, reconciliations,
  variance analysis at Thind Transport
- Understanding of accounting principles and how financial statements work

The CPA would formalize what I understand practically. I'm interested
in pursuing it, and FloQast would accelerate that by exposing me to
diverse accounting workflows across customers.

More importantly, for the AFDA role, the value is in the intersection
of accounting knowledge AND technical implementation. I understand the
workflows AND I can configure automation. That hybrid skillset is what
FloQast needs."
""")
    
    return score >= 60


def main():
    print("\n" + "="*70)
    print("DAY 5: HANDS-ON BEHAVIORAL INTERVIEW")
    print("="*70)
    
    print("""
Real interview questions - YOU answer them.

Available Questions:
  1 - Tell me about your automation project
  2 - Gap-owning: No CPA
  Q - Quit
""")
    
    while True:
        try:
            choice = input("\nChoose question (1-2, Q to quit): ").strip()
            
            if choice.lower() == 'q':
                break
            
            elif choice == '1':
                question_automation()
                input("\nPress Enter to continue...")
            
            elif choice == '2':
                question_gap_cpa()
                input("\nPress Enter to continue...")
            
            else:
                print("Invalid choice.")
                
        except KeyboardInterrupt:
            break
        except EOFError:
            question_automation()
            question_gap_cpa()
            break


if __name__ == "__main__":
    main()



