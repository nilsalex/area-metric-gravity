from cadabra2 import *

Indices(Ex(r'''{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z#}'''), Ex(r'''fourD, position=independent''') )
Integer(Ex(r'''{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z#}'''), Ex(r'''0..3''') )

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

Symmetric(Ex(r'''\eta_{a? b?}'''), Ex(r'''''') )
AntiSymmetric(Ex(r'''\epsilon_{a? b? c? d?}'''), Ex(r'''''') )

PartialDerivative(Ex(r'''\partial{#}'''), Ex(r'''''') )
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
Depends(Ex(r'''B1'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''U1'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''U2'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''V1'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''V2'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''W2'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dU1'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dU2'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dV1'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dV2'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dW2'''), Ex(r'''\partial{#})''') )

#SortOrder(Ex(r'''{dU{#},dV{#},dW{#},dB{#},dA,m{#},k{#},t{#},e{#},A,B{#},X{#},Y{#},Z{#},U{#},V{#},W{#},\epsilon{#},\gamma{#},\partial{#}{dU{#}},\partial{#}{dV{#}},\partial{#}{dW{#}},\partial{#}{dB{#}},\partial{#}{dA},\partial{#}{A},\partial{#}{B{#}},\partial{#}{X{#}},\partial{#}{Y{#}},\partial{#}{Z{#}},\partial{#}{U{#}},\partial{#}{V{#}},\partial{#}{W{#}}}'''), Ex(r'''''') )
SortOrder(Ex(r'''{\gamma_{p? q?},\epsilon_{p? q? r?},\gamma^{p? q?},\epsilon^{p? q? r?}'''), Ex(r'''''') )

#ruleH1  = Ex(r''' H1_{\mu \nu} -> \gamma_{\alpha \mu} \gamma_{\beta \nu} X^{\alpha \beta}''')
#ruleH2  = Ex(r''' H2_{\mu \nu \rho} -> \epsilon_{\alpha \nu \rho} * \gamma_{\mu \sigma} Z^{\alpha \sigma}''')
#ruleH3  = Ex(r''' H3_{\mu \nu \rho \sigma} -> \epsilon_{\alpha \mu \nu} \epsilon_{\beta \rho \sigma} Y^{\alpha \beta}''')

ruleH1 = Ex(r''' H1^{\alpha \beta} -> 2 A \gamma^{\alpha \beta} - X^{\alpha \beta}''')
ruleH2 = Ex(r''' H2^{\alpha \beta \gamma} -> -A \epsilon^{\alpha \beta \gamma} + B^{\beta} \gamma^{\alpha \gamma} - B^{\gamma} \gamma^{\alpha \beta} + \epsilon^{\mu \beta \gamma} \gamma_{\mu \nu} Z^{\nu \alpha} + (1/2) \epsilon^{\alpha \beta \gamma} \gamma_{\mu \nu} X^{\mu \nu}''')
ruleH3 = Ex(r''' H3^{\alpha \beta \gamma \delta} -> (\gamma^{\alpha \gamma} \gamma^{\beta \delta} - \gamma^{\alpha \delta} \gamma^{\beta \gamma}) \gamma_{\mu \nu} X^{\mu \nu} + \epsilon^{\mu \alpha \beta} \epsilon^{\nu \gamma \delta} \gamma_{\mu \rho} \gamma_{\nu \sigma} Y^{\rho \sigma}''')

ruleEta001  = Ex(r''' \eta_{0 0} -> 1''')
ruleEta002  = Ex(r''' \eta^{0 0} -> 1''')
ruleEta0a11  = Ex(r''' \eta_{0 \alpha} -> 0''')
ruleEta0a21  = Ex(r''' \eta_{\alpha 0} -> 0''')
ruleEta0a12  = Ex(r''' \eta^{0 \alpha} -> 0''')
ruleEta0a22  = Ex(r''' \eta^{\alpha 0} -> 0''')
ruleEtaab1  = Ex(r''' \eta^{\alpha \beta} -> -\gamma^{\alpha \beta}''')
ruleEtaab2  = Ex(r''' \eta_{\alpha \beta} -> -\gamma_{\alpha \beta}''')

ruleEtaEta1 = Ex(r'''\eta^{a? p} \eta_{b? p} -> \delta^{a?}_{b?}''')
ruleEtaEta2 = Ex(r'''\eta^{a? p} \eta_{p b?} -> \delta^{a?}_{b?}''')
ruleEtaEta3 = Ex(r'''\eta^{p a?} \eta_{b? p} -> \delta^{a?}_{b?}''')
ruleEtaEta4 = Ex(r'''\eta^{p a?} \eta_{p b?} -> \delta^{a?}_{b?}''')

ruleEtaEpsilon1_ = Ex(r'''\eta_{a? p} \epsilon^{p \alpha \beta \gamma} -> \delta^{0}_{a?} \epsilon^{\alpha \beta \gamma}''')
ruleEtaEpsilon2_ = Ex(r'''\eta_{p a?} \epsilon^{p \alpha \beta \gamma} -> \delta^{0}_{a?} \epsilon^{\alpha \beta \gamma}''')
ruleEtaEpsilon3_ = Ex(r'''\eta_{a? p} \epsilon^{\alpha p \beta \gamma} -> -\delta^{0}_{a?} \epsilon^{\alpha \beta \gamma}''')
ruleEtaEpsilon4_ = Ex(r'''\eta_{p a?} \epsilon^{\alpha p \beta \gamma} -> -\delta^{0}_{a?} \epsilon^{\alpha \beta \gamma}''')
ruleEtaEpsilon5_ = Ex(r'''\eta_{a? p} \epsilon^{\alpha \beta p \gamma} -> \delta^{0}_{a?} \epsilon^{\alpha \beta \gamma}''')
ruleEtaEpsilon6_ = Ex(r'''\eta_{p a?} \epsilon^{\alpha \beta p \gamma} -> \delta^{0}_{a?} \epsilon^{\alpha \beta \gamma}''')
ruleEtaEpsilon7_ = Ex(r'''\eta_{a? p} \epsilon^{\alpha \beta \gamma p} -> -\delta^{0}_{a?} \epsilon^{\alpha \beta \gamma}''')
ruleEtaEpsilon8_ = Ex(r'''\eta_{p a?} \epsilon^{\alpha \beta \gamma p} -> -\delta^{0}_{a?} \epsilon^{\alpha \beta \gamma}''')

