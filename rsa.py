from __future__ import division
import Gcd
import timeit
import random

class rsa:
   'rsa_bowo Kriptografi'
   n,m,e,d=0,0,0,0

   def __init__(self, p, q):
      self.p = p
      self.q = q
  
  # set Public key N
   def setN(self):
      self.n=self.p*self.q

   # Set m
   def setM(self):
      self.m=(self.p-1)*(self.q-1)

   # set Public key E
   def setE(self):
      list = []
      for x in range(10000,99999):
         c = Gcd.computeGCD(x,self.m)
         if c == 1:
            list.append(x)

      self.e = random.choice(list)

   # set Private Key
   def setD(self):
      i,o = 1,False

      while o != True:
        t = (1+(i*self.m))/self.e
        i += 1
        o = (t).is_integer()

      self.d = int(t)

   # Do Encrypt
   def doEncrypt(self,p):
      c = pow(p,self.e,self.n)
      return c 

   # Do Decrypt
   def doDecrypt(self,c):
      p = pow(c,self.d,self.n)
      return p
         
      
      


# rsa_bowo = rsa(857, 991)
# rsa_bowo.setN()
# rsa_bowo.setM()
# rsa_bowo.setE()
# rsa_bowo.setD()

# print("Nilai P : ")
# print(rsa_bowo.p)

# print("Nilai Q : ")
# print(rsa_bowo.q)

# print("Nilai N : ")
# print(rsa_bowo.n)

# print("Nilai M : ")
# print(rsa_bowo.m)

# print("Nilai E : ")
# print(rsa_bowo.e)

# print("Nilai D : ")
# print(rsa_bowo.d)

# print("Plaintext : ")
# text = "Python adalah bahasa pemrograman interpretatif multiguna[9] dengan filosofi perancangan yang berfokus pada tingkat keterbacaan kode.[10] Python diklaim sebagai bahasa yang menggabungkan kapabilitas, kemampuan, dengan sintaksis kode yang sangat jelas,[11] dan dilengkapi dengan fungsionalitas pustaka standar yang besar serta komprehensif. Python juga didukung oleh komunitas yang besar. Python mendukung multi paradigma pemrograman, utamanya; namun tidak dibatasi; pada pemrograman berorientasi objek, pemrograman imperatif, dan pemrograman fungsional. Salah satu fitur yang tersedia pada python adalah sebagai bahasa pemrograman dinamis yang dilengkapi dengan manajemen memori otomatis. Seperti halnya pada bahasa pemrograman dinamis lainnya, python umumnya digunakan sebagai bahasa skrip meski pada praktiknya penggunaan bahasa ini lebih luas mencakup konteks pemanfaatan yang umumnya tidak dilakukan dengan menggunakan bahasa skrip. Python dapat digunakan untuk berbagai keperluan pengembangan perangkat lunak dan dapat berjalan di berbagai platform sistem operasi."
# print(text)
# print("\n")

# start_plain = timeit.default_timer()
# plainText = [int(ord(c)) for c in text]
# print("ASCII Plaintext : ")
# print(plainText)
# print("\n")
# print("Need Time : ",timeit.default_timer() - start_plain)
# print("\n")

# start_encr = timeit.default_timer()
# cipherText = [int(rsa_bowo.doEncrypt(s)) for s in plainText]
# print("Encrypted : ")
# print(cipherText)
# print("\n")
# print("Need Time : ",timeit.default_timer() - start_encr)
# print("\n")

# start_decr = timeit.default_timer()
# textAsli = [int(rsa_bowo.doDecrypt(t)) for t in cipherText]
# print("Decrypted : ")
# print(textAsli)
# print("\n")
# print("Need Time : ",timeit.default_timer() - start_decr)
# print("\n")

# start_asli = timeit.default_timer()
# Teks = [chr(t) for t in textAsli]
# print("Text : ")
# print(Teks)
# print("\n")
# print("Need Time : ",timeit.default_timer() - start_asli)
# print("\n")

