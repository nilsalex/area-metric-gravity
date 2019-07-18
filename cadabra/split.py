from cadabra2 import *

Indices(Ex(r'''{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z#}'''), Ex(r'''fourD, position=independent''') )
Integer(Ex(r'''{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z#}'''), Ex(r'''0..4''') )

Indices(Ex(r'''{\alpha,\beta,\gamma,\delta,\epsilon,\zeta,\theta,\iota,\kappa,\lambda,\mu,\nu,\rho,\sigma,\tau#}'''), Ex(r'''threeD, position=independent, parent=fourD''') )
Integer(Ex(r'''{\alpha,\beta,\gamma,\delta,\epsilon,\zeta,\theta,\iota,\kappa,\lambda,\mu,\nu,\rho,\sigma,\tau#}'''), Ex(r'''1..3''') )

KroneckerDelta(Ex(r'''\delta{#}'''), Ex(r'''''') )
Symmetric(Ex(r'''\gamma_{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''\gamma^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''X^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''Y^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''Z^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''U^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''dU^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''V^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''dV^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''W^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''dW^{\alpha \beta}'''), Ex(r'''''') )
EpsilonTensor(Ex(r'''\epsilon_{\alpha \beta \gamma}'''), Ex(r'''''') )
EpsilonTensor(Ex(r'''\epsilon^{\alpha \beta \gamma}'''), Ex(r'''''') )

Symmetric(Ex(r'''\eta^{a? b?}'''), Ex(r'''''') )
AntiSymmetric(Ex(r'''\epsilon^{a? b? c? d?}'''), Ex(r'''''') )

PartialDerivative(Ex(r'''\partial{#}'''), Ex(r''')''') )
Depends(Ex(r'''H{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''H1{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''H2{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''H3{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''X{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''Y{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''Z{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''U{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dU{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''V{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dV{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''W{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dW{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''B{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dB{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''A'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dA'''), Ex(r'''\partial{#})''') )

SortOrder(Ex(r'''{dU{#},dV{#},dW{#},dB{#},dA,m{#},k{#},t{#},e{#},A,B{#},X{#},Y{#},Z{#},U{#},V{#},W{#},\partial{#},\epsilon{#},\gamma{#}}'''), Ex(r''')''') )

ruleH1  = Ex(r''' H1_{\mu \nu} ->-2*A*\gamma_{\mu \nu} + \gamma_{\mu \rho} \gamma_{\nu \sigma} X^{\rho \sigma}''')
#ruleH2  = Ex(r''' H2_{\mu \nu \rho} ->B^{\sigma} \gamma_{\sigma \nu} \gamma_{\mu \rho} - B^{\sigma} \gamma_{\sigma \rho} \gamma_{\mu \nu} + ((1/2) * \gamma_{\sigma \tau} X^{\sigma \tau} - A) * \epsilon_{\mu \nu \rho} + \epsilon_{\alpha \nu \rho} * \gamma_{\mu \sigma} Z^{\sigma \alpha}''')
ruleH2  = Ex(r''' H2_{\mu \nu \rho} ->B^{\sigma} \gamma_{\sigma \nu} \gamma_{\mu \rho} - B^{\sigma} \gamma_{\sigma \rho} \gamma_{\mu \nu} + \epsilon_{\alpha \nu \rho} * \gamma_{\mu \sigma} Z^{\sigma \alpha}''')
#ruleH3  = Ex(r''' H3_{\mu \nu \rho \sigma} -> (\gamma_{\alpha \mu} \epsilon_{\nu \rho \sigma} - \gamma_{\alpha \nu} \epsilon_{\mu \rho \sigma} + \gamma_{\alpha \rho} \epsilon_{\sigma \mu \nu} - \gamma_{\alpha \sigma} \epsilon_{\rho \mu \nu}) B^{\alpha} - (\gamma_{\mu \rho} \gamma_{\nu \sigma} - \gamma_{\mu \sigma} \gamma_{\nu \rho}) * \gamma_{\alpha \beta} X^{\alpha \beta} - \epsilon_{\alpha \mu \nu} \epsilon_{\beta \rho \sigma} Y^{\alpha \beta}''')
ruleH3  = Ex(r''' H3_{\mu \nu \rho \sigma} -> - (\gamma_{\mu \rho} \gamma_{\nu \sigma} - \gamma_{\mu \sigma} \gamma_{\nu \rho}) * \gamma_{\alpha \beta} X^{\alpha \beta} - \epsilon_{\alpha \mu \nu} \epsilon_{\beta \rho \sigma} Y^{\alpha \beta}''')

ruleEta00  = Ex(r''' \eta^{0 0} -> 1''')
ruleEta0a1  = Ex(r''' \eta^{0 \alpha} -> 0''')
ruleEta0a2  = Ex(r''' \eta^{\alpha 0} -> 0''')
ruleEtaab  = Ex(r''' \eta^{\alpha \beta} -> -\gamma^{\alpha \beta}''')

ruleTraceFree1  = Ex(r''' \gamma_{\alpha \beta} W^{\alpha \beta} -> 0''')
ruleTraceFree2  = Ex(r''' \gamma_{\alpha \beta} \partial_{p?}{W^{\alpha \beta}} -> 0''')
ruleTraceFree3  = Ex(r''' \gamma_{\alpha \beta} \partial_{p? q?}{W^{\alpha \beta}} -> 0''')

ruleX  = Ex(r''' X^{\alpha \beta} -> (1/2) * (U^{\alpha \beta} + V^{\alpha \beta})''')
ruleY  = Ex(r''' Y^{\alpha \beta} -> (-1/2) * (U^{\alpha \beta} - V^{\alpha \beta})''')
ruleZ  = Ex(r''' Z^{\alpha \beta} -> (1/2) * W^{\alpha \beta}''')

