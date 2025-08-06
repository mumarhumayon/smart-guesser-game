
import streamlit as st
import random 
from wordfreq import top_n_list
from collections import Counter
st.markdown("                                          -----🧠🧠🧠 Welcome to Smart Guesser 🧠🧠🧠-----                                         ")
def give_random_letters_according_to_difficuilty_level(n):
    if n==3:
        random_letters =['a', 'e', 'r', 't', 'l', 'n', 's', 'o', 'p', 'd']
        return random_letters
    elif n==4:
        random_letters =['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c']
        return random_letters
    elif n==5:
        random_letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u']
        return random_letters
    elif n==6:
        random_letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g']
        return random_letters
    elif n == 7:
        random_letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g', 'b', 'y']
        return random_letters
    elif n == 8:
        random_letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g', 'b']
        return random_letters
    elif n == 9:
        random_letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g', 'b', 'y']
        return random_letters
    elif n == 10:
        random_letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g', 'b', 'y', 'f']
        return random_letters
    elif n == 11:
        random_letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g', 'b', 'y', 'f', 'v']
        return random_letters
    elif n == 12:
        random_letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g', 'b', 'y', 'f', 'v', 'k']
        return random_letters


def difficuilty(n):
    if n==1 or n==2 or n==3:
      x=  difficuilty_easy()
      return x
    elif n>3 and n%3!=0 and n%2==0:
      x=  difficuilty_medium()
      return x
    elif n>3 and n%3==0 and n%2!=0 :
        x= difficuilty_hard()
        return x
def difficuilty_easy():
    number_of_letters=random.randint(3,6)
    return(number_of_letters)
def difficuilty_medium():
    number_of_letters=random.randint(5,8)
    return(number_of_letters)
     
def difficuilty_hard():
    number_of_letters=random.randint(9,12)
    return(number_of_letters)

