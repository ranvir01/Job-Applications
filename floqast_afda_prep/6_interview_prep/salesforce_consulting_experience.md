# 🎯 Salesforce Consulting Experience - Interview Stories

*Consultant: Ranvir (AI-Driven Business Growth)*  
*Client: AI-Driven Business Growth*  
*Timeline: On Call | ~30 hours total*  
*Rate: $25/hr SD Rate | $1,850 completed (Now)*

---

## 📖 The Narrative (How to Tell the Story)

"I came in, saw a Salesforce that was slow and full of noise. First thing—lead to opportunity conversion was broken. Description field disappeared, user ID wasn't passed, button didn't even show. I rebuilt the flow, remapped the fields, made sure the lead turned into an account and opportunity without any manual copy-paste. Then I cleaned the data—removed 700 duplicates between leads and contacts using a mass merge. After that, I built a simple flow: every time a lead pops in, boom—a task shows up for the rep: send intro email, pre-filled with the lead name. No more excuses. Later, I kept the thing breathing—updated dashboards so the CFO sees pipeline by week, color-coded by win-rate. Changed branding so it didn't look cheap. Backed up weekly. Caught bugs before the client screamed. No dev background—just logic, curiosity, and not accepting 'that's how it works.'"

---

## 🎯 Key Achievements Summary

| Area | What I Did | Impact |
|------|-----------|--------|
| **Lead-to-Opportunity Conversion** | Fixed broken flow (missing description, UserID, button visibility) | 95% completion rate for conversions |
| **Data Cleanup** | Mass merged 700+ duplicate leads/contacts | Clean, actionable database |
| **Workflow Automation** | Built automated task creation flow with pre-filled templates | Zero manual task creation; instant follow-up |
| **Executive Dashboards** | Updated CFO pipeline dashboards (weekly view, win-rate color coding) | Real-time visibility into sales pipeline |
| **System Maintenance** | Weekly backups, bug fixes, branding updates | System reliability & professional appearance |

---

## ⭐ STAR Stories for Interviews

### Story 1: Fixing Lead-to-Opportunity Conversion (Problem-Solving Under Pressure)

**Situation**  
When I started consulting for AI-Driven Business Growth, their Salesforce lead conversion process was completely broken. Sales reps couldn't convert leads to opportunities properly—the description field was disappearing, user IDs weren't being passed through, and the conversion button wasn't even showing up half the time. This meant manual data entry, lost information, and frustrated sales reps who were just avoiding the system.

**Task**  
My job was to diagnose the broken conversion flow and rebuild it so leads could convert to accounts and opportunities seamlessly—no manual copy-paste, no lost data, no user friction.

**Action**  
1. **Diagnosed the issue**: I mapped out the existing flow step-by-step. Found that field mappings were misconfigured—the description field wasn't mapped to the opportunity, UserID wasn't being passed during conversion, and visibility rules on the conversion button were too restrictive.

2. **Rebuilt the flow**: I went into Flow Builder and rebuilt the lead conversion automation from scratch:
   - Remapped all critical fields (Description → Opportunity Description, Lead Owner → Account Owner)
   - Fixed UserID passing to ensure ownership tracking
   - Adjusted button visibility rules so it appeared for all active leads

3. **Tested edge cases**: I ran through multiple scenarios—different lead sources, different user roles, leads with missing data—to ensure the flow didn't break under real-world conditions.

4. **Documented the fix**: Created process documentation so the client understood what was fixed and how to troubleshoot if issues arose.

**Result**  
Lead-to-opportunity conversion went from broken to **95% successfully completed**. Sales reps no longer had to manually copy data. The client saw immediate improvement in data quality and rep productivity. No dev background—just logical troubleshooting and refusing to accept "that's how it works."

---

### Story 2: Data Cleanup - 700 Duplicate Records (Data Quality & Operations)

**Situation**  
The Salesforce instance was full of noise—over 700 duplicate records between Leads and Contacts. This made reporting unreliable, caused confusion for sales reps (which record is the real one?), and inflated metrics artificially.

**Task**  
Clean up the duplicate records without losing critical data or breaking relationships to existing opportunities and accounts.

**Action**  
1. **Identified duplicates**: Used Salesforce's duplicate management tools and manual review to identify 700+ duplicate leads and contacts.

2. **Mass merge process**: 
   - Determined which record was the "master" (most complete, most recent activity)
   - Used Salesforce mass merge functionality to consolidate duplicates
   - Ensured all related tasks, emails, and opportunities were preserved under the master record

3. **Validation**: After merging, I ran reports to confirm no data loss and that all relationships (Account-Contact, Contact-Opportunity) were intact.

**Result**  
Removed **700+ duplicate records**, resulting in a clean, actionable database. Reporting accuracy improved immediately—the CFO could now trust pipeline numbers. Sales reps had clarity on who to contact without sifting through duplicates.

---

### Story 3: Automated Task Creation Workflow (Automation & User Adoption)

**Situation**  
Sales reps were inconsistent about following up on new leads. There was no structured process—some reps would forget, some would delay, and follow-up quality was inconsistent. The client needed a way to ensure every lead got immediate attention.

**Task**  
Build an automated workflow that created a task for the sales rep immediately when a new lead came in, with pre-filled context so they could act fast.

**Action**  
1. **Designed the flow**: Every time a lead is created in Salesforce, a Flow automatically:
   - Creates a task assigned to the lead owner
   - Pre-fills the task description with the lead's name, company, and source
   - Sets the task subject to "Send intro email"
   - Sets due date to same day (forcing immediate action)

2. **Used AI tools to accelerate**: Leveraged ChatGPT and Cursor to research best practices for Salesforce Flow automation and troubleshoot syntax issues during implementation.