ruleEps0000  = Ex(r''' \epsilon^{0 0 0 0} -> 0''')
ruleEps000a1  = Ex(r''' \epsilon^{0 0 0 \alpha} -> 0''')
ruleEps000a2  = Ex(r''' \epsilon^{0 0 \alpha 0} -> 0''')
ruleEps000a3  = Ex(r''' \epsilon^{0 \alpha 0 0} -> 0''')
ruleEps000a4  = Ex(r''' \epsilon^{\alpha 0 0 0} -> 0''')
ruleEps00ab1  = Ex(r''' \epsilon^{0 0 \alpha \beta} -> 0''')
ruleEps00ab2  = Ex(r''' \epsilon^{0 \alpha 0 \beta} -> 0''')
ruleEps00ab3  = Ex(r''' \epsilon^{0 \alpha \beta 0} -> 0''')
ruleEps00ab4  = Ex(r''' \epsilon^{\alpha 0 0 \beta} -> 0''')
ruleEps00ab5  = Ex(r''' \epsilon^{\alpha 0 \beta 0} -> 0''')
ruleEps00ab6  = Ex(r''' \epsilon^{\alpha \beta 0 0} -> 0''')
ruleEps0abc1  = Ex(r''' \epsilon^{0 \alpha \beta \gamma} -> -\epsilon^{\alpha \beta \gamma}''')
ruleEps0abc2  = Ex(r''' \epsilon^{\alpha 0 \beta \gamma} -> \epsilon^{\alpha \beta \gamma}''')
ruleEps0abc3  = Ex(r''' \epsilon^{\alpha \beta 0 \gamma} -> -\epsilon^{\alpha \beta \gamma}''')
ruleEps0abc4  = Ex(r''' \epsilon^{\alpha \beta \gamma 0} -> \epsilon^{\alpha \beta \gamma}''')
ruleEpsabcd  = Ex(r''' \epsilon^{\alpha \beta \gamma \delta} -> 0''')

rulegg1  = Ex(r''' \gamma^{\mu \nu} \gamma_{\mu \nu} -> 3''')
rulegg2  = Ex(r''' \gamma^{\mu \nu} \gamma_{\nu \mu} -> 3''')
rulegg3  = Ex(r''' \gamma^{\mu \nu} \gamma_{\mu \rho} -> \delta^{\nu}_{\rho}''')
rulegg4  = Ex(r''' \gamma^{\mu \nu} \gamma_{\rho \mu} -> \delta^{\nu}_{\rho}''')
rulegg5  = Ex(r''' \gamma^{\nu \mu} \gamma_{\mu \rho} -> \delta^{\nu}_{\rho}''')
rulegg6  = Ex(r''' \gamma^{\nu \mu} \gamma_{\rho \mu} -> \delta^{\nu}_{\rho}''')

ruleEpsToDelta1  = Ex(r''' \epsilon_{a? b? c?} \epsilon_{i? j? k?} ->\gamma_{a? i?} \gamma_{b? j?} \gamma_{c? k?} - \gamma_{a? i?} \gamma_{b? k?} \gamma_{c? j?} - \gamma_{a? j?} \gamma_{b? i?} \gamma_{c? k?} + \gamma_{a? j?} \gamma_{b? k?} \gamma_{c? i?} + \gamma_{a? k?} \gamma_{b? i?} \gamma_{c? j?} - \gamma_{a? k?} \gamma_{b? j?} \gamma_{c? i?}''')

ruleEpsToDelta2  = Ex(r''' \epsilon^{a? b? c?} \epsilon^{i? j? k?} ->\gamma^{a? i?} \gamma^{b? j?} \gamma^{c? k?} - \gamma^{a? i?} \gamma^{b? k?} \gamma^{c? j?} - \gamma^{a? j?} \gamma^{b? i?} \gamma^{c? k?} + \gamma^{a? j?} \gamma^{b? k?} \gamma^{c? i?} + \gamma^{a? k?} \gamma^{b? i?} \gamma^{c? j?} - \gamma^{a? k?} \gamma^{b? j?} \gamma^{c? i?}''')

ruleEpsToDelta3  = Ex(r''' \epsilon^{a? b? c?} \epsilon_{i? j? k?} ->\delta^{a?}_{i?} \delta^{b?}_{j?} \delta^{c?}_{k?} - \delta^{a?}_{i?} \delta^{b?}_{k?} \delta^{c?}_{j?} - \delta^{a?}_{j?} \delta^{b?}_{i?} \delta^{c?}_{k?} + \delta^{a?}_{j?} \delta^{b?}_{k?} \delta^{c?}_{i?} + \delta^{a?}_{k?} \delta^{b?}_{i?} \delta^{c?}_{j?} - \delta^{a?}_{k?} \delta^{b?}_{j?} \delta^{c?}_{i?}''')

allE = Ex(r'''e{1}, e{2}, e{3}, e{4}, e{5}, e{6}, e{7}, e{8}, e{9}, e{10}, e{11}, e{12}, e{13}, e{14}, e{15}, e{16}, e{17}, e{18}, e{19}, e{20}, e{21}, e{22}, e{23}, e{24}, e{25}, e{26}, e{27}, e{28}, e{29}, e{30}, e{31}, e{32}, e{33}, e{34}, e{35}, e{36}, e{37}, e{38}, e{39}, e{40}''')

def my_eliminate_metric(ex, repeat=False):
    substitute(ex, Ex(r'''\delta_{\alpha \beta} -> \gamma_{\alpha \beta}''', False), repeat=repeat)
    substitute(ex, Ex(r'''\delta^{\alpha \beta} -> \gamma^{\alpha \beta}''', False), repeat=repeat)
    substitute(ex, rulegg1, repeat=repeat)
    substitute(ex, rulegg2, repeat=repeat)
    substitute(ex, rulegg3, repeat=repeat)
    substitute(ex, rulegg4, repeat=repeat)
    substitute(ex, rulegg5, repeat=repeat)
    substitute(ex, rulegg6, repeat=repeat)
    return ex

def my_epsilon_to_delta(ex, repeat=False):
    substitute(ex, ruleEpsToDelta3)
    substitute(ex, ruleEpsToDelta1)
    substitute(ex, ruleEpsToDelta2)
    return ex

