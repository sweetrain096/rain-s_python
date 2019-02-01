dict1 = {"apple":"사과"}


dict1.update({"banana":"바나나"})
dict1["cherry"]="체리"

dict1["apple"] = "파인애플"
dict1.update({"banana":"바나나나나"})
dict2 = {"pineapple":"파인애플"}
dict1 = dict1 + dict2
print(dict1)