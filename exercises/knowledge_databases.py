from knowledge_model import Base, Player
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_player(name, number, overating):
	P = Player(name, number, overating)
	session.add(P)
	session.commit()

def query_all_players():
	return session.query(Player).all() 

def query_player_by_topic(name):
	return session.query(Player).filter_by(name=name).first()

def delete_player_by_topic(name):
	session.query(Player).filter_by(name=name).delete().first()
	session.commit()

def delete_all_players():
	session.query(Player).delete()
	session.commit()

def edit_player_overating(number,newrate):
	session.query(Player).filter_by(number=number).first().overating = newrate
	session.commit()


#print(query_player_by_topic("Michel Jorden"))
#delete_player_by_topic("Jimmy Butler")
edit_player_overating(21,90)
print(query_all_players())
# delete_all_players()

# add_player("Michel Jorden", 23, 99)
# add_player("Scottie Pippen", 33, 97)
# add_player("Derrick Rose", 1, 94)
# add_player("Artis Gilmore", 53, 94)
# add_player("Dennis Rodman", 91, 93)
# add_player("Jimmy Butler", 21, 90)
# add_player("Jerry Sloan", 4 , 89)
# add_player("Bob Love", 10, 88)
# add_player("Joakim Noah", 13, 87)
# add_player("Luol Deng", 9, 86)
# add_player("Horace Grant", 54, 85)
# add_player("B.J. Armstrong", 11, 85)
# add_player("Toni Kukoc", 7, 85)
# add_player("Charles Oakley", 34, 84)
# add_player("Steve Kerr", 25, 81)