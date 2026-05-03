import streamlit as st
import random

# B. Yalçınkaya
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

st.set_page_config(page_title="Kelime Uzmanı", layout="centered")

# --- Başlatma Fonksiyonu ---
def get_new_word():
    # Kalan kelimeleri bul (toplam eksi öğrenilenler)
    remaining_words = [w for w in words_dict.keys() if w not in st.session_state.learned_words]
    
    if not remaining_words:
        st.session_state.all_done = True
        return

    # %60 ihtimalle yanlış yapılanlardan sor (eğer yanlış listesindeyse ve hala öğrenilmediyse)
    wrong_candidates = [w for w in st.session_state.wrong_answers if w in remaining_words]
    
    if wrong_candidates and random.random() < 0.6:
        current = random.choice(wrong_candidates)
    else:
        current = random.choice(remaining_words)
        
    st.session_state.current_word = current
    
    # Şık hazırlama
    correct = words_dict[current]
    others = random.sample([v for k, v in words_dict.items() if v != correct], 3)
    options = others + [correct]
    random.shuffle(options)
    st.session_state.options = options

# --- Session State Kurulumu ---
if 'learned_words' not in st.session_state:
    st.session_state.learned_words = set()
if 'wrong_answers' not in st.session_state:
    st.session_state.wrong_answers = set()
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'all_done' not in st.session_state:
    st.session_state.all_done = False
if 'current_word' not in st.session_state:
    get_new_word()

# --- Arayüz ---
st.title("🏆 Kelime Master")

# TÜM KELİMELER BİTTİĞİNDE GÖSTERİLECEK EKRAN
if st.session_state.all_done:
    st.balloons()
    st.success("🎉 TEBRİKLER! Listedeki tüm kelimeleri başarıyla tamamladın!")
    st.write(f"Final Skorun: **{st.session_state.score}**")
    if st.button("Hepsini Sıfırla ve Yeniden Başla"):
        st.session_state.learned_words = set()
        st.session_state.wrong_answers = set()
        st.session_state.score = 0
        st.session_state.all_done = False
        get_new_word()
        st.rerun()
else:
    # İlerleme Çubuğu
    progress = len(st.session_state.learned_words) / len(words_dict)
    st.progress(progress)
    st.write(f"İlerleme: {len(st.session_state.learned_words)} / {len(words_dict)}")

    mode = st.radio("Mod:", ["Yazma", "Test"], horizontal=True)
    word = st.session_state.current_word
    st.subheader(f"Kelime: :orange[{word}]")

    if mode == "Yazma":
        user_ans = st.text_input("Tahmin:", key="txt").strip().lower()
    else:
        choice = st.radio("Seçiniz:", st.session_state.options, key="radio")

    if st.button("Kontrol Et / Onayla"):
        correct_ans = words_dict[word].lower()
        is_correct = False
        
        if mode == "Yazma":
            if user_ans and any(user_ans in m.strip() for m in correct_ans.split(',')):
                is_correct = True
        else:
            if choice == words_dict[word]:
                is_correct = True
                
        if is_correct:
            st.success(f"Harika! +10 Puan.")
            st.session_state.score += 10
            st.session_state.learned_words.add(word)
            if word in st.session_state.wrong_answers:
                st.session_state.wrong_answers.remove(word)
        else:
            st.error(f"Hata! Doğru cevap: {words_dict[word]}")
            st.session_state.wrong_answers.add(word)

    if st.button("Sonraki Kelime ➡️"):
        get_new_word()
        st.rerun()

# Sidebar Bilgileri
st.sidebar.metric("Puan", st.session_state.score)
st.sidebar.write(f"Öğrenilen: {len(st.session_state.learned_words)}")
st.sidebar.write(f"Zayıf Kelime: {len(st.session_state.wrong_answers)}")
