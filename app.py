import streamlit as st
import random

# WhatsApp Image 2026-05-03 at 20.03.38.jpg içeriğindeki tüm kelimeler ve örnek cümleleri
words_data = {
    "Against": ["karşı, zıt", "Our team played ___ a very difficult opponent last night."],
    "Amazing": ["harika, şaşırtıcı", "The fireworks display at the festival was truly ___."],
    "Animation": ["animasyon", "The new Pixar movie has incredible ___."],
    "Answer": ["cevap vermek", "Please write your ___ on the piece of paper."],
    "Aquarium": ["akvaryum", "We saw many colorful fish at the local ___."],
    "Assignment": ["ödev, görev", "I need to submit my science ___ by Friday."],
    "Author": ["yazar", "Who is the ___ of this interesting novel?"],
    "Be": ["olmak", "I want to ___ a genetic engineer in the future."],
    "Bed": ["yatak", "It is late, you should go to ___ now."],
    "Behind": ["arkasında", "The cat is hiding ___ the blue sofa."],
    "Between": ["arasında", "The library is located ___ the bank and the cafe."],
    "Bookcase": ["kitaplık", "He organized all his science books on the ___."],
    "Bookshelf": ["kitap rafı", "There is a small plant sitting on the top ___."],
    "Bookshop": ["kitap dükkanı", "I bought this dictionary from the ___ downtown."],
    "Bookworm": ["kitap kurdu", "She reads three books a week; she is a real ___."],
    "Borrow": ["ödünç almak", "Could I ___ your laptop for a few hours?"],
    "Box": "kutu", # Kısa tanımlar için otomatik cümle oluşturucu eklenebilir
    "Boy": ["erkek çocuk", "The ___ is playing football in the garden."],
    "Break": ["kırmak", "Be careful with that glass, don't ___ it!"],
    "Buy": ["satın almak", "I want to ___ a new computer for my research."],
    "Call": ["aramak", "Don't forget to ___ your mother tonight."],
    "Carpet": ["halı", "We have a soft grey ___ in our living room."],
    "Classmate": ["sınıf arkadaşı", "Kerem is my favorite ___ at school."],
    "Clock": ["saat", "Look at the ___ on the wall; it is already 10 PM."],
    "Coffee table": ["kahve masası", "Put your cup of tea on the ___."],
    "Come": ["gelmek", "Please ___ inside and have a seat."],
    "Come back": ["geri dönmek", "What time will you ___ from the museum?"],
    "Computer": ["bilgisayar", "I use my ___ to write Python scripts."],
    "Conversation": ["sohbet", "I had a very long ___ with my spouse today."],
    "Court": ["saha, alan", "The players are waiting on the tennis ___."],
    "Darkness": ["karanlık", "The cat can see very well in total ___."],
    "Dictionary": ["sözlük", "If you don't know the word, look it up in the ___."],
    "Different": ["farklı", "These two DNA samples belong to ___ organisms."],
    "Difficult": ["zor", "This math problem is very ___, I need help."],
    "Do homework": ["ödev yapmak", "I usually ___ right after school."],
    "Door": ["kapı", "Please close the ___ behind you."],
    "Draw": ["çizmek", "Can you ___ a picture of a fox?"],
    "Drawer": ["çekmece", "Your socks are in the top ___ of the dresser."],
    "E-book": ["elektronik kitap", "I prefer reading an ___ on my tablet."],
    "Enlighten": ["aydınlatmak", "Could you ___ me about your new project?"],
    "Fall": ["düşmek", "Be careful on the ice, you might ___."],
    "Feel": ["hissetmek", "I ___ very happy today because the weather is nice."],
    "Find": ["bulmak", "I can't ___ my keys, have you seen them?"],
    "Fireplace": ["ocak, şömine", "We sat near the ___ to stay warm."],
    "Fox": ["tilki", "The ___ is a very clever animal."],
    "Friend": ["arkadaş", "A true ___ always helps you in difficult times."],
    "Geography": ["coğrafya", "We studied the map of Australia in ___."],
    "Get up": ["uyanmak", "What time do you usually ___ in the morning?"],
    "Girl": ["kız", "The little ___ is drawing a flower."],
    "Give": ["vermek", "Can you ___ me that book, please?"],
    "Give up": ["pes etmek", "Never ___ on your dreams."],
    "Have": ["sahip olmak", "I ___ a very important meeting at 9 AM."],
    "Hear": ["duymak", "Did you ___ that strange noise outside?"],
    "Help": ["yardım etmek", "Can you ___ me with this heavy box?"],
    "History": ["tarih", "I love learning about ancient Roman ___."],
    "Home / House": ["ev", "I am going ___ to rest after work."],
    "Homework": ["ev ödevi", "I finished my English ___ an hour ago."],
    "Hour": ["saat", "There are sixty minutes in one ___."],
    "Houseplant": ["saksı çiçeği", "I forgot to water my ___ this week."],
    "How many": ["kaç tane", "___ students are there in the classroom?"],
    "How often": ["ne sıklıkla", "___ do you go to the gym?"],
    "Hurt": ["incitmek, incinmek", "Stop! You are going to ___ yourself."],
    "Ice skating": ["buz pateni", "We went ___ at the mall last winter."],
    "Important": ["önemli", "This is a very ___ document for my research."],
    "In": ["içinde", "The keys are ___ my pocket."],
    "In front of": ["önünde", "Wait for me ___ the shopping center."],
    "Information": ["bilgi", "I need more ___ about this project."],
    "Interesting": ["ilginç", "This is a very ___ discovery in genetics."],
    "Invite": ["davet etmek", "I want to ___ my friends to my birthday party."],
    "Keyboard": ["klavye", "I need a new ___ for my computer."],
    "Kind": ["çeşit", "What ___ of music do you like?"],
    "Kiosk": ["büfe", "I bought a newspaper from the ___."],
    "Kitten": ["kedi yavrusu", "The ___ is playing with a ball of yarn."],
    "Know": ["bilmek", "Do you ___ the answer to this question?"],
    "Lamp": ["lamba", "It is dark, please turn on the ___."],
    "Laptop": ["dizüstü bilgisayar", "I take my ___ to the office every day."],
    "Lend": ["ödünç vermek", "Can you ___ me your dictionary?"],
    "Let": ["izin vermek", "Please ___ me go to the party."],
    "Library": ["kütüphane", "I am going to the ___ to study."],
    "Literature": ["edebiyat", "She is a professor of English ___."],
    "Location": ["yer, konum", "Please send me your ___ on WhatsApp."],
    "Look": ["bakmak", "___ at that beautiful sunset!"],
    "Look for": ["aramak", "I am going to ___ my lost wallet."],
    "Look up": ["araştırmak", "You should ___ the word in a dictionary."],
    "Lose": ["kaybetmek", "Don't ___ your passport during the trip."],
    "Magazine": ["dergi", "I read a fashion ___ at the doctor's office."],
    "Make": ["yapmak", "Can you ___ some coffee for us?"],
    "Man": ["adam", "The ___ in the suit is our new manager."],
    "Many times": ["çok kez", "I have visited Sydney ___ in the past."],
    "Match": ["eşleştirmek", "Please ___ the words with their meanings."],
    "Meaning": ["anlam", "What is the ___ of this word?"],
    "Meet": ["buluşmak", "Let's ___ at the park at 5 PM."],
    "Museum": ["müze", "The Louvre is a very famous ___ in Paris."],
    "Near": ["yanında", "The bus stop is ___ my house."],
    "New": ["yeni", "I bought a ___ car last month."],
    "Newspaper": ["gazete", "My father reads the ___ every morning."],
    "Next to": ["bitişiğinde", "The pharmacy is right ___ the hospital."],
    "Novel": ["roman", "This is a very long and boring ___."],
    "Novelist": ["roman yazarı", "Orhan Pamuk is a famous Turkish ___."],
    "Object": ["nesne, eşya", "There is a strange ___ in the sky."],
    "Old": ["eski", "My grandfather lives in an ___ house."],
    "On": ["üstünde", "The book is ___ the table."],
    "Opinion": ["fikir", "In my ___, this is a great idea."],
    "Opposite": ["karşısında", "The park is ___ the school."],
    "Over": ["üzerinde", "The bridge goes ___ the river."],
    "Painting": ["resim, tablo", "That is a beautiful ___ on the wall."],
    "People": ["insanlar", "There are many ___ at the airport."],
    "Picture": ["resim", "Can I take a ___ of you?"],
    "Place": ["yer", "Sydney is a beautiful ___ to visit."],
    "Poetry": ["şairlik", "I love reading Turkish ___."],
    "Prepare": ["hazırlamak", "I need to ___ for my exam."],
    "Present": ["hediye", "I bought a ___ for my child's birthday."],
    "Puppy": ["köpek yavrusu", "The ___ is barking at the mailman."],
    "Read": ["okumak", "I like to ___ books before I sleep."],
    "Real": ["gerçek", "Is this a ___ diamond or a fake one?"],
    "Science": ["bilim", "Genetic engineering is a very exciting field of ___."],
    "Search": ["araştırmak", "I will ___ for the information online."],
    "Share": ["paylaşmak", "Please ___ your notes with me."],
    "Shopping center": ["alışveriş merkezi", "We spent all afternoon at the ___."],
    "Short story": ["kısa hikaye", "I wrote a ___ for the competition."],
    "Show": ["göstermek", "Can you ___ me the way to the library?"],
    "Sing": ["şarkı söylemek", "I like to ___ in the shower."],
    "Skates": ["patenler", "I need to buy new ___ for the winter."],
    "Sofa": ["kanepe", "The ___ in the living room is very comfortable."],
    "Someone": ["birileri", "___ is knocking at the door."],
    "Something": ["bir şeyler", "I want to eat ___ sweet."],
    "Star": ["yıldız", "Look at the bright ___ in the sky."],
    "Story": ["hikaye", "Tell me a ___ before I go to sleep."],
    "Story writer": ["hikaye yazarı", "He is a famous ___ for children."],
    "Take": ["almak, götürmek", "Don't forget to ___ your umbrella."],
    "Teddy bear": ["oyuncak ayı", "The child is sleeping with her ___."],
    "Theatre": ["tiyatro", "We are going to the ___ tonight."],
    "Then": ["sonra", "First eat your dinner, ___ you can have dessert."],
    "Toy bus": ["oyuncak otobüs", "The boy is playing with his red ___."],
    "Trousers": ["pantolon", "I need to wash my blue ___."],
    "Under": ["altında", "The ball is ___ the chair."],
    "Walk": ["yürümek", "I like to ___ in the park every evening."],
    "Watch": ["izlemek", "Let's ___ a movie tonight."],
    "Wall": ["duvar", "There is a large clock on the ___."],
    "Want": ["istemek", "I ___ to travel to Australia next month."],
    "What about you?": ["peki ya sen?", "I am fine, ___?"],
    "Word": ["kelime", "I don't know the meaning of this ___."],
    "Write": ["yazmak", "Please ___ your name on the paper."],
    "Year": ["yıl", "There are twelve months in a ___."]
}

