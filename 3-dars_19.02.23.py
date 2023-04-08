#           Bo'lim 3.5: Pythone ro'yxat metodlari TAKRORLASH

# 01 -> append() --> ro'yxatga oxiridan element qo'shadi
# a = [1, 2, 3]
# a.append(4)
# print(a)

# 02 -> extend() --> bitta ro'yxatni boshqa ro'yxatga qo'shib qo'yadi
# b = [1, 2, 3, 4]
# b.extend([5, 6, 7])
# print(b)           

# 03 -> insert() --> belgilangan indexga element joylashtirsh
# k = ['salom', 'mening', 'ismim']
# k.insert(3, 'Sardor')
# print(k)

# 04 -> remove() --> ro'yxatdan belgilangan elementni o'chiradi
# l = [3, 5, 9, 10]
# l.remove(5)
# print(l)

# 05 -> pop() --> Berilgan indexdagi elementni o'chiradi va qaytaradi
# suz = ['salom', 'olma', 'nok', 'meva']
# suz.pop(0)
# print(suz)

# 06 -> clear() --> ro'yxatndagi barcha elemntlarni o'chiradi
# son = [11, 46, 85, 56]
# son.clear()
# print(son)

# 07 -> index() --> birinchi mos kelgan elementning indexini qaytaradi
# son = [1,2,3,4,5]
# print(son.index(5))     tushunmadim??????

# 08 -> count() --> Argument sifatida uzatilgan sonni qaytaradi
# harf = [1,2,3,4,5,6]
# c = harf.count(6)
# print(c)                tushunmadim??????

# 09 -> sort() --> Ro'yxatni o'sish tartibida saralaydi
# son = [3, 2, 5, 1, 4, 6]
# son.sort()
# print(son)

# 10 -> reverse() --> ro'yxatni teskari tartibda taxlaydi
# son = [1, 2, 3, 4, 5]
# son.reverse()
# print(son)

# 11 -> copy() --> Ro'yxatning mustaqil nusxasini saqlaydi
# harf = ['a', 's', 'd', 'k']
# harf.copy()
# print(harf)



#           Bo'lim 3.6: Ro'yxat generatori: Yangi ro'yxat yaratishning eng zo'r usuli


# sonlar = [1, 2, 3, 4, 5]
# for aylanish in sonlar:
#     print(aylanish)


# harflar = str(['s', 'a', 'd', 'k', 'l', 'v'])
# print('\n')
# for tartib in harflar:
#     print(tartib)
    
    
# mehmonlar = ['Sarvar', 'Kamol', 'Murod', 'Aziz', 'Shohrux', 'Asil']
# for mehmon in mehmonlar:
#     s = (f'Hurmatli {mehmon}, sizni ko\'rganimdan hursandman!')
#     print(s)
# print('\nHurmat bilan, Sardor!')


# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
# print(mehmonlar) 


# son = list(range(10))
# for son1 in son:
#     print(son1)
    
    
# belgi = list(range(50))
# for belgi1 in belgi:
#     print(belgi1)


# Sonning n-darajasi misoli!
# a = list(range(6))
# for a1 in a:
#     c = a1**3
#     print(c)
       
       
#    Kara kara jadvali
# kara = list(range(11))
# for kara1 in kara:
#     takror  = (f'{2} x {kara1}  = {kara1*2}')
#     print(takror)


# son = list(range(11))
# for kara1 in son:
#     n = (f"{5} x {kara1} = {kara1*5}")
#     print(n)
# print(son)


# savol = '5 ta eng yaqin do\'stingiz kim?'
# print(savol)
# sonlar = range(1,5)
# dustlarim = []
# for son in sonlar:
#     natija = dustlarim.append(input(f" {son} - do'stingizni kiriting: "))
# print(dustlarim)


# son = 2
# son1 = list([1,2,3])
# for ortirma in son1:
#     n = ortirma * 2
#     print(n)


# sonlar = []
# for x in range(11):
#     sonlar.append(x ** 2)
#     print(sonlar)


# for son in range(10):
#     n = son ** 3
#     print(n)
    
# ikalasi bir xil berilishi    
    
# pow2 = [2**x for x in range(10)]
# print(pow2)