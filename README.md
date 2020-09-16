# area-metric-gravity
[![DOI](https://zenodo.org/badge/195409525.svg)](https://zenodo.org/badge/latestdoi/195409525)

Perturbative expansion of area metric gravity to second order in the equations of motion (third order in the lagrangian). Building up on the [paper](https://doi.org/10.1103/PhysRevD.101.084025) on covariant constructive gravity. This repository contains:

 * A [Haskell application](haskell/ansaetze) generating Lorentz invariant expansion coefficients and solving the diffeomorphism covariance equations perturbatively
 * [Cadabra code](cadabra) using the results from the Haskell application, performing a 3+1 split of the Lagrangian and deriving the corresponding field equations
 * [Maple and Mathematica code](field-equations) for further inspection of the field equations
