"""
Generate Q&A appendix slides for the presentation.

All new slides use a fixed 24x13.5cm canvas (16:9 aspect) with explicit
\\useasboundingbox so the rendered PNG comes out at consistent slide dimensions.
"""

import os
import shutil
import subprocess

ROOT    = "/home/rahul/thesis_template"
OUT_DIR = f"{ROOT}/figures/slides"
FIN_DIR = f"{ROOT}/figures/financial"
HOUSING = f"{ROOT}/figures/housing"
os.makedirs(OUT_DIR, exist_ok=True)

PREAMBLE = r"""\documentclass[border=0pt]{standalone}
\usepackage{fontspec}
\setmainfont{Carlito}
\usepackage{unicode-math}
\setmathfont{Latin Modern Math}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{tikz}
\usepackage{graphicx}

\definecolor{canvabg}{RGB}{246,244,241}
\definecolor{textDark}{RGB}{40,40,40}
\definecolor{textMute}{RGB}{125,120,113}
\definecolor{accent}{RGB}{18,125,108}
\definecolor{trough}{RGB}{160,55,50}
\definecolor{bridge}{RGB}{30,90,140}

\pagecolor{canvabg}

\providecommand{\Cref}[1]{}
\providecommand{\cref}[1]{}
\providecommand{\ab}[1]{#1}
"""

# Standard 16:9 canvas. Keep a margin inside.
# x: 0 to 24, y: 0 to 13.5
CANVAS_BB = r"\useasboundingbox (0,0) rectangle (24, 13.5);"


def write_tex(name, body):
    path = os.path.join(OUT_DIR, f"{name}.tex")
    with open(path, "w") as f:
        f.write(PREAMBLE + body)
    return path


def compile_tex(path):
    name = os.path.basename(path).replace(".tex", "")
    res = subprocess.run(
        ["lualatex", "-interaction=nonstopmode", "-output-directory", OUT_DIR, f"{name}.tex"],
        cwd=OUT_DIR, capture_output=True, text=True,
    )
    pdf = os.path.join(OUT_DIR, f"{name}.pdf")
    if not os.path.exists(pdf):
        print(f"FAILED: {name}")
        print("\n".join(res.stdout.splitlines()[-30:]))
        return None
    subprocess.run(
        ["pdftoppm", "-r", "200", "-png", "-singlefile", pdf, os.path.join(OUT_DIR, name)],
        check=True,
    )
    print(f"  PNG: {os.path.join(OUT_DIR, name)}.png")
    return pdf


def pdf_to_png(src_pdf, out_name):
    out_pdf = os.path.join(OUT_DIR, f"{out_name}.pdf")
    shutil.copyfile(src_pdf, out_pdf)
    subprocess.run(
        ["pdftoppm", "-r", "200", "-png", "-singlefile",
         out_pdf, os.path.join(OUT_DIR, out_name)],
        check=True,
    )
    print(f"  PNG: {os.path.join(OUT_DIR, out_name)}.png  (from {os.path.basename(src_pdf)})")


