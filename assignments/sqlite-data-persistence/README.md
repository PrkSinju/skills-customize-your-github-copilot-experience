# 📘 Assignment: SQLite Data Persistence

## 🎯 Objective

Teach students how to store and manage data in a local SQLite database using Python. This assignment covers creating tables, inserting records, querying data, and updating or deleting rows.

## 📝 Tasks

### 🛠️ Create a SQLite Database App

#### Description
Build a Python script that uses the `sqlite3` module to create a database file, define a table, and add new records from user input.

#### Requirements
Completed program should:

- Create or connect to a local SQLite database file (for example `data.db`).
- Create a table called `books` with fields `id`, `title`, `author`, `year`, and `read`.
- Insert at least three sample records when the database is first initialized.
- Prompt the user to add a new book record.
- Save the book record into the database.

### 🛠️ Query and Update Stored Data

#### Description
Add features for listing stored records, updating a record's status, and deleting entries.

#### Requirements
Completed program should:

- Query and print all books stored in the `books` table.
- Allow the user to mark a book as read or unread.
- Allow the user to delete a book by its `id`.
- Use SQL safely and handle errors when a requested record does not exist.

#### Example output

```text
Books in library:
1 | The Hobbit | J.R.R. Tolkien | 1937 | False
2 | Python Basics | Jane Doe | 2024 | True
```
