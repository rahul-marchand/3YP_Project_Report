# Presentation Scripts

Rahul's portion of the team's 20-minute presentation. Four sections totalling ~5:00 budget (~4:15 spoken, leaving slack for slide transitions, pauses on key numbers, and pacing variation).

Principles applied throughout: each section opens with substance (no meta-framing), lands one take-home, hands off cleanly. Statistics are kept lean so the ones that remain are remembered. The biotech examiners should follow the engineering, the business school examiners should follow the financial, and neither half should drown in the other.


## Introduction (~2:20s budget)

Around 40% of grassroots youth mild traumatic brain injuries (mTBIs) (commonly known as concussions) go unreported at the time of injury. These misses matter: second impact syndrome can be fatal, and roughly 15% of adults develop persistent post-concussive symptoms.

The reason they go unreported is a binary problem in the existing diagnosis pipeline. Screening is either accessible but subjective, like the CRT6 questionnaire a coach administers from memory, or accurate and inaccessible, like clinical pupillometers costing thousands of pounds. Nothing fills the gap between them.

So we surveyed every plausible screening modality against four requirements: they must be accessible, usable by non-experts, objective, and rapid. **Neuroimaging requires hospital grade equipment. Cognitive batteries take 25 minutes and need a baseline. Balance testing has poor sensitivity**. Only automated oculomotor screening satisfies three of the four out of the box. Accessibility is the remaining engineering gap that our project aims to solve.

We designed a headset that runs three oculomotor tests, each probing a semi-independent neural pathway. The pupillary light reflex flashes a brief light at the eye and measures the speed and amplitude of pupil constriction, probing the brainstem reflex arc. Smooth pursuit displays a target moving across the field of view and tracks how closely the eyes follow it, probing cortical attention and cerebellar circuits. Vergence brings a target slowly toward the bridge of the nose and records the nearest distance at which the eyes can still hold a single image, probing the midbrain convergence system. Diffuse axonal injury (the mechanism for mTBI) slows pupil constriction, forces catch-up saccades during smooth pursuit, and lengthens the near point of convergence. It hits these three pathways unevenly, so any single test can miss an mTBI that the others catch. That's the theoretical case for multi-modality, and a single-cohort study backs it up: in 220 high-school athletes, a logistic-regression model combining three oculomotor variables reached AUC 0.96, distinguishing concussed from control at 89% accuracy under cross-validation.


## Business Plan (~2:20 budget)

With regulatory considerations cleared and Suleiman's institution-first GTM strategy in place, the question is how this translates into revenue. 

This is fundamentally a hardware business: solving the problem from the intro requires mass-market device sales, which means making it to Phase 3. Phase 3 volumes of around ten thousand units a year give us the leverage to restructure the supply chain. The compute module migrates off the single-source Raspberry Pi onto a cheaper alternative, and we dual-source the optical components. Unit cost falls from £300 to around £150, which puts the device at the grassroots willingness-to-pay ceiling Victor identified, unlocking sustainable gross margins on the hardware.

But getting there means surviving two simultaneous cash burns: the medtech valley of death on the regulatory side, and the capital intensity of standing up a hardware supply chain. The model has to fund both without becoming so capital-hungry that we run out of runway before Phase 3.

***A less capital-intensive revenue model would be to license the technology instead, perhaps to a VR platform like Oculus. This would bridge Phase 2 cheaply, but it caps Phase 3: the overlap of rugby and VR audiences is small, and reliance on licensing fees would make it hard to build the supply chain we need at scale.***

So what is our solution? Beyond the hardware we sell, institutions need longitudinal baselines per athlete, roster management, and return-to-play tracking. That's genuine value, and it justifies a subscription that becomes our Phase 2 cash bridge. This works hand in hand with Suleiman's go-to-market strategy of targeting institutions first to build trust. The subscription is priced at £600 a year alongside £300 for the hardware.

Does this model hold up under financial analysis? Two highlights.First, the cash bridge holds: the unfunded trough bottoms at just £3.71 million in year six, against around £20 million for an average medtech raise, with EBITDA breakeven in year seven. And second, annual-in-advance institutional billing keeps working capital positive every year, reversing the usual trend for a hardware business, further reducing the capital required to build the business.

A Tornado sensitivity analysis of 7 key levers in the model further highlights how critical the subcription cash bridge is to the venctures financial success. A 5% change in subscription attach is enough to pull the business EBITDA negative in year seven. Insitutional attach directly hits both the second and third biggest levers in our model, subscription attach and adoption ramp. I'll now hand over to Eesh for rigorous scenario analysis.

(2mins 28secs)


---

## Bullet outline

