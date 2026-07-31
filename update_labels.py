with open('figures/architecture.tex', 'r') as f:
    content = f.read()

# Fix the dashed line passing through group1b
old_line = "\\draw[dashed_arrow] (calc_lambda.west) -| ($(diversify.west) + (-0.5,0)$) |- (min_weight.west);"
new_line = "\\draw[dashed_arrow] (calc_lambda.west) -| ($(window.west) + (-0.8,0)$) |- (min_weight.west);"
content = content.replace(old_line, new_line)

# Shift group1b label left
old_label1 = "label={[shift={(0,0)}]below:\\textbf{Synthetic Diversification}}"
new_label1 = "label={[shift={(-1.5cm,0)}]below:\\textbf{Synthetic Diversification}}"
content = content.replace(old_label1, new_label1)

# Fix group3 label shift. The user said "geser ke kiri" for the "Rolling Precision" label (meaning Precision-Feedback Damping)
# I will shift it back to center or far left. Let's shift it right to avoid the dashed line on the left.
old_label3 = "label={[shift={(-1.2cm,-0.9cm)}]below:\\textbf{Precision-Feedback Damping}}"
new_label3 = "label={[shift={(0cm,-0.9cm)}]below:\\textbf{Precision-Feedback Damping}}"
content = content.replace(old_label3, new_label3)

with open('figures/architecture.tex', 'w') as f:
    f.write(content)
print("Updated successfully.")
