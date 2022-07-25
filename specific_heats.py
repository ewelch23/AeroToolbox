## E. Welch
## inputs: specific gas constant, gamma
## output specific heats (cp and cv)

R = float(input("Specific gas constant? "))
gamma = float(input("ratio specific heats? "))

cv = R/(gamma-1)
cp = gamma* cv

print("cv = "+str(cv))
print("cp = "+str(cp))