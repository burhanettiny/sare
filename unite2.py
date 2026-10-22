import random
from io import BytesIO

import streamlit as st

st.set_page_config(page_title="Unit 2: Sports – Kelime Oyunu", page_icon="⚽", layout="centered")

# ---------------------------------------------------------------------------
# KELİMELER (7. sınıf 2. Ünite – defter görsellerinden)
# Biçim: "İngilizce": ("Türkçe", "Boşluklu örnek cümle")
# ---------------------------------------------------------------------------
WORDS = {
    "🏟️ Sporlar ve Sporcular": {
        "Sport": ("spor", "Football is the most popular ___ in Turkey."),
        "Indoor sports": ("kapalı alan sporları", "Basketball and volleyball are ___ because we play them in a hall."),
        "Outdoor sports": ("açık alan sporları", "Skiing and surfing are ___ because we do them outside."),
        "Team sports": ("takım sporları", "Football and volleyball are ___."),
        "Team game": ("takım oyunu", "Basketball is a ___; you need five players."),
        "Individual sports": ("bireysel sporlar", "Swimming and running are ___; you do them alone."),
        "Gym": ("spor salonu", "My brother works out at the ___ three times a week."),
        "Player": ("oyuncu", "Arda Güler is a famous football ___."),
        "Spectator": ("seyirci, izleyici", "Every ___ in the stadium was cheering for the team."),
        "Opponent": ("karşı taraf, rakip", "Our team will play against a strong ___ on Sunday."),
        "Athlete": ("atlet, sporcu", "The ___ won a gold medal in the 100-metre race."),
        "Swimmer": ("yüzücü", "Michael Phelps is a very famous ___."),
        "Swimming pool": ("yüzme havuzu", "We swim in the ___ every summer."),
        "Field": ("saha (futbol sahası)", "The football players are running on the ___."),
        "Court": ("saha (tenis/basketbol sahası)", "They are playing tennis on the ___."),
        "Cycling": ("bisiklet sürme", "___ is my favourite outdoor activity; I ride my bike every weekend."),
    },
    "🏄 Spor Aktiviteleri": {
        "Surfing": ("sörf yapma", "We went ___ in the sea last summer."),
        "Skiing": ("kayak yapma", "We go ___ on Uludağ every winter."),
        "Skating": ("patenle kayma", "My sister loves ___ in the park with her roller skates."),
        "Ice skating": ("buz pateni yapma", "We went ___ at the ice rink last weekend."),
        "Doing judo": ("judo yapma", "___ makes you strong and disciplined."),
        "Jogging": ("tempolu yürüyüş, koşu", "My father goes ___ in the park every morning."),
        "Go running": ("koşuya gitmek, koşuya çıkmak", "I ___ with my dad every Sunday morning."),
        "Go swimming": ("yüzmeye gitmek", "In summer, we ___ in the sea."),
        "Breaststroke": ("kurbağalama yüzüş", "In ___, you move your arms and legs like a frog."),
        "Freestyle": ("serbest stil", "___ is the fastest swimming style."),
        "Run": ("koşmak", "I can ___ very fast."),
        "Train": ("antrenman yapmak", "Footballers ___ hard before an important match."),
        "Work out": ("egzersiz yapmak", "I ___ at the gym three times a week."),
        "Do heavy exercises": ("ağır egzersizler yapmak", "Don't ___ right after a big meal."),
        "Work with the weights": ("ağırlıklarla çalışmak", "Bodybuilders ___ to build big muscles."),
        "Join a sports activity": ("bir spor aktivitesine katılmak", "I want to ___ at school this year."),
        "Compete in the races": ("yarışlarda yarışmak", "Athletes ___ at the Olympic Games."),
    },
    "🥗 Sağlıklı Yaşam ve Rutinler": {
        "Daily activities": ("günlük aktiviteler", "Brushing my teeth and having breakfast are my ___."),
        "Weekly routine": ("haftalık rutin", "Going to the cinema on Saturdays is part of my ___."),
        "Wake up early": ("erken uyanmak", "I ___ on school days, at 6:30."),
        "Get up late": ("geç uyanmak", "On Sundays, I ___ because there is no school."),
        "Eat a full breakfast": ("tam bir kahvaltı yapmak", "Always ___ before you go to school."),
        "Eat healthy food": ("sağlıklı yiyecekler yemek", "To stay healthy, you should ___ like fruit and vegetables."),
        "Go on a diet": ("diyete başlamak", "My uncle wants to lose weight, so he will ___."),
        "Have a special diet": ("özel bir diyet yapmak", "Athletes usually ___ before big competitions."),
        "Have junk food": ("abur cubur yemek", "Don't ___ like chips and hamburgers every day."),
        "Have energy drinks": ("enerji içecekleri içmek", "Children shouldn't ___; they are not healthy."),
        "Give energy": ("enerji vermek", "Bananas ___ to athletes."),
        "Make someone strong": ("birini güçlü yapmak", "Regular exercise can ___."),
        "Keep fit": ("formda kalmak", "I swim every day to ___."),
        "Regularly": ("düzenli olarak", "You should exercise ___ to stay healthy."),
        "Take a nap": ("kestirmek, şekerleme yapmak", "I am tired; I want to ___ in the afternoon."),
        "Rest": ("dinlenmek", "After a long training, players need to ___."),
        "Injury": ("yaralanma", "The player had a knee ___ and couldn't play."),
        "Hurt": ("acımak, incitmek", "Be careful! Don't ___ yourself."),
    },
    "🏆 Maç ve Başarı": {
        "Make a point": ("sayı yapmak, sayı almak", "In volleyball, you ___ when the ball touches the ground on the other side."),
        "Hit a ball": ("topa vurmak", "In tennis, you ___ with a racket."),
        "Throw": ("atmak, fırlatmak", "In basketball, you ___ the ball into the hoop."),
        "Touch": ("dokunmak", "In football, you can't ___ the ball with your hands."),
        "Beat": ("yenmek", "Our team wants to ___ the champions and win the cup."),
        "Lose": ("kaybetmek", "Don't be sad if you ___ a game; you can win the next one."),
        "Draw": ("berabere kalmak", "If the score is 2-2 at the end, the two teams ___."),
        "Cheer": ("tezahürat yapmak", "The fans ___ for their team in the stadium."),
        "Success": ("başarı", "Hard work is the key to ___."),
        "Succeed": ("başarmak", "If you study hard, you will ___."),
        "Interview": ("görüşme, röportaj", "The reporter had an ___ with the champion after the match."),
        "Watch a match": ("maç izlemek", "Let's ___ on TV tonight."),
        "Goal": ("hedef", "My ___ is to become a professional swimmer."),
        "Championship": ("şampiyonluk", "Our school team won the basketball ___."),
        "Medal": ("madalya", "She won a gold ___ at the Olympics."),
        "Equipment": ("ekipman, malzeme", "You need special ___ like a helmet and gloves for this sport."),
        "Racket": ("raket", "You need a ___ to play tennis."),
        "Net": ("file", "In volleyball, the ball must go over the ___."),
    },
}

