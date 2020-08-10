from cadabra2 import *

Indices(Ex(r'''{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z#}'''), Ex(r'''fourD, position=independent''') )
Integer(Ex(r'''{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z#}'''), Ex(r'''0..3''') )

Indices(Ex(r'''{\alpha,\beta,\gamma,\delta,\epsilon,\zeta,\theta,\iota,\kappa,\lambda,\mu,\nu,\rho,\sigma,\tau#}'''), Ex(r'''threeD, position=independent, parent=fourD''') )
Integer(Ex(r'''{\alpha,\beta,\gamma,\delta,\epsilon,\zeta,\theta,\iota,\kappa,\lambda,\mu,\nu,\rho,\sigma,\tau#}'''), Ex(r'''1..3''') )

KroneckerDelta(Ex(r'''\delta{#}'''), Ex(r'''''') )
Symmetric(Ex(r'''\gamma_{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''\gamma^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''X^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''X1^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''Y^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''Y1^{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''Z^{\alpha \beta}'''), Ex(r'''''') )
EpsilonTensor(Ex(r'''\epsilon_{\alpha \beta \gamma}'''), Ex(r'''''') )
EpsilonTensor(Ex(r'''\epsilon^{\alpha \beta \gamma}'''), Ex(r'''''') )

AntiSymmetric(Ex(r'''\epsilon_{a? b? c? d?}'''), Ex(r'''''') )

Weight(Ex(r'''X1{#}'''), Ex(r'''label=w, value=1'''))
Weight(Ex(r'''Y1{#}'''), Ex(r'''label=w, value=1'''))
Weight(Ex(r'''Z{#}'''), Ex(r'''label=w, value=1'''))
Weight(Ex(r'''N^{\alpha}'''), Ex(r'''label=w, value=1'''))
Weight(Ex(r'''N1'''), Ex(r'''label=w, value=1'''))

SortOrder(Ex(r'''{\gamma_{p? q?},\epsilon_{p? q? r?},\gamma^{p? q?},\epsilon^{p? q? r?}'''), Ex(r'''''') )

rulegg1  = Ex(r''' \gamma^{\mu \nu} \gamma_{\mu \nu} -> 3''')
rulegg2  = Ex(r''' \gamma^{\mu \nu} \gamma_{\nu \mu} -> 3''')
rulegg3  = Ex(r''' \gamma^{\mu \nu} \gamma_{\mu \rho} -> \delta^{\nu}_{\rho}''')
rulegg4  = Ex(r''' \gamma^{\mu \nu} \gamma_{\rho \mu} -> \delta^{\nu}_{\rho}''')
rulegg5  = Ex(r''' \gamma^{\nu \mu} \gamma_{\mu \rho} -> \delta^{\nu}_{\rho}''')
rulegg6  = Ex(r''' \gamma^{\nu \mu} \gamma_{\rho \mu} -> \delta^{\nu}_{\rho}''')

def my_eliminate_metric(ex, repeat=False):
    substitute(ex, rulegg1, repeat=repeat)
    substitute(ex, rulegg2, repeat=repeat)
    substitute(ex, rulegg3, repeat=repeat)
    substitute(ex, rulegg4, repeat=repeat)
    substitute(ex, rulegg5, repeat=repeat)
    substitute(ex, rulegg6, repeat=repeat)
    return ex

rule_epsGGGkkkk = Ex(r''' epsGGGkkkk^{m? n? p? q?} -> \epsilon_{0 \alpha \beta \gamma} GGGkkkk^{m? n? p? q? 0 \alpha \beta \gamma} + \epsilon_{\alpha 0 \beta \gamma} GGGkkkk^{m? n? p? q? \alpha 0 \beta \gamma} + \epsilon_{\alpha \beta 0 \gamma} GGGkkkk^{m? n? p? q? \alpha \beta 0 \gamma} + \epsilon_{\alpha \beta \gamma 0} GGGkkkk^{m? n? p? q? \alpha \beta \gamma 0} ''')

