x = "Smth"
Name = input("What is your name?")
print("Hello," + Name + "! I want to tell you a story, and I want you to help me. Please, answer my questions.")
Age = int(input("How old are you?"))
Place = input("What country would you most of all like to visit?")
Person = input("Who would you like to go there with?")
Sound = input ("What sound might scare you (screem, cry, laugh, etc...)?")
print(f"{Age - 7} years ago there was a little girl in {Place}. She lived in a big house with {Person} and her grandma. The house was very old and creepy. The girl didn't know, how many rooms it had, and she was always dreaded to get lost there. But the most terrible was a basement. It was very dark and wet. ")
print(f"One night the girl woke up, because she heard a {Sound}. It was very dark outside. She couldn't see the time on the clock. Suddenly she undersood: there's someone in her room.")
while x != "Yes" and x != "No":
    x = input("What will she do? Will she ask: 'Who is here?' (Enter 'Yes') or will she pretend to be asleep? (Enter 'No')")
    if x == "Yes":
        print("It was a little boy. Very odd boy in a dress. He started to run. «Wait!» - girl run after him. The girl was never seen again.")
    elif x == "No":
        print("She closed her eyes and pretended to be asleep. She could hear rustls and creaks. Then became silence. The girl slightly opened her eyes  and saw big and dark mouth of the bed monster, who then swallowed her. ")
    else:
        print("Wow! You've just made a mistake in such a simple word! Try again!")

