import streamlit as st
import random
import time

emojis={
    "🦁 + 👑": "Lion King",
    "🐞 + 🔧": "Debug",
    "🦇 + 👨": "Batman",
    "🧠 + 💾": "Memory",
    "🔥 + 🚒": "Fire Truck",
    "🔐 + 🔑": "Encryption",
    "📚 + 🐛": "Bookworm",
    "🐞 + 💣": "Bug",
    "🌧️ + 🏹": "Rainbow",
    "🛏️ + 🕒": "Bed Time",
    "🧱 + 🔗": "Blockchain",
    "🍫 + 🍰": "Chocolate Cake",
    "📦 + 📤": "Package",
    "🌐 + 🔍": "Web Search",
    "👂 + 📚": "Audiobook"
}
timer=30

def init_game():
    st.session_state.questions=random.sample(list(emojis.items()), len(emojis))
    st.session_state.index=0
    st.session_state.started=True
    st.session_state.feedback=""
    st.session_state.start_time=time.time()
    st.session_state.answered=False

def check_answer(user_ans, correct_ans):
    if user_ans.strip().lower()==correct_ans.strip().lower():
        st.session_state.feedback=f"✅ Correct! It was '{correct_ans}'."
    else:
        st.session_state.feedback=f"❌ Wrong! Correct answer: '{correct_ans}'."
    st.session_state.answered=True

def next_question():
    st.session_state.index+=1
    st.session_state.feedback=""
    st.session_state.start_time=time.time()
    st.session_state.answered=False

def main():
    st.set_page_config("Emoji Mime Game", layout="centered")
    st.title("🎭 Emoji Mime")
    st.markdown("Guess the word or phrase based on the emojis!")

    if not st.session_state.get("started"):
        st.image("https://placehold.co/600x200/ADD8E6/000000?text=Emoji+Mime+Game")
        if st.button("▶️ Start Game"):
            init_game()
            st.rerun()
        return

    if st.session_state.index>=len(st.session_state.questions):
        st.success(f"🎉 Game Over!")
        st.session_state.started=False
        return

    emoji, answer=st.session_state.questions[st.session_state.index]
    st.markdown(f"<h1 style='text-align:center;font-size:72px'>{emoji}</h1>", unsafe_allow_html=True)

    elapsed=int(time.time()-st.session_state.start_time)
    time_left=max(0, timer-elapsed)
    if not st.session_state.answered:
        st.info(f"⏳ Time Left: {time_left}s")
    if time_left==0 and not st.session_state.answered:
        st.session_state.feedback=f"⏰ Time's up! The answer was '{answer}'."
        st.session_state.answered=True

    if not st.session_state.answered:
        user_ans=st.text_input("Your Guess:")
        if st.button("Submit Answer"):
            if user_ans:
                check_answer(user_ans, answer)
                st.rerun()
            else:
                st.warning("Please enter your answer.")
    else:
        st.markdown(f"**{st.session_state.feedback}**")
        if st.button("Next"):
            next_question()
            st.rerun()

if __name__=="__main__":
    main()