class ArtGallery:

    # Parameterized constructor
    def __init__(self, gallery_name, location):
        self.gallery_name = gallery_name
        self.location = location

        # Empty artwork list by default
        self.artworks = []

        print("\nGallery created successfully!")

    def add_artwork(self):
        title = input("Enter artwork title: ")
        artist = input("Enter artist name: ")
        year = input("Enter year of artwork: ")

        artwork = {
            "title": title,
            "artist": artist,
            "year": year
        }

        self.artworks.append(artwork)

        print("Artwork added successfully!")

    def display_artworks(self):

        if len(self.artworks) == 0:
            print("\nNo artworks in the gallery.")
        else:
            print("\n========== ARTWORK COLLECTION ==========")

            for artwork in self.artworks:
                print("Title:", artwork["title"])
                print("Artist:", artwork["artist"])
                print("Year:", artwork["year"])
                print("--------------------------------------")


    def search_artwork(self):

        search_title = input("Enter artwork title to search: ")

        found = False

        for artwork in self.artworks:

            if artwork["title"].lower() == search_title.lower():

                print("\nArtwork Found!")
                print("Title:", artwork["title"])
                print("Artist:", artwork["artist"])
                print("Year:", artwork["year"])

                found = True

        if not found:
            print("Artwork not found.")

    def remove_artwork(self):

        remove_title = input("Enter artwork title to remove: ")

        for artwork in self.artworks:

            if artwork["title"].lower() == remove_title.lower():

                self.artworks.remove(artwork)

                print("Artwork removed successfully!")

                return

        print("Artwork not found.")

    def __del__(self):

        print("\nGallery object has been closed or deleted.")


gallery = ArtGallery(
    "Dream Art Gallery",
    "Lagos"
)

while True:

    print("\n==========================================")
    print("       ART GALLERY COLLECTION MANAGER")
    print("==========================================")

    print("Gallery:", gallery.gallery_name)
    print("Location:", gallery.location)

    print("\n1. Add Artwork")
    print("2. Display Artworks")
    print("3. Search Artwork")
    print("4. Remove Artwork")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        gallery.add_artwork()

    elif choice == "2":

        gallery.display_artworks()

    elif choice == "3":

        gallery.search_artwork()

    elif choice == "4":

        gallery.remove_artwork()

    elif choice == "5":

        print("\nThank you for using the Art Gallery Collection Manager!")

        break

    else:

        print("\nInvalid choice. Please try again.")