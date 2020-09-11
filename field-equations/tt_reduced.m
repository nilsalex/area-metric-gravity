k14 = 0
k16 = 1/6 k6 + 1/8 k7 - 1/2 k12

t1 = 1/2 k6 + 3/8 k7
t2 = -1/2 k6 - 3/8 k7
t3 = -1/2 k14
t4 = -1/2 k14
t5 = -2 k6 - 3/2 k7 + 6 k12 + 2 k14 + 12 k16
t6 = k6 + 3/4 k7 - 3 k12 - k14 - 6 k16
t7 = k6 + 3/4 k7 - 3 k12 - k14 - 6 k16
t8 = -k14

t9 = -1/2 k14
t10 = -1/2 k14
t11 = 2 k6 + 3/2 k7 - 6 k12 - 2 k14 - 12 k16
t12 = 1/2 k6 + 11/8 k7 + 2 k8 - 2 k13 - k14
t13 = -1/2 k6 - 11/8 k7 - 2 k8 + 2 k13 + k14
t14 = -2 k2
t15 = -2 k4 + 24 k5 - k6 - 3/4 k7 + 4 k8 - 12 k9 + 24 k10 - 24 k11 - 6 k12 - 4 k13 - 2 k14 - 48 k15 - 12 k16
t16 = 2 k4 - 24 k5 + k6 + 3/4 k7 - 4 k8 + 12 k9 - 24 k10 + 24 k11 + 6 k12 + 4 k13 + 2 k14 + 48 k15 + 12 k16
t17 = -24 k1 - 4 k2 - 24 k3

t18 = k6 + 3/4 k7 - 3 k12 - k14 - 6 k16
t19 = k6 + 3/4 k7 - 3 k12 - k14 - 6 k16
t20 = k14
t21 = -2 k4 + 24 k5 - k6 - 3/4 k7 + 4 k8 - 12 k9 + 24 k10 - 24 k11 - 6 k12 - 4 k13 - 2 k14 - 48 k15 - 12 k16
t22 = 2 k4 - 24 k5 + k6 + 3/4 k7 - 4 k8 + 12 k9 - 24 k10 + 24 k11 + 6 k12 + 4 k13 + 2 k14 + 48 k15 + 12 k16
t23 = -24 k1 - 4 k2 - 24 k3
t24 = -1/2 k6 - 11/8 k7 - 2 k8 + 2 k13 + k14
t25 = 1/2 k6 + 11/8 k7 + 2 k8 - 2 k13 - k14
t26 = 2 k2

vars = {k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k15}

MK = {}

AppendTo[MK, CoefficientArrays[t1, vars][[2]]]
AppendTo[MK, CoefficientArrays[t2, vars][[2]]]
AppendTo[MK, CoefficientArrays[t12, vars][[2]]]
AppendTo[MK, CoefficientArrays[t13, vars][[2]]]
AppendTo[MK, CoefficientArrays[t14, vars][[2]]]
AppendTo[MK, CoefficientArrays[t15, vars][[2]]]
AppendTo[MK, CoefficientArrays[t16, vars][[2]]]
AppendTo[MK, CoefficientArrays[t17, vars][[2]]]
AppendTo[MK, CoefficientArrays[t21, vars][[2]]]
AppendTo[MK, CoefficientArrays[t22, vars][[2]]]
AppendTo[MK, CoefficientArrays[t23, vars][[2]]]
AppendTo[MK, CoefficientArrays[t24, vars][[2]]]
AppendTo[MK, CoefficientArrays[t25, vars][[2]]]
AppendTo[MK, CoefficientArrays[t26, vars][[2]]]

mat := NullSpace[Transpose[MK]]

Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x12, x13, x14, x15, x16, x17, x21, x22, x23, x24, x25, x26})[[9]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x12, x13, x14, x15, x16, x17, x21, x22, x23, x24, x25, x26})[[8]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x12, x13, x14, x15, x16, x17, x21, x22, x23, x24, x25, x26})[[7]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x12, x13, x14, x15, x16, x17, x21, x22, x23, x24, x25, x26})[[6]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x12, x13, x14, x15, x16, x17, x21, x22, x23, x24, x25, x26})[[5]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x12, x13, x14, x15, x16, x17, x21, x22, x23, x24, x25, x26})[[4]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x12, x13, x14, x15, x16, x17, x21, x22, x23, x24, x25, x26})[[3]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x12, x13, x14, x15, x16, x17, x21, x22, x23, x24, x25, x26})[[2]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x12, x13, x14, x15, x16, x17, x21, x22, x23, x24, x25, x26})[[1]]]]]]

Print["t1 ="<>ToString[InputForm[Expand[t1]]]]
Print["t2 ="<>ToString[InputForm[Expand[t2]]]]
Print["t3 ="<>ToString[InputForm[Expand[t3]]]]
Print["t4 ="<>ToString[InputForm[Expand[t4]]]]
Print["t5 ="<>ToString[InputForm[Expand[t5]]]]
Print["t6 ="<>ToString[InputForm[Expand[t6]]]]
Print["t7 ="<>ToString[InputForm[Expand[t7]]]]
Print["t8 ="<>ToString[InputForm[Expand[t8]]]]
Print["t9 ="<>ToString[InputForm[Expand[t9]]]]
Print["t10 ="<>ToString[InputForm[Expand[t10]]]]
Print["t11 ="<>ToString[InputForm[Expand[t11]]]]
Print["t12 ="<>ToString[InputForm[Expand[t12]]]]
Print["t13 ="<>ToString[InputForm[Expand[t13]]]]
Print["t14 ="<>ToString[InputForm[Expand[t14]]]]
Print["t15 ="<>ToString[InputForm[Expand[t15]]]]
Print["t16 ="<>ToString[InputForm[Expand[t16]]]]
Print["t17 ="<>ToString[InputForm[Expand[t17]]]]
Print["t18 ="<>ToString[InputForm[Expand[t18]]]]
Print["t19 ="<>ToString[InputForm[Expand[t19]]]]
Print["t20 ="<>ToString[InputForm[Expand[t20]]]]
Print["t21 ="<>ToString[InputForm[Expand[t21]]]]
Print["t22 ="<>ToString[InputForm[Expand[t22]]]]
Print["t23 ="<>ToString[InputForm[Expand[t23]]]]
Print["t24 ="<>ToString[InputForm[Expand[t24]]]]
Print["t25 ="<>ToString[InputForm[Expand[t25]]]]
Print["t26 ="<>ToString[InputForm[Expand[t26]]]]
