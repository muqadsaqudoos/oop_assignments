class Singleton:
   __instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
         
         
s1 = Singleton.getInstance()
print(s1)

s2 = Singleton.getInstance()
print(s2)

s3 = Singleton.getInstance()
print(s3)