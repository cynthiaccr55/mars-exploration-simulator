# 🚀 Mars Exploration Simulator

import random


def countdown():
    countdown = int(input("The countdown begins in: "))
    while countdown >= 1:
        print(countdown)
        countdown -= 1
    print("🔥 🚀 Liftoff successful!")


def landing():
    speed = float(input("Enter descent speed: "))

    while speed > 10:
        print("⚠️ Danger! Reduce speed.")
        speed = float(input("Enter new descent speed: "))

    print("🛬 Landing sequence started")

    while speed > 0:
        print(f"Current speed: {speed} m/s")
        speed -= 1

    print("🛬 Successful landing on Mars.")


def exploration():
    max_time = 10

    while max_time > 0:
        print(f"\n⏳ Remaining time: {max_time} hours")
        print("Choose an action:")
        print("1 - Search resources (2h)")
        print("2 - Analyze soil (3h)")
        print("3 - Explore surroundings (1h)")

        option = input("Select option (1, 2, 3): ")

        if option == "1":
            if max_time >= 2:
                max_time -= 2
                print("🔍 Searching resources...")
            else:
                print("Not enough time.")

        elif option == "2":
            if max_time >= 3:
                max_time -= 3
                print("🧪 Analyzing soil...")
            else:
                print("Not enough time.")

        elif option == "3":
            if max_time >= 1:
                max_time -= 1
                print("🌌 Exploring surroundings...")
            else:
                print("Not enough time.")

        else:
            print("Invalid option.")

    print("\n⏳ Time's up. Returning to spacecraft...")


def repairs():
    failures = 3
    steps = ["adjust", "weld", "restart", "check"]

    while failures > 0:
        print("\n🔧 Repair a system failure")
        i = 0

        while i < len(steps):
            action = input(f"Step {i+1}: ")

            if action == steps[i]:
                i += 1
            else:
                print("❌ Error! Restarting sequence...")
                i = 0

        print("✅ Repair completed")
        failures -= 1

    print("🚀 All systems repaired. Ready for launch")


def storm_escape():
    astronaut = 0
    storm = 0
    goal = 50

    print("\n🌪️ Solar storm incoming! Reach the ship at 50 km.")

    while True:
        print(f"\n📍 Your position: {astronaut} km")
        print(f"🌪️ Storm position: {storm} km")

        advance = int(input("Advance distance (1 to 6 km): "))

        if advance < 1 or advance > 6:
            print("❌ Invalid distance.")
            continue

        astronaut += advance
        storm += random.randint(1, 5)

        if storm >= astronaut:
            print("💀 The storm caught you. Mission failed.")
            break

        if astronaut >= goal:
            print("🏁 You reached the ship. Mission success!")
            break


def main():
    print("🚀 Welcome to Mars Exploration Simulator")

    countdown()
    landing()
    exploration()
    repairs()
    storm_escape()


if __name__ == "__main__":
    main()