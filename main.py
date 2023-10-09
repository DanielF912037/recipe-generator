import random

# Define lists of ingredients and cuisines
ingredients = [
    "Chicken", "Beef", "Salmon", "Pasta", "Rice", "Broccoli",
    "Carrots", "Tomatoes", "Onions", "Garlic", "Olive Oil",
    "Bell Peppers", "Spinach", "Mushrooms", "Zucchini", "Kale",
    "Asparagus", "Basil", "Oregano", "Thyme", "Cumin", "Paprika",
    "Rosemary", "Coriander", "Pork", "Shrimp", "Tofu", "Lamb",
    "Turkey", "Duck", "Sausage", "Quinoa", "Couscous", "Barley",
    "Bulgur", "Farro", "Parmesan Cheese", "Feta Cheese", "Cheddar Cheese",
    "Cream Cheese", "Mozzarella Cheese", "Ricotta Cheese", "Sour Cream",
    "Soy Sauce", "Balsamic Vinegar", "Worcestershire Sauce", "Sriracha",
    "BBQ Sauce", "Tahini", "Pesto", "Almonds", "Walnuts", "Sunflower Seeds",
    "Chia Seeds", "Sesame Seeds", "Pine Nuts", "Apples", "Oranges",
    "Avocado", "Mango", "Pineapple", "Cranberries", "Blueberries",
    "Eggs", "Bread Crumbs", "Chicken Stock", "Vegetable Stock", "Red Wine",
    "Lemon Juice", "Honey", "Coconut Milk"
]

cuisines = [
    "Italian", "Mexican", "Chinese", "Indian", "Greek", "Thai"
]

# Define difficulty levels
difficulty_levels = ["Easy", "Medium", "Difficult"]

def generate_recipe(preferred_ingredients=[], excluded_ingredients=[]):
    # Filter ingredients based on user preferences
    available_ingredients = [ingredient for ingredient in ingredients if
                             ingredient not in excluded_ingredients and (not preferred_ingredients or ingredient in preferred_ingredients)]

    if not available_ingredients:
        return "No recipes match your preferences. Try different ingredients."

    main_ingredient = random.choice(available_ingredients)
    side_ingredient = random.choice(available_ingredients)
    cuisine = random.choice(cuisines)
    difficulty = random.choice(difficulty_levels)

    recipe = f"Recipe: {cuisine} {main_ingredient} with {side_ingredient}\n"
    recipe += f"Difficulty Level: {difficulty}\n"
    return recipe


if __name__ == "__main__":
    print("Welcome to the Recipe Generator!")

    while True:
        input("Press Enter to generate a recipe...")

        # Allow users to specify preferred and excluded ingredients
        preferred_ingredients = input("Enter preferred ingredients (comma-separated, or press Enter to skip): ").split(',')
        excluded_ingredients = input("Enter excluded ingredients (comma-separated, or press Enter to skip): ").split(',')

        recipe = generate_recipe(preferred_ingredients, excluded_ingredients)

        # Format and display the output
        print("\nHere is your random recipe:")
        print("-" * 50)  # Add a separator line
        print()
        print(recipe)
        print("\n" + "-" * 50)  # Add a separator line

        again = input("\nGenerate another recipe? (yes/y or no/n): ")
        if again.lower() not in ["yes", "y"]:
            break