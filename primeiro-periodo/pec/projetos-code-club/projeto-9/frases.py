def main():

    textSpeakDictionary = {
        "rs" : "risos",  
        "tmb" : "também" 
    }

    sentence = input("Insira uma frase para traduzir: ").lower() 
    wordsToTranslate = sentence.split()
    translatedSentence = ""

    for word in wordsToTranslate: 
        if word in textSpeakDictionary: 
            translatedSentence += textSpeakDictionary[word] + " "
        else:
            translatedSentence += word + " "

    print("===>")
    print(translatedSentence)

if __name__ == "__main__":
    main()