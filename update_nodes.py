import re

with open('figures/architecture.tex', 'r') as f:
    content = f.read()

# We need to replace everything from '% ---- Row 3: Adaptive drift handling' down to the start of Connections: Row 1
start_str = "% ---- Row 3: Adaptive drift handling"
end_str = "% ---- Connections: Row 1"

start_idx = content.find(start_str)
end_idx = content.find(end_str)

new_nodes = """% ---- Row 3: Adaptive drift handling (below ensemble) ----
\\node[decision, below=1.5cm of ensemble] (adwin) {ADWIN Detects\\\\ Drift ($D_t$)?};
\\node[process, right=1.3cm of adwin] (replace) {Replace with\\\\ Background Tree};

% ---- Row 4: Precision feedback + penalty update (bottom row) ----
\\node[box, below=1.0cm of adwin] (calc_lambda) {Update Penalty\\\\ $\\lambda_t = \\min(\\Lambda_{max}, IR_t(1{+}\\gamma D_t)) \\times \\rho_t$};
\\node[box, right=1.3cm of calc_lambda] (damping) {Precision-Feedback Damping\\\\ $\\rho_t = \\max(0.1,\\ \\hat{P}_t / P_{min})$\\\\ if $\\hat{P}_t < P_{min}$, else $1.0$};
\\node[process, right=1.3cm of damping] (precision) {Rolling Precision $\\hat{P}_t$\\\\ (last 200 predictions)};

"""

content = content[:start_idx] + new_nodes + content[end_idx:]

with open('figures/architecture.tex', 'w') as f:
    f.write(content)
print("Nodes updated.")
