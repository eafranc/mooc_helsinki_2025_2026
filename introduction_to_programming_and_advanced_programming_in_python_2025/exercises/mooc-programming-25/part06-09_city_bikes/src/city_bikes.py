# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    with open(filename) as file:
        stations = {}
        for line in file:
            line  = line.replace("\n", "")
            parts = line.split(";")
            name  = parts[3]
            if name == "name":
                continue
            (longitude, latitude) = parts[0:2]
            stations[name] = (float(longitude), float(latitude))
        return stations

def distance(stations: dict, station1: str, station2: str):
    (longitude1, latitude1) = stations[station1]
    (longitude2, latitude2) = stations[station2]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    st1 = {}
    st2 = {}
    greatest_dist = 0
    greatest_st1 = ""
    greatest_st2 = ""
    for station1, coordinates1 in stations.items():
        st1[station1] = coordinates1
        for station2, coordinates2 in stations.items():
            st2[station2] = coordinates2
            if st1[station1] == st2[station2]:
                continue
            d = distance(stations, station1, station2)
            if greatest_dist < d:
                greatest_dist = d
                greatest_st1 = station1
                greatest_st2 = station2
    return (greatest_st1, greatest_st2, greatest_dist)


if __name__ == "__main__":
    stations = get_station_data("stations1.csv")
    print(stations)
# {
#   "Kaivopuisto": (24.950292890004903, 60.155444793742276),
#   "Laivasillankatu": (24.956347471358754, 60.160959093887129),
#   "Kapteeninpuistikko": (24.944927399779715, 60.158189199971673)
# }

    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
# 0.9032737292463177
# 0.7753594392019532

    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
# Laivasillankatu Hietalahdentori 1.478708873076181