### Introduction
- ~40% of grassroots youth mTBIs go unreported at the time of injury
- Misses matter: second impact syndrome can be fatal; ~15% of adults develop persistent post-concussive symptoms
- Reason for under-reporting: binary problem in screening: accessible-but-subjective (CRT6) vs accurate-but-inaccessible (clinical pupillometers, thousands of pounds)
- Surveyed every modality against four criteria: accessible, non-expert, objective, rapid
  - Neuroimaging: needs hospital-grade equipment
  - Cognitive batteries: 25 minutes + baseline required
  - Balance testing: poor sensitivity
  - Oculomotor screening: satisfies 3/4 out of the box; accessibility is the remaining engineering gap our project closes
- Built a headset running three oculomotor tests, each probing a semi-independent neural pathway:
  - **PLR**: brief light flash, measures pupil constriction speed + amplitude; probes brainstem reflex arc
  - **Smooth pursuit**: target moving across field of view, tracks how closely eyes follow; probes cortical attention + cerebellar circuits
  - **Vergence**: target moves toward bridge of nose, records nearest distance eyes can hold a single image; probes midbrain convergence system
- DAI (mechanism of mTBI) slows pupil constriction, forces catch-up saccades in smooth pursuit, lengthens near point of convergence
- Hits the three pathways unevenly → any single test can miss an mTBI the others catch (the case for multi-modality)
- Empirical anchor: Kelly 2019, n = 220 high-school athletes, combined logistic-regression model reached **AUC 0.96, 89% accuracy** under cross-validation

### Business Plan
- Bridge: regulatory cleared in Phase 1, Suleiman's strategy targets institutions first → how does each customer translate to revenue?
- Two segments consume differently:
  - **Parents**: device only, used once when something happens
  - **Institutions**: service layer on top: longitudinal baselines, roster management, return-to-play tracking
- Revenue model forced into a hybrid: single hardware price across both segments + subscription paid only by institutions
- Pricing: hardware **£300**, institutional subscription **£600/year**
- Hardware cost trajectory: **£300 (Phase 1) → ~£150 (Phase 3)**, driven by migrating off Raspberry Pi + other off-the-shelf parts
- Key point: at Phase 2, cost floor ≈ grassroots willingness-to-pay ceiling (per Victor) → Phase 3 cost-down is an engineering deliverable, not a finance question

### Financial Plan
- Bridge: that's what we sell; now the seven-year picture
- Institutional unit economics work: 3-year LTV **£4,500** vs **£437** CAC = **10.4× LTV/CAC**, past the subscription benchmark
- EBITDA breakeven: **year 7**
- Cash dynamics positive: annual-in-advance institutional billing keeps working capital positive every year, even as hardware scales
- Cash trough: **£3.75M in year 6**, structurally small for medtech (average VC round ~£20M) → model is fundable
- But sensitivity (tornado): **institutional adoption dominates by more than 2× any other lever**
- Each hardware sale is a thin-margin bet on subscription attach; if adoption fails, hardware sales convert from lead generation into pure loss
- **Verdict: the whole model rests on institutional adoption: that's what the startup verdict ultimately turns on**


---

## Slide citations

Seven-slide structure. Author surnames are first-author; years from `references.bib`.

### Intro slides

**Slide 1 — Sankey of missed concussions**
> Sources: McCrea et al. (2004); Register-Mihalik et al. (2013); Echlin et al. (2010); May et al. (StatPearls); Mortaheb et al. (2021).

**Slide 2 — Decision matrix for oculomotor screening**
> Sources: Echemendia et al. (2023); Schatz et al. (2006); Bell et al. (2011); Bazarian et al. (2018); McDonald et al. (2022).

**Slide 3 — Three biomarker tests**
> Sources: Ciuffreda et al. (2017); McDonald et al. (2022); Searle et al. (2016); Bruggeman et al. (2020); Kelly et al. (2019).

### Business slides

**Slide 4 — Hardware business and the cash trough (valley of death + capital intensity)**
> Sources: Deloitte (2022); internal BoM and supply-chain analysis (Ch. 9); internal market analysis (Ch. 6); internal financial model (Ch. 11).

**Slide 5 — Revenue model choice (licensing vs subscription)**
> Sources: Teece (1986); Nagle & Müller (2017); Hinterhuber (2008); internal revenue-model analysis (Ch. 9).

**Slide 6 — Financials (three checks)**
> Sources: Gupta et al. (2004); Deloitte (2022); internal financial model (Ch. 11).

**Slide 7 — Sensitivity tornado**
> Sources: Internal sensitivity analysis (Ch. 11); Saltelli et al. (2004).