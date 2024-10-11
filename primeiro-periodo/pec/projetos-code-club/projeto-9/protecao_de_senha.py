passwordDictionary = {

        "sohail" : "letmein",
        "programador": "acesso"
    
    }
def main():
    print("Programa super secreto")
    print("====================")

    login_attempts = 0

    while login_attempts < 3:
        name = input("Nome : ").lower()
        password = input("Senha : ").lower()

        if name in passwordDictionary and passwordDictionary[name] == password:
            print("\nBEM-VINDO", name.upper())
            break
        else:
            print("Acesso negado\n")
        login_attempts += 1
        if login_attempts == 3:
            print("Acesso bloqueado.")
            break
    
    
    

if __name__ == '__main__':
    main()