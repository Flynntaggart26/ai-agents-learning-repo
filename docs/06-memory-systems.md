# 06 · Bellek Sistemleri

Bellek, bir ajentin tek bir sohbet turunun ötesinde bilgiyi tutmasını sağlayan şeydir. Bellek olmadan, bir ajent bağlam penceresi dolduğunda her şeyi unutur.

## Bellek türleri

### Kısa vadeli bellek (çalışma belleği)

Geçerli sohbet veya görev bağlamı, LLM'nin bağlam penceresinde tutulur.

- Son mesajları, araç sonuçlarını ve ara düşünceleri tutar.
- Modelin bağlam uzunluğu ile sınırlıdır (örneğin, 128k token).
- Oturum sona erdikçe veya pencere kısaltıldığında unutulur.

### Uzun vadeli bellek

İhtiyaç duyulduğunda alınabilen kalıcı olarak depolanan bilgi.

- Kullanıcı tercihleri ("kullanıcı kısa özetleri sever")
- Geçmiş sohbetler ("geçen hafta proje X hakkında konuştuk")
- Belgeler ve bilgi bankası makaleleri
- Bir alana ilişkin öğrenilen gerçekler

Çoğu zaman bir **vektör veritabanı** (embedding + benzerlik arama) ile uygulanır.

### Öznel bellek

Belirli olaylar veya bölümlerle ilgili bellek ("Salı günü bu yaklaşımı denemiştim ve başarısız olmuştu").

### Anlamsal bellek

Genel gerçekler ve kavramlar ("Paris Fransa'nın başkentidir").

## Ajentler için nasıl çalışır (RAG)

1. Ajentin bir sorgusu veya durumu vardır.
2. Sistem, sorguyu bir vektöre dönüştürür.
3. Benzer depolanan öğeleri bulmak için bir vektör veritabanında arama yapar.
4. En iyi sonuçlar ilgili bellek olarak bağlama enjekte edilir.
5. Ajent, hareket etmek için bu belleği kullanır.

Bu, ajentlere uygulandığında genellikle **Retrieval-Augmented Generation (RAG)** olarak adlandırılır.

## Pratikte bellek

| İhtiyaç | Basit yaklaşım | Üretim yaklaşımı |
|------|----------------|------------------|
| Geçerli sohbeti hatırlamak | Tam geçmişi LLM'e geçir | Eski mesajları özetle |
| Kullanıcı tercihlerini hatırlamak | JSON dosyasında sakla | Veritabanı + alma |
| Geçmiş belgeleri arama | Anahtar kelime arama | Vektör DB + embeddingler |
| Oturumlar arasında hatırlamak | Oturum kimlikleri + dosya deposu | Kullanıcı profilleri + vektör DB |

## Güvenlik ve gizlilik

- Şifreler, API anahtarları veya kişisel bilgileri (PII) ajent belleğinde şifrelenmemiş ve gerekli olmadığı sürece saklamayın.
- Kullanıcıların depolanan belleğini görmelerine ve silmelerine izin verin (GDPR / CCPA uyumluluğu).
- Ajentin neyi hatırladığı konusunda şeffaf olun.

## Sonraki adım

Birden fazla ajentin nasıl birlikte çalıştığını öğrenmek için [`docs/07-multi-agent-systems.md`](07-multi-agent-systems.md) dosyasını okuyun.