import json
import os

DATA_FILE = "moodsongs.json"

def load_data():
    """Load existing data from file."""
    if not os.path.exists(DATA_FILE):
        return {
            "Happy": ["Happy – Pharrell Williams", "Good Life – OneRepublic"],
            "Sad": ["Someone Like You – Adele", "Let Her Go – Passenger"],
            "Relaxed": ["Weightless – Marconi Union", "Better Together – Jack Johnson"],
            "Energetic": ["Can't Stop – Red Hot Chili Peppers", "Titanium – David Guetta"],
            "Angry": ["In the End – Linkin Park", "Smells Like Teen Spirit – Nirvana"]
        }
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    """Save current data to file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def show_all_moods(data):
    print("\n🎶 Available Moods and Songs:")
    for mood, songs in data.items():
        print(f"\n[{mood}]")
        for s in songs:
            print(f" - {s}")

def recommend_songs(data):
    mood = input("\nEnter your mood: ").capitalize()
    if mood in data:
        print(f"\n🎧 Songs for '{mood}' mood:")
        for s in data[mood]:
            print(f" - {s}")
    else:
        print(" Mood not found. Try adding it first!")

def add_song(data):
    mood = input("\nEnter mood: ").capitalize()
    song = input("Enter song name and artist: ")

    if mood in data:
        data[mood].append(song)
    else:
        data[mood] = [song]

    save_data(data)
    print(" Song added successfully!")

def update_mood(data):
    mood = input("\nEnter mood to update: ").capitalize()
    if mood not in data:
        print(" Mood not found.")
        return
    print("Current songs:")
    for s in data[mood]:
        print(f" - {s}")
    new_songs = input("Enter new song list (comma-separated): ").split(",")
    data[mood] = [s.strip() for s in new_songs]
    save_data(data)
    print(" Mood updated successfully!")


def main():
    data = load_data()

    while True:
        print("\n===== 🎵 MoodSync – Emotion-based Music Recommender =====")
        print("1. Show all moods and songs")
        print("2. Recommend songs for a mood")
        print("3. Add new song")
        print("4. Update song list for a mood")
        print("5. Exit")

        choice = input("\nEnter your choice (1–5): ")

        if choice == "1":
            show_all_moods(data)
        elif choice == "2":
            recommend_songs(data)
        elif choice == "3":
            add_song(data)
        elif choice == "4":
            update_mood(data)
        elif choice == "5":
            print("🎶 Thank you for using MoodSync! Goodbye.")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()

