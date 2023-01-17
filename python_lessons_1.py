#03 tasks
print('"Nexia", "Tico",' "'Damas' ko'rganlar qilar havas")

  #5 ning 4-darajasini toping
print("5 ning 4-darajasi:", 5**4)

  #22 ni 4 ga bo'lganda qancha qoldiq qoladi?
print("22 ni 4 ga bo'lganda", 22%4,"qoldiq qoladi")

  #Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
print("Tomonlari 125 ga teng kvadratning yuzi:",125**2," va perimetri:", 125*4)

  #Diametri 12 ga teng bo'lgan doiraning yuzini toping (π=3.14 deb oling)
print("Diametri 12 ga teng bo'lgan doiraning yuzi: ", 3.14*((12/2)**2))

  #Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)
print("Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi:", (6**2+7**2)**(1/2))
print("\n")



#04 tasks

  #"Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring

matn = "Hello World!"
print(matn)

  #xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.
xabar = "E'zoza dushanba kuni uyda bo'lmaydi -_- Iltimos keyinroq qo'ng'iroq qiling!"
print(xabar)
xabar = "Aziza ham uyda bo'lmaydi :)\n"
print(xabar, "\n")

  #class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va konsolga chiqaring (siz kutgan natija chiqdimi?):

  #class syntaxerror



#05 tasks

  #Quyidagi o'zgaruvchilarni yarating:
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
  #Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring: Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati 

print(kocha+" ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati ")

  # Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.

#kocha = input("Ko'cha: ") mahalla = input("Mahalla: ") tuman = input("Tuman: ") viloyat = input("Viloyat: ")

print(kocha+" ko'chasi,\n" + mahalla + " mahallasi,\n" + tuman + " tumani,\n" + viloyat + " viloyati")
  #Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing

  #Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
yangi_manzil = f"{kocha.capitalize()}, {mahalla.upper()}, {tuman.title()}, {viloyat.title()}"
print(yangi_manzil, "\n")



#06 tasks

  #Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
a = int(input(">>> "))

print(f"{a} sonining kvadrati {a**2}ga teng\n")
print(f"{a} sonining kubi {a**3}ga teng\n")

  #Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
print("Yoshingiz nechida?")
yosh = int(input(">>> "))
print(f"Siz {2022-yosh}-yilda tug'ilgansiz\n")

  #Foydalanuvchidan ikki son kiritishini so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))

print(f"{son1} + {son2} = {son1+son2}")
print(f"{son1} - {son2} = {son1-son2}")
print(f"{son1} * {son2} = {son1*son2}")
print(f"{son1} / {son2} = {son1/son2}\n")



#07 tasks

    #ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting

ismlar = ["Robiya", "Dildora", "Sevinch"]

  #Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:

print(f"""Salom {ismlar[0]} avtobus hali kelmadimi?
{ismlar[1]}aa tezroq ko'rishaylik, masalan Azon cafeda, soat 11:00 da. Vaqting bormi?
Kartezni tekshirib ko'ring-chi Payme'dan, {ismlar[-1]}, balki stipendiya tushgandir :)""")

  #sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).

sonlar = [28, -2004, 123, 45.06]

  #Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.

print("Dastlab:", sonlar[:])
sonlar[0] = sonlar[0]+5
sonlar[1] = sonlar[1] - 18
sonlar[-1] = 36/4
sonlar[-2] = sonlar[-1]*sonlar[-4]
print("So'ngra:", sonlar[:])

  #t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.

t_shaxslar = ["Abdulla Qodiriy", "O'tkir Hoshimov", "Tohir Malik"]
z_shaxslar = ["Akrom Malik", "Baxtiyor Abdug'ofur", "Javlon Jovliyev"]

  #Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:

print(f"Men tarixiy shaxslardan {t_shaxslar.pop(1)} bilan, zamonaviy shaxslardan esa {z_shaxslar.pop(-1)} bilan suhbat qilishni xohlardim.")

  #friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.

friends = []
friends.append("Zebo")
friends.append("Dildora")
friends.append("Robiya")
friends.append("Nargiza")
friends.append("Munisa")
friends.insert(0, "Xadicha")

print("Kechki bazmga" + friends[0], friends[1], friends[2], friends[3], friends[4], friends[5] + "larni taklif qildim.")

  #Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.

friends.remove("Dildora")
friends.remove("Munisa")

print("Ammo faqat",friends[:],"lar kela olar ekan.")

  #Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

