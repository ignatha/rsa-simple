from __future__ import division
import Gcd

class Rsa:
   'Rsa Kriptografi'
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
      for x in range(500,self.m):
         c = Gcd.computeGCD(x,self.m)

         if c == 1:
            self.e = x
            break

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
      c = p ** self.e % self.n
      return c 

   # Do Decrypt

   def doDecrypt(self,c):
      p = c ** self.d % self.n
      return p
         
      
      


rsa = Rsa(983, 991)
rsa.setN()
rsa.setM()
rsa.setE()
rsa.setD()
print(rsa.n)
print(rsa.m)
print(rsa.e)
print(rsa.d)

chiperText = rsa.doEncrypt(88)
print(chiperText)

plainText = rsa.doDecrypt(chiperText)
print(plainText)

print("---------------")

rsa2 = Rsa(311, 101)
rsa2.setN()
rsa2.setM()
rsa2.setE()
rsa2.setD()
print(rsa2.n)
print(rsa2.m)
print(rsa2.e)
print(rsa2.d)

chiperText2 = rsa2.doEncrypt(20)
print(chiperText2)

plainText2 = rsa2.doDecrypt(chiperText2)
print(plainText2)