import random
angka_rahasia = random.randint(1, 100)

print('='*40)
print('kami telah memiliki angka, silahkan tebak!')
print('='*40)

while True:
    jawaban = int(input('\nmasukan angka: '))

    if jawaban == angka_rahasia:
        print('selamat, tebakanmu benar!')
        break  # berhenti paksa!

    else:
        print(
            'tebakanmu terlalu ',
            'kecil' if jawaban < angka_rahasia else 'besar'
        )