rule_GGGkkkk = Ex(r''' GGGkkkk^{m? n? p? q? r? s? t? u?} -> GGG^{m? n? r? 0 0 p? s? 0 0 q? t? u?} k_{0} k_{0} k_{0} k_{0} + GGG^{m? n? r? 0 0 p? s? 0 \alpha q? t? u?} k_{0} k_{0} k_{0} k_{\alpha}  + GGG^{m? n? r? 0 0 p? s? \alpha 0 q? t? u?} k_{0} k_{0} k_{\alpha} k_{0} + GGG^{m? n? r? 0 \alpha p? s? 0 0 q? t? u?} k_{0} k_{\alpha} k_{0} k_{0} + GGG^{m? n? r? \alpha 0 p? s? 0 0 q? t? u?} k_{\alpha} k_{0} k_{0} k_{0} + GGG^{m? n? r? 0 0 p? s? \alpha \beta q? t? u?} k_{0} k_{0} k_{\alpha} k_{\beta} + GGG^{m? n? r? 0 \alpha p? s? 0 \beta q? t? u?} k_{0} k_{\alpha} k_{0} k_{\beta} + GGG^{m? n? r? \alpha 0 p? s? 0 \beta q? t? u?} k_{\alpha} k_{0} k_{0} k_{\beta} + GGG^{m? n? r? 0 \alpha p? s? \beta 0 q? t? u?} k_{0} k_{\alpha} k_{\beta} k_{0} + GGG^{m? n? r? \alpha 0 p? s? \beta 0 q? t? u?} k_{\alpha} k_{0} k_{\beta} k_{0} + GGG^{m? n? r? \alpha \beta p? s? 0 0 q? t? u?} k_{\alpha} k_{\beta} k_{0} k_{0} + GGG^{m? n? r? 0 \alpha p? s? \beta \gamma q? t? u?} k_{0} k_{\alpha} k_{\beta} k_{\gamma} + GGG^{m? n? r? \alpha 0 p? s? \beta \gamma q? t? u?} k_{\alpha} k_{0} k_{\beta} k_{\gamma} + GGG^{m? n? r? \alpha \beta p? s? 0 \gamma q? t? u?} k_{\alpha} k_{\beta} k_{0} k_{\gamma} + GGG^{m? n? r? \alpha \beta p? s? \gamma 0 q? t? u?} k_{\alpha} k_{\beta} k_{\gamma} k_{0} ''')

rule_GGG = Ex(r''' GGG^{m? n? r? a? b? p? s? c? d? q? t? u?} -> G^{m? n? r? a?} G^{b? p? s? c?} G^{d? q? t? u?} ''')

rule_G1 = Ex(r''' G^{0 0 0 0} -> 0 ''')
rule_G2 = Ex(r''' G^{0 0 0 \alpha} -> 0 ''')
rule_G3 = Ex(r''' G^{0 0 \alpha 0} -> 0 ''')
rule_G4 = Ex(r''' G^{0 \alpha 0 0} -> 0 ''')
rule_G5 = Ex(r''' G^{\alpha 0 0 0} -> 0 ''')
rule_G6 = Ex(r''' G^{0 0 \alpha \beta} -> 0 ''')
rule_G7 = Ex(r''' G^{0 \alpha 0 \beta} -> G^{0 \alpha 0 \beta} ''')
rule_G8 = Ex(r''' G^{\alpha 0 0 \beta} -> - G^{0 \alpha 0 \beta} ''')
rule_G9 = Ex(r''' G^{0 \alpha \beta 0} -> - G^{0 \alpha 0 \beta} ''')
rule_G10 = Ex(r''' G^{\alpha 0 \beta 0} -> G^{0 \alpha 0 \beta} ''')
rule_G11 = Ex(r''' G^{\alpha \beta 0 0} -> 0 ''')
rule_G12 = Ex(r''' G^{0 \alpha \beta \gamma} -> G^{0 \alpha \beta \gamma} ''')
rule_G13 = Ex(r''' G^{\alpha 0 \beta \gamma} -> -G^{0 \alpha \beta \gamma} ''')
rule_G14 = Ex(r''' G^{\alpha \beta 0 \gamma} -> G^{0 \gamma \alpha \beta} ''')
rule_G15 = Ex(r''' G^{\alpha \beta \gamma 0} -> -G^{0 \gamma \alpha \beta} ''')
rule_G16 = Ex(r''' G^{\alpha \beta \gamma \delta} -> G^{\alpha \beta \gamma \delta} ''')

