def palindrom(s):
    
    s_clean = ''.join(c.lower() for c in s if c.isalnum())

    if len(s_clean) <= 1:
        return True
    
    if s_clean[0] != s_clean[-1]:
        return False
        
    return palindrom(s_clean[1:-1])

print(palindrom("dom"))
print(palindrom("tot"))
print(palindrom("a"))
print(palindrom("Kamil slimAk"))
print(palindrom("ładny dom"))
print(palindrom(" "))

#Czas O(n), pamiec O(n^2)