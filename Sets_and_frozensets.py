# Sets --> Mutable,Nop duplicates, Unordered

lst = ['a','a','b','c','d','e']

s = set(lst)
s.update(['r','s']) # Update method is used to update the element

s.remove('a') # used to remove perticular elements

# Frozenset

s_1 = {50,20,50,90,80}
fs = frozenset(s_1)


