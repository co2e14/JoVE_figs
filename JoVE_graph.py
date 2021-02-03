import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def removespace(filein, fileout):
    fin = open(filein, "rt")
    fout = open(fileout, "wt")

    for line in fin:
        fout.write(" ".join(line.split()) + "\n")
    fin.close()
    fout.close()


values = pd.read_csv("values.csv")
flux = values.drop(labels="res", axis=1)
flux = flux.dropna()
res = values.drop(labels="flux", axis=1)
res = res.dropna()

inputfiles = ["Ca.dat", "Cl.dat", "S.dat", "P.dat"]
outputfiles = []

for data in inputfiles:
    out = data.lower()
    removespace(data, out)
    outputfiles += [out]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Energy')
ax1.set_ylabel("Res/f''", color='red')
plt.plot("energy", "res", data=res, marker="", color='red')

for data in outputfiles:
    toplot = pd.read_table(data, sep=" ", names=("energy", "fp", "fpp"))
    toplot = toplot.drop(labels="fp", axis=1)
    ax1.plot("energy", "fpp", data=toplot)

ax2 = ax1.twinx()

ax2.set_ylabel('Flux', color='purple')
ax2.plot("energy", "flux", data=flux, color='purple')
#fig.tight_layout()
plt.show()