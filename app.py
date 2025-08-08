import streamlit as st
import random
from wordfreq import top_n_list
from collections import Counter

# --- Initialize Session State ---
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "num_letters" not in st.session_state:
    st.session_state.num_letters = None
if "letters" not in st.session_state:
    st.session_state.letters = []
if "valid_words" not in st.session_state:
    st.session_state.valid_words = []
if "entered_correct_words" not in st.session_state:
    st.session_state.entered_correct_words = 0
if "total_words" not in st.session_state:
    st.session_state.total_words = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
# For showing feedback after a guess
if "last_feedback" not in st.session_state:
    st.session_state.last_feedback = ""

# --- Your Original Functions ---
def give_random_letters_according_to_difficuilty_level(n):
    letter_sets = {
        3: ['a','e','r','t','l','n','s','o','p','d'],
        4: ['e','a','r','t','l','n','s','o','d','m','p','c'],
        5: ['e','a','r','t','l','n','s','o','d','m','p','c','h','i','u'],
        6: ['e','a','r','t','l','n','s','o','d','m','p','c','h','i','u','g'],
        7: ['e','a','r','t','l','n','s','o','d','m','p','c','h','i','u','g','b','y'],
        8: ['e','a','r','t','l','n','s','o','d','m','p','c','h','i','u','g','b'],
        9: ['e','a','r','t','l','n','s','o','d','m','p','c','h','i','u','g','b','y'],
        10: ['e','a','r','t','l','n','s','o','d','m','p','c','h','i','u','g','b','y','f'],
        11: ['e','a','r','t','l','n','s','o','d','m','p','c','h','i','u','g','b','y','f','v'],
        12: ['e','a','r','t','l','n','s','o','d','m','p','c','h','i','u','g','b','y','f','v','k']
    }
    return letter_sets.get(n, [])

def difficuilty_easy():
    return random.randint(3, 6)
def difficuilty_medium():
    return random.randint(5, 8)
def difficuilty_hard():
    return random.randint(9, 12)

def difficuilty(n):
    if n <= 3:
        return difficuilty_easy()
    elif n > 3 and n % 3 != 0 and n % 2 == 0:
        return difficuilty_medium()
    elif n > 3 and n % 3 == 0 and n % 2 != 0:
        return difficuilty_hard()

def get_valid_words(n, letters):
    letter_bank = Counter(letters)
    common_words = top_n_list('en', 50000)
    valid_words = []
    for word in common_words:
        word = word.lower().strip()
        if len(word) != n:
            continue
        word_count = Counter(word)
        if all(word_count[c] <= letter_bank[c] for c in word_count):
            valid_words.append(word)
    return sorted(valid_words)

# --- First Stage Initialization ---
if st.session_state.num_letters is None:
    st.session_state.num_letters = difficuilty(st.session_state.stage)
    st.session_state.letters = give_random_letters_according_to_difficuilty_level(st.session_state.num_letters)
    st.session_state.valid_words = get_valid_words(st.session_state.num_letters, st.session_state.letters)
    st.session_state.total_words = len(st.session_state.valid_words)

# --- Display Game Info ---
st.markdown(f"### Stage {st.session_state.stage}")
st.markdown(f"**Letters:** {st.session_state.letters}")
st.markdown(f"❗ Each word must have {st.session_state.num_letters} letters")
st.markdown(f"✅ Correct words entered: {st.session_state.entered_correct_words} / 20")
st.markdown(f"Remaining possible words: {st.session_state.total_words}")

# --- Callback to process the entered word (runs when Enter pressed) ---
def _process_input():
    # read, process, clear — only using st.session_state (no st.write inside callback)
    w = st.session_state.word_input.strip().lower()
    if not w:
        return
    if w in st.session_state.valid_words:
        st.session_state.entered_correct_words += 1
        st.session_state.total_words -= 1
        st.session_state.valid_words.remove(w)
        st.session_state.last_feedback = f"✅ '{w}' is correct!"
    else:
        st.session_state.last_feedback = f"❌ '{w}' is not valid. Letters allowed: {st.session_state.letters}"
    # clear the input for the next word
    st.session_state.word_input = ""

# --- Input with on_change callback so pressing Enter submits and clears ---
st.text_input("➡️ Enter a word:", key="word_input", on_change=_process_input)

# --- Show feedback from last processed word ---
if st.session_state.last_feedback:
    # show feedback and then reset it (so it doesn't persist forever)
    st.markdown(st.session_state.last_feedback)
    st.session_state.last_feedback = ""

# --- Stage Progression ---
if st.session_state.entered_correct_words >= 20:
    if st.button("➡ Go to Next Stage"):
        st.session_state.stage += 1
        st.session_state.entered_correct_words = 0
        st.session_state.num_letters = difficuilty(st.session_state.stage)
        st.session_state.letters = give_random_letters_according_to_difficuilty_level(st.session_state.num_letters)
        st.session_state.valid_words = get_valid_words(st.session_state.num_letters, st.session_state.letters)
        st.session_state.total_words = len(st.session_state.valid_words)
        # ensure input cleared for new stage
        st.session_state.word_input = ""
        st.experimental_rerun()

# --- End Game ---
if st.button("❌ End Game"):
    st.session_state.game_over = True

if st.session_state.game_over:
    st.markdown("### 👋 Thanks for playing Smart Guesser!")
