artists = ["Billie Eilish", "Lana Del Rey", "Ariana Grande", "The Beatles"]
for a in artists:
    if (a == "The Beatles"):
        print(f"{a} are a great band")
    else:
        print(f"{a} is a good singer")

for a in artists[:-1]:
    print(f"{a} are solo artists")
