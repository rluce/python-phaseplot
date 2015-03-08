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
               Further methods of specifying the rectangular region are
               discussed below.

    Example:
    --------
    Here is a phase portrait of the function f(z) = z:
        >>> import phaseplot as pp
        >>> pp.phase_portrait(lambda(z) : z) #doctest: +ELLIPSIS
        <matplotlib.image.AxesImage object at 0x...>

    Note that a reference to the created AxesImage object is returned.
    Use matplotlib.pyplot.show() in order to display the actual image.

    Alternative box specification
    -----------------------------
    The |box| parameter also takes other forms than described above (all radii
    are understood in infinity norm):

      - A 3-tuple (m, r1, r2) where 'm' is the midpoint, 'r1' is the radius
        for the real part, and 'r2' is the radius for the imaginary part.
      - A 2-tuple (z1, z2) where z1, z2 are the lower-left and upper-right
        corners of the plot rectangle. NOTE: z2 must be of type 'complex'.
      - A 2-tuple (m, r) where 'm' is the midpoint and 'r' the radius for both
        the real and imaginary part.
      - A 1-tuple or scalar defining the midpoint m.  In this case a plot box
        with radius 1 is produced.
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
        (0.0, 2.0, -2.0, 0.0)
    """

    if (isinstance(box, float) or isinstance(box, complex) or
        isinstance(box, int)):
        # Turn scalar into 1-tuple
        box = box,

    if len(box) == 4:
        # Two intervals specified, nothing to do
        outbox = box
    elif len(box) == 3:
        # We have a midpoint and radii for real and imag part
        (mid, r_re, r_im) = box

        # Allow real input, interpret with mid.z == 0
        mid = complex(mid)
        outbox = (
            mid.real - r_re, mid.real + r_re,
            mid.imag - r_im, mid.imag + r_im
            )
    elif len(box) == 2 and type(box[1]) == complex:
        # We have lower-left and upper-right point in the complex plae

        (ll, ur) = box
        ll = complex(ll)

        outbox = (ll.real, ur.real, ll.imag, ur.imag)
    elif len(box) == 2:
        (mid, r) = box
        mid = complex(mid)
        outbox = (mid.real - r, mid.real + r, mid.imag - r, mid.imag + r)
    elif len(box) == 1:
        mid = complex(box[0])
        outbox = (mid.real - 1, mid.real + 1, mid.imag - 1, mid.imag + 1)
    else: assert(False)

    return tuple([float(v) for v in outbox])


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
