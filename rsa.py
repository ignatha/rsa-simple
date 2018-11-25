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