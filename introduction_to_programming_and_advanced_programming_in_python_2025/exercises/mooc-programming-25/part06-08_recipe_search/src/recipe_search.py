# Write your solution here
def get_cookbook(filename: str):
    lines = []
    cookbook = {}
    with open(filename) as file:
        for line in file:
            line = line.strip()
            lines.append(line)

        for i in range(len(lines)):
            if i == 0 or lines[i - 1] == "":
                recipe_name = lines[i]
                cookbook[recipe_name] = {"time": 0, "ingredients": []}
            else:
                if lines[i] == "":
                    continue
                elif cookbook[recipe_name]["time"] == 0:
                    cookbook[recipe_name]["time"] = int(lines[i]) # Takes the next line right after the recipe name
                else:
                    cookbook[recipe_name]["ingredients"].append(lines[i])
    return cookbook

def search_by_name(filename: str, word: str):
    cookbook = get_cookbook(filename)
    list_of_recipes = []
    for recipe, time_and_ingredients in cookbook.items():
        if word.lower() in recipe.lower():
            list_of_recipes.append(recipe)
    return list_of_recipes

def search_by_time(filename: str, prep_time: int):
    cookbook = get_cookbook(filename)
    list_of_recipes_by_prep_time = []
    for recipe in cookbook:
        if cookbook[recipe]["time"] <= prep_time:
            list_of_recipes_by_prep_time.append(f"{recipe}, preparation time {cookbook[recipe]["time"]} min")
    return list_of_recipes_by_prep_time

def search_by_ingredient(filename: str, ingredient: str):
    cookbook = get_cookbook(filename)
    list_of_recipes_by_ingredient = []
    for recipe in cookbook:
        if ingredient in cookbook[recipe]["ingredients"]:
            list_of_recipes_by_ingredient.append(f"{recipe}, preparation time {cookbook[recipe]["time"]} min")
    return list_of_recipes_by_ingredient

if __name__ == "__main__":
    cookbook = get_cookbook("recipes1.txt")
    print(cookbook)
    print("=======================================================")
    recipes = search_by_name("recipes1.txt", "cake")
    for recipe in recipes:
        print(recipe)
# Pancakes
# Cake pops
    print("=======================================================")
    recipes_by_prep_time = search_by_time("recipes1.txt", 20)
    for recipe in recipes_by_prep_time:
        print(recipe)
# Pancakes, preparation time 15 min
    print("=======================================================")
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)
# Pancakes, preparation time 15 min
# Meatballs, preparation time 45 min
# Cake pops, preparation time 60 min
    print("=======================================================")
