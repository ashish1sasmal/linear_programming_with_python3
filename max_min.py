def check(Cj,Zj,e):
	re=True
	for fr in Cj:
		if fr>0:
			re=False
			break
	return re

n=int(input("Enter no. of equations = "))
v=int(input("Enter total no.of variables = "))
ch=input("Max or Min ?")
print("enter main equation = ")
e=[int(u) for u in input().split(' ')]
e=e+[0]*n
l=[]
b=[]

for i in range(n):
    print(f'enter coefficients of {i+1} equation \n with one space seperation = ')
    l1=[int(k) for k in input().split(' ')]
    b.append(l1.pop())
    l1+=[0]*n
    l1[v+i]=1
    l.append(l1)

cb=[0]*v

Zj=[0]*len(e)
Cj=[0]*len(e)
th=[999999999]*n
div=[0]*n
cb=[0]*n
for y in range(len(e)):
        Cj[y]=e[y]-Zj[y]
        
while check(Cj,Zj,e)!=True:
    
    key_index=Cj.index(max(Cj))

    for j in range(n):
        div[j]=l[j][key_index]
    for r in range(n):
        if div[r]>0:
            th[r]=b[r]/div[r]
        else:
            	th[r]=9999999

    key_row=th.index(min(th))
    key_elem=l[key_row][key_index]
    cb[key_row]=e[key_index]

    for t in range(len(l[0])):
        l[key_row][t]=l[key_row][t]/key_elem
        
    b[key_row]/=key_elem
    for ash in range(n):
        o=l[ash][key_index]
        g=b[key_row]
        if o!=0 and ash!=key_row :
            b[ash]=b[ash]-b[key_row]*o
            for te in range(len(l[ash])):
                l[ash][te]=l[ash][te]-l[key_row][te]*o
	            	  
    for vr in range(len(e)):
            op=0
            for te in range(n):
                op+=(cb[te]*l[te][vr])
            Zj[vr]=op
            
    for cy in range(len(e)):
        Cj[cy]=e[cy]-Zj[cy]
        


maximum=0
for nd in range(n):maximum+=(cb[nd]*b[nd])
    
if ch=='min':print('MINIMUM = = = ',-1*maximum)  
else:print("MAXIMUM = = = ",maximum)