class Band:
    all = []
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        self._concerts = []
        Band.all.append(self)
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name,str) and len(name) > 0:
            self._name = name
        # else:
        #     raise Exception("Band name must be a non-empty string")
    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Hometown must be greater than zero characters")
        self._hometown = value
    def name(self):
        return self._name

    def concerts(self):
        return self._concerts
    def add_concert(self, concert):
        self._concerts.append(concert)

    def venues(self):
        return list({concert._venue for concert in self._concerts})

    # def venues(self):
    #     return set(concert.venue for concert in self.concerts)
    
    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]


class Concert:
    all = []
    def __init__(self, date, band, venue):
        self._date = date
        self._band = band
        self._venue = venue
        Concert.all.append(self)
        band._concerts.append(self)
        # venue.concerts.append(self)

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) > 0:
            self._date = date

    @property
    def band(self):
        return self._band
    @band.setter
    def band(self, band):
        if isinstance(band, Band):
            self._band = band

    @property
    def venue(self):
        return self._venue
    @venue.setter
    def venue(self, venue):
        if isinstance(venue, Venue):
            self._venue = venue

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
    
    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city) > 0:
            self._city = city
    

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        return list(set(concert.band for concert in self.concerts()))

band = Band(name="boygenius", hometown="NYC")
venue = Venue(name="Theatre", city="NYC")
concert_1 = Concert(date="Nov 22", band=band, venue=venue)
concert_2 = Concert(date="Nov 27", band=band, venue=venue)
band.add_concert(concert_1)
band.add_concert(concert_2)
# print(band.concerts)