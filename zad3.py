def znajdz_max_min(S):
    if len(S) == 1:
        return S[0], S[0]  
    
    min_reszta, max_reszta = znajdz_max_min(S[1:])
    
    nowe_min = S[0] if S[0] < min_reszta else min_reszta
    nowe_max = S[0] if S[0] > max_reszta else max_reszta
    
    return nowe_min, nowe_max
S=[2, 4, 10]
print(znajdz_max_min(S))
#Pamiec O(n^2)