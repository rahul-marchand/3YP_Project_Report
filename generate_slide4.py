"""
Generate slide 4: cash bridge schematic, two states.

State 1 — phase timeline + cash valley + hardware unit-cost trajectory.
          Asks: what funds P2?
State 2 — adds the subscription bridge across P2 with dashed extensions.

Hardware unit cost ranges sourced from chap_9_business.tex Table 9.x
(BoM + manufacturing total).
"""

import os
import subprocess

OUT_DIR = "/home/rahul/thesis_template/figures/slides"
os.makedirs(OUT_DIR, exist_ok=True)

PREAMBLE = r"""\documentclass[border=10pt]{standalone}
\usepackage{fontspec}
\setmainfont{Carlito}
\usepackage{unicode-math}
\setmathfont{Latin Modern Math}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{positioning, arrows.meta, calc}

\definecolor{canvabg}{RGB}{246,244,241}
\definecolor{trough}{RGB}{160,55,50}
\definecolor{bridge}{RGB}{30,90,140}
\definecolor{accent}{RGB}{18,125,108}
\definecolor{textDark}{RGB}{40,40,40}
\definecolor{textMute}{RGB}{125,120,113}

\pagecolor{canvabg}
"""

# Phase boundaries: P1 = [0.5, 5.5], P2 = [5.5, 12.5], P3 = [12.5, 17.5]
# (widths 5.0 / 7.0 / 5.0 ~ 2:3:2 year ratio)
# Label centres: 3.0, 9.0, 15.0
BASE = r"""
\begin{document}
\begin{tikzpicture}[
    every node/.style={text=textDark},
]
% Canvas: x in [0, 18], y in [0, 9]

% --- Phase axis (top): labels + light tick marks ---
\draw[gray!50, line width=0.5pt] (0.5, 8.0) -- (17.5, 8.0);
\foreach \x in {0.5, 5.5, 12.5, 17.5} {
    \draw[gray!55, line width=0.5pt] (\x, 8.0) -- (\x, 7.85);
}

\node[anchor=south, font=\bfseries\Large] at (3.0,  8.10) {Phase 1};
\node[anchor=south, font=\bfseries\Large] at (9.0,  8.10) {Phase 2};
\node[anchor=south, font=\bfseries\Large] at (15.0, 8.10) {Phase 3};

% --- Cash-neutral label (line drawn per-state) ---
\node[anchor=south west, font=\normalsize, text=textMute]
    at (0.5, 6.45) {cash neutral};

% --- Cash valley curve ---
\draw[trough, line width=1.6pt, line cap=round]
    (0.6, 6.4)
    .. controls (3.2, 6.4) and (4.8, 6.0) .. (5.8, 5.0)
    .. controls (7.4, 3.5) and (9.6, 2.7) .. (11.0, 3.0)
    .. controls (13.0, 3.7) and (14.6, 4.7) .. (15.7, 5.7)
    .. controls (16.6, 6.3) and (17.0, 6.4) .. (17.4, 6.4);

% --- Hardware unit cost row, treated as a section ---
% Header + thin underline anchor the row so the label doesn't float.
\node[font=\bfseries\Large, text=textDark] at (9.0, 2.30) {Hardware unit cost};
\draw[gray!45, line width=0.5pt] (6.5, 1.95) -- (11.5, 1.95);

\node[font=\bfseries\LARGE, text=textDark]        at (3.0,  1.20) {\pounds 305--380};
\node[font=\bfseries\LARGE, text=textDark]        at (9.0,  1.20) {\pounds 252--318};
\node[font=\bfseries\LARGE, text=accent!85!black] at (15.0, 1.20) {\pounds 138--209};
"""

CAPTION_STATE1 = r"""
% Cash-neutral baseline (state 1 only)
\draw[gray!45, line width=0.45pt, dashed] (0.5, 6.4) -- (17.5, 6.4);
"""

BRIDGE_STATE2 = r"""
% --- Subscription bridge ---
% Dashed extensions in P1 and P3 anchor the bridge visually
\draw[bridge, line width=1.0pt, dashed, dash pattern=on 4pt off 3pt, opacity=0.55]
    (0.5, 6.4) -- (5.5, 6.4);
\draw[bridge, line width=1.0pt, dashed, dash pattern=on 4pt off 3pt, opacity=0.55]
    (12.5, 6.4) -- (17.5, 6.4);

% Solid bridge across P2
\draw[bridge, line width=2.4pt, line cap=round] (5.5, 6.4) -- (12.5, 6.4);

% Subscription label
\node[font=\bfseries\Large, text=bridge]
    at (9.0, 6.85) {\pounds 600 / yr institutional subscription};
"""

END = r"""
\end{tikzpicture}
\end{document}
"""


def write_and_compile(name, body):
    src = os.path.join(OUT_DIR, f"{name}.tex")
    with open(src, "w") as f:
        f.write(PREAMBLE + body + END)
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
        ["pdftoppm", "-r", "300", "-png", "-singlefile", pdf, os.path.join(OUT_DIR, name)],
        check=True,
    )
    print(f"  PNG: {os.path.join(OUT_DIR, name)}.png")
    return pdf


if __name__ == "__main__":
    write_and_compile("slide4_cash_bridge_state1", BASE + CAPTION_STATE1)
    write_and_compile("slide4_cash_bridge_state2", BASE + BRIDGE_STATE2)
    print("Done.")
