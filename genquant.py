# Generate Quantiles for the Chi-Square distribution
# Requires that you have the scipy module installed
# Pretty ugly really but who cares
from scipy.stats import chi2, t
def buildlatex(distppf, quantiles, ran):
    buf = """\\setlength{\\tabcolsep}{3pt}
\\renewcommand{\\arraystretch}{1}
\\begin{center}
\\begin{tabular}{c |"""

    for quant in quantiles:
        buf += " c"

    buf += "}\n$n$"

    for quant in quantiles:
        buf += " & " + str(quant)

    buf += " \\\\\n\hline\n"

    for i in ran:
        buf += str(i)
        for quant in quantiles:
            buf += " & {:.2f}".format(distppf(quant, i))
        buf += " \\\\\n"

    buf += """\\end{tabular}
\\end{center}
\\renewcommand{\\arraystretch}{1.5}
\\setlength{\\tabcolsep}{5pt}"""

    return buf

def mchi2():
    quantiles = [0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95,
        0.975, 0.99, 0.995]
    ran = range(1, 31) + range(32, 40, 2) + range(42, 50, 4) + range(50, 101, 5)
    buf = buildlatex(chi2.ppf, quantiles, ran)

    with open('quant-chi2.tex', 'w') as f:
        f.write(buf)

def mt():
    quantiles = [0.6, 0.75, 0.8, 0.85, 0.9, 0.95, 0.975, 0.98, 0.99, 0.995,
        0.999, 0.9995]
    ran = range(1, 20) + range(20, 40, 2) + range(42, 51, 4) + range(50, 81, 10) + [100, 200, 9999999]
    buf = buildlatex(t.ppf, quantiles, ran)

    with open('quant-t.tex', 'w') as f:
        f.write(buf)

mchi2()
mt()
