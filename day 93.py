# menghitung diskon belanja

total = int(input("Masukkan Total Belanja : Rp. "))

if total >= 1000000:
    diskon = "30%"
    harga_diskon = total * 30/100
    harga_total = total -  harga_diskon
    print(f"Total Belanja Sebelum Diskon : Rp. {total},00")
    print(f"Diskon : {diskon}")
    print(f"Total Belanja Setelah Diskon : Rp. {harga_total},00")
    

elif total >= 800000:
    diskon = "25%"
    harga_diskon = total * 25/100
    harga_total = total -  harga_diskon
    print(f"Total Belanja Sebelum Diskon : Rp. {total},00")
    print(f"Diskon : {diskon}")
    print(f"Total Belanja Setelah Diskon : Rp. {harga_total},00")
    
elif total >= 500000 :
    diskon = "10%"
    harga_diskon = total * 10/100
    harga_total = total -  harga_diskon
    print(f"Total Belanja Sebelum Diskon : Rp. {total},00")
    print(f"Diskon : {diskon}")
    print(f"Total Belanja Setelah Diskon : Rp. {harga_total},00")
    
elif total >= 300000:
    diskon =  "5%"
    harga_diskon = total * 5/100
    harga_total = total -  harga_diskon
    print(f"Total Belanja Sebelum Diskon : Rp. {total},00")
    print(f"Diskon : {diskon}")
    print(f"Total Belanja Setelah Diskon : Rp. {harga_total},00")
    
elif total >= 170000 :
    diskon = "3%"
    harga_diskon = total * 3/100
    harga_total = total -  harga_diskon
    print(f"Total Belanja Sebelum Diskon : Rp. {total},00")
    print(f"Diskon : {diskon}")
    print(f"Total Belanja Setelah Diskon : Rp. {harga_total},00")
    
else:
    diskon = "Tidak Ada Diskon"
    
    print(f"Total Belanja : Rp. {total},00")
    print(f"Diskon : {diskon}")