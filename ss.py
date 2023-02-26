import os
import shutil
liste=['/Users/sina/Desktop/s/','/Users/sina/Desktop/hw1/']
a="/Users/sina/Desktop/"
for j in liste:
    kaynak = f"{j}"
    hedef = f"{a}"
    files = os.listdir(kaynak)
    files.sort()
    dosya_sayisi = 0
    for f in files:
        if f.endswith(".csv"):
            dosya_sayisi += 1
            k = kaynak + f
            h = hedef + f
            shutil.copy(k, h)

print("%d adet dosya kopyalandı" % dosya_sayisi)
