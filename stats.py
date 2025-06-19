def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    characters_dict = {}
    for c in book_text:
        c = c.lower()
        if c not in characters_dict:
            characters_dict[c] = 1
        else:
            characters_dict[c] += 1
    return(characters_dict)

def sort_dict(dict):
    # helper function for sorting
    def sort_on(dict):
        return dict["num"]
    # create a list of dictionaries with the same key/value so we can sort on it
    dict_list = []
    for i in dict:
        dict_list.append({"char": i, "num": dict[i]})
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

test_dict = {'t': 29493, 'h': 19176, 'e': 44538}

sort_dict(test_dict)