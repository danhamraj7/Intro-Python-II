# Implement a class to hold room information.
# This should have name and description attributes.

class Room:
    def __init__(self, name, description, n_to=None, e_to=None, s_to=None, w_to=None,):
        self.name = name
        self.description = description
        self.routes = {
            "n": n_to,
            "e": n_to,
            "s": n_to,
            "w": n_to,
        }
