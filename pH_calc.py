__author__ = 'heath'
__author__ = 'ulmchemistry'
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

def f(vT,cT,vA,cA,pKa):
    if vA*cA - vT*cT > 0:
        pH = pKa + np.log10((vT*cT)/(vA*cA-vT*cT))
    else:
        if vA*cA - vT*cT == 0:
            pH = 14 - (-np.log10((10^(-pKa)*vA*cA)^(0.5)))
        else:
            pH = 14 - (-np.log10(vT*cT-vA*cA))
    return pH



pKa = [3.74,4.74,5.74,6.74]
pK = np.arange(1,6.5,0.25)
vA = 15
cA = 0.01
cT = 0.01
vol = np.arange(0.001, 25.0, 0.1)
pH = np.vectorize(f)
plt.figure(1)
for i in pK:
    plt.plot(vol, pH(vol,cT,vA,cA,i), 'k-')
plt.show()