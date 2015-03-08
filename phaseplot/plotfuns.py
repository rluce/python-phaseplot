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


    Example:
    Here is a phase portrait of the function f(z) = z:
        >>> import phaseplot as pp
        >>> pp.phase_portrait(lambda(z) : z) #doctest: +ELLIPSIS
        <matplotlib.image.AxesImage object at 0x...>

    Note that a reference to the created AxesImage object is returned.
    Use matplotlib.pyplot.show() in order to display the actual image.
    """
    x = np.arange(box[0], box[1], delta)
    y = np.arange(box[2], box[3], delta)

    # Generate plot domain
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Evaluate function
    fZ = fun(Z)

    # Pass over for display, and return AxesImage
    return show_portrait(Z, fZ, box)


def show_portrait(Z, fZ, box, modulus=False):
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
    return plt.imshow(imvals, origin='lower', extent=tuple(box))
