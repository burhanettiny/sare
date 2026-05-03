import streamlit as st
import random

# WhatsApp Image 2026-05-03 at 20.03.38.jpg dosyasındaki tüm kelimeler
words_dict = {
    # A - B
    "Against": "karşı, zıt", "Amazing": "harika, şaşırtıcı", "Animation": "animasyon", 
    "Answer": "cevap vermek", "Aquarium": "akvaryum", "Assignment": "ödev, görev", 
    "Author": "yazar", "Be": "olmak", "Bed": "yatak", "Behind": "arkasında", 
    "Between": "arasında", "Bookcase": "kitaplık", "Bookshelf": "kitap rafı", 
    "Bookshop": "kitap dükkanı", "Bookworm": "kitap kurdu", "Borrow": "ödünç almak", 
    "Box": "kutu", "Boy": "erkek çocuk", "Break": "kırmak", "Buy": "satın almak",
    # C - D
    "Call": "aramak", "Carpet": "halı", "Classmate": "sınıf arkadaşı", "Clock": "saat", 
    "Coffee table": "kahve masası", "Come": "gelmek", "Come back": "geri dönmek", 
    "Computer": "bilgisayar", "Conversation": "sohbet", "Court": "saha, alan", 
    "Darkness": "karanlık", "Dictionary": "sözlük", "Different": "farklı", 
    "Difficult": "zor", "Do homework": "ödev yapmak", "Door": "kapı", 
    "Draw": "çizmek", "Drawer": "çekmece",
    # E - F - G
    "E-book": "elektronik kitap", "Enlighten": "aydınlatmak", "Fall": "düşmek", 
    "Feel": "hissetmek", "Find": "bulmak", "Fireplace": "ocak, şömine", "Fox": "tilki", 
    "Friend": "arkadaş", "Geography": "coğrafya", "Get up": "uyanmak", "Girl": "kız",
    # G (devam) - H
    "Give": "vermek", "Give up": "pes etmek", "Have": "sahip olmak", "Hear": "duymak", 
    "Help": "yardım etmek", "History": "tarih", "Home / House": "ev", 
    "Homework": "ev ödevi", "Hour": "saat", "Houseplant": "saksı çiçeği", 
    "How many": "kaç tane", "How often": "ne sıklıkla", "Hurt": "incitmek, incinmek",
    # I - K
    "Ice skating": "buz pateni", "Important": "önemli", "In": "içinde", 
    "In front of": "önünde", "Information": "bilgi", "Interesting": "ilginç", 
    "Invite": "davet etmek", "Keyboard": "klavye", "Kind": "çeşit", "Kiosk": "büfe", 
    "Kitten": "kedi yavrusu", "Know": "bilmek",
    # L - M
    "Lamp": "lamba", "Laptop": "dizüstü bilgisayar", "Lend": "ödünç vermek", 
    "Let": "izin vermek", "Library": "kütüphane", "Literature": "edebiyat", 
    "Location": "yer, konum", "Look": "bakmak", "Look for": "aramak", 
    "Look up": "araştırmak", "Lose": "kaybetmek", "Magazine": "dergi", 
    "Make": "yapmak", "Man": "adam", "Many times": "çok kez", "Match": "eşleştirmek", 
    "Meaning": "anlam", "Meet": "buluşmak", "Museum": "müze",
    # N - O - P
    "Near": "yanında", "New": "yeni", "Newspaper": "gazete", "Next to": "bitişiğinde", 
    "Novel": "roman", "Novelist": "roman yazarı", "Object": "nesne, eşya", 
    "Old": "eski", "On": "üstünde", "Opinion": "fikir", "Opposite": "karşısında", 
    "Over": "üzerinde", "Painting": "resim, tablo", "People": "insanlar", 
    "Picture": "resim", "Place": "yer", "Poetry": "şairlik", "Prepare": "hazırlamak", 
    "Present": "hediye", "Puppy": "köpek yavrusu",
    # R - S
    "Read": "okumak", "Real": "gerçek", "Science": "bilim", "Search": "araştırmak", 
    "Share": "paylaşmak", "Shopping center": "alışveriş merkezi", 
    "Short story": "kısa hikaye", "Show": "göstermek", "Sing": "şarkı söylemek", 
    "Skates": "patenler", "Sofa": "kanepe", "Someone": "birileri", 
    "Something": "bir şeyler", "Star": "yıldız", "Story": "hikaye", 
    "Story writer": "hikaye yazarı",
    # T - Y
    "Take": "almak, götürmek", "Teddy bear": "oyuncak ayı", "Theatre": "tiyatro", 
    "Then": "sonra", "Toy bus": "oyuncak otobüs", "Trousers": "pantolon", 
    "Under": "altında", "Walk": "yürümek", "Watch": "izlemek", "Wall": "duvar", 
    "Want": "istemek", "What about you?": "peki ya sen?", "Word": "kelime", 
    "Write": "yazmak", "Year": "yıl"
}

st.set_page_config(page_title="Kelime Öğren", page_icon="📖")

# Uygulama Başlığı
st.title("🔤 Kelime Ezberleme Uygulaması")
st.write(f"Listedeki toplam kelime sayısı: **{len(words_dict)}**")

# Hafıza Yönetimi
if 'current_word' not in st.session_state:
    st.session_state.current_word = random.choice(list(words_dict.keys()))
    st.session_state.score = 0
    st.session_state.attempts = 0

def next_word():
    st.session_state.current_word = random.choice(list(words_dict.keys()))
    st.session_state.feedback = ""

# Arayüz
st.divider()
st.subheader("Bu kelimenin anlamı nedir?")
st.header(f":orange[{st.session_state.current_word}]")

user_input = st.text_input("Türkçe karşılığını yazın:", placeholder="Buraya yazın...", key="user_input").strip()

col1, col2 = st.columns(2)

with col1:
    if st.button("✅ Kontrol Et", use_container_width=True):
        st.session_state.attempts += 1
        correct_ans = words_dict[st.session_state.current_word].lower()
        
        # Basit bir kontrol algoritması (virgüllü anlamlardan birini bilse yeterli)
        meanings = [m.strip().lower() for m in correct_ans.replace(',', ';').split(';')]
        
        if user_input.lower() in meanings or any(user_input.lower() in m for m in meanings):
            st.success(f"Doğru! Cevap: {words_dict[st.session_state.current_word]}")
            st.session_state.score += 1
        else:
            st.error(f"Yanlış! Doğru cevap: {words_dict[st.session_state.current_word]}")

with col2:
    if st.button("➡️ Sıradaki Kelime", use_container_width=True):
        next_word()
        st.rerun()

# İstatistikler
st.sidebar.title("İstatistikler")
st.sidebar.metric("Doğru Sayısı", st.session_state.score)
st.sidebar.metric("Toplam Deneme", st.session_state.attempts)

if st.sidebar.button("Skoru Sıfırla"):
    st.session_state.score = 0
    st.session_state.attempts = 0
    st.rerun()

st.sidebar.divider()
st.sidebar.write("Kaynak: WhatsApp Image 2026-05-03 at 20.03.38.jpg")
