## E. Welch 2022
## inputs: gamma, M1, wave angle
## outputs: stagnation pressure ratio, static temp, pressure, and density ratio
## for either oblique or normal shock

from numpy import sin, deg2rad, log

gamma = float(input("gamma? "))
M1 = float(input("M1? "))
theta = deg2rad(float(input("wave angle (for normal shock input 90)? ")))
R = float(input("Specific gas constant? "))

p02 = (((gamma+1)/2 * M1**2*(sin(theta)**2))/( 1 + (gamma-1)/2 * M1**2*(sin(theta))**2 ))**(gamma/(gamma-1))

p01 = ( 2*gamma/(gamma+1) * M1**2 * (sin(theta))**2 - (gamma-1)/(gamma+1) )**(1/(gamma-1))

pr_stag = p02/p01

pr_static = (2*gamma)/(gamma+1) * M1**2*(sin(theta))**2 - (gamma-1)/(gamma+1)

T2 = (1 + (gamma-1)/2 * M1**2 * (sin(theta))**2) * (2*gamma/(gamma-1)*M1**2*(sin(theta))**2-1)
T1 = (gamma+1)**2/(2*(gamma-1)) * M1**2 * (sin(theta))**2
Tr_static = T2/T1
densityr_static = 2/((gamma+1)*M1**2*(sin(theta))**2) + (gamma-1)/(gamma+1)

# deltas = R/(gamma-1) * log(2*gamma/(gamma+1)*M1**2-(gamma-1)/(gamma+1)) - gamma/(gamma-1) * log((((gamma+1)/2)*M1**2)/(1+(gamma-1)/2*M1**2))
delta_s = R * log(1/pr_stag)

print("-----------------------------------------------------------------------")
print("p02/p01 = " + str(pr_stag))
print("p2/p1 = "+str(pr_static))
print("T2/T1 = " + str(Tr_static))
print("rho1/rho2 = "+str(densityr_static))
print("change in entropy across shock = " + str(delta_s))