rule_GX = Ex(r''' G^{0 \alpha 0 \beta} -> - \gamma^{\alpha \beta} ''')
rule_GZ = Ex(r''' G^{0 \alpha \beta \gamma} -> \epsilon^{\alpha \beta \gamma} ''')
rule_GY = Ex(r''' G^{\alpha \beta \gamma \delta} -> \gamma^{\alpha \gamma} \gamma^{\beta \delta} - \gamma^{\alpha \delta} \gamma^{\beta \gamma} ''')

# rule_GX = Ex(r''' G^{0 \alpha 0 \beta} -> -1/(N*N) X^{\alpha \beta} ''')
# rule_GZ = Ex(r''' G^{0 \alpha \beta \gamma} -> 1/(N*N) X^{\alpha \gamma} N^{\beta} - 1/(N*N) X^{\alpha \beta} N^{\gamma} + 1/N * w * \epsilon^{\alpha \beta \gamma} + 1/N * w * \epsilon^{\mu \beta \gamma} \gamma_{\mu \nu} Z^{\alpha \nu} ''')
# rule_GY = Ex(r''' G^{\alpha \beta \gamma \delta} -> -1/(N*N) N^{\alpha} N^{\gamma} X^{\beta \delta} + 1/(N*N) N^{\alpha} N^{\delta} X^{\beta \gamma} + 1/(N*N) N^{\beta} N^{\gamma} X^{\alpha \delta} - 1/(N*N) N^{\beta} N^{\delta} X^{\alpha \gamma} + 1/N * w * \epsilon^{\mu \gamma \delta} * \gamma_{\mu \nu} Z^{\beta \nu} N^{\alpha} - 1/N * w * \epsilon^{\mu \gamma \delta} * \gamma_{\mu \nu} Z^{\alpha \nu} N^{\beta} + 1/N * w * \epsilon^{\mu \alpha \beta} * \gamma_{\mu \nu} Z^{\delta \nu} N^{\gamma} - 1/N * w * \epsilon^{\mu \alpha \beta} * \gamma_{\mu \nu} Z^{\gamma \nu} N^{\delta} + 1/N * w * \epsilon^{\beta \gamma \delta} N^{\alpha} - 1/N * w * \epsilon^{\alpha \gamma \delta} N^{\beta} + 1/N * w * \epsilon^{\delta \alpha \beta} N^{\gamma} - 1/N * w * \epsilon^{\gamma \alpha \beta} N^{\delta} + w*w * \epsilon^{\mu \alpha \beta} \epsilon^{\nu \gamma \delta} \gamma_{\mu \rho} \gamma_{\nu \sigma} Y^{\rho \sigma}''')

rule_eps_eps = Ex(r''' \epsilon_{0 \alpha \beta \gamma} \epsilon_{0 \mu \nu \rho} -> \gamma_{\alpha \mu} \gamma_{\beta \nu} \gamma_{\gamma \rho} - \gamma_{\alpha \mu} \gamma_{\beta \rho} \gamma_{\gamma \nu} - \gamma_{\alpha \nu} \gamma_{\beta \mu} \gamma_{\gamma \rho} + \gamma_{\alpha \nu} \gamma_{\beta \rho} \gamma_{\gamma \mu} + \gamma_{\alpha \rho} \gamma_{\beta \mu} \gamma_{\gamma \nu} - \gamma_{\alpha \rho} \gamma_{\beta \nu} \gamma_{\gamma \mu} ''')

