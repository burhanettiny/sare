import streamlit as st
import random

# Veri seti: WhatsApp Image 2026-05-03 at 20.03.38.jpg içeriği
words_dict = {
    "Against": "karşı, zıt", "Amazing": "harika, şaşırtıcı", "Animation": "animasyon", 
    "Answer": "cevap vermek", "Aquarium": "akvaryum", "Assignment": "ödev, görev", 
    "Author": "yazar", "Be": "olmak", "Bed": "yatak", "Behind": "arkasında", 
    "Between": "arasında", "Bookcase": "kitaplık", "Bookshelf": "kitap rafı", 
    "Bookshop": "kitap dükkanı", "Bookworm": "kitap kurdu", "Borrow": "ödünç almak", 
    "Box": "kutu", "Boy": "erkek çocuk", "Break": "kırmak", "Buy": "satın almak",
    "Call": "aramak", "Carpet": "halı", "Classmate": "sınıf arkadaşı", "Clock": "saat", 
    "Coffee table": "kahve masası", "Come": "gelmek", "Come back": "geri dönmek", 
    "Computer": "bilgisayar", "Conversation": "sohbet", "Court": "saha, alan", 
    "Darkness": "karanlık", "Dictionary": "sözlük", "Different": "farklı", 
    "Difficult": "zor", "Do homework": "ödev yapmak", "Door": "kapı", 
    "Draw": "çizmek", "Drawer": "çekmece", "E-book": "elektronik kitap", 
    "Enlighten": "aydınlatmak", "Fall": "düşmek", "Feel": "hissetmek", "Find": "bulmak", 
    "Fireplace": "ocak, şömine", "Fox": "tilki", "Friend": "arkadaş", "Geography": "coğrafya", 
    "Get up": "uyanmak", "Girl": "kız", "Give": "vermek", "Give up": "pes etmek", 
    "Have": "sahip olmak", "Hear": "duymak", "Help": "yardım etmek", "History": "tarih", 
    "Home / House": "ev", "Homework": "ev ödevi", "Hour": "saat", "Houseplant": "saksı çiçeği", 
    "How many": "kaç tane", "How often": "ne sıklıkla", "Hurt": "incitmek, incinmek",
    "Ice skating": "buz pateni", "Important": "önemli", "In": "içinde", 
    "In front of": "önünde", "Information": "bilgi", "Interesting": "ilginç", 
    "Invite": "davet etmek", "Keyboard": "klavye", "Kind": "çeşit", "Kiosk": "büfe", 
    "Kitten": "kedi yavrusu", "Know": "bilmek", "Lamp": "lamba", 
    "Laptop": "dizüstü bilgisayar", "Lend": "ödünç vermek", "Let": "izin vermek", 
    "Library": "kütüphane", "Literature": "edebiyat", "Location": "yer, konum", 
    "Look": "bakmak", "Look for": "aramak", "Look up": "araştırmak", "Lose": "kaybetmek", 
    "Magazine": "dergi", "Make": "yapmak", "Man": "adam", "Many times": "çok kez", 
    "Match": "eşleştirmek", "Meaning": "anlam", "Meet": "buluşmak", "Museum": "müze",
    "Near": "yanında", "New": "yeni", "Newspaper": "gazete", "Next to": "bitişiğinde", 
    "Novel": "roman", "Novelist": "roman yazarı", "Object": "nesne, eşya", 
    "Old": "eski", "On": "üstünde", "Opinion": "fikir", "Opposite": "karşısında", 
    "Over": "üzerinde", "Painting": "resim, tablo", "People": "insanlar", 
    "Picture": "resim", "Place": "yer", "Poetry": "şairlik", "Prepare": "hazırlamak", 
    "Present": "hediye", "Puppy": "köpek yavrusu", "Read": "okumak", "Real": "gerçek", 
    "Science": "bilim", "Search": "araştırmak", "Share": "paylaşmak", 
    "Shopping center": "alışveriş merkezi", "Short story": "kısa hikaye", 
    "Show": "göstermek", "Sing": "şarkı söylemek", "Skates": "patenler", "Sofa": "kanepe", 
    "Someone": "birileri", "Something": "bir şeyler", "Star": "yıldız", "Story": "hikaye", 
    "Story writer": "hikaye yazarı", "Take": "almak, götürmek", "Teddy bear": "oyuncak ayı", 
    "Theatre": "tiyatro", "Then": "sonra", "Toy bus": "oyuncak otobüs", "Trousers": "pantolon", 
    "Under": "altında", "Walk": "yürümek", "Watch": "izlemek", "Wall": "duvar", 
    "Want": "istemek", "What about you?": "peki ya sen?", "Word": "kelime", 
    "Write": "yazmak", "Year": "yıl"
}

st.set_page_config(page_title="Kelime Ezber", layout="centered")

# --- Başlatma Fonksiyonu ---
def get_new_word():
    # Mevcut kelimeyi rastgele seç
    current = random.choice(list(words_dict.keys()))
    st.session_state.current_word = current
    
    # Şıkları oluştur
    correct = words_dict[current]
    # Yanlış şıklar için diğer tüm anlamları al
    all_meanings = [v for k, v in words_dict.items() if v != correct]
    others = random.sample(all_meanings, 3)
    
    options = others + [correct]
    random.shuffle(options)
    st.session_state.options = options

# --- Session State İlk Kurulum ---
if 'current_word' not in st.session_state or 'options' not in st.session_state:
    get_new_word()

if 'score' not in st.session_state:
    st.session_state.score = 0

# --- Arayüz ---
st.title("📚 İngilizce Kelime Hazinesi")

# Mod seçimi
mode = st.radio("Bir çalışma yöntemi seçin:", ["Yazma Modu", "Test Modu"], horizontal=True)

st.divider()

# Kelime Gösterimi (Güvenli erişim için .get kullanıyoruz)
word = st.session_state.get('current_word', 'Bekleniyor...')
st.subheader(f"Kelime: :blue[{word}]")

if mode == "Yazma Modu":
    user_ans = st.text_input("Türkçe anlamını yazın:", key="text_input").strip().lower()
    if st.button("Kontrol Et"):
        correct_ans = words_dict[word].lower()
        # Virgüllü anlamların herhangi birini içeriyor mu kontrolü
        if user_ans and any(user_ans in m.strip() for m in correct_ans.split(',')):
            st.success(f"Harika! ✅ Doğru cevap: {words_dict[word]}")
            st.session_state.score += 1
        else:
            st.error(f"Maalesef... ❌ Doğru cevap: {words_dict[word]}")

else:
    # Test Modu - Güvenli Liste Erişimi
    current_options = st.session_state.get('options', [])
    
    if current_options:
        choice = st.radio("Hangi seçenek doğru?", current_options)
        if st.button("Seçimi Onayla"):
            if choice == words_dict[word]:
                st.success("Tebrikler! Doğru şık. 🎉")
                st.session_state.score += 1
            else:
                st.error(f"Yanlış! Doğru cevap şuydu: {words_dict[word]}")
    else:
        st.warning("Seçenekler yüklenemedi. Lütfen 'Sıradaki Kelime'ye basın.")

# Sayfa sonu butonları
if st.button("Sıradaki Kelime ➡️"):
    get_new_word()
    st.rerun()

# Kenar Çubuğu
st.sidebar.metric("Toplam Puan", st.session_state.score)
if st.sidebar.button("Puanı Sıfırla"):
    st.session_state.score = 0
    st.rerun()
st.sidebar.write("---")
st.sidebar.caption("WhatsApp Image 2026-05-03 at 20.03.38.jpg")
