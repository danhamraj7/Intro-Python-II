# Write a class to hold player information, e.g.
# what room they are in currently.


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []

    def pickup_item(self, item):
        if self.location.items.count(item) > 0:
            self.items.append(item)
            self.location.items.remove(item)
            item.pick_up()
        else:
            print(f"The {item.name} is not in this room.")

    def drop_item(self, item):
        if self.items.count(item) > 0:
            self.location.items.append(item)
            self.items.remove(item)
            item.drop()
        else:
            print(f"You do not have a {item.name} to drop.")

    def print_items(self):
        if not self.items:
            print("You have no items.")
        else:
            print("You have the following items: ")
            for x in self.items:
                print(x.name)
