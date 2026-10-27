# 10 · Dağıtım ve Gözlenebilirlik

Ajentiniz yerel olarak çalışıyor olabilir; şimdi onu güvenilir bir şekilde çalıştırmanız ve ne yaptığını izlemeniz gerekiyor.

## Dağıtım seçenekleri

| Seçenek | En uygun kullanım | Notlar |
|--------|-----------|-------|
| Yerel betik | Kişisel kullanım, test | En basit, altyapı yok |
| Sunucusuz işlev (AWS Lambda, Vercel, Cloudflare Workers) | Olay tabanlı ajentler | Çağrı başına ödeme, sıfıra ölçeklenebilir |
| Konteyner (Docker, Kubernetes) | Uzun süren ajentler | Daha fazla kontrol, daha fazla işletme |
| Ajent platformu (LangSmith, LangGraph vb.) | Yönetilen ajent barındırma | Yerleşik izleme ve değerlendirme |

## Gözlenebilirlik: neyi günlüğe kaydedin

- Her kullanıcı girişi ve ajent çıktısı
- Her araç çağrısı: ad, bağımsız değişkenler, sonuç, süre
- Her LLM çağrısı: model, token, maliyet
- Hatalar ve istisnalar
- İnsan onayları ve reddedilmiş eylemler

## İzleme

Ajentin全 journey'sini görselleştirmek için bir izleme aracı kullanın (LangSmith, Langfuse, Helicone veya benzeri):

```
Kullanıcı sorgusu → LLM → Araç A → LLM → Araç B → LLM → Nihai yanıt
```

İzleme, ajentin nerede hata yaptığını debug etmenize yardımcı olur.

## Maliyet kontrolü

- Çalışma başına maksimum adım sayısı ayarlayın.
- Oturum başına maksimum maliyet ayarlayın (örneğin, 0,50 $).
- Basit görevler için daha ucuz modeller, karmaşık akıl yürütme için daha pahalı modeller kullanın.
- Güvenli olduğunda tekrarlanan LLM yanıtlarını önbelleğe alın.

## Üretimde güvenlik

- **İnsan-döngüsünde:** E-posta gönderme, dosya yazma, ödeme, silme gibi eylemler için insanın onayını gerektirin.
- **Hız sınırlama:** Bir kullanıcının ajenti ne sıklıkta tetikleyebileceğini sınırlayın.
- **Girdi doğrulama:** Kullanıcı girdisini LLM'e veya araçlara geçirmeden önce temizleyin.
- **Çıktı doğrulama:** Ajent çıktısının kullanıcıya ulaşmadan önce kontrol edin (özellikle kod veya e-posta için).

## Ortam değişkenleri

API anahtarlarını asla kodun içinde yazmayın. Ortam değişkenlerini kullanın:

```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
```

`.env` dosyasını `.gitignore`'a ekleyerek sırashı asla depoya gönderilmediğinden emin olun.

## Sonraki adım

[`docs/11-best-practices-and-security.md`](11-best-practices-and-security.md) dosyasını okuyun.