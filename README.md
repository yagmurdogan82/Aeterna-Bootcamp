# Aeterna: Otonom Dijital İkiz ve Simülasyon Ajanı 🧠🤖

Aeterna, kişisel verileri, geçmiş konuşma kayıtlarını ve özel dokümanları kullanarak belirli bir kişinin veya kurumun "dijital kopyasını" oluşturan, RAG (Retrieval-Augmented Generation) tabanlı interaktif bir yapay zeka ajanıdır. Otonom ajanlar sayesinde yalnızca soru cevaplamakla kalmaz, aynı zamanda kullanıcının geçmiş bağlamını hafızasında tutarak doğal ve sürekli bir iletişim simülasyonu sunar.

## 👥 Takım Bilgileri
**Takım İsmi:** Takım Aeterna  
**Üyeler ve Roller:**
* **Yağmur:** Product Owner, Scrum Master, Developer

## 🚀 Ürün Özellikleri
* **Gizlilik Odaklı Local RAG:** Yerel verilerle çalışan, dışa kapalı ve güvenli bilgi geri çağırma sistemi.
* **Ajan Orkestrasyonu:** LangChain altyapısı ile yönetilen, farklı görevleri yerine getirebilen otonom ajanlar.
* **Hafıza (Memory) Yönetimi:** Kullanıcı ile yapılan önceki etkileşimleri saklayan ve bağlamı koruyan konuşma geçmişi.
* **Semantik Arama:** ChromaDB vektör veritabanı üzerinden hızlı ve anlamsal doküman sorgulama.
* **Akıcı Arayüz:** Streamlit kullanılarak geliştirilmiş, etkileşimli ve kullanıcı dostu web arayüzü.

## 🛠 Teknoloji Yığını (Tech Stack)
* **Dil:** Python
* **LLM Orkestrasyonu:** LangChain
* **Vektör Veritabanı:** ChromaDB
* **Yerel Model Yönetimi:** Ollama (Llama 3.2 vb. modeller)
* **Arayüz:** Streamlit
* **Donanım Optimizasyonu:** Apple Silicon (M4 / 24GB RAM) mimarisi üzerinde MPS (Metal Performance Shaders) ile ivmelendirilmiş yerel çıkarım.

## 🎯 Hedef Kitle
* Mülakat simülasyonu yapmak isteyen İK departmanları.
* Önemli şahsiyetlerin veya uzmanların bilgi birikimini korumak isteyen eğitim kurumları.
* Kendi dijital arşivini ve asistanını yaratmak isteyen teknoloji meraklıları ve araştırmacılar.

## 📊 Proje Yönetimi
* **Product Backlog & Sprint Board:** [Buraya Kanban Board (Trello/Miro/GitHub Projects) Linki Gelecek]
* **Daily Scrum Notları:** [Sprint klasörleri içerisindeki dökümanlara veya wiki'ye link eklenecek]

---

## SPRINT 1

* **Sprint içi puan değerlendirmesi:** 10 olarak belirlenmiştir.
* **Puan tamamlama mantığı:** Proje boyunca tamamlanması gereken toplam backlog puanı 30'dur. Temel altyapı kurulumu ve ilk RAG testlerini kapsayan Sprint 1 için bitirilmesi hedeflenen puan sayısı 10 olarak belirlenmiş ve hedeflenen işlere başlanmıştır.
* **Daily Scrum:** Ekip tek kişiden (Yağmur) oluştuğu için Daily Scrum süreçleri metin bazlı olarak kendi kendine raporlama ("Dün ne yaptım?", "Bugün ne yapacağım?", "Önümde bir engel var mı?") formatında yürütülmektedir. 

[Sprint 1 Daily Scrum Notları ve Ekran Görüntüleri](buraya-klasor-linki-gelecek)

* **Geliştirme Mantığı ve Backlog:** Takımda Product Owner, Scrum Master ve Developer rolleri tek kişi tarafından üstlenilmiştir. İlk sprint tamamen araştırma, geliştirme ortamının kurulması (GitHub, ortam değişkenleri) ve yapay zeka modellerinin yerel donanımda (Ollama & ChromaDB) ayağa kaldırılması üzerine kurgulanmıştır.
  * **Story 1:** Proje yönetim ve versiyon kontrol araçlarının kurulumu.
  * **Story 2:** Yerel model (Llama 3.2) entegrasyonu ve Apple Silicon donanım ivmelendirmesiyle performans testlerinin yapılması.

* **Sprint 1 board update:** Sprint Board Screenshot:

![Sprint 1 Board](buraya-kanban-board-ekran-goruntusu-linki-gelecek.png)
