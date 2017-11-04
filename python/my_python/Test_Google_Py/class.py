###############################
# File Name: class.py         #
# Date 7/9/2017               #
# Author: Kobayshi Rui        #
###############################


#################################################


class animal():
  def __init__(self,name,voice):
       self.name = name
       self.voice = voice
  
  def call(self):
       print (self.voice)


class human(animal):
  def __inint__(self):
       super(human.self). __inint__(name, voice)
  
  def say(self):
       print 'human'
       print(self.voice)

class yaju(human):
  def __inint__(self,name,voice):
       super(yaju.self).__inint__(name,voice)
  def test(self):
       print'hello'


##################################################

if __name__ == '__main__':
   cat = animal('tama', 'nya')
   cat.call()
   dog = animal('poch', 'wan')
   dog.call()
   ff = human('kawamata', '114514')
   ff.say()
   ff.call()
   yy=yaju('senpai', 'iku')
   yy.say()
   yy.test()
       
