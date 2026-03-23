import sqlite3


def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)


def insert_books(conn):
    books = [
        ("1984", "Джордж Оруэлл", 1949, "Дистопия", 328, 5),
        ("Убить пересмешника", "Харпер Ли", 1960, "Роман", 281, 4),
        ("Великий Гэтсби", "Фрэнсис Скотт Фицджеральд", 1925, "Классика", 180, 3),
        ("Моби Дик", "Герман Мелвилл", 1851, "Приключения", 635, 2),
        ("Война и мир", "Лев Толстой", 1869, "Исторический", 1225, 6),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Философский", 671, 5),
        ("Над пропастью во ржи", "Дж. Д. Сэлинджер", 1951, "Роман", 277, 3),
        ("Гордость и предубеждение", "Джейн Остин", 1813, "Роман", 279, 4)

    ]

    for book in books:
        conn.execute("""
            INSERT INTO books 
            (name, author, publication_year, genre, number_of_pages, number_of_copies)
            VALUES (?, ?, ?, ?, ?, ?)
        """, book)


if __name__ == "__main__":
    conn = sqlite3.connect("library.db")

    create_table(conn)
    insert_books(conn)

    conn.commit()
    conn.close()