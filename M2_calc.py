## E. Welch 2022
## inputs: normal/oblique wave, gamma, M1
## if oblique, inputs also include: wave angle, deflection angle (in degrees)
## outputs: M2, M2_n
## calculate M2 for shock wave.
import numpy as np

criteria = input("Normal or oblique wave? ")

if criteria.lower() == 'normal':
    gamma = float(input("gamma? "))
    M1_n = float(input("M1? "))
    M2_n = np.sqrt(( M1_n**2+2/(gamma-1) ) / ( 2*gamma/(gamma-1)*M1_n**2 -1))
    print("---------------------------------------------------")
    print("M2 = " +str(M2_n))

elif criteria.lower() == "oblique":
    gamma = float(input("gamma? "))
    M1 = float(input("M1? "))
    theta = np.deg2rad(float(input("wave angle? ")))
    delta = np.deg2rad(float(input("deflection angle? ")))

    M1_n = M1*np.sin(theta)
    M2_n = np.sqrt(( M1_n**2+2/(gamma-1) ) / ( 2*gamma/(gamma-1)*M1_n**2 -1))
    M2_solved = M2_n / np.sin(theta-delta)
    print("M2_n = " + str(M2_n))
    print("------------------------------------------")
    print("M2 = " +str(M2_solved))

else:
    print("I can't understand. Check spelling?")