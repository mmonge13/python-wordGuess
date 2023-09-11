"""
La biblioteca random se utiliza para generar números aleatorios.
"""
import random

def get_player_name():
    """
    Solicita al usuario que ingrese su nombre y lo devuelve.
    """
    return input("What is your name? ")

def choose_random_word():
    """
    Elige una palabra al azar de una lista de palabras predefinidas y la devuelve.
    """
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']
    return random.choice(words)


def main():
    """
    Esta función implementa el juego de adivinanza de palabras.
    El jugador debe adivinar una palabra desconocida dentro de un número limitado de intentos.

    Parámetros:
    Ninguno

    Retorna:
    Ninguno

    Uso:
    Llame a esta función para iniciar el juego.

    Ejemplo:
    main()
    """
    name = get_player_name()
    print("Good Luck !", name)

    word = choose_random_word()
    print("Guess the characters")

    guesses = ['']

    # Cualquier número de turnos puede usarse aquí
    turns = 12

    while turns > 0:
        # Cuenta el número de veces que un usuario falla
        failed = 0

        # Recorre todos los caracteres de la palabra
        for char in word:
            # Compara ese carácter con los caracteres en 'guesses'
            if char in guesses:
                print(char, end=" ")
            else:
                print("_")
                # Incrementa 'failed' por cada falla
                failed += 1

        if failed == 0:
            # El usuario gana el juego si 'failed' es 0
            # y se muestra 'You Win' como resultado
            print("You Win")
            # Se imprime la palabra correcta
            print("The word is:", word)
            break

        # if user has input the wrong alphabet then
        # it will ask user to enter another alphabet
        print()
        guess = input("Guess a character: ")

        # Cada carácter ingresado se almacena en 'guesses'
        guesses += guess

        # Comprueba si el carácter ingresado coincide con la palabra
        if guess not in word:
            turns -= 1
            # Si el carácter no coincide con la palabra, se muestra "Wrong"
            print("Wrong")
            # Se muestra el número de turnos restantes para el usuario
            print("You have", turns, 'more guesses')

            if turns == 0:
                print("You Lose")

if __name__ == "__main__":
    main()
