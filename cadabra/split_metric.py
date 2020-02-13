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

Symmetric(Ex(r'''\eta_{a? b?}'''), Ex(r'''''') )

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
Depends(Ex(r'''dX{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''A'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''dA'''), Ex(r'''\partial{#})''') )
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

SortOrder(Ex(r'''{dX{#},dU{#},dV{#},dW{#},dB{#},dA,m{#},k{#},t{#},e{#},A,B{#},X{#},Y{#},Z{#},U{#},V{#},W{#},\partial{#},\gamma{#}}'''), Ex(r''')''') )

ruleH1  = Ex(r''' H1 -> -2 A''')
ruleH2  = Ex(r''' H2^{\mu} -> -B^{\mu}''')
ruleH3  = Ex(r''' H3^{\mu \nu} -> -X^{\mu \nu}''')

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

rulegg1  = Ex(r''' \gamma^{\mu \nu} \gamma_{\mu \nu} -> 3''')
rulegg2  = Ex(r''' \gamma^{\mu \nu} \gamma_{\nu \mu} -> 3''')
rulegg3  = Ex(r''' \gamma^{\mu \nu} \gamma_{\mu \rho} -> \delta^{\nu}_{\rho}''')
rulegg4  = Ex(r''' \gamma^{\mu \nu} \gamma_{\rho \mu} -> \delta^{\nu}_{\rho}''')
rulegg5  = Ex(r''' \gamma^{\nu \mu} \gamma_{\mu \rho} -> \delta^{\nu}_{\rho}''')
rulegg6  = Ex(r''' \gamma^{\nu \mu} \gamma_{\rho \mu} -> \delta^{\nu}_{\rho}''')

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

def kin_ABI():
    ruleM1 = Ex(r''' M{1}_{a? b? c? d?}^{p? q?} -> (-1/2) * \eta_{a? b?} \eta_{c? d?} \eta^{p? q?}''')
    ruleM2 = Ex(r''' M{2}_{a? b? c? d?}^{p? q?} ->          \delta_{a?}^{p?} \delta_{b?}^{q?} \eta_{c? d?}''')
    ruleM3 = Ex(r''' M{3}_{a? b? c? d?}^{p? q?} ->          \eta_{a? c?} \eta_{b? d?} \eta^{p? q?}''')
    ruleM4 = Ex(r''' M{4}_{a? b? c? d?}^{p? q?} ->  (1/2) * \eta_{a? b?} \delta_{c?}^{p?} \delta_{d?}^{q?}''')
    ruleM5 = Ex(r''' M{5}_{a? b? c? d?}^{p? q?} ->   (-2) * \eta_{a? c?} \delta_{b?}^{p?} \delta_{d?}^{q?}''')
    
    ruleM  = Ex(r''' M_{a? b? c? d?}^{p? q?} -> M{1}_{a? b? c? d?}^{p? q?} + M{2}_{a? b? c? d?}^{p? q?} + M{3}_{a? b? c? d?}^{p? q?} + M{4}_{a? b? c? d?}^{p? q?} + M{5}_{a? b? c? d?}^{p? q?}''')
    
    ruleMH1  = Ex(r''' M_{a b c? d?}^{p? q?} H^{a b} -> M_{0 0 c? d?}^{p? q?} H1 + (M_{0 \mu c? d?}^{p? q?} + M_{\mu 0 c? d?}^{p? q?}) H2^{\mu} + M_{\mu \nu c? d?}^{p? q?} H3^{\mu \nu}''')
    
    ruleMH2  = Ex(r''' M_{c? d? a b}^{p q} \partial_{p q}{H^{a b}} -> M_{c? d? 0 0}^{0 0} \partial_{0 0}{H1} + M_{c? d? 0 0}^{0 \alpha} \partial_{0 \alpha}{H1} + M_{c? d? 0 0}^{\alpha 0} \partial_{0 \alpha}{H1} + M_{c? d? 0 0}^{\alpha \beta} \partial_{\alpha \beta}{H1} + (M_{c? d? 0 \mu}^{0 0} + M_{c? d? \mu 0}^{0 0}) \partial_{0 0}{H2^{\mu}} + (M_{c? d? 0 \mu}^{0 \alpha} + M_{c? d? \mu 0}^{0 \alpha}) \partial_{0 \alpha}{H2^{\mu}} + (M_{c? d? 0 \mu}^{\alpha 0} + M_{c? d? \mu 0}^{\alpha 0}) \partial_{0 \alpha}{H2^{\mu}} + (M_{c? d? 0 \mu}^{\alpha \beta} + M_{c? d? \mu 0}^{\alpha \beta}) \partial_{\alpha \beta}{H2^{\mu}} + M_{c? d? \mu \nu}^{0 0} \partial_{0 0}{H3^{\mu \nu}} + M_{c? d? \mu \nu}^{0 \alpha} \partial_{0 \alpha}{H3^{\mu \nu}} + M_{c? d? \mu \nu}^{\alpha 0} \partial_{0 \alpha}{H3^{\mu \nu}} + M_{c? d? \mu \nu}^{\alpha \beta} \partial_{\alpha \beta}{H3^{\mu \nu}}''')
    
    ex  = Ex(r'''M_{a b c d}^{p q} H^{a b} \partial_{p q}{H^{c d}}''')
    
    
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

    three_plus_one(ex)

    return(ex)

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
    substitute(ex, ruleDelta2, repeat=True)
    substitute(ex, ruleDelta3, repeat=True)

def subs_delta_eta(ex):
    substitute(ex, Ex(r'''\delta^{p?}_{a} \eta^{a q?} -> \eta^{p? q?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{p?}_{a} \eta^{q? a} -> \eta^{p? q?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{a}_{p?} \eta_{a q?} -> \eta_{p? q?}'''), repeat=True)
    substitute(ex, Ex(r'''\delta^{a}_{p?} \eta_{q? a} -> \eta_{p? q?}'''), repeat=True)

