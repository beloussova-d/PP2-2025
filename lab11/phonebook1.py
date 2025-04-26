from configparser import ConfigParser
import psycopg2
import csv

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            # print('Connected to the PostgreSQL server.')
            return conn
    except (Exception, psycopg2.DatabaseError ) as error:
        print(error)

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
    """
    CREATE TABLE phones (
        user_name VARCHAR(255) PRIMARY KEY,
        user_phone VARCHAR(255) NOT NULL
    )
    """,
    )

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_from_csv(file_path):
    conn = connect(config)
    cur = conn.cursor()
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                name, phone = row
                sql="""INSERT INTO phones (user_name, user_phone) VALUES (%s, %s)
                ON CONFLICT (user_name) DO UPDATE 
                SET user_phone = %s"""
                cur.execute(sql, (name, phone, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("CSV data inserted successfully.")

def insert_from_console():
    conn = connect(config)
    cur = conn.cursor()
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    sql="""INSERT INTO phones (user_name, user_phone) VALUES (%s, %s)
    ON CONFLICT (user_name) DO UPDATE
                SET user_phone = %s"""
    cur.execute(sql, (name, phone, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("User data inserted successfully.")

def update_name(name,phone):
    updated_row_count = 0
    sql = """ UPDATE phones
                SET user_name = %s
                WHERE user_phone = %s"""
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (name, phone))
                updated_row_count = cur.rowcount
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

def update_phone(name,phone):
    updated_row_count = 0
    sql = """ UPDATE phones
                SET user_phone = %s
                WHERE user_name = %s"""
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (phone,name))
                updated_row_count = cur.rowcount
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count


def query_data():
    conn = connect(config)
    cur = conn.cursor()
    print("Filter options: all / name / phone")
    filter_by = input("Enter filter: ").strip().lower()

    if filter_by == "all":
        cur.execute("SELECT * FROM phones")
    elif filter_by == "name":
        name = input("Enter name to search: ")
        cur.execute("SELECT * FROM phones WHERE user_name ILIKE %s", (f"%{name}%",))
    elif filter_by == "phone":
        phone = input("Enter phone to search: ")
        cur.execute("SELECT * FROM phones WHERE user_phone LIKE %s", (f"%{phone}%",))
    else:
        print("Invalid filter.")
        return

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

def delete_by_name(name):
    """ Delete  """
    rows_deleted  = 0
    sql = 'DELETE FROM phones WHERE user_name = %s'
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (name,))
                rows_deleted = cur.rowcount
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted
def delete_by_phone(phone):
    """ Delete  """
    rows_deleted  = 0
    sql = 'DELETE FROM phones WHERE user_phone = %s'
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (phone,))
                rows_deleted = cur.rowcount
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted


with open('phonebook1.sql', 'r') as file:
    sql_code = file.read()

if __name__ == '__main__':
    config = load_config()
    # print(config)
    connect(config)
    # create_tables()
    # sqll="""ALTER TABLE phones
    # ADD CONSTRAINT unique_user_name UNIQUE (user_name);"""
    # try:
    #     config = load_config()
    #     with psycopg2.connect(**config) as conn:
    #         with conn.cursor() as cur:
    #             cur.execute(sqll)
    # except (psycopg2.DatabaseError, Exception) as error:
    #     print(error)

    while True:
        print("\nPhoneBook Menu:")
        print("1. Insert user")
        print("2. Update user")
        print("3. Query data/search")
        print("4. Delete data")
        print("5. ")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            way=input("Way: 1. console, 2. csv: ")
            if way == '1':
                insert_from_console()
            elif way == '2':
                file_path=input("enter path to csv: ")
                insert_from_csv(file_path)
            else:
                print("invalid")

        elif choice == '2':
            way=input("Update: 1. name, 2. phone: ")
            name = input("Name (new, if update it): ")
            phone = input("Phone (new, if update it): ")
            if way == '1':
                update_name(name, phone)
            elif way == '2':
                update_phone(name,phone)
            else:
                print("invalid")
        elif choice == '3':
            query_data()

        elif choice == '4':
            way=input("Way: 1. by name, 2. by phone: ")
            if way == '1':
                name = input("Enter name: ")
                rows_deleted=delete_by_name(name)
                print(f"Rows deleted: {rows_deleted}")
            elif way == '2':
                phone = input("Enter phone: ")
                rows_deleted=delete_by_phone(phone)
                print(f"Rows deleted: {rows_deleted}")
            else:
                print("invalid")

        elif choice == '5':   
            # limit = int(input("Limit: "))
            # offset = int(input("Offset: "))
            # call_get_users(limit, offset)
            import psycopg2

            names = ['Alice', 'Bob', 'Charlie']
            phones = ['1234567890', 'notaphone', '9876543210']

            conn = psycopg2.connect(**your_config)
            cur = conn.cursor()

            cur.execute("CALL insert_many_users(%s, %s);", (names, phones))

            conn.commit()
            cur.close()
            conn.close()

    
            

        # elif choice == '2':
        #     n = int(input("How many users? "))
        #     users = []
        #     for _ in range(n):
        #         name = input("Name: ")
        #         phone = input("Phone: ")
        #         users.append([name, phone])
        #     call_insert_many_users(users)

        # elif choice == '3':
        #     pattern = input("Search pattern: ")
        #     call_search(pattern)

        # elif choice == '4':
        #     limit = int(input("Limit: "))
        #     offset = int(input("Offset: "))
        #     call_get_users(limit, offset)

        # elif choice == '5':
        #     identifier = input("Name or Phone to delete: ")
        #     call_delete_user(identifier)

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