ALL_TOPICS = "🌟 Tüm Kelimeler"
ALL = {w: (tr, s, cat) for cat, d in WORDS.items() for w, (tr, s) in d.items()}

# Birbirine çok yakın anlamlı kelimeler aynı soruda şık olarak çıkmasın
CONFUSABLE = [
    {"Field", "Court"},
    {"Jogging", "Go running", "Run"},
    {"Skating", "Ice skating"},
    {"Train", "Work out", "Do heavy exercises", "Work with the weights"},
    {"Go on a diet", "Have a special diet"},
    {"Indoor sports", "Outdoor sports", "Team sports", "Individual sports", "Team game"},
    {"Daily activities", "Weekly routine"},
    {"Take a nap", "Rest"},
    {"Injury", "Hurt"},
    {"Success", "Succeed"},
    {"Keep fit", "Make someone strong", "Give energy"},
    {"Athlete", "Player", "Swimmer"},
]

Q_TYPES = {
    "EN_TR": "İngilizce → Türkçe",
    "TR_EN": "Türkçe → İngilizce",
    "SENTENCE": "Boşluk doldurma",
}

PRAISE = ["Harika! 🎉", "Süpersin! ⭐", "Aferin! 👏", "Bravo! 🏆", "Mükemmel! 🚀", "Tam isabet! 🎯"]
ENCOURAGE = ["Olsun, bir dahakine! 💪", "Az kaldı! 🙂", "Pes etmek yok! 🔁", "Bu kelimeyi tekrar soracağım 😉"]


