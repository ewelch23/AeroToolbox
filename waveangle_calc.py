## E. Welch 2022
## Newton-Raphson Method for oblique Mach waves
## inputs: gamma, M1, deflection angle, and an estimate for the wave angle
## returns: wave angle + iterations untill convergence
import numpy as np

## inputs in degrees only
gamma = float(input("gamma? "))
M1 = float(input("M1? "))
delta1 = np.deg2rad(float(input("deflection? ")))
est_wvangl = np.deg2rad(float(input("estimated angle? ")))

f_theta = lambda theta: ((gamma+1)/2 * M1**2/(M1**2 * (np.sin(theta))**2-1)-1) * np.tan(theta) - 1/np.tan(delta1)
df_theta = lambda theta: ((gamma+1)/2*M1**2/(M1**2*(np.sin(theta))**2-1)-1) * 1/(np.cos(theta))**2 - ((gamma+1)/2)*(M1**4 *np.sin(2*theta))/(M1**2*(np.sin(theta))**2-1)**2 * np.tan(theta)

def newton(f, df, guess, error):
    xi_1 = guess 
    iteration = 0
    while np.abs(f(xi_1)) > error:
        iteration += 1
        xi = xi_1 - f(xi_1)/df(xi_1)
        xi_1 = xi
        print("i = " +str(iteration), " theta = "+str(np.rad2deg(xi)))
        if iteration > 100:
            print("Not converging :(")
            break
    return iteration, xi, f(xi)

wave_angle1 = newton(f_theta, df_theta, est_wvangl, 0.001)
print("------------------------------------------------------------------")
print("iterations: "+ str(wave_angle1[0]), " wave angle: "+ str(np.rad2deg(wave_angle1[1])))


