s = "ababcbacadefegdehijhklij"

start=0
end=0
enum_s={c:i for i,c in enumerate(s)}
res=[]
for count,value in enumerate(s):
    print(count,value)
    end=max(end,enum_s[value])
    
    if count==end:
        res.append(end-start+1)
        start=count+1

print(res)