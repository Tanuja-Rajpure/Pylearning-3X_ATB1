a = int(input("Enter no num1:"))
b = int(input("Enter no num2:"))
c = a/b
print("Result div is:", c)

# WHat problem we might face
# 1- if num 1 = 10 , num2 = 0, c = 10/0- will give zero division error
# 2- If instead of number we use string/ special characters/ boolean, we will get - # Invalid indentation error

# Though its simple programme, we might get errors
# So twe need to handle the possible exceptions to improve customer experiance