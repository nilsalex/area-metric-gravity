k15 = -16 k9
k16 = -8 k13

t1 = -1/32 k15
t2 = 1/32 k15
t3 = 1/2 k9 + 1/32 k15
t4 = 1/2 k9 + 1/32 k15
t5 = -4 k13 - 1/2 k16
t6 = 2 k13 + 1/4 k16
t7 = 2 k13 + 1/4 k16
t8 = k9 + 1/16 k15

t9 = 1/2 k9 + 1/32 k15
t10 = 1/2 k9 + 1/32 k15
t11 = 4 k13 + 1/2 k16
t12 = 3/2 k4 - 6 k5 + 12 k6 + 8 k7 + 4 k8 + 6 k10 + 8 k12 + 4 k13 + 48 k14 + k16
t13 = -3/2 k4 + 6 k5 - 12 k6 - 8 k7 - 4 k8 - 6 k10 - 8 k12 - 4 k13 - 48 k14 - k16
t14 = 6 k1 + 24 k2 + 8 k3
t15 = 8 k7 - 8 k8 + 8 k12 + 4 k13 + 1/2 k16
t16 = -8 k7 + 8 k8 - 8 k12 - 4 k13 - 1/2 k16
t17 = 8 k3

t18 = 2 k13 + 1/4 k16
t19 = 2 k13 + 1/4 k16
t20 = -k9 - 1/16 k15
t21 = 8 k7 - 8 k8 + 8 k12 + 4 k13 + 1/2 k16
t22 = -8 k7 + 8 k8 - 8 k12 - 4 k13 - 1/2 k16
t23 = 8 k3
t24 = -3/2 k4 + 6 k5 - 12 k6 - 8 k7 - 4 k8 - 6 k10 - 8 k12 - 4 k13 - 48 k14 - k16
t25 = 3/2 k4 - 6 k5 + 12 k6 + 8 k7 + 4 k8 + 6 k10 + 8 k12 + 4 k13 + 48 k14 + k16
t26 = -6 k1 - 24 k2 - 8 k3

vars = {k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14}

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
