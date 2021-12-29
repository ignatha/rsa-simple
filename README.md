# ignatha/rsa-simple


Aplikasi sederhana untuk generate, enkripsi dan dekripsi sebuah pesan menggunakan algoritma RSA


## Install

Install package yang dibutuhkan ke dalam environment, disarankan menggunakan virtual environment seperti `virtualenv` atau `virtualenvwraper`. Setelah masuk virtualenv, jalankan perintah berikut

```bash
pip install -r requirements.txt
```

## Jalankan main.py
Setelah semua package yang dibutuhkan berhasil diinstall, jalankan scriptnya dengan perintah

```bash
python main.py
```

## NB
- Di testing di Python 3.7
- Angka prima yang dimasukkan untuk nilai P dan Q minimal 3 digit
- public key yang dihasilkan adalah pubic key dengan 5 digit angka, antara 10000 - 99999
- Bonus script untuk looping blangan prima di file `prime.py`, tinggal ganti batasan nilai dari angka prima yang diinginkan
- Jangan memasukkan nilai terlalu besar
- Kerusakan karena memaksa komputer menghitung angka terlalu besar bukan tanggung jawab kami
- Jangan lupa trakteer admin secangkir kopi 😃 [Trakteer](https://trakteer.id/ignatha/tip)
