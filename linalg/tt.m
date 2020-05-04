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
AppendTo[MK, CoefficientArrays[t18, vars][[2]]]
AppendTo[MK, CoefficientArrays[t19, vars][[2]]]
AppendTo[MK, CoefficientArrays[t20, vars][[2]]]
AppendTo[MK, CoefficientArrays[t21, vars][[2]]]
AppendTo[MK, CoefficientArrays[t22, vars][[2]]]
AppendTo[MK, CoefficientArrays[t23, vars][[2]]]
AppendTo[MK, CoefficientArrays[t24, vars][[2]]]
AppendTo[MK, CoefficientArrays[t25, vars][[2]]]
AppendTo[MK, CoefficientArrays[t26, vars][[2]]]

mat := NullSpace[Transpose[MK]]

Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[19]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[18]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[17]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[16]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[15]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[14]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[13]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[12]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[11]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[10]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[9]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[8]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[7]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[6]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[5]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[4]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[3]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[2]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26})[[1]]]]]]
