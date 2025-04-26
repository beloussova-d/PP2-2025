import psycopg2
from psycopg2 import sql

def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="password8"
    )

def call_insert_or_update_user(name, phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.callproc('insert_or_update_user', [name, phone])
            print("User inserted or updated.")

def call_insert_many_users(user_list):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.callproc('insert_many_users', (user_list,))
            invalids = cur.fetchone()[0]
            if invalids:
                print("Invalid entries:")
                for entry in invalids:
                    print(f" - Name: {entry[0]}, Phone: {entry[1]}")
            else:
                print("All users inserted successfully.")

def call_search(pattern):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
            rows = cur.fetchall()
            print("Search results:")
            for row in rows:
                print(row)

def call_get_users(limit, offset):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_users(%s, %s)", (limit, offset))
            rows = cur.fetchall()
            print(f"Users (limit={limit}, offset={offset}):")
            for row in rows:
                print(row)

def call_delete_user(identifier):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.callproc('delete_user', [identifier])
            print("User(s) deleted.")

# Simple CLI menu to test functions
if __name__ == "__main__":
    while True:
        print("\n📞 PhoneBook Menu:")
        print("1. Insert or update user")
        print("2. Insert many users")
        print("3. Search by pattern")
        print("4. Get users with pagination")
        print("5. Delete user by name or phone")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            call_insert_or_update_user(name, phone)

        elif choice == '2':
            n = int(input("How many users? "))
            users = []
            for _ in range(n):
                name = input("Name: ")
                phone = input("Phone: ")
                users.append([name, phone])
            call_insert_many_users(users)

        elif choice == '3':
            pattern = input("Search pattern: ")
            call_search(pattern)

        elif choice == '4':
            limit = int(input("Limit: "))
            offset = int(input("Offset: "))
            call_get_users(limit, offset)

        elif choice == '5':
            identifier = input("Name or Phone to delete: ")
            call_delete_user(identifier)

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
