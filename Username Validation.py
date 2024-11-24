# Instruction : 

# Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.

# If the username is valid then your program should return the string true, otherwise return the string false.

def CodelandUsernameValidation(strParam):

  if len(strParam) >= 4 and len(strParam) <= 25 and strParam[0].isalpha() and strParam[-1] != "_" and [i for i in strParam if i.isalnum() or i=="_"]:
    return True
  else:
    return False
    

  return strParam

print(CodelandUsernameValidation(input("Enter input: ")))

