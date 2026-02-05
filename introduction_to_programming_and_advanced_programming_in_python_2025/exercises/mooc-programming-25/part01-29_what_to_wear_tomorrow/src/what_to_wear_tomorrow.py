# Write your solution here
print("What is the weather forecast for tomorrow?")
temp_C  = int(input("Temperature:"))
rain_yn = input("Will it rain (yes/no):")

print("Wear jeans and a T-shirt")

if(temp_C <= 20):
    print("I recommend a jumper as well")

if(temp_C <= 10):
    print("Take a jacket with you")

if(temp_C <= 5):
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if(rain_yn == "yes"):
    print("Don't forget your umbrella!")
