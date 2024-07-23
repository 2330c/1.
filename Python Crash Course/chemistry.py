from chemlib import Compound, Reaction, Combustion
N2O5 = Compound("N2O5")
H2O = Compound("H2O")
HNO3 = Compound("HNO3")
r = Reaction([N2O5, H2O], [HNO3])

r = Reaction.by_formula("N2O5 + H2O --> HNO3")
print(r.formula)
print(r.is_balanced)
print(r.reactant_formulas)
print(r.product_formulas)

methane = Compound('CH4')
c = Combustion(methane)
print(c.formula)
print(c.is_balanced)

print(r.balance())
print(r.formula)