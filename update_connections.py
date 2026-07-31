with open('figures/architecture.tex', 'r') as f:
    content = f.read()

start_str = "% ---- Connections: Row 3"
end_str = "% Background Groups"

start_idx = content.find(start_str)
end_idx = content.find(end_str)

new_connections = """% ---- Connections: Row 3 ----
\\draw[arrow] (ensemble) -- (adwin);
\\draw[arrow] (adwin.east) -- node[above] {Yes} (replace.west);
\\draw[arrow] (replace.north) -- (ensemble.south east);

% ---- Connections: Row 4 (feedback loop) ----
\\draw[arrow] (prediction.south) -- (precision.north);
\\draw[arrow] (precision.west) -- (damping.east);
\\draw[arrow] (damping.west) -- (calc_lambda.east);
\\draw[dashed_arrow] (calc_lambda.west) -| ($(diversify.west) + (-0.5,0)$) |- (min_weight.west);
\\draw[dashed_arrow] (adwin.south) -- node[left] {Update $D_t$} (calc_lambda.north);

"""

content = content[:start_idx] + new_connections + content[end_idx:]

with open('figures/architecture.tex', 'w') as f:
    f.write(content)
print("Connections updated.")
