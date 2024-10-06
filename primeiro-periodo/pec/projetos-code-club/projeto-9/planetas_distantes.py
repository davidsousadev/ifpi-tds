
distances = {
    "jupiter"    : 628730000,
    "mercurio"   : 91700000,
    "marte"      : 54600000,
    "netuno"     : 4350000000,
    "plutao"     : 7370000000, 
    "saturno"    : 1275000000,
    "urano"      : 2720000000,
    "venus"      : 41400000,
}




def main():
    planet = input("Digite um planeta: ").lower()
    distance = distances[planet]
    print(planet , "está a" , distance , "km da Terra")




if __name__ == '__main__':
    main()