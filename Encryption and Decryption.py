#----------------------------------------------------------------------------------------------------------------------------------------


#Problem 1


S = input("What is your text? ")
n = int(input("What is your shift? "))
V = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def encryption(S,n):
   W = ""
   for i in S:
       if i == chr(32):
               W += i
       elif i in S:
           g = (ord(i) + n)
           if g >= 123:
               newi = V[(g-123)]
               W += newi
           else:
               newi = ord(i) + n
               W += chr(newi)
   print("Your enciphered text is: ", (W))
   return W


encryption(S,n)
 

#---------------------------------------------------------------------------------------------------------------------------------------


#Problem 2


S = input("What is your text? ")
n = int(input("What is your shift? "))
V = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def decryption(S,n):
   W = ""
   for i in S:
       if i == chr(32):
               W += i
       elif i in S:
           g = (ord(i) - n)
           if g <= 96:
               newi = V[(g-97)]
               W += newi
           else:
               newi = ord(i) - n
               W += chr(newi)
   print("Your deciphered text is: ", (W))
   return W


decryption(S,n)
