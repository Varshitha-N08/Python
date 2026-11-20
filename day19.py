# school={"ravi":{"maths":90,"cs":95},"sita":{"maths":80,"cs":99}}
# print(school["sita"]["cs"])
# school["ravi"]["maths"]=92
# print(school["ravi"])


#  print([x for x in [10,20]])

# l=[11,12]
# for x in l:
#     if x%2==0:
#         print("even",x)


print([f"{x} even" for x in [11,12] if x%2==0])