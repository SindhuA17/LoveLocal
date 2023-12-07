#easy 1

def lastword(s):
    word = s.split()
    if not word:
        return 0
    return len(word[-1])


user_input = input("Enter a string: ")
response = lastword(user_input)
print("Length :", response)