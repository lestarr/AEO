
# Project Instructions — Toolkit for Modern Marketing (SEO + AEO)

## Goal

Build and run a practical toolkit that:

1. **Assesses** current **SEO** (classic search) and **AEO/GENAI-O** (LLM/answer engines).
2. **Finds gaps** and produces a prioritized **action plan**.
3. **Evaluates** results with clear acceptance tests.
4. **Runs telemetry** (periodic LLM tests + dashboards) with short reports.

## Source of Truth (Docs)

**Prioritized Checklists:**
* **SEO Checks — Must Have** (🔴 P0 - Days 1-60) → checks_seo_must_have.md
* **SEO Checks — Nice to Have** (🟡 P1 - Days 61-90+) → checks_seo_nice_to_have.md
* **AEO Checks — Must Have** (🔴 P0 - Days 1-60) → checks_aeo_must_have.md
* **AEO Checks — Nice to Have** (🟡 P1 - Days 61-90+) → checks_aeo_nice_to_have.md

**Assessment Documents (2-phase: Discovery + Report):**
* **AEO Must Have Assessment** → assessment_aeo_must_have.md
* **AEO Nice to Have Assessment** → assessment_aeo_nice_to_have.md
* **SEO Must Have Assessment** → assessment_seo_must_have.md
* **SEO Nice to Have Assessment** → assessment_seo_nice_to_have.md
* **How to Run Assessments** → prompts_for_assessments.md (4 ready-to-use prompts)

**Supporting Docs:**
* **Telemetry & Evaluation — AEO + SEO** → telemetry_evaluation_aeo_seo_dashboards_test_deck_extractability.md
* **Governance & Ops — RACI, Editorial Rules, Cadence** → governance_ops_raci_editorial_rules_cadence.md
* **Templates & Glossary** → templates_glossary_starters_for_seo_aeo.md
* **90-Day Plan** → 90_day_plan_foundations_→_entity_→_proof_scale.md
* **Example: Persona & Cornerstone** → example_persona_cornerstone_rag_saas.md

## Inputs you can expect to receive

* Site URLs / sitemap; analytics access or exports; target markets/languages.
* Brand facts (legal name, founding year, locations, leadership), author list, social/profile links.
* Top personas (or a request to draft them), and 10–20 key questions per persona.
* Existing cornerstone pages, videos, LinkedIn posts, and any datasets/tables.

## What to produce (every run)

1. **Assessment (SEO + AEO)**

   * Start with **Must Have** checklists (🔴 P0) for both SEO and AEO.
   * Mark each item: **Green** (done), **Yellow** (partial), **Red** (missing).
   * Link to evidence (URLs/screenshots/validator output).
   * Only assess **Nice to Have** (🟡 P1) items after Must Haves are >80% complete.

2. **Gap Analysis & Action Plan**

   * Prioritize all **Red** Must Have items first.
   * For each **Yellow/Red** item: write a **fix** (what to do), **owner**, **ETA**, and **acceptance test** ("Done when …").
   * Add to the **90-Day Plan** (Days 1–30, 31–60, 61–90) with dates and owners.

3. **Evaluation (acceptance tests)**

   * Confirm each shipped fix against its “Done when” condition (e.g., schema validates; page has inline citations + methods table; cannibal pages merged).
   * Note pass/fail and blockers.

4. **Telemetry (LLM + SEO)**

   * Update **Telemetry & Evaluation**:

     * **LLM:** Run the **Test Deck** (e.g., “best credit card for travel”) across ChatGPT, Claude, Gemini, Perplexity in 2 regions; capture **AIO shown? included? position? citations?** and **screenshots/links**.
     * **SEO:** Refresh impressions/clicks/CTR/backlinks/assisted conversions for cornerstone pages.
   * Summarize **deltas vs last run** and **top 5 next actions**.

## Cadence

* **Weekly (Ops):** 30–45 min standup → update Checks, unblock owners, add tasks to the 90-Day Plan.
* **Monthly (AEO review):** Refresh LLM tests + Telemetry; ship **3–5 fixes** based on gaps (not cited/wrong fact/competitor preferred).
* **Quarterly (Audit):** Full schema validation, cannibalization sweep, inclusion trends by intent; reset targets.

## Prompts to use inside this project

> **For detailed assessment prompts:** See prompts_for_assessments.md (4 ready-to-use prompts with persona & rules)

* **Assessment (using assessment docs):** Use the 4 prompts from prompts_for_assessments.md with the corresponding assessment files. Each prompt ensures systematic, section-by-section evaluation.
* **Gaps → Plan:** "Turn all Red Must Have items into a prioritized action list with owner, ETA, acceptance test. Merge into the **90-Day Plan** Days 1-60."
* **Evaluation:** "Verify completed items against acceptance tests. Mark pass/fail and list blockers."
* **Telemetry:** "Run/update the **LLM Test Deck** for these prompts in US/EU; fill the telemetry table (inclusion, position, citations, sentiment) and summarize week-over-week changes. Refresh SEO KPIs for cornerstones and list the top 5 next actions."
* **After Must Haves complete:** Use the Nice to Have assessment prompts from prompts_for_assessments.md (only after Must Have score >80%).

## Success criteria (keep visible)

* **SEO:** Cornerstones live; cannibalization resolved; schema valid; traffic and assisted conversions trending up.
* **AEO:** Higher **share of inclusion**, better **position in answers** (Lead > Listed), more and higher-quality **citations**, stronger **overlap with organic** for target intents, and tangible **downstream impact** (brand queries, direct visits, leads).

Look up success_criteria.md

