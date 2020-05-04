k14 = 0
k16 = 1/6 k6 + 1/8 k7 - 1/2 k12

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

vars = {k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k15}

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

Print["v1 = "<>ToString[InputForm[Expand[v1]]]]
Print["v2 = "<>ToString[InputForm[Expand[v2]]]]
Print["v3 = "<>ToString[InputForm[Expand[v3]]]]
Print["v4 = "<>ToString[InputForm[Expand[v4]]]]
Print["v5 = "<>ToString[InputForm[Expand[v5]]]]
Print["v6 = "<>ToString[InputForm[Expand[v6]]]]
Print["v7 = "<>ToString[InputForm[Expand[v7]]]]
Print["v8 = "<>ToString[InputForm[Expand[v8]]]]
Print["v9 = "<>ToString[InputForm[Expand[v9]]]]
Print["v10 = "<>ToString[InputForm[Expand[v10]]]]
Print["v11 = "<>ToString[InputForm[Expand[v11]]]]
Print["v12 = "<>ToString[InputForm[Expand[v12]]]]
Print["v13 = "<>ToString[InputForm[Expand[v13]]]]
Print["v14 = "<>ToString[InputForm[Expand[v14]]]]
Print["v15 = "<>ToString[InputForm[Expand[v15]]]]
Print["v16 = "<>ToString[InputForm[Expand[v16]]]]
Print["v17 = "<>ToString[InputForm[Expand[v17]]]]
Print["v18 = "<>ToString[InputForm[Expand[v18]]]]
Print["v19 = "<>ToString[InputForm[Expand[v19]]]]
Print["v20 = "<>ToString[InputForm[Expand[v20]]]]
Print["v21 = "<>ToString[InputForm[Expand[v21]]]]
Print["v22 = "<>ToString[InputForm[Expand[v22]]]]
Print["v23 = "<>ToString[InputForm[Expand[v23]]]]
Print["v24 = "<>ToString[InputForm[Expand[v24]]]]
Print["v25 = "<>ToString[InputForm[Expand[v25]]]]
Print["v26 = "<>ToString[InputForm[Expand[v26]]]]
Print["v27 = "<>ToString[InputForm[Expand[v27]]]]
Print["v28 = "<>ToString[InputForm[Expand[v28]]]]
