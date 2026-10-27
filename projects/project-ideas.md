# AI Ajentleri İçin Proje Fikirleri

Ajent kavramlarını pekiştirmek için inşa edebileceğiniz başlangıçtan ileri seviyeye kadar proje fikirleri. Her biri bir zorluk seviyesi, önerilen araçlar ve ne öğreneceğinizi içerir.

## Başlangıç seviyesi

### 1. Kişisel Araştırma Asistanı
**Hedef:** Bir konu hakkında web'de arama yapıp kısa bir özet ve kaynaklar döndürmek.
**Araçlar:** Web arama, metin özetleme
**Öğrenecekleriniz:** Araç kullanımı, temel ajent döngüsü, kaynak gösterme

### 2. Hesap Makinesi Ajenti
**Hedef:** Bir hesap makinesi aracını çağırarak matematiksel kelime sorunlarını çözmek.
**Araçlar:** Hesap makinesi
**Öğrenecekleriniz:** Araç çağrısı, akıl yürütme, adım adım düşünme

### 3. Hava Durumu Raporcu
**Hedef:** Bir şehir verildiğinde, hava durumunu alıp giysiyorum önerisi sunmak.
**Araçlar:** Hava durumu API'si
**Öğrenecekleriniz:** API entegrasyonu, basit karar mantığı

## Orta seviye

### 4. E-posta Sıralama Ajenti
**Hedef:** Okunmamış e-postaları okuyup her birini özetle ve sizin onayınız için yanıt taslakları hazırlayın.
**Araçlar:** E-posta okuma, e-posta gönderme (yalnızca taslak)
**Öğrenecekleriniz:** Bellek, insan-döngüsünde onay, koruma mekanizmaları

### 5. Toplantı Hazırlama Ajenti
**Hedef:** Bir toplantı başlığı ve katılımcılar verildiğinde, geçmiş bilgi bulup konuşma notları hazırlayın.
**Araçlar:** Web arama, takvim, LinkedIn (kullanıcı profilleri)
**Öğrenecekleriniz:** Çoklu adımlı planlama, bilgi sentezi

### 6. Kod İnceleme Ajenti
**Hedef:** Bir pull request diff'ini okuyup iyileştirmeler önerin ve potansiyel hataları işaretleyin.
**Araçlar:** Dosya okuma, kod linter (sahte)
**Öğrenecekleriniz:** Refleksiyon, otomatik düzeltme, yapılandırılmış çıktı

## İleri seviye

### 7. Rekabetçi Araştırma Ajenti
**Hedef:** Bir şirket verildiğinde, rekabetçileri, fiyatlandırma ve özellikleri araştırıp bir karşılaştırma raporu üretin.
**Araçlar:** Web arama, tarayıcı, PDF oluşturucu
**Öğrenecekleriniz:** Karmaşık planlama, çoklu adımlı iş akışı, rapor oluşturma

### 8. Çoklu Ajent İçerik Takımı
**Hedef:** Araştırmacı → Yazar → Editör → Yayımlayan boru hattıyla blog yazıları üretin.
**Araçlar:** Web arama, CMS API'si (sahte), e-posta
**Öğrenecekleriniz:** Çoklu ajent sistemleri, aktarımlar, kalite kontrolü

### 9. Otonom Seyahat Planlayıcı
**Hedef:** Bütçesi sınırlı bir 3 günlük tatil planlayın: uçuşlar, otel, etkinlikler, takvim davetiyeleri.
**Araçlar:** Uçuş API'si, otel API'si, takvim, e-posta
**Öğrenecekleriniz:** Çoklu araç koordinasyonu, kısıtlamalar, bütçe takibi

### 10. Müşteri Desteği Ajenti
**Hedef:** Bilgi bankasından müşteri sorularına yanıt verin; emin olmadığınızda bir insana yönlendirin.
**Araçlar:** Vektör DB arama, bilet sistemi, e-posta
**Öğrenecekleriniz:** RAG, bellek, eskalasyon mantığı, güvenlik

## Nasıl seçersiniz?

- **Hiç ajent oluşturmadıysanız?** #1 veya #2 ile başlayın.
- **Temelleri biliyorsanız?** #4 veya #6'yı deneyin.
- **Bir zorluk istiyorsanız?** #8 veya #10'ı oluşturun.

## İpuçları

- Gerçek API'ları bağlamadan önce, sahte araçlar (sahte veri döndüren) ile başlayın.
- E-posta gönderme, para harcamak veya dosya yazma gibi her eylem için insan onayı ekleyin.
- Hata ayıklayabilmeniz için her adımı günlüğe kaydedin.
- Tamamladığınız projeyi bu depoya bir pull request olarak paylaşın.

---

Bir proje fikri eklemek istiyorsanız? [`projects/project-ideas.md`](projects/project-ideas.md) dosyasına bir pull request açın.