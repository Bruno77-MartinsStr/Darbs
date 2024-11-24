import random

start_phrase = "Reiz kādā tālā zemē..."

story = start_phrase + " " + random.choice(["dzīvoja gudrs princis.", "piedzimis dārgais princis.", "daba bija pārsteidzoša un brīnišķīga."])

print(f"Generated story: {story}")
