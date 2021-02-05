value = int(input('ใส่จำนวนรอบที่ต้องการรับค่า'))
i = 1
a = 0
while(i <= value) :
    number = int(input('กรอกตัวเลข : '))
    a+=number
    i+=1
print('ผลรวมที่รับค่าเข้ามาทั้งหมด = %d'%a)