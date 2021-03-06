word_list = open('wordleanswers.txt')

words_to_search = []
number_of_guesses = 0
start_words = ['fjord', 'waltz', 'quick', 'gyres', 'nymph']
greened_letters = ""

for word in word_list:
    if len(word) == 6:
        to_add = word.strip("\n")
        words_to_search.append(to_add)

while number_of_guesses != 6:
    if len(words_to_search) > 10:
        current_guess = start_words[number_of_guesses]
    else:
        print("sorting...")
        options = words_to_search
        options_score = {}

        current_option = ""
        current_highest = -1

        for word in options:
            word_score = 0
            for letter in word:
                for word_to_check in options:
                    if letter in word_to_check and word_to_check.count(letter) <= word.count(letter) and letter is not word[word_to_check.index(letter)]:
                        word_score += 1 / (word.count(letter) / word_to_check.count(letter))
                    elif word is not word_to_check and not (word_to_check.count(letter) >= word.count(letter) or word_to_check.count(
                                letter) <= word.count(letter)):
                        if letter is word_to_check[word.index(letter)]:
                            word_score += 2

            options_score.update({word: word_score})
            for key, value in options_score.items():
                if value > current_highest:
                    current_option = key
        current_guess = current_option

        if current_guess in words_to_search:
            words_to_search.pop(words_to_search.index(current_guess))

    print("Green = g, Yellow = y, grey = r")
    print("Please use the legend above to fill in your results from the wordle: ")
    print(current_guess)
    results = input()

    for letter in current_guess:
        current_letter_index = current_guess.index(letter)
        for word in words_to_search:
            if word != "":
                if results[current_guess.index(letter)] == "g" and (current_guess[current_letter_index] != word[current_letter_index] or current_guess[current_letter_index] not in word):
                    words_to_search[words_to_search.index(word)] = ""

                elif results[current_guess.index(letter)] == "r":
                    if current_guess.count(letter) == 1:
                        if current_guess[current_letter_index] in word:
                            words_to_search[words_to_search.index(word)] = ""
                    else:
                        if current_guess[current_letter_index] is word[current_letter_index]:
                            words_to_search[words_to_search.index(word)] = ""

                elif results[current_guess.index(letter)] == "y":
                    in_word = letter
                    if letter not in word or word[current_letter_index] is letter:
                        words_to_search[words_to_search.index(word)] = ""

    num_of_posses = 0
    new_words = []
    for word in words_to_search:
        if word != "":
            new_words.append(word)

    words_to_search = new_words
    print(words_to_search)

    number_of_guesses += 1
