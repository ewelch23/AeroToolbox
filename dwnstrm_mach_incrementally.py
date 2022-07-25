## E. Welch
## July 2022

'''This program is used to calculate the downstream Mach number resulting
from a series of deflections of equal value.'''

import numpy as np
import tabulate as tabulate

## determine wave angle
def det_waveangle(M1, delta1, est_wvangl, gamma):
    f_theta = lambda theta: ((gamma+1)/2 * M1**2/(M1**2 * (np.sin(theta))**2-1)-1) * np.tan(theta) - 1/np.tan(delta1)
    df_theta = lambda theta: ((gamma+1)/2*M1**2/(M1**2*(np.sin(theta))**2-1)-1) * 1/(np.cos(theta))**2 - ((gamma+1)/2)*(M1**4 *np.sin(2*theta))/(M1**2*(np.sin(theta))**2-1)**2 * np.tan(theta)
    xi_1 = est_wvangl
    iteration = 0
    while np.abs(f_theta(xi_1)) > 0.01:
        iteration += 1
        xi = xi_1 - f_theta(xi_1)/df_theta(xi_1)
        xi_1 = xi
        if iteration > 10 or xi_1 < 0:
            print("Not converging, try different initial guess for wave angle")
            quit()
    print("wave angle found in "+ str(iteration)+" iterations", "\nwave angle: "+ str(np.rad2deg(xi_1)))
    return xi_1  # returns radians


## determine M2
def M2_calc(M1, waveangle, deflection, gamma):
    M1_n = M1*np.sin(waveangle)
    M2_n = np.sqrt(( M1_n**2+2/(gamma-1) ) / ( 2*gamma/(gamma-1)*M1_n**2 -1))
    M2 = M2_n / np.sin(waveangle-deflection)
    return M2


M = float(input("Upstream Mach number = "))
gamma = float(input("Ratio of specific heats = "))
total_deflect = float(input("Total deflection angle (degrees) = "))
turns = float(input("Amount of turns/deflections = "))
wvangl_est = float(input("Wave angle estimate (for Newton's method) = "))

delta = total_deflect/turns


number_deflections = 1
while number_deflections <= turns: 
    print("##########################################")
    print("delta = "+str(delta))
    print("M = " + str(M))
    print("deflection number = "+str(number_deflections))
    print("wave angle estimation = "+ str(wvangl_est))
    print("finding wave angle.........")
    theta = det_waveangle(M, np.deg2rad(delta), np.deg2rad(wvangl_est), gamma)
    M2 = M2_calc(M, theta, delta, gamma)
    print("M_2 = "+str(M2))
    wvangl_est += np.deg2rad(1.5)  # a general estimate; may be increased or decreased depending on upstream conditions/increment
    M = M2
    number_deflections += 1

print("Mach found for "+str(number_deflections)+" deflections of angle "+str(delta)+" degrees")
print("Downstream Mach number = "+str(M))

