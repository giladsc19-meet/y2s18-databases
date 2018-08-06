from sqlalchemy import Column, Integer, String, Boolean, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Player(Base):
	primary_key = column(Integer,primary_key)
	name = column(String)
	number = column(Integer)
	height = column(Double)

	def __repr__(Player):
		

	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	pass