def kin_ABI():
    ruleM1  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? c?} \eta^{b? d?} \eta^{e? g?} \eta^{f? h?} \eta^{i? j?}''')
    ruleM2  = Ex(r''' M{2}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? c?} \eta^{b? d?} \eta^{e? g?} \eta^{f? i?} \eta^{h? j?}''')
    ruleM3  = Ex(r''' M{3}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? c?} \eta^{b? e?} \eta^{d? g?} \eta^{f? h?} \eta^{i? j?}''')
    ruleM4  = Ex(r''' M{4}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? c?} \eta^{b? e?} \eta^{d? g?} \eta^{f? i?} \eta^{h? j?}''')
    ruleM5  = Ex(r''' M{5}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? c?} \eta^{b? i?} \eta^{d? j?} \eta^{e? g?} \eta^{f? h?}''')
    ruleM6  = Ex(r''' M{6}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? e?} \eta^{b? f?} \eta^{c? g?} \eta^{d? h?} \eta^{i? j?}''')
    ruleM7  = Ex(r''' M{7}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? e?} \eta^{b? f?} \eta^{c? g?} \eta^{d? i?} \eta^{h? j?}''')
    ruleM8  = Ex(r''' M{8}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? e?} \eta^{b? g?} \eta^{c? f?} \eta^{d? h?} \eta^{i? j?}''')
    ruleM9  = Ex(r''' M{9}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? e?} \eta^{b? i?} \eta^{c? g?} \eta^{d? j?} \eta^{f? h?}''')
    ruleM10  = Ex(r''' M{10}^{a? b? c? d? e? f? g? h? i? j?} ->\epsilon^{a? b? c? d?} \eta^{e? g?} \eta^{f? h?} \eta^{i? j?}''')
    ruleM11  = Ex(r''' M{11}^{a? b? c? d? e? f? g? h? i? j?} ->\epsilon^{a? b? c? d?} \eta^{e? g?} \eta^{f? i?} \eta^{h? j?}''')
    ruleM12  = Ex(r''' M{12}^{a? b? c? d? e? f? g? h? i? j?} ->\epsilon^{a? b? e? f?} \eta^{c? g?} \eta^{d? h?} \eta^{i? j?}''')
    ruleM13  = Ex(r''' M{13}^{a? b? c? d? e? f? g? h? i? j?} ->\epsilon^{a? b? e? f?} \eta^{c? g?} \eta^{d? i?} \eta^{h? j?}''')
    ruleM14  = Ex(r''' M{14}^{a? b? c? d? e? f? g? h? i? j?} ->\epsilon^{a? b? e? i?} \eta^{c? g?} \eta^{d? h?} \eta^{f? j?}''')
    ruleM15  = Ex(r''' M{15}^{a? b? c? d? e? f? g? h? i? j?} ->\epsilon^{e? f? g? h?} \eta^{a? c?} \eta^{b? d?} \eta^{i? j?}''')
    ruleM16  = Ex(r''' M{16}^{a? b? c? d? e? f? g? h? i? j?} ->\epsilon^{e? f? g? h?} \eta^{a? c?} \eta^{b? i?} \eta^{d? j?}''')
    
    ruleM  = Ex(r''' M^{a? b? c? d? e? f? g? h? i? j?} ->e{1} * M{1}^{a? b? c? d? e? f? g? h? i? j?} + e{2} * M{2}^{a? b? c? d? e? f? g? h? i? j?} + e{3} * M{3}^{a? b? c? d? e? f? g? h? i? j?} + e{4} * M{4}^{a? b? c? d? e? f? g? h? i? j?} + e{5} * M{5}^{a? b? c? d? e? f? g? h? i? j?} + e{6} * M{6}^{a? b? c? d? e? f? g? h? i? j?} + e{7} * M{7}^{a? b? c? d? e? f? g? h? i? j?} + e{8} * M{8}^{a? b? c? d? e? f? g? h? i? j?} + e{9} * M{9}^{a? b? c? d? e? f? g? h? i? j?} + e{10} * M{10}^{a? b? c? d? e? f? g? h? i? j?} + e{11} * M{11}^{a? b? c? d? e? f? g? h? i? j?} + e{12} * M{12}^{a? b? c? d? e? f? g? h? i? j?} + e{13} * M{13}^{a? b? c? d? e? f? g? h? i? j?} + e{14} * M{14}^{a? b? c? d? e? f? g? h? i? j?} + e{15} * M{15}^{a? b? c? d? e? f? g? h? i? j?} + e{16} * M{16}^{a? b? c? d? e? f? g? h? i? j?}''')
    
    ruleMH1  = Ex(r''' M^{a b c d e? f? g? h? i? j?} H_{a b c d} ->(M^{0 \mu 0 \nu e? f? g? h? i? j?} - M^{0 \mu \nu 0 e? f? g? h? i? j?} - M^{\mu 0 0 \nu e? f? g? h? i? j?} + M^{\mu 0 \nu 0 e? f? g? h? i? j?}) H1_{\mu \nu} + (M^{0 \mu \nu \rho e? f? g? h? i? j?} - M^{\mu 0 \nu \rho e? f? g? h? i? j?} + M^{\nu \rho 0 \mu e? f? g? h? i? j?} - M^{\nu \rho \mu 0 e? f? g? h? i? j?}) H2_{\mu \nu \rho} + M^{\mu \nu \rho \sigma e? f? g? h? i? j?} H3_{\mu \nu \rho \sigma}''')
    
    ruleMH2  = Ex(r''' M^{e? f? g? h? a b c d p q} \partial_{p q}{H_{a b c d}} ->(M^{e? f? g? h? 0 \mu 0 \nu 0 0} - M^{e? f? g? h? 0 \mu \nu 0 0 0} - M^{e? f? g? h? \mu 0 0 \nu 0 0} + M^{e? f? g? h? \mu 0 \nu 0 0 0}) \partial_{0 0}{H1_{\mu \nu}} + (M^{e? f? g? h? 0 \mu 0 \nu 0 \alpha} - M^{e? f? g? h? 0 \mu \nu 0 0 \alpha} - M^{e? f? g? h? \mu 0 0 \nu 0 \alpha} + M^{e? f? g? h? \mu 0 \nu 0 0 \alpha}) \partial_{0 \alpha}{H1_{\mu \nu}} + (M^{e? f? g? h? 0 \mu 0 \nu \alpha 0} - M^{e? f? g? h? 0 \mu \nu 0 \alpha 0} - M^{e? f? g? h? \mu 0 0 \nu \alpha 0} + M^{e? f? g? h? \mu 0 \nu 0 \alpha 0}) \partial_{0 \alpha}{H1_{\mu \nu}} + (M^{e? f? g? h? 0 \mu 0 \nu \alpha \beta} - M^{e? f? g? h? 0 \mu \nu 0 \alpha \beta} - M^{e? f? g? h? \mu 0 0 \nu \alpha \beta} + M^{e? f? g? h? \mu 0 \nu 0 \alpha \beta}) \partial_{\alpha \beta}{H1_{\mu \nu}} + (M^{e? f? g? h? 0 \mu \nu \rho 0 0} - M^{e? f? g? h? \mu 0 \nu \rho 0 0} + M^{e? f? g? h? \nu \rho 0 \mu 0 0} - M^{e? f? g? h? \nu \rho \mu 0 0 0}) \partial_{0 0}{H2_{\mu \nu \rho}} + (M^{e? f? g? h? 0 \mu \nu \rho 0 \alpha} - M^{e? f? g? h? \mu 0 \nu \rho 0 \alpha} + M^{e? f? g? h? \nu \rho 0 \mu 0 \alpha} - M^{e? f? g? h? \nu \rho \mu 0 0 \alpha}) \partial_{0 \alpha}{H2_{\mu \nu \rho}} + (M^{e? f? g? h? 0 \mu \nu \rho \alpha 0} - M^{e? f? g? h? \mu 0 \nu \rho \alpha 0} + M^{e? f? g? h? \nu \rho 0 \mu \alpha 0} - M^{e? f? g? h? \nu \rho \mu 0 \alpha 0}) \partial_{0 \alpha}{H2_{\mu \nu \rho}} + (M^{e? f? g? h? 0 \mu \nu \rho \alpha \beta} - M^{e? f? g? h? \mu 0 \nu \rho \alpha \beta} + M^{e? f? g? h? \nu \rho 0 \mu \alpha \beta} - M^{e? f? g? h? \nu \rho \mu 0 \alpha \beta}) \partial_{\alpha \beta}{H2_{\mu \nu \rho}} + M^{e? f? g? h? \mu \nu \rho \sigma 0 0} \partial_{0 0}{H3_{\mu \nu \rho \sigma}} + M^{e? f? g? h? \mu \nu \rho \sigma 0 \alpha} \partial_{0 \alpha}{H3_{\mu \nu \rho \sigma}} + M^{e? f? g? h? \mu \nu \rho \sigma \alpha 0} \partial_{0 \alpha}{H3_{\mu \nu \rho \sigma}} + M^{e? f? g? h? \mu \nu \rho \sigma \alpha \beta} \partial_{\alpha \beta}{H3_{\mu \nu \rho \sigma}}''')
    
    ex  = Ex(r'''M^{a b c d e f g h i j} H_{a b c d} \partial_{i j}{H_{e f g h}}''')
    
    
    substitute(ex, ruleMH1)
    distribute(ex)
    substitute(ex, ruleMH2)
    distribute(ex)
    
    
    substitute(ex, ruleM)
    substitute(ex, ruleM1)
    substitute(ex, ruleM2)
    substitute(ex, ruleM3)
    substitute(ex, ruleM4)
    substitute(ex, ruleM5)
    substitute(ex, ruleM6)
    substitute(ex, ruleM7)
    substitute(ex, ruleM8)
    substitute(ex, ruleM9)
    substitute(ex, ruleM10)
    substitute(ex, ruleM11)
    substitute(ex, ruleM12)
    substitute(ex, ruleM13)
    substitute(ex, ruleM14)
    substitute(ex, ruleM15)
    substitute(ex, ruleM16)
    
    
    substitute(ex, ruleEta00)
    substitute(ex, ruleEta0a1)
    substitute(ex, ruleEta0a2)
    substitute(ex, ruleEtaab)
    
    
    substitute(ex, ruleEps0000)
    substitute(ex, ruleEps000a1)
    substitute(ex, ruleEps000a2)
    substitute(ex, ruleEps000a3)
    substitute(ex, ruleEps000a4)
    substitute(ex, ruleEps00ab1)
    substitute(ex, ruleEps00ab2)
    substitute(ex, ruleEps00ab3)
    substitute(ex, ruleEps00ab4)
    substitute(ex, ruleEps00ab5)
    substitute(ex, ruleEps00ab6)
    substitute(ex, ruleEps0abc1)
    substitute(ex, ruleEps0abc2)
    substitute(ex, ruleEps0abc3)
    substitute(ex, ruleEps0abc4)
    substitute(ex, ruleEpsabcd)
    
    
    substitute(ex, ruleH1)
    substitute(ex, ruleH2)
    substitute(ex, ruleH3)
    
    
    distribute(ex)
    unwrap(ex)
    
    
    my_epsilon_to_delta(ex)
    my_epsilon_to_delta(ex)
    my_epsilon_to_delta(ex)
    
    
    distribute(ex)
    
    rewrite_indices(ex, Ex(r'\epsilon_{\alpha \beta \gamma}'), Ex(r'\gamma^{\alpha \beta}'))

    my_eliminate_metric(ex)
    eliminate_kronecker(ex)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex)
    
    
    sort_product(ex)
    sort_sum(ex)
    
    
    canonicalise(ex)
    rename_dummies(ex)
    
    
    substitute(ex, ruleX)
    substitute(ex, ruleY)
    substitute(ex, ruleZ)
    
    
    unwrap(ex)
    distribute(ex)
    
    
    substitute(ex, ruleTraceFree1)
    substitute(ex, ruleTraceFree2)
    substitute(ex, ruleTraceFree3)
    
    distribute(ex)
    
    sort_product(ex)
    sort_sum(ex)
    canonicalise(ex)
    rename_dummies(ex)
    
    collect_terms(ex)
    
    return(ex)

def kin_ApBq():
    ruleM1  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? c?} \eta^{b? d?} \eta^{e? f?} \eta^{g? h?} \eta^{i? j?}''')
    ruleM2  = Ex(r''' M{2}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? c?} \eta^{b? d?} \eta^{e? j?} \eta^{f? h?} \eta^{g? i?}''')
    ruleM3  = Ex(r''' M{3}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? c?} \eta^{b? e?} \eta^{d? f?} \eta^{g? h?} \eta^{i? j?}''')
    ruleM4  = Ex(r''' M{4}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? c?} \eta^{b? f?} \eta^{d? h?} \eta^{e? j?} \eta^{g? i?}''')
    ruleM5  = Ex(r''' M{5}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? c?} \eta^{b? f?} \eta^{d? j?} \eta^{e? h?} \eta^{g? i?}''')
    ruleM6  = Ex(r''' M{6}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? e?} \eta^{b? f?} \eta^{c? h?} \eta^{d? i?} \eta^{g? j?}''')
    ruleM7  = Ex(r''' M{7}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? f?} \eta^{b? g?} \eta^{c? h?} \eta^{d? i?} \eta^{e? j?}''')
    ruleM8  = Ex(r''' M{8}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? f?} \eta^{b? g?} \eta^{c? h?} \eta^{d? j?} \eta^{e? i?}''')
    ruleM9  = Ex(r''' M{9}^{a? b? c? d? e? f? g? h? i? j?} ->\eta^{a? f?} \eta^{b? h?} \eta^{c? g?} \eta^{d? i?} \eta^{e? j?}''')
    ruleM10  = Ex(r''' M{10}^{a? b? c? d? e? f? g? h? i? j?} ->\epsilon^{a? b? c? d?} \eta^{e? f?} \eta^{g? h?} \eta^{i? j?}''')
    ruleM11  = Ex(r''' M{11}^{a? b? c? d? e? f? g? h? i? j?} ->\epsilon^{a? b? c? d?} \eta^{e? j?} \eta^{f? h?} \eta^{g? i?}''')
    ruleM12  = Ex(r''' M{12}^{a? b? c? d? e? f? g? h? i? j?} ->\epsilon^{a? b? e? f?} \eta^{c? h?} \eta^{d? i?} \eta^{g? j?}''')
    ruleM13  = Ex(r''' M{13}^{a? b? c? d? e? f? g? h? i? j?} ->\epsilon^{a? b? f? g?} \eta^{c? e?} \eta^{d? h?} \eta^{i? j?}''')
    ruleM14  = Ex(r''' M{14}^{a? b? c? d? e? f? g? h? i? j?} ->\epsilon^{a? b? f? g?} \eta^{c? h?} \eta^{d? i?} \eta^{e? j?}''')
    ruleM15  = Ex(r''' M{15}^{a? b? c? d? e? f? g? h? i? j?} ->\epsilon^{a? b? f? g?} \eta^{c? h?} \eta^{d? j?} \eta^{e? i?}''')
    
    ruleM  = Ex(r''' M^{a? b? c? d? e? f? g? h? i? j?} ->e{1} * M{1}^{a? b? c? d? e? f? g? h? i? j?} + e{2} * M{2}^{a? b? c? d? e? f? g? h? i? j?} + e{3} * M{3}^{a? b? c? d? e? f? g? h? i? j?} + e{4} * M{4}^{a? b? c? d? e? f? g? h? i? j?} + e{5} * M{5}^{a? b? c? d? e? f? g? h? i? j?} + e{6} * M{6}^{a? b? c? d? e? f? g? h? i? j?} + e{7} * M{7}^{a? b? c? d? e? f? g? h? i? j?} + e{8} * M{8}^{a? b? c? d? e? f? g? h? i? j?} + e{9} * M{9}^{a? b? c? d? e? f? g? h? i? j?} + e{10} * M{10}^{a? b? c? d? e? f? g? h? i? j?} + e{11} * M{11}^{a? b? c? d? e? f? g? h? i? j?} + e{12} * M{12}^{a? b? c? d? e? f? g? h? i? j?} + e{13} * M{13}^{a? b? c? d? e? f? g? h? i? j?} + e{14} * M{14}^{a? b? c? d? e? f? g? h? i? j?} + e{15} * M{15}^{a? b? c? d? e? f? g? h? i? j?}''')
    
    ruleMH1  = Ex(r''' M^{a b c d e f? g? h? i? j?} \partial_{e}{H_{a b c d}} ->(M^{0 \mu 0 \nu 0 f? g? h? i? j?} - M^{0 \mu \nu 0 0 f? g? h? i? j?} - M^{\mu 0 0 \nu 0 f? g? h? i? j?} + M^{\mu 0 \nu 0 0 f? g? h? i? j?}) \partial_{0}{H1_{\mu \nu}} + (M^{0 \mu 0 \nu \alpha f? g? h? i? j?} - M^{0 \mu \nu 0 \alpha f? g? h? i? j?} - M^{\mu 0 0 \nu \alpha f? g? h? i? j?} + M^{\mu 0 \nu 0 \alpha f? g? h? i? j?}) \partial_{\alpha}{H1_{\mu \nu}} + (M^{0 \mu \nu \rho 0 f? g? h? i? j?} - M^{\mu 0 \nu \rho 0 f? g? h? i? j?} + M^{\nu \rho 0 \mu 0 f? g? h? i? j?} - M^{\nu \rho \mu 0 0 f? g? h? i? j?}) \partial_{0}{H2_{\mu \nu \rho}} + (M^{0 \mu \nu \rho \alpha f? g? h? i? j?} - M^{\mu 0 \nu \rho \alpha f? g? h? i? j?} + M^{\nu \rho 0 \mu \alpha f? g? h? i? j?} - M^{\nu \rho \mu 0 \alpha f? g? h? i? j?}) \partial_{\alpha}{H2_{\mu \nu \rho}} + M^{\mu \nu \rho \sigma 0 f? g? h? i? j?} \partial_{0}{H3_{\mu \nu \rho \sigma}} + M^{\mu \nu \rho \sigma \alpha f? g? h? i? j?} \partial_{\alpha}{H3_{\mu \nu \rho \sigma}}''')
    
    ruleMH2  = Ex(r''' M^{f? g? h? i? j? a b c d e} \partial_{e}{H_{a b c d}} ->(M^{f? g? h? i? j? 0 \mu 0 \nu 0} - M^{f? g? h? i? j? 0 \mu \nu 0 0} - M^{f? g? h? i? j? \mu 0 0 \nu 0} + M^{f? g? h? i? j? \mu 0 \nu 0 0}) \partial_{0}{H1_{\mu \nu}} + (M^{f? g? h? i? j? 0 \mu 0 \nu \alpha} - M^{f? g? h? i? j? 0 \mu \nu 0 \alpha} - M^{f? g? h? i? j? \mu 0 0 \nu \alpha} + M^{f? g? h? i? j? \mu 0 \nu 0 \alpha}) \partial_{\alpha}{H1_{\mu \nu}} + (M^{f? g? h? i? j? 0 \mu \nu \rho 0} - M^{f? g? h? i? j? \mu 0 \nu \rho 0} + M^{f? g? h? i? j? \nu \rho 0 \mu 0} - M^{f? g? h? i? j? \nu \rho \mu 0 0}) \partial_{0}{H2_{\mu \nu \rho}} + (M^{f? g? h? i? j? 0 \mu \nu \rho \alpha} - M^{f? g? h? i? j? \mu 0 \nu \rho \alpha} + M^{f? g? h? i? j? \nu \rho 0 \mu \alpha} - M^{f? g? h? i? j? \nu \rho \mu 0 \alpha}) \partial_{\alpha}{H2_{\mu \nu \rho}} + M^{f? g? h? i? j? \mu \nu \rho \sigma 0} \partial_{0}{H3_{\mu \nu \rho \sigma}} + M^{f? g? h? i? j? \mu \nu \rho \sigma \alpha} \partial_{\alpha}{H3_{\mu \nu \rho \sigma}}''')
    
    ex  = Ex(r''' M^{a b c d e f g h i j} \partial_{e}{H_{a b c d}} \partial_{j}{H_{f g h i}}''')
    
    
    substitute(ex, ruleMH1)
    distribute(ex)
    substitute(ex, ruleMH2)
    distribute(ex)
    
    
    substitute(ex, ruleM)
    substitute(ex, ruleM1)
    substitute(ex, ruleM2)
    substitute(ex, ruleM3)
    substitute(ex, ruleM4)
    substitute(ex, ruleM5)
    substitute(ex, ruleM6)
    substitute(ex, ruleM7)
    substitute(ex, ruleM8)
    substitute(ex, ruleM9)
    substitute(ex, ruleM10)
    substitute(ex, ruleM11)
    substitute(ex, ruleM12)
    substitute(ex, ruleM13)
    substitute(ex, ruleM14)
    substitute(ex, ruleM15)
    
    
    substitute(ex, ruleEta00)
    substitute(ex, ruleEta0a1)
    substitute(ex, ruleEta0a2)
    substitute(ex, ruleEtaab)
    
    
    substitute(ex, ruleEps0000)
    substitute(ex, ruleEps000a1)
    substitute(ex, ruleEps000a2)
    substitute(ex, ruleEps000a3)
    substitute(ex, ruleEps000a4)
    substitute(ex, ruleEps00ab1)
    substitute(ex, ruleEps00ab2)
    substitute(ex, ruleEps00ab3)
    substitute(ex, ruleEps00ab4)
    substitute(ex, ruleEps00ab5)
    substitute(ex, ruleEps00ab6)
    substitute(ex, ruleEps0abc1)
    substitute(ex, ruleEps0abc2)
    substitute(ex, ruleEps0abc3)
    substitute(ex, ruleEps0abc4)
    substitute(ex, ruleEpsabcd)
    
    
    substitute(ex, ruleH1)
    substitute(ex, ruleH2)
    substitute(ex, ruleH3)
    
    
    distribute(ex)
    unwrap(ex)
    
    
    my_epsilon_to_delta(ex)
    my_epsilon_to_delta(ex)
    my_epsilon_to_delta(ex)
    
    rewrite_indices(ex, Ex(r'\epsilon_{\alpha \beta \gamma}'), Ex(r'\gamma^{\alpha \beta}'))
    
    distribute(ex)
    
    
    my_eliminate_metric(ex)
    eliminate_kronecker(ex)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex)
    
    
    sort_product(ex)
    sort_sum(ex)
    
    
    canonicalise(ex)
    rename_dummies(ex)
    
    
    substitute(ex, ruleX)
    substitute(ex, ruleY)
    substitute(ex, ruleZ)
    
    
    unwrap(ex)
    distribute(ex)
    
    
    substitute(ex, ruleTraceFree1)
    substitute(ex, ruleTraceFree2)
    substitute(ex, ruleTraceFree3)
    
    distribute(ex)
    
    sort_product(ex)
    sort_sum(ex)
    canonicalise(ex)
    rename_dummies(ex)

    collect_terms(ex)
    
    return(ex)

