import csv

class Customer:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }

class CRMSystem:
    def __init__(self, file_name='customers.csv'):
        self.file_name = file_name
        self.customers = self.load_customers()

    def load_customers(self):
        customers = []
        try:
            with open(self.file_name, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    customers.append(Customer(row['name'], row['email'], row['phone'], row['address']))
        except FileNotFoundError:
            print("No customer data found, starting fresh.")
        return customers

    def save_customers(self):
        with open(self.file_name, 'w', newline='') as file:
            fieldnames = ['name', 'email', 'phone', 'address']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for customer in self.customers:
                writer.writerow(customer.to_dict())

    def add_customer(self, name, email, phone, address):
        new_customer = Customer(name, email, phone, address)
        self.customers.append(new_customer)
        self.save_customers()
        print(f"Customer {name} added successfully.")

    def view_customers(self):
        if not self.customers:
            print("No customers found.")
            return
        print("\nCustomer List:")
        for customer in self.customers:
            print(f"Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}, Address: {customer.address}")

    def search_customer(self, search_term):
        found = False
        for customer in self.customers:
            if search_term.lower() in customer.name.lower() or search_term.lower() in customer.email.lower():
                print(f"Found: Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}, Address: {customer.address}")
                found = True
        if not found:
            print(f"No customer found for search term '{search_term}'.")

    def update_customer(self, email, name=None, phone=None, address=None):
        for customer in self.customers:
            if customer.email.lower() == email.lower():
                if name:
                    customer.name = name
                if phone:
                    customer.phone = phone
                if address:
                    customer.address = address
                self.save_customers()
                print(f"Customer {customer.name} updated successfully.")
                return
        print(f"No customer found with email {email}.")

    def delete_customer(self, email):
        for customer in self.customers:
            if customer.email.lower() == email.lower():
                self.customers.remove(customer)
                self.save_customers()
                print(f"Customer {customer.name} deleted successfully.")
                return
        print(f"No customer found with email {email}.")

def main():
    crm = CRMSystem()

    while True:
        print("\nCustomer Relationship Management System")
        print("1. Add Customer")
        print("2. View All Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone Number: ")
            address = input("Enter Address: ")
            crm.add_customer(name, email, phone, address)

        elif choice == '2':
            crm.view_customers()

        elif choice == '3':
            search_term = input("Enter name or email to search: ")
            crm.search_customer(search_term)

        elif choice == '4':
            email = input("Enter email of the customer to update: ")
            name = input("Enter new Name (leave blank to keep unchanged): ")
            phone = input("Enter new Phone (leave blank to keep unchanged): ")
            address = input("Enter new Address (leave blank to keep unchanged): ")
            crm.update_customer(email, name or None, phone or None, address or None)

        elif choice == '5':
            email = input("Enter email of the customer to delete: ")
            crm.delete_customer(email)

        elif choice == '6':
            print("Exiting CRM system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
