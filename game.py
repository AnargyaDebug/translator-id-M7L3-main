from speech import speech
from random import choice, randint
import time

difficulties = {
    "easy": ["spiel", "sprachen", "tee"],
    "medium": ["frühstück", "algorithmus", "kodierer"],
    "hard": ["krankenhaus", "maschine",
    "künstliche Intelligenz"],
    "extreme": ["mittagessen und frühstück", "speicherleck", "programmierbar"]
}

def play_game(difficulty):
    words = difficulties.get(difficulty, [])
    
    if not words:
        return
    
    score = 0

    for _ in range(5):
        random_word = choice(words)
        print(random_word)
        recognized_word = speech().lower()
        print(recognized_word)

        if random_word == recognized_word:
            score += 1
        else:
            print("Word was not the same")
        
        time.sleep(4)

    print(f"Score: {score}")