def confusable(a, b):
    return any(a in g and b in g for g in CONFUSABLE)


def mastery():
    return st.session_state.get("mastery", 2)


def word_pool():
    topic = st.session_state.get("topic", ALL_TOPICS)
    return [w for w, v in ALL.items() if topic == ALL_TOPICS or v[2] == topic]


def remaining():
    return [w for w in word_pool() if st.session_state.counts.get(w, 0) < mastery()]


@st.cache_data(show_spinner=False)
def pronounce(text):
    """İngilizce telaffuz (gTTS kuruluysa). Hata olursa sessizce None döner."""
    try:
        from gtts import gTTS
        buf = BytesIO()
        gTTS(text=text, lang="en").write_to_fp(buf)
        return buf.getvalue()
    except Exception:
        return None


# ---------------------------------------------------------------------------
# OYUN MANTIĞI
# ---------------------------------------------------------------------------
def new_question():
    rem = remaining()
    if not rem:
        st.session_state.q = None
        return

    prev = st.session_state.q["word"] if st.session_state.get("q") else None
    weak = [w for w in rem if w in st.session_state.wrong]
    choices = weak if (weak and random.random() < 0.5) else rem
    if len(choices) > 1 and prev in choices:
        choices = [c for c in choices if c != prev]
    word = random.choice(choices)

    qtypes = st.session_state.get("qtypes") or list(Q_TYPES)
    qtype = random.choice(qtypes)
    tr = ALL[word][0]

    candidates = [w for w in ALL if w != word and not confusable(w, word) and ALL[w][0] != tr]
    same_cat = [w for w in candidates if ALL[w][2] == ALL[word][2]]
    distract = random.sample(same_cat, 3) if len(same_cat) >= 3 else random.sample(candidates, 3)

    if qtype == "EN_TR":
        correct = tr
        options = [ALL[w][0] for w in distract] + [tr]
    else:
        correct = word
        options = distract + [word]
    random.shuffle(options)

    st.session_state.q = {"word": word, "type": qtype, "options": options, "correct": correct}
    st.session_state.answered = False
    st.session_state.chosen = None
    st.session_state.qid += 1


def answer(opt):
    ss = st.session_state
    if ss.answered:
        return  # aynı soruya ikinci kez puan verilmesin
    ss.answered = True
    ss.chosen = opt
    ss.total += 1
    word = ss.q["word"]
    if opt == ss.q["correct"]:
        ss.correct_total += 1
        ss.streak += 1
        ss.best_streak = max(ss.best_streak, ss.streak)
        ss.score += 10 + (5 if ss.streak >= 3 else 0)
        ss.counts[word] = ss.counts.get(word, 0) + 1
        ss.wrong.discard(word)
        ss.msg = random.choice(PRAISE)
    else:
        ss.streak = 0
        ss.counts[word] = 0
        ss.wrong.add(word)
        ss.msg = random.choice(ENCOURAGE)


def reset_game():
    ss = st.session_state
    ss.counts, ss.wrong = {}, set()
    ss.score = ss.streak = ss.best_streak = ss.total = ss.correct_total = 0
    ss.qid, ss.q, ss.msg = 0, None, ""
    new_question()


if "counts" not in st.session_state:
    reset_game()

# ---------------------------------------------------------------------------
# KENAR ÇUBUĞU
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Ayarlar")
    st.selectbox("Konu", [ALL_TOPICS] + list(WORDS), key="topic", on_change=reset_game)
    st.multiselect("Soru tipleri", list(Q_TYPES), default=list(Q_TYPES),
                   format_func=Q_TYPES.get, key="qtypes")
    st.slider("Bir kelime kaç doğruda öğrenilmiş sayılsın?", 1, 3, 2, key="mastery")
    st.checkbox("🔊 Telaffuzu dinlet", value=True, key="audio")

    st.divider()
    c1, c2 = st.columns(2)
    c1.metric("Puan", st.session_state.score)
    c2.metric("Seri 🔥", st.session_state.streak)
    c1.metric("En iyi seri", st.session_state.best_streak)
    c2.metric("Doğru", f"{st.session_state.correct_total}/{st.session_state.total}")

    if st.session_state.wrong:
        with st.expander(f"⚠️ Zayıf kelimeler ({len(st.session_state.wrong)})"):
            for w in sorted(st.session_state.wrong):
                st.write(f"**{w}** – {ALL[w][0]}")

    st.button("🔄 Baştan başla", on_click=reset_game, width="stretch")

