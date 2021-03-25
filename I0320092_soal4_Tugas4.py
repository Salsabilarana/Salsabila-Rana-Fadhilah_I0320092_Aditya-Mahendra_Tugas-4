#pendaftaran kursus online
usia = int(input("Masukan usia :"))
ujian = (input("Anda lulus ujian atau tidak (Y/T):"))

if (usia>=21) and (ujian == "Y"):
    print("Anda dapat mendaftar di kursus")
else :
    print("Anda tidak dapat mendaftar di kursus")