import random

# Rastgele sayı listesi oluştur
def rastgele_liste_uret(boyut, minimum, maksimum):
    return [random.randint(minimum, maksimum) for _ in range(boyut)]

# Insertion Sort algoritması
def siralama_islemi(sayilar):
    for i in range(1, len(sayilar)):
        mevcut = sayilar[i]
        pozisyon = i - 1

        # Mevcut sayıyı doğru yere yerleştir
        while pozisyon >= 0 and sayilar[pozisyon] > mevcut:
            sayilar[pozisyon + 1] = sayilar[pozisyon]
            pozisyon -= 1
        sayilar[pozisyon + 1] = mevcut

        # Her adımı ekrana yazdır
        print(f"Adım {i}: {sayilar}")

# Rastgele bir liste oluştur ve sıralama yap
boyut = int(input("Kaç adet rastgele sayı üretmek istersiniz? "))
minimum = int(input("En küçük değer: "))
maksimum = int(input("En büyük değer: "))

sayilar = rastgele_liste_uret(boyut, minimum, maksimum)

print("\nOluşturulan Liste:", sayilar)
siralama_islemi(sayilar)
print("\nSıralı Liste:", sayilar)