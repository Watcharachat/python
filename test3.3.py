list=[]
i=1
s=0
print('ป้อนชื่ออารหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม')
while(i<999):
    อาหาร=str(input('อาหารโปรดอันดับที่ '+ str(i)+' คือ\t'))
    if อาหาร=='exit':
        break
    list.append(อาหาร)
    i+=1
print('อาหารสุดโปรดของคุณมีดังนี้',end='  ')
for i in list:
    s=s+1
    print('%s.'%s,i,end='\t')



