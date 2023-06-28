import pandas as p
from apyori import apriori
d=p.read_csv("C:\\Users\\premb\\Downloads\\grocer.csv",sep='delimeter',engine='python',header=None)
a=[j.to_list() for (i,j) in d.iterrows()]
e=[]
m=[]
for i in a:
    for j in i:
        j=j.split(",")
        m.append(j)
        for k in j:
            e.append((k))
q={}
for i in e:
    if i not in q:
        q[i]=1
    else:
        q[i]+=1
z= sorted(q.items(), key=lambda x: x[1], reverse=True)
c=0
bb={}
for i in z:
    bb[i[0]]=i[1]
    c+=1
print(bb)
dict={"item_name":[i for i,j in bb.items()],"item_count":[j for i,j in bb.items()]}
dd=p.DataFrame(dict)
print(type(e))
association_rules=(apriori(m,min_support=0.004,min_confidence=0.3,min_lift=1,min_length=1.2))
association_results = list(association_rules)
print("There are {} Relation derived.".format(len(association_results)))
for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    try:
        print("Rule: " + items[0] + " -> " + items[1])
    except:
        ajay=1
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
dd['item_percent']=dd["item_count"]/len(e)
print(dd)
r=round(dd[:20]['item_percent'].sum()*100,2)
print(r)
