v1 = 2 k6 + 3/2 k7
v2 = k6 + 3/4 k7 - k14
v3 = -2 k6 - 3/2 k7 + 6 k12 + 2 k14 + 12 k16
v4 = 2 k6 + 3/2 k7 - 6 k12 - 2 k14 - 12 k16
v5 = -k14

v6 = -2 k14
v7 = 4 k6 + 3 k7 - 12 k12 - 4 k14 - 24 k16
v8 = k6 + 11/4 k7 + 4 k8 - 4 k13 - 3 k14
v9 = -k6 - 11/4 k7 - 4 k8 + 4 k13 + 2 k14
v10 = 2 k6 + 3/2 k7 - 6 k12 - 2 k14 - 12 k16
v11 = -4 k2
v12 = -4 k4 + 48 k5 - 2 k6 - 3/2 k7 + 8 k8 - 24 k9 + 48 k10 - 48 k11 - 12 k12 - 8 k13 - 4 k14 - 96 k15 - 24 k16
v13 = 4 k4 - 48 k5 + 2 k6 + 3/2 k7 - 8 k8 + 24 k9 - 48 k10 + 48 k11 + 12 k12 + 8 k13 + 4 k14 + 96 k15 + 24 k16
v14 = -48 k1 - 8 k2 - 48 k3

v15 = 4 k6 + 3 k7 - 12 k12 - 4 k14 - 24 k16
v16 = 2 k14
v17 = -4 k4 + 48 k5 + 8 k8 - 24 k9 + 48 k10 - 48 k11 - 18 k12 - 8 k13 - 6 k14 - 96 k15 - 36 k16
v18 = 4 k4 - 48 k5 + 2 k6 + 3/2 k7 - 8 k8 + 24 k9 - 48 k10 + 48 k11 + 12 k12 + 8 k13 + 4 k14 + 96 k15 + 24 k16
v19 = k14
v20 = -48 k1 - 8 k2 - 48 k3
v21 = -k6 - 11/4 k7 - 4 k8 + 4 k13 + 2 k14
v22 = k6 + 11/4 k7 + 4 k8 - 4 k13 - 2 k14
v23 = 4 k2

v24 = 4 k6 + 3 k7
v25 = 2 k6 + 3/2 k7 - 2 k14
v26 = -4 k6 - 3 k7 + 12 k12 + 4 k14 + 24 k16
v27 = 4 k6 + 3 k7 - 12 k12 - 4 k14 - 24 k16
v28 = -2 k14

vars = {k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16}

MK = {}

AppendTo[MK, CoefficientArrays[v1, vars][[2]]]
AppendTo[MK, CoefficientArrays[v2, vars][[2]]]
AppendTo[MK, CoefficientArrays[v3, vars][[2]]]
AppendTo[MK, CoefficientArrays[v4, vars][[2]]]
AppendTo[MK, CoefficientArrays[v5, vars][[2]]]
AppendTo[MK, CoefficientArrays[v6, vars][[2]]]
AppendTo[MK, CoefficientArrays[v7, vars][[2]]]
AppendTo[MK, CoefficientArrays[v8, vars][[2]]]
AppendTo[MK, CoefficientArrays[v9, vars][[2]]]
AppendTo[MK, CoefficientArrays[v10, vars][[2]]]
AppendTo[MK, CoefficientArrays[v11, vars][[2]]]
AppendTo[MK, CoefficientArrays[v12, vars][[2]]]
AppendTo[MK, CoefficientArrays[v13, vars][[2]]]
AppendTo[MK, CoefficientArrays[v14, vars][[2]]]
AppendTo[MK, CoefficientArrays[v15, vars][[2]]]
AppendTo[MK, CoefficientArrays[v16, vars][[2]]]
AppendTo[MK, CoefficientArrays[v17, vars][[2]]]
AppendTo[MK, CoefficientArrays[v18, vars][[2]]]
AppendTo[MK, CoefficientArrays[v19, vars][[2]]]
AppendTo[MK, CoefficientArrays[v20, vars][[2]]]
AppendTo[MK, CoefficientArrays[v21, vars][[2]]]
AppendTo[MK, CoefficientArrays[v22, vars][[2]]]
AppendTo[MK, CoefficientArrays[v23, vars][[2]]]
AppendTo[MK, CoefficientArrays[v24, vars][[2]]]
AppendTo[MK, CoefficientArrays[v25, vars][[2]]]
AppendTo[MK, CoefficientArrays[v26, vars][[2]]]
AppendTo[MK, CoefficientArrays[v27, vars][[2]]]
AppendTo[MK, CoefficientArrays[v28, vars][[2]]]

mat := NullSpace[Transpose[MK]]

Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[21]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[20]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[19]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[18]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[17]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[16]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[15]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[14]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[13]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[12]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[11]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[10]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[9]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[8]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[7]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[6]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[5]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[4]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[3]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[2]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28})[[1]]]]]]
