from idlelib.pyshell import usage_msg

punctuation_remove = (",.!?")
punctuation_space = ("'")

def find_3_letter_words(filename):
    """""
    Finds all the 3 letter words starting with B in a file
    :param filename: the name of the file
    :return: None
    """
    with open(filename) as f:
        #go line by line
        for line in f:
            #replace punctuation
                for p in punctuation_remove:
                    line = line.replace(p, "")
                for p in punctuation_space:
                    line = line.replace(p, "")
                words = line.split()
                # iterate over the list of words
                for word in words:
                    if len(word) == 3 and word[0] in["b" or "B"]:
                        print(word)
find_3_letter_words("input.txt")

