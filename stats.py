
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(content):
    word_count = len(content.split())
    return word_count

def get_num_character(content):
    
    # returns: a dictionary 

    # init stage 

    # problem: how to create key
    # sol:  dynamicly add new key when needed

    character_count = {}

    # ------------data preprocessing------------------

    # make all lowercase 
    cleaned_content = content.lower()

    # split content in string 
    split_content = cleaned_content.split()

    # loop the list
    
    for strings in split_content:
        for character in strings:
            if character not in character_count:
                character_count[character] = 1
            else:
                character_count[character] += 1

    return character_count
    

# ----------------------polish------------------------------------


def sort_on(items):
    return items["num"]



def sort_dictionary(dictionary):
    dict_list = []
    for key, value in dictionary.items():
        dict_list.append({"char":key, "num" : value})
   
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list



