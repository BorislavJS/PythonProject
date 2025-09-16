# import math
# from math import ceil
#
# class PhotoAlbum:
#     PHOTOS_PER_PAGE = 4
#
#     def __init__(self, pages: int):
#         self.pages = pages
#         self.photos = [[] for _ in range(self.pages)]
#
#     @classmethod
#     def from_photos_count(cls, photos_count: int):
#         pages = math.ceil(photos_count / cls.PHOTOS_PER_PAGE)
#         return cls(pages)
#
#     def add_photo(self, label: str):
#         for idx, page in enumerate(self.photos):
#             if len(page) < self.PHOTOS_PER_PAGE:
#                 page.append(label)
#                 return f'{label} photo added successfully on page {idx + 1} slot {len(page)}'
#         return 'No more free slots'
#
#     def display(self):
#         result = []
#         for page in self.photos:
#             result.append("-" * 11)
#             photos_line = ' '.join("[]" for _ in page)
#             result.append(photos_line)
#         result.append("-" * 11)
#         return '\n'.join(result)
#
# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())
#

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, data: str):
        title, author = data.split(" - ")
        return cls(title, author)

    def info(self):
        return f"'{self.title}' by {self.author}"


book1 = Book("1984", "George Orwell")
book2 = Book.from_string("The Hobbit - J.R.R. Tolkien")

print(book1.info())  # '1984' by George Orwell
print(book2.info())  # 'The Hobbit' by J.R.R. Tolkien
