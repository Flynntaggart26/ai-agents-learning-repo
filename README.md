# AI Agents: Pratik Öğrenme Deposu

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Language: Turkish](https://img.shields.io/badge/language-Turkish-red.svg)](README.md)
[![GitHub release](https://img.shields.io/github/release/Flynntaggart26/ai-agents-learning-repo.svg?label=Latest%20Release)](https://github.com/Flynntaggart26/ai-agents-learning-repo/releases)
[![GitHub last commit](https://img.shields.io/github/last-commit/Flynntaggart26/ai-agents-learning-repo)](https://github.com/Flynntaggart26/ai-agents-learning-repo/commits/main)
[![Open Issues](https://img.shields.io/github/issues/Flynntaggart26/ai-agents-learning-repo)](https://github.com/Flynntaggart26/ai-agents-learning-repo/issues)
[![Open Pull Requests](https://img.shields.io/github/issues-pr/Flynntaggart26/ai-agents-learning-repo)](https://github.com/Flynntaggart26/ai-agents-learning-repo/pulls)

Kapsamlı, açık kaynaklı ve eğitici bir **yapay zeka ajentleri (AI Agents)** öğrenme deposu. Ajentlerin ne olduklarını, nasıl çalıştıklarını, nasıl inşa edildiklerini ve nasıl üretime alındıklarını adım adım öğrenin.

> **Misyon:** Yapay zeka ajenti deneyimi olmayan herkesin bu depoyu okuyabilmesi, örnek kodları çalıştırabilmesi ve kendi çalışan ajentini sıfırdan inşa edebilmesini sağlamak.

---

## 📖 Bu Depo Nedir?

AI ajentleri, sadece metin üreten sohbet robotlarından çok ötesindedir. Bir ajent, bir büyük dil modelini (LLM) "beyni" olarak kullanarak ortamını algılayabilir, karar alabilir, araçları çağırabilir, hatalarını düzeltebilir ve bir hedefe ulaşana kadar otonom olarak çalışabilir.

### Ajent döngüsü nasıl çalışır?

```mermaid
flowchart LR
    A[Kullanıcı Girişi] --> B[Algıla / Perceive]
    B --> C[Düşün / Think]
    C --> D[Eylem Yap / Act]
    D --> E[Gözlemle / Observe]
    E --> F{Hedef Ulaşıldı mı?}
    F -->|Hayır| C
    F -->|Evet| G[Nihai Yanıtı Döndür]
    style A fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style G fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
```

Bu depo, teorik bilgi ve pratik örnekleri bir araya getirerek şu soruların cevabını verir:

- **AI ajenti nedir?** (düz bir LLM'den nasıl farklıdır?)
- **Ajent nasıl çalışır?** (algıla → düşün → eylem yap → gözlemle döngüsü)
- **Ajentlere nasıl araç eklenir?** (web arama, hesap makinesi, e-posta, veritabanı vb.)
- **Bir ajent nasıl inşa edilir?** (adım adım rehber)
- **Ajent kalitesi nasıl ölçülür ve geliştirilir?** (değerlendirme ve test)
- **Ajent üretimde nasıl güvenli bir şekilde çalıştırılır?** (dağıtım, gözlenebilirlik, güvenlik)

---

## 🗺️ Öğrenme Yolu (Roadmap)

Depodaki belgeleri sırayla okumak önerilir. Her belge, öncekini temel alır:

| Sıra | Dosya | Ne Öğreneceksiniz |
|------|-------|-------------------|
| 1 | [`docs/01-introduction-to-ai-agents.md`](docs/01-introduction-to-ai-agents.md) | AI ajenti nedir, sohbet robotu ve asistan arasındaki farklar, temel bileşenler |
| 2 | [`docs/02-how-agents-work.md`](docs/02-how-agents-work.md) | Ajent döngüsü: algıla → düşün → eylem yap → gözlemle |
| 3 | [`docs/03-agent-architecture.md`](docs/03-agent-architecture.md) | ReAct, planlama, refleksiyon ve çoklu ajent mimarileri |
| 4 | [`docs/04-core-capabilities.md`](docs/04-core-capabilities.md) | Akıl yürütme, planlama, refleksiyon, otomatik düzeltme |
| 5 | [`docs/05-tools-and-integrations.md`](docs/05-tools-and-integrations.md) | Ajentlere araç verme, güvenlik kuralları, popüler çerçeveler |
| 6 | [`docs/06-memory-systems.md`](docs/06-memory-systems.md) | Kısa vadeli, uzun vadeli, öznel ve anlamsal bellek; RAG |
| 7 | [`docs/07-multi-agent-systems.md`](docs/07-multi-agent-systems.md) | Çoklu ajent sistemleri: boru hattı, tartışma, yönlendirici desenler |
| 8 | [`docs/08-building-an-agent.md`](docs/08-building-an-agent.md) | İlk ajentinizi sıfırdan inşa etme (adım adım rehber) |
| 9 | [`docs/09-evaluation-and-testing.md`](docs/09-evaluation-and-testing.md) | Ajent kalitesini ölçme, değerlendirme yöntemleri, test stratejileri |
| 10 | [`docs/10-deployment-and-observability.md`](docs/10-deployment-and-observability.md) | Üretimde dağıtım, izleme, maliyet kontrolü, güvenlik |
| 11 | [`docs/11-best-practices-and-security.md`](docs/11-best-practices-and-security.md) | En iyi uygulamalar, istem enjeksiyonu savunması, insan-döngüsünde onay |

---

## 🚀 Hızlı Başlangıç

İlk ajentinizi çalıştırmak için aşağıdaki adımları izleyin.

### 1. Depoyu klonlayın

```bash
git clone https://github.com/Flynntaggart26/ai-agents-learning-repo.git
cd ai-agents-learning-repo
```

### 2. Örnek kodları inceleyin

Depoda iki programlama dilinde çalıştırılabilir örnekler bulunur:

**Python — Temel ReAct Ajenti**

```python
from openai import OpenAI

client = OpenAI()

def run_agent(user_message):
    messages = [
        {"role": "system", "content": "You are a helpful agent. Use tools when needed."},
        {"role": "user", "content": user_message}
    ]
    
    for _ in range(10):  # maksimum 10 adım
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=[...]  # araç tanımlarınız
        )
        message = response.choices[0].message
        messages.append(message)
        
        if not message.tool_calls:
            return message.content  # nihai yanıt
        
        for tool_call in message.tool_calls:
            result = execute_tool(tool_call)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })
    
    return "Maksimum adım sayısına ulaşıldı."
```

Tam çalışır örneği: [`examples/python/basic_agent/agent.py`](examples/python/basic_agent/agent.py)

**JavaScript — Temel Ajent**

```javascript
const { OpenAI } = require("openai");
const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function runAgent(userMessage) {
  const messages = [
    { role: "system", content: "You are a helpful agent." },
    { role: "user", content: userMessage }
  ];
  
  for (let step = 0; step < 10; step++) {
    const response = await client.chat.completions.create({
      model: "gpt-4o-mini",
      messages,
      tools: [...]
    });
    const message = response.choices[0].message;
    messages.push(message);
    
    if (!message.tool_calls || message.tool_calls.length === 0) {
      return message.content;
    }
    // araç çağrılarını çalıştır ve geri besle...
  }
  return "Maksimum adım sayısına ulaşıldı.";
}
```

Tam çalışır örneği: [`examples/javascript/basic_agent.js`](examples/javascript/basic_agent.js)

### 3. Çalıştırın

**Python:**
```bash
cd examples/python/basic_agent
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."
python agent.py
```

**JavaScript:**
```bash
cd examples/javascript
npm install openai dotenv
export OPENAI_API_KEY="sk-..."
node basic_agent.js
```

> ⚠️ `OPENAI_API_KEY` ortam değişkeninizi ayarlamayı unutmayın. API anahtarınızı asla depoya göndermeyin (`.gitignore` zaten `.env` dosyasını hariç tutmaktadır).

---

## 📁 Depo Yapısı

```mermaid
flowchart TD
    root[ai-agents-learning-repo]
    root --> docs[docs/]
    root --> examples[examples/]
    root --> resources[resources/]
    root --> projects[projects/]
    root --> glossary[glossary.md]
    root --> mkdocs[mkdocs.yml]
    root --> ci[.github/workflows/ci.yml]
    root --> license[LICENSE]
    root --> contributing[CONTRIBUTING.md]
    
    docs --> d1[01-introduction]
    docs --> d2[02-how-agents-work]
    docs --> d3[03-architecture]
    docs --> d4[04-capabilities]
    docs --> d5[05-tools]
    docs --> d6[06-memory]
    docs --> d7[07-multi-agent]
    docs --> d8[08-building]
    docs --> d9[09-evaluation]
    docs --> d10[10-deployment]
    docs --> d11[11-best-practices]
    
    examples --> py[python/]
    examples --> js[javascript/]
    py --> basic[basic_agent/]
    py --> web[web_search_agent/]
    
    style root fill:#f9f,stroke:#333,stroke-width:4px
    style docs fill:#e1f5fe,stroke:#01579b
    style examples fill:#e8f5e9,stroke:#2e7d32
    style resources fill:#fff3e0,stroke:#ef6c00
    style projects fill:#f3e5f5,stroke:#7b1fa2
```

---

## 👥 Kimler İçindir?

Bu depo aşağıdaki kişiler için tasarlanmıştır:

- **Yazılım geliştiricileri:** AI ajentleriyle çalışmak için pratik kod örnekleri arıyorsanız.
- **Öğrenciler:** Tabanlı (LLM) sistemler ve ajent mimarileri öğrenmek istiyorsanız.
- **Teknoloji meraklıları:** "Ajent nedir?" sorusunun derinlemesine cevabını arıyorsanız.

**Önkoşul:** Önceki makine öğrenmesi deneyimi **gerekli değildir**. Temel programlama bilgisi (Python veya JavaScript) yeterlidir.

---

## 🤝 Katkıda Bulunma

Katkılarınızı memnuniyetle karşılarız! Düzeltilmesi gereken bir şey, yeni bir örnek veya çevrilen bir belge varsa lütfen bir pull request açın.

1. Bu depoyu fork'layın.
2. Yeni bir dal oluşturun: `git checkout -b iyilestirme-adiniz`
3. Değişikliklerinizi yapın ve commit atın: `git commit -m "feat: ..."`
4. Dalınızı pushlayın: `git push origin iyilestirme-adiniz`
5. Bir pull request açın ve değişikliklerinizi açıklayın.

Detaylı bilgi için [`CONTRIBUTING.md`](CONTRIBUTING.md) dosyasını okuyun.

---

## 📄 Lisans

Bu depo [MIT Lisansı](LICENSE) ile lisanslanmıştır — serbestçe kullanabilir, değiştirebilir ve paylaşabilirsiniz.

---

## 🔗 Faydalı Bağlantılar

- [`resources/free-resources.md`](resources/free-resources.md) — Ücretsiz kitaplar, makaleler, dersler ve araçlar
- [`projects/project-ideas.md`](projects/project-ideas.md) — Pratik yapmak için proje fikirleri
- [`glossary.md`](glossary.md) — Anahtar terimlerin basit açıklamaları

---

*Öğrenenler için oluşturuldu, ücretsiz ve açık tutuldu.*