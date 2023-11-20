print("AREXUS - Kalan Maaş Hesaplama")
print("")
ad = input("Lütfen adınızı giriniz: ")
print("Merhaba " + ad + ".")
print("")

maas = float(input("Maaşınızı yazınız: "))
vergi_orani = float(input("Vergi oranını yüzde olarak giriniz: ")) / 100

kalan_maas = maas - (maas * vergi_orani)
print("Tüm vergiler çıkıldığında size kalan maaş: " + str(kalan_maas))
print("Bizi seçtiğiniz için teşekkürler.")
