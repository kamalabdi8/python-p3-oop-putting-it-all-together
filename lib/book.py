class Book:
    def __init__(self, title, page_count, author="Unknown", genre="Unknown", price=0.0):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 100:
            self._title = value
        else:
            raise ValueError("Title must be a string between 1 and 100 characters.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 50:
            self._author = value
        else:
            raise ValueError("Author name must be a string between 1 and 50 characters.")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 30:
            self._genre = value
        else:
            raise ValueError("Genre must be a string between 1 and 30 characters.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._price = value
        else:
            raise ValueError("Price must be a non-negative number.")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int) and value > 0:
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")        
