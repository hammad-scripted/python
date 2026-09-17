class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = False
        print( f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}\nIs Read: {self.is_read}" )
        print("\n")
        print(f"self is: {self}")
    
    def describe(self):
        print(f"This book is {self.title} by {self.author}")
    
    
book1=Book("The Great Gatsby","F. Scott Fitzgerald", 180)
print(f"book1 is: {book1}")
book1.describe()