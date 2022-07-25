The primary purpose of the toolbox is to provide myself with some practice using git. These files are all calculators related to common aerospace problems, including, most prominently, calculations of the values given in NACA 1135. The files include:

1. arearatio_mach.py -> a calculation to find the Mach number of a given area ratio.
2. dwnstrm_mach_incrementally.py -> a program to calculate the downstream Mach number resulting from a series of deflections of equal value. For example, a total deflection of 30 degrees broken into 5 equal 6 degree deflections.
M2_calc.py -> calculates the downstream Mach number after a normal or oblique shock wave.
specific_heats.py -> a simple program to output the specific heats c_v and c_p of a gas. Inputs are specific gas constant R and the ratio of specific heats, gamma.
stag_pr.py -> calculates the stagnation properties after an oblique or normal shock.
waveangle.py -> utilizes Newton's method to calculate the wave angle.

Coming soon:
1. standard atmosphere calculator. Input your altitude, specify units, and output pressure, temperature, and density.
