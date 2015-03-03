import phaseplot as pp

def example_polynomial():
    """Standard phase portait of a degree-two polynomial"""

    def polyfun(z):
        return z*z - z + 1

    p = pp.phase_portrait(polyfun)
