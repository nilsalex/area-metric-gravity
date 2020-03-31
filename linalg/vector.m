v1 = -1/8 k15
v2 = k9 + 1/16 k15
v3 = -4 k13 - 1/2 k16

v4 = 2 k9 + 1/8 k15
v5 = 8 k13 + k16
v6 = 3 k4 - 12 k5 + 24 k6 + 16 k7 + 8 k8 + 12 k10 + 16 k12 + 8 k13 + 96 k14 + 2 k16
v7 = -3 k4 + 12 k5 - 24 k6 - 16 k7 - 8 k8 - 12 k10 - 16 k12 - 8 k13 - 96 k14 - 2 k16
v8 = 12 k1 + 48 k2 + 16 k3
v9 = 16 k3

v10 = 8 k13 + k16
v11 = -2 k9 - 1/8 k15
v12 = 16 k7 - 16 k8 + 16 k12 + 8 k13 + k16
v13 = -16 k7 + 16 k8 - 16 k12 - 8 k13 - k16
v14 = 16 k3
v15 = -12 k1 - 48 k2 - 16 k3

vars = {k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16}

MK = {}

AppendTo[MK, CoefficientArrays[s1, vars][[2]]]
AppendTo[MK, CoefficientArrays[s2, vars][[2]]]
AppendTo[MK, CoefficientArrays[s3, vars][[2]]]
AppendTo[MK, CoefficientArrays[s4, vars][[2]]]
AppendTo[MK, CoefficientArrays[s5, vars][[2]]]
AppendTo[MK, CoefficientArrays[s6, vars][[2]]]
AppendTo[MK, CoefficientArrays[s7, vars][[2]]]
AppendTo[MK, CoefficientArrays[s8, vars][[2]]]
AppendTo[MK, CoefficientArrays[s9, vars][[2]]]
AppendTo[MK, CoefficientArrays[s10, vars][[2]]]
AppendTo[MK, CoefficientArrays[s11, vars][[2]]]
AppendTo[MK, CoefficientArrays[s12, vars][[2]]]
AppendTo[MK, CoefficientArrays[s13, vars][[2]]]
AppendTo[MK, CoefficientArrays[s14, vars][[2]]]
AppendTo[MK, CoefficientArrays[s15, vars][[2]]]

mat := NullSpace[Transpose[MK]]

Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15})[[10]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15})[[9]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15})[[8]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15})[[7]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15})[[6]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15})[[5]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15})[[4]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15})[[3]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15})[[2]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15})[[1]]]]]]
