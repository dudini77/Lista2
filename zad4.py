def mnozenie(m, n):

    if n == 0:
        return 0
    
    return m + mnozenie(m, n-1)

print(mnozenie(5, 6))
print(mnozenie(0, 2))
print(mnozenie(10, 0))
print(mnozenie(7, 8))
#pamieciowa, czasowa O(n).