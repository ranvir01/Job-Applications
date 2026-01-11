"""
Variance Analysis Validator - AI-Style Feedback
Checks if you identified material variances and provided explanations
"""

import openpyxl
import sys
from datetime import datetime

class VarianceValidator:
    def __init__(self, workbook_path):
        try:
            self.wb = openpyxl.load_workbook(workbook_path)
        except FileNotFoundError:
            print(f"❌ Error: Could not find {workbook_path}")
            sys.exit(1)
    
    def validate(self):
        print("\n" + "="*80)
        print("VARIANCE ANALYSIS VALIDATION")
        print("="*80)
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        try:
            ws_analysis = self.wb["Variance Analysis"]
        except KeyError:
            print("❌ Could not find 'Variance Analysis' sheet")
            return
        
        print("Checking your variance explanations...\n")
        print(f"{'Account':<25} {'Material?':<12} {'Explanation?':<15}")
        print("-"*60)
        
        score = 0
        max_score = 4
        
        # Check rows 11-14 (Revenue, Fuel, Maintenance, Net Income)
        accounts = [
            ("Revenue", 11),
            ("Fuel Expense", 12),
            ("Maintenance Expense", 13),
            ("Net Income", 14)
        ]
        
        for account, row in accounts:
            material = ws_analysis[f'F{row}'].value
            explanation = ws_analysis[f'G{row}'].value
            
            # Check if they provided an explanation
            has_explanation = False
            if explanation and isinstance(explanation, str):
                explanation = explanation.strip().replace('[Your explanation here]', '').strip()
                if explanation and len(explanation) > 20:
                    has_explanation = True
            
            material_display = material if material else "---"
            expl_display = "✓ PROVIDED" if has_explanation else "❌ MISSING"
            
            if has_explanation:
                score += 1
            
            print(f"{account:<25} {material_display:<12} {expl_display:<15}")
        
        print("-"*60)
        pct = int(score / max_score * 100)
        print(f"EXPLANATIONS PROVIDED: {score}/{max_score} ({pct}%)\n")
        
        # Detailed feedback
        print("="*80)
        print("FEEDBACK")
        print("="*80)
        
        if score >= 3:
            print("\n✓ GOOD WORK! You provided explanations for most material variances.")
        else:
            print("\n⚠️  You need to provide explanations for material variances.")
            print("   Material = variance > 10% OR > $5,000")
        
        print("\n💡 HOW TO WRITE GOOD VARIANCE EXPLANATIONS:")
        print("  1. Quantify the change: '$6,500 increase (29.5%)'")
        print("  2. Identify root cause: 'Fuel price increase from $3.80 to $4.50/gal'")
        print("  3. Add business context: 'Peak season demand + 15% more deliveries'")
        print("  4. Be specific: Use numbers, dates, names")
        
        print("\n📊 COMPARE YOUR EXPLANATIONS TO FLUX AI:")
        print("  • Open the 'Flux AI Simulation' sheet")
        print("  • See how FloQast's AI automatically generates variance narratives")
        print("  • Notice the level of detail and business context")
        
        # Example comparison
        print("\n" + "="*80)
        print("EXAMPLE: Good vs. Bad Explanation")
        print("="*80)
        print("\n❌ BAD: 'Fuel went up'")
        print("   → Too vague, no specifics")
        
        print("\n✓ GOOD: 'Fuel costs increased 29.5% ($6,500) due to: 1) 15% increase in")
        print("   mileage from peak season demand (2,850 gallons vs 2,400), and 2) 18.4%")
        print("   fuel price spike from $3.80/gal to $4.50/gal.'")
        print("   → Specific numbers, multiple causes identified, quantified")
        
        # Interview tip
        print("\n" + "="*80)
        print("💡 INTERVIEW TIP - How to explain variance analysis:")
        print("="*80)
        print('"At Thind Transport, I performed monthly variance analysis comparing actuals')
        print('to prior month and budget. For example, in December, we saw fuel expense')
        print('increase 29.5% - I identified this was driven by both volume (15% more')
        print('deliveries) and price (fuel went from $3.80 to $4.50/gal). I documented')
        print('these explanations for management review. This is similar to what FloQast\'s')
        print('Flux agent automates - it analyzes variances and generates narrative')
        print('explanations using AI."')
        
        print("\n" + "="*80)
        if score >= 3:
            print("🏆 WELL DONE! You understand variance analysis.")
            print("   Day 1 complete! Ready for Day 2: Web ERP simulators")
        else:
            print("📚 PRACTICE MORE! Add detailed explanations for each variance.")
        print("="*80)

def main():
    if len(sys.argv) < 2:
        print("Usage: py validate_variance_analysis.py variance_analysis.xlsx")
        sys.exit(1)
    
    workbook_path = sys.argv[1]
    validator = VarianceValidator(workbook_path)
    validator.validate()

if __name__ == "__main__":
    main()



