"""
    Basit Hatırlatıcı: Kullanıcının belirttiği bir mesajı ve süreyi kullanan bir hatırlatıcı
"""


# Zamanla ilgili işlemler yapmak için time modülünü dahil ediyorum
import time  

# Hatırlatıcı fonksiyonunu tanımlıyorum
def hatirlatici(mesaj, sure):
    # Kullanıcıya hatırlatma mesajının kaç saniye sonra hatırlatılacağını belirtiyorum
    print(f"{sure} saniye sonra hatırlatılacak: {mesaj}")
    time.sleep(sure)  # Belirtilen süre kadar bekliyorum
    # Belirtilen süre geçtikten sonra hatırlatma mesajını ekrana yazdırıyorum
    print(f"Hatırlatma: {mesaj}")


# Kullanıcıdan hatırlatma mesajını girmesini istiyorum
mesaj = input("Hatırlatma mesajını girin: ")
# Kullanıcıdan kaç saniye sonra hatırlatma yapmak istediğini soruyorum
sure = int(input("Kaç saniye sonra hatırlatılacak: "))

# Hatırlatıcı fonksiyonunu, kullanıcıdan aldığım mesaj ve süre ile çağırıyorum
hatirlatici(mesaj, sure)
