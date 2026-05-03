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

st.set_page_config(page_title="Kelime Avcısı", layout="centered")

# --- Session State Hazırlığı ---
if 'current_word' not in st.session_state:
    st.session_state.current_word = random.choice(list(words_dict.keys()))
    st.session_state.score = 0
    st.session_state.options = []

def get_new_word():
    st.session_state.current_word = random.choice(list(words_dict.keys()))
    # Çoklu seçim için 4 şık hazırla
    correct = words_dict[st.session_state.current_word]
    others = random.sample([v for k, v in words_dict.items() if v != correct], 3)
    options = others + [correct]
    random.shuffle(options)
    st.session_state.options = options

if not st.session_state.options:
    get_new_word()

# --- Arayüz ---
st.title("🎓 İngilizce Kelime Öğrenme")

mode = st.radio("Çalışma Modu Seçin:", ["Yazarak Tahmin Et", "Çoktan Seçmeli (Test)"], horizontal=True)

st.divider()
st.subheader(f"Kelime: :blue[{st.session_state.current_word}]")

if mode == "Yazarak Tahmin Et":
    user_ans = st.text_input("Türkçe karşılığını yazın:", key="text_input").strip().lower()
    if st.button("Kontrol Et"):
        correct_ans = words_dict[st.session_state.current_word].lower()
        if user_ans and (user_ans in correct_ans or any(user_ans in m.strip() for m in correct_ans.split(','))):
            st.success(f"Harika! Doğru cevap: {words_dict[st.session_state.current_word]}")
            st.session_state.score += 1
        else:
            st.error(f"Hata! Doğru cevap: {words_dict[st.session_state.current_word]}")

else:
    # Çoktan Seçmeli Mod
    choice = st.radio("Doğru anlamı seçin:", st.session_state.options, key="radio_choice")
    if st.button("Cevabı Onayla"):
        if choice == words_dict[st.session_state.current_word]:
            st.success("Tebrikler, doğru şık!")
            st.session_state.score += 1
        else:
            st.error(f"Yanlış! Doğru cevap şuydu: {words_dict[st.session_state.current_word]}")

if st.button("Sonraki Kelime ➡️"):
    get_new_word()
    st.rerun()

# --- Sidebar ---
st.sidebar.title("📈 Başarım")
st.sidebar.metric("Toplam Puan", st.session_state.score)
if st.sidebar.button("Puanı Sıfırla"):
    st.session_state.score = 0
    st.rerun()

st.sidebar.info("Kaynak: WhatsApp Image 2026-05-03 at 20.03.38.jpg")
