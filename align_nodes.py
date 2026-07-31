with open('figures/architecture.tex', 'r') as f:
    content = f.read()

old_nodes = """% ---- Row 3: Adaptive drift handling (below ensemble) ----
\\node[decision, below=1.5cm of ensemble] (adwin) {ADWIN Detects\\\\ Drift ($D_t$)?};
\\node[process, right=1.3cm of adwin] (replace) {Replace with\\\\ Background Tree};

% ---- Row 4: Precision feedback + penalty update (bottom row) ----
\\node[box, below=2.8cm of adwin] (calc_lambda) {Update Penalty\\\\ $\\lambda_t = \\min(\\Lambda_{max}, IR_t(1{+}\\gamma D_t)) \\times \\rho_t$};
\\node[box, right=1.3cm of calc_lambda] (damping) {Precision-Feedback Damping\\\\ $\\rho_t = \\max(0.1,\\ \\hat{P}_t / P_{min})$\\\\ if $\\hat{P}_t < P_{min}$, else $1.0$};
\\node[process, right=1.3cm of damping] (precision) {Rolling Precision $\\hat{P}_t$\\\\ (last 200 predictions)};"""

new_nodes = """% ---- Row 3: Adaptive drift handling (below ensemble) ----
\\node[decision, below=1.5cm of ensemble] (adwin) {ADWIN Detects\\\\ Drift ($D_t$)?};
\\node[process] (replace) at (aggregation |- adwin) {Replace with\\\\ Background Tree};

% ---- Row 4: Precision feedback + penalty update (bottom row) ----
\\node[box, below=2.8cm of adwin] (calc_lambda) {Update Penalty\\\\ $\\lambda_t = \\min(\\Lambda_{max}, IR_t(1{+}\\gamma D_t)) \\times \\rho_t$};
\\node[box] (damping) at (aggregation |- calc_lambda) {Precision-Feedback Damping\\\\ $\\rho_t = \\max(0.1,\\ \\hat{P}_t / P_{min})$\\\\ if $\\hat{P}_t < P_{min}$, else $1.0$};
\\node[process] (precision) at (prediction |- calc_lambda) {Rolling Precision $\\hat{P}_t$\\\\ (last 200 predictions)};"""

if old_nodes in content:
    content = content.replace(old_nodes, new_nodes)
    with open('figures/architecture.tex', 'w') as f:
        f.write(content)
    print("Alignment updated.")
else:
    print("Could not find the target string to replace.")
