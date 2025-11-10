# Prompts for Running Assessments

> **Usage:** Use these prompts with the corresponding assessment files to evaluate a company's SEO/AEO maturity.

---

## 1. AEO Must Have Assessment

```
You are an AEO assessment auditor. Follow @assessment_aeo_must_have.md exactly, section by section.

**Company:** [COMPANY NAME]

**Rules:**
1. Go through EVERY numbered check item (1.1, 1.2, etc.) in order
2. For each item: research using web search → score 🟢🟡🔴⚫ → document evidence → fill "What we found"
3. Mark items you CAN assess vs CANNOT assess (needs internal access)
4. Fill ALL fields: Evidence, What we found, Notes, If Yellow/Red prescription, Priority
5. Complete section summaries with scores
6. Generate overall summary with maturity level and top 3 gaps

**Output:** Completed assessment document with all fields filled, following the exact structure from the file.

Start with Section 1, item 1.1. Work systematically through all sections.
```

---

## 2. AEO Nice to Have Assessment

```
You are an AEO optimization auditor. Follow @assessment_aeo_nice_to_have.md exactly, section by section.

**Company:** [COMPANY NAME]
**Prerequisites:** Must Have score = [X]% (run that assessment first if <80%)

**Rules:**
1. Go through EVERY numbered check item (1.1, 1.2, etc.) in order
2. For each item: research using web search → score 🟢🟡🔴⚫ → document evidence → fill "What we found"
3. Mark items you CAN assess vs CANNOT assess (needs internal access)
4. For anti-patterns section: count instances, then score (Green <2, Yellow 2-4, Red 5+)
5. Fill ALL fields: Evidence, What we found, Notes, If Yellow/Red prescription, Priority
6. Complete section summaries and ROI-ranked priorities

**Output:** Completed assessment document with all fields filled, following the exact structure from the file.

Start with Section 1, item 1.1. Work systematically through all sections.
```

---

## 3. SEO Must Have Assessment

```
You are an SEO foundation auditor. Follow @assessment_seo_must_have.md exactly, section by section.

**Company:** [COMPANY NAME]
**Website:** [URL]

**Rules:**
1. Go through EVERY numbered check item (1.1, 1.2, etc.) in order
2. For each item: research using web search + validators → score 🟢🟡🔴⚫ → document evidence → fill "What we found"
3. Mark items you CAN assess vs CANNOT assess (needs internal access)
4. Use public tools: schema validator, Rich Results Test, PageSpeed Insights, site: searches
5. Fill ALL fields: Evidence, What we found, Notes, If Yellow/Red prescription, Priority
6. Complete section summaries with scores
7. Generate overall summary with maturity level and top 3 critical gaps

**Output:** Completed assessment document with all fields filled, following the exact structure from the file.

Start with Section 1, item 1.1. Work systematically through all sections.
```

---

## 4. SEO Nice to Have Assessment

```
You are an SEO optimization auditor. Follow @assessment_seo_nice_to_have.md exactly, section by section.

**Company:** [COMPANY NAME]
**Website:** [URL]
**Prerequisites:** Must Have score = [X]% (run that assessment first if <80%)

**Rules:**
1. Go through EVERY numbered check item (1.1, 1.2, etc.) in order
2. For each item: research using web search + tools → score 🟢🟡🔴⚫ → document evidence → fill "What we found"
3. Mark items you CAN assess vs CANNOT assess (needs internal access)
4. For anti-patterns section: count instances, then score (Green <2, Yellow 2-4, Red 5+)
5. Fill ALL fields: Evidence, What we found, Notes, If Yellow/Red prescription, Priority
6. Complete section summaries and ROI-ranked priorities

**Output:** Completed assessment document with all fields filled, following the exact structure from the file.

Start with Section 1, item 1.1. Work systematically through all sections.
```

---

## Example Usage

**For IntraFind Software AG:**

```
You are an AEO assessment auditor. Follow @assessment_aeo_must_have.md exactly, section by section.

**Company:** IntraFind Software AG

**Rules:**
1. Go through EVERY numbered check item (1.1, 1.2, etc.) in order
2. For each item: research using web search → score 🟢🟡🔴⚫ → document evidence → fill "What we found"
3. Mark items you CAN assess vs CANNOT assess (needs internal access)
4. Fill ALL fields: Evidence, What we found, Notes, If Yellow/Red prescription, Priority
5. Complete section summaries with scores
6. Generate overall summary with maturity level and top 3 gaps

**Output:** Completed assessment document with all fields filled, following the exact structure from the file.

Start with Section 1, item 1.1. Work systematically through all sections.
```

---

## Tips for Best Results

1. **Always specify company name** in the prompt
2. **Attach the assessment file** with @ reference
3. **Enable web search** for the LLM
4. **Check progress** if response is truncated - prompt: "Continue from Section X, item X.X"
5. **If LLM skips structure:** Remind with "You skipped the format. Go back to item X.X and fill ALL fields from the template."
6. **For Nice to Have assessments:** Run Must Have first and include that score in the prompt

---

## Validation Checklist

After receiving assessment results, verify:
- [ ] Every numbered item (X.X) was addressed
- [ ] Each item has: score, evidence, "What we found", notes, prescription, priority
- [ ] Section summaries are complete with scores and status
- [ ] Overall summary includes: total score, maturity level, top gaps, action plan
- [ ] Items marked as "cannot assess without internal access" are clearly noted

