# 09 · Değerlendirme ve Test

Ajentiniz gerçekten iyi mi? Değerlendirme bunu söyler. Test hataları yakalar.

## Neden ajentleri değerlendirmek gerekir?

LLM'ler deterministik değildir — aynı girdi farklı çıktılar üretebilir. Ajentler araç kullanımı ve döngülerle daha fazla belirsizlik ekler. Sistematik bir değerlendirmeye ihtiyacınız vardır.

## Ne ölçülür

| Ölçüt | Ne anlama gelir | Nasıl ölçülür |
|--------|---------------|---------------|
| Görev tamamlama | Ajent hedefi tamamladı mı? | İnsan incelemesi veya LLM jürisi |
| Araç doğruluğu | Doğru araçlar doğru bağımsız değişkenlerle çağrıldı mı? | Günlük denetimi |
| Tamamlama adımları | Kaç adım sürdü? | Döngü yinelemelerini sayın |
| Hata oranı | Kaç sıklıkta araçlar başarısız oldu? | Hataları kaydedin |
| Gecikme | Kaç sürdü? | Başlangıç → bitiş süresi |
| Maliyet | LLM çağrıları ne kadar pahalı? | Token sayımı |

## Değerlendirme yöntemleri

### 1. Altın veri kümeleri

Beklenen sonuçları içeren örnek girdilerin bir kümesi oluşturun.

| Girdi | Beklenen sonuç |
|-------|----------------|
| "2+2 kaç?" | Ajent "4" yanıtlasın |
| "AI haberleri ara" | Ajent web_search çağırıp özet döndürsün |

Her girdi üzerinde ajenti çalıştırın ve sonucun beklentiyle eşleşip eşleşmediğini kontrol edin.

### 2. LLM jürisi

Ajentin çıktısını puanlamak için güçlü bir LLM kullanın:

> "Bu ajent yanıtını doğruluk, yardımcı olabilirlik ve güvenlik açısından 1-5 arasında derecelendirin."

### 3. İnsan incelemesi

İnsanların ajenti test etmesini sağlayın ve şunları rapor etmesi için onaylayın:
- Görevi tamamladı mı?
- Hata yaptı mı?
- Yeterince hızlı mıydı?

### 4. A/B testi

Bir istem veya araç kümesinin iki sürümünü deneyin ve sonuçları karşılaştırın.

## Test stratejileri

- **Birim testleri:** Tek tek araçları izolasyonla test edin.
- **Entegrasyon testleri:** Ajent döngüsünü sahte araçlarla (gerçek API çağrılarına gerek yok) test edin.
- **Uçtan uca testler:** Gerçek hedefler üzerinde tam ajenti çalıştırın (maliyetli olduğunda dikkatli kullanın).
- **Kırmızı takım testi:** Ajenti güvensiz veya yanlış bir şey yapmaya zorlamaya çalışın.

## Örnek test (Python)

```python
def test_web_search_tool():
    result = web_search("capital of France")
    assert "Paris" in result
```

## Bir ajent "iyi yeterli" ne zaman?

Mükemmel bir puan yok. Kendi çubugunuzu kendiniz belirleyin:

- Test kümesinde %90 görev tamamlama
- 100 test çalışmasında hiçbir güvensiz eylem yok
- Ortalama tamamlama süresi 30 saniye altında

## Sonraki adım

Ajentleri üretimde çalıştırmayı öğrenmek için [`docs/10-deployment-and-observability.md`](10-deployment-and-observability.md) dosyasını okuyun.