# A story with some words missing .
story = "A {} was running against me. I am very {} and {} fastly." \
        "Suddenly I saw a {} and {} there.After sometimes it {}."

# Ask the user to enter words

animal = input("Enter a animal name")
adj = input("Enter a adjective")
verb = input("Enter a verb")
noun = input("Enter a noun")
noun2 = input("Enter a noun")
verb2 = input("Enter a verb ")


# Display the story
print(story.format(animal, adj, verb, noun, noun2,verb2))