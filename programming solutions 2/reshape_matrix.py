mat = [[1,2],[3,4]]
r = 4
c = 1
tmp=[mat[i][j] for i in range(0,len(mat)) for j in range(0,len(mat[0]))]
new=[]
print(tmp)

step=len(tmp)/r

print(step)


if r*c!=len(tmp):
    print(mat)
else:
    start=0
    end=step
    for row in range(0,r):
        print(f'start: {start} end:{end}')
        new.append([tmp[i] for i in range(int(start),int(end))])
        start=end
        end=end+step
    print(new)

"""x=0
for row in range(0,r):
    for col in range(0,c):
        new[row].append(tmp[x])
        x+=1
print(new)"""