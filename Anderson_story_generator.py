# Creativity Addition:
# Extended the story and included more words to be filled.
# Implemented logic to handle "a" or "an" appropriately based on the next word.

def main():
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb1 = input("Enter a verb: ")
    exclamation = input("Enter an exclamation: ").capitalize()
    verb2 = input("Enter another verb: ")
    verb3 = input("Enter one more verb: ")
    adverb = input("Enter an adverb: ")
    noun = input("Enter a noun: ")
    article = "an" if noun[0].lower() in ['a', 'e', 'i', 'o', 'u'] else "a"

    story = (
        f"The other day, I was really in trouble. "
        f"It all started when I saw a very {adjective} {animal} {verb1} down the hallway. "
        f'"{exclamation}" I yelled. But all I could think to do was to {verb2} over and over. '
        f"Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family. "
        f"I quickly grabbed {article} {noun} and {adverb} ran away."
    )

    print(story)

if __name__ == "__main__":
    main()
