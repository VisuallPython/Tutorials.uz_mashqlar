#           BO'LIM 3.4; Elementlarni almashtirish

#           Ro'yxatni biror elementini "Del" bn o'chirish;
# mening_ruyxatim = ['s', 'a', 'l', 'o', 'm']
# del mening_ruyxatim[2]
# print(mening_ruyxatim)    # ro'yxatdan 'l' o'chirildi

#       Ro'yxatni qaysidir qismini o'chirish
# mening_ruyxatim1 = ['h', 'e', 'l', 'l', 'o']
# del mening_ruyxatim1[1:3]
# print(mening_ruyxatim1)              # Natija: h, l, o


#       Ro'yxatni butunlay o'chrish
# mening_ruyxatim2 = ['M', 'e', 'n']
# del  mening_ruyxatim2
# print(mening_ruyxatim2)         #Ro'yxat o'chirilgani uchun Error berdi. 


#   Takrorlash: listga qiymat qo'shish
# son = [1, 2, 3, 4]
# son.append(5)
# print(son)

# son1 = [1, 2, 3, 4, 5]
# son1.extend([6, 7, 8])
# print(son1)

# son2 = [5, 4, 3, 2, 1]
# son2.insert(2, 0)
# print(son2)


#       """ Elementni o'chirish uchun 'REMOVE' va 'POP' metodlari qo'llanislishi"""
# Berilgan belgini o'chirish uchun remove ishlatiladi!
# suzlar = ['suv', 'yo\'lak', 'xalqa', 'maydon']
# suzlar.remove('yo\'lak') 
# print(suzlar)               # REMOVE demak faqat ko'rsatilgan belgini o'chiradi

# son = [9, 8, 7, 6]
# son.remove(8)
# print(son)

# sonlar = [1, 2, 3, 4]
# sonlar.remove(3)
# print(sonlar)

# suzlar1 = ['malika', 'tandir', 'android', 'windows']
# ajratilgan = suzlar1.pop(0)
# print(suzlar1)      #pop da index berib elementni sug'urib olish mumkin.
# print(ajratilgan)

# dasturlar = ['telegram', 'whatsapp', 'youtube', 'google']
# dasturlar.pop()
# print(dasturlar)       # pop ga index berilmasa oxirgi element o'chiriladi

# ilovalar = ['chrome', 'internet', 'snake']
# ilovalar.clear()
# print(ilovalar)         # Clear butunlay ro'yxatni tozalaydi.

# Elementni ham o'chirib ham boshqa qiymat berish usuli!
# kompyuterlar = ['Win', 'Mac', 'Linux']
# kompyuterlar[0:1] = ['android']
# # nomi[qaysidan:qaysigacha] = [o'chirilgan elementga almashadigan yangi element]
# print(kompyuterlar)

# maxsulot = ['qozon', 'kosa', 'choynak', 'piola']
# maxsulot[0:2] = ['vilka', 'pichoq']
# print(maxsulot)

# remove, pop va del metodlari farqlari

# # remove alohida sonni emas birinchi mos kelgan qiymatni o'chiradi
# a = [2, 3, 5, 3, 8]
# a.remove(2)
# print(a)

# # del ma'lum indeksdagi elementni o'chiradi
# b = [1, 2, 3, 4]
# del b[1]
# print(b)

# c = ['son', 'matn', 'lug\'at']
# del c[-1]
# print(c)

# #pop ma'lum indeksdagi qiymatni o'chirib so'ng qaytaradi
# d = [1, 2, 3, 4, 5]
# d.pop(2)
# print(d)
# print('suz ' * 10)
