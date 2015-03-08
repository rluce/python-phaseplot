import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def phase_portrait(fun, delta=0.01, box=(-1, 1, -1, 1)):
    """Display phase portrait of a given function.

    Arguments:
        delta  Sampling rate; defines the resolution of the portrait.
               Default value: 0.01

        box    A 4-tuple defining the rectangular plot region in the complex
               plane:
                   box[0] <= real(z) <= box[1] 
                   box[2] <= imag(z) <= box[3] 
               Default value: (-1,1,-1,1)

    Example:
    Here is a phase portrait of the function f(z) = z:
        >>> import phaseplot as pp
        >>> pp.phase_portrait(lambda(z) : z) #doctest: +ELLIPSIS
        <matplotlib.image.AxesImage object at 0x...>

    Note that a reference to the created AxesImage object is returned.
    Use matplotlib.pyplot.show() in order to display the actual image.
    """

    box = interpret_box(box)
    x = np.arange(box[0], box[1], delta)
    y = np.arange(box[2], box[3], delta)

    # Generate plot domain
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Evaluate function
    fZ = fun(Z)

    # Pass over for display, and return AxesImage
    return gen_portrait(Z, fZ, box)

########### NON API #####################################################

def interpret_box(box):
    """Expand given tuple for box specification to 4-tuple form.
    The returned values are normalized to be of type float, even if
    corresponding values of the input weren't originally.
    Examples:
        >>> interpret_box( (1,2,3,4) )
        (1.0, 2.0, 3.0, 4.0)
        >>> interpret_box( (1+1j, 2, 3) )
        (-1.0, 3.0, -2.0, 4.0)
        >>> interpret_box( (1+1j, 2+4j) )
        (1.0, 2.0, 1.0, 4.0)
        >>> interpret_box( (0+1j, 1) )
        (-1.0, 1.0, 0.0, 2.0)
        >>> interpret_box( (1-1j) )
        (0.0, 2.0, 0.0, -2.0)
    """

    if len(box) == 4:
        return box
    else:
        return (-1,1,-1,1)


def gen_portrait(Z, fZ, box, modulus=False):
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
