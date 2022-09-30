
cantik = 1
bilangan_X = input("Masukan X :")

def check(n):
    if str(n) == str(n)[0] * len(str(n)):
        return True
    else:
        return False
dibagi_2 = int(bilangan_X)%2
dibagi_5 = int(bilangan_X) % 5


if dibagi_2 != 0 and dibagi_5 != 0 :
    #print("Mohon Tunggu Program sedang Bekerja . . .")
    while True:
        mod = cantik % int(bilangan_X)
        if mod == 0:
            if check(cantik) == True:
                print(f"Bilangan Cantik Terkecil yang habis dibagi {bilangan_X} ialah {cantik}")
                break
            else:
                cantik = cantik + 1;
                
                
        else:
            cantik = cantik + 1;
            
           
else:
    print(f"Bilangan {bilangan_X}  tidak lolos selesksi karena bilangan {bilangan_X}  tidak habis dibagi 2 dan tidak habis di bagi 5")

    



        







