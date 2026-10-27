# 02 · Ajentler Nasıl Çalışır

## Ajent döngüsü

Çoğu ajent tekrarlanan bir döngü çalıştırır:

1. **Algıla** — Giriş alın (kullanıcı mesajı, olay, zamanlanmış tetikleyici).
2. **Düşün** — LLM, talimatlara ve bağlama dayanarak sonra ne yapacağına karar verir.
3. **Eylem yap** — Ajent bir araç çağırır, mesaj gönderir veya belleği günceller.
4. **Gözlemle** — Sonuç geri döner (araç çıktısı, hata, yeni bilgi).
5. **Tekrarla** — Hedef tamamlanana veya bir durdurma koşulu gelene kadar adım 2'ye dön.

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ Algıla  │───▶│ Düşün   │───▶│ Eylem   │───▶│ Gözlemle│
└─────────┘    └─────────┘    └─────────┘    └─────────┘
      ▲                                         │
      └──────────────────────(döngü)────────────┘
```

## Somut bir örnek

**Hedef:** "Bugünkü en iyi AI haberlerini bul ve bana bir özet e-posta olarak gönder."

1. **Algıla:** Kullanıcı hedefi gönderir.
2. **Düşün:** "AI haberlerini aramam, ardından bir e-posta taslağı hazırlamalı ve göndermeliyim."
3. **Eylem:** Web-arama aracını "bugünkü en iyi AI haberleri" sorgusu ile çağır.
4. **Gözlemle:** Arama sonuçları geri döner (bağlantılar, özetler).
5. **Düşün:** "Şimdi makaleleri okuyup bir özet tasarlamalıyım."
6. **Eylem:** Üst makaleleri açmak için tarayıcı/getirme aracını çağır.
7. **Gözlemle:** Makale içeriği geri döner.
8. **Düşün:** "E-posta özetini tasarla."
9. **Eylem:** E-posta aracını çağırarak taslağı gönder.
10. **Gözlemle:** E-posta gönderildi. Hedef tamamlandı. Dur.

## Kontrolör olarak LLM

LLM web arama veya e-posta göndermeyi yerel olarak "bilmemektedir". Bunun yerine, bir araç çağrısı için bir **istek** oluşturur (genellikle yapılandırılmış bir JSON biçiminde). Ajent çerçevesi bu aracı çalıştırır, sonucu LLM'e yeni bir mesaj olarak besler ve döngü devam eder.

Bu bazen **araç kullanımı** veya **işlev çağrısı** olarak adlandırılır.

## Döngü ne zaman durur?

Bir ajent şu durumlarda durur:

- Hedef başarılır (LLM başarıyı bildirir).
- Maksimum adım sayısına ulaşıldığında (sonsuz döngüyü önlemek için).
- Geri dönüşümlenemeyen bir hata oluştuğunda.
- Bir insan "dur" der veya bir eylemi reddeder.

## Döngüdeki güvenlik

Ajentler otonom olarak hareket ettiği için, e-posta gönderme, dosya yazma veya para harcamak gibi yan etkileri olan her eylem, ajenti güvenle kullanabileceğinize kadar **insan-döngüsünde onay** gerektirmelidir. Bkz. [`docs/11-best-practices-and-security.md`](11-best-practices-and-security.md).

## Sonraki adım

ReAct ve planlama ajentleri gibi yaygın mimari desenler için [`docs/03-agent-architecture.md`](03-agent-architecture.md) dosyasını okuyun.