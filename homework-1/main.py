import psycopg2
import pandas as pd
conn = psycopg2.connect(
    dbname="north",
    user="jasey",
    password="jasey",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Загрузка данных из файла north_data.csv
employees = pd.read_csv('employees_data.csv')
customers = pd.read_csv('customers_data.csv')
orders = pd.read_csv('orders_data.csv')
# Запись данных в таблицу в базе данных
for row in employees.itertuples(index=False, name=None):
    cursor.execute("INSERT INTO employees VALUES %s", (row,))

for row in customers.itertuples(index=False, name=None):
    cursor.execute("INSERT INTO customers VALUES %s", (row,))

for row in orders.itertuples(index=False, name=None):
    cursor.execute("INSERT INTO orders (order_id,customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s,%s)", (row[0], row[1], row[2], row[3],row[4]))
# Подтверждение изменений и закрытие курсора и соединения
conn.commit()
cursor.close()
conn.close()