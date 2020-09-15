# field-equations

Mathematica and Maple code for inspection of the area metric gravity field equations derived in [../cadabra/](../cadabra/).

* The Mathematica files `*.m` are used for constructing a basis of gravitational constants from the entirety of coefficients present in the linearized field equations. The suffix `_reduced` indicates that the theory has been further reduced (`k_14 = 0` and `k_16 = ...` as consequence of a phenomenological requirement).
* The Maple files define (non-redundant subsets of) the field equations for the various modes in fourier space, where a factor `a` comes from a time derivative and a factor `b` from a spatial derivative. These are used for investigating the principal polynomial, solving the stationary case, etc.
