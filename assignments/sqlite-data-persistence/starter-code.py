import sqlite3
from sqlite3 import Error

DB_FILE = "data.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    read INTEGER NOT NULL DEFAULT 0
);
"""

SAMPLE_BOOKS = [
    ("The Hobbit", "J.R.R. Tolkien", 1937, 0),
    ("Python Basics", "Jane Doe", 2024, 1),
    ("Data Science 101", "Alex Smith", 2025, 0),
]


def create_connection(db_file: str):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None


def initialize_database(conn):
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE_SQL)
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM books")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.executemany(
            "INSERT INTO books (title, author, year, read) VALUES (?, ?, ?, ?)",
            SAMPLE_BOOKS,
        )
        conn.commit()


def list_books(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, year, read FROM books")
    books = cursor.fetchall()
    print("Books in library:")
    for book in books:
        read_status = bool(book[4])
        print(f"{book[0]} | {book[1]} | {book[2]} | {book[3]} | {read_status}")


def add_book(conn, title, author, year, read):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, year, read) VALUES (?, ?, ?, ?)",
        (title, author, year, int(read)),
    )
    conn.commit()
    return cursor.lastrowid


def update_read_status(conn, book_id, read):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE books SET read = ? WHERE id = ?",
        (int(read), book_id),
    )
    conn.commit()
    return cursor.rowcount


def delete_book(conn, book_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    return cursor.rowcount


def main():
    conn = create_connection(DB_FILE)
    initialize_database(conn)

    list_books(conn)

    print("\nAdd a new book")
    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year: "))
    read = input("Read? (y/n): ").strip().lower() == "y"
    book_id = add_book(conn, title, author, year, read)
    print(f"Added book with ID: {book_id}\n")

    list_books(conn)

    print("\nUpdate read status for a book")
    book_id = int(input("Book ID to update: "))
    read = input("Mark as read? (y/n): ").strip().lower() == "y"
    rows = update_read_status(conn, book_id, read)
    if rows:
        print("Book status updated.")
    else:
        print("Book not found.")

    print("\nDelete a book")
    book_id = int(input("Book ID to delete: "))
    rows = delete_book(conn, book_id)
    if rows:
        print("Book deleted.")
    else:
        print("Book not found.")

    print("\nFinal book list:")
    list_books(conn)
    conn.close()


if __name__ == "__main__":
    main()
