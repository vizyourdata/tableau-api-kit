import pandas as pd
import random
import datetime

# Generate a 3-year history of daily order dates
start_date = datetime.datetime.now() - datetime.timedelta(weeks=3 * 52)
num_days = 3 * 365  # Approximate number of days in 3 years

# Additional product categories
additional_categories = [
    'Books', 'Beauty Products', 'Toys', 'Kitchen Appliances',
    'Health Supplements', 'Fitness Equipment', 'Clothing Accessories',
    'Pet Supplies', 'Home Decor', 'Office Supplies'
]

# Generate consistent product data
product_categories = ['Electronics', 'Apparel', 'Home Goods'] + additional_categories
products_sample = pd.DataFrame({
    'id': range(1, 31),  # 30 products
    'name': [f"Product {i}" for i in range(1, 31)],
    'category': [random.choice(product_categories) for _ in range(30)],
    'tax_rate': [round(random.uniform(0.05, 0.15), 2) for _ in range(30)],
    'currency_code': ['USD' for _ in range(30)],
    'price_gross': [round(random.uniform(20, 200), 2) for _ in range(30)],
    'price_net': [round(random.uniform(15, 150), 2) for _ in range(30)],
})

# Generate variable purchases
def generate_variable_purchases(categories, days, start_date):
    purchases = []
    for day in range(days):
        current_date = start_date + datetime.timedelta(days=day)
        for category in categories:
            # Randomize purchases: favor certain categories or periods
            daily_count = random.choices([0, 1, 2, 3, 4, 5], weights=[50, 20, 15, 10, 4, 1])[0]
            for _ in range(daily_count):
                purchase_time = current_date + datetime.timedelta(
                    hours=random.randint(0, 23), minutes=random.randint(0, 59)
                )
                purchases.append((category, purchase_time))
    return purchases

variable_purchases = generate_variable_purchases(product_categories, num_days, start_date)

# Create orders dataset
orders_sample = pd.DataFrame({
    'order_id': range(1, len(variable_purchases) + 1),
    'category': [purchase[0] for purchase in variable_purchases],
    'created_at': [purchase[1].strftime('%Y-%m-%d %H:%M:%S') for purchase in variable_purchases],
    'updated_at': [(purchase[1] + datetime.timedelta(hours=random.randint(1, 48))).strftime('%Y-%m-%d %H:%M:%S')
                   for purchase in variable_purchases],
    'device_id': [random.randint(1000, 2000) for _ in range(len(variable_purchases))],
    'location_id': [random.randint(1, 5) for _ in range(len(variable_purchases))],
    'employee_id': [random.randint(1, 10) for _ in range(len(variable_purchases))],
    'currency_code': ['USD' for _ in range(len(variable_purchases))],
    'receipt_number': [f"RCPT-{random.randint(1000, 9999)}" for _ in range(len(variable_purchases))],
    'type': ['sale' for _ in range(len(variable_purchases))],
    'total_gross': [round(random.uniform(100, 500), 2) for _ in range(len(variable_purchases))],
    'total_tax': [round(random.uniform(10, 50), 2) for _ in range(len(variable_purchases))],
    'total_net': [round(random.uniform(50, 450), 2) for _ in range(len(variable_purchases))],
    'payment_method': ['card' for _ in range(len(variable_purchases))],
    'paid_amount': [round(random.uniform(100, 500), 2) for _ in range(len(variable_purchases))],
    'note': [None for _ in range(len(variable_purchases))],
})

# Create order lines dataset
order_lines_sample = pd.DataFrame({
    'unit_price': [round(random.uniform(10, 100), 2) for _ in range(len(variable_purchases) * 3)],  # 3 lines per order
    'price': [round(random.uniform(50, 300), 2) for _ in range(len(variable_purchases) * 3)],
    'tax_rate': [round(random.uniform(0.05, 0.15), 2) for _ in range(len(variable_purchases) * 3)],
    'tax_amount': [round(random.uniform(5, 30), 2) for _ in range(len(variable_purchases) * 3)],
    'price_net': [round(random.uniform(40, 270), 2) for _ in range(len(variable_purchases) * 3)],
    'product_id': [random.randint(1, 30) for _ in range(len(variable_purchases) * 3)],  # Match product IDs
    'order_id': [random.randint(1, len(variable_purchases)) for _ in range(len(variable_purchases) * 3)],
    'quantity': [random.randint(1, 5) for _ in range(len(variable_purchases) * 3)],
})

# Save datasets to CSV
orders_sample.to_csv('orders.csv', index=False)
products_sample.to_csv('products.csv', index=False)
order_lines_sample.to_csv('order_lines.csv', index=False)
