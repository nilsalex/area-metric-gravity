k15 = -16 k9
k16 = -8 k13

v1 = -1/8 k15
v2 = k9
v3 = -4 k13 - 1/2 k16
v4 = 4 k13 + 1/2 k16
v5 = k9 + 1/16 k15

v6 = 2 k9 + 1/8 k15
v7 = 8 k13 + k16
v8 = 3 k4 - 12 k5 + 24 k6 + 16 k7 + 8 k8 + k9 + 12 k10 + 16 k12 + 8 k13 + 96 k14 + 1/16 k15 + 2 k16
v9 = -3 k4 + 12 k5 - 24 k6 - 16 k7 - 8 k8 - 12 k10 - 16 k12 - 8 k13 - 96 k14 - 2 k16
v10 = 4 k13 + 1/2 k16
v11 = 12 k1 + 48 k2 + 16 k3
v12 = 16 k7 - 16 k8 + 16 k12 + 8 k13 + k16
v13 = -16 k7 + 16 k8 - 16 k12 - 8 k13 - k16
v14 = 16 k3

v15 = 8 k13 + k16
v16 = -2 k9 - 1/8 k15
v17 = 16 k7 - 16 k8 + 16 k12 + 12 k13 + 3/2 k16
v18 = -16 k7 + 16 k8 - 16 k12 - 8 k13 - k16
v19 = -k9 - 1/16 k15
v20 = 16 k3
v21 = -3 k4 + 12 k5 - 24 k6 - 16 k7 - 8 k8 - 12 k10 - 16 k12 - 8 k13 - 96 k14 - 2 k16
v22 = 3 k4 - 12 k5 + 24 k6 + 16 k7 + 8 k8 + 12 k10 + 16 k12 + 8 k13 + 96 k14 + 2 k16
v23 = -12 k1 - 48 k2 - 16 k3

v24 = -1/4 k15
v25 = 2 k9
v26 = -8 k13 - k16
v27 = 8 k13 + k16
v28 = 2 k9 + 1/8 k15

vars = {k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14}

MK = {}

AppendTo[MK, CoefficientArrays[v1, vars][[2]]]
AppendTo[MK, CoefficientArrays[v2, vars][[2]]]
AppendTo[MK, CoefficientArrays[v8, vars][[2]]]
AppendTo[MK, CoefficientArrays[v9, vars][[2]]]
AppendTo[MK, CoefficientArrays[v11, vars][[2]]]
AppendTo[MK, CoefficientArrays[v12, vars][[2]]]
AppendTo[MK, CoefficientArrays[v13, vars][[2]]]
AppendTo[MK, CoefficientArrays[v14, vars][[2]]]
AppendTo[MK, CoefficientArrays[v17, vars][[2]]]
AppendTo[MK, CoefficientArrays[v18, vars][[2]]]
AppendTo[MK, CoefficientArrays[v20, vars][[2]]]
AppendTo[MK, CoefficientArrays[v21, vars][[2]]]
AppendTo[MK, CoefficientArrays[v22, vars][[2]]]
AppendTo[MK, CoefficientArrays[v23, vars][[2]]]
AppendTo[MK, CoefficientArrays[v24, vars][[2]]]
AppendTo[MK, CoefficientArrays[v25, vars][[2]]]

mat := NullSpace[Transpose[MK]]

Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x8, x9, x11, x12, x13, x14, x17, x18, x20, x21, x22, x23, x24, x25})[[11]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x8, x9, x11, x12, x13, x14, x17, x18, x20, x21, x22, x23, x24, x25})[[10]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x8, x9, x11, x12, x13, x14, x17, x18, x20, x21, x22, x23, x24, x25})[[9]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x8, x9, x11, x12, x13, x14, x17, x18, x20, x21, x22, x23, x24, x25})[[8]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x8, x9, x11, x12, x13, x14, x17, x18, x20, x21, x22, x23, x24, x25})[[7]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x8, x9, x11, x12, x13, x14, x17, x18, x20, x21, x22, x23, x24, x25})[[6]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x8, x9, x11, x12, x13, x14, x17, x18, x20, x21, x22, x23, x24, x25})[[5]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x8, x9, x11, x12, x13, x14, x17, x18, x20, x21, x22, x23, x24, x25})[[4]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x8, x9, x11, x12, x13, x14, x17, x18, x20, x21, x22, x23, x24, x25})[[3]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x8, x9, x11, x12, x13, x14, x17, x18, x20, x21, x22, x23, x24, x25})[[2]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x8, x9, x11, x12, x13, x14, x17, x18, x20, x21, x22, x23, x24, x25})[[1]]]]]]

Print["v1 = "<>ToString[InputForm[v1]]]
Print["v2 = "<>ToString[InputForm[v2]]]
Print["v3 = "<>ToString[InputForm[v3]]]
Print["v4 = "<>ToString[InputForm[v4]]]
Print["v5 = "<>ToString[InputForm[v5]]]
Print["v6 = "<>ToString[InputForm[v6]]]
Print["v7 = "<>ToString[InputForm[v7]]]
Print["v8 = "<>ToString[InputForm[v8]]]
Print["v9 = "<>ToString[InputForm[v9]]]
Print["v10 = "<>ToString[InputForm[v10]]]
Print["v11 = "<>ToString[InputForm[v11]]]
Print["v12 = "<>ToString[InputForm[v12]]]
Print["v13 = "<>ToString[InputForm[v13]]]
Print["v14 = "<>ToString[InputForm[v14]]]
Print["v15 = "<>ToString[InputForm[v15]]]
Print["v16 = "<>ToString[InputForm[v16]]]
Print["v17 = "<>ToString[InputForm[v17]]]
Print["v18 = "<>ToString[InputForm[v18]]]
Print["v19 = "<>ToString[InputForm[v19]]]
Print["v20 = "<>ToString[InputForm[v20]]]
Print["v21 = "<>ToString[InputForm[v21]]]
Print["v22 = "<>ToString[InputForm[v22]]]
Print["v23 = "<>ToString[InputForm[v23]]]
Print["v24 = "<>ToString[InputForm[v24]]]
Print["v25 = "<>ToString[InputForm[v25]]]
Print["v26 = "<>ToString[InputForm[v26]]]
Print["v27 = "<>ToString[InputForm[v27]]]
Print["v28 = "<>ToString[InputForm[v28]]]
