# AEO Assessment — Must Have Foundation

> **Purpose:** Score current state of AEO foundations to identify gaps and prioritize fixes  
> **Scoring:** 🟢 Green (3pts) | 🟡 Yellow (2pts) | 🔴 Red (1pt) | ⚫ N/A (skip)  
> **Time:** 2-4 hours for full assessment

## Assessment Info
- **Company/Brand:** _[name]_
- **Assessed by:** _[name]_
- **Date:** _[YYYY-MM-DD]_
- **Stakeholders present:** _[names]_

---

## Section 1: Entity Clarity & Knowledge Graph

**Section Score:** ____ / ____ points (____ %)  
*(Calculate: Sum of points / Sum of max points for applicable items × 100)*

### 1.1 Public fact sheet (company & leadership)
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:** 
- URL: _____________________
- Screenshot: _[attach if needed]_

**What we found:**
_[Describe current state: e.g., "About page exists at /about but missing founding year, certifications, and client list"]_

**Notes:**
_[Why this matters for this company, specific gaps, opportunities]_

**If Yellow/Red, what's needed to reach Green:**
_[Specific actions: e.g., "Add: founding year (2015), SOC 2 certification, 3-5 notable clients, leadership bios with photos"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

### 1.2 Organization & Person schema with `sameAs`
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Schema validator URL: _____________________ (https://validator.schema.org/)
- Schema present: [ ] Yes | [ ] No
- Validation result: [ ] Pass | [ ] Fail | [ ] Warnings

**What we found:**
_[e.g., "Organization schema exists on /about but missing sameAs links; Person schema not found on any author pages"]_

**Notes:**
- Organization schema: _[present/missing, what's included]_
- Person schema: _[how many author pages, which have schema]_
- sameAs links: _[which profiles are linked: LinkedIn, X, YouTube, GitHub, etc.]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Add sameAs to Org schema (LinkedIn, X, YouTube); Create Person schema for 3 key authors; Validate all schemas"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

### 1.3 Wikidata entity verification & creation
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Wikidata Q-ID (company): _____________________ (or "Not found")
- Wikidata Q-IDs (key people): _____________________
- Wikipedia page: [ ] Yes | [ ] No | [ ] Draft submitted

**What we found:**
_[e.g., "No Wikidata entry found for company; CEO has Q-ID Q67890 but missing company affiliation"]_

**Notes:**
- Company notability: [ ] Meets criteria | [ ] Borderline | [ ] Does not meet
- Key people to include: _[list names, roles]_
- Data accuracy: _[if exists, what needs updating]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Create Wikidata entry with: legal name, founding date (2015), HQ (San Francisco), industry (SaaS), website, sameAs links; Create entries for CEO and CTO"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

### 1.4 Google Knowledge Graph presence verified
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Knowledge Graph API result: [ ] Found | [ ] Not found
- API URL: _____________________ (https://developers.google.com/knowledge-graph/)
- Screenshot: _[if found]_

**What we found:**
_[e.g., "Appears in KG but with outdated logo and wrong headquarters location"]_

**Notes:**
- Entity type shown: _[Organization, Company, etc.]_
- Description accuracy: _[correct/incorrect/missing]_
- Logo/image: _[correct/outdated/missing]_
- Linked profiles: _[which appear, which are missing]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Update Wikidata with current logo (→ propagates to KG); Fix headquarters location; Wait 2-4 weeks for KG refresh"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

### 1.5 Consistency across profiles
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Profiles checked: _[list: website, LinkedIn, X, YouTube, GitHub, etc.]_
- Brand name variants found: _[list any inconsistencies]_

**What we found:**
_[e.g., "Company name consistent but logo varies; LinkedIn bio is 3x longer than website; CTO profile mixes personal and company topics"]_

**Notes:**
- Name consistency: _[✓ consistent | ✗ variations found: _____]_
- Logo consistency: _[✓ consistent | ✗ variations: _____]_
- Bio consistency: _[✓ aligned | ✗ differs: _____]_
- Topic focus: _[✓ tight | ✗ mixed (list off-topic content)]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Standardize logo across all profiles (use 2024 version); Shorten LinkedIn bio to match website (3 sentences); Update bios on X and GitHub"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

**Section 1 Summary:**
- **Applicable checks:** ___ / 5  
- **Points earned:** ___ / ___ possible  
- **Section score:** ___ %
- **Status:** [ ] 🟢 Green (80-100%) | [ ] 🟡 Yellow (50-79%) | [ ] 🔴 Red (0-49%)

**Top 3 priorities for this section:**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

## Section 2: Citable Content & Sourceability

**Section Score:** ____ / ____ points (____ %)

### 2.1 Inline citations next to important claims
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Pages reviewed: _[list 5-10 key pages checked]_
- Citations found: ___ inline citations across all pages
- Average citations per claim: ___

**What we found:**
_[e.g., "0 inline citations found. All claims unsourced. Some links at bottom but not next to claims. Sources used: 2 blogs, 1 vendor site (low quality)"]_

**Notes:**
- Strong claims without sources: _[count, examples]_
- Sources currently used: _[types: gov/edu, media, blogs, etc.]_
- Citation placement: _[next to claims | bunched at bottom | missing]_
- Source quality: _[reputable | mixed | low-quality]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Add 15-20 inline citations to top 3 cornerstone pages; Source from: industry standards (NIST), top-tier media (WSJ, TechCrunch), platform docs; Place immediately after each claim"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

### 2.2 Methods & data for numeric claims (table/CSV)
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Pages with numeric claims: _[count]_
- Pages with methods documented: _[count]_
- Pages with data tables: _[count]_
- Downloadable datasets: _[count]_

**What we found:**
_[e.g., "5 pages make numeric claims (ROI, benchmark stats) but 0 explain methodology. No data tables or CSV downloads found."]_

**Notes:**
- Types of claims: _[benchmarks, ROI, performance, survey results, etc.]_
- Current evidence level: _[none | vague | partial | complete]_
- What's missing: _[sample size, date, method, tools, etc.]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Add Methods & Data section to benchmark page: 'Tested 47 tools (Nov 2024), using X methodology, sample size N=1000'; Create 3-column table with results; Offer CSV download; Optional: get DOI via Zenodo"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

### 2.3 Author expertise visible
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Content pages reviewed: _[count]_
- Pages with author attribution: _[count]_
- Pages with author boxes: _[count]_
- Author pages with Person schema: _[count]_

**What we found:**
_[e.g., "All articles show author name but no photo, title, or link to profile. No author pages exist. No Person schema found."]_

**Notes:**
- Current attribution: _[name only | name+title | full box with photo]_
- Author pages: _[exist | missing]_
- Person schema: _[present on ___ pages | missing]_
- Credentials shown: _[yes | no | partial]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Create author boxes for 3 key contributors (name, title, headshot, 2-sentence bio, link); Build author profile pages at /authors/[name]; Add Person schema with jobTitle, affiliation, sameAs to LinkedIn"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

**Section 2 Summary:**
- **Applicable checks:** ___ / 3  
- **Points earned:** ___ / ___ possible  
- **Section score:** ___ %
- **Status:** [ ] 🟢 Green (80-100%) | [ ] 🟡 Yellow (50-79%) | [ ] 🔴 Red (0-49%)

**Top 3 priorities for this section:**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

## Section 3: Extractability Assessment

**Section Score:** ____ / ____ points (____ %)

### 3.1 Score key passages using 0–3 rubric
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Passages scored: ___ / 20-30 target
- Score 3 (Excellent): ___ passages (___%)
- Score 2 (Good): ___ passages (___%)
- Score 1 (Weak): ___ passages (___%)
- Score 0 (Not extractable): ___ passages (___%)
- **Average score:** ___ / 3

**What we found:**
_[e.g., "Scored 10 passages from 3 cornerstone pages. Average 1.2/3. Most are rambling paragraphs without clear claims or sources."]_

**Notes:**
- Pages assessed: _[URLs]_
- Common issues: _[list: no sources, vague claims, missing dates, poor formatting, etc.]_
- Best examples: _[passages that scored 2-3, why they work]_
- Worst examples: _[passages that scored 0-1, what's missing]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Rewrite 8 low-scoring passages to be concise (2-3 sentences); Add inline citations; Add dates; Break rambling paragraphs; Add tables for numeric claims; Target: 70%+ passages at score ≥2"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

**Attach:** Link to extractability scoring sheet with passage-by-passage breakdown

---

**Section 3 Summary:**
- **Applicable checks:** ___ / 1  
- **Points earned:** ___ / ___ possible  
- **Section score:** ___ %
- **Status:** [ ] 🟢 Green (80-100%) | [ ] 🟡 Yellow (50-79%) | [ ] 🔴 Red (0-49%)

**Top priority for this section:**
1. _______________________________________________

---

## Section 4: Fact-Checking & Content Updates

**Section Score:** ____ / ____ points (____ %)

### 4.1 Fact-checking workflow for new claims
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Written workflow doc: [ ] Yes | [ ] No
- 2-source rule documented: [ ] Yes | [ ] No
- Correction process exists: [ ] Yes | [ ] No
- Correction SLA: ___ hours/days

**What we found:**
_[e.g., "No documented fact-checking process. Content goes live without verification. No correction policy visible."]_

**Notes:**
- Current approval flow: _[describe who approves, what they check]_
- Source verification: _[done | not done | inconsistent]_
- Correction handling: _[process exists | ad-hoc | none]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Create 1-page fact-checking workflow: 2 independent sources required for strong claims; Legal review for medical/financial; Corrections within 48 hours; Reviewer sign-off before publish"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

### 4.2 Quarterly fact refresh
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Last content review date: _____________________
- Pages showing "Last updated": ___ / ___ pages
- Review cadence: [ ] Quarterly | [ ] 6-month | [ ] Annual | [ ] None

**What we found:**
_[e.g., "No 'Last updated' dates shown. Oldest content from 2019. Statistics from 2021 still cited as current. No review schedule."]_

**Notes:**
- Outdated content found: _[list examples: old stats, former employees, expired certs]_
- Content freshness: _[current | somewhat current | very outdated]_
- Review process: _[scheduled | ad-hoc | none]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Add 'Last updated: YYYY-MM-DD' to all cornerstones; Review & update stats/certs/leadership quarterly; Set Q1/Q2/Q3/Q4 review calendar; Assign review owner"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

### 4.3 Correction policy visible
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Corrections page exists: [ ] Yes | [ ] No
- URL: _____________________
- Number of corrections logged: ___

**What we found:**
_[e.g., "No public corrections page. No transparency on what changes when errors are found."]_

**Notes:**
- Corrections needed now: _[list any known errors]_
- Transparency level: _[high | medium | low]_
- Trust signals: _[present | missing]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Create /corrections page; Format: Date | Page | What Changed | Why; Add note to corrected pages linking to corrections log; Builds trust with LLMs and readers"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

**Section 4 Summary:**
- **Applicable checks:** ___ / 3  
- **Points earned:** ___ / ___ possible  
- **Section score:** ___ %
- **Status:** [ ] 🟢 Green (80-100%) | [ ] 🟡 Yellow (50-79%) | [ ] 🔴 Red (0-49%)

**Top 3 priorities for this section:**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

## Section 5: Competitive Intelligence & Monitoring (Baseline)

**Section Score:** ____ / ____ points (____ %)

### 5.1 LLM Test Deck (baseline run)
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Test deck exists: [ ] Yes | [ ] No
- Number of prompts: ___ / 20-40 target per persona
- Engines tested: [ ] ChatGPT [ ] Claude [ ] Gemini [ ] Perplexity
- Regions tested: ___ / 2 target (e.g., US, EU)
- Baseline run completed: [ ] Yes | [ ] No | [ ] Partial

**What we found:**
_[e.g., "No test deck exists. Have not tested if company appears in AI answers. Don't know current inclusion rate or position."]_

**Notes:**
- Prompts created: _[count, examples]_
- Coverage: _[entity queries | commercial | disambiguation | all three]_
- Testing frequency: _[monthly | quarterly | none]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Create 30 prompts (10 per persona): entity ('Who is [Company]?'), commercial ('Best [solution] for [use case]'), disambiguation ('Facts about [Company]'); Run across 4 engines × 2 regions = 240 tests; Document results in spreadsheet"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

### 5.2 Document baseline results
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Results documented: [ ] Yes | [ ] No
- Current inclusion rate: ___ % (if known)
- Position distribution: Lead ___ % | Listed ___ % | Footnote ___ %
- Top competitors cited: _____________________

**What we found:**
_[e.g., "Manual spot-check: Appeared in 2/10 test queries, both as Footnote. Competitors X and Y cited as Lead in 8/10 queries."]_

**Notes:**
- Where we appear: _[which engines, which types of queries]_
- Where we don't: _[gaps, patterns]_
- Competitor advantage: _[why they're cited instead]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Complete full test deck run (from 5.1); Log all results: Included Y/N, Position (Lead/Listed/Footnote), Rationale given, Sources cited, Competitors mentioned; Calculate baseline inclusion rate"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

**Section 5 Summary:**
- **Applicable checks:** ___ / 2  
- **Points earned:** ___ / ___ possible  
- **Section score:** ___ %
- **Status:** [ ] 🟢 Green (80-100%) | [ ] 🟡 Yellow (50-79%) | [ ] 🔴 Red (0-49%)

**Top 2 priorities for this section:**
1. _______________________________________________
2. _______________________________________________

---

## Section 6: Measurement (AEO) — Basic Tracking

**Section Score:** ____ / ____ points (____ %)

### 6.1 Track basic AEO KPIs monthly
- [ ] 🟢 Green (3pts) | [ ] 🟡 Yellow (2pts) | [ ] 🔴 Red (1pt) | [ ] ⚫ N/A

**Evidence:**
- Tracking system exists: [ ] Yes | [ ] No (spreadsheet/dashboard)
- Metrics tracked: [ ] Share of Inclusion [ ] Position [ ] Citations [ ] None
- Tracking frequency: [ ] Monthly | [ ] Quarterly | [ ] Ad-hoc | [ ] None
- Baseline data: [ ] Yes | [ ] No

**What we found:**
_[e.g., "No AEO tracking. Track website traffic and SEO rankings but not AI citations. No baseline data on inclusion rate."]_

**Notes:**
- Current tracking: _[what's measured now]_
- Data availability: _[easy to get | requires manual work | don't know how]_
- Owner: _[who would track this]_

**If Yellow/Red, what's needed to reach Green:**
_[e.g., "Set up monthly tracking sheet with: Share of Inclusion (% of test prompts where we appear), Position distribution (Lead/Listed/Footnote %), Citation presence (Y/N per test); Run baseline in Month 1, track MoM changes; Assign owner"]_

**Estimated effort:** ___ hours  
**Priority:** [ ] Critical | [ ] High | [ ] Medium | [ ] Low

---

**Section 6 Summary:**
- **Applicable checks:** ___ / 1  
- **Points earned:** ___ / ___ possible  
- **Section score:** ___ %
- **Status:** [ ] 🟢 Green (80-100%) | [ ] 🟡 Yellow (50-79%) | [ ] 🔴 Red (0-49%)

**Top priority for this section:**
1. _______________________________________________

---

## OVERALL ASSESSMENT SUMMARY

### Total Score
- **Total applicable checks:** ___ / 15 maximum
- **Total points earned:** ___ / ___ possible  
- **Overall AEO Maturity Score:** ___ %

**Maturity Level:**
- [ ] 🟢 **Green (80-100%)** — Strong foundation, ready for amplification
- [ ] 🟡 **Yellow (50-79%)** — Foundation started, key gaps remain
- [ ] 🔴 **Red (0-49%)** — Significant work needed before AI can cite you

---

### Scores by Section

| Section | Score | Status | Top Gap |
|---------|-------|--------|---------|
| 1. Entity Clarity | ___% | 🟢🟡🔴 | _________________ |
| 2. Citable Content | ___% | 🟢🟡🔴 | _________________ |
| 3. Extractability | ___% | 🟢🟡🔴 | _________________ |
| 4. Fact-Checking | ___% | 🟢🟡🔴 | _________________ |
| 5. Competitive Intel | ___% | 🟢🟡🔴 | _________________ |
| 6. Measurement | ___% | 🟢🟡🔴 | _________________ |

---

### What's Working ✅
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

### Critical Gaps 🚨
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

### Quick Wins (High impact, low effort)
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

### Recommended Focus

**Phase 1 (Days 1-14): Critical fixes**
- [ ] Fix #1: _____________________________________ (___ hrs)
- [ ] Fix #2: _____________________________________ (___ hrs)
- [ ] Fix #3: _____________________________________ (___ hrs)

**Phase 2 (Days 15-30): High-priority improvements**
- [ ] Fix #4: _____________________________________ (___ hrs)
- [ ] Fix #5: _____________________________________ (___ hrs)
- [ ] Fix #6: _____________________________________ (___ hrs)

**Phase 3 (Days 31-60): Complete foundation**
- [ ] Fix #7: _____________________________________ (___ hrs)
- [ ] Fix #8: _____________________________________ (___ hrs)
- [ ] Fix #9: _____________________________________ (___ hrs)

**Total estimated effort:** ___ hours (~___ weeks with ___ people)

---

### Next Steps

1. **Review findings** with stakeholders (_________________)
2. **Prioritize fixes** based on impact and effort
3. **Assign owners** to critical items (Phase 1)
4. **Set 30-day sprint** to complete Phase 1
5. **Schedule follow-up assessment** (_________________)

---

## Assessment Methodology

**Time spent:** ___ hours  
**Tools used:** _[list: validators, APIs, manual review, etc.]_  
**Pages reviewed:** ___ total  
**People interviewed:** _[names, roles]_  

**Limitations:**
_[Note any areas not fully assessed, data unavailable, etc.]_

**Confidence level:** [ ] High | [ ] Medium | [ ] Low  
**Reason:** _______________________________________________

