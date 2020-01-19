class GPS:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def get_lat(self):
        return self.lat

    def set_lat(self, lat):
        self.lat = lat

    def get_lon(self):
        return self.lon

    def set_lon(self, lon):
        self.lon = lon

    def __repr__(self):
     return str(self.lat) + str(self.lon)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)