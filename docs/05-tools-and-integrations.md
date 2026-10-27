# 05 · Araçlar ve Entegrasyonlar

Araçlar, bir ajentin sadece konuşmak yerine dünyada hareket etmesini sağlayan şeylerdir. Bir araç, LLM'nin talep edebildiği ve ajent çerçevesinin yürüttüğü bir işlevdir.

## Yaygın araç kategorileri

| Kategori | Örnek araçlar | Neyi sağlar |
|----------|---------------|-------------|
| Arama | Web arama, haber arama, site arama | Güncel bilgiyi bulma |
| Hesap | Hesap makinesi, Python yorumlayıcı, SQL | Matematik, veri analizi, kod yürütme |
| İletişim | E-posta, Slack, Discord, SMS | Mesaj ve bildirim gönderme |
| Veri | Veritabanı sorgusu, API çağrısı, elektronik tablo | Yapılandırılmış veriyi okuma ve yazma |
| Tarayıcı | Web getirme, ekran görüntüsü, PDF çıkarma | Web siteleriyle etkileşime geçme |
| Dosya sistemi | Dosya okuma/yazma, yükleme/indirme | Belgeleri yönetme |

## Araç çağırma nasıl çalışır (basitleştirilmiş)

1. Sistem talimatı, LLM'e mevcut araçları ve imzalarını (ad, açıklama, parametreler) söyler.
2. LLM, bir araca ihtiyaç duyduğuna karar verir ve bir araç çağrısı isteği oluşturur (genellikle JSON).
3. Ajent çerçevesi, aracı verilen bağımsız değişkenlerle yürütür.
4. Araç sonucu, yeni bir mesaj olarak LLM'e geri beslenir.
5. LLM, sonucu kullanıp devam eder veya nihai yanıtı verir.

## Python araç tanımı örneği

```python
TOOLS = [
    {
        "name": "web_search",
        "description": "Search the web for information",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"}
            },
            "required": ["query"]
        }
    }
]
```

## Araçlar için güvenlik kuralları

- **Ajenta, veri silebilen, para harcayabilecek veya e-posta gönderebilecek araçları vermemeye dikkat edin** — tamamen test edene kadar insan onayı olmadan.
- Varsayılan olarak **sadece okuma** araçları kullanın. Yazma araçlarını yalnızca ihtiyaç olduğunda ve koruma mekanizmalarıyla ekleyin.
- Her araç çağrısını ve sonucunu denetim amacıyla günlüğe kaydedin.
- Araç bağımsız değişkenlerini yürütmeden önce doğrulayın (tür, aralık, izin verilen değerler).

## Araçları işleyen popüler çerçeveler

- LangChain / LangGraph
- LlamaIndex
- AutoGPT / AgentGPT desenleri
- CrewAI
- Microsoft Semantic Kernel
- OpenAI Assistants API (yerleşik araç kullanımı)

Minimal araç kullanan ajent kodu için [`examples/`](../examples/) dosyasına bakın.

## Sonraki adım

Ajentlerin bilgiyi nasıl hatırladığını öğrenmek için [`docs/06-memory-systems.md`](06-memory-systems.md) dosyasını okuyun.