def znajdz_max(S, n=None):

    if n is None:
        n = len(S)
    
    if n == 1:
        return S[0]
    
    max_podlista = znajdz_max(S, n - 1)
    
    return max_podlista if max_podlista > S[n - 1] else S[n - 1]

S = [7, 19, 33, 78]
print(znajdz_max(S))
#pamiec O(n) czas O(n)