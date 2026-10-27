# 07 · Çoklu Ajent Sistemleri

Bir çoklu ajent sisteminde iki veya daha fazla ajent birlikte çalışır, her biri uzmanlaşmış bir role sahiptir. Bir genelist ajentin her şeyi yapmasını sağlamak yerine, işi bir ekibe bölersiniz.

## Neden çoklu ajent?

- **Uzmanlaşma:** Bir ajent araştırır, diğeri yazar, bir diğeri inceler.
- **Denetim ve denge:** Bir inceleyen ajent, yazar ajentin hatalarını yakalar.
- **Eşzamanlı çalışma:** Ajentler görevin farklı bölümlerini eşzamanlı olarak üstlenebilir.
- **Daha kolay hata ayıklama:** Hangi ajentin hangi çıktıyı ürettiğini görebilirsiniz.

## Yaygın çoklu ajent desenleri

### 1. Boru hattı (montaj hattı)

Ajent A → Ajent B → Ajent C

Örnek: Araştırmacı → Yazar → Editör → Yayımlayan.

### 2. Tartışma / eleştirme

Ajent A bir taslak üretir. Ajent B onu eleştirir. Ajent A, Ajent B onaylayana kadar revize eder.

### 3. Yönlendirici / dağıtıcı

Bir şöfre ajent isteği alır ve en uygun uzman ajent'e yönlendirir.

Örnek: "Faturalama sorusu → Faturajent", "Teknik soru → DestekAjenti".

### 4. İşbirlikçi / siyah pano

Tüm ajentler, birbirlerinin çalışmalarına dayanarak paylaşılan bir alanda okuma ve yazma yapar.

## Ajentler arasındaki iletişim

Ajentler genellikle şu şekilde iletişim kurar:

- Mesaj geçişi (metin veya yapılandırılmış veri)
- Paylaşılan bellek veya siyah pano'ya okuma/yazma
- Birbirlerini araç olarak çağırmak

## İçerik oluşturma için örnek ekibiniz

| Ajent | Rol |
|-------|-----|
| Araştırmacı | Gerçekleri ve kaynakları bulur |
| Yazar | Makale taslağını yazar |
| Editör | Tonu, netliği ve gerçekleri kontrol eder |
| Yayımlayan | Biçimlendirir ve hedef yere gönderir |

## Zorluklar

- **Koordinasyon:** Ajentler döngülerde kalabilir veya sonsuz aktarımda kalabilir.
- **Maliyet:** Daha fazla ajent = daha fazla LLM çağrısı = daha yüksek maliyet ve gecikme.
- **Tutarlılık:** Farklı ajentler birbirleriyle çelişebilir.
- **Hata ayıklama:** Hangi ajentin hataya neden olduğunu izlemek daha zordur.

## Çoklu ajent ne zaman kullanılır?

Bunu şu durumlarda kullanın:
- Görev doğal olarak farklı roller haline bölünebildiğinde.
- Kaliteyi sağlamak için inceleme/eleştiriye ihtiyacınız olduğunda.
- Tek bir ajent yeterli değilse (karmaşık, uzun süren iş akışları).

Önce tek bir ajentle başlayın. Tek bir ajent karmaşıklığı taşıyamayabilirken daha fazla ajent ekleyin.

## Sonraki adım

Adım adım derleme rehberi için [`docs/08-building-an-agent.md`](08-building-an-agent.md) dosyasını okuyun.