ruleEtaEpsilon1 = Ex(r'''\eta^{a? p} \epsilon_{p \alpha \beta \gamma} -> \delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon2 = Ex(r'''\eta^{p a?} \epsilon_{p \alpha \beta \gamma} -> \delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon3 = Ex(r'''\eta^{a? p} \epsilon_{\alpha p \beta \gamma} -> -\delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon4 = Ex(r'''\eta^{p a?} \epsilon_{\alpha p \beta \gamma} -> -\delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon5 = Ex(r'''\eta^{a? p} \epsilon_{\alpha \beta p \gamma} -> \delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon6 = Ex(r'''\eta^{p a?} \epsilon_{\alpha \beta p \gamma} -> \delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon7 = Ex(r'''\eta^{a? p} \epsilon_{\alpha \beta \gamma p} -> -\delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')
ruleEtaEpsilon8 = Ex(r'''\eta^{p a?} \epsilon_{\alpha \beta \gamma p} -> -\delta^{a?}_{0} \epsilon_{\alpha \beta \gamma}''')

ruleDelta1 = Ex(r'''\delta_{p?}^{q?} -> \delta^{q?}_{p?}''')
ruleDelta2 = Ex(r'''\delta^{0}_{\alpha} -> 0''')
ruleDelta3 = Ex(r'''\delta^{\alpha}_{0} -> 0''')

ruleDeltaDelta1 = Ex(r'''\delta^{p}_{q?} \delta^{r?}_{p} -> \delta^{r?}_{q?}''')
ruleDeltaDelta2 = Ex(r'''\delta^{r?}_{p} \delta^{p}_{q?} -> \delta^{r?}_{q?}''')

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
ruleEps0abc1  = Ex(r''' \epsilon^{0 \alpha \beta \gamma} -> \epsilon^{\alpha \beta \gamma}''')
ruleEps0abc2  = Ex(r''' \epsilon^{\alpha 0 \beta \gamma} -> -\epsilon^{\alpha \beta \gamma}''')
ruleEps0abc3  = Ex(r''' \epsilon^{\alpha \beta 0 \gamma} -> \epsilon^{\alpha \beta \gamma}''')
ruleEps0abc4  = Ex(r''' \epsilon^{\alpha \beta \gamma 0} -> -\epsilon^{\alpha \beta \gamma}''')
ruleEpsabcd  = Ex(r''' \epsilon^{\alpha \beta \gamma \delta} -> 0''')

ruleEps0000_  = Ex(r''' \epsilon_{0 0 0 0} -> 0''')
ruleEps000a1_  = Ex(r''' \epsilon_{0 0 0 \alpha} -> 0''')
ruleEps000a2_  = Ex(r''' \epsilon_{0 0 \alpha 0} -> 0''')
ruleEps000a3_  = Ex(r''' \epsilon_{0 \alpha 0 0} -> 0''')
ruleEps000a4_  = Ex(r''' \epsilon_{\alpha 0 0 0} -> 0''')
ruleEps00ab1_  = Ex(r''' \epsilon_{0 0 \alpha \beta} -> 0''')
ruleEps00ab2_  = Ex(r''' \epsilon_{0 \alpha 0 \beta} -> 0''')
ruleEps00ab3_  = Ex(r''' \epsilon_{0 \alpha \beta 0} -> 0''')
ruleEps00ab4_  = Ex(r''' \epsilon_{\alpha 0 0 \beta} -> 0''')
ruleEps00ab5_  = Ex(r''' \epsilon_{\alpha 0 \beta 0} -> 0''')
ruleEps00ab6_  = Ex(r''' \epsilon_{\alpha \beta 0 0} -> 0''')
ruleEps0abc1_  = Ex(r''' \epsilon_{0 \alpha \beta \gamma} -> \epsilon_{\alpha \beta \gamma}''')
ruleEps0abc2_  = Ex(r''' \epsilon_{\alpha 0 \beta \gamma} -> -\epsilon_{\alpha \beta \gamma}''')
ruleEps0abc3_  = Ex(r''' \epsilon_{\alpha \beta 0 \gamma} -> \epsilon_{\alpha \beta \gamma}''')
ruleEps0abc4_  = Ex(r''' \epsilon_{\alpha \beta \gamma 0} -> -\epsilon_{\alpha \beta \gamma}''')
ruleEpsabcd_  = Ex(r''' \epsilon_{\alpha \beta \gamma \delta} -> 0''')

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

def kin_ABCI():
    rulesM = [
      Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? h?} \eta_{i? k?} \eta_{j? l?} \eta^{m? n?}'''),
      Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? h?} \eta_{i? k?} \delta_{j?}^{m?} \delta_{l?}^{n?}'''),
      Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? i?} \eta_{h? k?} \eta_{j? l?} \eta^{m? n?}'''),
      Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? i?} \eta_{h? k?} \delta_{j?}^{m?} \delta_{l?}^{n?}'''),
      Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? i?} \delta_{h?}^{m?} \eta_{j? k?} \delta_{l?}^{n?}'''),
      Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \delta_{f?}^{m?} \delta_{h?}^{n?} \eta_{i? k?} \eta_{j? l?}'''),
      Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? d?} \eta_{e? i?} \eta_{f? j?} \eta_{g? k?} \eta_{h? l?} \eta^{m? n?}'''),
      Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? d?} \eta_{e? i?} \eta_{f? j?} \eta_{g? k?} \delta_{h?}^{m?} \delta_{l?}^{n?}'''),
      Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? d?} \eta_{e? i?} \eta_{f? k?} \eta_{g? j?} \eta_{h? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \eta_{f? h?} \eta_{i? k?} \eta_{j? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \eta_{f? h?} \eta_{i? k?} \delta_{j?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \eta_{f? i?} \eta_{h? k?} \eta_{j? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \eta_{f? i?} \eta_{h? k?} \delta_{j?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \eta_{f? i?} \delta_{h?}^{m?} \eta_{j? k?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \delta_{f?}^{m?} \delta_{h?}^{n?} \eta_{i? k?} \eta_{j? l?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? i?} \eta_{f? g?} \eta_{h? k?} \eta_{j? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? i?} \eta_{f? g?} \eta_{h? k?} \delta_{j?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? i?} \eta_{f? g?} \delta_{h?}^{m?} \eta_{j? k?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? i?} \eta_{f? j?} \eta_{g? k?} \eta_{h? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? i?} \eta_{f? j?} \eta_{g? k?} \delta_{h?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? i?} \eta_{f? k?} \eta_{g? j?} \delta_{h?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? i?} \eta_{f? k?} \eta_{g? l?} \delta_{h?}^{m?} \delta_{j?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? i?} \delta_{f?}^{m?} \eta_{g? j?} \eta_{h? k?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? i?} \delta_{f?}^{m?} \eta_{g? k?} \eta_{h? l?} \delta_{j?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? i?} \delta_{f?}^{m?} \eta_{g? k?} \delta_{h?}^{n?} \eta_{j? l?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \delta_{d?}^{m?} \eta_{f? g?} \delta_{h?}^{n?} \eta_{i? k?} \eta_{j? l?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? e?} \delta_{d?}^{m?} \eta_{f? i?} \eta_{g? j?} \eta_{h? k?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? i?} \eta_{d? k?} \eta_{e? g?} \delta_{f?}^{m?} \delta_{h?}^{n?} \eta_{j? l?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? c?} \eta_{b? i?} \eta_{d? k?} \eta_{e? j?} \delta_{f?}^{m?} \eta_{g? l?} \delta_{h?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \eta_{d? h?} \eta_{i? k?} \eta_{j? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \eta_{d? h?} \eta_{i? k?} \delta_{j?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? e?} \eta_{b? f?} \eta_{c? i?} \eta_{d? j?} \eta_{g? k?} \eta_{h? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? e?} \eta_{b? f?} \eta_{c? i?} \eta_{d? j?} \eta_{g? k?} \delta_{h?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? e?} \eta_{b? f?} \eta_{c? i?} \eta_{d? k?} \eta_{g? j?} \eta_{h? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? e?} \eta_{b? g?} \eta_{c? f?} \eta_{d? h?} \eta_{i? k?} \eta_{j? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? e?} \eta_{b? g?} \eta_{c? f?} \eta_{d? h?} \eta_{i? k?} \delta_{j?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? e?} \eta_{b? g?} \eta_{c? i?} \eta_{d? j?} \eta_{f? k?} \eta_{h? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? e?} \eta_{b? g?} \eta_{c? i?} \eta_{d? j?} \eta_{f? k?} \delta_{h?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta_{a? e?} \eta_{b? i?} \eta_{c? g?} \eta_{d? k?} \delta_{f?}^{m?} \delta_{h?}^{n?} \eta_{j? l?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? c? d?} \eta_{e? g?} \eta_{f? h?} \eta_{i? k?} \eta_{j? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? c? d?} \eta_{e? g?} \eta_{f? h?} \eta_{i? k?} \delta_{j?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? c? d?} \eta_{e? g?} \eta_{f? i?} \eta_{h? k?} \eta_{j? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? c? d?} \eta_{e? g?} \eta_{f? i?} \eta_{h? k?} \delta_{j?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? c? d?} \eta_{e? g?} \eta_{f? i?} \delta_{h?}^{m?} \eta_{j? k?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? c? d?} \eta_{e? g?} \delta_{f?}^{m?} \delta_{h?}^{n?} \eta_{i? k?} \eta_{j? l?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? c? d?} \eta_{e? i?} \eta_{f? j?} \eta_{g? k?} \eta_{h? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? c? d?} \eta_{e? i?} \eta_{f? j?} \eta_{g? k?} \delta_{h?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? c? d?} \eta_{e? i?} \eta_{f? k?} \eta_{g? j?} \eta_{h? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? h?} \eta_{i? k?} \eta_{j? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? h?} \eta_{i? k?} \delta_{j?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? i?} \eta_{h? k?} \eta_{j? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? i?} \eta_{h? k?} \delta_{j?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? i?} \delta_{h?}^{m?} \eta_{j? k?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? f?} \eta_{c? g?} \delta_{d?}^{m?} \delta_{h?}^{n?} \eta_{i? k?} \eta_{j? l?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? f?} \eta_{c? i?} \eta_{d? j?} \eta_{g? k?} \eta_{h? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? f?} \eta_{c? i?} \eta_{d? j?} \eta_{g? k?} \delta_{h?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? f?} \eta_{c? i?} \eta_{d? k?} \eta_{g? j?} \eta_{h? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? i?} \eta_{c? f?} \eta_{d? j?} \eta_{g? k?} \eta_{h? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? i?} \eta_{c? f?} \eta_{d? j?} \eta_{g? k?} \delta_{h?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? i?} \eta_{c? f?} \eta_{d? k?} \eta_{g? j?} \eta_{h? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? i?} \eta_{c? f?} \eta_{d? k?} \eta_{g? j?} \delta_{h?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? i?} \eta_{c? f?} \eta_{d? k?} \eta_{g? l?} \delta_{h?}^{m?} \delta_{j?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? i?} \eta_{c? f?} \delta_{d?}^{m?} \eta_{g? j?} \eta_{h? k?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? i?} \eta_{c? f?} \delta_{d?}^{m?} \eta_{g? k?} \eta_{h? l?} \delta_{j?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? e? i?} \eta_{c? f?} \delta_{d?}^{m?} \eta_{g? k?} \delta_{h?}^{n?} \eta_{j? l?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta^{p m?} \epsilon_{a? b? e? p} \eta_{c? f?} \eta_{d? i?} \eta_{g? j?} \eta_{h? k?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? i? j?} \eta_{c? e?} \eta_{d? f?} \eta_{g? k?} \eta_{h? l?} \eta^{m? n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? i? j?} \eta_{c? e?} \eta_{d? f?} \eta_{g? k?} \delta_{h?}^{m?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{a? b? i? j?} \eta_{c? e?} \eta_{d? k?} \delta_{f?}^{m?} \eta_{g? l?} \delta_{h?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta^{p m?} \epsilon_{a? b? i? p} \eta_{c? e?} \eta_{d? f?} \eta_{g? j?} \eta_{h? k?} \delta_{l?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \eta^{p m?} \epsilon_{a? b? i? p} \eta_{c? e?} \eta_{d? f?} \eta_{g? k?} \eta_{h? l?} \delta_{j?}^{n?}'''),
       Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?}^{m? n?}  -> \epsilon_{i? j? k? l?} \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? h?} \eta^{m? n?}''')
      ]
    
    ruleMH1  = Ex(r''' M_{a b c d e? f? g? h? i? j? k? l?}^{m? n?} H^{a b c d} ->(M_{0 \mu 0 \nu e? f? g? h? i? j? k? l?}^{m? n?} - M_{0 \mu \nu 0 e? f? g? h? i? j? k? l?}^{m? n?} - M_{\mu 0 0 \nu e? f? g? h? i? j? k? l?}^{m? n?} + M_{\mu 0 \nu 0 e? f? g? h? i? j? k? l?}^{m? n?}) H1^{\mu \nu} + (M_{0 \mu \nu \rho e? f? g? h? i? j? k? l?}^{m? n?} - M_{\mu 0 \nu \rho e? f? g? h? i? j? k? l?}^{m? n?} + M_{\nu \rho 0 \mu e? f? g? h? i? j? k? l?}^{m? n?} - M_{\nu \rho \mu 0 e? f? g? h? i? j? k? l?}^{m? n?}) H2^{\mu \nu \rho} + M_{\mu \nu \rho \sigma e? f? g? h? i? j? k? l?}^{m? n?} H3^{\mu \nu \rho \sigma}''')

    ruleMH2  = Ex(r''' M_{e? f? g? h? a b c d i? j? k? l?}^{m? n?} H^{a b c d} ->(M_{e? f? g? h? 0 \mu 0 \nu i? j? k? l?}^{m? n?} - M_{e? f? g? h? 0 \mu \nu 0 i? j? k? l?}^{m? n?} - M_{e? f? g? h? \mu 0 0 \nu i? j? k? l?}^{m? n?} + M_{e? f? g? h? \mu 0 \nu 0 i? j? k? l?}^{m? n?}) H1^{\mu \nu} + (M_{e? f? g? h? 0 \mu \nu \rho i? j? k? l?}^{m? n?} - M_{e? f? g? h? \mu 0 \nu \rho i? j? k? l?}^{m? n?} + M_{e? f? g? h? \nu \rho 0 \mu i? j? k? l?}^{m? n?} - M_{e? f? g? h? \nu \rho \mu 0 i? j? k? l?}^{m? n?}) H2^{\mu \nu \rho} + M_{e? f? g? h? \mu \nu \rho \sigma i? j? k? l?}^{m? n?} H3^{\mu \nu \rho \sigma}''')
    
    ruleMH3  = Ex(r''' M_{e? f? g? h? i? j? k? l? a b c d}^{p q} \partial_{p q}{H^{a b c d}} ->(M_{e? f? g? h? i? j? k? l? 0 \mu 0 \nu}^{0 0} - M_{e? f? g? h? i? j? k? l? 0 \mu \nu 0}^{0 0} - M_{e? f? g? h? i? j? k? l? \mu 0 0 \nu}^{0 0} + M_{e? f? g? h? i? j? k? l? \mu 0 \nu 0}^{0 0}) \partial_{0 0}{H1^{\mu \nu}} + (M_{e? f? g? h? i? j? k? l? 0 \mu 0 \nu}^{0 \alpha} - M_{e? f? g? h? i? j? k? l? 0 \mu \nu 0}^{0 \alpha} - M_{e? f? g? h? i? j? k? l? \mu 0 0 \nu}^{0 \alpha} + M_{e? f? g? h? i? j? k? l? \mu 0 \nu 0}^{0 \alpha}) \partial_{0 \alpha}{H1^{\mu \nu}} + (M_{e? f? g? h? i? j? k? l? 0 \mu 0 \nu}^{\alpha 0} - M_{e? f? g? h? i? j? k? l? 0 \mu \nu 0}^{\alpha 0} - M_{e? f? g? h? i? j? k? l? \mu 0 0 \nu}^{\alpha 0} + M_{e? f? g? h? i? j? k? l? \mu 0 \nu 0}^{\alpha 0}) \partial_{0 \alpha}{H1^{\mu \nu}} + (M_{e? f? g? h? i? j? k? l? 0 \mu 0 \nu}^{\alpha \beta} - M_{e? f? g? h? i? j? k? l? 0 \mu \nu 0}^{\alpha \beta} - M_{e? f? g? h? i? j? k? l? \mu 0 0 \nu}^{\alpha \beta} + M_{e? f? g? h? i? j? k? l? \mu 0 \nu 0}^{\alpha \beta}) \partial_{\alpha \beta}{H1^{\mu \nu}} + (M_{e? f? g? h? i? j? k? l? 0 \mu \nu \rho}^{0 0} - M_{e? f? g? h? i? j? k? l? \mu 0 \nu \rho}^{0 0} + M_{e? f? g? h? i? j? k? l? \nu \rho 0 \mu}^{0 0} - M_{e? f? g? h? i? j? k? l? \nu \rho \mu 0}^{0 0}) \partial_{0 0}{H2^{\mu \nu \rho}} + (M_{e? f? g? h? i? j? k? l? 0 \mu \nu \rho}^{0 \alpha} - M_{e? f? g? h? i? j? k? l? \mu 0 \nu \rho}^{0 \alpha} + M_{e? f? g? h? i? j? k? l? \nu \rho 0 \mu}^{0 \alpha} - M_{e? f? g? h? i? j? k? l? \nu \rho \mu 0}^{0 \alpha}) \partial_{0 \alpha}{H2^{\mu \nu \rho}} + (M_{e? f? g? h? i? j? k? l? 0 \mu \nu \rho}^{\alpha 0} - M_{e? f? g? h? i? j? k? l? \mu 0 \nu \rho}^{\alpha 0} + M_{e? f? g? h? i? j? k? l? \nu \rho 0 \mu}^{\alpha 0} - M_{e? f? g? h? i? j? k? l? \nu \rho \mu 0}^{\alpha 0}) \partial_{0 \alpha}{H2^{\mu \nu \rho}} + (M_{e? f? g? h? i? j? k? l? 0 \mu \nu \rho}^{\alpha \beta} - M_{e? f? g? h? i? j? k? l? \mu 0 \nu \rho}^{\alpha \beta} + M_{e? f? g? h? i? j? k? l? \nu \rho 0 \mu}^{\alpha \beta} - M_{e? f? g? h? i? j? k? l? \nu \rho \mu 0}^{\alpha \beta}) \partial_{\alpha \beta}{H2^{\mu \nu \rho}} + M_{e? f? g? h? i? j? k? l? \mu \nu \rho \sigma}^{0 0} \partial_{0 0}{H3^{\mu \nu \rho \sigma}} + M_{e? f? g? h? i? j? k? l? \mu \nu \rho \sigma}^{0 \alpha} \partial_{0 \alpha}{H3^{\mu \nu \rho \sigma}} + M_{e? f? g? h? i? j? k? l? \mu \nu \rho \sigma}^{\alpha 0} \partial_{0 \alpha}{H3^{\mu \nu \rho \sigma}} + M_{e? f? g? h? i? j? k? l? \mu \nu \rho \sigma}^{\alpha \beta} \partial_{\alpha \beta}{H3^{\mu \nu \rho \sigma}}''')
    

    terms = []

    for (i,rule) in enumerate(rulesM):
      print(i)
      ex  = Ex('e{{{0}}} '.format(i+1) + r'''M_{a b c d e f g h i j k l}^{m n} H^{a b c d} H^{e f g h} \partial_{m n}{H^{i j k l}}''')
    
      substitute(ex, ruleMH1)
      distribute(ex)
      substitute(ex, ruleMH2)
      distribute(ex)
      substitute(ex, ruleMH3)
      distribute(ex)

      substitute(ex, rule)
    
      three_plus_one(ex)

      terms.append(ex)
    
    res = Ex('+'.join([terms[i].input_form() for i in range(len(rulesM))]))

    return(res)

def eliminate_eta(ex):
    substitute(ex, ruleEtaEta1, repeat=True)
    substitute(ex, ruleEtaEta2, repeat=True)
    substitute(ex, ruleEtaEta3, repeat=True)
    substitute(ex, ruleEtaEta4, repeat=True)

def three_plus_one_eta(ex):
    substitute(ex, ruleEta001, repeat=True)
    substitute(ex, ruleEta0a11, repeat=True)
    substitute(ex, ruleEta0a21, repeat=True)
    substitute(ex, ruleEtaab1, repeat=True)
    
    substitute(ex, ruleEta002, repeat=True)
    substitute(ex, ruleEta0a12, repeat=True)
    substitute(ex, ruleEta0a22, repeat=True)
    substitute(ex, ruleEtaab2, repeat=True)

def my_eliminate_kronecker(ex):
    substitute(ex, ruleDeltaDelta1, repeat=True)
    substitute(ex, ruleDeltaDelta2, repeat=True)

def three_plus_one_delta(ex):
    substitute(ex, ruleDelta1, repeat=True)
    substitute(ex, ruleDelta2, repeat=True)
    substitute(ex, ruleDelta3, repeat=True)

def three_plus_one_epsilon(ex):
    substitute(ex, ruleEps0000, repeat=True)
    substitute(ex, ruleEps000a1, repeat=True)
    substitute(ex, ruleEps000a2, repeat=True)
    substitute(ex, ruleEps000a3, repeat=True)
    substitute(ex, ruleEps000a4, repeat=True)
    substitute(ex, ruleEps00ab1, repeat=True)
    substitute(ex, ruleEps00ab2, repeat=True)
    substitute(ex, ruleEps00ab3, repeat=True)
    substitute(ex, ruleEps00ab4, repeat=True)
    substitute(ex, ruleEps00ab5, repeat=True)
    substitute(ex, ruleEps00ab6, repeat=True)
    substitute(ex, ruleEps0abc1, repeat=True)
    substitute(ex, ruleEps0abc2, repeat=True)
    substitute(ex, ruleEps0abc3, repeat=True)
    substitute(ex, ruleEps0abc4, repeat=True)
    substitute(ex, ruleEpsabcd, repeat=True)
    substitute(ex, ruleEps0000_, repeat=True)
    substitute(ex, ruleEps000a1_, repeat=True)
    substitute(ex, ruleEps000a2_, repeat=True)
    substitute(ex, ruleEps000a3_, repeat=True)
    substitute(ex, ruleEps000a4_, repeat=True)
    substitute(ex, ruleEps00ab1_, repeat=True)
    substitute(ex, ruleEps00ab2_, repeat=True)
    substitute(ex, ruleEps00ab3_, repeat=True)
    substitute(ex, ruleEps00ab4_, repeat=True)
    substitute(ex, ruleEps00ab5_, repeat=True)
    substitute(ex, ruleEps00ab6_, repeat=True)
    substitute(ex, ruleEps0abc1_, repeat=True)
    substitute(ex, ruleEps0abc2_, repeat=True)
    substitute(ex, ruleEps0abc3_, repeat=True)
    substitute(ex, ruleEps0abc4_, repeat=True)
    substitute(ex, ruleEpsabcd_, repeat=True)

def subs_delta_eta(ex):
    substitute(ex, Ex(r'''\delta^{p?}_{a} \eta^{a q?} -> \eta^{p? q?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{p?}_{a} \eta^{q? a} -> \eta^{p? q?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{a}_{p?} \eta_{a q?} -> \eta_{p? q?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{a}_{p?} \eta_{q? a} -> \eta_{p? q?}'''), repeat=True)

def subs_delta_epsilon(ex):
    substitute(ex, Ex(r'''\delta^{a}_{p?} \epsilon_{q? r? s? a} -> \epsilon_{q? r? s? p?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{a}_{p?} \epsilon_{q? r? a s?} -> \epsilon_{q? r? p? s?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{a}_{p?} \epsilon_{q? a r? s?} -> \epsilon_{q? p? r? s?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{a}_{p?} \epsilon_{a q? r? s?} -> \epsilon_{p? q? r? s?}'''), repeat=True)

    substitute(ex, Ex(r'''\delta_{a}^{p?} \epsilon^{q? r? s? a} -> \epsilon^{q? r? s? p?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta_{a}^{p?} \epsilon^{q? r? a s?} -> \epsilon^{q? r? p? s?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta_{a}^{p?} \epsilon^{q? a r? s?} -> \epsilon^{q? p? r? s?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta_{a}^{p?} \epsilon^{a q? r? s?} -> \epsilon^{p? q? r? s?}'''), repeat=True)

def subs_eta_epsilon(ex):
    substitute(ex, Ex(r'''\eta^{0 a} \epsilon_{p? q? r? a} -> \epsilon_{p? q? r? 0}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{0 a} \epsilon_{p? q? a r?} -> \epsilon_{p? q? 0 r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{0 a} \epsilon_{p? a q? r?} -> \epsilon_{p? 0 q? r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{0 a} \epsilon_{a p? q? r?} -> \epsilon_{0 p? q? r?}'''), repeat=True)

    substitute(ex, Ex(r'''\eta^{a 0} \epsilon_{p? q? r? a} -> \epsilon_{p? q? r? 0}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{a 0} \epsilon_{p? q? a r?} -> \epsilon_{p? q? 0 r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{a 0} \epsilon_{p? a q? r?} -> \epsilon_{p? 0 q? r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{a 0} \epsilon_{a p? q? r?} -> \epsilon_{0 p? q? r?}'''), repeat=True)

    substitute(ex, Ex(r'''\eta^{\alpha a} \epsilon_{p? q? r? a} -> -\gamma^{\alpha \mu} \epsilon_{p? q? r? \mu}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{\alpha a} \epsilon_{p? q? a r?} -> -\gamma^{\alpha \mu} \epsilon_{p? q? \mu r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{\alpha a} \epsilon_{p? a q? r?} -> -\gamma^{\alpha \mu} \epsilon_{p? \mu q? r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{\alpha a} \epsilon_{a p? q? r?} -> -\gamma^{\alpha \mu} \epsilon_{\mu p? q? r?}'''), repeat=True)

    substitute(ex, Ex(r'''\eta^{a \alpha} \epsilon_{p? q? r? a} -> -\gamma^{\alpha \mu} \epsilon_{p? q? r? \mu}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{a \alpha} \epsilon_{p? q? a r?} -> -\gamma^{\alpha \mu} \epsilon_{p? q? \mu r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{a \alpha} \epsilon_{p? a q? r?} -> -\gamma^{\alpha \mu} \epsilon_{p? \mu q? r?}'''), repeat=True)
    substitute(ex, Ex(r'''\eta^{a \alpha} \epsilon_{a p? q? r?} -> -\gamma^{\alpha \mu} \epsilon_{\mu p? q? r?}'''), repeat=True)

def normalize_delta(ex):
    substitute(ex, Ex(r'''\delta_{p?}^{q?} -> \delta^{q?}_{p?}'''), repeat=True)

def my_canonicalise(ex):
    sort_product(ex)
    sort_sum(ex)
    canonicalise(ex)
    rename_dummies(ex)
    collect_terms(ex)

def three_plus_one(ex):
    three_plus_one_delta(ex)
    three_plus_one_eta(ex)

    distribute(ex, repeat=True)

    normalize_delta(ex)
    my_eliminate_kronecker(ex)
    three_plus_one_delta(ex)
    
    three_plus_one_epsilon(ex)
    subs_delta_eta(ex)
    
    my_canonicalise(ex)

    normalize_delta(ex)
    subs_delta_epsilon(ex)
    subs_eta_epsilon(ex)

    three_plus_one_delta(ex)
    three_plus_one_epsilon(ex)
    three_plus_one_eta(ex)

    my_canonicalise(ex)

    substitute(ex, ruleH1, repeat=True)
    substitute(ex, ruleH2, repeat=True)
    substitute(ex, ruleH3, repeat=True)

    distribute(ex)
    unwrap(ex)

    my_epsilon_to_delta(ex)
    my_epsilon_to_delta(ex)
    my_epsilon_to_delta(ex)
    
    distribute(ex)

    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)

    my_canonicalise(ex)
    
    rewrite_indices(ex, Ex(r'\epsilon_{\alpha \beta \gamma}'), Ex(r'\gamma^{\alpha \beta}'))

    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)
    
    my_canonicalise(ex)
    
    substitute(ex, ruleX)
    substitute(ex, ruleY)
    substitute(ex, ruleZ)
    
    unwrap(ex)
    distribute(ex)
    
    substitute(ex, ruleTraceFree1, repeat=True)
    substitute(ex, ruleTraceFree2, repeat=True)
    substitute(ex, ruleTraceFree3, repeat=True)
    
    distribute(ex)
    
    my_canonicalise(ex)

    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)

    my_canonicalise(ex)
    
    return(ex)

def kin_ABpCq():
    rulesM = [
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? h?} \delta_{j?}^{i?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? h?} \eta^{i? n?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \delta_{f?}^{i?} \eta_{h? j?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? j?} \eta_{h? l?} \delta_{k?}^{i?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? j?} \eta_{h? l?} \eta^{i? n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? j?} \delta_{h?}^{n?} \delta_{l?}^{i?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? d?} \delta_{e?}^{i?} \eta_{f? j?} \eta_{g? k?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? d?} \delta_{e?}^{i?} \eta_{f? j?} \eta_{g? l?} \eta_{h? m?} \delta_{k?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? d?} \eta_{e? j?} \eta_{f? k?} \eta_{g? l?} \eta_{h? m?} \eta^{i? n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \eta_{f? h?} \delta_{j?}^{i?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \eta_{f? h?} \eta^{i? n?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \delta_{f?}^{i?} \eta_{h? j?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \delta_{f?}^{i?} \delta_{h?}^{n?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \eta_{f? j?} \eta_{h? l?} \delta_{k?}^{i?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \eta_{f? j?} \eta_{h? l?} \eta^{i? n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \eta_{f? j?} \delta_{h?}^{n?} \delta_{l?}^{i?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \delta_{d?}^{i?} \eta_{f? g?} \eta_{h? j?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \delta_{d?}^{i?} \eta_{f? g?} \delta_{h?}^{n?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \delta_{d?}^{i?} \eta_{f? j?} \eta_{g? k?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \delta_{d?}^{i?} \eta_{f? j?} \eta_{g? l?} \eta_{h? m?} \delta_{k?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \delta_{d?}^{i?} \eta_{f? j?} \eta_{g? l?} \delta_{h?}^{n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? j?} \eta_{f? g?} \delta_{h?}^{i?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? j?} \eta_{f? g?} \eta_{h? k?} \delta_{l?}^{i?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? j?} \eta_{f? g?} \eta_{h? l?} \delta_{k?}^{i?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? j?} \eta_{f? g?} \eta_{h? l?} \delta_{m?}^{i?} \delta_{k?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? j?} \eta_{f? g?} \eta_{h? l?} \eta^{i? n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? j?} \eta_{f? g?} \delta_{h?}^{n?} \delta_{l?}^{i?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? j?} \delta_{f?}^{i?} \eta_{g? k?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? j?} \delta_{f?}^{i?} \eta_{g? l?} \eta_{h? m?} \delta_{k?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? j?} \eta_{f? k?} \delta_{g?}^{i?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \eta_{d? j?} \eta_{f? l?} \eta_{g? k?} \delta_{h?}^{n?} \delta_{m?}^{i?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \delta_{d?}^{n?} \eta_{f? g?} \delta_{h?}^{i?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \eta_{b? e?} \delta_{d?}^{n?} \eta_{f? g?} \eta_{h? j?} \delta_{l?}^{i?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? c?} \delta_{b?}^{i?} \delta_{d?}^{n?} \eta_{e? g?} \eta_{f? h?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \eta_{d? h?} \delta_{j?}^{i?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \eta_{d? h?} \eta^{i? n?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \delta_{d?}^{i?} \eta_{h? j?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \delta_{d?}^{i?} \delta_{h?}^{n?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \eta_{d? j?} \delta_{h?}^{i?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \eta_{d? j?} \eta_{h? k?} \delta_{l?}^{i?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \eta_{d? j?} \eta_{h? l?} \delta_{k?}^{i?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \eta_{d? j?} \eta_{h? l?} \delta_{m?}^{i?} \delta_{k?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \eta_{d? j?} \eta_{h? l?} \eta^{i? n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \eta_{d? j?} \delta_{h?}^{n?} \delta_{l?}^{i?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \delta_{d?}^{n?} \delta_{h?}^{i?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? g?} \delta_{d?}^{n?} \eta_{h? j?} \delta_{l?}^{i?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \delta_{c?}^{i?} \eta_{d? j?} \eta_{g? k?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \delta_{c?}^{i?} \eta_{d? j?} \eta_{g? l?} \eta_{h? m?} \delta_{k?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \delta_{c?}^{i?} \eta_{d? j?} \eta_{g? l?} \delta_{h?}^{n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? j?} \eta_{d? k?} \delta_{g?}^{i?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? j?} \eta_{d? k?} \eta_{g? l?} \eta_{h? m?} \eta^{i? n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? f?} \eta_{c? j?} \eta_{d? l?} \delta_{g?}^{i?} \eta_{h? k?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? g?} \eta_{c? f?} \eta_{d? h?} \delta_{j?}^{i?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? g?} \eta_{c? f?} \eta_{d? h?} \eta^{i? n?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \delta_{b?}^{i?} \eta_{c? f?} \eta_{d? j?} \eta_{g? k?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \delta_{b?}^{i?} \eta_{c? f?} \eta_{d? j?} \eta_{g? l?} \delta_{h?}^{n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? j?} \eta_{c? f?} \eta_{d? k?} \delta_{g?}^{i?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta_{a? e?} \eta_{b? j?} \eta_{c? f?} \eta_{d? k?} \eta_{g? l?} \eta_{h? m?} \eta^{i? n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? c? d?} \eta_{e? g?} \eta_{f? h?} \delta_{j?}^{i?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? c? d?} \eta_{e? g?} \eta_{f? h?} \eta^{i? n?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? c? d?} \eta_{e? g?} \delta_{f?}^{i?} \eta_{h? j?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? c? d?} \eta_{e? g?} \eta_{f? j?} \eta_{h? l?} \delta_{k?}^{i?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? c? d?} \eta_{e? g?} \eta_{f? j?} \eta_{h? l?} \eta^{i? n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? c? d?} \eta_{e? g?} \eta_{f? j?} \delta_{h?}^{n?} \delta_{l?}^{i?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? c? d?} \delta_{e?}^{i?} \eta_{f? j?} \eta_{g? k?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? c? d?} \delta_{e?}^{i?} \eta_{f? j?} \eta_{g? l?} \eta_{h? m?} \delta_{k?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? c? d?} \eta_{e? j?} \eta_{f? k?} \eta_{g? l?} \eta_{h? m?} \eta^{i? n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? h?} \delta_{j?}^{i?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? h?} \eta^{i? n?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \delta_{d?}^{i?} \eta_{h? j?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \delta_{d?}^{i?} \delta_{h?}^{n?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? j?} \delta_{h?}^{i?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? j?} \eta_{h? k?} \delta_{l?}^{i?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? j?} \eta_{h? l?} \delta_{k?}^{i?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? j?} \eta_{h? l?} \delta_{m?}^{i?} \delta_{k?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? j?} \eta_{h? l?} \eta^{i? n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? j?} \delta_{h?}^{n?} \delta_{l?}^{i?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \delta_{d?}^{n?} \delta_{h?}^{i?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \delta_{d?}^{n?} \eta_{h? j?} \delta_{l?}^{i?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \delta_{c?}^{i?} \eta_{d? j?} \eta_{g? k?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \delta_{c?}^{i?} \eta_{d? j?} \eta_{g? l?} \eta_{h? m?} \delta_{k?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \delta_{c?}^{i?} \eta_{d? j?} \eta_{g? l?} \delta_{h?}^{n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? j?} \eta_{d? k?} \delta_{g?}^{i?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? j?} \eta_{d? k?} \eta_{g? l?} \eta_{h? m?} \eta^{i? n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? f?} \eta_{c? j?} \eta_{d? l?} \delta_{g?}^{i?} \eta_{h? k?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta^{p i?} \epsilon_{a? b? e? p} \eta_{c? f?} \eta_{d? g?} \eta_{h? j?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta^{p i?} \epsilon_{a? b? e? p} \eta_{c? f?} \eta_{d? g?} \delta_{h?}^{n?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta^{p i?} \epsilon_{a? b? e? p} \eta_{c? f?} \eta_{d? j?} \eta_{g? k?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta^{p i?} \epsilon_{a? b? e? p} \eta_{c? f?} \eta_{d? j?} \eta_{g? l?} \eta_{h? m?} \delta_{k?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta^{p i?} \epsilon_{a? b? e? p} \eta_{c? f?} \eta_{d? j?} \eta_{g? l?} \delta_{h?}^{n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta^{p i?} \epsilon_{a? b? e? p} \eta_{c? g?} \eta_{d? h?} \eta_{f? j?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta^{p i?} \epsilon_{a? b? e? p} \eta_{c? g?} \eta_{d? h?} \delta_{f?}^{n?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta^{p i?} \epsilon_{a? b? e? p} \eta_{c? g?} \eta_{d? j?} \eta_{f? k?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta^{p i?} \epsilon_{a? b? e? p} \eta_{c? g?} \eta_{d? j?} \eta_{f? l?} \delta_{h?}^{n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \eta_{d? g?} \delta_{h?}^{i?} \eta_{k? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \eta_{d? g?} \eta_{h? k?} \delta_{l?}^{i?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \eta_{d? g?} \eta_{h? l?} \delta_{k?}^{i?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \eta_{d? g?} \eta_{h? l?} \delta_{m?}^{i?} \delta_{k?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \eta_{d? g?} \eta_{h? l?} \eta^{i? n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \eta_{d? g?} \delta_{h?}^{n?} \delta_{l?}^{i?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \delta_{d?}^{i?} \eta_{g? k?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \delta_{d?}^{i?} \eta_{g? l?} \eta_{h? m?} \delta_{k?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \delta_{d?}^{i?} \eta_{g? l?} \delta_{h?}^{n?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \eta_{d? k?} \delta_{g?}^{i?} \eta_{h? l?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \eta_{d? k?} \eta_{g? l?} \eta_{h? m?} \eta^{i? n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \eta_{d? l?} \delta_{g?}^{i?} \eta_{h? k?} \delta_{m?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \eta_{d? l?} \delta_{g?}^{i?} \eta_{h? m?} \delta_{k?}^{n?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{a? b? e? j?} \eta_{c? f?} \eta_{d? l?} \eta_{g? k?} \delta_{h?}^{n?} \delta_{m?}^{i?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \eta^{p n?} \epsilon_{a? b? e? p} \eta_{c? f?} \eta_{d? g?} \delta_{h?}^{i?} \eta_{j? l?} \eta_{k? m?} '''),
        Ex(r''' M_{a? b? c? d? e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} -> \epsilon_{e? f? g? h?} \eta_{a? c?} \eta_{b? d?} \delta_{j?}^{i?} \eta_{k? l?} \delta_{m?}^{n?} ''')
      ]
    
    ruleMH1  = Ex(r''' M_{a b c d e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} H^{a b c d} ->(M_{0 \mu 0 \nu e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} - M_{0 \mu \nu 0 e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} - M_{\mu 0 0 \nu e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} + M_{\mu 0 \nu 0 e? f? g? h?}^{i?}_{j? k? l? m?}^{n?}) H1^{\mu \nu} + (M_{0 \mu \nu \rho e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} - M_{\mu 0 \nu \rho e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} + M_{\nu \rho 0 \mu e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} - M_{\nu \rho \mu 0 e? f? g? h?}^{i?}_{j? k? l? m?}^{n?}) H2^{\mu \nu \rho} + M_{\mu \nu \rho \sigma e? f? g? h?}^{i?}_{j? k? l? m?}^{n?} H3^{\mu \nu \rho \sigma}''')

    ruleMH2  = Ex(r''' M_{p? q? r? s? a b c d}^{e}_{f? g? h? i?}^{j?} \partial_{e}{H^{a b c d}} ->(M_{p? q? r? s? 0 \mu 0 \nu}^{0}_{f? g? h? i?}^{j?} - M_{p? q? r? s? 0 \mu \nu 0}^{0}_{f? g? h? i?}^{j?} - M_{p? q? r? s? \mu 0 0 \nu}^{0}_{f? g? h? i?}^{j?} + M_{p? q? r? s? \mu 0 \nu 0}^{0}_{f? g? h? i?}^{j?}) \partial_{0}{H1^{\mu \nu}} + (M_{p? q? r? s? 0 \mu 0 \nu}^{\alpha}_{f? g? h? i?}^{j?} - M_{p? q? r? s? 0 \mu \nu 0}^{\alpha}_{f? g? h? i?}^{j?} - M_{p? q? r? s? \mu 0 0 \nu}^{\alpha}_{f? g? h? i?}^{j?} + M_{p? q? r? s? \mu 0 \nu 0}^{\alpha}_{f? g? h? i?}^{j?}) \partial_{\alpha}{H1^{\mu \nu}} + (M_{p? q? r? s? 0 \mu \nu \rho}^{0}_{f? g? h? i?}^{j?} - M_{p? q? r? s? \mu 0 \nu \rho}^{0}_{f? g? h? i?}^{j?} + M_{p? q? r? s? \nu \rho 0 \mu}^{0}_{f? g? h? i?}^{j?} - M_{p? q? r? s? \nu \rho \mu 0}^{0}_{f? g? h? i?}^{j?}) \partial_{0}{H2^{\mu \nu \rho}} + (M_{p? q? r? s? 0 \mu \nu \rho}^{\alpha}_{f? g? h? i?}^{j?} - M_{p? q? r? s? \mu 0 \nu \rho}^{\alpha}_{f? g? h? i?}^{j?} + M_{p? q? r? s? \nu \rho 0 \mu}^{\alpha}_{f? g? h? i?}^{j?} - M_{p? q? r? s? \nu \rho \mu 0}^{\alpha}_{f? g? h? i?}^{j?}) \partial_{\alpha}{H2^{\mu \nu \rho}} + M_{p? q? r? s? \mu \nu \rho \sigma}^{0}_{f? g? h? i?}^{j?} \partial_{0}{H3^{\mu \nu \rho \sigma}} + M_{p? q? r? s? \mu \nu \rho \sigma}^{\alpha}_{f? g? h? i?}^{j?} \partial_{\alpha}{H3^{\mu \nu \rho \sigma}}''')
    
    ruleMH3  = Ex(r''' M_{p? q? r? s? f? g? h? i?}^{j?}_{a b c d}^{e} \partial_{e}{H^{a b c d}} ->(M_{p? q? r? s? f? g? h? i?}^{j?}_{0 \mu 0 \nu}^{0} - M_{p? q? r? s? f? g? h? i?}^{j?}_{0 \mu \nu 0}^{0} - M_{p? q? r? s? f? g? h? i?}^{j?}_{\mu 0 0 \nu}^{0} + M_{p? q? r? s? f? g? h? i?}^{j?}_{\mu 0 \nu 0}^{0}) \partial_{0}{H1^{\mu \nu}} + (M_{p? q? r? s? f? g? h? i?}^{j?}_{0 \mu 0 \nu}^{\alpha} - M_{p? q? r? s? f? g? h? i?}^{j?}_{0 \mu \nu 0}^{\alpha} - M_{p? q? r? s? f? g? h? i?}^{j?}_{\mu 0 0 \nu}^{\alpha} + M_{p? q? r? s? f? g? h? i?}^{j?}_{\mu 0 \nu 0}^{\alpha}) \partial_{\alpha}{H1^{\mu \nu}} + (M_{p? q? r? s? f? g? h? i?}^{j?}_{0 \mu \nu \rho}^{0} - M_{p? q? r? s? f? g? h? i?}^{j?}_{\mu 0 \nu \rho}^{0} + M_{p? q? r? s? f? g? h? i?}^{j?}_{\nu \rho 0 \mu}^{0} - M_{p? q? r? s? f? g? h? i?}^{j?}_{\nu \rho \mu 0}^{0}) \partial_{0}{H2^{\mu \nu \rho}} + (M_{p? q? r? s? f? g? h? i?}^{j?}_{0 \mu \nu \rho}^{\alpha} - M_{p? q? r? s? f? g? h? i?}^{j?}_{\mu 0 \nu \rho}^{\alpha} + M_{p? q? r? s? f? g? h? i?}^{j?}_{\nu \rho 0 \mu}^{\alpha} - M_{p? q? r? s? f? g? h? i?}^{j?}_{\nu \rho \mu 0}^{\alpha}) \partial_{\alpha}{H2^{\mu \nu \rho}} + M_{p? q? r? s? f? g? h? i?}^{j?}_{\mu \nu \rho \sigma}^{0} \partial_{0}{H3^{\mu \nu \rho \sigma}} + M_{p? q? r? s? f? g? h? i?}^{j?}_{\mu \nu \rho \sigma}^{\alpha} \partial_{\alpha}{H3^{\mu \nu \rho \sigma}}''')
    
    ex  = Ex(r''' M_{a b c d}^{e}_{f g h i}^{j} \partial_{e}{H^{a b c d}} \partial_{j}{H^{f g h i}}''')
    
    terms = []

    for (i,rule) in enumerate(rulesM):
      print(i)
      ex  = Ex('e{{{0}}} '.format(i+1) + r'''M_{a b c d e f g h}^{i}_{j k l m}^{n} H^{a b c d} \partial_{i}{H^{e f g h}} \partial_{n}{H^{j k l m}}''')
    
      substitute(ex, ruleMH1)
      distribute(ex)
      substitute(ex, ruleMH2)
      distribute(ex)
      substitute(ex, ruleMH3)
      distribute(ex)

      substitute(ex, rule)
    
      three_plus_one(ex)

      terms.append(ex)
    
    res = Ex('+'.join([terms[i].input_form() for i in range(len(rulesM))]))

    return(res)

def mass_ABC():
    ruleM1  = Ex(r''' M{1}_{a? b? c? d? e? f? g? h? i? j? k? l?}  -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? h?} \eta_{i? k?} \eta_{j? l?}''')
    ruleM2  = Ex(r''' M{2}_{a? b? c? d? e? f? g? h? i? j? k? l?}  -> \eta_{a? c?} \eta_{b? d?} \eta_{e? g?} \eta_{f? i?} \eta_{h? k?} \eta_{j? l?}''')
    ruleM3  = Ex(r''' M{3}_{a? b? c? d? e? f? g? h? i? j? k? l?}  -> \eta_{a? c?} \eta_{b? d?} \eta_{e? i?} \eta_{f? j?} \eta_{g? k?} \eta_{h? l?}''')
    ruleM4  = Ex(r''' M{4}_{a? b? c? d? e? f? g? h? i? j? k? l?}  -> \eta_{a? c?} \eta_{b? d?} \eta_{e? i?} \eta_{f? k?} \eta_{g? j?} \eta_{h? l?}''')
    ruleM5  = Ex(r''' M{5}_{a? b? c? d? e? f? g? h? i? j? k? l?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? g?} \eta_{f? i?} \eta_{h? k?} \eta_{j? l?}''')
    ruleM6  = Ex(r''' M{6}_{a? b? c? d? e? f? g? h? i? j? k? l?}  -> \eta_{a? c?} \eta_{b? e?} \eta_{d? i?} \eta_{f? g?} \eta_{h? k?} \eta_{j? l?}''')
    ruleM7  = Ex(r''' M{7}_{a? b? c? d? e? f? g? h? i? j? k? l?}  -> \eta_{a? e?} \eta_{b? f?} \eta_{c? i?} \eta_{d? j?} \eta_{g? k?} \eta_{h? l?}''')
    ruleM8  = Ex(r''' M{8}_{a? b? c? d? e? f? g? h? i? j? k? l?}  -> \eta_{a? e?} \eta_{b? f?} \eta_{c? i?} \eta_{d? k?} \eta_{g? j?} \eta_{h? l?}''')
    ruleM9  = Ex(r''' M{9}_{a? b? c? d? e? f? g? h? i? j? k? l?}  -> \epsilon_{a? b? c? d?} \eta_{e? g?} \eta_{f? h?} \eta_{i? k?} \eta_{j? l?}''')
    ruleM10 = Ex(r''' M{10}_{a? b? c? d? e? f? g? h? i? j? k? l?} -> \epsilon_{a? b? c? d?} \eta_{e? g?} \eta_{f? i?} \eta_{h? k?} \eta_{j? l?}''')
    ruleM11 = Ex(r''' M{11}_{a? b? c? d? e? f? g? h? i? j? k? l?} -> \epsilon_{a? b? c? d?} \eta_{e? i?} \eta_{f? j?} \eta_{g? k?} \eta_{h? l?}''')
    ruleM12 = Ex(r''' M{12}_{a? b? c? d? e? f? g? h? i? j? k? l?} -> \epsilon_{a? b? c? d?} \eta_{e? i?} \eta_{f? k?} \eta_{g? j?} \eta_{h? l?}''')
    ruleM13 = Ex(r''' M{13}_{a? b? c? d? e? f? g? h? i? j? k? l?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? h?} \eta_{i? k?} \eta_{j? l?}''')
    ruleM14 = Ex(r''' M{14}_{a? b? c? d? e? f? g? h? i? j? k? l?} -> \epsilon_{a? b? e? f?} \eta_{c? g?} \eta_{d? i?} \eta_{h? k?} \eta_{j? l?}''')
    ruleM15 = Ex(r''' M{15}_{a? b? c? d? e? f? g? h? i? j? k? l?} -> \epsilon_{a? b? e? f?} \eta_{c? i?} \eta_{d? j?} \eta_{g? k?} \eta_{h? l?}''')
    
    ruleM  = Ex(r''' M_{a? b? c? d? e? f? g? h? i? j? k? l?} -> e{1} * M{1}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{2} * M{2}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{3} * M{3}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{4} * M{4}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{5} * M{5}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{6} * M{6}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{7} * M{7}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{8} * M{8}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{9} * M{9}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{10} * M{10}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{11} * M{11}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{12} * M{12}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{13} * M{13}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{14} * M{14}_{a? b? c? d? e? f? g? h? i? j? k? l?} + e{15} * M{15}_{a? b? c? d? e? f? g? h? i? j? k? l?} ''')
    
    ruleMH1  = Ex(r''' M_{a b c d e? f? g? h? i? j? k? l?} H^{a b c d} ->(M_{0 \mu 0 \nu e? f? g? h? i? j? k? l?} - M_{0 \mu \nu 0 e? f? g? h? i? j? k? l?} - M_{\mu 0 0 \nu e? f? g? h? i? j? k? l?} + M_{\mu 0 \nu 0 e? f? g? h? i? j? k? l?}) H1^{\mu \nu} + (M_{0 \mu \nu \rho e? f? g? h? i? j? k? l?} - M_{\mu 0 \nu \rho e? f? g? h? i? j? k? l?} + M_{\nu \rho 0 \mu e? f? g? h? i? j? k? l?} - M_{\nu \rho \mu 0 e? f? g? h? i? j? k? l?}) H2^{\mu \nu \rho} + M_{\mu \nu \rho \sigma e? f? g? h? i? j? k? l?} H3^{\mu \nu \rho \sigma}''')
    
    ruleMH2  = Ex(r''' M_{e? f? g? h? a b c d i? j? k? l?} H^{a b c d} ->(M_{e? f? g? h? 0 \mu 0 \nu i? j? k? l?} - M_{e? f? g? h? 0 \mu \nu 0 i? j? k? l?} - M_{e? f? g? h? \mu 0 0 \nu i? j? k? l?} + M_{e? f? g? h? \mu 0 \nu 0 i? j? k? l?}) H1^{\mu \nu} + (M_{e? f? g? h? 0 \mu \nu \rho i? j? k? l?} - M_{e? f? g? h? \mu 0 \nu \rho i? j? k? l?} + M_{e? f? g? h? \nu \rho 0 \mu i? j? k? l?} - M_{e? f? g? h? \nu \rho \mu 0 i? j? k? l?}) H2^{\mu \nu \rho} + M_{e? f? g? h? \mu \nu \rho \sigma i? j? k? l?} H3^{\mu \nu \rho \sigma}''')

    ruleMH3  = Ex(r''' M_{e? f? g? h? i? j? k? l? a b c d} H^{a b c d} ->(M_{e? f? g? h? i? j? k? l? 0 \mu 0 \nu} - M_{e? f? g? h? i? j? k? l? 0 \mu \nu 0} - M_{e? f? g? h? i? j? k? l? \mu 0 0 \nu} + M_{e? f? g? h? i? j? k? l? \mu 0 \nu 0}) H1^{\mu \nu} + (M_{e? f? g? h? i? j? k? l? 0 \mu \nu \rho} - M_{e? f? g? h? i? j? k? l? \mu 0 \nu \rho} + M_{e? f? g? h? i? j? k? l? \nu \rho 0 \mu} - M_{e? f? g? h? i? j? k? l? \nu \rho \mu 0}) H2^{\mu \nu \rho} + M_{e? f? g? h? i? j? k? l? \mu \nu \rho \sigma} H3^{\mu \nu \rho \sigma}''')
    
    ex  = Ex(r''' M_{a b c d e f g h i j k l} H^{a b c d} H^{e f g h} H^{i j k l}''')
    
    substitute(ex, ruleMH1)
    distribute(ex)
    substitute(ex, ruleMH2)
    distribute(ex)
    substitute(ex, ruleMH3)
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
    
    three_plus_one(ex)
    
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

def eom(massABC, kinABCI, kinABpCq, toVary):
    shift(kinABCI, kinABpCq)

    apply_sol(massABC)
    apply_sol(kinABCI)
    apply_sol(kinABpCq)

    variation = Ex(r'd' + toVary.input_form())
    ruleVary = Ex(r'@{toVary} -> @{variation}')

    ex = Ex(r'\int{@(massABC) + @(kinABCI) + @(kinABpCq)}{x}')

    distribute(ex, repeat=True)
    my_canonicalise(ex)

    vary(ex, ruleVary)

    integrate_by_parts(ex, Ex(r'\partial_{\alpha?}{@(variation)}'), repeat=True)
    unwrap(ex, repeat=True)
    product_rule(ex, repeat=True)
    distribute(ex, repeat=True)
    my_canonicalise(ex)

    integrate_by_parts(ex, Ex(r'\partial^{\alpha?}{@(variation)}'), repeat=True)
    unwrap(ex, repeat=True)
    product_rule(ex, repeat=True)
    distribute(ex, repeat=True)
    my_canonicalise(ex)

    integrate_by_parts(ex, variation, repeat=True)
    unwrap(ex, repeat=True)
    product_rule(ex, repeat=True)
    distribute(ex, repeat=True)
    my_canonicalise(ex)

    factor_out(ex, variation)

    return ex

def eom_from_files(toVary):
    ex1 = load_AB()
    ex2 = load_ABI()
    ex3 = load_ApBq()

    my_eliminate_metric(ex1)
    eliminate_kronecker(ex1, repeat=True)
    my_canonicalise(ex1)
    substitute(ex1, ruleTraceFree1)
    substitute(ex1, ruleTraceFree2)

    my_eliminate_metric(ex2)
    eliminate_kronecker(ex2, repeat=True)
    my_canonicalise(ex2)
    substitute(ex2, ruleTraceFree1)
    substitute(ex2, ruleTraceFree2)

    my_eliminate_metric(ex3)
    eliminate_kronecker(ex3, repeat=True)
    my_canonicalise(ex3)
    substitute(ex3, ruleTraceFree1)
    substitute(ex3, ruleTraceFree2)

    return eom(ex1, ex2, ex3, toVary)

def tt(ex):
  substitute(ex, Ex(r'''\int{Q??}{x} -> Q??'''))
  distribute(ex)
  my_canonicalise(ex)
  substitute(ex, Ex(r'''A -> 0'''))
  substitute(ex, Ex(r'''B^{\alpha} -> 0'''))
  substitute(ex, Ex(r'''U^{\mu \nu} \gamma_{\mu \nu} -> 0'''))
  substitute(ex, Ex(r'''V^{\mu \nu} \gamma_{\mu \nu} -> 0'''))
  substitute(ex, Ex(r'''W^{\mu \nu} \gamma_{\mu \nu} -> 0'''))
  substitute(ex, Ex(r'''U^{\nu \mu} \gamma_{\mu \nu} -> 0'''))
  substitute(ex, Ex(r'''V^{\nu \mu} \gamma_{\mu \nu} -> 0'''))
  substitute(ex, Ex(r'''W^{\nu \mu} \gamma_{\mu \nu} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? q?}{U^{\mu \nu}} \gamma_{\mu \nu} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? q?}{V^{\mu \nu}} \gamma_{\mu \nu} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? q?}{W^{\mu \nu}} \gamma_{\mu \nu} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? q?}{U^{\nu \mu}} \gamma_{\mu \nu} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? q?}{V^{\nu \mu}} \gamma_{\mu \nu} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? q?}{W^{\nu \mu}} \gamma_{\mu \nu} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? \mu}{U^{q? \mu}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? \mu}{V^{q? \mu}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? \mu}{W^{q? \mu}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? \mu}{U^{\mu q?}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? \mu}{V^{\mu q?}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? \mu}{W^{\mu q?}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\mu p?}{U^{q? \mu}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\mu p?}{V^{q? \mu}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\mu p?}{W^{q? \mu}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\mu p?}{U^{\mu q?}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\mu p?}{V^{\mu q?}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\mu p?}{W^{\mu q?}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\mu \nu}{U^{\mu \nu}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\mu \nu}{V^{\mu \nu}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\mu \nu}{W^{\mu \nu}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\mu \nu}{U^{\nu \mu}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\mu \nu}{V^{\nu \mu}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\mu \nu}{W^{\nu \mu}} -> 0'''))

  simplify3d(ex)

  factor_in(ex, Ex(r'''k{1}, k{2}, k{3}, k{4}, k{5}, k{6}, k{7}, k{8}, k{9}, k{10}, k{11}, k{12}, k{13}, k{14}, k{15}, k{16}'''))

def vector(ex):
  substitute(ex, Ex(r'''\int{Q??}{x} -> Q??'''))
  distribute(ex)
  my_canonicalise(ex)
  substitute(ex, Ex(r'''A -> 0'''))
  substitute(ex, Ex(r'''U^{\alpha \beta} -> \gamma^{\alpha \mu} \partial_{\mu}{U^{\beta}} + \gamma^{\beta \mu} \partial_{\mu}{U^{\alpha}}'''))
  substitute(ex, Ex(r'''V^{\alpha \beta} -> \gamma^{\alpha \mu} \partial_{\mu}{U^{\beta}} + \gamma^{\beta \mu} \partial_{\mu}{U^{\alpha}}'''))
  substitute(ex, Ex(r'''W^{\alpha \beta} -> \gamma^{\alpha \mu} \partial_{\mu}{W^{\beta}} + \gamma^{\beta \mu} \partial_{\mu}{W^{\alpha}}'''))

  simplify3d(ex)

  substitute(ex, Ex(r'''\partial_{\alpha}{B^{\alpha}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\alpha}{U^{\alpha}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\alpha}{W^{\alpha}} -> 0'''))

  substitute(ex, Ex(r'''\partial_{p? \alpha}{B^{\alpha}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? \alpha}{U^{\alpha}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? \alpha}{W^{\alpha}} -> 0'''))

  substitute(ex, Ex(r'''\partial_{\alpha p?}{B^{\alpha}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\alpha p?}{U^{\alpha}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\alpha p?}{W^{\alpha}} -> 0'''))

  substitute(ex, Ex(r'''\partial_{p? q? \alpha}{B^{\alpha}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? q? \alpha}{U^{\alpha}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? q? \alpha}{W^{\alpha}} -> 0'''))

  substitute(ex, Ex(r'''\partial_{p? \alpha q?}{B^{\alpha}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? \alpha q?}{U^{\alpha}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{p? \alpha q?}{W^{\alpha}} -> 0'''))

  substitute(ex, Ex(r'''\partial_{\alpha p? q?}{B^{\alpha}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\alpha p? q?}{U^{\alpha}} -> 0'''))
  substitute(ex, Ex(r'''\partial_{\alpha p? q?}{W^{\alpha}} -> 0'''))

  simplify3d(ex)

  factor_in(ex, Ex(r'''k{1}, k{2}, k{3}, k{4}, k{5}, k{6}, k{7}, k{8}, k{9}, k{10}, k{11}, k{12}, k{13}, k{14}, k{15}, k{16}'''))

def scalar(ex):
  substitute(ex, Ex(r'''\int{Q??}{x} -> Q??'''))
  distribute(ex)
  my_canonicalise(ex)
  substitute(ex, Ex(r'''B^{\alpha} -> 0'''))
  substitute(ex, Ex(r'''U^{\alpha \beta} -> \gamma^{\alpha \beta} U1 - (\gamma^{\alpha \mu} \gamma^{\beta \nu} \partial_{\mu \nu}{V2} + 1/3 \gamma^{\alpha \beta} \gamma^{\mu \nu} \partial_{\mu \nu}{V2})'''))
  substitute(ex, Ex(r'''V^{\alpha \beta} -> \gamma^{\alpha \beta} V1 + (\gamma^{\alpha \mu} \gamma^{\beta \nu} \partial_{\mu \nu}{V2} - 1/3 \gamma^{\alpha \beta} \gamma^{\mu \nu} \partial_{\mu \nu}{V2})'''))
  substitute(ex, Ex(r'''W^{\alpha \beta} -> (\gamma^{\alpha \mu} \gamma^{\beta \nu} \partial_{\mu \nu}{W2} - 1/3 \gamma^{\alpha \beta} \gamma^{\mu \nu} \partial_{\mu \nu}{W2})'''))

  sort_product(ex)
  sort_sum(ex)
  canonicalise(ex)
  rename_dummies(ex)

  factor_in(ex, Ex(r'''k{1}, k{2}, k{3}, k{4}, k{5}, k{6}, k{7}, k{8}, k{9}, k{10}, k{11}, k{12}, k{13}, k{14}, k{15}, k{16}'''))

def apply_sol(ex):
    substitute(ex, Ex(r'''e{1} -> 1*k{1}'''))
    substitute(ex, Ex(r'''e{2} -> 1*k{2}'''))
    substitute(ex, Ex(r'''e{3} -> (-2)*k{1} + (-2/3)*k{2}'''))
    substitute(ex, Ex(r'''e{4} -> 4*k{1} + 1/3*k{2}'''))
    substitute(ex, Ex(r'''e{5} -> 1*k{3}'''))
    substitute(ex, Ex(r'''e{6} -> (-3)*k{1} + (-1/2)*k{2} + (-3)*k{3}'''))
    substitute(ex, Ex(r'''e{7} -> 1*k{4}'''))
    substitute(ex, Ex(r'''e{8} -> 1*k{5}'''))
    substitute(ex, Ex(r'''e{9} -> 1*k{6}'''))
    substitute(ex, Ex(r'''e{10} -> 1*k{7}'''))
    substitute(ex, Ex(r'''e{11} -> 1*k{8}'''))
    substitute(ex, Ex(r'''e{12} -> 1/2*k{6} + 5/8*k{7}'''))
    substitute(ex, Ex(r'''e{13} -> (-16/3)*k{4} + 16*k{5} + (-7/3)*k{6} + (-5/12)*k{7} + 4/3*k{8}'''))
    substitute(ex, Ex(r'''e{14} -> (-8/3)*k{4} + 8*k{5} + (-13/6)*k{6} + (-11/24)*k{7} + 2/3*k{8}'''))
    substitute(ex, Ex(r'''e{15} -> 1*k{4} + (-1/8)*k{6} + (-23/32)*k{7} + (-1/2)*k{8}'''))
    substitute(ex, Ex(r'''e{16} -> 1*k{9}'''))
    substitute(ex, Ex(r'''e{17} -> 1*k{10}'''))
    substitute(ex, Ex(r'''e{18} -> 3/2*k{4} + 3/4*k{6} + (-3/16)*k{7} + 3*k{9}'''))
    substitute(ex, Ex(r'''e{19} -> 1/2*k{4} + 1/4*k{6} + (-1/16)*k{7} + 1*k{9}'''))
    substitute(ex, Ex(r'''e{20} -> (-1/4)*k{4} + (-1/8)*k{6} + 1/32*k{7} + (-1/2)*k{9}'''))
    substitute(ex, Ex(r'''e{21} -> 1*k{4} + (-3)*k{5} + 1/4*k{6} + (-3/16)*k{7} + (-1/2)*k{8} + 1*k{9} + (-3)*k{10}'''))
    substitute(ex, Ex(r'''e{22} -> 1*k{11}'''))
    substitute(ex, Ex(r'''e{23} -> 1*k{12}'''))
    substitute(ex, Ex(r'''e{24} -> 1*k{13}'''))
    substitute(ex, Ex(r'''e{25} -> 1*k{14}'''))
    substitute(ex, Ex(r'''e{26} -> 1*k{6} + 3/4*k{7} + (-1)*k{14}'''))
    substitute(ex, Ex(r'''e{27} -> (-1)*k{4} + 1/2*k{7}'''))
    substitute(ex, Ex(r'''e{28} -> 5/3*k{4} + 5/12*k{6} + (-25/48)*k{7} + (-2)*k{11} + (-1)*k{12} + (-2/3)*k{13} + (-1/4)*k{14}'''))
    substitute(ex, Ex(r'''e{29} -> 1*k{6} + 3/4*k{7} + (-1)*k{14}'''))
    substitute(ex, Ex(r'''e{30} -> (-4/3)*k{4} + (-5/6)*k{6} + 1/24*k{7} + 4*k{11} + 2*k{12} + 1/3*k{13} + 1/2*k{14}'''))
    substitute(ex, Ex(r'''e{31} -> 1*k{15}'''))
    substitute(ex, Ex(r'''e{32} -> 1*k{16}'''))
    substitute(ex, Ex(r'''e{33} -> 1*k{4} + (-1/2)*k{7} + (-3)*k{11} + (-1/2)*k{13} + (-6)*k{15}'''))
    substitute(ex, Ex(r'''e{34} -> 1/2*k{6} + 3/8*k{7} + (-3/2)*k{12} + (-1/2)*k{14} + (-3)*k{16}'''))
    substitute(ex, Ex(r'''e{35} -> (-2)*k{4} + (-1)*k{6} + 1/4*k{7}'''))
    substitute(ex, Ex(r'''e{36} -> (-1)*k{4} + 1/2*k{7} + (-3/2)*k{12} + (-1/2)*k{14} + (-3)*k{16}'''))
    substitute(ex, Ex(r'''e{37} -> 1/12*k{4} + 1/12*k{6} + 1/48*k{7} + (-1/8)*k{12} + (-1/24)*k{14} + 1*k{15} + 1/4*k{16}'''))
    substitute(ex, Ex(r'''e{38} -> (-2)*k{4} + 1*k{7}'''))
    substitute(ex, Ex(r'''e{39} -> (-2)*k{6} + (-3/2)*k{7}'''))
    substitute(ex, Ex(r'''e{40} -> 1*k{4} + 1/2*k{6} + (-1/8)*k{7}'''))
    substitute(ex, Ex(r'''e{41} -> 1*k{17}'''))
    substitute(ex, Ex(r'''e{42} -> 1*k{18}'''))
    substitute(ex, Ex(r'''e{43} -> 1*k{19}'''))
    substitute(ex, Ex(r'''e{44} -> 1*k{20}'''))
    substitute(ex, Ex(r'''e{45} -> (-1)*k{1} + (-1/4)*k{2} + (-1)*k{18} + (-2)*k{19} + (-1)*k{20}'''))
    substitute(ex, Ex(r'''e{46} -> 1*k{1} + 1/4*k{2} + 1*k{18} + 2*k{19} + 1*k{20}'''))
    substitute(ex, Ex(r'''e{47} -> (-3/4)*k{1} + 1/16*k{2} + (-18)*k{17} + (-9/4)*k{18} + 1/2*k{19} + 7/4*k{20}'''))
    substitute(ex, Ex(r'''e{48} -> 11/6*k{1} + 1/8*k{2} + 36*k{17} + 29/6*k{18} + (-1/3)*k{19} + (-19/6)*k{20}'''))
    substitute(ex, Ex(r'''e{49} -> 1*k{21}'''))
    substitute(ex, Ex(r'''e{50} -> (-5/3)*k{1} + (-1/4)*k{2} + (-2)*k{3} + (-1/6)*k{18} + (-1/3)*k{19} + (-5/3)*k{20} + (-12)*k{21}'''))
    substitute(ex, Ex(r'''e{51} -> 169/216*k{1} + 31/288*k{2} + 7/12*k{3} + 1*k{17} + 43/216*k{18} + 13/108*k{19} + 139/216*k{20} + 14/3*k{21}'''))
    substitute(ex, Ex(r'''e{52} -> 11/108*k{1} + 5/144*k{2} + 1/3*k{3} + (-2)*k{17} + (-25/108)*k{18} + 5/54*k{19} + 41/108*k{20} + 8/3*k{21}'''))
    substitute(ex, Ex(r'''e{53} -> 5/8*k{1} + 1/8*k{2} + 3/4*k{3} + (-9/2)*k{17} + (-1/2)*k{18} + 1/2*k{19} + 1*k{20} + 3*k{21}'''))
    substitute(ex, Ex(r'''e{54} -> 13/4*k{1} + 7/16*k{2} + 3*k{3} + 1/4*k{18} + 3/2*k{19} + 9/4*k{20} + 12*k{21}'''))
    substitute(ex, Ex(r'''e{55} -> (-7/4)*k{1} + (-3/16)*k{2} + (-3/2)*k{3} + (-1/4)*k{18} + (-3/2)*k{19} + (-9/4)*k{20} + (-12)*k{21}'''))
    substitute(ex, Ex(r'''e{56} -> 1*k{22}'''))
    substitute(ex, Ex(r'''e{57} -> 1*k{23}'''))
    substitute(ex, Ex(r'''e{58} -> (-3)*k{4} + 11/16*k{6} + 143/64*k{7} + 3/4*k{8} + (-3/4)*k{11} + (-1/2)*k{12} + (-1/16)*k{14} + (-3/2)*k{22}'''))
    substitute(ex, Ex(r'''e{59} -> 4*k{4} + (-3/4)*k{6} + (-47/16)*k{7} + (-1)*k{8} + 1*k{11} + 1/4*k{14} + 2*k{22}'''))
    substitute(ex, Ex(r'''e{60} -> 1*k{24}'''))
    substitute(ex, Ex(r'''e{61} -> (-1)*k{4} + 3/16*k{6} + 47/64*k{7} + 1/4*k{8} + 1/4*k{11} + (-1/4)*k{12} + (-1/16)*k{14} + 1/2*k{22}'''))
    substitute(ex, Ex(r'''e{62} -> 1*k{25}'''))
    substitute(ex, Ex(r'''e{63} -> 3*k{4} + (-3/4)*k{6} + (-9/4)*k{7} + (-3/4)*k{8} + 1/2*k{11} + 1/2*k{12} + 1/8*k{14} + 1*k{22} + 1/2*k{25}'''))
    substitute(ex, Ex(r'''e{64} -> 1*k{26}'''))
    substitute(ex, Ex(r'''e{65} -> 1*k{27}'''))
    substitute(ex, Ex(r'''e{66} -> 1*k{28}'''))
    substitute(ex, Ex(r'''e{67} -> 4*k{4} + (-1/4)*k{6} + (-37/16)*k{7} + (-1)*k{8} + (-1/2)*k{13} + (-5/4)*k{14} + (-1)*k{27}'''))
    substitute(ex, Ex(r'''e{68} -> (-2/3)*k{4} + 7/8*k{6} + 97/96*k{7} + 1/6*k{8} + (-1/12)*k{13} + (-5/8)*k{14} + (-1/6)*k{27}'''))
    substitute(ex, Ex(r'''e{69} -> (-4)*k{4} + 3/4*k{6} + 47/16*k{7} + 1*k{8} + 1/2*k{13} + (-1/4)*k{14} + 1*k{27}'''))
    substitute(ex, Ex(r'''e{70} -> 2/3*k{4} + 3/8*k{6} + (-19/96)*k{7} + (-1/6)*k{8} + (-5/2)*k{11} + 1/4*k{12} + (-2/3)*k{13} + (-1/4)*k{14} + (-1)*k{22} + (-2)*k{24} + (-4)*k{26} + (-1/3)*k{27}'''))
    substitute(ex, Ex(r'''e{71} -> 4/3*k{4} + (-3/4)*k{6} + (-61/48)*k{7} + (-1/3)*k{8} + 1/6*k{13} + 1/4*k{14} + 1/3*k{27}'''))
    substitute(ex, Ex(r'''e{72} -> 1*k{29}'''))
    substitute(ex, Ex(r'''e{73} -> 1*k{30}'''))
    substitute(ex, Ex(r'''e{74} -> (-2/3)*k{4} + 8*k{5} + (-5/12)*k{6} + (-67/48)*k{7} + (-1/3)*k{8}'''))
    substitute(ex, Ex(r'''e{75} -> (-13/3)*k{4} + 4*k{5} + (-7/12)*k{6} + 41/24*k{7} + 4/3*k{8} + 1/4*k{13} + 3/8*k{14} + 1/2*k{27}'''))
    substitute(ex, Ex(r'''e{76} -> 8/3*k{4} + 3/4*k{6} + (-71/48)*k{7} + (-5/3)*k{8} + (-1/6)*k{13} + (-3/4)*k{14} + (-1/3)*k{27}'''))
    substitute(ex, Ex(r'''e{77} -> (-2)*k{4} + (-1/2)*k{6} + 7/8*k{7} + 1*k{8} + 1/2*k{13} + 5/4*k{14} + 1*k{27} + (-1)*k{29}'''))
    substitute(ex, Ex(r'''e{78} -> 1*k{31}'''))
    substitute(ex, Ex(r'''e{79} -> 4*k{4} + 3/2*k{6} + (-15/8)*k{7} + (-2)*k{8} + (-1)*k{13} + (-1)*k{14} + (-2)*k{27} + 2*k{29} + (-1)*k{31}'''))
    substitute(ex, Ex(r'''e{80} -> (-4/3)*k{4} + (-1)*k{6} + 5/6*k{7} + 4/3*k{8} + 1/3*k{13} + 1/2*k{14} + 2/3*k{27} + (-2)*k{29} + 1*k{31}'''))
    substitute(ex, Ex(r'''e{81} -> 4/3*k{4} + (-5/8)*k{6} + (-119/96)*k{7} + (-1/3)*k{8} + 5/2*k{11} + (-1/4)*k{12} + 2/3*k{13} + 1/4*k{14} + 1*k{22} + 2*k{24} + 4*k{26} + 1/3*k{27}'''))
    substitute(ex, Ex(r'''e{82} -> (-10/3)*k{4} + (-3/4)*k{6} + 73/48*k{7} + 1/3*k{8} + 4/3*k{13} + 1/2*k{14} + 2/3*k{27} + (-1)*k{29}'''))
    substitute(ex, Ex(r'''e{83} -> (-4)*k{4} + (-1/2)*k{6} + 21/8*k{7} + 2*k{8}'''))
    substitute(ex, Ex(r'''e{84} -> 1*k{4} + (-1/4)*k{6} + (-1/2)*k{7} + (-1/4)*k{13} + (-3/8)*k{14} + (-1/2)*k{27}'''))
    substitute(ex, Ex(r'''e{85} -> (-2/3)*k{4} + 3/2*k{6} + 2/3*k{7} + (-1/3)*k{8} + 1/6*k{13} + 3/4*k{14} + 1/3*k{27}'''))
    substitute(ex, Ex(r'''e{86} -> 2*k{4} + (-1/4)*k{6} + (-23/16)*k{7} + (-1)*k{8}'''))
    substitute(ex, Ex(r'''e{87} -> 19/6*k{4} + (-9/8)*k{6} + (-235/96)*k{7} + (-1/6)*k{8} + 1/12*k{13} + 5/8*k{14} + 1/6*k{27} + (-1)*k{30}'''))
    substitute(ex, Ex(r'''e{88} -> 3/2*k{6} + 7/8*k{7} + (-3/2)*k{13} + (-3/4)*k{14} + (-1)*k{27} + 1*k{29}'''))
    substitute(ex, Ex(r'''e{89} -> 1/2*k{4} + 1/2*k{5} + (-1/16)*k{6} + (-23/64)*k{7}'''))
    substitute(ex, Ex(r'''e{90} -> 1*k{32}'''))
    substitute(ex, Ex(r'''e{91} -> 1*k{33}'''))
    substitute(ex, Ex(r'''e{92} -> 2*k{4} + (-1/4)*k{6} + (-23/16)*k{7} + (-3/2)*k{8} + 1*k{29}'''))
    substitute(ex, Ex(r'''e{93} -> (-1)*k{4} + 1/8*k{6} + 23/32*k{7} + (-1/4)*k{8} + 1*k{30}'''))
    substitute(ex, Ex(r'''e{94} -> (-4)*k{4} + (-3/4)*k{6} + 37/16*k{7} + 2*k{8} + 1/2*k{13} + 5/4*k{14} + 1*k{27} + (-1)*k{29}'''))
    substitute(ex, Ex(r'''e{95} -> 4*k{4} + (-1/2)*k{6} + (-23/8)*k{7} + (-2)*k{8} + 1*k{31}'''))
    substitute(ex, Ex(r'''e{96} -> 4*k{4} + 3/2*k{6} + (-19/8)*k{7} + (-2)*k{8} + (-1)*k{13} + (-1)*k{14} + (-2)*k{27} + 2*k{29} + (-1)*k{31}'''))
    substitute(ex, Ex(r'''e{97} -> (-2)*k{4} + (-2)*k{6} + 3/8*k{7} + 3/2*k{8} + 1/2*k{13} + 5/4*k{14} + 1*k{27} + (-2)*k{29} + 1*k{31}'''))
    substitute(ex, Ex(r'''e{98} -> 4/3*k{4} + (-7/8)*k{6} + (-125/96)*k{7} + (-4/3)*k{8} + (-5/2)*k{11} + 1/4*k{12} + 2/3*k{13} + 1/2*k{14} + (-1)*k{22} + (-2)*k{24} + (-4)*k{26} + 1/3*k{27}'''))
    substitute(ex, Ex(r'''e{99} -> (-10/3)*k{4} + (-1)*k{6} + 29/24*k{7} + 5/6*k{8} + 4/3*k{13} + 1/2*k{14} + 2/3*k{27} + (-1)*k{29}'''))
    substitute(ex, Ex(r'''e{100} -> 7/6*k{4} + (-7/8)*k{6} + (-97/96)*k{7} + 1/3*k{8} + 1/12*k{13} + 5/8*k{14} + 1/6*k{27} + (-1)*k{30}'''))
    substitute(ex, Ex(r'''e{101} -> 4*k{4} + 1*k{6} + (-2)*k{7} + (-1)*k{8} + (-3/2)*k{13} + (-3/4)*k{14} + (-1)*k{27} + 1*k{29}'''))
    substitute(ex, Ex(r'''e{102} -> (-109/18)*k{4} + 8/3*k{6} + 269/36*k{7} + 143/36*k{8} + 13/3*k{11} + 5/3*k{12} + (-25/36)*k{13} + (-17/12)*k{14} + (-20/3)*k{22} + 48*k{23} + 20/3*k{24} + (-3)*k{25} + 16/3*k{26} + (-13/18)*k{27} + 8*k{28} + 3*k{32}'''))
    substitute(ex, Ex(r'''e{103} -> (-16/9)*k{4} + 35/24*k{6} + 689/288*k{7} + 49/36*k{8} + 11/3*k{11} + 19/12*k{12} + (-17/36)*k{13} + (-23/24)*k{14} + (-10/3)*k{22} + 24*k{23} + 10/3*k{24} + (-3/2)*k{25} + 8/3*k{26} + (-29/18)*k{27} + 4*k{28}'''))
    substitute(ex, Ex(r'''e{104} -> (-5/6)*k{4} + (-5/12)*k{6} + 13/16*k{7} + 5/12*k{8} + (-1)*k{11} + (-1/2)*k{12} + 1/12*k{13} + 1/2*k{14} + 5/6*k{27} + 1*k{32}'''))
    substitute(ex, Ex(r'''e{105} -> (-85/36)*k{4} + 11/12*k{6} + 161/72*k{7} + 101/72*k{8} + 25/6*k{11} + 11/6*k{12} + (-19/72)*k{13} + (-5/6)*k{14} + (-10/3)*k{22} + 24*k{23} + 10/3*k{24} + (-3/2)*k{25} + 8/3*k{26} + (-55/36)*k{27} + 4*k{28} + (-1/2)*k{32}'''))
    substitute(ex, Ex(r'''e{106} -> (-187/72)*k{4} + (-5)*k{5} + 13/16*k{6} + 193/72*k{7} + 79/72*k{8} + 101/24*k{11} + (-7/12)*k{12} + 1/18*k{13} + (-13/48)*k{14} + 25/12*k{22} + (-6)*k{23} + 8/3*k{24} + (-3/8)*k{25} + 25/3*k{26} + 19/36*k{27} + (-2)*k{28} + 1*k{32} + (-3)*k{33}'''))
    substitute(ex, Ex(r'''e{107} -> 50/9*k{4} + (-29/12)*k{6} + (-797/144)*k{7} + (-29/9)*k{8} + (-22/3)*k{11} + (-19/6)*k{12} + 4/9*k{13} + 7/6*k{14} + 20/3*k{22} + (-48)*k{23} + (-20/3)*k{24} + 3*k{25} + (-16/3)*k{26} + 20/9*k{27} + (-8)*k{28}'''))
    substitute(ex, Ex(r'''e{108} -> 1*k{4} + (-1/4)*k{6} + (-23/16)*k{7} + (-1/2)*k{8} + (-1)*k{27} + (-2)*k{32}'''))
    substitute(ex, Ex(r'''e{109} -> 1*k{4} + (-2)*k{5} + (-11/16)*k{7} + (-1/4)*k{8} + 5/2*k{11} + (-1/4)*k{12} + (-1/8)*k{14} + 1*k{22} + 2*k{24} + 4*k{26} + (-1)*k{28} + (-2)*k{33}'''))
    substitute(ex, Ex(r'''e{110} -> 1*k{4} + (-5/2)*k{6} + (-35/8)*k{7} + (-3/2)*k{8} + 6*k{11} + 3*k{12} + 1/2*k{13} + 1/2*k{14} + (-3)*k{27} + (-6)*k{32}'''))
    substitute(ex, Ex(r'''e{111} -> 1/3*k{4} + (-7/6)*k{6} + (-37/24)*k{7} + (-1/2)*k{8} + 2*k{11} + 1*k{12} + 1/6*k{13} + 1/2*k{14} + (-1)*k{27} + (-2)*k{32}'''))
    substitute(ex, Ex(r'''e{112} -> (-1/6)*k{4} + 1/12*k{6} + 31/48*k{7} + 1/4*k{8} + (-1)*k{11} + (-1/2)*k{12} + (-1/12)*k{13} + (-1/4)*k{14} + 1/2*k{27} + 1*k{32}'''))
    substitute(ex, Ex(r'''e{113} -> 43/36*k{4} + 10*k{5} + (-1)*k{6} + (-707/288)*k{7} + (-25/36)*k{8} + (-71/12)*k{11} + 11/12*k{12} + (-1/9)*k{13} + 5/12*k{14} + (-19/6)*k{22} + 12*k{23} + (-10/3)*k{24} + 3/4*k{25} + (-38/3)*k{26} + (-19/18)*k{27} + 4*k{28} + (-2)*k{32} + 6*k{33}'''))
    substitute(ex, Ex(r'''e{114} -> 1*k{34}'''))
    substitute(ex, Ex(r'''e{115} -> 1*k{35}'''))
    substitute(ex, Ex(r'''e{116} -> (-5/32)*k{4} + (-7/64)*k{6} + (-1/256)*k{7} + (-5/16)*k{9} + 3/32*k{12} + 1/32*k{14} + (-3/4)*k{15} + (-5/16)*k{16} + (-3/2)*k{34}'''))
    substitute(ex, Ex(r'''e{117} -> 1*k{36}'''))
    substitute(ex, Ex(r'''e{118} -> 11/18*k{4} + (-2)*k{5} + (-5/96)*k{6} + (-89/1152)*k{7} + (-5/72)*k{8} + 1/2*k{9} + (-1)*k{10} + (-5/12)*k{11} + 23/48*k{12} + (-1/36)*k{13} + 5/48*k{14} + (-1)*k{15} + (-1/6)*k{22} + (-1/3)*k{24} + (-3/8)*k{25} + (-2/3)*k{26} + (-1/18)*k{27} + 2*k{34} + (-12)*k{35}'''))
    substitute(ex, Ex(r'''e{119} -> (-1/32)*k{4} + (-3/64)*k{6} + (-5/256)*k{7} + (-1/16)*k{9} + 3/32*k{12} + 1/32*k{14} + 1/4*k{15} + (-1/16)*k{16} + 1/2*k{34}'''))
    substitute(ex, Ex(r'''e{120} -> (-79/27)*k{4} + 4*k{5} + 43/72*k{6} + 1325/864*k{7} + 23/54*k{8} + (-5/3)*k{9} + 8/3*k{10} + (-23/18)*k{11} + (-37/18)*k{12} + 1/27*k{13} + (-17/36)*k{14} + (-4/3)*k{15} + (-1/3)*k{16} + 5/9*k{22} + (-8)*k{23} + (-8/9)*k{24} + 1*k{25} + 20/9*k{26} + 5/27*k{27} + (-2/3)*k{28} + (-8)*k{34} + 32*k{35}'''))
    substitute(ex, Ex(r'''e{121} -> (-289/216)*k{4} + 2*k{5} + 13/36*k{6} + 649/864*k{7} + 23/108*k{8} + (-7/12)*k{9} + 4/3*k{10} + (-23/36)*k{11} + (-37/36)*k{12} + 1/54*k{13} + (-17/72)*k{14} + (-2/3)*k{15} + 1/3*k{16} + 5/18*k{22} + (-4)*k{23} + (-4/9)*k{24} + 1/2*k{25} + 10/9*k{26} + 5/54*k{27} + (-1/3)*k{28} + (-4)*k{34} + 16*k{35} + 1/2*k{36}'''))
    substitute(ex, Ex(r'''e{122} -> (-167/576)*k{4} + 1*k{5} + 19/384*k{6} + 223/4608*k{7} + 5/144*k{8} + (-7/32)*k{9} + 1/2*k{10} + 5/24*k{11} + (-55/192)*k{12} + 1/72*k{13} + (-13/192)*k{14} + (-1/8)*k{15} + (-1/32)*k{16} + 1/12*k{22} + 1/6*k{24} + 3/16*k{25} + 1/3*k{26} + 1/36*k{27} + (-5/4)*k{34} + 6*k{35}'''))
    substitute(ex, Ex(r'''e{123} -> (-1099/288)*k{4} + 3/2*k{5} + (-29/192)*k{6} + 4715/2304*k{7} + 8/9*k{8} + (-89/48)*k{9} + 3/2*k{10} + 3/8*k{11} + 29/32*k{12} + 7/72*k{13} + 1/8*k{14} + 3/4*k{15} + 37/16*k{16} + (-5/4)*k{22} + 1/36*k{27} + 1/2*k{32} + (-9/2)*k{34} + 1*k{36}'''))
    substitute(ex, Ex(r'''e{124} -> (-5/4)*k{4} + 1/4*k{5} + 1/32*k{6} + 97/128*k{7} + 3/8*k{8} + (-1/4)*k{9} + 3/4*k{10} + (-5/8)*k{11} + 1/16*k{12} + 1/32*k{14} + (-1/4)*k{22} + (-3)*k{23} + (-1/2)*k{24} + (-1)*k{26} + (-1/2)*k{28} + (-6)*k{35}'''))
    substitute(ex, Ex(r'''e{125} -> 1309/288*k{4} + (-3)*k{5} + (-157/192)*k{6} + (-6701/2304)*k{7} + (-215/144)*k{8} + 83/48*k{9} + (-3)*k{10} + 33/8*k{11} + 1/32*k{12} + 115/144*k{13} + 5/8*k{14} + 35/4*k{15} + 5/16*k{16} + 11/4*k{22} + 55/72*k{27} + 1/4*k{32} + 11/2*k{34}'''))
    substitute(ex, Ex(r'''e{126} -> 2327/1728*k{4} + (-1/2)*k{5} + (-863/1152)*k{6} + (-16519/13824)*k{7} + (-343/864)*k{8} + (-47/288)*k{9} + (-1/2)*k{10} + 13/16*k{11} + 107/192*k{12} + 191/864*k{13} + 15/32*k{14} + 41/24*k{15} + 127/96*k{16} + 25/24*k{22} + 179/432*k{27} + (-1/12)*k{29} + 1/16*k{31} + 5/24*k{32} + 17/12*k{34} + 1/3*k{36}'''))
    substitute(ex, Ex(r'''e{127} -> 83/72*k{4} + 3*k{5} + (-47/48)*k{6} + (-763/576)*k{7} + 19/72*k{8} + (-17/12)*k{9} + 3*k{10} + (-3)*k{11} + 5/8*k{12} + (-29/72)*k{13} + 1/2*k{14} + (-7)*k{15} + 7/4*k{16} + 1*k{22} + 19/36*k{27} + 1/2*k{32} + (-2)*k{34} + 2*k{36}'''))
    substitute(ex, Ex(r'''e{128} -> 667/216*k{4} + (-17/3)*k{5} + (-2)*k{6} + (-2269/864)*k{7} + (-20/27)*k{8} + (-61/36)*k{9} + 1*k{10} + 95/12*k{11} + 13/12*k{12} + 79/108*k{13} + 83/72*k{14} + 35/3*k{15} + 11/4*k{16} + 19/6*k{22} + 7/3*k{24} + (-1/2)*k{25} + 10/3*k{26} + 32/27*k{27} + (-4/3)*k{28} + 1/3*k{29} + (-1)*k{30} + 4/3*k{32} + (-2)*k{33} + 14/3*k{34} + (-16)*k{35} + 4/3*k{36}'''))
    substitute(ex, Ex(r'''e{129} -> (-1003/216)*k{4} + (-1/3)*k{5} + 23/6*k{6} + 4153/864*k{7} + 23/108*k{8} + 217/36*k{9} + (-7)*k{10} + (-23/12)*k{11} + (-5/6)*k{12} + 2/27*k{13} + (-119/72)*k{14} + 13/3*k{15} + (-13/4)*k{16} + (-31/6)*k{22} + (-7/3)*k{24} + 1/2*k{25} + (-10/3)*k{26} + (-121/54)*k{27} + 4/3*k{28} + (-1/3)*k{29} + 1*k{30} + (-7/3)*k{32} + 2*k{33} + 10/3*k{34} + 16*k{35} + (-22/3)*k{36}'''))
    substitute(ex, Ex(r'''e{130} -> 1165/864*k{4} + (-8/3)*k{5} + (-169/64)*k{6} + (-13769/6912)*k{7} + 121/432*k{8} + (-757/144)*k{9} + 4*k{10} + 19/24*k{11} + 149/96*k{12} + (-161/432)*k{13} + 23/18*k{14} + (-61/12)*k{15} + 71/16*k{16} + 29/12*k{22} + 7/3*k{24} + (-1/2)*k{25} + 10/3*k{26} + 319/216*k{27} + (-4/3)*k{28} + 1/3*k{29} + (-1)*k{30} + 25/12*k{32} + (-2)*k{33} + (-29/6)*k{34} + (-16)*k{35} + 16/3*k{36}'''))
    substitute(ex, Ex(r'''e{131} -> (-15/16)*k{4} + 9*k{5} + (-23/16)*k{6} + (-93/64)*k{7} + (-1/16)*k{8} + (-33/8)*k{9} + 6*k{10} + 15/4*k{11} + (-3/2)*k{12} + 9/16*k{13} + 1/4*k{14} + 5/2*k{15} + 9/8*k{16} + 3*k{22} + 3/2*k{24} + 9/8*k{25} + 6*k{26} + 9/8*k{27} + 3/4*k{32} + (-7)*k{34} + 36*k{35} + 2*k{36}'''))
    substitute(ex, Ex(r'''e{132} -> (-143/288)*k{4} + 47/192*k{6} + 1279/2304*k{7} + 25/144*k{8} + (-1/48)*k{9} + (-3/8)*k{11} + (-11/32)*k{12} + (-5/144)*k{13} + (-1/8)*k{14} + (-9/4)*k{15} + (-7/16)*k{16} + (-1/4)*k{22} + 7/72*k{27} + 1/4*k{32} + (-9/2)*k{34} + 2*k{36}'''))
    substitute(ex, Ex(r'''e{133} -> (-223/864)*k{4} + 1/2*k{5} + (-149/576)*k{6} + (-385/6912)*k{7} + 2/27*k{8} + (-125/144)*k{9} + 1/2*k{10} + (-5/8)*k{11} + 23/96*k{12} + (-23/216)*k{13} + 3/32*k{14} + (-19/12)*k{15} + 31/48*k{16} + 1/12*k{22} + 7/108*k{27} + 1/12*k{29} + (-1/16)*k{31} + 1/6*k{32} + (-7/6)*k{34} + 2/3*k{36}'''))
    substitute(ex, Ex(r'''e{134} -> (-65/72)*k{4} + 29/48*k{6} + 457/576*k{7} + 17/72*k{8} + 11/12*k{9} + 1/8*k{12} + (-7/72)*k{13} + (-1/4)*k{14} + 1*k{15} + (-1/4)*k{16} + (-1)*k{22} + (-19/36)*k{27} + (-1/2)*k{32} + 2*k{34} + (-2)*k{36}'''))
    substitute(ex, Ex(r'''e{135} -> 739/288*k{4} + (-14/3)*k{5} + (-1841/576)*k{6} + (-427/256)*k{7} + 233/144*k{8} + (-163/48)*k{9} + 4*k{10} + (-89/24)*k{11} + 421/96*k{12} + (-61/144)*k{13} + 131/72*k{14} + (-41/12)*k{15} + 169/48*k{16} + 7/4*k{22} + (-2/3)*k{24} + (-11/4)*k{25} + (-26/3)*k{26} + 107/72*k{27} + (-4/3)*k{28} + 9/4*k{32} + (-2)*k{33} + 29/2*k{34} + (-88)*k{35} + 4*k{36}'''))
    substitute(ex, Ex(r'''e{136} -> (-365/576)*k{4} + (-7/3)*k{5} + (-1121/1152)*k{6} + 655/1536*k{7} + 335/288*k{8} + (-139/96)*k{9} + 2*k{10} + (-89/48)*k{11} + 457/192*k{12} + (-103/288)*k{13} + 77/144*k{14} + (-53/24)*k{15} + 133/96*k{16} + (-5/8)*k{22} + (-1/3)*k{24} + (-11/8)*k{25} + (-13/3)*k{26} + (-7/144)*k{27} + (-2/3)*k{28} + 3/8*k{32} + (-1)*k{33} + 25/4*k{34} + (-44)*k{35} + 1*k{36}'''))
    substitute(ex, Ex(r'''e{137} -> 139/72*k{4} + (-67/48)*k{6} + (-1031/576)*k{7} + (-17/36)*k{8} + (-19/12)*k{9} + 1/2*k{12} + 7/36*k{13} + 3/4*k{14} + 2*k{16} + 2*k{22} + 19/18*k{27} + 1*k{32} + 2*k{36}'''))
    substitute(ex, Ex(r'''e{138} -> 491/288*k{4} + (-9/2)*k{5} + 55/192*k{6} + (-553/2304)*k{7} + 1/18*k{8} + 121/48*k{9} + (-7/2)*k{10} + (-21/8)*k{11} + 17/32*k{12} + (-13/36)*k{13} + (-1/4)*k{14} + (-7/4)*k{15} + (-53/16)*k{16} + (-5/4)*k{22} + (-3/2)*k{24} + (-9/8)*k{25} + (-6)*k{26} + (-8/9)*k{27} + (-1)*k{32} + 17/2*k{34} + (-36)*k{35} + (-1)*k{36}'''))
    substitute(ex, Ex(r'''e{139} -> 1/9*k{4} + (-21/4)*k{5} + (-1/48)*k{6} + 847/1152*k{7} + 65/144*k{8} + 11/24*k{9} + (-3/4)*k{10} + 7/16*k{11} + 15/16*k{12} + (-1/36)*k{13} + 17/96*k{14} + 1/2*k{15} + 1/8*k{16} + 3/8*k{22} + (-3)*k{23} + (-15/16)*k{25} + (-1/2)*k{26} + 11/72*k{27} + (-1)*k{28} + 1/2*k{32} + (-3/2)*k{33} + 5*k{34} + (-24)*k{35}'''))
    substitute(ex, Ex(r'''e{140} -> (-87/16)*k{4} + 9*k{5} + (-9/32)*k{6} + 205/128*k{7} + 1/8*k{8} + (-51/8)*k{9} + 7*k{10} + 21/4*k{11} + (-27/16)*k{12} + 5/8*k{13} + 5/2*k{15} + 39/8*k{16} + 3/2*k{22} + 3*k{24} + 9/4*k{25} + 12*k{26} + 5/4*k{27} + 3/2*k{32} + (-19)*k{34} + 72*k{35} + 2*k{36}'''))
    substitute(ex, Ex(r'''e{141} -> (-725/144)*k{4} + 64/3*k{5} + 179/288*k{6} + 2489/1152*k{7} + 23/8*k{8} + (-67/24)*k{9} + 8*k{10} + (-181/12)*k{11} + 17/48*k{12} + (-11/8)*k{13} + (-5/36)*k{14} + (-97/6)*k{15} + 41/24*k{16} + (-9/2)*k{22} + (-14/3)*k{24} + 1*k{25} + (-20/3)*k{26} + (-3/4)*k{27} + 8/3*k{28} + (-1/2)*k{32} + 4*k{33} + (-3)*k{34} + 32*k{35} + (-4)*k{36}'''))
    substitute(ex, Ex(r'''e{142} -> (-2999/864)*k{4} + 26/3*k{5} + 979/576*k{6} + 15715/6912*k{7} + 523/432*k{8} + 215/144*k{9} + (-121/24)*k{11} + (-21/32)*k{12} + (-227/432)*k{13} + (-127/144)*k{14} + (-11/4)*k{15} + (-95/48)*k{16} + (-43/12)*k{22} + (-7/3)*k{24} + 1/2*k{25} + (-10/3)*k{26} + (-323/216)*k{27} + 4/3*k{28} + 1/6*k{29} + (-1/8)*k{31} + (-17/12)*k{32} + 2*k{33} + 7/6*k{34} + 16*k{35} + (-14/3)*k{36}'''))
    substitute(ex, Ex(r'''e{143} -> 737/72*k{4} + (-20)*k{5} + (-7/6)*k{6} + (-781/144)*k{7} + (-305/72)*k{8} + 53/12*k{9} + (-10)*k{10} + 23/3*k{11} + 7/12*k{12} + 61/72*k{13} + 1*k{14} + 9*k{15} + (-3/4)*k{16} + 11/3*k{22} + 7/3*k{24} + (-3/4)*k{25} + 8/3*k{26} + 25/36*k{27} + (-2)*k{28} + (-1/2)*k{32} + 10*k{34} + (-24)*k{35}'''))
    substitute(ex, Ex(r'''e{144} -> 577/288*k{4} + (-7)*k{5} + (-127/192)*k{6} + (-2231/2304)*k{7} + (-79/72)*k{8} + (-5/48)*k{9} + (-2)*k{10} + 65/24*k{11} + 1/96*k{12} + 23/72*k{13} + 3/8*k{14} + 15/4*k{15} + (-3/16)*k{16} + 13/12*k{22} + 7/6*k{24} + (-3/8)*k{25} + 4/3*k{26} + 23/36*k{27} + (-1)*k{28} + 1/2*k{32} + 7/2*k{34} + (-12)*k{35}'''))
    substitute(ex, Ex(r'''e{145} -> 727/144*k{4} + (-6)*k{5} + (-103/96)*k{6} + (-3575/1152)*k{7} + (-131/72)*k{8} + 17/24*k{9} + (-6)*k{10} + 3/4*k{11} + 7/16*k{12} + 19/72*k{13} + 3/4*k{14} + (-3/2)*k{15} + 11/8*k{16} + 5/2*k{22} + 31/36*k{27} + 1/2*k{32} + (-3)*k{34} + 4*k{36}'''))
    substitute(ex, Ex(r'''e{146} -> (-31/72)*k{4} + 14/3*k{5} + 85/72*k{6} + 11/24*k{7} + 11/72*k{8} + 31/12*k{9} + (-2)*k{10} + (-41/12)*k{11} + 7/12*k{12} + (-13/72)*k{13} + (-7/36)*k{14} + (-1/3)*k{15} + 5/12*k{16} + (-5/2)*k{22} + (-7/3)*k{24} + 1/2*k{25} + (-10/3)*k{26} + (-43/36)*k{27} + 4/3*k{28} + (-3/2)*k{32} + 2*k{33} + 2*k{34} + 16*k{35} + (-4)*k{36}'''))
    substitute(ex, Ex(r'''e{147} -> (-49/144)*k{4} + 7/3*k{5} + 47/72*k{6} + 65/192*k{7} + 11/144*k{8} + 37/24*k{9} + (-2)*k{10} + (-41/24)*k{11} + (-1/12)*k{12} + (-13/144)*k{13} + (-2/9)*k{14} + (-1/6)*k{15} + (-13/24)*k{16} + (-5/4)*k{22} + (-7/6)*k{24} + 1/4*k{25} + (-5/3)*k{26} + (-43/72)*k{27} + 2/3*k{28} + (-3/4)*k{32} + 1*k{33} + 1*k{34} + 8*k{35} + (-2)*k{36}'''))
    substitute(ex, Ex(r'''e{148} -> (-1/2)*k{4} + (-3/4)*k{6} + (-5/16)*k{7} + (-1)*k{9} + 3/2*k{12} + 1/2*k{14} + (-4)*k{15} + 3*k{16} + (-8)*k{34} + 4*k{36}'''))
    substitute(ex, Ex(r'''e{149} -> (-65/36)*k{4} + 29/24*k{6} + 457/288*k{7} + 17/36*k{8} + 11/6*k{9} + 1/4*k{12} + (-7/36)*k{13} + (-1/2)*k{14} + 2*k{15} + (-1/2)*k{16} + (-2)*k{22} + (-19/18)*k{27} + (-1)*k{32} + 4*k{34} + (-4)*k{36}'''))
    substitute(ex, Ex(r'''e{150} -> (-83/36)*k{4} + (-6)*k{5} + 35/24*k{6} + 655/288*k{7} + (-19/36)*k{8} + 17/6*k{9} + (-6)*k{10} + 6*k{11} + 1/4*k{12} + 29/36*k{13} + (-1/2)*k{14} + 10*k{15} + (-1/2)*k{16} + (-2)*k{22} + (-19/18)*k{27} + (-1)*k{32} + (-4)*k{34}'''))
    substitute(ex, Ex(r'''e{151} -> (-359/54)*k{4} + 32/3*k{5} + (-319/72)*k{6} + 1043/864*k{7} + 367/108*k{8} + (-133/9)*k{9} + 24*k{10} + (-13/6)*k{11} + 5/4*k{12} + (-59/108)*k{13} + 35/36*k{14} + (-16)*k{15} + 16/3*k{16} + 17/3*k{22} + 14/3*k{24} + (-1)*k{25} + 20/3*k{26} + 187/54*k{27} + (-8/3)*k{28} + (-2/3)*k{29} + 2*k{30} + 13/3*k{32} + (-4)*k{33} + (-16/3)*k{34} + (-32)*k{35} + 28/3*k{36}'''))
    substitute(ex, Ex(r'''e{152} -> 913/108*k{4} + 4/3*k{5} + 49/18*k{6} + (-1585/432)*k{7} + (-101/54)*k{8} + 161/18*k{9} + (-12)*k{10} + (-59/6)*k{11} + (-3)*k{12} + (-34/27)*k{13} + (-35/36)*k{14} + (-10)*k{15} + (-47/6)*k{16} + (-11/3)*k{22} + (-14/3)*k{24} + 1*k{25} + (-20/3)*k{26} + (-65/27)*k{27} + 8/3*k{28} + 2/3*k{29} + (-2)*k{30} + (-10/3)*k{32} + 4*k{33} + 4/3*k{34} + 32*k{35} + (-16/3)*k{36}'''))
    substitute(ex, Ex(r'''e{153} -> (-769/432)*k{4} + (-40/3)*k{5} + 77/288*k{6} + 7301/3456*k{7} + (-151/216)*k{8} + 1/72*k{9} + 145/12*k{11} + 13/16*k{12} + 275/216*k{13} + (-5/18)*k{14} + 27/2*k{15} + 23/24*k{16} + 19/6*k{22} + 14/3*k{24} + (-1)*k{25} + 20/3*k{26} + 83/108*k{27} + (-8/3)*k{28} + (-2/3)*k{29} + 2*k{30} + 5/6*k{32} + (-4)*k{33} + 17/3*k{34} + (-32)*k{35} + 4/3*k{36}'''))
    substitute(ex, Ex(r'''e{154} -> 19/24*k{4} + (-3)*k{6} + (-25/24)*k{7} + 41/24*k{8} + (-17/4)*k{9} + 6*k{10} + (-15/2)*k{11} + 15/4*k{12} + (-13/24)*k{13} + 3/2*k{14} + (-7)*k{15} + 9/4*k{16} + (-3)*k{24} + (-9/4)*k{25} + (-12)*k{26} + 11/12*k{27} + 3/2*k{32} + 10*k{34} + (-72)*k{35} + 4*k{36}'''))
    substitute(ex, Ex(r'''e{155} -> 27/16*k{4} + (-6)*k{5} + 63/32*k{6} + 53/128*k{7} + (-7/8)*k{8} + 39/8*k{9} + (-6)*k{10} + 3/4*k{11} + (-9/16)*k{12} + (-1/8)*k{13} + (-3/4)*k{14} + 5/2*k{15} + (-21/8)*k{16} + (-3/2)*k{22} + (-5/4)*k{27} + (-3/2)*k{32} + 5*k{34} + (-4)*k{36}'''))
    substitute(ex, Ex(r'''e{156} -> (-991/144)*k{4} + 32/3*k{5} + (-413/288)*k{6} + 3265/1152*k{7} + 43/12*k{8} + (-205/24)*k{9} + 14*k{10} + (-1/12)*k{11} + 7/16*k{12} + (-5/12)*k{13} + 5/36*k{14} + (-23/6)*k{15} + 91/24*k{16} + 11/6*k{22} + 7/3*k{24} + (-1/4)*k{25} + 4*k{26} + 3/2*k{27} + (-2/3)*k{28} + 3*k{32} + (-4)*k{33} + (-5)*k{34} + (-8)*k{35} + 4*k{36}'''))
    substitute(ex, Ex(r'''e{157} -> (-245/144)*k{4} + 16/3*k{5} + (-155/144)*k{6} + (-53/576)*k{7} + 61/48*k{8} + (-89/24)*k{9} + 7*k{10} + 13/12*k{11} + 1/2*k{12} + (-5/48)*k{13} + 7/36*k{14} + (-7/6)*k{15} + 41/24*k{16} + 5/3*k{22} + 7/6*k{24} + (-1/8)*k{25} + 2*k{26} + 11/24*k{27} + (-1/3)*k{28} + 3/4*k{32} + (-2)*k{33} + (-1)*k{34} + (-4)*k{35} + 2*k{36}'''))
    substitute(ex, Ex(r'''e{158} -> (-143/144)*k{4} + 47/96*k{6} + 1279/1152*k{7} + 25/72*k{8} + (-1/24)*k{9} + (-3/4)*k{11} + (-11/16)*k{12} + (-5/72)*k{13} + (-1/4)*k{14} + (-1/2)*k{15} + (-7/8)*k{16} + (-1/2)*k{22} + 7/36*k{27} + 1/2*k{32} + (-1)*k{34}'''))
    substitute(ex, Ex(r'''e{159} -> 235/72*k{4} + (-8)*k{5} + (-29/24)*k{6} + (-427/288)*k{7} + (-61/72)*k{8} + (-7/4)*k{9} + 2*k{10} + 14/3*k{11} + 7/3*k{12} + 41/72*k{13} + 3/2*k{14} + 7*k{15} + 19/4*k{16} + 5/3*k{22} + 7/3*k{24} + (-3/4)*k{25} + 8/3*k{26} + 53/36*k{27} + (-2)*k{28} + 3/2*k{32} + 6*k{34} + (-24)*k{35}'''))
    substitute(ex, Ex(r'''e{160} -> 397/144*k{4} + (-71/96)*k{6} + (-2273/1152)*k{7} + (-59/72)*k{8} + 29/24*k{9} + (-3)*k{10} + (-37/8)*k{11} + 27/16*k{12} + (-1/9)*k{13} + 25/48*k{14} + 1/2*k{15} + 1/8*k{16} + (-9/4)*k{22} + 6*k{23} + (-3)*k{24} + (-3/8)*k{25} + (-11)*k{26} + (-23/36)*k{27} + 2*k{28} + (-1)*k{32} + 3*k{33} + 5*k{34} + (-24)*k{35}'''))
    substitute(ex, Ex(r'''e{161} -> (-721/144)*k{4} + 8*k{5} + 127/96*k{6} + 3095/1152*k{7} + 43/36*k{8} + 5/24*k{9} + (-2)*k{10} + (-65/12)*k{11} + (-145/48)*k{12} + (-23/36)*k{13} + (-7/4)*k{14} + (-15/2)*k{15} + (-45/8)*k{16} + (-13/6)*k{22} + (-7/3)*k{24} + 3/4*k{25} + (-8/3)*k{26} + (-23/18)*k{27} + 2*k{28} + (-1)*k{32} + (-7)*k{34} + 24*k{35}'''))
    substitute(ex, Ex(r'''e{162} -> 685/144*k{4} + (-8)*k{5} + (-139/96)*k{6} + (-3059/1152)*k{7} + (-43/36)*k{8} + (-17/24)*k{9} + 2*k{10} + 65/12*k{11} + 145/48*k{12} + 23/36*k{13} + 7/4*k{14} + 15/2*k{15} + 45/8*k{16} + 13/6*k{22} + 7/3*k{24} + (-3/4)*k{25} + 8/3*k{26} + 23/18*k{27} + (-2)*k{28} + 1*k{32} + 7*k{34} + (-24)*k{35}'''))
    substitute(ex, Ex(r'''e{163} -> 2*k{4} + (-6)*k{5} + 1/2*k{6} + (-3/8)*k{7} + (-1)*k{8} + 2*k{9} + (-6)*k{10}'''))
    substitute(ex, Ex(r'''e{164} -> 115/432*k{4} + (-1)*k{5} + 41/288*k{6} + (-155/3456)*k{7} + (-4/27)*k{8} + 89/72*k{9} + (-1)*k{10} + 5/4*k{11} + 13/48*k{12} + 23/108*k{13} + 1/16*k{14} + 7/6*k{15} + 5/24*k{16} + (-1/6)*k{22} + (-7/54)*k{27} + (-1/6)*k{29} + 1/8*k{31} + (-1/3)*k{32} + (-5/3)*k{34} + 2/3*k{36}'''))
    substitute(ex, Ex(r'''e{165} -> 49/144*k{4} + (-7/6)*k{5} + 1/576*k{6} + (-83/2304)*k{7} + 1/48*k{8} + (-1/6)*k{9} + 1/2*k{10} + 41/48*k{11} + 13/96*k{12} + 1/48*k{13} + 5/72*k{14} + 1/3*k{15} + 1/12*k{16} + 3/8*k{22} + 7/12*k{24} + (-1/8)*k{25} + 5/6*k{26} + 1/6*k{27} + (-1/3)*k{28} + 1/4*k{32} + (-1/2)*k{33} + 1*k{34} + (-4)*k{35}'''))
    substitute(ex, Ex(r'''e{166} -> 1*k{37}'''))
    substitute(ex, Ex(r'''e{167} -> 1*k{38}'''))
    substitute(ex, Ex(r'''e{168} -> 1*k{39}'''))
    substitute(ex, Ex(r'''e{169} -> 1*k{40}'''))
    substitute(ex, Ex(r'''e{170} -> (-1)*k{4} + 1/2*k{6} + 7/8*k{7} + (-1/2)*k{12} + 1/2*k{13} + (-1/4)*k{14} + (-1)*k{40}'''))
    substitute(ex, Ex(r'''e{171} -> (-3/4)*k{4} + 3/8*k{7} + 1/2*k{11} + 1/4*k{13}'''))
    substitute(ex, Ex(r'''e{172} -> 1*k{41}'''))
    substitute(ex, Ex(r'''e{173} -> 1*k{42}'''))
    substitute(ex, Ex(r'''e{174} -> 1*k{43}'''))
    substitute(ex, Ex(r'''e{175} -> 1*k{44}'''))
    substitute(ex, Ex(r'''e{176} -> 1*k{45}'''))
    substitute(ex, Ex(r'''e{177} -> (-1)*k{4} + (-1/8)*k{6} + 13/32*k{7} + (-1)*k{11} + 1/4*k{13} + 1/8*k{14} + (-1)*k{39} + (-2)*k{41} + (-1)*k{43}'''))
    substitute(ex, Ex(r'''e{178} -> 1*k{4} + 1/4*k{6} + (-5/16)*k{7} + (-1/2)*k{12} + (-1/2)*k{13} + (-1/2)*k{14} + (-1)*k{40} + (-1)*k{42}'''))
    substitute(ex, Ex(r'''e{179} -> (-3)*k{4} + (-5/4)*k{6} + 9/16*k{7} + 1/2*k{12} + 3/2*k{13} + 1*k{14} + 1*k{40} + 1*k{42}'''))
    substitute(ex, Ex(r'''e{180} -> (-1/2)*k{4} + 1/4*k{7} + 1/2*k{13}'''))
    substitute(ex, Ex(r'''e{181} -> 1*k{4} + 1/4*k{6} + (-5/16)*k{7} + 1*k{11} + (-1/4)*k{13} + (-1/4)*k{14} + 1*k{39} + 2*k{41} + 1*k{43}'''))
    substitute(ex, Ex(r'''e{182} -> (-1)*k{4} + (-1/4)*k{6} + 5/16*k{7} + 1/2*k{12} + 1/2*k{13} + 3/4*k{14} + 1*k{40} + 1*k{42}'''))
    substitute(ex, Ex(r'''e{183} -> 1*k{4} + 1*k{6} + 1/4*k{7} + (-1/2)*k{12} + (-1/2)*k{13} + (-3/4)*k{14} + (-1)*k{40} + (-1)*k{42}'''))
    substitute(ex, Ex(r'''e{184} -> (-1)*k{4} + 1/8*k{6} + 19/32*k{7} + (-1)*k{11} + 1/4*k{13} + (-1/8)*k{14} + (-1)*k{39} + (-2)*k{41} + (-1)*k{43}'''))
    substitute(ex, Ex(r'''e{185} -> 1*k{46}'''))
    substitute(ex, Ex(r'''e{186} -> (-1)*k{4} + (-1/4)*k{6} + 5/16*k{7} + (-1/2)*k{12} + 1/2*k{13} + 1/2*k{14} + (-1)*k{40} + (-1)*k{42} + (-1)*k{46}'''))
    substitute(ex, Ex(r'''e{187} -> (-17/3)*k{4} + (-29/12)*k{6} + 49/48*k{7} + 8*k{11} + 9/2*k{12} + 13/6*k{13} + 3/2*k{14} + 1*k{40} + 1*k{42}'''))
    substitute(ex, Ex(r'''e{188} -> 1*k{4} + 1/4*k{6} + (-5/16)*k{7} + 1/2*k{12} + (-1/2)*k{13} + (-1/2)*k{14} + 1*k{40} + 1*k{42} + 1*k{46}'''))
    substitute(ex, Ex(r'''e{189} -> (-10/3)*k{4} + (-4/3)*k{6} + 2/3*k{7} + 4*k{11} + 2*k{12} + 4/3*k{13} + 1*k{14}'''))
    substitute(ex, Ex(r'''e{190} -> 4*k{4} + (-2)*k{7} + (-2)*k{13}'''))
    substitute(ex, Ex(r'''e{191} -> (-1/4)*k{4} + 1/8*k{6} + 7/32*k{7} + (-1/8)*k{14}'''))
    substitute(ex, Ex(r'''e{192} -> 3*k{4} + 3/4*k{6} + (-15/16)*k{7} + (-1/2)*k{12} + (-3/2)*k{13} + (-1/2)*k{14} + (-1)*k{40} + (-1)*k{42}'''))
    substitute(ex, Ex(r'''e{193} -> 1/4*k{6} + 3/16*k{7} + 1/2*k{13} + (-1/4)*k{14}'''))
    substitute(ex, Ex(r'''e{194} -> 2*k{4} + (-1)*k{7} + (-1)*k{13}'''))
    substitute(ex, Ex(r'''e{195} -> 1*k{47}'''))
    substitute(ex, Ex(r'''e{196} -> (-1/2)*k{4} + 7/36*k{6} + 19/48*k{7} + (-2/3)*k{11} + (-13/18)*k{12} + 11/36*k{13} + (-5/72)*k{14} + (-2)*k{38} + (-5/18)*k{40} + 7/18*k{42} + (-2/3)*k{45} + 1/12*k{46}'''))
    substitute(ex, Ex(r'''e{197} -> 47/12*k{4} + 91/96*k{6} + (-479/384)*k{7} + (-15/4)*k{11} + (-7/4)*k{12} + (-27/16)*k{13} + (-47/96)*k{14} + (-18)*k{37} + (-6)*k{38} + (-3/2)*k{39} + (-2)*k{40} + 2*k{41} + (-1/4)*k{42} + 5/2*k{43} + (-4)*k{44} + (-1)*k{45} + (-1/8)*k{46} + (-3)*k{47}'''))
    substitute(ex, Ex(r'''e{198} -> (-13/3)*k{4} + (-11/6)*k{6} + 19/24*k{7} + 4*k{11} + 5/2*k{12} + 11/6*k{13} + 5/4*k{14} + 1*k{40} + 1*k{42} + (-1/2)*k{46}'''))
    substitute(ex, Ex(r'''e{199} -> (-1/6)*k{4} + (-59/48)*k{6} + (-161/192)*k{7} + 23/6*k{11} + 7/2*k{12} + (-11/24)*k{13} + 5/16*k{14} + 12*k{37} + 12*k{38} + 7/3*k{39} + 4*k{40} + 8/3*k{41} + 1/2*k{42} + (-5/3)*k{43} + 2*k{45} + 1/4*k{46} + (-6)*k{47}'''))
    substitute(ex, Ex(r'''e{200} -> 3/8*k{4} + 1/8*k{6} + (-3/32)*k{7} + (-1/4)*k{13} + (-1/8)*k{14} + 1/2*k{39} + 1*k{41} + 1/2*k{43} + (-1)*k{44} + (-2)*k{47}'''))
    substitute(ex, Ex(r'''e{201} -> (-8/9)*k{6} + (-2/3)*k{7} + 4/3*k{11} + 13/9*k{12} + (-1/9)*k{13} + 37/72*k{14} + 4*k{38} + 14/9*k{40} + 2/9*k{42} + 1/3*k{45} + (-1/6)*k{46}'''))
    substitute(ex, Ex(r'''e{202} -> (-23/3)*k{4} + (-2/3)*k{6} + 10/3*k{7} + 14/3*k{11} + 23/6*k{13} + 2/3*k{14} + 24*k{37} + 5/3*k{39} + (-14/3)*k{41} + (-7/3)*k{43} + 8*k{44} + 12*k{47}'''))
    substitute(ex, Ex(r'''e{203} -> 20/3*k{4} + 8/3*k{6} + (-4/3)*k{7} + (-8)*k{11} + (-4)*k{12} + (-8/3)*k{13} + (-2)*k{14} + 1*k{46}'''))
    substitute(ex, Ex(r'''e{204} -> (-1/2)*k{6} + (-3/8)*k{7} + 1/2*k{14}'''))
    substitute(ex, Ex(r'''e{205} -> 1*k{48}'''))
    substitute(ex, Ex(r'''e{206} -> 1*k{49}'''))
    substitute(ex, Ex(r'''e{207} -> 1*k{50}'''))
    substitute(ex, Ex(r'''e{208} -> 7/48*k{6} + 7/64*k{7} + (-4/3)*k{11} + (-7/24)*k{12} + (-3/16)*k{14} + (-4)*k{15} + (-7/4)*k{16} + (-1/3)*k{39} + 1/6*k{40} + (-2/3)*k{41} + (-1/12)*k{42} + (-11/6)*k{43} + 1/4*k{46} + (-12)*k{48} + (-6)*k{49} + (-1)*k{50}'''))
    substitute(ex, Ex(r'''e{209} -> (-7/48)*k{6} + (-7/64)*k{7} + 4/3*k{11} + 7/24*k{12} + 3/16*k{14} + 4*k{15} + 5/4*k{16} + 1/3*k{39} + (-1/6)*k{40} + 2/3*k{41} + 1/12*k{42} + 11/6*k{43} + (-1/4)*k{46} + 12*k{48} + 6*k{49} + 1*k{50}'''))
    substitute(ex, Ex(r'''e{210} -> 1/2*k{15}'''))
    substitute(ex, Ex(r'''e{211} -> (-11/96)*k{4} + (-11/192)*k{6} + 11/768*k{7} + 1/6*k{11} + 11/96*k{12} + 5/144*k{13} + 1/72*k{14} + (-2/3)*k{15} + (-5/48)*k{16} + 1*k{37} + 1/2*k{38} + 1/6*k{39} + 5/24*k{40} + 1/48*k{42} + (-1/8)*k{43} + 1/12*k{44} + 1/24*k{45} + 1/48*k{46} + (-1)*k{48} + (-1/2)*k{49} + (-5/12)*k{50}'''))
    substitute(ex, Ex(r'''e{212} -> (-7/48)*k{6} + (-7/64)*k{7} + 4/3*k{11} + 7/24*k{12} + 3/16*k{14} + 4*k{15} + 5/4*k{16} + 1/3*k{39} + (-1/6)*k{40} + 2/3*k{41} + 1/12*k{42} + 11/6*k{43} + (-1/4)*k{46} + 12*k{48} + 6*k{49} + 1*k{50}'''))
    substitute(ex, Ex(r'''e{213} -> 11/48*k{4} + 11/96*k{6} + (-11/384)*k{7} + (-1/3)*k{11} + (-11/48)*k{12} + (-5/72)*k{13} + (-1/36)*k{14} + 1/3*k{15} + 5/24*k{16} + (-2)*k{37} + (-1)*k{38} + (-1/3)*k{39} + (-5/12)*k{40} + (-1/24)*k{42} + 1/4*k{43} + (-1/6)*k{44} + (-1/12)*k{45} + (-1/24)*k{46} + 2*k{48} + 1*k{49} + (-1/6)*k{50}'''))
    substitute(ex, Ex(r'''e{214} -> 73/96*k{4} + (-19/768)*k{6} + (-1225/3072)*k{7} + (-115/96)*k{11} + (-125/384)*k{13} + 19/768*k{14} + (-9/4)*k{15} + (-3/2)*k{37} + (-31/96)*k{39} + (-25/48)*k{41} + (-25/96)*k{43} + 3/4*k{47} + (-3)*k{48} + (-1/8)*k{50}'''))
    substitute(ex, Ex(r'''e{215} -> (-65/48)*k{4} + 5/12*k{6} + 95/96*k{7} + 7/12*k{11} + (-53/48)*k{12} + 23/32*k{13} + (-41/192)*k{14} + 5/2*k{15} + (-11/16)*k{16} + (-3)*k{38} + 1/12*k{39} + (-43/48)*k{40} + 1/6*k{41} + (-5/24)*k{42} + 11/24*k{43} + (-1/2)*k{45} + 3*k{48} + (-3/2)*k{49} + 1/4*k{50}'''))
    substitute(ex, Ex(r'''e{216} -> (-15/8)*k{4} + 1/64*k{6} + 243/256*k{7} + 29/8*k{11} + 27/32*k{13} + (-1/64)*k{14} + 6*k{15} + (-1/8)*k{39} + 5/4*k{41} + 5/8*k{43} + (-3/2)*k{50}'''))
    substitute(ex, Ex(r'''e{217} -> 11/8*k{4} + (-3/8)*k{6} + (-31/32)*k{7} + 1/2*k{11} + 9/8*k{12} + (-11/16)*k{13} + 15/32*k{14} + 3*k{15} + 27/8*k{16} + 1/2*k{39} + (-3/8)*k{40} + 1*k{41} + 3/4*k{42} + 11/4*k{43} + (-3/8)*k{46} + 18*k{48} + 9*k{49} + 3/2*k{50}'''))
    substitute(ex, Ex(r'''e{218} -> (-11/8)*k{4} + 3/8*k{6} + 31/32*k{7} + (-1/2)*k{11} + (-9/8)*k{12} + 11/16*k{13} + (-15/32)*k{14} + (-3)*k{15} + (-27/8)*k{16} + (-1/2)*k{39} + 3/8*k{40} + (-1)*k{41} + (-3/4)*k{42} + (-11/4)*k{43} + 3/8*k{46} + (-18)*k{48} + (-9)*k{49} + (-3/2)*k{50}'''))
    substitute(ex, Ex(r'''e{219} -> 0'''))
    substitute(ex, Ex(r'''e{220} -> 1*k{4} + 13/128*k{6} + (-217/512)*k{7} + (-11/48)*k{11} + (-1/32)*k{12} + (-91/192)*k{13} + (-35/384)*k{14} + 1*k{15} + 1/16*k{16} + (-3)*k{37} + (-5/48)*k{39} + 13/24*k{41} + 13/48*k{43} + (-1)*k{44} + (-3/2)*k{47} + 1/4*k{50}'''))
    substitute(ex, Ex(r'''e{221} -> (-31/24)*k{4} + (-11/24)*k{6} + 29/96*k{7} + 1/3*k{11} + 17/24*k{12} + 9/16*k{13} + 29/96*k{14} + (-2)*k{15} + (-1/8)*k{16} + (-1/6)*k{39} + 7/24*k{40} + (-1/3)*k{41} + (-1/12)*k{42} + (-11/12)*k{43} + (-6)*k{48} + (-3)*k{49} + (-1/2)*k{50}'''))
    substitute(ex, Ex(r'''e{222} -> (-1/24)*k{4} + (-1/24)*k{6} + (-1/96)*k{7} + 1/16*k{12} + 1/48*k{14} + (-1/2)*k{15} + (-1/8)*k{16}'''))
    substitute(ex, Ex(r'''e{223} -> (-37/24)*k{4} + 49/96*k{6} + 443/384*k{7} + (-15/4)*k{11} + (-23/12)*k{12} + 5/6*k{13} + (-11/24)*k{14} + (-8)*k{15} + (-19/8)*k{16} + 12*k{37} + (-1/4)*k{39} + (-17/24)*k{40} + (-11/2)*k{41} + (-13/12)*k{42} + (-7/2)*k{43} + 5*k{44} + 1/2*k{45} + 1/4*k{46} + 6*k{47} + (-6)*k{48} + (-3)*k{49} + 1/2*k{50}'''))
    substitute(ex, Ex(r'''e{224} -> (-5/6)*k{4} + (-1/3)*k{6} + 1/6*k{7} + 3*k{11} + 5/4*k{12} + 1/2*k{13} + 5/12*k{14} + 2*k{15} + 1/2*k{16}'''))
    substitute(ex, Ex(r'''e{225} -> (-1/4)*k{4} + (-83/48)*k{6} + (-75/64)*k{7} + 23/6*k{11} + 23/6*k{12} + 1/4*k{13} + 13/8*k{14} + 4*k{15} + 19/4*k{16} + 11/6*k{39} + 17/12*k{40} + 5/3*k{41} + 13/6*k{42} + 7/3*k{43} + (-2)*k{44} + (-1)*k{45} + (-1/2)*k{46} + 12*k{48} + 6*k{49} + 3*k{50}'''))
    substitute(ex, Ex(r'''e{226} -> 5/3*k{4} + 2*k{6} + 2/3*k{7} + (-23/3)*k{11} + (-59/12)*k{12} + (-3/4)*k{13} + (-47/24)*k{14} + (-10)*k{15} + (-7)*k{16} + (-2/3)*k{39} + 1/6*k{40} + (-4/3)*k{41} + (-4/3)*k{42} + (-11/3)*k{43} + 3/4*k{46} + (-24)*k{48} + (-12)*k{49} + (-2)*k{50}'''))
    substitute(ex, Ex(r'''e{227} -> (-2/3)*k{4} + (-7/4)*k{6} + (-47/48)*k{7} + 14/3*k{11} + 25/6*k{12} + 1/4*k{13} + 41/24*k{14} + 4*k{15} + 11/2*k{16} + 2/3*k{39} + (-1/6)*k{40} + 4/3*k{41} + 4/3*k{42} + 11/3*k{43} + (-3/4)*k{46} + 24*k{48} + 12*k{49} + 2*k{50}'''))
    substitute(ex, Ex(r'''e{228} -> 2/3*k{4} + (-7/6)*k{6} + (-29/24)*k{7} + 5/3*k{11} + 35/12*k{12} + (-1/4)*k{13} + 31/24*k{14} + 2*k{15} + 5*k{16} + 2/3*k{39} + (-1/6)*k{40} + 4/3*k{41} + 4/3*k{42} + 11/3*k{43} + (-3/4)*k{46} + 24*k{48} + 12*k{49} + 2*k{50}'''))
    substitute(ex, Ex(r'''e{229} -> 1/4*k{4} + (-1/8)*k{6} + (-7/32)*k{7} + 3/4*k{12} + 1/4*k{14} + 3/2*k{16}'''))
    substitute(ex, Ex(r'''e{230} -> 0'''))
    substitute(ex, Ex(r'''e{231} -> 5/6*k{4} + 5/3*k{6} + 5/6*k{7} + (-14/3)*k{11} + (-11/3)*k{12} + (-1/4)*k{13} + (-37/24)*k{14} + (-8)*k{15} + (-13/2)*k{16} + (-2/3)*k{39} + 1/6*k{40} + (-4/3)*k{41} + (-4/3)*k{42} + (-11/3)*k{43} + 3/4*k{46} + (-24)*k{48} + (-12)*k{49} + (-2)*k{50}'''))
    substitute(ex, Ex(r'''e{232} -> 29/48*k{4} + 31/384*k{6} + (-371/1536)*k{7} + 43/48*k{11} + (-55/192)*k{13} + (-31/384)*k{14} + 3*k{15} + (-3)*k{37} + (-5/48)*k{39} + 13/24*k{41} + 13/48*k{43} + (-1)*k{44} + (-3/2)*k{47} + 1/4*k{50}'''))
    substitute(ex, Ex(r'''e{233} -> (-31/48)*k{4} + (-7/24)*k{6} + 5/48*k{7} + 1/6*k{11} + 13/24*k{12} + 9/32*k{13} + 41/192*k{14} + (-1)*k{15} + 5/16*k{16} + (-1/12)*k{39} + 7/48*k{40} + (-1/6)*k{41} + (-1/24)*k{42} + (-11/24)*k{43} + (-3)*k{48} + (-3/2)*k{49} + (-1/4)*k{50}'''))
    substitute(ex, Ex(r'''e{234} -> (-1)*k{4} + 1/2*k{7} + 3*k{11} + 1/2*k{13} + 6*k{15}'''))
    substitute(ex, Ex(r'''e{235} -> 7/12*k{4} + 5/24*k{6} + (-13/96)*k{7} + 1/4*k{12} + 1/12*k{14} + (-2)*k{15} + (-1/2)*k{16}'''))
    substitute(ex, Ex(r'''e{236} -> (-17/48)*k{4} + (-5/16)*k{6} + (-11/192)*k{7} + 1/6*k{11} + 25/24*k{12} + 9/32*k{13} + 73/192*k{14} + (-2)*k{15} + 13/16*k{16} + (-1/12)*k{39} + 7/48*k{40} + (-1/6)*k{41} + (-1/24)*k{42} + (-11/24)*k{43} + (-3)*k{48} + (-3/2)*k{49} + (-1/4)*k{50}'''))
    substitute(ex, Ex(r'''e{237} -> (-17/192)*k{4} + 49/2304*k{6} + 185/3072*k{7} + (-23/288)*k{11} + (-19/288)*k{12} + 13/288*k{13} + (-5/1152)*k{14} + (-1/6)*k{15} + (-5/192)*k{16} + (-1/4)*k{38} + (-29/288)*k{39} + (-79/576)*k{40} + (-23/144)*k{41} + (-11/288)*k{42} + (-7/144)*k{43} + 1/6*k{44} + 1/4*k{47} + 1/4*k{48} + 1/8*k{49} + (-1/48)*k{50}'''))
    return(ex)

def shift(massABC, kinABCI, kinABpCq):
    substitute(massABC,  Ex(r'e{q??} -> f{q??}'))
    substitute(kinABCI,  Ex(r'e{q??} -> f{q??}'))
    substitute(kinABpCq, Ex(r'e{q??} -> f{q??}'))

    substitute(massABC, Ex(r'f{1} -> e{41}'))
    substitute(massABC, Ex(r'f{2} -> e{42}'))
    substitute(massABC, Ex(r'f{3} -> e{43}'))
    substitute(massABC, Ex(r'f{4} -> e{44}'))
    substitute(massABC, Ex(r'f{5} -> e{45}'))
    substitute(massABC, Ex(r'f{6} -> e{46}'))
    substitute(massABC, Ex(r'f{7} -> e{47}'))
    substitute(massABC, Ex(r'f{8} -> e{48}'))
    substitute(massABC, Ex(r'f{9} -> e{49}'))
    substitute(massABC, Ex(r'f{10} -> e{50}'))
    substitute(massABC, Ex(r'f{11} -> e{51}'))
    substitute(massABC, Ex(r'f{12} -> e{52}'))
    substitute(massABC, Ex(r'f{13} -> e{53}'))
    substitute(massABC, Ex(r'f{14} -> e{54}'))
    substitute(massABC, Ex(r'f{15} -> e{55}'))

    substitute(kinABCI, Ex(r'f{1} -> e{166}'))
    substitute(kinABCI, Ex(r'f{2} -> e{167}'))
    substitute(kinABCI, Ex(r'f{3} -> e{168}'))
    substitute(kinABCI, Ex(r'f{4} -> e{169}'))
    substitute(kinABCI, Ex(r'f{5} -> e{170}'))
    substitute(kinABCI, Ex(r'f{6} -> e{171}'))
    substitute(kinABCI, Ex(r'f{7} -> e{172}'))
    substitute(kinABCI, Ex(r'f{8} -> e{173}'))
    substitute(kinABCI, Ex(r'f{9} -> e{174}'))
    substitute(kinABCI, Ex(r'f{10} -> e{175}'))
    substitute(kinABCI, Ex(r'f{11} -> e{176}'))
    substitute(kinABCI, Ex(r'f{12} -> e{177}'))
    substitute(kinABCI, Ex(r'f{13} -> e{178}'))
    substitute(kinABCI, Ex(r'f{14} -> e{179}'))
    substitute(kinABCI, Ex(r'f{15} -> e{180}'))
    substitute(kinABCI, Ex(r'f{16} -> e{181}'))
    substitute(kinABCI, Ex(r'f{17} -> e{182}'))
    substitute(kinABCI, Ex(r'f{18} -> e{183}'))
    substitute(kinABCI, Ex(r'f{19} -> e{184}'))
    substitute(kinABCI, Ex(r'f{20} -> e{185}'))
    substitute(kinABCI, Ex(r'f{21} -> e{186}'))
    substitute(kinABCI, Ex(r'f{22} -> e{187}'))
    substitute(kinABCI, Ex(r'f{23} -> e{188}'))
    substitute(kinABCI, Ex(r'f{24} -> e{189}'))
    substitute(kinABCI, Ex(r'f{25} -> e{190}'))
    substitute(kinABCI, Ex(r'f{26} -> e{191}'))
    substitute(kinABCI, Ex(r'f{27} -> e{192}'))
    substitute(kinABCI, Ex(r'f{28} -> e{193}'))
    substitute(kinABCI, Ex(r'f{29} -> e{194}'))
    substitute(kinABCI, Ex(r'f{30} -> e{195}'))
    substitute(kinABCI, Ex(r'f{31} -> e{196}'))
    substitute(kinABCI, Ex(r'f{32} -> e{197}'))
    substitute(kinABCI, Ex(r'f{33} -> e{198}'))
    substitute(kinABCI, Ex(r'f{34} -> e{199}'))
    substitute(kinABCI, Ex(r'f{35} -> e{200}'))
    substitute(kinABCI, Ex(r'f{36} -> e{201}'))
    substitute(kinABCI, Ex(r'f{37} -> e{202}'))
    substitute(kinABCI, Ex(r'f{38} -> e{203}'))
    substitute(kinABCI, Ex(r'f{39} -> e{204}'))
    substitute(kinABCI, Ex(r'f{40} -> e{205}'))
    substitute(kinABCI, Ex(r'f{41} -> e{206}'))
    substitute(kinABCI, Ex(r'f{42} -> e{207}'))
    substitute(kinABCI, Ex(r'f{43} -> e{208}'))
    substitute(kinABCI, Ex(r'f{44} -> e{209}'))
    substitute(kinABCI, Ex(r'f{45} -> e{210}'))
    substitute(kinABCI, Ex(r'f{46} -> e{211}'))
    substitute(kinABCI, Ex(r'f{47} -> e{212}'))
    substitute(kinABCI, Ex(r'f{48} -> e{213}'))
    substitute(kinABCI, Ex(r'f{49} -> e{214}'))
    substitute(kinABCI, Ex(r'f{50} -> e{215}'))
    substitute(kinABCI, Ex(r'f{51} -> e{216}'))
    substitute(kinABCI, Ex(r'f{52} -> e{217}'))
    substitute(kinABCI, Ex(r'f{53} -> e{218}'))
    substitute(kinABCI, Ex(r'f{54} -> e{219}'))
    substitute(kinABCI, Ex(r'f{55} -> e{220}'))
    substitute(kinABCI, Ex(r'f{56} -> e{221}'))
    substitute(kinABCI, Ex(r'f{57} -> e{222}'))
    substitute(kinABCI, Ex(r'f{58} -> e{223}'))
    substitute(kinABCI, Ex(r'f{59} -> e{224}'))
    substitute(kinABCI, Ex(r'f{60} -> e{225}'))
    substitute(kinABCI, Ex(r'f{61} -> e{226}'))
    substitute(kinABCI, Ex(r'f{62} -> e{227}'))
    substitute(kinABCI, Ex(r'f{63} -> e{228}'))
    substitute(kinABCI, Ex(r'f{64} -> e{229}'))
    substitute(kinABCI, Ex(r'f{65} -> e{230}'))
    substitute(kinABCI, Ex(r'f{66} -> e{231}'))
    substitute(kinABCI, Ex(r'f{67} -> e{232}'))
    substitute(kinABCI, Ex(r'f{68} -> e{233}'))
    substitute(kinABCI, Ex(r'f{69} -> e{234}'))
    substitute(kinABCI, Ex(r'f{70} -> e{235}'))
    substitute(kinABCI, Ex(r'f{71} -> e{236}'))
    substitute(kinABCI, Ex(r'f{72} -> e{237}'))

    substitute(kinABpCq, Ex(r'f{1} -> e{56}'))
    substitute(kinABpCq, Ex(r'f{2} -> e{57}'))
    substitute(kinABpCq, Ex(r'f{3} -> e{58}'))
    substitute(kinABpCq, Ex(r'f{4} -> e{59}'))
    substitute(kinABpCq, Ex(r'f{5} -> e{60}'))
    substitute(kinABpCq, Ex(r'f{6} -> e{61}'))
    substitute(kinABpCq, Ex(r'f{7} -> e{62}'))
    substitute(kinABpCq, Ex(r'f{8} -> e{63}'))
    substitute(kinABpCq, Ex(r'f{9} -> e{64}'))
    substitute(kinABpCq, Ex(r'f{10} -> e{65}'))
    substitute(kinABpCq, Ex(r'f{11} -> e{66}'))
    substitute(kinABpCq, Ex(r'f{12} -> e{67}'))
    substitute(kinABpCq, Ex(r'f{13} -> e{68}'))
    substitute(kinABpCq, Ex(r'f{14} -> e{69}'))
    substitute(kinABpCq, Ex(r'f{15} -> e{70}'))
    substitute(kinABpCq, Ex(r'f{16} -> e{71}'))
    substitute(kinABpCq, Ex(r'f{17} -> e{72}'))
    substitute(kinABpCq, Ex(r'f{18} -> e{73}'))
    substitute(kinABpCq, Ex(r'f{19} -> e{74}'))
    substitute(kinABpCq, Ex(r'f{20} -> e{75}'))
    substitute(kinABpCq, Ex(r'f{21} -> e{76}'))
    substitute(kinABpCq, Ex(r'f{22} -> e{77}'))
    substitute(kinABpCq, Ex(r'f{23} -> e{78}'))
    substitute(kinABpCq, Ex(r'f{24} -> e{79}'))
    substitute(kinABpCq, Ex(r'f{25} -> e{80}'))
    substitute(kinABpCq, Ex(r'f{26} -> e{81}'))
    substitute(kinABpCq, Ex(r'f{27} -> e{82}'))
    substitute(kinABpCq, Ex(r'f{28} -> e{83}'))
    substitute(kinABpCq, Ex(r'f{29} -> e{84}'))
    substitute(kinABpCq, Ex(r'f{30} -> e{85}'))
    substitute(kinABpCq, Ex(r'f{31} -> e{86}'))
    substitute(kinABpCq, Ex(r'f{32} -> e{87}'))
    substitute(kinABpCq, Ex(r'f{33} -> e{88}'))
    substitute(kinABpCq, Ex(r'f{34} -> e{89}'))
    substitute(kinABpCq, Ex(r'f{35} -> e{90}'))
    substitute(kinABpCq, Ex(r'f{36} -> e{91}'))
    substitute(kinABpCq, Ex(r'f{37} -> e{92}'))
    substitute(kinABpCq, Ex(r'f{38} -> e{93}'))
    substitute(kinABpCq, Ex(r'f{39} -> e{94}'))
    substitute(kinABpCq, Ex(r'f{40} -> e{95}'))
    substitute(kinABpCq, Ex(r'f{41} -> e{96}'))
    substitute(kinABpCq, Ex(r'f{42} -> e{97}'))
    substitute(kinABpCq, Ex(r'f{43} -> e{98}'))
    substitute(kinABpCq, Ex(r'f{44} -> e{99}'))
    substitute(kinABpCq, Ex(r'f{45} -> e{100}'))
    substitute(kinABpCq, Ex(r'f{46} -> e{101}'))
    substitute(kinABpCq, Ex(r'f{47} -> e{102}'))
    substitute(kinABpCq, Ex(r'f{48} -> e{103}'))
    substitute(kinABpCq, Ex(r'f{49} -> e{104}'))
    substitute(kinABpCq, Ex(r'f{50} -> e{105}'))
    substitute(kinABpCq, Ex(r'f{51} -> e{106}'))
    substitute(kinABpCq, Ex(r'f{52} -> e{107}'))
    substitute(kinABpCq, Ex(r'f{53} -> e{108}'))
    substitute(kinABpCq, Ex(r'f{54} -> e{109}'))
    substitute(kinABpCq, Ex(r'f{55} -> e{110}'))
    substitute(kinABpCq, Ex(r'f{56} -> e{111}'))
    substitute(kinABpCq, Ex(r'f{57} -> e{112}'))
    substitute(kinABpCq, Ex(r'f{58} -> e{113}'))
    substitute(kinABpCq, Ex(r'f{59} -> e{114}'))
    substitute(kinABpCq, Ex(r'f{60} -> e{115}'))
    substitute(kinABpCq, Ex(r'f{61} -> e{116}'))
    substitute(kinABpCq, Ex(r'f{62} -> e{117}'))
    substitute(kinABpCq, Ex(r'f{63} -> e{118}'))
    substitute(kinABpCq, Ex(r'f{64} -> e{119}'))
    substitute(kinABpCq, Ex(r'f{65} -> e{120}'))
    substitute(kinABpCq, Ex(r'f{66} -> e{121}'))
    substitute(kinABpCq, Ex(r'f{67} -> e{122}'))
    substitute(kinABpCq, Ex(r'f{68} -> e{123}'))
    substitute(kinABpCq, Ex(r'f{69} -> e{124}'))
    substitute(kinABpCq, Ex(r'f{70} -> e{125}'))
    substitute(kinABpCq, Ex(r'f{71} -> e{126}'))
    substitute(kinABpCq, Ex(r'f{72} -> e{127}'))
    substitute(kinABpCq, Ex(r'f{73} -> e{128}'))
    substitute(kinABpCq, Ex(r'f{74} -> e{129}'))
    substitute(kinABpCq, Ex(r'f{75} -> e{130}'))
    substitute(kinABpCq, Ex(r'f{76} -> e{131}'))
    substitute(kinABpCq, Ex(r'f{77} -> e{132}'))
    substitute(kinABpCq, Ex(r'f{78} -> e{133}'))
    substitute(kinABpCq, Ex(r'f{79} -> e{134}'))
    substitute(kinABpCq, Ex(r'f{80} -> e{135}'))
    substitute(kinABpCq, Ex(r'f{81} -> e{136}'))
    substitute(kinABpCq, Ex(r'f{82} -> e{137}'))
    substitute(kinABpCq, Ex(r'f{83} -> e{138}'))
    substitute(kinABpCq, Ex(r'f{84} -> e{139}'))
    substitute(kinABpCq, Ex(r'f{85} -> e{140}'))
    substitute(kinABpCq, Ex(r'f{86} -> e{141}'))
    substitute(kinABpCq, Ex(r'f{87} -> e{142}'))
    substitute(kinABpCq, Ex(r'f{88} -> e{143}'))
    substitute(kinABpCq, Ex(r'f{89} -> e{144}'))
    substitute(kinABpCq, Ex(r'f{90} -> e{145}'))
    substitute(kinABpCq, Ex(r'f{91} -> e{146}'))
    substitute(kinABpCq, Ex(r'f{92} -> e{147}'))
    substitute(kinABpCq, Ex(r'f{93} -> e{148}'))
    substitute(kinABpCq, Ex(r'f{94} -> e{149}'))
    substitute(kinABpCq, Ex(r'f{95} -> e{150}'))
    substitute(kinABpCq, Ex(r'f{96} -> e{151}'))
    substitute(kinABpCq, Ex(r'f{97} -> e{152}'))
    substitute(kinABpCq, Ex(r'f{98} -> e{153}'))
    substitute(kinABpCq, Ex(r'f{99} -> e{154}'))
    substitute(kinABpCq, Ex(r'f{100} -> e{155}'))
    substitute(kinABpCq, Ex(r'f{101} -> e{156}'))
    substitute(kinABpCq, Ex(r'f{102} -> e{157}'))
    substitute(kinABpCq, Ex(r'f{103} -> e{158}'))
    substitute(kinABpCq, Ex(r'f{104} -> e{159}'))
    substitute(kinABpCq, Ex(r'f{105} -> e{160}'))
    substitute(kinABpCq, Ex(r'f{106} -> e{161}'))
    substitute(kinABpCq, Ex(r'f{107} -> e{162}'))
    substitute(kinABpCq, Ex(r'f{108} -> e{163}'))
    substitute(kinABpCq, Ex(r'f{109} -> e{164}'))
    substitute(kinABpCq, Ex(r'f{110} -> e{165}'))

def noether0():
  n1temp = eom_from_files(Ex(r'A'))
  substitute(n1temp, Ex(r'\int{Q??}{x} -> Q??'))
  distribute(n1temp, repeat=True)
  substitute(n1temp, Ex(r'dA -> 1'))
  n1 = Ex(r'\partial_{0}{@(n1temp)}')
  simplify3d(n1)

  n2temp = eom_from_files(Ex(r'B^{\alpha}'))
  substitute(n2temp, Ex(r'\int{Q??}{x} -> Q??'))
  distribute(n2temp, repeat=True)
  substitute(n2temp, Ex(r'dB^{\alpha} -> \gamma^{\alpha \tau101}'))
  n2 = Ex(r'\partial_{\tau101}{@(n2temp)}')
  simplify3d(n2)

  n = Ex(r'@(n1) - @(n2)')
  simplify3d(n)

  factor_in(n, Ex(r'k{1}, k{2}, k{3}, k{4}, k{5}, k{6}, k{7}, k{8}, k{9}, k{10}, k{11}, k{12}, k{13}, k{14}, k{15}, k{16}'))

  return(n)

def noethera():
  n1temp = eom_from_files(Ex(r'B^{\alpha}'))
  substitute(n1temp, Ex(r'\int{Q??}{x} -> Q??'))
  distribute(n1temp, repeat=True)
  substitute(n1temp, Ex(r'dB^{\alpha} -> \delta^{\alpha}_{\tau100}'))
  n1 = Ex(r'\partial_{0}{@(n1temp)}')
  simplify3d(n1)

  n2temp = eom_from_files(Ex(r'U^{\alpha \beta}'))
  substitute(n2temp, Ex(r'\int{Q??}{x} -> Q??'))
  distribute(n2temp, repeat=True)
  substitute(n2temp, Ex(r'dU^{\alpha \beta} -> 1/2 \delta^{\alpha}_{\tau100} \gamma^{\beta \tau101} + 1/2 \delta^{\beta}_{\tau100} \gamma^{\alpha \tau101}'))
  n2 = Ex(r'\partial_{\tau101}{@(n2temp)}')
  simplify3d(n2)

  n = Ex(r'@(n1) - 4 @(n2)')
  simplify3d(n)

  factor_in(n, Ex(r'k{1}, k{2}, k{3}, k{4}, k{5}, k{6}, k{7}, k{8}, k{9}, k{10}, k{11}, k{12}, k{13}, k{14}, k{15}, k{16}, k{17}, k{18}, k{19}, k{20}, k{21}, k{22}, k{23}, k{24}, k{25}, k{26}, k{27}, k{28}, k{29}, k{30}, k{31}, k{32}, k{33}, k{34}, k{35}, k{36}, k{37}, k{38}, k{39}, k{40}, k{41}, k{42}, k{43}, k{44}, k{45}, k{46}, k{47}, k{48}, k{49}, k{50}'))

  return(n)

def noether():
  return(noether0(),noethera())

def simplify3d(n):
  distribute(n, repeat=True)
  unwrap(n, repeat=True)
  distribute(n, repeat=True)
  unwrap(n, repeat=True)
  distribute(n, repeat=True)
  unwrap(n, repeat=True)

  substitute(n, ruleEpsToDelta1, repeat=True)
  substitute(n, ruleEpsToDelta2, repeat=True)
  substitute(n, ruleEpsToDelta3, repeat=True)

  distribute(n, repeat=True)

  rewrite_indices(n, Ex(r'\epsilon_{\alpha \beta \gamma}'), Ex(r'\gamma^{\alpha \beta}'))

  my_eliminate_metric(n)
  eliminate_kronecker(n, repeat=True)
  my_eliminate_metric(n)
  eliminate_kronecker(n, repeat=True)
  my_eliminate_metric(n)
  eliminate_kronecker(n, repeat=True)
  my_eliminate_metric(n)
  eliminate_kronecker(n, repeat=True)

  my_canonicalise(n)
