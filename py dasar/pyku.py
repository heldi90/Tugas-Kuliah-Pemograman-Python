
indo = int(input("Bhs Indonesia : "))
ipa = int(input("ipa : "))
matematika = int(input("matematika : "))

tidak_lulus = 0

if indo < 60 :
    tidak_lulus = 1

if ipa < 60 :
    tidak_lulus = 1

if matematika < 70 :
    tidak_lulus = 1

if tidak_lulus > 0 :
    print ("Status Kelulusan : TIDAK LULUS")
else :
    print ("Status Kelulusan : LULUS")
