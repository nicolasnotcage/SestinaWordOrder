# Program takes a list of words to be used as the end-words in a sestina and generates their order throughout
# all seven stanzas of the poem
words = ["whine", "shadow", "blast", "tunnel", "rest", "letter"]
stanza_dict = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}


def permutate(sestina_words):
    # The algorithm for the permutation has a pattern where we first subtract by 5, then add by 4, then subtract by 3,
    # then add by 2, and finally subtract by 1.
    temp_words = [0, 0, 0, 0, 0, 0]

    # Stores the index of the element of sestina_list that will next be placed in temp_words.
    location = 5

    # Used to indicate the amount by which we add or subtract for any given index and is decremented after each pass.
    scaler = 5

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


def sestina_me(six_words, final_dict, count=1):
    # Stopping condition
    if count == 1:
        final_dict[count] = six_words
        count += 1
        sestina_me(six_words, final_dict, count)

    elif final_dict[6]:
        # Final stanza consists of only three lines, so for simplicity, we'll handle manually
        final_dict[7] = [six_words[0], six_words[4], six_words[5]]
        return final_dict

    # Extremely iterative recursive solution
    else:
        new_perm = permutate(six_words)
        final_dict[count] = new_perm
        count += 1
        sestina_me(new_perm, final_dict, count)

    return final_dict


final_form = sestina_me(words, stanza_dict)

# Prints list of stanzas
for stanza in final_form:
    print("Stanza ", stanza)
    print(final_form[stanza])