rule_epsI_epsI = Ex(r''' \epsilon^{\alpha \beta \gamma} \epsilon^{\mu \nu \rho} -> \gamma^{\alpha \mu} \gamma^{\beta \nu} \gamma^{\gamma \rho} - \gamma^{\alpha \mu} \gamma^{\beta \rho} \gamma^{\gamma \nu} - \gamma^{\alpha \nu} \gamma^{\beta \mu} \gamma^{\gamma \rho} + \gamma^{\alpha \nu} \gamma^{\beta \rho} \gamma^{\gamma \mu} + \gamma^{\alpha \rho} \gamma^{\beta \mu} \gamma^{\gamma \nu} - \gamma^{\alpha \rho} \gamma^{\beta \nu} \gamma^{\gamma \mu} ''')


def poly():
    ex = Ex(r''' -N*N/(24*w*w) ( \epsilon_{0 \alpha \beta \gamma} epsGGGkkkk^{0 \alpha \beta \gamma} + \epsilon_{\alpha 0 \beta \gamma} epsGGGkkkk^{\alpha 0 \beta \gamma} + \epsilon_{\alpha \beta 0 \gamma} epsGGGkkkk^{\alpha \beta 0 \gamma} + \epsilon_{\alpha \beta \gamma 0} epsGGGkkkk^{\alpha \beta \gamma 0} ) ''')

    distribute(ex, repeat=True)

    substitute(ex, rule_epsGGGkkkk)
    distribute(ex, repeat=True)

    substitute(ex, rule_GGGkkkk)
    distribute(ex, repeat=True)
    substitute(ex, rule_GGG)

    substitute(ex, rule_G1)
    substitute(ex, rule_G2)
    substitute(ex, rule_G3)
    substitute(ex, rule_G4)
    substitute(ex, rule_G5)
    substitute(ex, rule_G6)
    substitute(ex, rule_G7)
    substitute(ex, rule_G8)
    substitute(ex, rule_G9)
    substitute(ex, rule_G10)
    substitute(ex, rule_G11)
    substitute(ex, rule_G12)
    substitute(ex, rule_G13)
    substitute(ex, rule_G14)
    substitute(ex, rule_G15)
    substitute(ex, rule_G16)

    my_canonicalise(ex)

    substitute(ex, rule_eps_eps)
    distribute(ex, repeat=True)

    my_canonicalise(ex)

    substitute(ex, rule_GX, repeat=True)
    distribute(ex, repeat=True)
    my_canonicalise(ex)

    substitute(ex, rule_GY, repeat=True)
    distribute(ex, repeat=True)
    my_canonicalise(ex)

    substitute(ex, rule_GZ, repeat=True)
    distribute(ex, repeat=True)
    my_canonicalise(ex)

    my_eliminate_metric(ex, repeat=True)
    eliminate_kronecker(ex, repeat=True)

    my_eliminate_metric(ex, repeat=True)
    eliminate_kronecker(ex, repeat=True)

    my_eliminate_metric(ex, repeat=True)
    eliminate_kronecker(ex, repeat=True)

    my_canonicalise(ex)

    substitute(ex, rule_epsI_epsI)
    distribute(ex, repeat=True)

    my_eliminate_metric(ex, repeat=True)
    eliminate_kronecker(ex, repeat=True)

    my_eliminate_metric(ex, repeat=True)
    eliminate_kronecker(ex, repeat=True)

    my_eliminate_metric(ex, repeat=True)
    eliminate_kronecker(ex, repeat=True)

    my_canonicalise(ex)

    map_sympy(ex, "simplify")
    my_canonicalise(ex)

    substitute(ex, Ex(r'''\gamma_{\alpha \beta} Z^{\alpha \beta} -> 0'''))

    return(ex)

def my_canonicalise(ex):
    sort_product(ex)
    sort_sum(ex)
    canonicalise(ex)
    rename_dummies(ex)
    collect_terms(ex)

