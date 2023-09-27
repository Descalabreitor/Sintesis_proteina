class ARN:

    def __init__(self, adn):
        self.hebra = adn.data.replace("T", "U")

    def getData(self):
        return self.hebra
