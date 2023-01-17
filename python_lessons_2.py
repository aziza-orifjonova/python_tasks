#019 tasks
 
  # Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

def born_year(name, current_age):
  print(f"{name}, Siz {2022-current_age}-yilda tug'ilgan ekansiz.")

ism = input("Assalamu alaykum. Ismingiz nima? ")
yosh = int(input("Necha yoshdasiz? "))
born_year(ism, yosh)

  # Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

def kv_kub(num):
  print(f"{num} kvadrati: {num**2}"
  f"\n{num} kubi: {num**3}")

son = float(input("Son kiriting: "))
kv_kub(son)

  # Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

def is_even_odd(num):
  print(f"{num} bu toq son. ") if num%2 else print(f"{num} bu juft son. ")

son1 = float(input("Son kiriting: "))
is_even_odd(son1)

  # Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def compare_nums(first, second):
  if first == second:
    print("Sonlar teng.")
  elif first > second:
    print("Kattasi:", first)
  else:
    print("Kattasi:", second)


a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))
compare_nums(a, b)

  # Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.

def darajani_hisobla(x, y=2):
  print(f"{x} ning {y} darajasi {x**y}ga teng")


x = float(input("1-sonni kiriting: "))
y = float(input("2-sonni kiriting: "))
darajani_hisobla(x,y)
  # Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.

  # Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
def is_divides(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

son2 = float(input("Son kiriting: "))
is_divides(son2)



#020 tasks

  #range() funksiyasi qo'lbola usulda
def oraliq(min,max, step=1):
    sonlar = [] # bo'sh ro'yxat
    while min<max:
      if step == 1:
        sonlar.append(min)
        min += 1
      else:
        sonlar.append(min)
        min += step
    return sonlar


print(oraliq(2,20,2))

  # Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

def personal_info(ism, familiya, t_yili, email_add="", t_joyi = ""):
  info = {
    "Ism": ism,
    "Familiya": familiya,
    "Tug'ilgan yili": t_yili
  }
  if email_add:
    info['E-mail manzili'] = email_add
  elif t_joyi:
    info['Tug\'ilgan joyi'] = t_joyi

  return info

# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
mijozlar = []
print("Mijozlar ro'yxatini kiriting: ")

while True:
  ism = input("Ism: ")
  familya = input("Familiya: ")
  t_yil = input("Tug'ilgan yili: ")
  t_joyi = input("Tug'ilgan joyi: ")
  e_manzil = input("Email manzili: ")

  mijozlar.append(personal_info(ism, familya, t_yil, e_manzil, t_joyi))

  javob = input("Davom etamizmi? (yes/no) ")
  if javob.lower != "yes":
    break
# print(mijozlar)
for mijoz in mijozlar:
  print(mijoz['Ism'], mijoz['Familiya'].title(),2022 - int(mijoz['Tug\'ilgan yili']), "yoshda, e-mail manzili:", mijoz['E-mail manzili'])

    #Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

def max_return(a, b, c):
  max = a
  if b >= a:
    max = b
  if c >= a:
    max = c
  return max

  #Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

def aylana_info(radius, pi = 3.14):
  aylana = {
    "radius": radius,
    "diametr": radius*2,
    "perimetri": 2*pi*radius,
    "yuza": pi*radius**2
  }


  #Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

def show_primes(min, max):
  tub_sonlar = []
  for x in range(min, max):
    tub = True

    if x <= 1:
      tub = False
    elif x == 2:
      tub = True
    else:
      for r in range(2, x):
        if x%r == 0:
          tub = False
    if tub:
      tub_sonlar.append(x)
  return tub_sonlar


print(show_primes(-2, 20))

  #Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

def fibonachi_list(son):
  fibonacci_list = []
  for x in range (son):
    if x == 0 or x == 1:
      fibonacci_list.append(1)
    else:
      fibonacci_list.append(fibonacci_list[x-1]+ fibonacci_list[x-2])
  return fibonacci_list


print(fibonachi_list(20))



#021 tasks

  # Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.
 
def title_it(lst):
  for n in range (len(lst)):
    lst[n] = lst[n].title()
  return lst


lst = ['aziza', 'laziza', 'shaxnoza']
print(title_it(lst[:]))
print(lst)
  # Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring

  #done)

  # Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

def bahola(ismlar):
  baholar = {}
  for n in range(len(ismlar)):
      ism = ismlar[n]
      baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
      baholar[ism]=baho
  return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)



#022 tasks

  # Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

def kopaytir(*sonlar):
  kopaytma = 1
  for son in sonlar:
    kopaytma *= son
  return kopaytma


print(kopaytir(123, 2, 3))

  # Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funksiya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def talaba_info(ism, familya, **extra):
  extra['ism'] = ism
  extra['familya'] = familya
  return extra


print(talaba_info("Aziza", "Orifjonova", Kasbi= "talaba"))