st.set_page_config(page_title="Cloze Test Master", layout="centered")

# --- Fonksiyonlar ---
def get_new_question():
    remaining = [w for w in words_data.keys() if w not in st.session_state.learned_words]
    
    if not remaining:
        st.session_state.all_done = True
        return

    # Yanlış yapılanlara öncelik ver
    wrong_candidates = [w for w in st.session_state.wrong_answers if w in remaining]
    if wrong_candidates and random.random() < 0.5:
        current = random.choice(wrong_candidates)
    else:
        current = random.choice(remaining)
        
    st.session_state.current_word = current
    
    # Şık hazırlama
    correct = current
    all_keys = list(words_data.keys())
    others = random.sample([k for k in all_keys if k != correct], 3)
    options = others + [correct]
    random.shuffle(options)
    st.session_state.options = options
    st.session_state.answered = False

# --- Session State ---
if 'learned_words' not in st.session_state:
    st.session_state.learned_words = set()
if 'wrong_answers' not in st.session_state:
    st.session_state.wrong_answers = set()
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'all_done' not in st.session_state:
    st.session_state.all_done = False
if 'current_word' not in st.session_state:
    get_new_question()

# --- Arayüz ---
st.title("📖 Cümle İçinde Kelime Ezberleme")
st.write("Görseldeki tüm kelimelerle hazırlanan akıllı çalışma sistemi.")

