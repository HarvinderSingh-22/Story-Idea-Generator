#Story Idea Generator

import random

# Define genres, themes, and character types
genres = {
    "fantasy": "In a forgotten realm, {} must embark on a quest to {}.",
    "mystery": "In a city full of secrets, a detective must {} to uncover the truth behind {}.",
    "sci-fi": "In a distant future, {} fight against a regime while discovering {}.",
    "romance": "Years after their breakup, two estranged lovers {} when they {}."
}

themes = {
    "redemption": "redeem their past mistakes",
    "betrayal": "uncover the betrayal that changed everything",
    "survival": "survive against all odds",
    "second chances": "get a second chance at love",
    "overcoming obstacles": "overcome impossible challenges"
}

character_types = {
    "hero": "a reluctant hero",
    "villain": "a genius villain with a secret agenda",
    "lover": "a pair of estranged lovers",
    "leader": "a fallen leader",
    "detective": "a cynical detective"
}

# Function to generate a story prompt
def generate_story_prompt(genre, theme, character):
    genre_template = genres.get(genre.lower())
    theme_detail = themes.get(theme.lower())
    character_detail = character_types.get(character.lower())
    
    if genre_template and theme_detail and character_detail:
        return genre_template.format(character_detail, theme_detail)
    else:
        return "Invalid input. Please provide valid genre, theme, and character."

# Example usage
print("Welcome to the Story Idea Generator!")
genre = input("Choose a genre (fantasy, mystery, sci-fi, romance): ")
theme = input("Choose a theme (redemption, betrayal, survival, second chances, overcoming obstacles): ")
character = input("Choose a character type (hero, villain, lover, leader, detective): ")

# Generate and display the story idea
story_prompt = generate_story_prompt(genre, theme, character)
print("\nStory Idea:")
print(story_prompt)
