x = input()
for e in x:
    #print(f"Valor de e : {e}")
    if e  == ")":
        x = x.replace(":-)", "🙂")
        
    if e == "(":
        x = x.replace(":-(", "🙁")
        

print(f'{x}')