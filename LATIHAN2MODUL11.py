#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:44:23 2022

@author: sonyaridesia
"""

class Mahasiswa:
    
    def __init__(self, nama, nilai):
        self.nama = nama
        self.__nilai = nilai
        
    @property
    def detail(self):
        return "nama : {} \nNilai: {}".format(self.nama, self.__nilai)
    
    @property
    def nilai(self):
        pass
    
    @nilai.getter
    def nilai(self):
        return self.__nilai
    
    @nilai.setter
    def nilai(self, input):
        self.__nilai = input
        
    @nilai.deleter
    def nilai(self):
        self.__nilai = None
        
def banner():
    print("===== program oop =====")
    print("1. mendeklarasikan objek")
    print("2. menampilkan objek")
    print("3. merubah nilai objek")
    print("4. menghapus objek") 
    print("5. keluar Dari program\n")
banner()
        
def main():
    mahasiswa = Mahasiswa(None, None)
    F = False
    while(not F):
        pilihan = int(input("Masukkan pilihan berapa Angka(1/2/3/4/5): "))
        if(pilihan == 1):
            nama = input("Masukkan Namamu: ")
            nilai = int(input("Masukkan nilaimu:"))
            mahasiswa = Mahasiswa(nama, nilai)
            print("Data Berhasil Ditambahkan")
            print("\n")
        elif(pilihan == 2):
            print("\n")
            print(mahasiswa.detail)
            print("\n")
        elif(pilihan == 3):
            opsi = input("Apa yang ingin diubah (Nama/Nilai): ").upper()
            if(opsi == "NAMA"):
                nama = input("Masukkan Nama: ")
                mahasiswa.nama = nama
                print("Data Nama Berhasil Dirubah")
                print("\n")
            elif(opsi == "NILAI"):
                nilai = int(input("Masukkan Nilai"))
                mahasiswa.nilai = nilai
                print("Data Nilai Berhasil Dirubah")
                print("\n")
            else:
                print("Masukkan opsi yang sesuai antara Nama/Nilai")
                print("\n")
        elif(pilihan == 4):
            mahasiswa.nilai = None
            del mahasiswa.nilai
            print("Data Berhasil Dihapus")
            print("\n")
        elif(pilihan == 5):
            print("Terima Kasih Sudah Menggunakan Program Saya")
            F =True
        else:
            print("Masukkan Angka yang sesuai dengan yang ada di Menu!")
            print("\n")
main()