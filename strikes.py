# import failure

class Strikes:

    def __init__(self):
        self.counter = 0

    def strike(self):
        self.counter += 1
        if self.counter >= 3:
            pass # call failure function
