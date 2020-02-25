# Generate Quantiles for the Chi-Square distribution
# Requires that you have the scipy module installed
# Pretty ugly really but who cares
from scipy.stats import chi2

buf = """
\\begin{center}
\\begin{tabular}{c | c c c c c c c c c c c c}
$n$"""

quantiles = [0.005, 0.01, 0.025, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.975, 0.99,
0.995]

for quant in quantiles:
    buf += " & " + str(quant)

buf += " \\\\\n\hline\n"

for i in range(1, 31) + range(35, 60, 5) + range(60, 101, 10):
    buf += str(i)
    for quant in quantiles:
        buf += " & {:.2f}".format(chi2.ppf(quant, i), 2)
    buf += " \\\\\n"

buf += """\\end{tabular}
\\end{center}"""

with open('quant.tex', 'w') as f:
    f.write(buf)
