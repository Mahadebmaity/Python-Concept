# question : print all vowel in the given string  like mahadeb 



# name = "mahadeb"
# lenth = len(name)
# print(name)
# i = 0
# for i in range(i,lenth):
#     if name[i] =="a" or "e" or "i" or "o" or "u":
#         print(name[i])
#     else:
#         print("")


# name = "mahadeb"
# lenth = len(name)
# i = 0
# if name in 'aeiou':
#         print(name)
# else:
#         print("")

# name="sourav"

# for i in name:
#     print(i)
#     if(i=='a' or 'e' or 'i' or 'o' or 'u'):
#         print(name)
#         print(i)
      



# name = "sourav"

# for i in name:
#     print(i)
#     if i in 'aeiou':
#         print(name)
#         print(i)


# Given string
name = "sourav"
print(list(name))
# Loop through each character
store = []
for i in name:
    if i in 'aeiouAEIOU':
        store.append(i)

print(store, len(store))
result=''.join(store)
print(result)
