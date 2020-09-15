# second order area metric gravity

 * [](split.py) performs constructs the 3+1 theory from the ansätze and solutions derived in [](../../haskell/ansaetze)
 * `mass_ABC*.cdb, kin_ABCI*.cdb, kin_ABpCq*.cdb` contain the respective constituents of the Lagrangian. A suffix `sol` indicates
   that the constants are solved. A suffix like `A` indicates that the term is ready for variation with respect to the field (A in this example).
   We only care for field equations at `B^\alpha = 0, W^{\alpha\beta} = 0, U^{\alpha\beta} = U1 \gamma^{\alpha\beta}, V^{\alpha\beta} = V1^{\alpha\beta}`,
   so these substitutions are made *except for the field which is to be varied*.
 * `eom_*.cdb` contains the field equations. A suffix `tf` indicates the trace-free part, a suffix `trace` indicates the trace part, a suffix `part` indicates that double derivatives have been integrated "away" by integration by parts.
