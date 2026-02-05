# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        if name != "":
            self.__name = name
        else:
            raise ValueError("The name may not be an empty string")
        self.__observations = []

    def __str__(self):
        return f"{self.__name}, {len(self.__observations)} observations"

    def add_observation(self, observation: str):
        self.__observations.append(observation)

    def latest_observation(self):
        if len(self.__observations) > 0:
            return self.__observations[-1]
        else:
            return ""

    def number_of_observations(self):
        return len(self.__observations)

if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation()) # Sunny

    station.add_observation("Thunderstorm")
    print(station.latest_observation()) # Thunderstorm

    print(station.number_of_observations()) # 3
    print(station) # Houston, 3 observations