# =============================================================================
# A1 — Kelly 2019 study card
# =============================================================================
KELLY_BODY = rf"""
\begin{{document}}
\begin{{tikzpicture}}[every node/.style={{text=textDark}}]
{CANVAS_BB}

% Header
\node[anchor=north west, font=\bfseries\LARGE] at (1.0, 12.5)
    {{Kelly et al.\ (2019) — combined oculomotor screening}};
\node[anchor=north west, font=\itshape\large, text=textMute, text width=22cm]
    at (1.0, 11.6)
    {{\textit{{J Head Trauma Rehabil}} 34(3):176--188 \textperiodcentered{{}} PMID 30234848}};

\draw[gray!50, line width=0.5pt] (1.0, 11.0) -- (23.0, 11.0);

% Three-column body
\node[anchor=north west, font=\bfseries\Large] at (1.0, 10.4) {{Design}};
\node[anchor=north west, text width=6.5cm, font=\large] at (1.0, 9.6)
    {{220 high-school athletes (concussed and healthy controls).
     Cross-sectional, video-oculography in clinic.}};

\node[anchor=north west, font=\bfseries\Large] at (8.7, 10.4) {{Method}};
\node[anchor=north west, text width=6.5cm, font=\large] at (8.7, 9.6)
    {{Logistic regression on three oculomotor variables across PLR,
     smooth pursuit and vergence. Cross-validated.}};

\node[anchor=north west, font=\bfseries\Large] at (16.4, 10.4) {{Result}};
\node[anchor=north west, text width=6.5cm, font=\large] at (16.4, 9.6)
    {{\textbf{{AUC 0.96}} \textperiodcentered{{}} \textbf{{89\% accuracy}}
     distinguishing concussed from control under cross-validation.}};

% Why we cite
\draw[gray!45, line width=0.5pt] (1.0, 6.6) -- (23.0, 6.6);
\node[anchor=north west, font=\bfseries\Large] at (1.0, 6.0) {{Why we cite it}};
\node[anchor=north west, text width=22cm, font=\large] at (1.0, 5.2)
    {{Single-cohort apples-to-apples comparison of single-test vs combined-test
     classifiers — establishes the multi-modal performance ceiling on the
     same population, controlling for cohort and methodology variance that
     confounds across-study comparisons. The number anchoring our
     three-test architecture is its 0.96 AUC, not single-test AUCs reported
     elsewhere.}};

% Caveats
\node[anchor=north west, font=\bfseries, text=textMute] at (1.0, 1.7) {{Caveats}};
\node[anchor=north west, text width=22cm, font=\normalsize, text=textMute]
    at (1.0, 1.2)
    {{Single-site cohort \textperiodcentered{{}} in-clinic video-oculography (not
     pitch-side) \textperiodcentered{{}} subject-level CV is the appropriate
     generalisation estimate but external replication remains future work.}};

\end{{tikzpicture}}
\end{{document}}
"""


# =============================================================================
# A2 — Hardware CAD: specs at top in two columns, figure below in a white box
# =============================================================================
CAD_BODY = rf"""
\begin{{document}}
\begin{{tikzpicture}}[every node/.style={{text=textDark}}]
{CANVAS_BB}

\node[anchor=north west, font=\bfseries\LARGE] at (1.0, 12.7)
    {{Headset hardware: housing geometry}};
\draw[gray!50, line width=0.5pt] (1.0, 12.1) -- (23.0, 12.1);

% Key specs in two columns
\renewcommand{{\arraystretch}}{{1.3}}
\node[anchor=north west, font=\large] at (1.5, 11.6) {{%
\begin{{tabular}}{{ll}}
    Centre of mass & 22.4\,mm forward of face plane \\
    Compute        & Raspberry Pi 5 (Phase 1--2) \\
    Cameras        & Dual Arducam OV9281 global shutter \\
    Optics         & Longpass dichroic plate beamsplitter \\
\end{{tabular}}}};

\node[anchor=north west, font=\large] at (13.5, 11.6) {{%
\begin{{tabular}}{{ll}}
    Illumination  & 850\,nm NIR, decoupled from stimulus \\
    BoM at launch & \textasciitilde \pounds 250 (Phase 1--2) \\
    BoM at scale  & \textasciitilde \pounds 150 (Phase 3) \\
\end{{tabular}}}};

% White box behind the figure (top below the specs row)
\fill[white, rounded corners=4pt] (3.0, 0.3) rectangle (21.0, 8.0);

% Combined housing figure inside the box
\node[anchor=center] at (12.0, 4.15)
    {{\includegraphics[width=16cm,height=7.0cm,keepaspectratio]{{{ROOT}/figures/housing_figure.pdf}}}};

\end{{tikzpicture}}
\end{{document}}
"""


