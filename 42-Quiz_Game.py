
print("Hoşgeldiniz!!!")
while True:
    skor = 0
    print("----SORULAR----")

    soru1=input("1-Aşağıdaki Şehirlerden hangisi Türkiye'nin başkentidir?\nA-Ankara\nB-Bakü\nC-Londra\nD-La Paz\nCevap :")
    soru1=soru1.upper()
    if soru1=="A":
        print("DOĞRU")
        skor=skor+10

    else:
        print("YANLIŞ")

    print("\n")

    soru2=input("2-Aşağıdaki Şehirlerden hangisi Azerbaycan'nın başkentidir?\nA-Londra\nB-Ankara\nC-Bakü\nD-Sofya\nCevap :")
    soru2=soru2.upper()
    if soru2=="C":
        print("DOĞRU")
        skor=skor+10

    else:
        print("YANLIŞ")
    print("\n")

    soru3=input("3-Aşağıdaki Şehirlerden hangisi Belçika'nın başkentidir?\nA-Pekin\nB-Kopenhag\nC-Buenos Aires\nD-Brüksel\nCevap :")
    soru3=soru3.upper()
    if soru3=="D":
        print("DOĞRU")
        skor=skor+10

    else:
        print("YANLIŞ")

    print("\n")

    soru4=input("4-Aşağıdaki Şehirlerden hangisi Bolivya'nın başkentidir?\nA-La Paz\nB-Kopenhag\nC-Brasilia\nD-Havana\nCevap :")
    soru4=soru4.upper()
    if soru4=="A":
        print("DOĞRU")
        skor=skor+10

    else:
        print("YANLIŞ")

    print("\n")



    soru5=input("5-Aşağıdaki Şehirlerden hangisi Brezilya'nın başkentidir?\nA-Londra\nB-Brasilia\nC-Pekin\nD-Havana\nCevap :")
    soru5=soru5.upper()
    if soru5=="B":
        print("DOĞRU")
        skor=skor+10

    else:
        print("YANLIŞ")

    print("\n")


    soru6=input("6-Aşağıdaki Şehirlerden hangisi Bulgaristan'nın başkentidir?\nA-Selanik\nB-Sofya\nC-Pekin\nD-Havana\nCevap :")
    soru6=soru6.upper()
    if soru6=="B":
        print("DOĞRU")
        skor=skor+10

    else:
        print("YANLIŞ")

    print("\n")

    soru7=input("7-Aşağıdaki Şehirlerden hangisi Arjantin'nın başkentidir?\nA-Pekin\nB-Selanik\nC-Brasilia\nD-Buenos Aires\nCevap :")
    soru7=soru7.upper()
    if soru7=="D":
        print("DOĞRU")
        skor=skor+10

    else:
        print("YANLIŞ")

    print("\n")


    soru8=input("8-Aşağıdaki Şehirlerden hangisi Çin'nın başkentidir?\nA-Pekin\nB-Selanik\nC-Brasilia\nD-Buenos Aires\nCevap :")
    soru8=soru8.upper()
    if soru8=="A":
        print("DOĞRU")
        skor=skor+10

    else:
        print("YANLIŞ")

    print("\n")


    soru9=input("9-Aşağıdaki Şehirlerden hangisi Küba'nın başkentidir?\nA-Ankara\nB-Selanik\nC-Havana\nD-Sofya\nCevap :")
    soru9=soru9.upper()
    if soru9=="C":
        print("DOĞRU")
        skor=skor+10

    else:
        print("YANLIŞ")

    print("\n")


    soru10=input("10-Aşağıdaki Şehirlerden hangisi Danimarka'nın başkentidir?\nA-İzmir\nB-La Paz\nC-Havana\nD-Kopenhag\nCevap :")
    soru10=soru10.upper()
    if soru10=="D":
        print("DOĞRU")
        skor=skor+10

    else:
        print("YANLIŞ")

    print("Skor:{}".format(skor))

    oyna=input("Tekrar Oynamak İstiyormusunuz?(Evet,Hayır):")
    oyna=oyna.upper()
    if oyna !="EVET":
        print("Byeee")
        quit()
