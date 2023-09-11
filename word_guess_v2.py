"""
La biblioteca random se utiliza para generar números aleatorios.
"""
import random

# Diccionarios de traducción para español e inglés
translations = {
    'en': {
        'welcome': "What is your name? ",
        'good_luck': "Good Luck!",
        'choose_source': "Do you want to use pre-stored words or enter your own words? (pre-stored/enter): ",
        'custom_word_prompt': "Enter custom word {num} (or press Enter to finish): ",
        'invalid_word': "Please enter a valid word.",
        'no_custom_words': "You didn't enter any custom words.",
        'guess_prompt': "Guess a character: ",
        'win_message': "You Win",
        'lose_message': "You Lose",
        'final_score': "Final score:",
        'more_guesses': "You have {num} more guesses",
        'correct_word': "The word is:",
        'current_score': "Your score:",
    },
    'es': {
        'welcome': "¿Cuál es tu nombre? ",
        'good_luck': "¡Buena suerte!",
        'choose_source': "¿Deseas usar palabras predefinidas o ingresar tus propias palabras? (predefinidas/ingresar): ",
        'custom_word_prompt': "Ingresa la palabra personalizada {num} (o presiona Enter para terminar): ",
        'invalid_word': "Por favor, ingresa una palabra válida.",
        'no_custom_words': "No ingresaste ninguna palabra personalizada.",
        'guess_prompt': "Adivina una letra: ",
        'win_message': "Ganaste",
        'lose_message': "Perdiste",
        'final_score': "Puntuación final:",
        'more_guesses': "Tienes {num} intentos más",
        'correct_word': "La palabra es:",
        'current_score': "Tu puntuación:",
    }
}


def choose_language():
    """
    Pregunta al usuario que seleccione su idioma y devuelve el código de idioma correspondiente.

    Returns:
        str: El código de idioma seleccionado por el usuario ("en" para inglés o "es" para español).
    """
    while True:
        lang_choice = input(
            "Choose a language (English(en)/Español(es)): ").strip().lower()
        if lang_choice in translations:
            return lang_choice
        else:
            print("Invalid choice. Please choose English or Español.")


def choose_word_source(lang):
    """
    Permite al usuario seleccionar una fuente de palabras (prealmacenadas o propias) y devuelve una palabra aleatoria de la fuente elegida.

    Args:
        lang (str): El código de idioma para mostrar mensajes al usuario.

    Returns:
        str: Una palabra aleatoria de la fuente seleccionada (prealmacenadas o propias).
    """
    while True:
        print("Choose a word source:")
        print("1. Pre-stored")
        print("2. Enter your own")
        choice = input(f"Enter {1} or {2}: ")
        if choice == "1":
            return random.choice(pre_stored_words)
        if choice == "2":
            custom_words = []
            for i in range(12):
                custom_word = input(
                    translations[lang]['custom_word_prompt'].format(num=i + 1)).lower()
                if custom_word == "":
                    break
                if custom_word.isalpha():
                    custom_words.append(custom_word)
                else:
                    print(translations[lang]['invalid_word'])
            if custom_words:
                return random.choice(custom_words)
            print(translations[lang]['no_custom_words'])
        print("Invalid choice. Please enter 1 or 2.")


def save_score(username, scores, attempts):
    """
    Guarda una lista de puntajes en un archivo llamado "scores.txt".

    Args:
        scores (list): Una lista de cadenas que representan los puntajes.
    """
    with open('score.txt', 'a', encoding="utf-8") as file:
        file.write(
            f'Username: {username}, Score: {scores}, Attempts: {attempts}\n')


# Inicialización del juego
lang = choose_language()
name = input(translations[lang]['welcome'])
print(translations[lang]['good_luck'], name)

pre_stored_words = ['rainbow', 'computer', 'science', 'programming',
                    'python', 'mathematics', 'player', 'condition',
                    'reverse', 'water', 'board', 'geeks']

word = choose_word_source(lang)

print(translations[lang]['guess_prompt'])

guesses = ['']
turns = [12]
scores = [0]

while turns > 0:
    failed = [0]
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")

            failed += 1

    if failed == 0:
        print(translations[lang]['win_message'])
        print(translations[lang]['correct_word'], word)
        scores += 1
        print(translations[lang]['current_score'], scores)
        break

    print()

    while True:
        guess = input(translations[lang]['guess_prompt']).lower()

        if len(guess) == 1 and guess.isalpha():
            break
        print("Please enter a single letter.")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print(translations[lang]['more_guesses'].format(num=turns))

        if turns == 0:
            print(translations[lang]['lose_message'])

        # Llamar a save_score aquí
        save_score(name, scores, 12 - turns)

print(translations[lang]['final_score'], scores)
