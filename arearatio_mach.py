import numpy as np

'''This program utilizes Newton's method to find the Mach number of a given area ratio.'''
## assuming the working fluid is air: ##
gamma = 1.4
A_Astar = float(input("Area ratio = "))
Mach_guess = float(input("Mach estimate = "))
def newton(f, df, est, error):
    xi_1 = est
    # print("initial guess:", xi_1)
    iteration = 0
    while np.abs(f(xi_1)) > error:
        iteration += 1
        xi = xi_1 - f(xi_1)/df(xi_1)
        xi_1 = xi
        # print("i="+str(iteration),"x="+str(xi_1**2))
        if iteration > 10:
            print("Not converging :(")
            quit()
    print("Mach number is: "+ str(xi_1**2), " found in : "+ str(iteration) + " iterations.")
    return xi_1

P = 2/(gamma+1)
Q = (gamma-1)/(gamma+1)
R = A_Astar**2
f = lambda x: (P+Q*x)**(1/Q)-R*x
df = lambda x: (P+Q*x)**(1/Q-1) - R
new_Mach = np.sqrt(newton(f, df, Mach_guess**2, 0.001))
print("The Mach number for area ratio ",A_Astar," is",new_Mach)