3. **User training**: Walked the sales team through the new workflow—explained why it existed (no more excuses for not following up), how it worked, and what they needed to do.

**Result**  
**Zero manual task creation**—every lead automatically generated a task. Follow-up became systematic. Sales reps had no excuse for missing leads because the task was already in their queue with all the context they needed. Adoption was immediate because it made their job easier, not harder.

---

### Story 4: Executive Dashboard for CFO (Reporting & Stakeholder Management)

**Situation**  
The CFO needed real-time visibility into the sales pipeline but was relying on static spreadsheets that were outdated by the time they were reviewed. He wanted to see pipeline by week, understand win rates, and identify risks quickly.

**Task**  
Build a dynamic Salesforce dashboard that gave the CFO the insights he needed without requiring manual data pulls.

**Action**  
1. **Gathered requirements**: Sat down with the CFO to understand what metrics mattered—weekly pipeline value, win rate by stage, deal velocity, and at-risk opportunities.

2. **Built the dashboard**:
   - Created weekly pipeline view (grouped by expected close date)
   - Added color coding based on win-rate probability (green = high, yellow = medium, red = at-risk)
   - Included filters for deal size, sales rep, and lead source

3. **Customized branding**: Updated the dashboard colors and layout so it didn't look "cheap"—professional, clean, executive-ready.

4. **Training**: Walked the CFO through how to use filters, drill into specific deals, and interpret the metrics.

**Result**  
The CFO went from **static spreadsheets to real-time visibility**. He could now see pipeline health at a glance, identify at-risk deals before they fell through, and hold sales reps accountable. The dashboard became his primary tool for weekly pipeline reviews.

---

### Story 5: Ongoing System Maintenance (Proactive Problem-Solving)

**Situation**  
After the initial implementation, the client needed ongoing support—bug fixes, minor updates, and system reliability.

**Task**  
Keep the Salesforce system running smoothly, catch issues before they became problems, and ensure data integrity.

**Action**  
1. **Weekly backups**: Implemented a backup schedule for critical data (leads, contacts, opportunities).
2. **Bug fixes**: Proactively monitored for errors (flow failures, field mapping issues) and fixed them before the client noticed.
3. **Testing & updates**: Tested new features before rolling them out, ensured updates didn't break existing workflows.
4. **Branding updates**: Made UI improvements so the system looked professional and aligned with the company's brand.

**Result**  
The client experienced **zero major outages or data loss**. Bugs were caught and fixed proactively. The system became reliable and trustworthy, which increased user adoption.

---

## 🔗 How This Experience Connects to FloQast AFDA Role

| FloQast Requirement | My Salesforce Experience |
|---------------------|--------------------------|
| **Understand customer workflows** | Mapped broken lead conversion process, understood sales team pain points |
| **Configure automation** | Built automated task creation, rebuilt lead-to-opportunity flow |
| **Train users** | Trained sales team on new workflows, walked CFO through dashboard |
| **Troubleshoot & debug** | Fixed field mapping issues, flow errors, button visibility problems |
| **Data quality** | Cleaned 700+ duplicates, ensured data integrity during merges |
| **Proactive problem-solving** | Weekly backups, caught bugs before escalation |
| **Customer-facing communication** | Worked directly with sales reps and CFO to gather requirements and train |
| **No dev background, self-taught** | Same as my Salesforce work—logic, curiosity, AI tools, refusing to accept "it can't be done" |

---

## 💡 Key Talking Points for Interviews

### "I learn by doing"
- No formal Salesforce training—just jumped in, used AI tools (ChatGPT, Cursor), and figured it out
- Same approach I'd take with FloQast's Transform AI Agents platform

### "I focus on impact, not just implementation"
- Fixed lead conversion → 95% completion rate
- Cleaned data → CFO could trust pipeline numbers
- Automated tasks → reps had no excuse for not following up

### "I make complex systems simple for users"
- Sales reps didn't need to understand flows—they just needed tasks to appear
- CFO didn't need to understand Salesforce architecture—he just needed a dashboard he could read

### "I don't accept 'that's how it works'"
- Lead conversion was broken? I rebuilt it.
- Data was messy? I cleaned it.
- Follow-up was inconsistent? I automated it.

---

## 📊 By the Numbers

- **30 hours** of consulting work completed
- **$1,850** revenue generated (SD Rate $25/hr)
- **700+ duplicate records** cleaned
- **95% lead conversion** completion rate
- **Zero manual task creation** after automation
- **Real-time executive dashboards** replacing static spreadsheets
- **No dev background** → self-taught via AI tools and logical problem-solving

---

## 🎤 How to Use This in Interviews

### For behavioral questions:
- "Tell me about a time you solved a complex problem" → **Story 1: Lead Conversion**
- "Tell me about a time you improved a process" → **Story 3: Automated Tasks**
- "Tell me about a time you managed data quality" → **Story 2: Duplicate Cleanup**
- "Tell me about a time you worked with stakeholders" → **Story 4: CFO Dashboard**

### For automation questions:
- "What's your experience with workflow automation?" → **Story 3: Task Automation + Story 1: Flow Rebuild**

### For customer-facing questions:
- "How do you gather requirements?" → **Story 4: CFO Dashboard**
- "How do you train users?" → **Story 3: Sales Team Training**

### For technical questions:
- "How do you troubleshoot system issues?" → **Story 1: Debugging Lead Conversion + Story 5: Proactive Maintenance**

---

*This experience demonstrates: automation, problem-solving, customer communication, data quality, user training, proactive maintenance, self-directed learning—all core to the FloQast AFDA role.*

---

**Last Updated:** January 3, 2026

