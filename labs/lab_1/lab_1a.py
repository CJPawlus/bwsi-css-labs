"""
lab_1a.py

The first lab in the BWSI CSS course. To complete this lab, fill out the variable on line 10
with your name. Then, save the code, add it to the staging area, and commit it to the Git tree.
"""

def main():
    print("Hello World!")

    name = "Christopher Pawlus" # TODO: Insert your name between the double quotes

    introduction= "Hello everyone! My name is Christopher Pawlus, a Junior at Andover High School in Andover Massachusetts. I've lived here for most of my life, excluding a one year stay in Oregon. My favorite subject in school depends on the day but it's always either a science or math class. As of writing this I like statistics the most because right now our unit is blending what we have been learning all year into one procedure! Outside of school my favorite activity is either playing with friends or doing anything that is related to engineering like robotics (proud ARC Thunder member here) or personal projects. I would say something that is unique about me is my current engineering project in which I am designing and prototyping a mono-wing aircraft that utilizes a custom flap control system to explore unconventional solutions to flight control."

    print(f"{name}, Welcome to the CSS course!")
    print(f"This is your introduction from the begining of the class: {introduction}")
if __name__ == "__main__":
    main()
