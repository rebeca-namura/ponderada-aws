import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

data = """10053 5.00 0.00
10456 5.00 0.00
10858 5.00 0.00
11259 5.00 0.00
11662 5.00 0.00
12064 4.03 0.97
12467 2.69 2.31
12869 1.80 3.20
13272 1.21 3.79
13674 0.81 4.19
14076 0.54 4.46
14479 0.36 4.64
14881 0.24 4.76
15283 0.16 4.84
15685 0.11 4.89
16088 0.07 4.93
16490 0.05 4.95
16892 0.03 4.97
17295 0.02 4.98
17697 0.01 4.99
18100 0.01 4.99
18502 0.00 5.00
18905 0.00 5.00
19306 0.00 5.00
19708 0.00 5.00





"""

df = pd.read_csv(StringIO(data), sep=" ", names=["tempo", "tR", "tC"])

plt.figure(figsize=(8,4))
plt.plot(df["tempo"], df["tR"], label="Tensão no Resistor (Vc)", color="pink", marker='o')
plt.plot(df["tempo"], df["tC"], label="Tensão no Capacitor (Vr)", color="green", marker='x')

plt.xlabel("Tempo (ms)")
plt.ylabel("Tensão (V)")
plt.title("Curva de Carga no Circuito RC")
plt.legend()
plt.grid(True)
plt.show()