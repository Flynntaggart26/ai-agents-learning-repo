# 03 · Ajent Mimarisi

## Yaygın desenler

Bir ajentin tek "doğru" mimarisi yoktur. Bunlar, en basitten en gelişmelere doğru, en yaygın desenlerdir.

### 1. Basit ReAct ajenti

**ReAct** = Düşün + Eylem Yap. Model ne yapacağını akıl yürüterek karar verir, bir araç seçer, çağırır, sonucu gözlemler ve tekrarlar.

En uygun kullanım: Bilgi arama veya kod çalıştırma gerektiren araç kullanan ajentler.

```
Kullanıcı sorgusu
   │
   ▼
[LLM: "X için arama yapmam gerekiyor"]
   │
   ▼
[Araç: web arama] → sonuç
   │
   ▼
[LLM: "Sonuca dayanarak Y hesaplamam gerekiyor"]
   │
   ▼
[Araç: hesap makinesi] → sonuç
   │
   ▼
[LLM: "Nihai yanıt: ..."]
   │
   ▼
Kullanıcı
```

### 2. Planlama ajenti

Ajent önce çoklu adımlı bir plan oluşturur, ardından her adımı çalıştırır ve yeni bilgiler öğrenildiğinde planı günceller.

En uygun kullanım: "3 günlük bir tatil planla" veya "araştırma raporu yaz" gibi karmaşık görevler.

```
Plan: [Adım 1, Adım 2, Adım 3]
   │
   ▼
Adım 1'i çalıştır → gözlemle → planı güncelle
   │
   ▼
Adım 2'yi çalıştır → gözlemle → planı güncelle
   │
   ▼
Adım 3'ü çalıştır → bitti
```

### 3. Refleksiyon / otomatik düzeltme ajenti

Bir yanıt üretildikten sonra, ayrı bir "eleştiren" geçiş (veya aynı LLM farklı bir rolde) çıktıyı inceler ve düzeltmeler önerir. Ajent, nihai yanıtı döndürmeden önce revize eder.

En uygun kullanım: Kod üretimi, yazı, matematik — hataların yaygın olduğu her şey.

```
Taslak → Eleştir → Revize et → Nihai
```

### 4. Çoklu ajent sistemi

Birden fazla uzman ajent birlikte çalışır. Bir kişi araştırır, bir yazar yazdırmış, bir inceler, bir yayımlar. Mesaj geçişiyle iletişim kurarlar.

En uygun kullanım: Yazılım geliştirme, içerik üretimi veya müşteri desteği gibi karmaşık iş akışları.

Bkz. [`docs/07-multi-agent-systems.md`](07-multi-agent-systems.md).

## Mimari seçme

| İhtiyacınız | Önerilen desen |
|-----------|-------------------|
| Bilgi bul + yanıt ver | Basit ReAct |
| Çoklu adımlı görev | Planlama ajenti |
| Kod veya yazı kalitesi | Refleksiyon ajenti |
| Ekip gibi iş akışı | Çoklu ajent sistemi |

Desenleri karıştırabilirsiniz. Birçok üretim ajenti ReAct + planlama + refleksiyon birleşimini kullanır.

## Python örnek iskeleti

Minimal bir ReAct stilinde ajent çalıştırabilmeniz için [`examples/python/basic_agent/agent.py`](../examples/python/basic_agent/agent.py) dosyasına bakın.

## Sonraki adım

Ajentlerin ne yapabildiğini (akıl yürütme, planlama, refleksiyon, otomatik düzeltme) öğrenmek için [`docs/04-core-capabilities.md`](04-core-capabilities.md) dosyasını okuyun.