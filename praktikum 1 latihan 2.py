# -*- coding: utf-8 -*-
"""

@materi : Algoritma dan pemograman
@judul : Menghitung luas segi panjang
@hari/tanggal : senin, 20210927
@nim : 065002100023
@author : Tri Bintang Pamungkas

"""

print("Menghitung Luas Persegi Panjang")
which = int(input("masukan panjang nya: "))
luas = int(input("masukan lebar nya: "))
satuan = input("masukan satuan(meter/inchi) :")

if satuan == "meter" :
    conv_luas = (luas * which)
    print("luas ruangan dengan panjang",which,"dan lebar",luas,"adalah",conv_luas,satuan)

elif satuan == "inchi" :
    conv_luas = (luas * which)
    print("luas ruangan dengan panjang",which,"dan lebar",luas,"adalah",conv_luas,satuan)