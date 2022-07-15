import sys

n=int(input("Enter n: "))
listi=[]
dicti={}

if n >= 0 and n <= 10**5:
    for i in range(n):
        words=input(f"Enter word {i+1}: ")
        if words.islower():
            listi.append(words)
            if words in dicti:
                dicti[words] += 1
            else:
                dicti[words] = 1
        else:
            sys.exit("Please enter lowercase words!")
else:
    sys.exit("Please enter the valid number!")
    
print(len(set(listi)))
for word, times in dicti.items():
    print (times, end=" ")