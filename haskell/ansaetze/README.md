# ansaetze

* Makes use of [safe-tensor](https://hackage.haskell.org/package/safe-tensor), the ansatz generation capabilities of [sparse-tensor](https://hackage.haskell.org/package/sparse-tensor), and a [compatibility layer](https://github.com/nilsalex/safe-tensor/tree/master/packages/safe-tensor-sparse-tensor-compat) in order to construct Lorentz invariant ansätze for diffeomorphism invariant area metric gravity.
* The ansaetze are stored in [./first_order/](./first_order/) for linear area metric gravity and in [./second_order/](./second_order/) for second order area metric gravity.
* Solves these ansätze for diffeomorphism invariance using [safe-tensor](https://hackage.haskell.org/package/safe-tensor).
* The solution is given by substitution rules for the gravitational constants, stored in [./first_order/rules.txt](./first_order/rules.txt) and [./second_order/rules.txt](./second_order/rules.txt).
