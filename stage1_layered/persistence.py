# PERSISTENCE LAYER: stores and finds data.
# No shop rules, no status codes. It imports nothing from the other layers.

books = {}
orders = {}


def reset():
    books.clear()
    orders.clear()


def save_book(title, price_cents, stock):
    book = {"id": len(books) + 1, "title": title, "price_cents": price_cents, "stock": stock}
    books[book["id"]] = book
    return book


def find_book(book_id):
    return books.get(book_id)


def all_books():
    book_list = []
    for book in books.values():
        book_list.append(book)
    return book_list


def update_stock(book_id, new_stock):
    book = books.get(book_id)
    book["stock"] = new_stock



def save_order(order):
    order["id"] = len(orders)+1
    orders[order["id"]] = order
    return order
    # TODO step 1: give the order the next id, store it in `orders` and return it
    raise NotImplementedError("TODO step 1")


def find_order(order_id):
    if not orders.get(order_id):
        return None
    return orders.get(order_id)
    # TODO step 1: return the order, or None if it does not exist
    raise NotImplementedError("TODO step 1")