def normalize_delta(ex):
    substitute(ex, Ex(r'''\delta_{p?}^{q?} -> \delta^{q?}_{p?}'''), repeat=True)

def my_canonicalise(ex):
    sort_product(ex)
    sort_sum(ex)
    canonicalise(ex)
    rename_dummies(ex)
    collect_terms(ex)

def three_plus_one(ex):
    eliminate_eta(ex)
    three_plus_one_eta(ex)

    distribute(ex, repeat=True)

    normalize_delta(ex)
    my_eliminate_kronecker(ex)
    three_plus_one_delta(ex)
    
    subs_delta_eta(ex)
    
    my_canonicalise(ex)

    normalize_delta(ex)

    three_plus_one_delta(ex)
    three_plus_one_eta(ex)

    my_canonicalise(ex)

    substitute(ex, ruleH1, repeat=True)
    substitute(ex, ruleH2, repeat=True)
    substitute(ex, ruleH3, repeat=True)

    distribute(ex)
    unwrap(ex)

    distribute(ex)

    my_canonicalise(ex)
    
    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)
    
    my_canonicalise(ex)
    
    unwrap(ex)
    distribute(ex)
    
    distribute(ex)
    
    my_canonicalise(ex)

    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)
    my_eliminate_metric(ex)
    eliminate_kronecker(ex, repeat=True)

    my_canonicalise(ex)
    
    return(ex)

def kin_ApBq():
    ruleM1 = Ex(r''' M{1}_{a? b?}^{p?}_{c? d?}^{q?} -> (-1/4) * \eta_{a? b?} \eta_{c? d?} \eta^{p? q?}''')
    ruleM2 = Ex(r''' M{2}_{a? b?}^{p?}_{c? d?}^{q?} ->          \eta_{a? b?} \delta_{c?}^{p?} \delta_{d?}^{q?}''')
    ruleM3 = Ex(r''' M{3}_{a? b?}^{p?}_{c? d?}^{q?} -> (-1/2) * \delta_{a?}^{q?} \eta_{b? c?} \delta_{d?}^{p?}''')
    ruleM4 = Ex(r''' M{4}_{a? b?}^{p?}_{c? d?}^{q?} ->  (3/4) * \eta_{a? c?} \eta_{b? d?} \eta^{p? q?}''')
    ruleM5 = Ex(r''' M{5}_{a? b?}^{p?}_{c? d?}^{q?} ->   (-1) * \delta_{a?}^{p?} \eta_{b? c?} \delta_{d?}^{q?}''')
    
    ruleM  = Ex(r''' M_{a? b?}^{p?}_{c? d?}^{q?} -> M{1}_{a? b?}^{p?}_{c? d?}^{q?} + M{2}_{a? b?}^{p?}_{c? d?}^{q?} + M{3}_{a? b?}^{p?}_{c? d?}^{q?} + M{4}_{a? b?}^{p?}_{c? d?}^{q?} + M{5}_{a? b?}^{p?}_{c? d?}^{q?}''')
    
    ruleMH1  = Ex(r''' M_{a b}^{p}_{c? d?}^{q?} \partial_{p}{H^{a b}} -> M_{0 0}^{0}_{c? d?}^{q?} \partial_{0}{H1} + M_{0 0}^{\alpha}_{c? d?}^{q?} \partial_{\alpha}{H1} + (M_{0 \mu}^{0}_{c? d?}^{q?} + M_{\mu 0}^{0}_{c? d?}^{q?}) \partial_{0}{H2^{\mu}} + (M_{0 \mu}^{\alpha}_{c? d?}^{q?} + M_{\mu 0}^{\alpha}_{c? d?}^{q?}) \partial_{\alpha}{H2^{\mu}} + M_{\mu \nu}^{0}_{c? d?}^{q?} \partial_{0}{H3^{\mu \nu}} + M_{\mu \nu}^{\alpha}_{c? d?}^{q?} \partial_{\alpha}{H3^{\mu \nu}}''')
    
    ruleMH2  = Ex(r''' M_{c? d?}^{q?}_{a b}^{p} \partial_{p}{H^{a b}} -> M_{c? d?}^{q?}_{0 0}^{0} \partial_{0}{H1} + M_{c? d?}^{q?}_{0 0}^{\alpha} \partial_{\alpha}{H1} + (M_{c? d?}^{q?}_{0 \mu}^{0} + M_{c? d?}^{q?}_{\mu 0}^{0}) \partial_{0}{H2^{\mu}} + (M_{c? d?}^{q?}_{0 \mu}^{\alpha} + M_{c? d?}^{q?}_{\mu 0}^{\alpha}) \partial_{\alpha}{H2^{\mu}} + M_{c? d?}^{q?}_{\mu \nu}^{0} \partial_{0}{H3^{\mu \nu}} + M_{c? d?}^{q?}_{\mu \nu}^{\alpha} \partial_{\alpha}{H3^{\mu \nu}}''')
    
    ex  = Ex(r''' M_{a b}^{p}_{c d}^{q} \partial_{p}{H^{a b}} \partial_{q}{H^{c d}}''')
    
    
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
    
    three_plus_one(ex)

    return(ex)

def eom(kinABI, kinApBq, toVary):
    apply_sol(kinABI)
    apply_sol(kinApBq)

    variation = Ex(r'd' + toVary.input_form())
    ruleVary = Ex(r'@{toVary} -> @{variation}')

    ex = Ex(r'\int{@(massAB) + @(kinABI) + @(kinApBq)}{x}')

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