friends.insert(0, "Muslima")
friends.insert(-1, "Sevinch")
friends.insert(-3, "Sojida")

print(f"Bazmga {friends[0]}, {friends[-3]} va {friends[-1]} ham kelib qolishi mumkin")

  #Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

yangi_mehmonlar = []

yangi_mehmon = friends.pop(0)
yangi_mehmonlar.append(yangi_mehmon)

yangi_mehmonlar.append(friends.pop(-1))
print(yangi_mehmonlar[:])



#08 tasks

  #O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring

davlatlar = ["Germaniya", "Turkiya", "Kanada", "BAA"]
print("\nDavlatlar: ", davlatlar[:])

  #Ro'yxatning uzunligini konsolga chiqaring

print("Royxat uzunligi: ", len(davlatlar))

  #sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring

print("Tartib bilan :",sorted(davlatlar))

  #sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring

print("\t\t",sorted(davlatlar, reverse=True))

  #Asl ro'yxatni qaytadan konsolga chiqaring

print(davlatlar)

  #reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

  #sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.

davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

  #120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing

juft_sonlar = list(range(120, 1200, 2))
#print("Juft sonlar: ", juft_sonlar)

  #Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring

print("Juft sonlar yig'indisi: ", sum(juft_sonlar))

  #Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring

print("max-min =", max(juft_sonlar)-min(juft_sonlar))

  #Ro'yxatdagi elementlar sonini hisoblang

print("Elementlar soni: ", len(juft_sonlar))

  #Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring

print(juft_sonlar[:20])
print(juft_sonlar[220:240])
print(juft_sonlar[520:])

  #taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting

taomlar = ["osh", "somsa", "manti", "xonim", "kabob"]

  #nonushta degan yangi ro'yxatga taomlardan nusxa oling

nonushta = taomlar[:]

  #Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing

del nonushta[2:]
nonushta.remove("osh")

nonushta.append("tuxum")
nonushta.append("bo'tqa")

  #Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring

print("Taomlar:", taomlar)
print("Nonushta:", nonushta)

  #Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.

nonushta = tuple(nonushta)



#09 tasks

  #Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing

ismlar = ["Aziza", "Laziza", "E'zoza", "Fariza", "Shaxnoza"]
marta = 0
for ism in ismlar:
  print(f"{ism}, xush kelibsan!")
  marta+=1
  #Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)

print("\nKod", marta, "takrorlandi\n")

  #10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.

toq_sonlar = list(range(11, 100, 2))
for son in toq_sonlar:
  print(f"{son} ning kubi {son**3}")

  #Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.

kinolar = []
print("5 ta eng sevimli kinoyingizni kiriting:")
for k in range(5):
  kinolar.append(input())
print(kinolar)

  #Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

odamlar = []
nechta = int(input("Nechta odam bilan suhbatlashdingiz? "))

for n in range(nechta):
  odamlar.append(input(f"{n+1}-shaxsning ismi nima? "))

print(odamlar)



#10 tasks

  #Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car == 'gm':
    print(car.upper())
  else:
    print(car.capitalize())

  #Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
print("\n")
for car in cars:
  if car != 'gm':
    print(car.capitalize())
  else:
    print(car.upper())

  #Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.

user_ism = input("Ismingizni kiriting: ")
if user_ism.lower() == 'admin':
  print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?\n")
else:
  print(f"Xush kelibsiz, {user_ism}!\n")

  #Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.

a = float(input("1-son: "))
b = float(input("2-son: "))
if a==b: print(f"Sonlar teng: {a} = {b}")

  #Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.

user_son = float(input("Son kiriting: "))

print("Manfiy son\n") if user_son < 0 else print("Musbat son\n")

  #Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.

son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')



#11 tasks

  #Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

user_son2 = int(input("Juft son kiriting: "))
print("Rahmat!") if user_son2%2 == 0 else print("Bu son juft emas..")

  #Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

    #Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
    #Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
    #Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

user_age = int(input("Yoshingizni kiriting: "))

if user_age < 4 or 60 < user_age:
  print("Siz uchun bepul. Marhamat, muzeyga kiravering!")
elif user_age < 18:
  print("Chipta narxi Siz uchun 10000 so'm.")
else:
  print("20000 to'lov qilishingiz kerak.")

  #Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring

son1 = float(input("1-son: "))
son2 = float(input("2-son: "))

if son1 == son2:
  print(f"{son1}={son2}")
elif son1 < son2:
  print(f"{son1}<{son2}")