# =============================================================================
# A4 — Financial model assumptions
# =============================================================================
ASSUMPTIONS_BODY = rf"""
\renewcommand{{\arraystretch}}{{1.25}}

\begin{{document}}
\begin{{tikzpicture}}[every node/.style={{text=textDark}}]
{CANVAS_BB}

\node[anchor=north west, font=\bfseries\LARGE] at (1.0, 12.5)
    {{Financial model — year-by-year operational drivers}};
\node[anchor=north west, font=\itshape\large, text=textMute, text width=22cm]
    at (1.0, 11.6)
    {{Drivers grouped by P\&L block. Rows marked \emph{{derived}} are computed
     from the others and retained as audit anchors.}};

\draw[gray!50, line width=0.5pt] (1.0, 11.0) -- (23.0, 11.0);

\node[anchor=north west, font=\normalsize] at (1.0, 10.5) {{%
\begin{{tabular}}{{lllrrrrrrr}}
    \toprule
     & \textbf{{Driver}} & \textbf{{Source}} & \textbf{{Y1}} & \textbf{{Y2}} & \textbf{{Y3}} & \textbf{{Y4}} & \textbf{{Y5}} & \textbf{{Y6}} & \textbf{{Y7}} \\
    \midrule
    \textit{{Rev.}} & Institutional buyers (schools + clubs) & GTM & 0 & 0 & 30 & 90 & 150 & 400 & 750 \\
     & DTC buyers (direct-to-consumer) & GTM & 0 & 0 & 0 & 0 & 1{{,}}041 & 1{{,}}954 & 5{{,}}325 \\
     & Total headsets sold (\emph{{derived}}) &  & 0 & 0 & 90 & 270 & 1{{,}}491 & 3{{,}}154 & 7{{,}}575 \\
     & Hardware ASP (\pounds) & Pricing & 300 & 300 & 300 & 300 & 300 & 300 & 300 \\
     & Subscription price (\pounds/headset/yr) & Pricing & 600 & 600 & 600 & 600 & 600 & 600 & 600 \\
     & Annual churn (\%) & Unit econ & 10\% & 10\% & 10\% & 10\% & 10\% & 10\% & 10\% \\
     & Active headset subs (\emph{{derived}}) &  & 0 & 0 & 90 & 351 & 766 & 1{{,}}889 & 3{{,}}950 \\
    \textit{{COGS}} & Effective unit cost (\pounds) & Cost stack & 340 & 340 & 285 & 285 & 174 & 174 & 174 \\
    \textit{{OpEx}} & Total FTE & Headcount & 4.0 & 5.0 & 8.0 & 12.0 & 15.0 & 16.5 & 18.0 \\
     & Loaded payroll (\pounds k, \emph{{derived}}) & 1.19 \texttimes{{}} base & 220 & 283 & 503 & 737 & 917 & 1{{,}}002 & 1{{,}}086 \\
     & R\&D non-payroll (\pounds k) & dev tools, CAD & 15 & 20 & 25 & 30 & 30 & 30 & 30 \\
     & Regulatory \& clinical direct (\pounds k) & MDR pathway & 0 & 130 & 140 & 55 & 55 & 60 & 65 \\
     & Marketing — institutional (\pounds k) & GTM & 5 & 10 & 25 & 50 & 50 & 75 & 100 \\
     & Marketing — DTC (\pounds k) & GTM & 0 & 0 & 0 & 0 & 100 & 225 & 400 \\
     & G\&A non-payroll (\pounds k) & ops & 30 & 69 & 119 & 178 & 241 & 304 & 365 \\
    \textit{{Capex}} & Capex (\pounds k) & Mfg roadmap & 6.5 & 6.0 & 15.0 & 20.0 & 30.0 & 12.0 & 22.0 \\
    \bottomrule
\end{{tabular}}
}};

\end{{tikzpicture}}
\end{{document}}
"""


