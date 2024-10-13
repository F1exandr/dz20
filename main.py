import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="northwind",
    user="your_username",
    password="your_password"
)

cur = conn.cursor()

def main_menu():
    print("Northwind Database Interactive System")
    print("-------------------------------------")
    print("1. View all customers")
    print("2. View all orders for a customer")
    print("3. Add a new order")
    print("4. Update an existing order")
    print("5. Delete an order")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_all_customers()
    elif choice == "2":
        view_all_orders_for_customer()
    elif choice == "3":
        add_new_order()
    elif choice == "4":
        update_existing_order()
    elif choice == "5":
        delete_order()
    elif choice == "6":
        print("Goodbye!")
        conn.close()
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def view_all_customers():
    cur.execute("SELECT * FROM customers")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    main_menu()

def view_all_orders_for_customer():
    customer_id = input("Enter the customer ID: ")
    cur.execute("SELECT * FROM orders WHERE customer_id = %s", (customer_id,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    main_menu()

def add_new_order():
    customer_id = input("Enter the customer ID: ")
    order_date = input("Enter the order date (YYYY-MM-DD): ")
    required_date = input("Enter the required date (YYYY-MM-DD): ")
    shipped_date = input("Enter the shipped date (YYYY-MM-DD): ")
    freight = input("Enter the freight: ")
    ship_name = input("Enter the ship name: ")
    ship_address = input("Enter the ship address: ")
    ship_city = input("Enter the ship city: ")
    ship_region = input("Enter the ship region: ")
    ship_postal_code = input("Enter the ship postal code: ")
    ship_country = input("Enter the ship country: ")

    cur.execute("""
        INSERT INTO orders (
            customer_id,
            order_date,
            required_date,
            shipped_date,
            freight,
            ship_name,
            ship_address,
            ship_city,
            ship_region,
            ship_postal_code,
            ship_country
        ) VALUES (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
    """, (
        customer_id,
        order_date,
        required_date,
        shipped_date,
        freight,
        ship_name,
        ship_address,
        ship_city,
        ship_region,
        ship_postal_code,
        ship_country
    ))

    conn.commit()
    print("Order added successfully!")
    main_menu()

def update_existing_order():
    order_id = input("Enter the order ID: ")
    column_name = input("Enter the column name to update: ")
    new_value = input("Enter the new value: ")

    cur.execute("UPDATE orders SET {} = %s WHERE order_id = %s".format(column_name), (new_value, order_id))

    conn.commit()
    print("Order updated successfully!")
    main_menu()

def delete_order():
    order_id = input("Enter the order ID: ")

    cur.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))

    conn.commit()
    print("Order deleted successfully!")
    main_menu()

main_menu()