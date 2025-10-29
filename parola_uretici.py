
import os
import base64
import datetime

def parola_uret(uzunluk):
    """Belirtilen uzunlukta güvenli bir parola üretir."""
    raw = base64.b64encode(os.urandom(48)).decode('utf-8')
    return raw[:uzunluk]

def secileni_kaydet(parola, dosya_adi="secili_parolalar.txt"):
    """Seçilen parolayı tarihle birlikte dosyaya ekler (şifreleme yok)."""
    zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(dosya_adi, "a", encoding="utf-8") as f:
        f.write(f"{zaman} - Seçtiğiniz şifre: {parola}\n")
    print(f"✅ Seçilen parola '{dosya_adi}' dosyasına kaydedildi.")

def parola_oezellikleri_goster(parolalar):
    print("\nOluşturulan parolalar:")
    for i, p in enumerate(parolalar, start=1):
        print(f"{i}) {p}")

def kullanici_secim_sor(parolalar):
    """Parolalar gösterildikten sonra kullanıcıya seçim sorgulama akışı."""
    while True:
        secim = input("\nAralarında seçtiğiniz var mı? (e/h): ").strip().lower()
        if secim not in ("e", "h"):
            print("Lütfen 'e' (evet) veya 'h' (hayır) girin.")
            continue

        if secim == "e":
            cevap = input("Seçtiğiniz şifreyi numara ile mi (örnek: 2) yoksa tam metin olarak mı gireceksiniz? (n/m): ").strip().lower()
            if cevap == "n":
                numara = input("Lütfen seçtiğiniz parolanın numarasını girin: ").strip()
                if not numara.isdigit():
                    print("Geçersiz numara. Tekrar deneyin.")
                    continue
                idx = int(numara) - 1
                if idx < 0 or idx >= len(parolalar):
                    print("Numara aralık dışında. Tekrar deneyin.")
                    continue
                secilen = parolalar[idx]
                secileni_kaydet(secilen)
                return True  # seçildi, döngüyü sonlandır
            elif cevap == "m":
                girilen = input("Lütfen tam parolayı yapıştırın: ").strip()
                if girilen in parolalar:
                    secileni_kaydet(girilen)
                    return True
                else:
                    # Kullanıcı tam metni girdi ama listede yoksa yine kabul edip kaydedebiliriz
                    onay = input("Girdiğiniz parola önerilenler arasında değil. Yine de kaydetmek istiyor musunuz? (e/h): ").strip().lower()
                    if onay == "e":
                        secileni_kaydet(girilen)
                        return True
                    else:
                        print("Seçim kaydedilmedi. Yeni parolalar istiyorsanız 'h' ile devam edebilirsiniz.")
                        return False
            else:
                print("Geçersiz seçim. 'n' (numara) veya 'm' (metin) girin.")
                continue
        else:
            # secim == "h" -> yeni parolalar iste
            return False

def main():
    print("🔑 Parola Üreticiye Hoş Geldiniz! (Python sürümü)\n")

    # Parola uzunluğu
    try:
        uzunluk = int(input("Lütfen üretilecek parolanın uzunluğunu girin: ").strip())
        if uzunluk <= 0:
            print("Hata: Pozitif bir sayı girin.")
            return
    except ValueError:
        print("Hata: Geçerli bir sayı girmeniz gerekiyor.")
        return

    
    try:
        adet_input = input("Kaç adet parola üretmek istersiniz? (varsayılan 3): ").strip()
        adet = int(adet_input) if adet_input else 3
        if adet <= 0:
            print("Hata: Pozitif bir sayı girin.")
            return
    except ValueError:
        print("Hata: Geçerli bir sayı girmeniz gerekiyor.")
        return

    
    while True:
        parolalar = [parola_uret(uzunluk) for _ in range(adet)]
        parola_oezellikleri_goster(parolalar)

        secim_sonucu = kullanici_secim_sor(parolalar)
        if secim_sonucu:
            
            break
        else:
           
            print("\nYeni parolalar oluşturuluyor...")

    print("\nProgram sonlandırıldı. İyi günler!")

if __name__ == "__main__":
    main()