def words_for_each_num_of_letter(n): 
       
    if n == 3:
            letters = ['a', 'e', 'r', 't', 'l', 'n', 's', 'o', 'p', 'd']
            letter_bank = Counter(letters)
            common_words = top_n_list('en', 50000)
            valid_words = []
            for word in common_words:
                    word = word.lower()   
                    if len(word) != 3:
                            continue
                    word_count = Counter(word)
                    if all(word_count[c] <= letter_bank[c] for c in word_count):
                            valid_words.append(word)
            words = sorted(valid_words)
            total_words=len(words)
            entered_correct_words=0
            st.markdown("                                     ❗You Have to Enter at least 20 words to finish this stage ❗")
            st.markdown(f"Total Words: {total_words}") 
            st.markdown(" Start Entering Words One By One.")
            r=total_words
    
            for _ in range(r):
                    p=0
                    while True:
                            
                            x = st.text_input("➡️  ", key=f"word_input_{p}").strip().lower()
                            if x:
                             if x in words:
                                    total_words -= 1
                                    entered_correct_words += 1
                                    st.markdown(f"  ✅ Entered Correct Word                                                          Correct words entered: {entered_correct_words}   Remaining words: {total_words}")
                                    break
                             else:
                                    st.markdown(f"  ❌ Incorrect Word. Please enter a valid word below.                         Letters Allowed {letters} ")
                            
                            p+=1
                            if entered_correct_words >= 20:
                                if entered_correct_words % 2 == 0:
                                    skip = st.text_input("  ➡ For Going to the next stage, Enter (YES). Otherwise (NO): ").strip().lower()
                                    if skip == "yes":
                                                    st.markdown(f"\n  🎉 Hurray! You have entered {entered_correct_words} Correct Words! 🏆")
                                                    st.markdown("                        ---Moving to Next Stage---")
                                                    return
                                    else:
                                            pass
                                    
                    
    elif n == 4:
        letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c']
        letter_bank = Counter(letters)
        common_words = top_n_list('en', 50000)
        valid_words = []
        for word in common_words:
            word = word.lower().strip()  # ensure lowercase and clean
            if len(word) != 4:
                continue
            word_count = Counter(word)
            if all(word_count[c] <= letter_bank[c] for c in word_count):
                valid_words.append(word)
        words = sorted(valid_words)
        total_words = len(words)
        entered_correct_words = 0

        st.markdown("                                     ❗You Have to Enter at least 20 words to finish this stage ❗")
        st.markdown(f"Total Words: {total_words}") 
        st.markdown(" Start Entering Words One By One.")
        r = total_words

        for _ in range(r):
            p=0
            while True:
                x = st.text_input("➡️  ", key=f"word_input_{p}").strip().lower()
                if x:
                 if x in words:
                    total_words -= 1
                    entered_correct_words += 1
                    st.markdown(f"  ✅ Entered Correct Word                                                          Correct words entered: {entered_correct_words}   Remaining words: {total_words}")
                    break
                 else:
                    st.markdown(f"  ❌ Incorrect Word. Please enter a valid word below.     Letters Allowed {letters}")
                p+=1
            if entered_correct_words >= 20:
               if entered_correct_words % 2 == 0:
                  skip = st.text_input("    ➡ For Going to the next stage, Enter (YES). Otherwise (NO): ").strip().lower()
                  if skip == "yes":
                    st.markdown(f"\n  🎉 Hurray! You have entered {entered_correct_words} Correct Words! 🏆")
                    st.markdown("                        ---Moving to Next Stage---")
                    return


    elif n == 5:
 
        letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u']
        letter_bank = Counter(letters)
        common_words = top_n_list('en', 50000)
        valid_words = []
        for word in common_words:
            word = word.lower().strip()
            if len(word) != 5:
                continue
            word_count = Counter(word)
            if all(word_count[c] <= letter_bank[c] for c in word_count):
                valid_words.append(word)
        words = sorted(valid_words)
        total_words = len(words)
        entered_correct_words = 0

        st.markdown("                                     ❗You Have to Enter at least 20 words to finish this stage ❗")
        st.markdown(f"Total Words: {total_words}") 
        st.markdown(" Start Entering Words One By One.")
        r = total_words

        for _ in range(r):
            p=0
            while True:
                x = st.text_input("➡️  ", key=f"word_input_{p}").strip().lower()
                if x:
                 if x in words:
                    total_words -= 1
                    entered_correct_words += 1
                    st.markdown(f"  ✅ Entered Correct Word                                                          Correct words entered: {entered_correct_words}   Remaining words: {total_words}")
                    break
                 else:
                    st.markdown(f"  ❌ Incorrect Word. Please enter a valid word below.    Letters Allowed {letters}")
            p+=1
            if entered_correct_words >= 20:
              if entered_correct_words % 2 == 0:
                skip = st.text_input("    ➡ For Going to the next stage, Enter (YES). Otherwise (NO): ").strip().lower()
                if skip == "yes":
                    st.markdown(f"\n  🎉 Hurray! You have entered {entered_correct_words} Correct Words! 🏆")
                    st.markdown("                        ---Moving to Next Stage---")
                    return


    elif n == 6:
        letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g']
        letter_bank = Counter(letters)
        common_words = top_n_list('en', 50000)
        valid_words = []
        for word in common_words:
            word = word.lower().strip()
            if len(word) != 6:
                continue
            word_count = Counter(word)
            if all(word_count[c] <= letter_bank[c] for c in word_count):
                valid_words.append(word)
        words = sorted(valid_words)
        total_words = len(words)
        entered_correct_words = 0

        st.markdown("                                     ❗You Have to Enter at least 20 words to finish this stage ❗")
        st.markdown(f"Total Words: {total_words}") 
        st.markdown(" Start Entering Words One By One.")
        r = total_words

        for _ in range(r):
            p=0
            while True:
                x = st.text_input("➡️  ", key=f"word_input_{p }").strip().lower()
                if x:
                 if x in words:
                    total_words -= 1
                    entered_correct_words += 1
                    st.markdown(f"  ✅ Entered Correct Word                                                          Correct words entered: {entered_correct_words}   Remaining words: {total_words}")
                    break
                 else:
                    st.markdown(f"  ❌ Incorrect Word. Please enter a valid word below.")
                    st.markdown(f"                      Letters Allowed {letters}")
                p+=1
            if entered_correct_words >= 20:
              if entered_correct_words % 2 == 0:
                skip = st.text_input("  ➡ For Going to the next stage, Enter (YES). Otherwise (NO): ").strip().lower()
                if skip == "yes":
                    st.markdown(f"\n  🎉 Hurray! You have entered {entered_correct_words} Correct Words! 🏆")
                    st.markdown("                        ---Moving to Next Stage---")
                    return


    elif n == 7:
        letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g', 'b', 'y']
        letter_bank = Counter(letters)
        common_words = top_n_list('en', 50000)
        valid_words = []
        for word in common_words:
            word = word.lower().strip()
            if len(word) != 7:
                continue
            word_count = Counter(word)
            if all(word_count[c] <= letter_bank[c] for c in word_count):
                valid_words.append(word)
        words = sorted(valid_words)
        total_words = len(words)
        entered_correct_words = 0

        st.markdown("                                     ❗You Have to Enter at least 20 words to finish this stage ❗")
        st.markdown(f"Total Words: {total_words}")
        st.markdown(" Start Entering Words One By One.")

        r = total_words

        for _ in range(r):
            p=0
            while True:
                x = st.text_input("➡️  ", key=f"word_input_{p }").strip().lower()
                if x:
                 if x in words:
                    total_words -= 1
                    entered_correct_words += 1
                    st.markdown(f"  ✅ Entered Correct Word                                                          Correct words entered: {entered_correct_words}   Remaining words: {total_words}")
                    break
                 else:
                    st.markdown(f"  ❌ Incorrect Word. Please enter a valid word below. ")
                    st.markdown(f"                      Letters Allowed {letters}")
                p+=1
            if entered_correct_words >= 20:
             if entered_correct_words % 2 == 0:
                skip = st.text_input("  ➡ For Going to the next stage, Enter (YES). Otherwise (NO): ").strip().lower()
                if skip == "yes":
                    st.markdown(f"\n  🎉 Hurray! You have entered {entered_correct_words} Correct Words! 🏆")
                    st.markdown("                        ---Moving to Next Stage---")
                    return


    elif n == 8:
        letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g', 'b']
        letter_bank = Counter(letters)
        common_words = top_n_list('en', 50000)
        valid_words = []
        for word in common_words:
            word = word.lower().strip()
            if len(word) != 8:
                continue
            word_count = Counter(word)
            if all(word_count[c] <= letter_bank[c] for c in word_count):
                valid_words.append(word)
        words = sorted(valid_words)
        total_words = len(words)
        entered_correct_words = 0

        st.markdown("                                     ❗You Have to Enter at least 20 words to finish this stage ❗")
        st.markdown(f"Total Words: {total_words}")
        st.markdown(" Start Entering Words One By One.")

        r = total_words

        for _ in range(r):
            p=0
            while True:
                x = st.text_input("➡️  ", key=f"word_input_{p }").strip().lower()
                if x:
                 if x in words:
                    total_words -= 1
                    entered_correct_words += 1
                    st.markdown(f"  ✅ Entered Correct Word                                                          Correct words entered: {entered_correct_words}   Remaining words: {total_words}")
                    break
                 else:
                    st.markdown(f"  ❌ Incorrect Word. Please enter a valid word below.")
                    st.markdown(f"                      Letters Allowed {letters}")
                p+=1
            if entered_correct_words >= 20 :
              if entered_correct_words % 2 == 0:
                skip = st.text_input("  ➡ For Going to the next stage, Enter (YES). Otherwise (NO): ").strip().lower()
                if skip == "yes":
                    st.markdown(f"\n  🎉 Hurray! You have entered {entered_correct_words} Correct Words! 🏆")
                    st.markdown("                        ---Moving to Next Stage---")
                    return


    elif n == 9:
 
        letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g', 'b', 'y']
        letter_bank = Counter(letters)
        common_words = top_n_list('en', 50000)
        valid_words = []
        for word in common_words:
            word = word.lower().strip()
            if len(word) != 9:
                continue
            word_count = Counter(word)
            if all(word_count[c] <= letter_bank[c] for c in word_count):
                valid_words.append(word)
        words = sorted(valid_words)
        total_words = len(words)
        entered_correct_words = 0

        st.markdown("                                     ❗You Have to Enter at least 20 words to finish this stage ❗")
        st.markdown(f"Total Words: {total_words}")
        st.markdown(" Start Entering Words One By One.")

        r = total_words

        for _ in range(r):
            p=0
            while True:
                x = st.text_input("➡️  ", key=f"word_input_{p }").strip().lower()
                if x:
                 if x in words:
                    total_words -= 1
                    entered_correct_words += 1
                    st.markdown(f"  ✅ Entered Correct Word                                                          Correct words entered: {entered_correct_words}   Remaining words: {total_words}")
                    break
                 else:
                    st.markdown(f"❌ Incorrect Word. Please enter a valid word below.")
                    st.markdown(f"                      Letters Allowed {letters}")
            p+=1
            if entered_correct_words >= 20:
              if entered_correct_words % 2 == 0:
                skip = st.text_input("  ➡ For Going to the next stage, Enter (YES). Otherwise (NO): ").strip().lower()
                if skip == "yes":
                    st.markdown(f"\n  🎉 Hurray! You have entered {entered_correct_words} Correct Words! 🏆")
                    st.markdown("                        ---Moving to Next Stage---")
                    return


    elif n == 10:
        letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g', 'b', 'y', 'f']
        letter_bank = Counter(letters)
        common_words = top_n_list('en', 50000)
        valid_words = []
        for word in common_words:
            word = word.lower().strip()
            if len(word) != 10:
                continue
            word_count = Counter(word)
            if all(word_count[c] <= letter_bank[c] for c in word_count):
                valid_words.append(word)
        words = sorted(valid_words)
        total_words = len(words)
        entered_correct_words = 0

        st.markdown("                                     ❗You Have to Enter at least 20 words to finish this stage ❗")
        st.markdown(f"Total Words: {total_words}")
        st.markdown(" Start Entering Words One By One.")

        r = total_words

        for _ in range(r):
            p=0
            while True:
                x = st.text_input("➡️  ", key=f"word_input_{p }").strip().lower()
                if x:
                 if x in words:
                    total_words -= 1
                    entered_correct_words += 1
                    st.markdown(f"  ✅ Entered Correct Word                                                          Correct words entered: {entered_correct_words}   Remaining words: {total_words}")
                    break
                 else:
                    st.markdown(f"  ❌ Incorrect Word. Please enter a valid word below. ")
                    st.markdown(f"                      Letters Allowed {letters}")
            p+=1
            if entered_correct_words >= 20:
             if entered_correct_words % 2 == 0:
                skip = st.text_input("➡ For Going to the next stage, Enter (YES). Otherwise (NO): ").strip().lower()
                if skip == "yes":
                    st.markdown(f"\n  🎉 Hurray! You have entered {entered_correct_words} Correct Words! 🏆")
                    st.markdown("                        ---Moving to Next Stage---")
                    return


    elif n == 11:
        letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g', 'b', 'y', 'f', 'v']
        letter_bank = Counter(letters)
        common_words = top_n_list('en', 50000)
        valid_words = []
        for word in common_words:
            word = word.lower().strip()
            if len(word) != 11:
                continue
            word_count = Counter(word)
            if all(word_count[c] <= letter_bank[c] for c in word_count):
                valid_words.append(word)
        words = sorted(valid_words)
        total_words = len(words)
        entered_correct_words = 0

        st.markdown("                                     ❗You Have to Enter at least 20 words to finish this stage ❗")
        st.markdown(f"Total Words: {total_words}")
        st.markdown(" Start Entering Words One By One.")

        r = total_words

        for _ in range(r):
            p=0
            while True:
                x = st.text_input("➡️  ", key=f"word_input_{p}").strip().lower()
                if x:
                 if x in words:
                    total_words -= 1
                    entered_correct_words += 1
                    st.markdown(f"  ✅ Entered Correct Word                                                          Correct words entered: {entered_correct_words}   Remaining words: {total_words}")
                    break
                 else:
                    st.markdown(f"  ❌ Incorrect Word. Please enter a valid word below.")
                    st.markdown(f"                      Letters Allowed {letters}")
            p+=1
            if entered_correct_words >= 20:
              if entered_correct_words % 2 == 0:
                skip = st.text_input("  ➡ For Going to the next stage, Enter (YES). Otherwise (NO): ").strip().lower()
                if skip == "yes":
                    st.markdown(f"\n  🎉 Hurray! You have entered {entered_correct_words} Correct Words! 🏆")
                    st.markdown("                        ---Moving to Next Stage---")
                    return


    elif n == 12:
        letters = ['e', 'a', 'r', 't', 'l', 'n', 's', 'o', 'd', 'm', 'p', 'c', 'h', 'i', 'u', 'g', 'b', 'y', 'f', 'v', 'k']
        letter_bank = Counter(letters)
        common_words = top_n_list('en', 50000)
        valid_words = []
        for word in common_words:
            word = word.lower().strip()
            if len(word) != 12:
                continue
            word_count = Counter(word)
            if all(word_count[c] <= letter_bank[c] for c in word_count):
                valid_words.append(word)
        words = sorted(valid_words)
        total_words = len(words)
        entered_correct_words = 0

        st.markdown("                                     ❗You Have to Enter at least 20 words to finish this stage ❗")
        st.markdown(f"Total Words: {total_words}")
        st.markdown(" Start Entering Words One By One.")

        r = total_words

        for _ in range(r):
            p=0
            while True:
                x = st.text_input("➡️  ", key=f"word_input_{p }").strip().lower()
                if x:
                 if x in words:
                    total_words -= 1
                    entered_correct_words += 1
                    st.markdown(f"  ✅ Entered Correct Word                                                          Correct words entered: {entered_correct_words}   Remaining words: {total_words} ")
                    break
                 else:
                    st.markdown(f"  ❌ Incorrect Word. Please enter a valid word below. Letters Allowed {letters}")
                p+=1
            if entered_correct_words >= 20:
              if entered_correct_words % 2 == 0:
                skip = st.text_input(" ➡ For Going to the next stage, Enter (YES). Otherwise (NO): ").strip().lower()
                if skip == "yes":
                    st.markdown(f"\n🎉 Hurray! You have entered {entered_correct_words} Correct Words! 🏆")
                    st.markdown("                        ---Moving to Next Stage---")
                    return
def main():
    inc=1
    num_of_letters_for_each_word=difficuilty(inc)
    while True:
    #    num_of_letters_for_each_word=difficuilty_easy()
       letters=give_random_letters_according_to_difficuilty_level(num_of_letters_for_each_word)
       print (f"Make words from the follwing letters")
       st.markdown(f"            {letters}") 
       st.markdown(f" ❗ Each Word must be of {num_of_letters_for_each_word} letters")
       words_for_each_num_of_letter(num_of_letters_for_each_word)
       
       level=st.text_input("""Do you want to move to the next stage? 📈
                   Enter 'Yes' to move to the next stage, 'No' to exit""").lower()
       if level=='yes':
           break
       st.markdown(                            "🌟" * inc + " Moving to the next Difficulty Level " + "🌟" * inc)  
       inc+=1

    st.markdown("                                                       ---- Goodbye 👋 ----")

main()
