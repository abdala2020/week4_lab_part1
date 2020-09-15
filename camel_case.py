

#this function filters only string value
def validator(word):
    return ''.join(filter(str.isalpha, word))


"""This capitalizes the first letter of each word except the first word and joins all the words together"""
def capitalize(sentence):
    if sentence:
        splitSentence = sentence.strip().split()
        #create a new list and start with the fist word of the sentence in lower case
        capitalized_sentence = [splitSentence[0].lower()] # 
        for i in range(1, len(splitSentence)):
            capitalized_sentence.append(splitSentence[i].capitalize())
        # remove none string value from the sentence
        filtered = [validator(word) for word in capitalized_sentence]
        return ''.join(filtered) #put the words to gether
    else:
        return

    

    



def main():
    sentence = input("Please Enter a senctence ")
    
    result = capitalize(sentence)
    print(result)

main()