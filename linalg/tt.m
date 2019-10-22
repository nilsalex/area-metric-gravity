t1 = 1/8 * k4 +  1/8 * k5 -  1/2 * k6 - 3 * k7 - 5 * k8 - 12 * k9 - 6 * k10 - 3 * k11 + 5/2 * k12 + 3 * k13 + 3/16 * k16
t2 = 6 * k1 - 24 * k2 - 8 * k3
t3 = -1/2 * k4 - 1/2 * k5 + 2 * k6 + 12 * k7 + 12 * k8 - 8 * k14 - 4 * k15
t4 = -8 * k3
t5 = -3/16 * k4 - 3/16 * k5 + 3/4 * k6 + 9/2 * k7 + 3/2 * k8 + 3/4 * k9 + 3/8 * k10 + 1/16 * k11 - 19/32 * k12 - 3/16 * k13 + 7/256 * k16
t6 = 4 * k15

t7 = -1/2 * k4 - 1/2 * k5 + 2 * k6 + 12 * k7 + 12 * k8 - 8 * k14 - 4 * k15
t8 = -8 * k3
t9 = -1/8 * k4 - 1/8 * k5 + 1/2 * k6 + 3 * k7 + 5 * k8 + 12 * k9 + 6 * k10 + 3 * k11 - 5/2 * k12 - 3 * k13 - 3/16 * k16
t10 = -6 * k1 + 24 * k2 + 8 * k3
t11 = 2 * k15
t12 = 3/8 * k4 + 3/8 * k5 - 3/2 * k6 - 9 * k7 - 3 * k8 - 3/2 * k9 - 3/4 * k10 - 1/8 * k11 + 19/16 * k12 + 3/8 * k13 - 7/128 * k16

t13 = 1/4 * k4 + 1/4 * k5 - k6 - 8 * k7 - 6 * k8 - 27/2 * k9 - 27/4 * k10 - 9/8 * k11 + 27/16 * k12 + 27/8 * k13 + 17/128 * k16
t14 = -3/16 * k4 - 3/16 * k5 + 3/4 * k6 + 9/2 * k7 + 3/2 * k8 + 3/4 * k9 + 3/8 * k10 + 1/16 * k11 - 19/32 * k12 - 3/16 * k13 + 7/256 * k16
t15 = 2 * k15
t16 = -4 * k15
t17 = -3/8 * k4 - 3/8 * k5 + 3/2 * k6 + 9 * k7 + 3 * k8 + 3/2 * k9 + 3/4 * k10 + 1/8 * k11 - 19/16 * k12 - 3/8 * k13 + 7/128 * k16

vars = {k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16}

MK = {}

AppendTo[MK, CoefficientArrays[t1, vars][[2]]]
AppendTo[MK, CoefficientArrays[t2, vars][[2]]]
AppendTo[MK, CoefficientArrays[t3, vars][[2]]]
AppendTo[MK, CoefficientArrays[t4, vars][[2]]]
AppendTo[MK, CoefficientArrays[t5, vars][[2]]]
AppendTo[MK, CoefficientArrays[t6, vars][[2]]]
AppendTo[MK, CoefficientArrays[t7, vars][[2]]]
AppendTo[MK, CoefficientArrays[t8, vars][[2]]]
AppendTo[MK, CoefficientArrays[t9, vars][[2]]]
AppendTo[MK, CoefficientArrays[t10, vars][[2]]]
AppendTo[MK, CoefficientArrays[t11, vars][[2]]]
AppendTo[MK, CoefficientArrays[t12, vars][[2]]]
AppendTo[MK, CoefficientArrays[t13, vars][[2]]]
AppendTo[MK, CoefficientArrays[t14, vars][[2]]]
AppendTo[MK, CoefficientArrays[t15, vars][[2]]]
AppendTo[MK, CoefficientArrays[t16, vars][[2]]]
AppendTo[MK, CoefficientArrays[t17, vars][[2]]]

mat := NullSpace[Transpose[MK]]
