# 04 · Temel Yetenekler

AI ajentleri, akıl yürütme, planlama, bellek ve araç kullanımını birleştirerek düz bir sohbet robotundan daha fazlasını yapar. Bunlar, bir ajenti "ajent" yapan temel yeteneklerdir.

## 1. Akıl yürütme

Akıl yürütme, bir problemi adımlara ayırıp mantıksal olarak ilerleyebilme yeteneğidir.

**Zincir-sezgisi:** Ajent, hareket etmeden önce sesli olarak düşünür.
> "Kullanıcı 500 doların altında uçak bileti istiyor. Önce uçuşları aramam, ardından fiyata göre filtrelemeli ve sonra müsadeliği kontrol etmeliyim."

**Akıl yürütme olmadan:** Ajent tahmin yapabilir veya yanlış bilgi üretebilir.

## 2. Planlama

Planlama, bir hedefe ulaşmak için gereken eylem sırasını belirlemektir.

**Basit plan:** Araştır → Oku → Özetle → E-posta gönder.
**Dinamik plan:** Ajent, yeni bilgiler öğrendikçe planı değiştirir (örneğin, arama sonuç vermiyorsa farklı bir sorgu dener).

## 3. Refleksiyon ve otomatik düzeltme

Refleksiyon, ajentin kendi çalışmasını inceleyip hatalarını düzeltmesi demektir.

- **Otomatik düzeltme:** "Önceki yanıttam bir matematik hatası var. Tekrar hesaplayayım."
- **Eleştiren ajent:** Çıktıyı incelemek ve nihai yanıttan önce sorunları işaretlemek için ayrı bir LLM geçişi.

Bu, kod üretimi, matematik ve gerçekçilik açısından yazılar için kritiktir.

## 4. Araç kullanımı

Ajentler dış işlevleri çağırabilir:
- Web arama
- Hesap makinesi / kod yürütme
- Veritabanı sorguları
- E-posta / mesajlaşma API'leri
- Dosya sistemi işlemleri

Araç kullanımı, ajentlerin sadece konuşmak yerine **yapabilmelerini** sağlar.

## 5. Bellek

Bellek, ajentin adımlar ve oturumlar arasında bilgi tutmasını sağlar.

- **Kısa vadeli bellek:** Mevcut sohbet veya görev bağlamı.
- **Uzun vadeli bellek:** Geçmiş etkileşimler, kullanıcı tercihleri, bir vektör veritabanında saklanan belgeler.

Bkz. [`docs/06-memory-systems.md`](06-memory-systems.md).

## 6. Çoklu ajent iş birliği

Birden fazla uzman ajent birlikte çalışır, her birinin kendi rolü vardır (araştırmacı, yazar, inceleyen, kodlayıcı).

Bkz. [`docs/07-multi-agent-systems.md`](07-multi-agent-systems.md).

## Yetenek kontrol listesi

Bir ajenti değerlendirir veya inşa ederken şunları sorun:

- [ ] Bir hedefi adımlara bölebiliyor mu? (planlama)
- [ ] Dış araçları kullanabiliyor mu? (araç kullanımı)
- [ ] Geçmiş adımları hatırlayabiliyor mu? (bellek)
- [ ] Kendi hatalarını düzeltiyor mu? (refleksiyon)
- [ ] Diğer ajentlerle birlikte çalışabiliyor mu? (çoklu ajent)
- [ ] Ne zaman insana danışacağını biliyor mu? (güvenlik / korumalar)

## Sonraki adım

Ajentlere araç nasıl verileceğini öğrenmek için [`docs/05-tools-and-integrations.md`](05-tools-and-integrations.md) dosyasını okuyun.