class Notification:
    #this is the only job of this class: send a message
    def send(self, message):
        print(f"[Notification] {message}")
