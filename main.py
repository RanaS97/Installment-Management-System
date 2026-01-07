import modules.customer as customer
import modules.product as product
import modules.installment as installment

def print_start_menu():
    print("\n" + "="*60)
    print("  INSTALLMENT MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Admin Panel (Full Control)")
    print("2. Customer Panel (View Only)")
    print("3. Exit")
    print("-"*60)

def print_admin_menu():
    print("\n" + "="*60)
    print("      ADMIN PANEL")
    print("="*60)
    print("1. Customer Management")
    print("2. Product Management")
    print("3. Installment Management")
    print("4. Back to Start")
    print("-"*60)

def print_customer_view_menu():
    print("\n" + "="*60)
    print("      CUSTOMER PANEL (View Only)")
    print("="*60)
    print("1. View All Customers")
    print("2. View All Products")
    print("3. View All Installments")
    print("4. Back to Start")
    print("-"*60)

def customer_menu():
    while True:
        print("\n" + "="*60)
        print("      CUSTOMER MANAGEMENT")
        print("="*60)
        print("1. Add Customer")
        print("2. View All Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Back to Main Menu")
        print("-"*60)
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '1':
            print("\n--- Add Customer ---")
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            address = input("Enter address: ").strip()
            
            success, message = customer.add_customer(name, phone, address)
            print(f"✓ {message}" if success else f"✗ {message}")
        
        elif choice == '2':
            print("\n--- All Customers ---")
            customer.view_all_customers()
        
        elif choice == '3':
            print("\n--- Search Customer ---")
            customer_id = input("Enter customer ID: ").strip()
            cust, message = customer.search_customer(customer_id)
            
            if cust:
                print(f"\nID: {cust['customer_id']}")
                print(f"Name: {cust['name']}")
                print(f"Phone: {cust['phone']}")
                print(f"Address: {cust['address']}")
            else:
                print(f"✗ {message}")
        
        elif choice == '4':
            print("\n--- Update Customer ---")
            customer_id = input("Enter customer ID: ").strip()
            name = input("Enter new name (blank to skip): ").strip() or None
            phone = input("Enter new phone (blank to skip): ").strip() or None
            address = input("Enter new address (blank to skip): ").strip() or None
            
            success, message = customer.update_customer(customer_id, name, phone, address)
            print(f"✓ {message}" if success else f"✗ {message}")
        
        elif choice == '5':
            print("\n--- Delete Customer ---")
            customer_id = input("Enter customer ID: ").strip()
            confirm = input("Confirm (yes/no): ").strip().lower()
            
            if confirm == 'yes':
                success, message = customer.delete_customer(customer_id)
                print(f"✓ {message}" if success else f"✗ {message}")
            else:
                print("✗ Cancelled")
        
        elif choice == '6':
            break
        else:
            print("✗ Invalid choice")

def product_menu():
    while True:
        print("\n" + "="*60)
        print("      PRODUCT MANAGEMENT")
        print("="*60)
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Back to Main Menu")
        print("-"*60)
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '1':
            print("\n--- Add Product ---")
            product_name = input("Enter product name: ").strip()
            price = input("Enter price: ").strip()
            
            success, message = product.add_product(product_name, price)
            print(f"✓ {message}" if success else f"✗ {message}")
        
        elif choice == '2':
            print("\n--- All Products ---")
            product.view_all_products()
        
        elif choice == '3':
            print("\n--- Search Product ---")
            product_id = input("Enter product ID: ").strip()
            prod, message = product.search_product(product_id)
            
            if prod:
                print(f"\nID: {prod['product_id']}")
                print(f"Name: {prod['product_name']}")
                print(f"Price: {prod['price']}")
            else:
                print(f"✗ {message}")
        
        elif choice == '4':
            print("\n--- Update Product ---")
            product_id = input("Enter product ID: ").strip()
            product_name = input("Enter new name (blank to skip): ").strip() or None
            price = input("Enter new price (blank to skip): ").strip() or None
            
            success, message = product.update_product(product_id, product_name, price)
            print(f"✓ {message}" if success else f"✗ {message}")
        
        elif choice == '5':
            print("\n--- Delete Product ---")
            product_id = input("Enter product ID: ").strip()
            confirm = input("Confirm (yes/no): ").strip().lower()
            
            if confirm == 'yes':
                success, message = product.delete_product(product_id)
                print(f"✓ {message}" if success else f"✗ {message}")
            else:
                print("✗ Cancelled")
        
        elif choice == '6':
            break
        else:
            print("✗ Invalid choice")

def installment_menu():
    while True:
        print("\n" + "="*60)
        print("      INSTALLMENT MANAGEMENT")
        print("="*60)
        print("1. Create Installment")
        print("2. View All Installments")
        print("3. Search Installment")
        print("4. Make Payment")
        print("5. Customer Total Balance")
        print("6. Customer Installments")
        print("7. Back to Main Menu")
        print("-"*60)
        
        choice = input("Enter choice (1-7): ").strip()
        
        if choice == '1':
            print("\n--- Create Installment ---")
            customer_id = input("Enter customer ID: ").strip()
            product_id = input("Enter product ID: ").strip()
            paid_amount = input("Enter paid amount: ").strip()
            
            success, message = installment.create_installment(customer_id, product_id, paid_amount)
            print(f"✓ {message}" if success else f"✗ {message}")
        
        elif choice == '2':
            print("\n--- All Installments ---")
            installment.view_all_installments()
        
        elif choice == '3':
            print("\n--- Search Installment ---")
            installment_id = input("Enter installment ID: ").strip()
            inst, message = installment.search_installment(installment_id)
            
