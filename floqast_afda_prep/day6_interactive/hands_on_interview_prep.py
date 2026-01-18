# -*- coding: utf-8 -*-
"""
Day 6: Hands-On Interview Prep
Practice key interview moments
"""

import sys

def get_input(prompt=""):
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        return ""

def opening_pitch():
    """Practice opening statement"""
    
    print("\n" + "="*70)
    print("INTERVIEW OPENING")
    print("="*70)
    
    print("""
INTERVIEWER:
"Thanks for being here today. Tell me about yourself and what brings
you to FloQast."

YOUR TASK: Give your opening pitch (aim for 1-2 minutes).
Type your answer.
""")
    
    answer = get_input("\nYOU: ")
    
    score = 0
    feedback = []
    
    # Check components
    if 'uw' in answer.lower() or 'university' in answer.lower() or 'foster' in answer.lower():
        score += 10
        feedback.append("✓ Mentioned education")
    
    if 'thind' in answer.lower():
        score += 15
        feedback.append("✓ Mentioned Thind Transport")
    else:
        feedback.append("✗ Should mention Thind Transport experience")
    
    if 'consulting' in answer.lower() or 'client' in answer.lower():
        score += 15
        feedback.append("✓ Mentioned consulting work")
    else:
        feedback.append("~ Could mention consulting experience")
    
    if any(word in answer.lower() for word in ['automation', 'vba', 'automated']):
        score += 20
        feedback.append("✓ Highlighted automation experience")
    else:
        feedback.append("✗ Must mention automation (your key differentiator)")
    
    if '80' in answer or '8 hours' in answer.lower():
        score += 15
        feedback.append("✓ Included your 80% metric")
    
    if 'floqast' in answer.lower():
        score += 15
        feedback.append("✓ Mentioned why FloQast")
    else:
        feedback.append("✗ Should explain why you're interested in FloQast")
    
    if any(word in answer.lower() for word in ['excited', 'passionate', 'love', 'thrive']):
        score += 10
        feedback.append("✓ Showed enthusiasm")
    else:
        feedback.append("~ Could show more enthusiasm")
    
    # Length check
    word_count = len(answer.split())
    if 80 <= word_count <= 150:
        feedback.append(f"✓ Good length ({word_count} words)")
    elif word_count < 80:
        feedback.append(f"~ Too brief ({word_count} words - aim for 100-150)")
    else:
        feedback.append(f"~ Too long ({word_count} words - aim for 100-150)")
    
    # Results
    print("\n" + "-"*70)
    print("OPENING PITCH SCORE:")
    for fb in feedback:
        print(f"  {fb}")
    
    print(f"\nTOTAL: {score}/100")
    
    print("\n" + "-"*70)
    print("IDEAL OPENING:")
    print("-"*70)
    print("""
"I'm Ranvir Thind, Finance grad from UW Foster with hands-on accounting
experience at Thind Transport and consulting. 

At Thind Transport, I supported month-end close - accruals, reconciliations,
variance analysis. The manual work frustrated me, so I taught myself VBA
and automated our monthly reporting, cutting 8 hours down to 1.5 hours -
an 80% time savings.

In my consulting work, I've done client-facing financial modeling and
automated Salesforce workflows for 2,000+ accounts. I've learned to
translate complex technical solutions into business value for stakeholders.

What excites me about FloQast's AFDA role is that it combines everything
I love: accounting fundamentals, process automation, and customer
partnership. I understand the pain of manual month-end work, and I want
to help customers solve it with technology."

[~140 words, ~1 minute speaking]
""")
    
    return score >= 60