def mass_AB():
    ruleM1  = Ex(r''' M{1}^{a? b? c? d? e? f? g? h?} ->\eta^{a? c?} \eta^{b? d?} \eta^{e? g?} \eta^{f? h?}''')
    ruleM2  = Ex(r''' M{2}^{a? b? c? d? e? f? g? h?} ->\eta^{a? c?} \eta^{b? e?} \eta^{d? g?} \eta^{f? h?}''')
    ruleM3  = Ex(r''' M{3}^{a? b? c? d? e? f? g? h?} ->\eta^{a? e?} \eta^{b? f?} \eta^{c? g?} \eta^{d? h?}''')
    ruleM4  = Ex(r''' M{4}^{a? b? c? d? e? f? g? h?} ->\eta^{a? e?} \eta^{b? g?} \eta^{c? f?} \eta^{d? h?}''')
    ruleM5  = Ex(r''' M{5}^{a? b? c? d? e? f? g? h?} ->\epsilon^{a? b? c? d?} \eta^{e? g?} \eta^{f? h?}''')
    ruleM6  = Ex(r''' M{6}^{a? b? c? d? e? f? g? h?} ->\epsilon^{a? b? e? f?} \eta^{c? g?} \eta^{d? h?}''')
    
    ruleM  = Ex(r''' M^{a? b? c? d? e? f? g? h?} ->e{1} * M{1}^{a? b? c? d? e? f? g? h?} + e{2} * M{2}^{a? b? c? d? e? f? g? h?} + e{3} * M{3}^{a? b? c? d? e? f? g? h?} + e{4} * M{4}^{a? b? c? d? e? f? g? h?} + e{5} * M{5}^{a? b? c? d? e? f? g? h?} + e{6} * M{6}^{a? b? c? d? e? f? g? h?}''')
    
    ruleMH1  = Ex(r''' M^{a b c d e? f? g? h?} H_{a b c d} ->(M^{0 \mu 0 \nu e? f? g? h?} - M^{0 \mu \nu 0 e? f? g? h?} - M^{\mu 0 0 \nu e? f? g? h?} + M^{\mu 0 \nu 0 e? f? g? h?}) H1_{\mu \nu} + (M^{0 \mu \nu \rho e? f? g? h?} - M^{\mu 0 \nu \rho e? f? g? h?} + M^{\nu \rho 0 \mu e? f? g? h?} - M^{\nu \rho \mu 0 e? f? g? h?}) H2_{\mu \nu \rho} + M^{\mu \nu \rho \sigma e? f? g? h?} H3_{\mu \nu \rho \sigma}''')
    
    ruleMH2  = Ex(r''' M^{e? f? g? h? a b c d} H_{a b c d} ->(M^{e? f? g? h? 0 \mu 0 \nu} - M^{e? f? g? h? 0 \mu \nu 0} - M^{e? f? g? h? \mu 0 0 \nu} + M^{e? f? g? h? \mu 0 \nu 0}) H1_{\mu \nu} + (M^{e? f? g? h? 0 \mu \nu \rho} - M^{e? f? g? h? \mu 0 \nu \rho} + M^{e? f? g? h? \nu \rho 0 \mu} - M^{e? f? g? h? \nu \rho \mu 0}) H2_{\mu \nu \rho} + M^{e? f? g? h? \mu \nu \rho \sigma} H3_{\mu \nu \rho \sigma}''')
    
    ex  = Ex(r''' M^{a b c d e f g h} H_{a b c d} H_{e f g h}''')
    
    
    substitute(ex, ruleMH1)
    distribute(ex)
    substitute(ex, ruleMH2)
    distribute(ex)
    
    
    substitute(ex, ruleM)
    substitute(ex, ruleM1)
    substitute(ex, ruleM2)
    substitute(ex, ruleM3)
    substitute(ex, ruleM4)
    substitute(ex, ruleM5)
    substitute(ex, ruleM6)
    
    
    substitute(ex, ruleEta00)
    substitute(ex, ruleEta0a1)
    substitute(ex, ruleEta0a2)
    substitute(ex, ruleEtaab)
    
    
    substitute(ex, ruleEps0000)
    substitute(ex, ruleEps000a1)
    substitute(ex, ruleEps000a2)
    substitute(ex, ruleEps000a3)
    substitute(ex, ruleEps000a4)
    substitute(ex, ruleEps00ab1)
    substitute(ex, ruleEps00ab2)
    substitute(ex, ruleEps00ab3)
    substitute(ex, ruleEps00ab4)
    substitute(ex, ruleEps00ab5)
    substitute(ex, ruleEps00ab6)
    substitute(ex, ruleEps0abc1)
    substitute(ex, ruleEps0abc2)
    substitute(ex, ruleEps0abc3)
    substitute(ex, ruleEps0abc4)
    substitute(ex, ruleEpsabcd)
    
    
    substitute(ex, ruleH1)
    substitute(ex, ruleH2)
    substitute(ex, ruleH3)

    
    distribute(ex)
    unwrap(ex)
    
    
    my_epsilon_to_delta(ex)
    my_epsilon_to_delta(ex)
    my_epsilon_to_delta(ex)
    
    rewrite_indices(ex, Ex(r'\epsilon_{\alpha \beta \gamma}'), Ex(r'\gamma^{\alpha \beta}'))
    
    distribute(ex)
    
    
    my_eliminate_metric(ex)
    eliminate_kronecker(ex)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex)
    
    
    sort_product(ex)
    sort_sum(ex)
    
    
    canonicalise(ex)
    rename_dummies(ex)
    
    
    substitute(ex, ruleX)
    substitute(ex, ruleY)
    substitute(ex, ruleZ)
    
    
    unwrap(ex)
    distribute(ex)
    
    
    substitute(ex, ruleTraceFree1)
    substitute(ex, ruleTraceFree2)
    substitute(ex, ruleTraceFree3)

    
    distribute(ex)
    sort_product(ex)
    sort_sum(ex)
    canonicalise(ex)
    rename_dummies(ex)

    collect_terms(ex)
    
    return(ex)