else:
  print(f"{son1}>{son2}")

  #mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

mahsulotlar = ["tuz", "murch", "bulg'ori", "un", "shakar", "yog'", "saryog'", "margarin", "buxonka non", "patir"]

savat = []

for n in range(5):
  savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

for mahsulot in savat:
  if mahsulot in mahsulotlar:
    print(f"{mahsulot} do'konimizda bor")
  else:
    print(f"{mahsulot} do'konimizda yo'q")

  #Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

  #foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

foydalanuvchilar = ["aziza", "ezoza", "fariizaa", "dilnoza", "shaxnoza"]
new_login = input("Login tanlang: ")
print("Login band, yangisini tanlang!") if new_login in foydalanuvchilar else print("Xush kelibsiz, foydalanuvchi!")

  #Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

y = int(input("Biror butun son kiriting: "))
print(f"{y} soni quyidagilarga qoldiqsiz bo'linadi:")
for n in range(2,10):
  if not y % n:
    print(n,end=" ")



#14 tasks

  #otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

onam = {
  "ismi": "Mukambar",
  "tugilgan_yili": 1983,
  "tugilgan_shahri": "Toshkent",
  "kasbi": "tarbiyachi"
}

print(f"Onamning ismlari {onam['ismi']}, {onam['tugilgan_yili']}-yilda {onam['tugilgan_shahri']}da tavallud topganlar.")

  #Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

fav_food_fam = {
  "Murodjon": "qovurilgan kartoshka",
  "Mukambar": "mastava",
  "Mahmudjon": "goroh sho'rva",
  "Muhammadjon": "qovurma lag'mon",
  "E'zoza": "osh"
}

for qiymat in fav_food_fam.keys():
  print(f"{qiymat}ning sevimli taomi {fav_food_fam[qiymat]}")

  #Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

py_dict = {
  "int": "butun son",
  "float": "o'nli kasr",
  "if, elif, else": "tarmoqlanuvchi operatorlar",
  "for, while": "loops",
  "list": "ro'yxat",
  "tuple": "qat'iy ro'yxat",
  "dict": "lug'at"
}

  #Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

search = input("Qaysi so'z ma'nosiga qiziqyapsiz? ")

print(py_dict[search]) if search in py_dict else print("Bunday so'z mavjud emas")



#15 tasks

  #Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.

py_dct = {
  "int": "butun son",
  "float": "o'nli kasr",
  "if, elif, else": "tarmoqlanuvchi operatorlar",
  "for, while": "loops",
  "list": "ro'yxat",
  "tuple": "qat'iy ro'yxat",
  "dict": "lug'at",
  "numpy": "kutubxona",
  "pandas": "kutubxona",
  "python": "dasturlash tili"
}

for key, value in sorted(py_dct.items()):
  print(f"{key} --> {value}")

  #Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

davlatlar = {
  "O'zbekiston": "Toshkent",
  "Turkiya": "Anqara",
  "Fransiya": "Parij",
  "Rossiya": "Moskva",
  "Braziliya": "Brazilia"
}

for davlat in sorted(davlatlar):
  print(davlat)

for poytaxt in sorted(davlatlar.values()):
  print(poytaxt)

  #Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

user_country = input("\nIstalgan davlatni kiriting: ")
capital = davlatlar.get(user_country)

if not capital==None:
  print(f"{user_country}ning poytaxti {davlatlar[user_country]}\n")
else:
  print("Bizda bunday ma'lumot yo'q")

  #Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

restoran_menyusi = {
  "Mujskoy kapriz salati": 29000,
  "Kiyev kotleti": 30000,
  "Iskandar kabob": 56000,
  "Chechevitsa sho'rva": 30000,
  "Adana kabob": 68000,
  "Choyxona palov": 40000,
  "Achiqqina mastava": 40000,
  "Manti": 35000,
  "Xonim": 35000,
  "Norin": 45000
}
buyurtmalar = []
for n in range(3):
  buyurtmalar.append(input(f"{n+1}-buyurtma uchun nima istaysiz?"))

for buyurtma in buyurtmalar:
  if buyurtma in restoran_menyusi:
    print(f"{buyurtma}ning narxi: {restoran_menyusi[buyurtma]}")
  else:
    print(f"Kechirasiz, bizda {buyurtma} mavjud emas.")

  #Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

avloniy = {
  "ism": "Abdulla Avloniy",
  "t_yili": 1878,
  "t_kuni": "12-iyul",
  "t_shahri": "Toshkent",
  "v_yili": 1934,
  "asarlar": ["Turkiy guliston yoxud axloq", "Maktab gulistoni", "Toshkent tongi"]
  }
  
