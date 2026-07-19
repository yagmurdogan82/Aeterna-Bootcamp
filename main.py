from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

def test_ollama_connection():
    print("Aeterna Dijital İkiz Sistemi Başlatılıyor...")
    
    try:
        # Güncel kütüphane ve dili toparlaması için düşük temperature değeri (0.1) ekledik
        llm = OllamaLLM(model="llama3.2", temperature=0.1)
        
        # Modeli SADECE Türkçe konuşmaya zorlayan daha katı bir prompt şablonu
        template = """
        Sen Aeterna adında, kullanıcısına yardımcı olan zeki bir profesyonel asistan ve dijital ikizsin.
        Kural: Aşağıdaki soruya SADECE Türkçe olarak, dil bilgisi kurallarına tam uyarak, net ve doğal bir dille yanıt ver. Kesinlikle başka bir dil veya yabancı kelime kullanma.
        
        Soru: {soru}
        Yanıt:"""
        
        prompt = PromptTemplate(template=template, input_variables=["soru"])
        
        chain = prompt | llm
        
        print("\nModel Yüklendi. Test Sorusu Soruluyor...")
        
        test_sorusu = "Merhaba Aeterna, nasılsın? Bootcamp projesi için hazır mısın?"
        print(f"Kullanıcı: {test_sorusu}")
        
        # Yanıtı alıyoruz
        yanit = chain.invoke({"soru": test_sorusu})
        print(f"\nAeterna: {yanit}")
        print("\n✅ Test Başarılı! Bağlantı sağlandı ve güncel kütüphane kullanıldı.")
        
    except Exception as e:
        print(f"\n❌ Bir hata oluştu: {e}")

if __name__ == "__main__":
    test_ollama_connection()