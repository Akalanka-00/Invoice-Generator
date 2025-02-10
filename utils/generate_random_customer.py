from faker import Faker

# Initialize the Faker library
fake = Faker()

# Function to generate and return random customer data
def generate_customer():
    customer = {
        'Name': fake.name(),
        'Address': fake.address(),
        'Email': fake.email(),
        'Phone': fake.phone_number(),
        'Country': fake.country(),
        'City': fake.city(),
        'Postal Code': fake.zipcode()
    }
    return customer


