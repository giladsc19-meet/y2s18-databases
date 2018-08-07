from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Player(Base):
	__tablename__ = "player"
	primary_key = Column(Integer,primary_key = True)
	name = Column(String)
	number = Column(Integer)
	overating = Column(Float)

	def __init__(self,name,number,overating):
		self.name=name
		self.number=number
		self.overating=overating
		
	def __repr__(self):
		if self.overating>=90:
			return("An ALL-STAR Player! :)"
			"name: {}\n"
			"number: {}\n"
			"overating: {}\n").format(self.name,self.number,self.overating)
		if 70<=self.overating<90:
			return("An AVARGE Player! :|"
			"name: {}\n"
			"number: {}\n"
			"overating: {}\n").format(self.name,self.number,self.overating)
		if self.overating<70:
			return("A ROOKIE! :("
			"name: {}\n"
			"number: {}\n"
			"overating: {}\n").format(self.name,self.number,self.overating)

# jordan = Player(name = "Michael Jordan",number = 23,overating = 99.0)
# print(Jordan)
# pippen = Player(name = "Scottie Pippen",number =33 ,overating = 97.0)
# print(Pippen)
# rose = Player(name = "Derrick Rose",number = 1,overating = 94.0)
# print(Rose)
# gilmore = Player(name = "Artis Gilmore",number = 53,overating = 94.0)
# print(Gilmore)
# rodman = Player(name = "Dennis Rodman",number = 91,overating = 93.0)
# print(Rodman)
# butler = Player(name = "Jimmy Butler",number = 21,overating = 90.0)
# print(Butler)
