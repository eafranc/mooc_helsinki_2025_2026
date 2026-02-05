# Write your solution here
class Player:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def __str__(self):
        return f"{self.name:20} {self.team:3} {self.goals:3} + {self.assists:2} = {self.points():3}"

    def __repr__(self):
        return f"Player('{self.name}', '{self.nationality}', {self.assists}, {self.goals}, {self.penalties}, '{self.team}', {self.games})"

    def points(self):
        return self.goals + self.assists

class Database:
    def __init__(self, filename: str):
        self.database = []
        self.get_json(filename)

    def get_json(self, filename: str):
        import json
        with open(filename) as file:
            data = file.read()
        players = json.loads(data)
        self.add_all_players(players)

    def add_all_players(self, players: list):
        for player in players:
            self.database.append(Player(player["name"],
                                        player["nationality"],
                                        player["assists"],
                                        player["goals"],
                                        player["penalties"],
                                        player["team"],
                                        player["games"]
                                        )
                                )
        print(f"read the data of {len(self.database)} players")

    def search_player(self, name: str):
        search = list(filter(lambda p: p.name == name, self.database))
        if len(search) == 1:
            for player in search:
                print(player)
        else:
            print("player not found")

    def all_players(self):
        return sorted(self.database, key=lambda p: p.name)

    def all_teams(self):
        return sorted(list(set([player.team for player in self.all_players()])))

    def all_countries(self):
        return sorted(list(set([player.nationality for player in self.all_players()])))

    def players_in_team(self, team: str):
        return sorted(list(filter(lambda p: p.team == team, self.all_players())), key= lambda p: p.points(), reverse= True)

    def players_from_country(self, country: str):
        return sorted(list(filter(lambda p: p.nationality == country, self.all_players())), key= lambda p: p.points(), reverse= True)

    def most_points(self, number: int):
        return sorted(self.all_players(), key= (lambda p: (-p.points(), -p.goals)))[:number] # uses minus on lambda function to reverse the sorting

    def most_goals(self, number: int):
        return sorted(self.all_players(), key= lambda p: (-p.goals, p.games))[:number]  # the value of goals is reversed (max first)
                                                                                        # but the value games isn't (min first)

class Application:
    def __init__(self):
        self.execute()

    def menu(self):
        print(
        '''
        commands:
        0 quit
        1 search for player
        2 teams
        3 countries
        4 players in team
        5 players from country
        6 most points
        7 most goals
        '''
        )

    def get_file(self):
        filename = input("file name: ")
        self.get_database(filename)

    def get_database(self, filename: str):
        self.__database = Database(filename)

    def search_player(self):
        name = input("name: ")
        self.__database.search_player(name)

    def all_teams(self):
        for team in self.__database.all_teams():
            print(team)

    def all_countries(self):
        for country  in self.__database.all_countries():
            print(country)

    def players_in_team(self):
        team = input("team: ")
        for player in self.__database.players_in_team(team):
            print(player)

    def players_from_country(self):
        country = input("country: ")
        for player in self.__database.players_from_country(country):
            print(player)

    def most_points(self):
        number = int(input("how many: "))
        for player in self.__database.most_points(number):
            print(player)

    def most_goals(self):
        number = int(input("how many: "))
        for player in self.__database.most_goals(number):
            print(player)

    def execute(self):
        self.get_file()
        self.menu()
        while True:
            print()
            command = input("command: ")

            if command == "0":
                break
            elif command == "1":
                self.search_player()
            elif command == "2":
                self.all_teams()
            elif command == "3":
                self.all_countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
            else:
                self.menu()

def main():
    app = Application()

main()

if __name__ == "__main__":
    print("=" * 100)
    print("Testing Database class:\n")
    players = Database("partial.json")

    print("=" * 100)
    print("Displaying all players:")
    for player in players.all_players():
        print(player)

    print("=" * 100)
    print("Displaying all teams:")
    for team in players.all_teams():
        print(team)

    print("=" * 100)
    print("Displaying all nationalities:")
    for country in players.all_countries():
        print(country)

    print("=" * 100)
    print("Searching players")
    players.search_player("Travis Zajac")
    players.search_player("Travis ZajX")

    print("=" * 100)
    print("Testing Application:\n")
    app = Application()

