import string


def create_dict():
    dictionary = {}
    file_gettysburg = open("gettysburg.txt", "r")
    file_stopwords = open("stopwords.txt")
    stopwords = file_stopwords.read().splitlines()

    for line in file_gettysburg:
        line = line.lower().split()
        for word in line:
            if word in stopwords:
                continue
            word = word.strip(string.whitespace)
            word = word.strip(string.punctuation)
            add_to_dict(word, dictionary)

    file_gettysburg.close()
    file_stopwords.close()
    return dictionary


def add_to_dict(word, dictionary):
    for key in dictionary.keys():
        if key == word:
            dictionary[key] += 1
            return dictionary
    else:
        dictionary[word] = 1
        return dictionary


def create_html(dictionary):
    file_word_cloud = open("WordCloud.html", "w")
    file_word_cloud.write('\
<!DOCTYPE html>\n\
<html>\n\
    <head lang="en">\n\
        <meta charset="UTF-8">\n\
        <title>Tag Cloud Generator</title>\n\
    </head>\n\
    <body>\n\
        <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">\n')

    for key in dictionary.keys():
        file_word_cloud.write('\
            <span style="font-size:')
        file_word_cloud.write(str(dictionary[key]*10))
        file_word_cloud.write('px">')
        file_word_cloud.write(key)
        file_word_cloud.write('</span>\n')

    file_word_cloud.write('\
        </div>\n\
    </body>\n\
</html>')

    file_word_cloud.close()


create_html(create_dict())
