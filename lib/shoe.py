class Shoe:
    def __init__(self, brand, size, color="Black", price=100):
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            raise ValueError("Brand must be a string.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if  not isinstance(value, int):
            print("size must be an integer") 
            self._size = value
        else:
             
             self._size = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str):
            self._color = value
        else:
            raise ValueError("Color must be a string.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._price = value
        else:
            raise ValueError("Price must be a positive number.")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"   
