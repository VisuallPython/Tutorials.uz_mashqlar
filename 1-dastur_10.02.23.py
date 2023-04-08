# print("Hello World!")


#    Taqqoslash operatori 
# x=10 
# y=12
# print("x>y is", x>y)

# print ("x<y is", x<y)

# print ("x==y is", x==y)

# print ("x!=y is", x!=y)

# print ("x<=y is", x<=y)

# print ("x>=y is", x>=y)


#       Arifmetik operatorlar 
# x = 3 
# y = 6 

# print ("x**y =", x**y) 

# print ("x/y =", x/y)

# print ("x//y =", x//y)   #Sonning butun qismi chiqadi 

# print("x%y =", x%y)       #Sonning qoldig'i chiqadi


#       Bir xillik operatorlar
# x1 = 5
# y1 = 5
# x2 = 'Hello'
# y2 = 'Hello'
# x3 = [1,2,3]
# y3 = [1,2,3]

# print(x1 is not y1)    # ikkalasi bir xil ma'no beradi
# print(x1 != y1)

# print(x2 is y2)         #ikkalsi bir xil
# print(x2 == y2)   

# print(x3 is y3)        # x3 va y3 bir xil ammo ular xotirada turli xil joy olgani uchun False qaytadi
# print(x3 == y3)


#           Murakkab sonlar

# from math import *
# print(3+2j) 

# print(1j * 1j)

# z = (3 + 5j)     # z = (a + bj)
# print(z.real)
# print(z.imag)

# import cmath 
# print(cmath.sqrt(-1))
# b = cmath.cos(30)
# print(b)


#           Name yozish va INPUT

# name = 'Sardor'
# sharif = 'Abdug\'affor o\'g\'li'        # \'  bu o' va g' harflarini yo'qotmadsdan saqlaydi
# print('Mening ismim ', name)
# print('Mening familiyam Temirov!')
# print("Hozirda men shu satrni \n pastga '\\n' bilan tushirdim")
# print("Men " f"{name} {sharif}")

# ism = input("Ismingiz ->")
# print('Uning ismi ', ism)

# son = int(input("Sonni yozing ->"))
# print("Bu son = ", son)


#           Ro'yxatlar (LIST)

# x = [1, 2, 3, 6]
# print('Ro\'yxatlar -> ', x)

# #           Pythone da massivlaR 

# ruyxat = [1, 'besh', 'olma', [5, 9, 0]]   #ichma-ich joylashgan ro'yxatni alohida sanamaydi
# print(ruyxat)
# print(len(ruyxat))      # ro'yxatda nechta o'zgaruvchi qatnashganini bildiradi!


#           Ro'yxat indekslari
# mevalar = ['olma', 'anor', 'anjir', 'gilos']
# # #Indekslari  0        1       2         3
# print(mevalar[1])
# print(mevalar[3], '\n')

# print(mevalar[-1])
# print(mevalar[-2])

# print(mevalar[0:-1])    #birnchidan to oxiridazn bitta oldingi o'zgaruvchiga chiqararkan


#           Ro'yxatni o'zgartrish
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8]
# print("1-kurinish ", sonlar, "\n")

# sonlar[2] = 9
# sonlar[5] = 11
# print(sonlar)  

# mashina = ['nexia', 'cobalt', 'gentra', 'malibu']
# mashina.append('captiva')
# print(mashina)
# mashina.clear()      #o'zgaruvchini qiymatini o'chirib yuboradi.
# print(mashina)


# append() -> metodi. 1 ta qiymat qo'shadi
# shahar = ["Nyu York", "fransiya", "Germaniya"]
# shahar.append("Italiya")
# print(shahar)

# extend() -> metodi. Bir nechta qiymat kiritish mumkin. 
# kuchalar = ["Beruniy", "Alisher Navoiy", "Hamza"]
# kuchalar.extend(["Nurafshon", "Nurota", "Amir Temur"])         # extend([]) -> ichida albatda [] bo'lishi kk
# print(kuchalar)

# sonlar = [2, 4, 6]
# sonlar.extend([8, 10])
# print(sonlar)

#   + va * orqali qiymat qo'shish va uni takrorlash
# sonlar = [1, 3, 4]
# print(sonlar + [6, 7, 9])

# suz = "mashina"
# print([suz] * 3)      #suz nomli qiymati []  ichida bo'lishi kerak

# son = 5
# son1 = ([son] * 5)
# print(son1)


#   insert() -> Ro'yxatni ixtiyoriy joyiga qiymat qo'shish un
# raqamlar = [10, 20, 31, 51]
# raqamlar.insert(1, 25)      #keyingi qiymatni o'zgaruvchi bn belgilash shart emas
# print(raqamlar)

# raqamlar1 = [3.2, 6.5, 11.8]
# raqamlar1.insert(-1, 7.3)
# print(raqamlar1)

# raqamlar2 = [56, 21, 91, 36]
# raqamlar2.insert(2, 44)
# print(raqamlar2)

# To'plamning bo'sh qismiga bir nechta qiymat kiritib qo'yish
# mashina = ["Mersedes", "Malibu", "Tesla"]
# mashina[2:2] = ['Matiz', 'Tiko', 'Damas']
# print(mashina)