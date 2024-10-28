from pulp import LpMaximize, LpProblem, LpVariable

# Model
model = LpProblem(name="maximize-drinks-production", sense=LpMaximize)
# Lemonade and Fruit Juice
lemonade = LpVariable(name="lemonade", lowBound=0, cat='Continuous')
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Continuous')
# Maximize the total amount of lemonade and fruit juice produced
model += lemonade + fruit_juice, "Total_Production"
# Add the constraints based on the available resources:
# Water constraint: 2*lemonade + 1*fruit_juice <= 100
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
# Sugar constraint: 1*lemonade <= 50
model += lemonade <= 50, "Sugar_Constraint"
# Lemon juice constraint: 1*lemonade <= 30
model += lemonade <= 30, "Lemon_Juice_Constraint"
# Fruit puree constraint: 2*fruit_juice <= 40
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"
# Solve the optimization problem
model.solve()

# Results
print("Result")
print("----------------------------------------------")
print(f"Lemonade produced: {lemonade.varValue}")
print("----------------------------------------------")
print(f"Fruit juice produced: {fruit_juice.varValue}")
print("----------------------------------------------")
print(f"Total production: {lemonade.varValue + fruit_juice.varValue}")
print("----------------------------------------------")
