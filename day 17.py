# # s={1,2,3}
# # s.discard(9)
# # print(s)
  
  
# # s={1,2,3}
# # s.remove(9)

# s={1,2}
# s.add(3)
# s.add(2)
# s.update([4,5,5])
# print(s) 

A={1,2}
B={1,2,3,4}
print(A.issubset(B))
print(B.issuperset(A)) 
print(A.isdisjoint({7,8}))
print(B.isdisjoint({4,9}))   
