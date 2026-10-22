import random
from io import BytesIO

import streamlit as st

st.set_page_config(page_title="Unit 2: Sports – Kelime Oyunu", page_icon="⚽", layout="centered")

# ---------------------------------------------------------------------------
# KELİMELER (7. sınıf 2. Ünite – defter görsellerinden)
# Biçim: "İngilizce": ("Türkçe", ["cümle 1", "cümle 2", "cümle 3"])
# ---------------------------------------------------------------------------
WORDS = {
    "🏟️ Sporlar ve Sporcular": {
        "Sport": ("spor", [
            "Football is the most popular ___ in Turkey.",
            "Which ___ do you like best, basketball or tennis?",
            "Doing ___ every day is good for your health."]),
        "Indoor sports": ("kapalı alan sporları", [
            "Basketball and volleyball are ___ because we play them in a hall.",
            "We can't play outside when it rains, so we do ___.",
            "Table tennis and judo are ___."]),
        "Outdoor sports": ("açık alan sporları", [
            "Skiing and surfing are ___ because we do them outside.",
            "I like ___ because I love fresh air.",
            "Cycling and jogging are ___."]),
        "Team sports": ("takım sporları", [
            "Football and volleyball are ___.",
            "In ___, players work together to win.",
            "Basketball is one of my favourite ___."]),
        "Team game": ("takım oyunu", [
            "Basketball is a ___; you need five players.",
            "Volleyball is a ___ with six players on each side.",
            "Football is a ___, not an individual sport."]),
        "Individual sports": ("bireysel sporlar", [
            "Swimming and running are ___; you do them alone.",
            "In ___, you don't need a team.",
            "Judo and skiing are ___."]),
        "Gym": ("spor salonu", [
            "My brother works out at the ___ three times a week.",
            "There are many weights and machines in the ___.",
            "We have our P.E. lessons in the school ___."]),
        "Player": ("oyuncu", [
            "Arda Güler is a famous football ___.",
            "Who is the best ___ in your team?",
            "The ___ kicked the ball into the goal."]),
        "Spectator": ("seyirci, izleyici", [
            "Every ___ in the stadium was cheering for the team.",
            "A ___ watches a match but doesn't play.",
            "The ___ bought a ticket for the final match."]),
        "Opponent": ("karşı taraf, rakip", [
            "Our team will play against a strong ___ on Sunday.",
            "Our ___ was very fast, but we won the race.",
            "In a tennis match, you play against one ___."]),
        "Athlete": ("atlet, sporcu", [
            "The ___ won a gold medal in the 100-metre race.",
            "Usain Bolt is a famous ___ from Jamaica.",
            "A good ___ trains hard every day."]),
        "Swimmer": ("yüzücü", [
            "Michael Phelps is a very famous ___.",
            "The ___ jumped into the pool.",
            "A good ___ can swim very fast."]),
        "Swimming pool": ("yüzme havuzu", [
            "We swim in the ___ every summer.",
            "There is a big ___ at our sports centre.",
            "Don't run near the ___; it is slippery."]),
        "Field": ("saha (futbol sahası)", [
            "The football players are running on the ___.",
            "The football ___ is green and very big.",
            "The players walked onto the ___ before the match."]),
        "Court": ("saha (tenis/basketbol sahası)", [
            "They are playing tennis on the ___.",
            "A basketball ___ has two hoops.",
            "The volleyball players are waiting on the ___."]),
        "Cycling": ("bisiklet sürme", [
            "___ is my favourite outdoor activity; I ride my bike every weekend.",
            "I go ___ with my friends on Saturdays.",
            "___ is good for your legs."]),
    },
    "🏄 Spor Aktiviteleri": {
        "Surfing": ("sörf yapma", [
            "We went ___ in the sea last summer.",
            "You need big waves for ___.",
            "___ is a popular water sport in Hawaii."]),
        "Skiing": ("kayak yapma", [
            "We go ___ on Uludağ every winter.",
            "You need snow for ___.",
            "___ is my favourite winter sport."]),
        "Skating": ("patenle kayma", [
            "My sister loves ___ in the park with her roller skates.",
            "You need skates for ___.",
            "___ in the park is fun on sunny days."]),
        "Ice skating": ("buz pateni yapma", [
            "We went ___ at the ice rink last weekend.",
            "___ is fun, but you can fall on the ice.",
            "I want to try ___ this winter."]),
        "Doing judo": ("judo yapma", [
            "___ makes you strong and disciplined.",
            "My brother is good at ___; he has a black belt.",
            "___ is an individual sport from Japan."]),
        "Jogging": ("tempolu yürüyüş, koşu", [
            "My father goes ___ in the park every morning.",
            "___ in the morning makes me feel fresh.",
            "I go ___ along the seaside."]),
        "Go running": ("koşuya gitmek, koşuya çıkmak", [
            "I ___ with my dad every Sunday morning.",
            "Let's ___ in the park after school.",
            "Athletes ___ every day."]),
        "Go swimming": ("yüzmeye gitmek", [
            "In summer, we ___ in the sea.",
            "When it is hot, we ___ in the pool.",
            "Do you want to ___ with me tomorrow?"]),
        "Breaststroke": ("kurbağalama yüzüş", [
            "In ___, you move your arms and legs like a frog.",
            "___ is a slow but easy swimming style.",
            "My swimming teacher taught me ___."]),
        "Freestyle": ("serbest stil", [
            "___ is the fastest swimming style.",
            "In ___, swimmers move their arms one after the other.",
            "She won the 100-metre ___ race."]),
        "Run": ("koşmak", [
            "I can ___ very fast.",
            "Don't ___ in the classroom!",
            "Cheetahs ___ faster than any other animal."]),
        "Train": ("antrenman yapmak", [
            "Footballers ___ hard before an important match.",
            "Our team will ___ every day before the championship.",
            "Athletes ___ for many hours a day."]),
        "Work out": ("egzersiz yapmak", [
            "I ___ at the gym three times a week.",
            "I ___ to keep fit.",
            "Let's ___ together at the gym."]),
        "Do heavy exercises": ("ağır egzersizler yapmak", [
            "Don't ___ right after a big meal.",
            "Children shouldn't ___; light ones are better.",
            "Weightlifters ___ to get very strong."]),
        "Work with the weights": ("ağırlıklarla çalışmak", [
            "Bodybuilders ___ to build big muscles.",
            "I ___ at the gym to make my arms strong.",
            "You need a trainer when you ___ for the first time."]),
        "Join a sports activity": ("bir spor aktivitesine katılmak", [
            "I want to ___ at school this year.",
            "If you ___, you can make new friends.",
            "My teacher wants all students to ___."]),
        "Compete in the races": ("yarışlarda yarışmak", [
            "Athletes ___ at the Olympic Games.",
            "Runners ___ to win medals.",
            "Our swimmers will ___ next week."]),
    },
    "🥗 Sağlıklı Yaşam ve Rutinler": {
        "Daily activities": ("günlük aktiviteler", [
            "Brushing my teeth and having breakfast are my ___.",
            "Going to school and doing homework are ___.",
            "Write about your ___ in your notebook."]),
        "Weekly routine": ("haftalık rutin", [
            "Going to the cinema on Saturdays is part of my ___.",
            "My ___ includes swimming on Tuesdays and judo on Fridays.",
            "What is your ___? Do you do sports every week?"]),
        "Wake up early": ("erken uyanmak", [
            "I ___ on school days, at 6:30.",
            "I ___ to catch the school bus.",
            "If you go to bed late, it is difficult to ___."]),
        "Get up late": ("geç uyanmak", [
            "On Sundays, I ___ because there is no school.",
            "I ___ on holidays and have breakfast at 11.",
            "Don't ___ on school days, or you will miss the bus."]),
        "Eat a full breakfast": ("tam bir kahvaltı yapmak", [
            "Always ___ before you go to school.",
            "Athletes ___ to have energy in the morning.",
            "I ___ with eggs, cheese and olives."]),
        "Eat healthy food": ("sağlıklı yiyecekler yemek", [
            "To stay healthy, you should ___ like fruit and vegetables.",
            "If you ___, you will be strong.",
            "Athletes ___ to keep fit."]),
        "Go on a diet": ("diyete başlamak", [
            "My uncle wants to lose weight, so he will ___.",
            "The doctor told him to ___.",
            "I eat too much junk food; maybe I should ___."]),
        "Have a special diet": ("özel bir diyet yapmak", [
            "Athletes usually ___ before big competitions.",
            "Footballers ___ with lots of protein.",
            "Some swimmers ___ before a race."]),
        "Have junk food": ("abur cubur yemek", [
            "Don't ___ like chips and hamburgers every day.",
            "It is unhealthy to ___ too often.",
            "My mum doesn't let me ___ before dinner."]),
        "Have energy drinks": ("enerji içecekleri içmek", [
            "Children shouldn't ___; they are not healthy.",
            "Some athletes ___, but water is better.",
            "My doctor says I mustn't ___."]),
        "Give energy": ("enerji vermek", [
            "Bananas ___ to athletes.",
            "Fruits and nuts ___ to our body.",
            "A full breakfast can ___ for the whole morning."]),
        "Make someone strong": ("birini güçlü yapmak", [
            "Regular exercise can ___.",
            "Healthy food and sports ___.",
            "Milk and vegetables can ___."]),
        "Keep fit": ("formda kalmak", [
            "I swim every day to ___.",
            "Jogging helps me ___.",
            "Athletes exercise regularly to ___."]),
        "Regularly": ("düzenli olarak", [
            "You should exercise ___ to stay healthy.",
            "I go to the gym ___, three times a week.",
            "Athletes train ___ to win medals."]),
        "Take a nap": ("kestirmek, şekerleme yapmak", [
            "I am tired; I want to ___ in the afternoon.",
            "My grandfather likes to ___ after lunch.",
            "Babies ___ many times a day."]),
        "Rest": ("dinlenmek", [
            "After a long training, players need to ___.",
            "You are tired; sit down and ___.",
            "After the match, the players went home to ___."]),
        "Injury": ("yaralanma", [
            "The player had a knee ___ and couldn't play.",
            "He couldn't play in the final because of an ___.",
            "Warm up before sports to avoid ___."]),
        "Hurt": ("acımak, incitmek", [
            "Be careful! Don't ___ yourself.",
            "My leg will ___ if I run too much.",
            "Did you ___ your arm when you fell?"]),
    },
    "🏆 Maç ve Başarı": {
        "Make a point": ("sayı yapmak, sayı almak", [
            "In volleyball, you ___ when the ball touches the ground on the other side.",
            "Our team needs to ___ to win the game.",
            "In basketball, you ___ when the ball goes into the hoop."]),
        "Hit a ball": ("topa vurmak", [
            "In tennis, you ___ with a racket.",
            "In baseball, players ___ with a bat.",
            "In volleyball, you ___ with your hands."]),
        "Throw": ("atmak, fırlatmak", [
            "In basketball, you ___ the ball into the hoop.",
            "Can you ___ the ball to me?",
            "In handball, players ___ the ball into the goal."]),
        "Touch": ("dokunmak", [
            "In football, you can't ___ the ball with your hands.",
            "Don't ___ the net in volleyball!",
            "Goalkeepers can ___ the ball with their hands."]),
        "Beat": ("yenmek", [
            "Our team wants to ___ the champions and win the cup.",
            "We will try to ___ them in the next match.",
            "Can you ___ me in a race?"]),
        "Lose": ("kaybetmek", [
            "Don't be sad if you ___ a game; you can win the next one.",
            "If we don't train hard, we will ___ the championship.",
            "Nobody likes to ___ a match."]),
        "Draw": ("berabere kalmak", [
            "If the score is 2-2 at the end, the two teams ___.",
            "When both teams score the same number of goals, they ___.",
            "Strong teams often ___ when they play against each other."]),
        "Cheer": ("tezahürat yapmak", [
            "The fans ___ for their team in the stadium.",
            "We ___ loudly when our team scores a goal.",
            "Let's ___ for our school team!"]),
        "Success": ("başarı", [
            "Hard work is the key to ___.",
            "Winning the gold medal was a big ___ for her.",
            "Training regularly brings ___."]),
        "Succeed": ("başarmak", [
            "If you study hard, you will ___.",
            "You can ___ if you never give up.",
            "Athletes train hard to ___."]),
        "Interview": ("görüşme, röportaj", [
            "The reporter had an ___ with the champion after the match.",
            "The famous player gave an ___ on TV.",
            "The journalist asked many questions in the ___."]),
        "Watch a match": ("maç izlemek", [
            "Let's ___ on TV tonight.",
            "We went to the stadium to ___.",
            "My dad and I like to ___ together on Sundays."]),
        "Goal": ("hedef", [
            "My ___ is to become a professional swimmer.",
            "Winning the championship is our team's ___.",
            "What is your ___ for this year?"]),
        "Championship": ("şampiyonluk", [
            "Our school team won the basketball ___.",
            "Which team will win the ___ this year?",
            "They celebrated after winning the ___."]),
        "Medal": ("madalya", [
            "She won a gold ___ at the Olympics.",
            "The winner gets a gold ___.",
            "He won a silver ___ in swimming."]),
        "Equipment": ("ekipman, malzeme", [
            "You need special ___ like a helmet and gloves for this sport.",
            "Rackets and balls are tennis ___.",
            "The school bought new sports ___ for the gym."]),
        "Racket": ("raket", [
            "You need a ___ to play tennis.",
            "Badminton players hit the shuttlecock with a ___.",
            "My tennis ___ is broken; I need a new one."]),
        "Net": ("file", [
            "In volleyball, the ball must go over the ___.",
            "The tennis ball hit the ___ and fell down.",
            "The goalkeeper stands in front of the ___."]),
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
    "EN_TR": "🇬🇧→🇹🇷 İngilizce → Türkçe",
    "TR_EN": "🇹🇷→🇬🇧 Türkçe → İngilizce",
    "SENTENCE": "📝 Boşluk doldurma",
    "TF": "👍👎 Doğru mu, yanlış mı?",
    "SPELL": "⌨️ Yazarak cevapla",
    "LISTEN": "🎧 Dinle ve seç",
}

PRAISE = ["Harika! 🎉", "Süpersin! ⭐", "Aferin! 👏", "Bravo! 🏆", "Mükemmel! 🚀", "Tam isabet! 🎯"]
ENCOURAGE = ["Olsun, bir dahakine! 💪", "Az kaldı! 🙂", "Pes etmek yok! 🔁", "Bu kelimeyi tekrar soracağım 😉"]


def confusable(a, b):
    return any(a in g and b in g for g in CONFUSABLE)


def norm(text):
    return " ".join(str(text).lower().replace("’", "'").split())


def mastery():
    return st.session_state.get("mastery", 3)


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


def spell_hint(word):
    """'Keep fit' -> 'K _ _ _   _ _ _'"""
    parts = []
    for i, part in enumerate(word.split()):
        letters = [part[0] if i == 0 else "_"] + ["_"] * (len(part) - 1)
        parts.append(" ".join(letters))
    return "     ".join(parts)


# ---------------------------------------------------------------------------
# OYUN MANTIĞI
# ---------------------------------------------------------------------------
def new_question():
    ss = st.session_state
    rem = remaining()
    if not rem:
        ss.q = None
        return

    prev = ss.q["word"] if ss.get("q") else None
    weak = [w for w in rem if w in ss.wrong]
    choices = weak if (weak and random.random() < 0.5) else rem
    if len(choices) > 1 and prev in choices:
        choices = [c for c in choices if c != prev]
    word = random.choice(choices)
    tr, sentences, cat = ALL[word]

    qtypes = list(ss.get("qtypes") or Q_TYPES)
    # Dinleme sorusu yalnızca ses açıksa ve gTTS çalışıyorsa
    if "LISTEN" in qtypes and (not ss.get("audio", True) or pronounce(word) is None):
        qtypes.remove("LISTEN")
    # Aynı tip art arda gelmesin (mümkünse)
    prev_type = ss.q["type"] if ss.get("q") else None
    if len(qtypes) > 1 and prev_type in qtypes:
        qtypes.remove(prev_type)
    qtype = random.choice(qtypes or ["EN_TR"])

    candidates = [w for w in ALL if w != word and not confusable(w, word) and ALL[w][0] != tr]
    same_cat = [w for w in candidates if ALL[w][2] == cat]
    distract = random.sample(same_cat, 3) if len(same_cat) >= 3 else random.sample(candidates, 3)

    q = {"word": word, "type": qtype, "sentence": random.choice(sentences)}
    if qtype == "EN_TR":
        q["correct"] = tr
        q["options"] = [ALL[w][0] for w in distract] + [tr]
    elif qtype == "TF":
        truth = random.random() < 0.5
        q["shown"] = tr if truth else ALL[distract[0]][0]
        q["correct"] = "Doğru 👍" if truth else "Yanlış 👎"
        q["options"] = ["Doğru 👍", "Yanlış 👎"]
    elif qtype == "SPELL":
        q["correct"] = word
        q["options"] = []
    else:  # TR_EN, SENTENCE, LISTEN
        q["correct"] = word
        q["options"] = distract + [word]
    if qtype != "TF":
        random.shuffle(q["options"])

    ss.q = q
    ss.answered = False
    ss.chosen = None
    ss.qid += 1


def answer(opt):
    ss = st.session_state
    if ss.answered:
        return  # aynı soruya ikinci kez puan verilmesin
    ss.answered = True
    ss.chosen = opt
    ss.total += 1
    word = ss.q["word"]
    if norm(opt) == norm(ss.q["correct"]):
        ss.correct_total += 1
        ss.streak += 1
        ss.best_streak = max(ss.best_streak, ss.streak)
        bonus = 10 if ss.q["type"] == "SPELL" else 0  # yazmak daha zor
        ss.score += 10 + bonus + (5 if ss.streak >= 3 else 0)
        ss.counts[word] = ss.counts.get(word, 0) + 1
        ss.wrong.discard(word)
        ss.msg = random.choice(PRAISE)
        ss.last_ok = True
    else:
        ss.streak = 0
        ss.counts[word] = 0
        ss.wrong.add(word)
        ss.msg = random.choice(ENCOURAGE)
        ss.last_ok = False


def spell_submit():
    answer(st.session_state.get(f"spell_{st.session_state.qid}", ""))


def reset_game():
    ss = st.session_state
    ss.counts, ss.wrong = {}, set()
    ss.score = ss.streak = ss.best_streak = ss.total = ss.correct_total = 0
    ss.qid, ss.q, ss.msg, ss.last_ok = 0, None, "", False
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
    st.slider("Bir kelime kaç doğruda öğrenilmiş sayılsın?", 1, 5, 3, key="mastery")
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
        ss = st.session_state
        word = q["word"]
        tr, _, cat = ALL[word]
        sentence = q["sentence"]
        answered = ss.answered
        st.caption(f"{cat}  ·  {Q_TYPES[q['type']]}")

        def big(text, color):
            st.markdown(f"<h1 style='text-align:center;color:{color}'>{text}</h1>", unsafe_allow_html=True)

        # --- Soru metni ---
        if q["type"] == "EN_TR":
            st.subheader("Bu kelimenin Türkçesi hangisi?")
            big(word, "#1f77b4")
            if ss.get("audio") and (audio := pronounce(word)):
                st.audio(audio, format="audio/mp3")
        elif q["type"] == "TR_EN":
            st.subheader("Bunun İngilizcesi hangisi?")
            big(tr, "#d62728")
        elif q["type"] == "SENTENCE":
            st.subheader("Boşluğa hangi kelime gelir?")
            st.markdown(f"### {sentence.replace('___', '_______')}")
            with st.expander("💡 İpucu"):
                st.write(f"Türkçe anlamı: **{tr}**")
        elif q["type"] == "TF":
            st.subheader("Bu eşleşme doğru mu?")
            big(f"{word} = {q['shown']}", "#9467bd")
        elif q["type"] == "SPELL":
            st.subheader("İngilizcesini yaz!")
            big(tr, "#2ca02c")
            st.markdown(f"<p style='text-align:center;font-size:1.6rem;letter-spacing:2px'>"
                        f"{spell_hint(word)}</p>", unsafe_allow_html=True)
        elif q["type"] == "LISTEN":
            st.subheader("Dinle ve duyduğun kelimeyi seç 🎧")
            st.audio(pronounce(word), format="audio/mp3")

        st.write("")

        # --- Cevap alanı ---
        if q["type"] == "SPELL":
            with st.form(key=f"form_{ss.qid}"):
                st.text_input("Cevabın:", key=f"spell_{ss.qid}", disabled=answered,
                              placeholder="İngilizce kelimeyi buraya yaz")
                st.form_submit_button("Kontrol et ✔️", on_click=spell_submit, disabled=answered)
        else:
            cols = st.columns(2)
            for i, opt in enumerate(q["options"]):
                label = opt
                if answered:
                    if opt == q["correct"]:
                        label = f"✅ {opt}"
                    elif opt == ss.chosen:
                        label = f"❌ {opt}"
                cols[i % 2].button(label, key=f"opt_{ss.qid}_{i}",
                                   on_click=answer, args=(opt,), disabled=answered, width="stretch")

        # --- Geri bildirim ---
        if answered:
            if ss.last_ok:
                st.success(ss.msg)
            elif q["type"] == "TF":
                st.error(ss.msg)
            elif q["type"] == "SPELL":
                st.error(f"{ss.msg}  Senin yazdığın: *{ss.chosen or '(boş)'}* → Doğrusu: **{word}**")
            else:
                st.error(f"{ss.msg}  Doğru cevap: **{q['correct']}**")

            fill = word if sentence.startswith("___") else word[0].lower() + word[1:]
            st.info(f"**{word}** = {tr}\n\n📝 {sentence.replace('___', f'**{fill}**')}")
            if ss.get("audio") and q["type"] not in ("EN_TR", "LISTEN") and (audio := pronounce(word)):
                st.audio(audio, format="audio/mp3")

            st.button("Sonraki soru ➡️", on_click=new_question, type="primary", width="stretch")

with tab_study:
    search = st.text_input("🔍 Kelime ara (İngilizce veya Türkçe)").strip().lower()
    for cat, d in WORDS.items():
        rows = []
        for w, (tr, _) in d.items():
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
