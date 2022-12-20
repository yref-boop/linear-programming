from pyomo.environ import *
from pyomo.opt import SolverFactory

# define models
model=ConcreteModel()

# variable definition
model.x=Var(domain=NonNegativeIntegers)
model.y=Var(domain=NonNegativeIntegers)
model.z=Var(domain=NonNegativeIntegers)

# objetive function definition
model.profit=Objective(expr=2*model.x+3*model.y+model.z, sense=maximize)

# constraints
model.r1=Constraint(expr=650*model.x+420*model.y+720*model.z<=12000)
model.r2=Constraint(expr=model.z>=5)
model.r3=Constraint(expr=model.y>=2)
model.r4=Constraint(expr=model.y<=5)
model.r5=Constraint(expr=model.x-5*model.y<=0)
model.r6=Constraint(expr=-model.x+2*model.y<=0)

# solve problem
results=SolverFactory('glpk').solve(model)
results.write()

# show results
if results.solver.status=='ok':
    model.pprint()
    print('Beneficio=', model.profit())
    print('x=',model.x())
    print('y=',model.y())
    print('y=',model.z())