# ---------------------------------------------------------------------------
# ANA EKRAN
# ---------------------------------------------------------------------------
st.title("⚽ Unit 2: Sports – Kelime Oyunu")
tab_game, tab_study = st.tabs(["🎯 Oyna", "📖 Kelimelere Çalış"])

with tab_game:
    pool = word_pool()
    learned = sum(st.session_state.counts.get(w, 0) >= mastery() for w in pool)
    st.progress(learned / len(pool), text=f"{learned} / {len(pool)} kelime öğrenildi")

    q = st.session_state.q
    if q is None:
        st.balloons()
        st.success(f"🏆 Tebrikler! Bu konudaki tüm kelimeleri öğrendin! Puanın: {st.session_state.score}")
        st.button("🔁 Tekrar oyna", on_click=reset_game, type="primary")
    else:
        word = q["word"]
        tr, sentence, cat = ALL[word]
        answered = st.session_state.answered
        st.caption(cat)

        if q["type"] == "EN_TR":
            st.subheader("Bu kelimenin Türkçesi hangisi?")
            st.markdown(f"<h1 style='text-align:center;color:#1f77b4'>{word}</h1>", unsafe_allow_html=True)
            if st.session_state.get("audio"):
                audio = pronounce(word)
                if audio:
                    st.audio(audio, format="audio/mp3")
        elif q["type"] == "TR_EN":
            st.subheader("Bunun İngilizcesi hangisi?")
            st.markdown(f"<h1 style='text-align:center;color:#d62728'>{tr}</h1>", unsafe_allow_html=True)
        else:
            st.subheader("Boşluğa hangi kelime gelir?")
            st.markdown(f"### {sentence.replace('___', '_______')}")
            with st.expander("💡 İpucu"):
                st.write(f"Türkçe anlamı: **{tr}**")

        st.write("")
        cols = st.columns(2)
        for i, opt in enumerate(q["options"]):
            label = opt
            if answered:
                if opt == q["correct"]:
                    label = f"✅ {opt}"
                elif opt == st.session_state.chosen:
                    label = f"❌ {opt}"
            cols[i % 2].button(label, key=f"opt_{st.session_state.qid}_{i}",
                               on_click=answer, args=(opt,), disabled=answered, width="stretch")

        if answered:
            if st.session_state.chosen == q["correct"]:
                st.success(st.session_state.msg)
            else:
                st.error(f"{st.session_state.msg}  Doğru cevap: **{q['correct']}**")

            fill = word if sentence.startswith("___") else word[0].lower() + word[1:]
            st.info(f"**{word}** = {tr}\n\n📝 {sentence.replace('___', f'**{fill}**')}")
            if st.session_state.get("audio") and q["type"] != "EN_TR":
                audio = pronounce(word)
                if audio:
                    st.audio(audio, format="audio/mp3")

            st.button("Sonraki soru ➡️", on_click=new_question, type="primary", width="stretch")

with tab_study:
    search = st.text_input("🔍 Kelime ara (İngilizce veya Türkçe)").strip().lower()
    for cat, d in WORDS.items():
        rows = []
        for w, (tr, s) in d.items():
            if search and search not in w.lower() and search not in tr.lower():
                continue
            if st.session_state.counts.get(w, 0) >= mastery():
                status = "✅"
            elif w in st.session_state.wrong:
                status = "⚠️"
            else:
                status = ""
            rows.append({"": status, "İngilizce": w, "Türkçe": tr})
        if rows:
            st.subheader(cat)
            st.dataframe(rows, hide_index=True, width="stretch")