# =============================================================================
# A5 — Unit economics
# =============================================================================
UNIT_ECON_BODY = rf"""
\renewcommand{{\arraystretch}}{{1.45}}

\begin{{document}}
\begin{{tikzpicture}}[every node/.style={{text=textDark}}]
{CANVAS_BB}

\node[anchor=north west, font=\bfseries\LARGE] at (1.0, 12.5)
    {{Unit economics: institutional vs DTC, Phase 3 steady state}};
\node[anchor=north west, font=\itshape\large, text=textMute, text width=22cm]
    at (1.0, 11.6)
    {{Per-customer build from hardware and subscription contributions.
     Institutional LTV reflects three headsets per customer.}};

\draw[gray!50, line width=0.5pt] (1.0, 11.0) -- (23.0, 11.0);

% Table
\node[anchor=north, font=\large] at (12.0, 10.5) {{%
\begin{{tabular}}{{lrr}}
    \toprule
    \textbf{{Per-headset metric}} & \multicolumn{{2}}{{r}}{{\textbf{{Value}}}} \\
    \midrule
    Hardware contribution per headset        & \multicolumn{{2}}{{r}}{{\pounds 126}} \\
    Subscription contribution per headset/yr & \multicolumn{{2}}{{r}}{{\pounds 510}} \\
    \midrule
    \textbf{{Per-channel metric}} & \textbf{{Institutional}} & \textbf{{DTC}} \\
    \midrule
    3-year LTV per customer                  & \pounds 4{{,}}524 & \pounds 126 \\
    CAC per new customer                     & \pounds 403       & \pounds 75  \\
    LTV : CAC ratio                          & 11.2$\times$      & 1.7$\times$ \\
    Payback period (months)                  & 3.2               & instant\textsuperscript{{*}} \\
    \bottomrule
\end{{tabular}}
}};

\node[anchor=north west, text width=22cm, font=\large] at (1.0, 3.5)
    {{\textbf{{Reading the table.}} Institutional channel funds the company;
     DTC just clears acquisition cost. The 11.2$\times$ LTV/CAC sits
     comfortably above the 3$\times$ benchmark for subscription businesses
     (Gupta et al.\ 2004). Hardware is sold at thin/negative Phase-2 margin
     as a deliberate acquisition strategy: each unit is a bet on subscription
     attach, justified only if institutional LTV materialises.}};

\node[anchor=north west, font=\small, text=textMute, text width=22cm] at (1.0, 0.7)
    {{\textsuperscript{{*}}DTC payback at point of sale: contribution
     exceeds CAC, no time-discounting required.}};

\end{{tikzpicture}}
\end{{document}}
"""


# =============================================================================
# A11 — Scalar / structural assumptions (modelling conventions)
# =============================================================================
CONVENTIONS_BODY = rf"""
\renewcommand{{\arraystretch}}{{1.3}}

\begin{{document}}
\begin{{tikzpicture}}[every node/.style={{text=textDark}}]
{CANVAS_BB}

\node[anchor=north west, font=\bfseries\LARGE] at (1.0, 12.5)
    {{Financial model — scalar assumptions}};
\node[anchor=north west, font=\itshape\large, text=textMute, text width=22cm]
    at (1.0, 11.6)
    {{Modelling conventions and structural assumptions, grouped by function.
     Year-varying drivers are tabulated separately (see A4).}};

\draw[gray!50, line width=0.5pt] (1.0, 11.0) -- (23.0, 11.0);

\node[anchor=north west, font=\normalsize] at (1.0, 10.5) {{%
\begin{{tabular}}{{lllp{{6cm}}}}
    \toprule
     & \textbf{{Assumption}} & \textbf{{Value}} & \textbf{{Source / note}} \\
    \midrule
    \textit{{Revenue / COGS}} & Returns allowance              & 2\% of gross hardware revenue   & DOA + trial returns \\
                              & Subscription COGS              & 15\% of subscription revenue    & cloud, support, data egress \\
                              & Extended-warranty gross margin & 45\%                            & ops warranty \\
                              & Sales commission               & 15\% of new ARR from Y4         & ops org \\
                              & Subscription billing           & Annually in advance             & drives deferred revenue \\
    \textit{{Payroll}}        & Founder partial cash           & \pounds 30{{,}}000 reduction Y1--Y2 & vs full salary; pre-Series A only \\
    \textit{{Working capital}} & DIO / DSO / DPO                & 75 / 45 / 45 days               & medtech default \\
    \textit{{Tax}}            & UK corporation tax             & 25\% main rate                  & full loss carry-forward \\
                              & SME R\&D tax credit            & 18.6\% effective rate           & post-April 2024 SME scheme \\
                              & R\&D qualifying split          & 60 / 40 / 30 / 50 / 100\%       & eng / reg / clin / trial / non-payroll \\
    \textit{{Accounting}}     & Depreciation                   & SL; 3y IT/bench, 5y tooling     & ops facilities \\
                              & Interest on cash               & 3\% p.a.\ on opening cash       & business savings rate \\
                              & Inflation                      & nil; constant 2026 GBP          & modelling convention \\
                              & Foreign exchange               & frozen 2026 rates               & modelling convention \\
    \bottomrule
\end{{tabular}}
}};

\end{{tikzpicture}}
\end{{document}}
"""

