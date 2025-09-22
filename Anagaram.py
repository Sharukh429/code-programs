
#Anagram program in python
#take user input
String1 = "Listen"
String2 = "Silent"

String1 = sorted(String1,lower())
string2 = sorted(String2,lower())

print("String after sorting:",string1)
print("String after sorting:",string2)

# check if now strings matches
if string1 == string2:
    print('String are anagram')
else:
    print('String are not anagram')  
