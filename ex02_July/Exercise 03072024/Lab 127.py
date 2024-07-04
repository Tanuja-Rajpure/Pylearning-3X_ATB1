# Erros - are something which are difficult to recover
# Def- Error- Are more severe issue that typically pevent programme from running
# Syntax , Indentation error

#import math

#math.exp(1000)  # OverflowError: math range error

# Exceptions - They will be return as error only but it is possible to handle them
# Def- Are events that occur during execution
# programme recover is possible
# Overflow error under math errror
try:
    import math

    math.exp(1000)

except Exception as e:
    print(e)
