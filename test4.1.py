import os
grocery=[]
amount=[0,0,0,0,0]
price=[15,25,75,5,10]
print('\tโปรแกรมร้านค้าออนไลน์\n','-'*36)
def menu():
    global choice
    print('1. แสดงรายการสินค้า\n2. หยิบสินค้าเข้าตะกร้า\n3. แสดงรายจำนวนและราคาที่หยิบ\n4. หยิบสินค้าออกจากตะกร้า\n5. ปิดโปรแกรม\n')
    choice = input('กรุณาเลือกทำรายการ : ')

def one():
    print('\tรายการสินค้า\n','-'*36,'\n','\t1. ยาดม ราคา 15 บาท\n\t2. ยาสระผม ราคา 25 บาท\n\t3. สบู่ ราคา 75 บาท\n\t4. ยาสีฟัน ราคา 5 บาท\n\t5. แปรงสีฟัน ราคา 10 บาท')

def two():
    animal = 0
    while(True):
        print('\t1. ยาดม\n\t2. ยาสระผม\n\t3. สบู่\n\t4. ยาสีฟัน\n\t5. แปรงสีฟัน\n\t6. ออกจากฟังก์ชัน')
        animal = input('เลือกหยิบสินค้าหมายเลข : ')
        try:
            if int(animal)==1 or animal=='1':
                grocery.append('ยาดม')
            elif int(animal)==2 or animal=='2':
                grocery.append('ยาสระผม')
            elif int(animal)==3 or animal=='3':
                grocery.append('สบู่')
            elif int(animal)==4 or animal=='4':
                grocery.append('ยาสีฟัน')
            elif int(animal)==5 or animal=='5':
                grocery.append('แปรงสีฟัน')
            elif int(animal)==6 or animal=='6':
                break
            else:
                print('กรุณากรอกหมายเลขให้ถูกต้อง')
        except:
            print('กรุณากรอกหมายเลขให้ถูกต้อง')
            pass
def three():
    for i in grocery:
        if i == 'ยาดม':
            amount[0]+=1
        elif i == 'ยาสระผม':
            amount[1]+=1
        elif i == 'สบู่':
            amount[2]+=1
        elif i == 'ยาสีฟัน':
            amount[3]+=1
        elif i == 'แปรงสีฟัน':
            amount[4]+=1
    amounttt=amount[0]+amount[1]+amount[2]+amount[3]+amount[4]
    pricett=amount[0]*15+amount[1]*25+amount[2]*75+amount[3]*5+amount[4]*10
    print('')
    print('{0:_<10}{1}{0:_<10}'.format('','สินค้าที่คุณหยิบไปมีดังนี้'))
    print('{0:.<6}{1}{0:.<6}{2}{0:.<6}{3}{0:.<7}'.format('','สินค้า','จำนวน','ราคา'))
    print('{0:_<38}'.format(''))
    if amount[0]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:<9}{3}{0:.<10}'.format('','ยาดม',str(amount[0]),str(amount[0]*15)))
    if amount[1]!=0:
        print('{0:.<4}{1}{0:.<6}{2}{0:<9}{3}{0:.<10}'.format('','ยาสระผม',str(amount[1]),str(amount[1]*25)))
    if amount[2]!=0:
        print('{0:.<6}{1}{0:.<6}{2}{0:<9}{3}{0:.<10}'.format('','สบู่',str(amount[2]),str(amount[2]*75)))
    if amount[3]!=0:
        print('{0:.<6}{1}{0:.<8}{2}{0:<9}{3}{0:.<10}'.format('','ยาสีฟัน',str(amount[3]),str(amount[3]*5)))
    if amount[4]!=0:
        print('{0:.<6}{1}{0:.<3}{2}{0:<9}{3}{0:.<10}'.format('','แปรงสีฟัน',str(amount[4]),str(amount[4]*10)))
    print('{0:_<38}'.format(''))
    print('{0:.<6}{1}{0:.<6}{2}{0:<9}{3}{0:.<10}'.format('','รวม',str(amounttt),str(pricett)))
    print('')

def four():
    n=0
    while(True):
        print('\tสินค้าในตะกร้ามีดังนี้')
        for i in grocery:
            n+=1
            print('\t'+str(n)+'.'+i)
        n=0
        animal2=int(input('เลือกลำดับสินค้าาที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก:'))
        try:
            if animal2<=len(grocery) and animal2!=-1:
                grocery.pop(animal2-1)
            elif animal2==0 and animal2<=len(grocery) and animal2!=-1:
                grocery.pop(animal2)
            elif animal2==-1:
                break
        except:
            print('กรุณากรอกลำดับสินค้าให้ถูกต้อง')
            pass

def clear():
    os.system('cls')

while True:
    menu()
    if choice == '1':
        clear()
        one()
    elif choice == '2':
        clear()
        two()
    elif choice == '3':
        clear()
        three()
    elif choice == '4':
        clear()
        four()
    else:
        yesno=input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n : ')
        if yesno == 'y':
            break
        elif yesno == 'n':
            continue


