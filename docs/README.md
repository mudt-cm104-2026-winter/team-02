# Documentation of our project: "Cybersecurity Study Resources"

This simple project written in Python designed for organizing and storing useful educational or work resources.

# The menu

As the application is opened, the user is offered 5 options: Add resource, Show resources, Add category, Browse categories and quit. Users can add new resources by entering a topic, material type, URL link, and assigning an appropriate category. Additionally, the application allows for the creation of custom categories, while resources without a selected group are automatically labeled as Uncategorized. Through a clear text-based menu, the user can list all saved materials at once at any time. A filtering feature is also implemented, enabling users to browse resources sorted exclusively within a single selected category. The entire program runs in an interactive loop that executes until the user explicitly selects the option to exit the application.

# Example Usage in Python

1) Add resource  2) Show resources  3) Add category  4) Browse categories  5) Quit
> 1
Topic: Internet Network
Material: Wireshark Packet Sniffer
URL: wireshark.org
No categories yet. Saving as Uncategorized.
Saved.

1) Add resource  2) Show resources  3) Add category  4) Browse categories  5) Quit
> 3
Category name: Network Module
Category added.

1) Add resource  2) Show resources  3) Add category  4) Browse categories  5) Quit
> 1
Topic: DNS
Material: website for DNS
URL: dnschecker.org
1. Network Module
Category number (Enter to skip): 1
Saved.

1) Add resource  2) Show resources  3) Add category  4) Browse categories  5) Quit
> 2
1. Internet Network
   Category: Uncategorized
   Material: Wireshark Packet Sniffer
   URL: wireshark.org
2. DNS
   Category: Network Module
   Material: website for DNS
   URL: dnschecker.org

1) Add resource  2) Show resources  3) Add category  4) Browse categories  5) Quit
> 4
1. Network Module
Category number: 1

--- Network Module ---
1. DNS
   Category: Network Module
   Material: website for DNS
   URL: dnschecker.org

1) Add resource  2) Show resources  3) Add category  4) Browse categories  5) Quit
> 5

This is an example of this application run in Terminal. We firstly added one material on a certain topic and it was saved as Uncategorized. After being taken back to the main menu, the same 5 offers were shown. Now, the category option was chosen beforehand. After that the new material was added and saved in the category recently created. Addiotionally, by choosing Show resources option, list of all materials with its resources is shown. Finally, the option quit makes application to stop working.


# Future Improvements

- adding search by keyboard, delete and edit feature


# Limitations

- cannot check if the URL is valid


# Conclusion

Overall, the application successfully fulfills its core goal of storing, categorizing, and retrieving useful links through an intuitive command-line interface. Its straightforward architecture makes it easy to use out of the box while leaving a solid foundation for future features such as keyword search, entry editing, and URL validation.