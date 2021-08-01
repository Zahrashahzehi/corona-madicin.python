n = int(input()) # mobtalayan shekarestan
k = int(input()) # foti hay shekarestan
p = int(input()) # mobtalayan namakestan
q = int(input()) # foti hay namakestan 
if n-k > p-q :
    print("Shekarestan")
elif n-k < p-q:
    print("Namakestan")
else :
    print("Equal")        
