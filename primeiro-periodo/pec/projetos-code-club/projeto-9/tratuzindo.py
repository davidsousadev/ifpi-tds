def main():

    textSpeakDictionary = {
        "rs" : "risos",  
        "tmb" : "também" 
    }

    print("Dicionário = ", textSpeakDictionary)

    print("\nrs =", textSpeakDictionary["rs"])

    key = input("\nO que você gostaria de converter? ")
    print(key, "=", textSpeakDictionary[key])

if __name__ == '__main__':
    main()