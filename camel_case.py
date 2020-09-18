

#this function filters only string value
def Remove_noneString_values(word):
    return ''.join(filter(str.isalpha, word))


"""This capitalizes the first letter of each word except the first word and joins all the words together"""
def Camel_case(sentence):
    if sentence:
        splitSentence = sentence.strip().split()
        #create a new list and start with the fist word of the sentence in lower case
        capitalized_sentence = [splitSentence[0].lower()] # 
        for i in range(1, len(splitSentence)):
            capitalized_sentence.append(splitSentence[i].capitalize())
        # remove none string value from the sentence
        filtered = [Remove_noneString_values(word) for word in capitalized_sentence]
        return ''.join(filtered) #put the words to gether
    else:
        return

def main():
    sentence = input("Please Enter a senctence ")
    result = Camel_case(sentence)
    print(result)

if __name__ == '__main__':
    main()