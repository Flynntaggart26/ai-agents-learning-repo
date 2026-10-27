# 08 · Bir Ajent İnşa Etme: Adım Adım

Bu rehber, ilk çalışan ajentinizi inşa etmeniz boyunca size yol gösterir. Python kullanıyoruz, ancak aynı adımlar her dilde geçerlidir.

## Önkoşullar

- Python 3.9+
- Bir LLM API anahtarı (OpenAI, Anthropic veya Ollama üzerinden yerel model)
- `pip install openai` (veya sağlayıcınızın SDK'sı)

## Adım 1: Hedefi tanımlayın

Ajentin tam olarak ne yapması gerektiğini yazın.

> Örnek: "Bugünkü en iyi 3 AI hikayesini web'de ara ve bana bir özet e-postası olarak gönder."

Spesifik olun. Belirsiz hedefler ajentleri sapanmaya neden olur.

## Adım 2: Araçlarınızı seçin

Ajentin ihtiyaç duyduğu araçları listeleyin:

- `web_search(query)` — web'de ara
- `send_email(to, subject, body)` — e-posta gönder

1-3 aracıyla başlayın. Daha fazla araç = daha fazla karmaşıklık.

## Adım 3: Sistem talimatını yazın

LLM'e rolünü, hedefini, mevcut araçlarını ve kurallarını söyleyin.

```text
Sen yardımcı bir araştırma asistanısındır.
Hedefin haberleri bulmak ve özetlemektir.
Kullanılabilir araçlar: web_search, send_email.
Kurallar:
- Her zaman bilgiyi göndermeden önce doğrula.
- Kaynaklar olmadan asla e-posta gönderme.
- Bir araç başarısız olursa, bir kez daha deneyin, ardından hatayı raporla.
```

## Adım 4: Ajent döngüsünü uygulayın

1. Kullanıcı girişini al.
2. LLM'i talimat + araçlar + sohbet geçmişi ile çağır.
3. LLM bir araç talep ederse, aracı çalıştır ve sonucu geri besle.
4. LLM araç çağrısı yapmadan nihai yanıt vereene kadar tekrarlayın.
5. Yanıtı kullanıcıya döndür.

Çalıştırılabilir bir sürüm için [`examples/python/basic_agent/agent.py`](../examples/python/basic_agent/agent.py) dosyasına bakın.

## Adım 5: Bellek ekleyin

- Kısa vadeli: Son N mesajı bağlamda tutun.
- Uzun vadeli (isteğe bağlı): Özetleri bir dosyaya veya vektör veritabanına saklayın.

## Adım 6: Korumalar ekleyin

- E-posta gönderme veya dosya yazma gibi eylemler için insanın onayını gerektirin.
- Sıçrama döngülerini önlemek için oturum başına araç çağrı sayısını sınırlayın (örneğin, maksimum 10).
- Tüm araç girdilerini doğrulayın.

## Adım 7: Test edin

Ajenti birkaç farklı hedefle çalıştırın:
- Kolay: "Fransa'nın başkenti nedir?"
- Orta: "Bu makaleyi özetle: [URL]"
- Zor: "Şirket X'in rekabetçilerini bul ve bana bir karşılaştırma e-postası gönder."

## Adım 8: Değerlendirin

Bkz. [`docs/09-evaluation-and-testing.md`](09-evaluation-and-testing.md).

## Hızlı örnek: Python

```python
from openai import OpenAI

client = OpenAI()

def agent_loop(user_message):
    messages = [
        {"role": "system", "content": "You are a helpful agent. Use tools when needed."},
        {"role": "user", "content": user_message}
    ]
    
    for _ in range(10):  # maximum 10 steps to prevent loops
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=[...]  # your tool definitions
        )
        
        message = response.choices[0].message
        messages.append(message)
        
        if not message.tool_calls:
            return message.content  # final answer
        
        for tool_call in message.tool_calls:
            result = execute_tool(tool_call)  # your tool runner
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })
    
    return "Agent reached max steps without completing."
```

## Tam çalıştırılabilir örnek

[`examples/python/basic_agent/agent.py`](../examples/python/basic_agent/agent.py) dosyasını açın ve çalıştırın:

```bash
cd examples/python/basic_agent
pip install -r requirements.txt
python agent.py
```

## JavaScript örneği

[`examples/javascript/basic_agent.js`](../examples/javascript/basic_agent.js) dosyasını açın.

## Yeni başlayanların yaygın hataları

| Hata | Çözüm |
|------|-----|
| Maksimum adım sınırı yok | Adım sayacı ekle |
| Aksiyonlar için insan onayı yok | Onay istemleri ekle |
| Aynı anda çok fazla araç | 1-2 araçla başla |
| Belirsiz sistem talimatı | Rol ve kuralları netleştir |
| Hata yönetimi yok | Araç çağrılarını try/except ile sarmala |

## Sonraki adım

Ajent kalitesini ölçmeyi öğrenmek için [`docs/09-evaluation-and-testing.md`](09-evaluation-and-testing.md) dosyasını okuyun.