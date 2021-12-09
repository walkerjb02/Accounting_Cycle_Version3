from matplotlib import pyplot as pt
import pandas as pd

class mixed_costs:
    def fixed_costs(self):
        pass
    def contribution_margin(self, sp, vc):
        def wrapper():
            con = sp - vc
            return con
        return wrapper()

    def components(self):
        sp = input()
        vc = input()
        return sp, vc

    def direct_costs(self):
        pass

    def indirect_costs(self):
        pass

    def factory_overhead(self):
        pass

    def tmfg(self):
        pass

m = mixed_costs()

class budgets:
    pass

b = budgets()

class income_s:
    def con_margin_generator(self):
        pass
    def breakeven_point(self):
        pass

i = income_s()

class graphs:
    def cvp(self):
        pass

g = graphs()
