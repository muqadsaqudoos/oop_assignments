class EventTracker:
    _self = None

    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self):
        self.api_url = "http://example.com"

    def printTrack(self):
        print(f"TODO track event at {self.api_url}")

    def updateTrack(self, trk):
        self.api_url = trk

tracker1 = EventTracker()
tracker2 = EventTracker()
print(tracker2 is tracker1)
tracker2.updateTrack("http://not-an-example.com")
tracker1.printTrack()
print(tracker1 is tracker2)


