import pandas as pd
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionSuggestRecipe(Action):
    def name(self):
        return "action_suggest_recipe"

    def run(self, dispatcher, tracker, domain):
        # Load the dataset
        df = pd.read_csv("unique_recipe_dataset.csv")

        # Extract user ingredients
        user_ingredients = [tracker.get_slot("ingredient")]

        # Find a matching recipe
        for _, row in df.iterrows():
            ingredients = row["ingredients"].split(", ")
            if any(ing in ingredients for ing in user_ingredients):
                dispatcher.utter_message(f"You can try making {row['recipe_name']} with {row['ingredients']}")
                return []

        dispatcher.utter_message("Sorry, I couldn't find a matching recipe.")
        return []
