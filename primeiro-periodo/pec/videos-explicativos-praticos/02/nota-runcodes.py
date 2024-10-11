def desconto(dias):
    return dias * 5

def main():
    d = int(input())
    desc = desconto(d)
    print(f'{desc}')

if __name__ == '__main__':
    main()