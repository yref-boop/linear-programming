from pyomo.environ import *
from pyomo.opt import SolverFactory

# define models
model=ConcreteModel()

# variable definition
model.x0=Var(domain=NonNegativeIntegers)
model.x1=Var(domain=NonNegativeIntegers)
model.x2=Var(domain=NonNegativeIntegers)
model.x3=Var(domain=NonNegativeIntegers)

model.y0=Var(domain=NonNegativeIntegers)
model.y1=Var(domain=NonNegativeIntegers)
model.y2=Var(domain=NonNegativeIntegers)

model.z=Var(domain=NonNegativeIntegers)

# objetive function definition
model.profit=Objective(expr=0.04*(model.x0+model.x1+model.x2+model.x3)+0.07*(model.y0+model.y1+model.y2)+0.1*model.z, sense=maximize)

# constraints
model.r0=Constraint(expr=model.x0+model.y0<=2500)
model.r1=Constraint(expr=model.x1+model.y1<=(2500-model.y0+0.04*model.x0))
model.r2=Constraint(expr=model.x2+model.y2+model.z<=(2500+0.04*model.x0)-model.y1+0.07*model.y0+0.04*model.x1)
model.r3=Constraint(expr=model.x2+model.y2+model.z<=((2500+0.04*model.x0)+0.07*model.y0+0.04*model.x1)+0.7*model.y1+0.4*model.x2-model.x3)

# solve problem
results=SolverFactory('glpk').solve(model)
results.write()

# show results
if results.solver.status=='ok':
    model.pprint()
    print('profit=', model.profit())

    print('x0=',model.x0())
    print('x1=',model.x1())
    print('x2=',model.x2())
    print('x3=',model.x3())

    print('y0=',model.y0())
    print('y1=',model.y1())
    print('y2=',model.y2())

    print('z=',model.z())
