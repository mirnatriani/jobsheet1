import random 
from guess import tebakangka

tebak = tebakangka()
tebak.jawaban = random.randint(1,10)
tebak.tebakan = int(input("tebak angka dari 1 sd 10 :"))

if tebak.cek():
    print("jawaban kamu benar")
else:
    print("jawaban kamu salah")