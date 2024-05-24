import csv
import random

languages = [
    "Python",
    "Java",
    "JavaScript",
    "C#",
    "Swift",
    "Go",
    "Kotlin",
    "Rust",
]
os = ["Windows", "macOS", "Linux", "BSD", "Solaris"]
hobbies = [
    "Reading",
    "Gaming",
    "Hiking",
    "Coding",
    "Music",
    "Art",
    "Photography",
    "Writing",
    "Traveling",
    "Sports",
]

with open("data/survey.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        ["Favourite Programming Language", "Favourite OS", "Age", "Gender", "Hobbies"]
    )

    for _ in range(50):
        row = [
            random.choice(languages),
            random.choice(os),
            random.randint(12, 30),
            random.choice(["male", "female"]),
            ", ".join(random.sample(hobbies, random.randint(1, len(hobbies)))),
        ]
        writer.writerow(row)
