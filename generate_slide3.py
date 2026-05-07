"""
Generate slide 3: three biomarker tests.

Layout (matches slide 4 vocabulary):
    - Three column headers (test names) along a top axis
    - Each column shows a small signal trace: healthy (solid dark) vs
      concussed (dashed red)
    - Pathway label (what it probes)
    - mTBI effect label (red, bold)
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
\definecolor{healthy}{RGB}{40,40,40}
\definecolor{concussed}{RGB}{160,55,50}
\definecolor{accent}{RGB}{18,125,108}
\definecolor{textDark}{RGB}{40,40,40}
\definecolor{textMute}{RGB}{125,120,113}

\pagecolor{canvabg}
"""

# Column centres at x = 3.0, 9.0, 15.0 (matching slide 4)
# Plot bounding boxes per column:
#   col 1 (PLR):      x in [1.0, 5.0], y in [4.7, 7.6]
#   col 2 (SP):       x in [7.0, 11.0]
#   col 3 (Vergence): x in [13.0, 17.0]
BODY = r"""
\begin{document}
\begin{tikzpicture}[
    every node/.style={text=textDark},
]
% Canvas: x in [0, 18], y in [0, 9]

% --- Top axis with three column headers ---
\draw[gray!50, line width=0.5pt] (0.5, 8.4) -- (17.5, 8.4);
\foreach \x in {0.5, 6.0, 12.0, 17.5} {
    \draw[gray!55, line width=0.5pt] (\x, 8.4) -- (\x, 8.25);
}

\node[anchor=south, font=\bfseries\Large] at (3.0,  8.5) {Pupillary Light Reflex};
\node[anchor=south, font=\bfseries\Large] at (9.0,  8.5) {Smooth Pursuit};
\node[anchor=south, font=\bfseries\Large] at (15.0, 8.5) {Vergence};

% --- Unified legend strip (just under the header axis) ---
\draw[healthy, line width=1.4pt, line cap=round] (7.0, 8.05) -- (7.7, 8.05);
\node[anchor=west, font=\normalsize] at (7.75, 8.05) {healthy};

\draw[concussed, line width=1.4pt, line cap=round, dash pattern=on 4pt off 2pt]
    (9.4, 8.05) -- (10.1, 8.05);
\node[anchor=west, font=\normalsize, text=concussed] at (10.15, 8.05) {mTBI};

% =========================================================================
% Column 1: PLR — pupil diameter vs time, light flash marker
% =========================================================================
% Axes (light, anchored to plot bottom-left)
\draw[gray!55, line width=0.5pt, -{Stealth[length=4pt]}] (1.0, 4.85) -- (5.2, 4.85);
\draw[gray!55, line width=0.5pt, -{Stealth[length=4pt]}] (1.0, 4.85) -- (1.0, 7.55);
\node[anchor=north, font=\small, text=textMute] at (5.05, 4.83) {time};
\node[font=\small, text=textMute, rotate=90] at (0.55, 6.2) {pupil diameter};

% Light flash marker
\draw[gray!55, line width=0.4pt, dashed] (2.0, 4.85) -- (2.0, 7.4);
\node[anchor=south, font=\small\itshape, text=textMute] at (2.0, 7.4) {light flash};

% Healthy: sharp dip at flash, full constriction, recovery
\draw[healthy, line width=1.4pt, line cap=round]
    (1.0, 7.1) -- (2.0, 7.1)
    .. controls (2.05, 7.1) and (2.15, 5.4) .. (2.30, 5.3)
    .. controls (2.50, 5.3) and (3.5, 6.0) .. (5.0, 6.7);

% mTBI: shallower, slower, less constriction
\draw[concussed, line width=1.4pt, line cap=round, dash pattern=on 4pt off 2pt]
    (1.0, 7.1) -- (2.0, 7.1)
    .. controls (2.30, 7.1) and (2.7, 6.2) .. (3.00, 6.1)
    .. controls (3.40, 6.1) and (4.2, 6.4) .. (5.0, 6.7);

% =========================================================================
% Column 2: Smooth pursuit — target wave with healthy smooth follow
%            and mTBI stairstep (catch-up saccades)
% =========================================================================
% Axes
\draw[gray!55, line width=0.5pt, -{Stealth[length=4pt]}] (7.0, 4.85) -- (11.2, 4.85);
\draw[gray!55, line width=0.5pt, -{Stealth[length=4pt]}] (7.0, 4.85) -- (7.0, 7.55);
\node[anchor=north, font=\small, text=textMute] at (11.05, 4.83) {time};
\node[font=\small, text=textMute, rotate=90] at (6.55, 6.2) {eye position};

% Target reference (light gray, dotted) — a gentle sine wave
\draw[gray!50, line width=0.5pt, dotted]
    (7.0, 6.15)
    .. controls (7.4, 7.5) and (8.6, 7.5) .. (9.0, 6.15)
    .. controls (9.4, 4.8) and (10.6, 4.8) .. (11.0, 6.15);
\node[anchor=west, font=\small\itshape, text=textMute] at (10.7, 6.45) {target};

% Healthy: smooth sine, tracks target closely
\draw[healthy, line width=1.4pt, line cap=round]
    (7.0, 6.15)
    .. controls (7.4, 7.35) and (8.6, 7.35) .. (9.0, 6.15)
    .. controls (9.4, 4.95) and (10.6, 4.95) .. (11.0, 6.15);

% mTBI: sawtooth — eye trails healthy line (below on ascent, above on
% descent), with vertical saccades snapping back onto healthy.
\draw[concussed, line width=1.4pt, line cap=round, dash pattern=on 4pt off 2pt]
    (7.0, 6.15)
    % Ascent 1: drift below healthy, saccade up to it
    -- (7.4, 6.50) -- (7.4, 6.78)
    -- (7.8, 6.85) -- (7.8, 7.02)
    -- (8.0, 7.05)
    % Descent 1: drift above healthy, saccade down to it
    -- (8.4, 7.10) -- (8.4, 6.97)
    -- (8.8, 6.65) -- (8.8, 6.42)
    -- (9.0, 6.15)
    % Descent 2: continue above healthy, saccades down
    -- (9.4, 5.80) -- (9.4, 5.55)
    -- (9.8, 5.45) -- (9.8, 5.30)
    -- (10.0, 5.25)
    % Ascent 2: below healthy, saccades up
    -- (10.4, 5.30) -- (10.4, 5.43)
    -- (10.8, 5.75) -- (10.8, 5.96)
    -- (11.0, 6.15);


% =========================================================================
% Column 3: Vergence — convergence angle as the target approaches the face
% =========================================================================
% Axes
\draw[gray!55, line width=0.5pt, -{Stealth[length=4pt]}] (13.0, 4.85) -- (17.2, 4.85);
\draw[gray!55, line width=0.5pt, -{Stealth[length=4pt]}] (13.0, 4.85) -- (13.0, 7.55);
\node[anchor=north, font=\small, text=textMute, align=center, text width=4cm]
    at (15.05, 4.83) {target distance to face (decreasing)};
\node[font=\small, text=textMute, rotate=90] at (12.55, 6.2) {convergence angle};

% Healthy: rises smoothly, then drops at healthy NPC (target close to face).
\draw[healthy, line width=1.4pt, line cap=round]
    (13.0, 5.2)
    .. controls (13.8, 5.3) and (14.5, 6.7) .. (15.5, 7.1)
    .. controls (15.9, 7.18) and (16.2, 7.22) .. (16.4, 7.22)
    -- (16.55, 5.20)
    -- (17.0, 5.20);

% mTBI: tracks healthy until NPC fails earlier (target further from face),
% then drops sharply. Bezier subdivided at t=0.6 so the two paths coincide
% before the failure point.
\draw[concussed, line width=1.4pt, line cap=round, dash pattern=on 4pt off 2pt]
    (13.0, 5.2)
    .. controls (13.48, 5.26) and (13.93, 5.79) .. (14.42, 6.29)
    -- (14.55, 5.20)
    -- (17.0, 5.20);

% NPC failure annotations
\draw[concussed!90!black, line width=0.5pt, dotted] (14.42, 6.35) -- (14.42, 7.40);
\node[anchor=south, font=\small\itshape, text=concussed!90!black]
    at (14.42, 7.40) {mTBI NPC};

\draw[healthy, line width=0.5pt, dotted] (16.40, 7.28) -- (16.40, 7.55);
\node[anchor=south, font=\small\itshape, text=healthy]
    at (16.40, 7.55) {healthy NPC};

% =========================================================================
% Pathway labels (italic, muted) — what each test probes
% =========================================================================
\node[font=\large\itshape, text=textMute, align=center, text width=4.5cm]
    at (3.0,  3.2) {brainstem reflex arc};
\node[font=\large\itshape, text=textMute, align=center, text width=4.5cm]
    at (9.0,  3.2) {cortical attention\\+ cerebellar circuits};
\node[font=\large\itshape, text=textMute, align=center, text width=4.5cm]
    at (15.0, 3.2) {midbrain convergence};

% =========================================================================
% mTBI effect labels (bold, red) — how concussion alters each
% =========================================================================
\draw[gray!45, line width=0.5pt] (1.5, 1.85) -- (4.5, 1.85);
\draw[gray!45, line width=0.5pt] (7.0, 1.85) -- (11.0, 1.85);
\draw[gray!45, line width=0.5pt] (13.0, 1.85) -- (17.0, 1.85);

\node[font=\bfseries\large, text=textDark] at (3.0, 2.20) {mTBI effect};
\node[font=\bfseries\large, text=textDark] at (9.0, 2.20) {mTBI effect};
\node[font=\bfseries\large, text=textDark] at (15.0, 2.20) {mTBI effect};

\node[font=\bfseries\Large, text=concussed] at (3.0,  1.10) {slowed constriction};
\node[font=\bfseries\Large, text=concussed] at (9.0,  1.10) {catch-up saccades};
\node[font=\bfseries\Large, text=concussed] at (15.0, 1.10) {longer near point};

\end{tikzpicture}
\end{document}
"""


def write_and_compile(name, body):
    src = os.path.join(OUT_DIR, f"{name}.tex")
    with open(src, "w") as f:
        f.write(PREAMBLE + body)
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
    write_and_compile("slide3_three_tests", BODY)
    print("Done.")