def save_all():
  save_AB()
  save_ApBq()
  save_ABI()

def save_AB():
    ex = mass_AB()
    with open("mass_AB.cdb", "w") as file:
      file.write(ex.input_form()+"\n")

def save_ApBq():
    ex = kin_ApBq()
    with open("kin_ApBq.cdb", "w") as file:
      file.write(ex.input_form()+"\n")

def save_ABI():
    ex = kin_ABI()
    with open("kin_ABI.cdb", "w") as file:
      file.write(ex.input_form()+"\n")

def load_AB():
    with open("mass_AB.cdb", "r") as file:
      ex = Ex(file.readline())
    return(ex)

def load_ApBq():
    with open("kin_ApBq.cdb", "r") as file:
      ex = Ex(file.readline())
    return(ex)

def load_ABI():
    with open("kin_ABI.cdb", "r") as file:
      ex = Ex(file.readline())
    return(ex)

def eom_from_files(toVary):
    ex1 = load_AB()
    ex2 = load_ABI()
    substitute(ex2, Ex(r'e{1} -> e{22}'))
    substitute(ex2, Ex(r'e{2} -> e{23}'))
    substitute(ex2, Ex(r'e{3} -> e{24}'))
    substitute(ex2, Ex(r'e{4} -> e{25}'))
    substitute(ex2, Ex(r'e{5} -> e{26}'))
    substitute(ex2, Ex(r'e{6} -> e{27}'))
    substitute(ex2, Ex(r'e{7} -> e{28}'))
    substitute(ex2, Ex(r'e{8} -> e{29}'))
    substitute(ex2, Ex(r'e{9} -> e{30}'))
    substitute(ex2, Ex(r'e{10} -> e{31}'))
    substitute(ex2, Ex(r'e{11} -> e{32}'))
    substitute(ex2, Ex(r'e{12} -> e{33}'))
    substitute(ex2, Ex(r'e{13} -> e{34}'))
    substitute(ex2, Ex(r'e{14} -> e{35}'))
    substitute(ex2, Ex(r'e{15} -> e{36}'))
    substitute(ex2, Ex(r'e{16} -> e{37}'))
    ex3 = load_ApBq()
    substitute(ex3, Ex(r'e{1} -> e{7}'))
    substitute(ex3, Ex(r'e{2} -> e{8}'))
    substitute(ex3, Ex(r'e{3} -> e{9}'))
    substitute(ex3, Ex(r'e{4} -> e{10}'))
    substitute(ex3, Ex(r'e{5} -> e{11}'))
    substitute(ex3, Ex(r'e{6} -> e{12}'))
    substitute(ex3, Ex(r'e{7} -> e{13}'))
    substitute(ex3, Ex(r'e{8} -> e{14}'))
    substitute(ex3, Ex(r'e{9} -> e{15}'))
    substitute(ex3, Ex(r'e{10} -> e{16}'))
    substitute(ex3, Ex(r'e{11} -> e{17}'))
    substitute(ex3, Ex(r'e{12} -> e{18}'))
    substitute(ex3, Ex(r'e{13} -> e{19}'))
    substitute(ex3, Ex(r'e{14} -> e{20}'))
    substitute(ex3, Ex(r'e{15} -> e{21}'))

    variation = Ex(r'd' + toVary.input_form())
    ruleVary = Ex(r'@{toVary} -> @{variation}')

    ex = Ex(r'\int{@(ex1) + @(ex2) + @(ex3)}{x}')
    vary(ex, ruleVary)

    integrate_by_parts(ex, Ex(r'\partial_{\alpha?}{@(variation)}'))
    unwrap(ex)
    product_rule(ex)
    distribute(ex)
    integrate_by_parts(ex, variation)
    unwrap(ex)
    product_rule(ex)
    distribute(ex)

    sort_product(ex)
    sort_sum(ex)
    canonicalise(ex)
    rename_dummies(ex)
    collect_terms(ex)
    factor_out(ex, variation)

    return ex