qodiriy = {
  "ism": "Abdulla Qodiriy",
  "t_yili": 1894,
  "t_kuni": "12-aprel",
  "t_shahri": "Toshkent",
  "v_yili": 1938,
  'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
  }

sharafiddinov = {
  "ism": "Ozod Sharafiddinov",
  "t_yili": 1929,
  "t_kuni": "1-mart",
  "t_shahri": "Qo'qon",
  "v_yili": 2005,
  'asarlar':["Zamon. Qalb. Poeziya", "Adabiy etyudlar", "Yalovbardorlar"]
  }
  
behbudiy = {
  "ism": "Mahmudxo'ja Behbudiy",
  "t_yili": 1875,
  "t_kuni": "20-yanvar",
  "t_shahri": "Samarqand viloyati",
  "v_yili": 1919,
  "asarlar": ["Savod chiqarish kitobi", "Padarkush", "Aholi geografiyasiga kirish"]
  }

shaxslar = [avloniy, qodiriy, sharafiddinov, behbudiy]

for shaxs in shaxslar:
    ism = shaxs['ism']
    tyil = shaxs['t_yili']
    tkun = shaxs['t_kuni']
    tjoy = shaxs['t_shahri']
    vyil = shaxs["v_yili"]
    print(f"{ism} {tyil}-yili {tkun}da {tjoy}da tavallud topgan. "
          f"{vyil-tyil} yil umr ko'rgan.")

  #Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

for shaxs in shaxslar:
    ism = shaxs['ism']
    asarlar = shaxs['asarlar']
    print(f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar)

  #Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'atga saqlang. Natijani konsolga chiqaring.

questionnaire = {
  "Oyijonim": ["Nomus", "Qodirxon", "To'qlikka sho'xlik 1"],
  "Mahmudjon": ["Merlin", "Izquvar", "Interstellar"],
  "Muhammadjon": ["Wednesday", "Under the domb", "Harry Potter"]
  }

for ism, kinolar in questionnaire.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)

  #Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlats = {
  "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
}

for davlat, info in davlats.items():
    if davlat.lower()=='aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")

  #Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

davlat = input('Davlat nomini kiriting: ').lower()
if davlat in davlats:
    info = davlats[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")



#17 tasks

  #Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating

savol = '\nYoqtirgan kitoblaringizni kiriting:\n'
savol += '(dasturni to\'xtatish uchun \'stop\' so\'zini yozing)\t'

while True:
  qiymat = input(savol)
  if qiymat == 'stop':
    break

  #Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
    #Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)

savol2 = "\nYoshingiz nechida?  "
savol2 += "\n(dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing)\n"

while True:
  qiymat = input(savol2)
  if qiymat == 'exit' or qiymat == 'quit':
    break
  yosh = int(qiymat)
    
  if yosh<7:
        narx = 2000
  elif 7<=yosh<18:
        narx = 3000
  elif 18<=yosh<65:
        narx = 10000
  else: narx = 0
    
  if narx==0:
        print("Sizga chipta bepul")
  else:
        print(f"Chipta {narx} so'm")

  #Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)

    if qiymat.lower()=='exit':
        break

    qiymat = float(qiymat)
    if qiymat<0:
        continue
    else:
        ildiz = qiymat**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")



#18 tasks
       
  #Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

buyurtmalar = []

while True:
  buyurtma = input("\nMahsulot kiriting: ")
  buyurtmalar.append(buyurtma)
  javob = input("Yana biron nima qo'shasizmi? (ha\yo'q)\t")
  if javob.lower() != 'ha':
    break

  #e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

print("E-bozor uchun mahsulotlar va narxlarini kiriting.\n")
savat2 = {}

while True:
  mahsulot = input("\nMahsulot: ")
  narx = float(input("Narxi: "))
  savat2[mahsulot] = narx

  javob = input("Yana mahsulot kiritasizmi? (ha/yo'q)")
  if javob.lower() != 'ha':
    break

print("Do'kondagi mahsulotlar ro'yxati:\n")
while buyurtmalar:
  buyurtma = buyurtmalar.pop()
  if buyurtma in savat2.keys():
    narx = savat2[buyurtma]
    print(f"{buyurtma.title()} {narx} so'm")
  else:
    print(f"Bizda {buyurtma} mavjud emas")




#to_be_continued...