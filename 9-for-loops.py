artists = ["Billie Eilish", "The Beatles", "Lana Del Rey",  "Ariana Grande"]
for a in artists:
    if (a == "The Beatles"):
        print(f"{a} are a great band")
        break
    else:
        print(f"{a} is a good singer")

for a in artists[2:]:
    print(f"{a} are solo artists")
