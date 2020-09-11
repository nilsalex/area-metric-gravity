s1 = 2 k6 + 3/2 k7
s2 = -1/2 k6 - 3/8 k7
s3 = 3/2 k6 + 9/8 k7 - 6 k12 - 2 k14
s4 = -1/2 k6 - 3/8 k7 - 1/2 k14
s5 = 1/6 k6 + 1/8 k7 + 1/6 k14
s6 = k6 + 3/4 k7 - 3 k12 - k14 - 6 k16
s7 = -1/3 k6 - 1/4 k7 + k12 + 1/3 k14 + 2 k16

s8 = -2 k14
s9 = -1/2 k14
s10 = -3/2 k14
s11 = 1/2 k6 + 11/8 k7 + 2 k8 - 2 k13 - 1/2 k14
s12 = -1/2 k6 - 11/8 k7 - 2 k8 + 2 k13 + 7/6 k14
s13 = -2 k2
s14 = -2 k4 + 24 k5 - k6 - 3/4 k7 + 4 k8 - 12 k9 + 24 k10 - 24 k11 - 6 k12 - 4 k13 - 2 k14 - 48 k15 - 12 k16
s15 = 2 k4 - 24 k5 + k6 + 3/4 k7 - 4 k8 + 12 k9 - 24 k10 + 24 k11 + 6 k12 + 4 k13 + 2 k14 + 48 k15 + 12 k16
s16 = -24 k1 - 4 k2 - 24 k3

s17 = 4 k6 + 3 k7 - 12 k12 - 4 k14 - 24 k16
s18 = k6 + 3/4 k7 - 3 k12 - k14 - 6 k16
s19 = 3 k6 + 9/4 k7 - 9 k12 - 3 k14 - 18 k16
s20 = -2 k4 + 24 k5 - 2 k6 - 3/2 k7 + 4 k8 - 12 k9 + 24 k10 - 24 k11 - 3 k12 - 4 k13 - k14 - 48 k15 - 6 k16
s21 = 2 k4 - 24 k5 + 2/3 k6 + 1/2 k7 - 4 k8 + 12 k9 - 24 k10 + 24 k11 + 7 k12 + 4 k13 + 7/3 k14 + 48 k15 + 14 k16
s22 = -24 k1 - 4 k2 - 24 k3
s23 = -1/2 k6 - 11/8 k7 - 2 k8 + 2 k13 + k14
s24 = 1/2 k6 + 11/8 k7 + 2 k8 - 2 k13 - k14
s25 = 2 k2

s26 = -4/3 k6 - k7
s27 = -k6 - 3/4 k7
s28 = 1/3 k6 + 1/4 k7
s29 = -6 k12 - 2 k14
s30 = -k6 - 3/4 k7 + 4 k12 + 4/3 k14
s31 = 2/3 k6 + 1/2 k7
s32 = -1/9 k6 - 1/12 k7 - 1/9 k14
s33 = 2/9 k6 + 1/6 k7 - 2/3 k12 - 2/9 k14 - 4/3 k16

s34 = -8 k12 - 8/3 k14
s35 = -6 k12 - 2 k14
s36 = -k6 - 3/4 k7 + 4 k12 + 4/3 k14
s37 = -24 k5 + 2 k6 + 5/2 k7 - 4 k8 + 24 k11 - 12 k12 + 4 k13 - 4 k14
s38 = 24 k5 - 2 k6 - 5/2 k7 + 4 k8 - 24 k11 - 4 k13
s39 = 24 k1 + 4 k2
s40 = 4 k12 + 4/3 k14
s41 = 1/3 k6 + 1/4 k7 - 4/3 k12 - 7/9 k14
s42 = 2/3 k6 + 1/2 k7 - 2 k12 - 2/3 k14 - 4 k16

s43 = -4 k6 - 3 k7
s44 = -24 k12 - 8 k14
s45 = 4/3 k6 + k7 - 4/3 k14
s46 = 8/3 k6 + 2 k7 - 8 k12 - 8/3 k14 - 16 k16

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