def apply_sol(ex):
    substitute(ex, Ex(r'''e{1} -> (-1/6)*k{1}'''))
    substitute(ex, Ex(r'''e{2} -> 1*k{1}'''))
    substitute(ex, Ex(r'''e{3} -> (-1/2)*k{1} + (-1/2)*k{2}'''))
    substitute(ex, Ex(r'''e{4} -> 1*k{2}'''))
    substitute(ex, Ex(r'''e{5} -> (-1/3)*k{3}'''))
    substitute(ex, Ex(r'''e{6} -> 1*k{3}'''))
    substitute(ex, Ex(r'''e{7} -> (-1)*k{10} + (-1)*k{12}'''))
    substitute(ex, Ex(r'''e{8} -> (-1/6)*k{4} + (-1/6)*k{10} + (-1/6)*k{12}'''))
    substitute(ex, Ex(r'''e{9} -> 1*k{5} + 1*k{10} + 1*k{12}'''))
    substitute(ex, Ex(r'''e{10} -> 1*k{4}'''))
    substitute(ex, Ex(r'''e{11} -> 1*k{5}'''))
    substitute(ex, Ex(r'''e{12} -> (-1)*k{5} + 1*k{10} + 1*k{12}'''))
    substitute(ex, Ex(r'''e{13} -> (-1/2)*k{4} + (-1/2)*k{6} + 3/4*k{10} + 3/4*k{12}'''))
    substitute(ex, Ex(r'''e{14} -> (-1)*k{5} + (-1)*k{10} + (-1)*k{12}'''))
    substitute(ex, Ex(r'''e{15} -> 1*k{6}'''))
    substitute(ex, Ex(r'''e{16} -> 1/8*k{16}'''))
    substitute(ex, Ex(r'''e{17} -> 1/6*k{7} + (-1/3)*k{8}'''))
    substitute(ex, Ex(r'''e{18} -> 2*k{7}'''))
    substitute(ex, Ex(r'''e{19} -> 1*k{7}'''))
    substitute(ex, Ex(r'''e{20} -> 1*k{8}'''))
    substitute(ex, Ex(r'''e{21} -> 1*k{7}'''))
    substitute(ex, Ex(r'''e{22} -> (-1/6)*k{9} + (-1/6)*k{10} + (-1/12)*k{12}'''))
    substitute(ex, Ex(r'''e{23} -> 1/6*k{12}'''))
    substitute(ex, Ex(r'''e{24} -> 1*k{9}'''))
    substitute(ex, Ex(r'''e{25} -> 1*k{10}'''))
    substitute(ex, Ex(r'''e{26} -> 1/2*k{10}'''))
    substitute(ex, Ex(r'''e{27} -> (-1/2)*k{9} + 1/2*k{10} + (-1/2)*k{11} + 1/4*k{12}'''))
    substitute(ex, Ex(r'''e{28} -> (-2)*k{10} + (-1)*k{12}'''))
    substitute(ex, Ex(r'''e{29} -> 1*k{11}'''))
    substitute(ex, Ex(r'''e{30} -> 1*k{12}'''))
    substitute(ex, Ex(r'''e{31} -> (-1/2)*k{13} + (-1/12)*k{14} + 1*k{15} + (-1/48)*k{16}'''))
    substitute(ex, Ex(r'''e{32} -> 1*k{13}'''))
    substitute(ex, Ex(r'''e{33} -> (-1/2)*k{14} + (-6)*k{15} + 1/16*k{16}'''))
    substitute(ex, Ex(r'''e{34} -> 1*k{14}'''))
    substitute(ex, Ex(r'''e{35} -> 1*k{14}'''))
    substitute(ex, Ex(r'''e{36} -> 1*k{15}'''))
    substitute(ex, Ex(r'''e{37} -> (-1/16)*k{16}'''))
    substitute(ex, Ex(r'''e{38} -> (-8)*k{10} + (-8)*k{12}'''))
    substitute(ex, Ex(r'''e{39} -> 16*k{10} + 16*k{12}'''))
    substitute(ex, Ex(r'''e{40} -> 1*k{16}'''))
    return(ex)
