# Library List
library = []


def add_book():
    # Flush = True. Forces the terminal to show text the immediately
    print("/nis equals to Add Book", flush=True)
    book_id = input("Enter Book ID: ")
    print(f"-> Received ID: {book_id}")
    # This confirms python got your input
    name = input("Enter Book Name: ")
    print(f"-> Received Book Name:{name}")

    author = input("Enter Author Name: ")
    category = input("Enter Category: ")

    try:
        price = float(input("Enter Book Price: "))
    except ValueError:
        print("Invalid Price! Setting Price to 0.0")
        price = 0.0

    book = {
        "id": book_id,
        "name": name,
        "author": author,
        "category": category,
        "price": price,
        "status": "Available",
    }

    library.append(book)
    print("\nBook Added Successfully!", flush=True)
    print("Current Library Inventory: ", library, flush=True)
    # Run the function


def main():
    add_book()


if __name__ == "__main__":
    main()
