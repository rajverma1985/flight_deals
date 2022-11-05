class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city = city

    def iata_code(self):
        return self.city
