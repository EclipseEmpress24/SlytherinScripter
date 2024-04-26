#Getting input from User
str1 = input("Enter String: ")

#Leaving the string empty in the initial
str2 = ""

for i in str1:
  str2 = i + str2

print(str2)

# ----------------------------------------------------------------

#Concept:
#  Let's take the example string "ABC"
#  A   B   C
#  0   1   2  (Array position)

# i in  str1 => should do "i + str2" in str2
# str2 is blank in beginning

#S1: i=0 position
#  str2 = 0 [A] + str2 [""] == "A"

#S2: i=1 position
#  str2 = 1 [B] + str2 ["A"] == "BA"

#S3 i=2 position
#  str2 = 2 [C] + str2 ["BA"] == "CBA"

#iteration ends and printing the reversed string
