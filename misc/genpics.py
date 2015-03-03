# Simple script to generate some static pics for GitHub page etc.

import sys
import matplotlib.pyplot as plt

sys.path.append('../examples')
from ppexamples import example_polynomial

axim = example_polynomial()
plt.savefig('ex_poly.png', bbox_inches='tight')


