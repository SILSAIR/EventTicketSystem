class Payment:
    def __init__(self, method="cash"):
        self.method = method

    def process(self, amount):
        print(f"Processing payment of ${amount:.2f} via {self.method}")
        return True