# =============================================================================
# A8 — BoM and total unit cost stack
# =============================================================================
BOM_BODY = rf"""
\renewcommand{{\arraystretch}}{{1.2}}

\begin{{document}}
\begin{{tikzpicture}}[every node/.style={{text=textDark}}]
{CANVAS_BB}

\node[anchor=north west, font=\bfseries\LARGE] at (1.0, 12.5)
    {{Bill of materials and total unit cost, by phase}};
\node[anchor=north west, font=\itshape\large, text=textMute, text width=22cm]
    at (1.0, 11.6)
    {{Component prices from supplier listings (Mouser, DigiKey, Arducam, Waveshare,
     JLCPCB), April 2026, with standard quantity breaks per tier.}};

\draw[gray!50, line width=0.5pt] (1.0, 11.0) -- (23.0, 11.0);

% BoM table on left
\node[anchor=north west, font=\bfseries\large] at (1.0, 10.5) {{BoM by volume tier (\pounds)}};
\node[anchor=north west, font=\footnotesize] at (1.0, 9.95) {{%
\begin{{tabular}}{{lrrr}}
    \toprule
    \textbf{{Component}} & \textbf{{P1 ($\sim$10)}} & \textbf{{P2 ($\sim$500)}} & \textbf{{P3 ($\sim$10k)}} \\
    \midrule
    Compute module           & 83        & 83      & 35--55    \\
    Cameras (dual OV9281)    & 66--86    & 52--64  & 36--48    \\
    Internal display         & 33--35    & 24--28  & 15--20    \\
    NIR LEDs + drivers       & 22--28    & 12--16  & 7--10     \\
    Battery (2S LiPo)        & 10--13    & 5--7    & 3--5      \\
    Power management ICs     & 12--16    & 8--11   & 5--7      \\
    IMU                      & 3         & 2       & 1.5       \\
    Connectors, passives     & 11        & 6--7    & 3.5--4.5  \\
    Beamsplitter             & 8--12     & 4--7    & 2--4      \\
    Lenses, IR-pass filters  & 6--10     & 3--5    & 1.5--2.5  \\
    Enclosure (FDM/SLS/IM)   & 3--5      & 15--25  & 2--5      \\
    Strap, facial interface  & 8--13     & 5--8    & 2--3.5    \\
    Gaskets                  & 0.5       & 0.3     & 0.2       \\
    \midrule
    \textbf{{Total BoM}}     & \textbf{{266--316}} & \textbf{{219--264}} & \textbf{{114--166}} \\
    \bottomrule
\end{{tabular}}
}};

% Total unit cost stack on right
\node[anchor=north west, font=\bfseries\large] at (13.5, 10.5) {{Total unit cost stack (\pounds)}};
\node[anchor=north west, font=\footnotesize] at (13.5, 9.95) {{%
\begin{{tabular}}{{lrrr}}
    \toprule
    \textbf{{Cost element}} & \textbf{{P1}} & \textbf{{P2}} & \textbf{{P3}} \\
    \midrule
    Bill of materials              & 266--316 & 219--264 & 114--166 \\
    \midrule
    PCB fabrication (4-layer)      & 3--5     & 2--3     & 0.5--1   \\
    PCB assembly (SMT)             & 15--25   & 5--8     & 2--4     \\
    Assembly labour                & 14--22   & 14--22   & 7--11    \\
    Calibration, end-of-line test  & 7--12    & 7--12    & 3--6     \\
    Packaging, fulfilment          & ---      & 5--9     & 3--6     \\
    CM overhead                    & ---      & ---      & 8--15    \\
    \midrule
    \textbf{{Total unit cost}}     & \textbf{{305--380}} & \textbf{{252--318}} & \textbf{{138--209}} \\
    \bottomrule
\end{{tabular}}
}};

% Reading note
\node[anchor=north west, text width=22cm, font=\large] at (1.0, 2.5)
    {{\textbf{{Cost concentration.}} Three items (compute, dual cameras,
     display) account for $\sim$2/3 of BoM at every tier. The Raspberry Pi
     CM5 alone is $\sim$30\% in P1--P2; the P3 RK3588S migration cuts
     compute by half and shifts dominant cost to the cameras.}};

\end{{tikzpicture}}
\end{{document}}
"""

