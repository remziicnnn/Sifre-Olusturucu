📘 README.md
# 🔑 Parola Üretici (Python)

Bu proje, terminal üzerinden çalışan basit ama işlevsel bir **parola üretme aracı**dır.  
Kullanıcıya rastgele güçlü parolalar önerir, kullanıcı seçtiği parolayı belirtebilir ve tarih bilgisiyle birlikte bir `.txt` dosyasına kaydeder.  
Yeni parolalar üretmek mümkündür — tamamen etkileşimli bir yapıya sahiptir.

---

## 🚀 Özellikler

- Belirtilen uzunlukta rastgele parola üretimi  
- İstenilen sayıda parola önerisi  
- Kullanıcı seçimi sonrası otomatik tarihli kayıt  
- Şifreleme **yapmadan** düz metin kaydı (`secili_parolalar.txt`)  
- Basit ve tamamen terminal üzerinden kullanılabilir  

---

## 🧩 Kullanım

### 1️⃣ Gerekli kütüphane
Bu proje ek bir kütüphane gerektirmez (yalnızca Python’un standart kütüphaneleriyle çalışır).  
Python 3.6+ önerilir.

### 2️⃣ Çalıştırma
python parola_uretici.py

3️⃣ Adımlar

Program sizden parola uzunluğunu ister.

Kaç adet parola üretileceğini girersiniz (varsayılan: 3).

Üretilen parolalar listelenir.

Arasından birini seçerseniz, program seçilen parolayı tarih bilgisiyle birlikte secili_parolalar.txt dosyasına kaydeder.

Seçmezseniz, yeni parolalar önerilir.

📄 Kayıt Formatı

Seçilen her parola secili_parolalar.txt dosyasına şu formatta eklenir:

2025-10-29 14:42:03 - Seçtiğiniz şifre: TzLfdWbq2K7shn...

🧠 Örnek Terminal Çıktısı
🔑 Parola Üreticiye Hoş Geldiniz! (Python sürümü)

Lütfen üretilecek parolanın uzunluğunu girin: 12
Kaç adet parola üretmek istersiniz? (varsayılan 3): 3

Oluşturulan parolalar:
1) ZTdiZGQ0NGM5
2) bWFuY2h0ZXN0
3) d2VlbmVsdmVu

Aralarında seçtiğiniz var mı? (e/h): e
Seçtiğiniz şifreyi numara ile mi (örnek: 2) yoksa tam metin olarak mı gireceksiniz? (n/m): n
Lütfen seçtiğiniz parolanın numarasını girin: 2
✅ Seçilen parola 'secili_parolalar.txt' dosyasına kaydedildi.
