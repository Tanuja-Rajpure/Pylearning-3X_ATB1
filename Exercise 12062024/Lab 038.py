
# input = score
# output - print grade
# multiple cond - if elif else
# Stp 1- logic building
# Input =?
# Score- int
score=int(input("Enter the score\n : "))

#Step 2 write rough logic and convert to real
# score=>90 and score<=100 -> A
# score=>80 and score<=89 -> B
# score=>70 and score<=79 -> C
# score=>60 and score<=69 -> D
# score=>0 and score<=59 -> FAIL

if score >= 90 and score <= 100:
    print("Grade is A")
if score >= 80 and score <= 89:
    print("Grade is B")
if score >= 70 and score <= 79:
    print("Grade is C")
if score >= 60 and score <= 69:
    print("Grade is D")
if score >= 0 and score <= 59:
    print("Grade is FAIL")
else :
    print("Invalid score")