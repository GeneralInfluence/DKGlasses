import numpy as np

SR = np.arange(2,10,0.5)
Tam = np.arange(1,2,0.1)
Pm = np.arange(0.8,0.96,0.2)

Pa = [[[0] * len(SR)] * len(Tam)] * len(Pm)
for s,sr in enumerate(SR):
  for t,tam in enumerate(Tam):
    for p,pm in enumerate(Pm):
      Pa[s][t][p] = 1 - sr + tam * ( sr - (1-pm) )