# =============================================================================
# A7 — Scenarios
# =============================================================================
SCENARIOS_BODY = rf"""
\renewcommand{{\arraystretch}}{{1.45}}

\begin{{document}}
\begin{{tikzpicture}}[every node/.style={{text=textDark}}]
{CANVAS_BB}

\node[anchor=north west, font=\bfseries\LARGE] at (1.0, 12.5)
    {{Scenario analysis: base vs downside vs upside vs reg delay}};
\node[anchor=north west, font=\itshape\large, text=textMute, text width=22cm]
    at (1.0, 11.6)
    {{Downside compounds all headwinds (slower adoption, higher BoM, churn,
     payroll, marketing, reg cost). Upside reverses each lever. Reg Delay is
     a single-issue stress: UKCA slip by one year shifts the entire ramp right.}};

\draw[gray!50, line width=0.5pt] (1.0, 10.6) -- (23.0, 10.6);

\node[anchor=north, font=\large] at (12.0, 10.0) {{%
\begin{{tabular}}{{lrrrr}}
    \toprule
    \textbf{{Metric}} & \textbf{{Base}} & \textbf{{Downside}} & \textbf{{Upside}} & \textbf{{Reg Delay}} \\
    \midrule
    Y7 total revenue                  & \pounds 3{{,}}979k    & \pounds 1{{,}}960k    & \pounds 5{{,}}221k    & \pounds 1{{,}}761k \\
    Y7 gross profit                   & \pounds 2{{,}}398k    & \pounds 976k          & \pounds 3{{,}}416k    & \pounds 1{{,}}087k \\
    Y7 EBITDA                         & \pounds 149k          & (\pounds 1{{,}}413k)  & \pounds 1{{,}}273k    & (\pounds 1{{,}}147k) \\
    Y7 net income                     & \pounds 224k          & (\pounds 1{{,}}381k)  & \pounds 1{{,}}377k    & (\pounds 1{{,}}106k) \\
    Y7 closing cash                   & \pounds 869k          & (\pounds 2{{,}}468k)  & \pounds 3{{,}}155k    & (\pounds 1{{,}}719k) \\
    Peak unfunded cash trough         & (\pounds 3{{,}}709k)  & (\pounds 6{{,}}668k)  & (\pounds 2{{,}}656k)  & (\pounds 5{{,}}919k) \\
    First year of positive op.\ cash  & Y7                    & ---                   & Y6                    & --- \\
    \bottomrule
\end{{tabular}}
}};

\node[anchor=north west, text width=22cm, font=\large] at (1.0, 3.0)
    {{\textbf{{Reading the table.}} Base case: Y7 EBITDA just above zero,
     \pounds 3.71M trough, fundable. Downside roughly doubles the trough
     (\pounds 6.7M) and pushes EBITDA \pounds 1.4M into the red. Reg Delay
     alone moves the trough to \pounds 5.9M, showing how single-issue
     regulatory timing risk dominates the asymmetry.}};

\end{{tikzpicture}}
\end{{document}}
"""