if st.session_state.all_done:
    st.balloons()
    st.success("🎉 İnanılmaz! 130+ kelimenin tamamını cümle içinde öğrendin!")
    st.write(f"Final Skorunuz: **{st.session_state.score}**")
    if st.button("Sıfırla ve Baştan Başla"):
        st.session_state.learned_words = set()
        st.session_state.wrong_answers = set()
        st.session_state.score = 0
        st.session_state.all_done = False
        get_new_question()
        st.rerun()
else:
    # İlerleme
    total = len(words_data)
    current_count = len(st.session_state.learned_words)
    st.progress(current_count / total)
    st.caption(f"İlerleme: {current_count} / {total} kelime tamamlandı.")

    word = st.session_state.current_word
    meaning = words_data[word][0]
    sentence = words_data[word][1]

    st.info(f"💡 **Anlamı:** {meaning}")
    st.markdown(f"### Cümle: \n > {sentence}")

    # Çoktan Seçmeli
    choice = st.radio("Boşluğa hangisi gelmeli?", st.session_state.options, index=None, key="choice_radio")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Cevabı Onayla", use_container_width=True):
            if choice == word:
                st.success(f"Harika! +20 Puan. \nCümle: {sentence.replace('___', '**'+word+'**')}")
                st.session_state.score += 20
                st.session_state.learned_words.add(word)
                if word in st.session_state.wrong_answers:
                    st.session_state.wrong_answers.remove(word)
                st.session_state.answered = True
            else:
                st.error(f"Yanlış! Doğru cevap: **{word}**")
                st.session_state.wrong_answers.add(word)
                st.session_state.score -= 5

    with col2:
        if st.button("Sıradaki Kelime ➡️", use_container_width=True):
            get_new_question()
            st.rerun()

# --- Skor Tablosu ---
st.sidebar.metric("Skorun", st.session_state.score)
st.sidebar.write(f"Zayıf Kelime Sayısı: {len(st.session_state.wrong_answers)}")
if st.sidebar.button("İlerlemeyi Sıfırla"):
    st.session_state.learned_words = set()
    st.session_state.score = 0
    st.rerun()
