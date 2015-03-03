import phaseplot as pp
import matplotlib.pyplot as plt

def polyfun(z):
    return z*z - z + 1

pp.phase_portrait(polyfun)
plt.show()
