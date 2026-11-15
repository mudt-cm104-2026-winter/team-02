import json
import os

FILE = "resources.json"


def load():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):  # old v0/v1 file: just a list of resources
            data = {"categories": [], "resources": data}
        return data
    return {"categories": [], "resources": []}


def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def print_resource(i, r):
    print(f"{i}. {r['topic']}")
    print(f"   Category: {r.get('category', 'Uncategorized')}")
    print(f"   Material: {r['material']}")
    print(f"   URL: {r['url']}")


def pick_category(data):
    cats = data["categories"]
    if not cats:
        print("No categories yet. Saving as Uncategorized.")
        return "Uncategorized"
    for i, c in enumerate(cats, 1):
        print(f"{i}. {c}")
    choice = input("Category number (Enter to skip): ")
    if choice.isdigit() and 1 <= int(choice) <= len(cats):
        return cats[int(choice) - 1]
    return "Uncategorized"


def add_resource(data):
    topic = input("Topic: ")
    material = input("Material: ")
    url = input("URL: ")
    category = pick_category(data)
    data["resources"].append({"topic": topic, "material": material,
                              "url": url, "category": category})
    save(data)
    print("Saved.\n")


def show_resources(data):
    if not data["resources"]:
        print("No resources yet.\n")
        return
    for i, r in enumerate(data["resources"], 1):
        print_resource(i, r)
    print()


def add_category(data):
    name = input("Category name: ").strip()
    if not name:
        print("Name can't be empty.\n")
    elif name in data["categories"]:
        print("Category already exists.\n")
    else:
        data["categories"].append(name)
        save(data)
        print("Category added.\n")


def browse_categories(data):
    cats = data["categories"]
    if not cats:
        print("No categories yet.\n")
        return
    for i, c in enumerate(cats, 1):
        print(f"{i}. {c}")
    choice = input("Category number: ")
    if not (choice.isdigit() and 1 <= int(choice) <= len(cats)):
        print("Invalid choice.\n")
        return
    cat = cats[int(choice) - 1]
    found = [r for r in data["resources"] if r.get("category") == cat]
    if not found:
        print(f"No resources in {cat}.\n")
        return
    print(f"\n--- {cat} ---")
    for i, r in enumerate(found, 1):
        print_resource(i, r)
    print()


data = load()

while True:
    print("1) Add resource  2) Show resources  3) Add category  "
          "4) Browse categories  5) Quit")
    choice = input("> ")
    if choice == "1":
        add_resource(data)
    elif choice == "2":
        show_resources(data)
    elif choice == "3":
        add_category(data)
    elif choice == "4":
        browse_categories(data)
    elif choice == "5":
        break
    else:
        print("Invalid choice.\n")
