s = "z"
t = "abcde"
count=0
j=0
for i in range(len(s)):
    if s[i]==t[j]:
        j+=1


print(len(t)-j)