# =============================================================================
# A12 — Full P&L line-item table
# =============================================================================
PNL_TABLE_BODY = rf"""
\renewcommand{{\arraystretch}}{{1.35}}

\begin{{document}}
\begin{{tikzpicture}}[every node/.style={{text=textDark}}]
{CANVAS_BB}

\node[anchor=north west, font=\bfseries\LARGE] at (1.0, 12.5)
    {{P\&L: 7-year base-case projection}};
\node[anchor=north west, font=\itshape\large, text=textMute, text width=22cm]
    at (1.0, 11.6)
    {{All figures in \pounds{{}}\,thousand. Positive numbers are revenues or
     profits; parenthesised numbers are costs or losses.}};

\draw[gray!50, line width=0.5pt] (1.0, 11.0) -- (23.0, 11.0);

\node[anchor=north, font=\normalsize] at (12.0, 10.5) {{%
\begin{{tabular}}{{lrrrrrrr}}
    \toprule
    \textbf{{Line item (\pounds k)}} & \textbf{{Y1}} & \textbf{{Y2}} & \textbf{{Y3}} & \textbf{{Y4}} & \textbf{{Y5}} & \textbf{{Y6}} & \textbf{{Y7}} \\
    \midrule
    Hardware revenue                     & 0     & 0      & 26    & 79     & 438    & 927     & 2{{,}}227 \\
    Subscription revenue                 & 0     & 0      & 27    & 132    & 335    & 797     & 1{{,}}752 \\
    \textbf{{Total revenue}}             & \textbf{{0}}     & \textbf{{0}}     & \textbf{{53}}    & \textbf{{212}}   & \textbf{{773}}   & \textbf{{1{{,}}724}} & \textbf{{3{{,}}979}} \\
    \midrule
    Total COGS                           & 0     & 0      & (30)  & (97)   & (310)  & (668)   & (1{{,}}581) \\
    \textbf{{Gross profit}}              & \textbf{{0}}     & \textbf{{0}}     & \textbf{{24}}    & \textbf{{115}}   & \textbf{{464}}   & \textbf{{1{{,}}056}} & \textbf{{2{{,}}398}} \\
    \midrule
    Operating expenses                   & (270) & (512)  & (820) & (1{{,}}075) & (1{{,}}434) & (1{{,}}804) & (2{{,}}249) \\
    \textbf{{EBITDA}}                    & \textbf{{(270)}} & \textbf{{(512)}} & \textbf{{(797)}} & \textbf{{(960)}} & \textbf{{(970)}} & \textbf{{(748)}} & \textbf{{149}} \\
    \midrule
    Depreciation \& amortisation         & (1)   & (2)    & (6)   & (10)   & (16)   & (17)    & (19) \\
    \textbf{{EBIT (operating P/L)}}      & \textbf{{(271)}} & \textbf{{(514)}} & \textbf{{(802)}} & \textbf{{(969)}} & \textbf{{(986)}} & \textbf{{(765)}} & \textbf{{131}} \\
    \midrule
    + Interest income on cash            & 0     & 23     & 10    & 40     & 14     & 31      & 15 \\
    Net tax / (R\&D credit)              & 22    & 39     & 55    & 53     & 64     & 71      & 78 \\
    \textbf{{Net income}}                & \textbf{{(250)}} & \textbf{{(453)}} & \textbf{{(737)}} & \textbf{{(876)}} & \textbf{{(908)}} & \textbf{{(663)}} & \textbf{{224}} \\
    \bottomrule
\end{{tabular}}
}};

\end{{tikzpicture}}
\end{{document}}
"""


if __name__ == "__main__":
    print("Building appendix slides...")

    print("\n[A1] Kelly 2019 study card")
    compile_tex(write_tex("slide_appendix_a1_kelly", KELLY_BODY))

    print("\n[A2] Hardware CAD overview")
    compile_tex(write_tex("slide_appendix_a2_cad", CAD_BODY))

    print("\n[A4] Financial model assumptions")
    compile_tex(write_tex("slide_appendix_a4_assumptions", ASSUMPTIONS_BODY))

    print("\n[A5] Unit economics")
    compile_tex(write_tex("slide_appendix_a5_unit_econ", UNIT_ECON_BODY))

    print("\n[A7] Scenarios")
    compile_tex(write_tex("slide_appendix_a7_scenarios", SCENARIOS_BODY))

    print("\n[A3] PLR pipeline (reusing existing canva figure)")
    pdf_to_png(f"{ROOT}/figures/pipeline_figure_canva.pdf",
               "slide_appendix_a3_plr_pipeline")

    print("\n[A6] Sensitivity tornado (reusing existing canva figure)")
    pdf_to_png(f"{FIN_DIR}/fig_sensitivity_overview_canva.pdf",
               "slide_appendix_a6_tornado")

    print("\n[A8] BoM + total unit cost")
    compile_tex(write_tex("slide_appendix_a8_bom", BOM_BODY))

    print("\n[A9] P&L 4-panel (reusing existing canva figure)")
    pdf_to_png(f"{FIN_DIR}/fig_pnl_overview_canva.pdf",
               "slide_appendix_a9_pnl")

    print("\n[A10] Cash + working capital (reusing existing canva figure)")
    pdf_to_png(f"{FIN_DIR}/fig_cash_overview_canva.pdf",
               "slide_appendix_a10_cash")

    print("\n[A11] Scalar / structural assumptions")
    compile_tex(write_tex("slide_appendix_a11_conventions", CONVENTIONS_BODY))

    print("\n[A12] Full P&L line-item table")
    compile_tex(write_tex("slide_appendix_a12_pnl_table", PNL_TABLE_BODY))

    print("\nDone.")
