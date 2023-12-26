# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to _____ "
youtuber = "jun3rd" # some string variable

# a few ways to do this
print("subscribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")
print(".........................")

adj = input("Adjective: ")
verb1 = input("Verb1: ")
verb2 = input("Verb2: ")
famous_person = input("famous person: ")

madlib = f"Skateboarding is so {adj}! I am so scared to {verb1}. Stay safe and {verb2} with your gear, like {famous_person}!"

print(madlib)

