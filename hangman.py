import random


def random_word(some_list):
    offer = random.choice(some_list)
    if len(offer) > 3:
        return offer
    else:
        return random_word(some_list)


def choose_difficulty():
    level = input("Please, choose a level (e/m/h): ")
    if level == 'e':
        attempts_result = 10
        return attempts_result
    elif level == 'm':
        attempts_result = 8
        return attempts_result
    elif level == 'h':
        attempts_result = 6
        return attempts_result
    else:
        return choose_difficulty()


def check_for_not_printing(some_str, some_other_str):
    if some_str == some_other_str:
        return True
    else:
        return False


def guess(some_chr, some_sting):
    count = 0
    for character in some_sting:
        if character == some_chr:
            count += 1
    if count == 0:
        return False
    else:
        return count


wins = 0
loses = 0

play_coming = True
while play_coming:
    list_words = open("hangman_words.txt").read().splitlines()
    word = random_word(list_words)

    attempts = choose_difficulty()
    initial_attempts = attempts

    print(f'You have {attempts} attempts.')
    print("Please, use only small letters.")

    word_as_list = [x for x in word]
    string_for_not_printing_when_guessed = " ".join(word)

    letters_set = set(word_as_list)
    set_for_print = set(word_as_list)
    letters_until_now = []
    guessed_letters = []

    initial_output = len(word) * "_ "
    current_output = len(word) * "_ "

    print(initial_output)

    is_lost = False

    while letters_set:
        letter = input("Please, choose a letter ")
        if not letter.isalpha():
            print("This is not a letter.")
            print("------------------")
        elif letter in letters_until_now:
            print("You have tried this one.")
            print("------------------")
        else:
            letters_until_now.append(letter)
            if not guess(letter, word):
                print("The letter is not there.")
                attempts -= 1
                if attempts == 0:
                    print("You are dead!!!")
                    print(f"The word was: {word}.")
                    loses += 1
                    is_lost = True
                    break
                else:
                    print(f"You have {attempts} attempts remaining.")
                    print(current_output)
                    print("------------------")

            else:
                print(f"You have guessed {guess(letter, word)} letter(s).")
                print(f"You still have {attempts} attempts remaining.")
                print("------------------")
                guessed_letters.append(letter)
                letters_set.remove(letter)
                current_output = str()
                for element in word_as_list:
                    if element in guessed_letters:
                        current_output = current_output + f'{element} '
                    else:
                        current_output = current_output + "_ "
                if not check_for_not_printing(current_output, string_for_not_printing_when_guessed):
                    print(current_output)

    if not is_lost:
        print(f"Congratulations! You win! The word was: {word}.")
        print(f"You did it in {initial_attempts - attempts} attempts.")
        wins += 1

    print(f"The score is {wins}:{loses}")
    print("Do you want to play again?")
    play_again = input("Press (y) for Yes or (n) for No: ")
    if play_again == 'n':
        print(f"Final score: Wins: {wins}, Losses: {loses}")
        print("Bye, bye!")
        play_coming = False
