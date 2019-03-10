import matplotlib.pyplot as plt
import numpy as np
import array as arr
import math


def hDeF(f):
   return (0.4/(1.016-0.8*math.cos(2*(math.pi)*(f/1000))))





t1 = np.arange(100)
frec=np.arange(1,1000,0.1)
rtafrec=arr.array('d')

for i in frec:
    rtafrec.append(20*math.log10((hDeF(i))))


l = plt.plot(frec,rtafrec, 'ro')
plt.xlabel('Frecuencia[Hz]')
plt.ylabel('atenuacion [dB]')
plt.title('Respuesta en frecuencia')
plt.semilogx()
plt.setp(l, markersize=10)
plt.setp(l, markerfacecolor='C0')

plt.show()