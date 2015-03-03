import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def phase_portrait(fun, delta=0.01, box=[-1, 1, -1, 1]):
    """Display phase portrait of a given function.

    Arguments:
        delta  Sampling rate; defines the resolution of the portrait.
               Default value: 0.01

        box    Rectangular plot region in the complex plane:
                   box[0] <= real(z) <= box[1] 
                   box[2] <= imag(z) <= box[3] 
               Default value: [-1,1,-1,1]

    """
    x = np.arange(box[0], box[1], delta)
    y = np.arange(box[2], box[3], delta)

    # Generate plot domain
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Evaluate function
    fZ = fun(Z)

    # Pass over for display, and return AxesImage
    return show_portrait(Z, fZ)


def show_portrait(Z, fZ, modulus=False):
    """Show phase portrait represented by given rectangular array of
    complex numbers."""

    # Split f(Z) apart. Phase is oriented such that red >0 and blue <0
    phase = np.angle(-fZ)
    modulus = np.abs(fZ)

    # Get base hsv colormap
    cmap = cm.hsv
    norm = colors.Normalize()
    mapper = cm.ScalarMappable(norm=norm, cmap=cmap)

    imvals = mapper.to_rgba(phase)
    return plt.imshow(imvals)
