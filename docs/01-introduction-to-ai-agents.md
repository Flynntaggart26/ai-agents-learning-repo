# 01 · AI Ajentlerine Giriş

## AI ajenti nedir?

Bir **AI ajenti**, bir büyük dil modelini (LLM) "beyni" olarak kullanan, ortamını algılayabildiği, kararlar alabildiği, eylemler yapabildiği ve sonuçları gözlemleyebildiği — ardından bir hedefe ulaşana kadar bu döngüyü tekrarlayan bir sistendir.

Tek bir turda bir soruyu yanıtlayan standart bir LLM sohbet robotundan farklı olarak, bir ajent şunları yapabilir:

- Araç çağırabilir (web arama, kod çalıştırma, e-posta gönderme, veritabanı sorgulama)
- Geçmiş adımları ve sonuçları hatırlayabilir
- Çoklu adımlı iş akışları planlayabilir
- Hatalarını kendi düzelttebilir
- Tanımladığınız bir hedefe doğrultuda otonom olarak çalışabilir

## Ajent vs. sohbet robotu vs. asistan

| | Sohbet Robotu | AI Ajenti |
|---|---------|----------|
| **Birincil mod** | Soruları yanıtlar | Görevleri tamamlar |
| **Araçlar** | Genellikle yok | API'ler, kod, veritabanları çağırabilir |
| **Bellek** | Yalnızca sohbet geçmişi | Kısa vadeli + uzun vadeli bellek |
| **Planlama** | Tek yanıt | Çoklu adımlı planlar, döngüler |
| **Otonomluk** | Düşük (kullanıcı her turda yürürür) | Yüksek (bir hedefe doğru kendisi yürürür) |
| **Örnek** | "Hava durumu ne?" | "Bana 400 dolardan ucuz bir uçak bileti bul ve takvimime ekle" |

## Bir ajentin temel bileşenleri

1. **Model (LLM):** Akıl yürütme motoru.
2. **Araçlar:** Ajentin çağırabildiği işlevler (web arama, hesap makinesi, e-posta gönderici vb.).
3. **İstek / sistem talimatları:** Ajentine rolünü, hedeflerini ve kurallarını söyler.
4. **Bellek:** Kısa vadeli (geçerli sohbet) ve uzun vadeli (geçmiş etkileşimler, belgeler).
5. **Orkeştrasyon döngüsü:** Algıla → düşün → eylem yap → gözlemle döngüsünü sürekli çalıştıran mantık.
6. **Korumalar:** Ajentin ne yapabileceğini sınırlayan güvenlik kontrolleri.

## Neden ajentler önemli?

LLM'ler metin üretmede iyidir. Ajentler ise **iş yapmada** iyidir. Bir ajent bir konuştuşturabilir, bir rapor yazabilir, yayımlayabilir ve paydaşları bilgilendirebilir — bir insanın her düğmeye tıklamasına gerek kalmadan.

## Sık yanlış inançlar

- **"Ajentler tamamen otonomdur."** Hala değil. Çoğu kullanışlı ajent, e-posta gönderme, para harcamak veya veri silmek gibi önemli eylemler için henüz insanın onayına ihtiyaç duyar.
- **"Ajentler LLM'lerin yerini alır."** Hayır — ajentler LLM'lerin *üstüne* inşa edilir. LLM beyin; ajent gövdedir.
- **"Bunu inşa etmek için bir doktora dereceline ihtiyacın vardır."** Hayır. Temel bir ajent 100 satırdan az kodla inşa edilebilir (bkz. [`examples/`](../examples/)).

## Sonraki adım

Ajent döngüsünü ayrıntılı olarak anlamak için [`docs/02-how-agents-work.md`](02-how-agents-work.md) dosyasını okuyun.