s1 = -1/8 k15
s2 = 1/32 k15
s3 = 12 k11 + 4 k13 + 1/32 k15 + 1/2 k16
s4 = 1/2 k9 + 1/16 k15
s5 = -1/6 k9 - 1/48 k15
s6 = 2 k13 + 1/4 k16
s7 = -2/3 k13 - 1/12 k16

s8 = 2 k9 + 1/8 k15
s9 = 1/2 k9 + 1/32 k15
s10 = 3/2 k9 + 3/32 k15
s11 = 3/2 k4 - 6 k5 + 12 k6 + 8 k7 + 4 k8 - 1/2 k9 + 6 k10 + 8 k12 + 4 k13 + 48 k14 - 1/32 k15 + k16
s12 = -3/2 k4 + 6 k5 - 12 k6 - 8 k7 - 4 k8 - 1/6 k9 - 6 k10 - 8 k12 - 4 k13 - 48 k14 - 1/96 k15 - k16
s13 = 6 k1 + 24 k2 + 8 k3
s14 = 8 k7 - 8 k8 + 8 k12 + 4 k13 + 1/2 k16
s15 = -8 k7 + 8 k8 - 8 k12 - 4 k13 - 1/2 k16
s16 = 8 k3

s17 = 8 k13 + k16
s18 = 2 k13 + 1/4 k16
s19 = 6 k13 + 3/4 k16
s20 = 8 k7 - 8 k8 + 8 k12 + 2 k13 + 1/4 k16
s21 = -8 k7 + 8 k8 - 8 k12 - 14/3 k13 - 7/12 k16
s22 = 8 k3
s23 = -3/2 k4 + 6 k5 - 12 k6 - 8 k7 - 4 k8 - 6 k10 - 8 k12 - 4 k13 - 48 k14 - k16
s24 = 3/2 k4 - 6 k5 + 12 k6 + 8 k7 + 4 k8 + 6 k10 + 8 k12 + 4 k13 + 48 k14 + k16
s25 = -6 k1 - 24 k2 - 8 k3

s26 = 1/12 k15
s27 = 1/16 k15
s28 = -1/48 k15
s29 = 12 k11 + 4 k13 + 1/8 k15 + 1/2 k16
s30 = -8 k11 - 8/3 k13 - 1/48 k15 - 1/3 k16
s31 = -1/24 k15
s32 = 1/9 k9 + 1/72 k15
s33 = 4/9 k13 + 1/18 k16

s34 = 16 k11 + 16/3 k13 + 1/6 k15 + 2/3 k16
s35 = 12 k11 + 4 k13 + 1/8 k15 + 1/2 k16
s36 = -8 k11 - 8/3 k13 - 1/48 k15 - 1/3 k16
s37 = 24 k6 + 16 k7 + 8 k8 + 48 k11 - 8 k12 + 12 k13 - 48 k14 + 1/4 k15 + 5/2 k16
s38 = -24 k6 - 16 k7 - 8 k8 - 24 k11 + 8 k12 - 4 k13 + 48 k14 - 3/2 k16
s39 = -24 k2 - 8 k3
s40 = -8 k11 - 8/3 k13 - 1/12 k15 - 1/3 k16
s41 = 1/3 k9 + 8/3 k11 + 8/9 k13 + 1/36 k15 + 1/9 k16
s42 = 4/3 k13 + 1/6 k16

s43 = 1/4 k15
s44 = 48 k11 + 16 k13 + 1/2 k15 + 2 k16
s45 = 4/3 k9
s46 = 16/3 k13 + 2/3 k16

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
AppendTo[MK, CoefficientArrays[s16, vars][[2]]]
AppendTo[MK, CoefficientArrays[s17, vars][[2]]]
AppendTo[MK, CoefficientArrays[s18, vars][[2]]]
AppendTo[MK, CoefficientArrays[s19, vars][[2]]]
AppendTo[MK, CoefficientArrays[s20, vars][[2]]]
AppendTo[MK, CoefficientArrays[s21, vars][[2]]]
AppendTo[MK, CoefficientArrays[s22, vars][[2]]]
AppendTo[MK, CoefficientArrays[s23, vars][[2]]]
AppendTo[MK, CoefficientArrays[s24, vars][[2]]]
AppendTo[MK, CoefficientArrays[s25, vars][[2]]]
AppendTo[MK, CoefficientArrays[s26, vars][[2]]]
AppendTo[MK, CoefficientArrays[s27, vars][[2]]]
AppendTo[MK, CoefficientArrays[s28, vars][[2]]]
AppendTo[MK, CoefficientArrays[s29, vars][[2]]]
AppendTo[MK, CoefficientArrays[s30, vars][[2]]]
AppendTo[MK, CoefficientArrays[s31, vars][[2]]]
AppendTo[MK, CoefficientArrays[s32, vars][[2]]]
AppendTo[MK, CoefficientArrays[s33, vars][[2]]]
AppendTo[MK, CoefficientArrays[s34, vars][[2]]]
AppendTo[MK, CoefficientArrays[s35, vars][[2]]]
AppendTo[MK, CoefficientArrays[s36, vars][[2]]]
AppendTo[MK, CoefficientArrays[s37, vars][[2]]]
AppendTo[MK, CoefficientArrays[s38, vars][[2]]]
AppendTo[MK, CoefficientArrays[s39, vars][[2]]]
AppendTo[MK, CoefficientArrays[s40, vars][[2]]]
AppendTo[MK, CoefficientArrays[s41, vars][[2]]]
AppendTo[MK, CoefficientArrays[s42, vars][[2]]]
AppendTo[MK, CoefficientArrays[s43, vars][[2]]]
AppendTo[MK, CoefficientArrays[s44, vars][[2]]]
AppendTo[MK, CoefficientArrays[s45, vars][[2]]]
AppendTo[MK, CoefficientArrays[s46, vars][[2]]]

mat := NullSpace[Transpose[MK]]

Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[36]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[35]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[34]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[33]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[32]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[31]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[30]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[29]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[28]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[27]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[26]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[25]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[24]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[23]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[22]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[21]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[20]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[19]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[18]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[17]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[16]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[15]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[14]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[13]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[12]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[11]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[10]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[9]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[8]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[7]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[6]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[5]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[4]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[3]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[2]]]]]]
Print["0 = "<>ToString[InputForm[Expand[-(mat.{x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35, x36, x37, x38, x39, x40, x41, x42, x43, x44, x45, x46})[[1]]]]]]
