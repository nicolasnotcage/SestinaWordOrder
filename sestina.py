# Program takes a list of words to be used as the end-words in a sestina and generates their order throughout
# all stanzas of the poem. While a sestina traditionally has only six words, this program can apply the sestina
# permutation algorithm to word lists of arbitrary size.

def permutate(sestina_words):
    # The algorithm for the permutation of the traditional sestina has a pattern where we first subtract by 5,
    # then add by 4, then subtract by 3, then add by 2, and finally subtract by 1. Applying this method to the length
    # of the initial list of words allows us to perform this permutation for any number of words.

    # Creates temporary list for permutation of the length of the passed list
    temp_words = [None] * len(sestina_words)

    # Stores the index of the element of sestina_words that will next be placed in temp_words.
    location = len(sestina_words) - 1

    # Used to indicate the amount by which we add or subtract for any given index and is decremented after each pass.
    # Begins as equal to the total number of words passed to the permutation function.
    scaler = len(sestina_words) - 1

    for num in range(0, len(temp_words)):
        # Even indices will occur when we are subtracting, and odd indices occur when we add.
        if num % 2 == 0:
            temp_words[num] = sestina_words[location]
            location -= scaler

        else:
            temp_words[num] = sestina_words[location]
            location += scaler

        scaler -= 1

    return temp_words


# The main function for the program. Accepts list of words. Users can specify whether the final envoi should be
# reversed or not. envoi=False will return normal ECA tercet, and envoi=True will return ACE tercet.
def sestina_me(words, final_dict=None, count=1, envoi=False):
    # Needs better error handling, but it works for current needs.
    if len(words) <= 2:
        return "ERROR: The word count must be greater than two words."

    elif final_dict is None and count == 1:
        # Initializes dictionary to store word order by stanza number
        final_dict = {}
        for i in range(1, len(words) + 1):
            final_dict[i] = ''

        # Assigns the original word order to the first stanza
        final_dict[count] = words
        count += 1
        sestina_me(words, final_dict, count, envoi)

    # Stopping condition
    elif final_dict[len(words)]:
        # Final stanza should contain half of the lines of the original stanza size (a standard 6 line stanza sestina
        # has a final 3 line stanza). The below code halves the total number of lines. If the number of words is odd,
        # then 1 is added to the final value to be used if desired by the writer.
        i = int(len(words) / 2)

        if len(words) % 2 != 0:
            i += 1

        final_stanza = []

        for num in range(-i, 0):
            final_stanza.append(words[len(words) + num])

        if envoi:
            final_stanza.reverse()

        final_dict[len(words) + 1] = final_stanza

        return final_dict

    # Permutates word order and recursively passes new permutation
    else:
        new_perm = permutate(words)
        final_dict[count] = new_perm
        count += 1
        sestina_me(new_perm, final_dict, count, envoi)

    return final_dict


test_words = ["whine", "shadow", "blast", "tunnel", "rest", "letter"]
final_form = sestina_me(test_words)

big_test_words = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
big_final_form = sestina_me(big_test_words)

small_test_words = ["A", "B", "C"]
small_final_form = sestina_me(small_test_words)

bigger_test_words = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
bigger_final_form = sestina_me(bigger_test_words, envoi=True)

# Printing results of standard sestina with six lines
print("Standard sestina with six lines:")
for stanza in final_form:
    print("Stanza ", stanza)
    print(final_form[stanza])

print()

# Printing results of larger sestina with ten lines
print("Larger sestina with ten lines:")
for stanza in big_final_form:
    print("Stanza ", stanza)
    print(big_final_form[stanza])

print()

# Printing results of smaller sestina with two lines
print("Smaller sestina with three lines:")
for stanza in small_final_form:
    print("Stanza ", stanza)
    print(small_final_form[stanza])

print()

# Largest sestina with eleven lines and reversed envoi
print("Largest sestina with eleven lines:")
for stanza in bigger_final_form:
    print("Stanza ", stanza)
    print(bigger_final_form[stanza])


