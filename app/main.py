import json
import os

FILE = "resources.json"


def load():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save(resources):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(resources, f, indent=2)


def add(resources):
    topic = input("Topic: ")
    material = input("Material: ")
    url = input("URL: ")
    resources.append({"topic": topic, "material": material, "url": url})
    save(resources)
    print("Saved.\n")


def show(resources):
    if not resources:
        print("No resources yet.\n")
        return
    for i, r in enumerate(resources, 1):
        print(f"{i}. {r['topic']}")
        print(f"   Material: {r['material']}")
        print(f"   URL: {r['url']}")
    print()


resources = load()

while True:
    print("1) Add resource  2) Show resources  3) Quit")
    choice = input("> ")
    if choice == "1":
        add(resources)
    elif choice == "2":
        show(resources)
    elif choice == "3":
        break
    else:
        print("Invalid choice.\n")
        
