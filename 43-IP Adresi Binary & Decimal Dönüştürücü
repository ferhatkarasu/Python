def ip_to_binary(ip):
    try:
        parts=ip.split(".")
        if len(parts) !=4:
            raise ValueError("Geçersiz ip formatı!!!")

        binary_parts = [format(int(part), '08b') for part in parts]  # Decimal → Binary (8-bit)
        return '.'.join(binary_parts)

    except ValueError:
        return "Hatalı ip formatı!!!"
    
def binary_to_ip(binary_ip):
    try:
        parts = binary_ip.split(".")
        if len(parts) != 4:
            raise ValueError("Geçersiz ip formatı!!!")  

        decimal_parts = [str(int(part, 2)) for part in parts]
        return '.'.join(decimal_parts)  

    except ValueError:
        return "Hatalı ip formatı!!!"
    

def menu():
    print("IP Adresi Dönüştürücü")
    print("1. Decimal IP → Binary")
    print("2. Binary IP → Decimal")
    print("3. Çıkış")
    
    choice = input("Bir seçenek girin (1/2/3): ")
    
    if choice == '1':
        ip = input("Decimal IP adresini girin (Örnek: 192.168.1.1): ")
        print("Binary IP:", ip_to_binary(ip))
    elif choice == '2':
        binary_ip = input("Binary IP adresini girin (Örnek: 11000000.10101000.00000001.00000001): ")
        print("Decimal IP:", binary_to_ip(binary_ip))
    elif choice == '3':
        print("Çıkılıyor...")
        exit()
    else:
        print("Geçersiz seçenek! Lütfen tekrar deneyin.")
        menu()

menu()