def quick_fire_questions():
    """Rapid-fire common questions"""
    
    print("\n" + "="*70)
    print("QUICK-FIRE QUESTIONS")
    print("="*70)
    
    print("""
Practice answering common questions quickly and clearly.
Give concise answers (30-60 seconds each).
""")
    
    total_score = 0
    
    questions = [
        {
            "q": "Why FloQast?",
            "key_words": ["ai", "accounting", "bridge", "forward deployed", "customer"],
            "ideal": "AI + accounting is the future. The AFDA role is unique - it's the bridge between accounting and technology, which is exactly where I thrive. Plus I love being forward deployed with customers."
        },
        {
            "q": "Why this role specifically?",
            "key_words": ["customer", "diverse", "configure", "impact", "consulting"],
            "ideal": "I love being embedded with customers, seeing diverse workflows, configuring real solutions, and seeing direct impact. That's the consulting experience I love, with a product I believe in."
        },
        {
            "q": "What's your biggest strength?",
            "key_words": ["automation", "technical", "accounting", "hybrid", "translate"],
            "ideal": "My hybrid skillset - I understand accounting workflows from hands-on experience AND I can configure technical automation. I translate between accounting and technology."
        }
    ]
    
    for i, q_data in enumerate(questions, 1):
        print(f"\n--- Question {i}/3 ---")
        print(f"INTERVIEWER: {q_data['q']}")
        
        answer = get_input("\nYOU: ")
        
        score = 0
        for keyword in q_data['key_words']:
            if keyword in answer.lower():
                score += 20
        
        score = min(score, 100)
        total_score += score
        
        if score >= 60:
            print(f"✓ Good answer ({score}/100)")
        else:
            print(f"~ Needs work ({score}/100)")
            print(f"Ideal: {q_data['ideal']}")
    
    avg_score = total_score / 3
    
    print("\n" + "-"*70)
    print(f"AVERAGE SCORE: {avg_score:.0f}/100")
    
    if avg_score >= 70:
        print("✓ Strong quick responses!")
    else:
        print("~ Practice these until they're second nature")
    
    return avg_score >= 60


def your_questions():
    """Questions for the interviewer"""
    
    print("\n" + "="*70)
    print("YOUR QUESTIONS FOR THEM")
    print("="*70)
    
    print("""
INTERVIEWER:
"We have a few minutes left. What questions do you have for me?"

YOUR TASK: Ask 3 thoughtful questions.
Type each question.
""")
    
    score = 0
    feedback = []
    questions_asked = []
    
    good_topics = ['team', 'success', 'onboard', 'train', 'customer', 'day', 'challenge', 
                   'typical', 'deployment', 'first', '90 days', 'feedback', 'product']
    
    bad_topics = ['salary', 'vacation', 'benefits', 'hours', 'remote', 'time off']
    
    for i in range(1, 4):
        q = get_input(f"\nQuestion {i}: ")
        questions_asked.append(q)
        
        if any(topic in q.lower() for topic in good_topics):
            score += 33
            feedback.append(f"✓ Q{i}: Good question")
        elif any(topic in q.lower() for topic in bad_topics):
            score -= 20
            feedback.append(f"✗ Q{i}: Avoid compensation/schedule questions in first interview")
        else:
            score += 10
            feedback.append(f"~ Q{i}: Okay but could be more specific")
    
    # Results
    print("\n" + "-"*70)
    print("YOUR QUESTIONS SCORE:")
    for fb in feedback:
        print(f"  {fb}")
    
    print(f"\nTOTAL: {max(0, score)}/100")
    
    print("\n" + "-"*70)
    print("IDEAL QUESTIONS:")
    print("-"*70)
    print("""
1. "What does a typical customer deployment look like from start to finish?"
2. "How is the AFDA team structured? Who would I work with day-to-day?"
3. "What are the most common challenges AFDAs face in the first 90 days?"
4. "How does customer feedback flow back to the product team?"
5. "What does success look like for an AFDA in the first year?"

AVOID asking about: salary, vacation, benefits, remote work in first interview
""")
    
    return score >= 50


def main():
    print("\n" + "="*70)
    print("DAY 6: HANDS-ON INTERVIEW PREP")
    print("="*70)
    
    print("""
Practice key interview moments.

Available Exercises:
  1 - Opening Pitch
  2 - Quick-Fire Questions
  3 - Your Questions for Them
  Q - Quit
""")
    
    while True:
        try:
            choice = input("\nChoose exercise (1-3, Q to quit): ").strip()
            
            if choice.lower() == 'q':
                break
            
            elif choice == '1':
                opening_pitch()
                input("\nPress Enter to continue...")
            
            elif choice == '2':
                quick_fire_questions()
                input("\nPress Enter to continue...")
            
            elif choice == '3':
                your_questions()
                input("\nPress Enter to continue...")
            
            else:
                print("Invalid choice.")
                
        except KeyboardInterrupt:
            break
        except EOFError:
            opening_pitch()
            quick_fire_questions()
            your_questions()
            break


if __name__ == "__main__":
    main()



