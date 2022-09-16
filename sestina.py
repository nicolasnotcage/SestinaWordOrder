# Still very rough, but the idea is there

words = ["whine", "shadow", "blast", "tunnel", "rest", "letter"]
stanza_dict = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}


def permutate(sestina_words):
    temp_words = [0, 0, 0, 0, 0, 0]

    # TODO: Is there some bigger algorithmic pattern here?
    # for num in range(0, len(temp_words)):
    #     if num % 2 == 0:
    #         temp_words[num] = sestina_words[num - 1]

    temp_words[1] = sestina_words[0]
    temp_words[3] = sestina_words[1]
    temp_words[5] = sestina_words[2]
    temp_words[4] = sestina_words[3]
    temp_words[2] = sestina_words[4]
    temp_words[0] = sestina_words[5]

    return temp_words


def sestina_me(six_words, final_dict, count=1):
    # Stopping condition
    if final_dict[6]:
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
