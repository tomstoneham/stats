# Generate Quantiles for the Chi-Square distribution
# Requires that you have the scipy module installed
# Pretty ugly really but who cares
from scipy.stats import chi2

buf = """\\setlength{\\tabcolsep}{3pt}
\\renewcommand{\\arraystretch}{1}
\\begin{center}
\\begin{tabular}{c | c c c c c c c c c c c c}
$n$"""

quantiles = [0.005, 0.01, 0.025, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.975, 0.99,
0.995]

for quant in quantiles:
    buf += " & " + str(quant)

buf += " \\\\\n\hline\n"

for i in range(1, 31) + range(32, 40, 2) + range(42, 50, 4) + range(50, 101, 5):
    buf += str(i)
    for quant in quantiles:
        buf += " & {:.2f}".format(chi2.ppf(quant, i), 2)
    buf += " \\\\\n"

buf += """\\end{tabular}
\\end{center}
\\renewcommand{\\arraystretch}{1.5}
\\setlength{\\tabcolsep}{5pt}"""

with open('quant.tex', 'w') as f:
    f.write(buf)
