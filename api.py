from user import User
from movie import Movie 

if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter()

    nick = User("nmcassa")
    print("JSON of my User Object:\n")
    print(nick.jsonify())

    king = Movie("king kong")
    print("\n JSON of Movie Object:\n")
    print(king.jsonify())

    king_plus = Movie("king kong", 2005)
    print("\n JSON of Movie Object w/ year:\n")
    print(king_plus.jsonify())
    

    
