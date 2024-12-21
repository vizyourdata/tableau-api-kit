
# import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL


load_dotenv()
def redshift_query(qry):
    REDSHIFT_USER = os.environ.get('post_user')
    REDSHIFT_PASSWORD = os.environ.get('post_password')
    REDSHIFT_HOST = os.environ.get('post_host')
    REDSHIFT_PORT = os.environ.get('post_port')
    REDSHIFT_DATABASE = os.environ.get('post_database')


    
    # Create the connection string
    db_url = URL.create(
        drivername="postgresql+psycopg2",
        username=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD,
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT,
        database=REDSHIFT_DATABASE
    )

    # Create an engine
    engine = create_engine(
        db_url,
        pool_size=10,      # Set the pool size (e.g., 10)
        max_overflow=20,   # Allow extra connections beyond the pool size (e.g., 20)
        pool_timeout=30,   # Timeout after 30 seconds if no connections are available
        pool_recycle=300  # Recycle connections every 30 minutes (1800 seconds)
        )

    with engine.connect() as connection:
        df = pd.read_sql(qry, connection)
    
    # Optional: You could also explicitly dispose of the engine to clean up connections
    engine.dispose()
    
    return df



def superstore_corr():
    # SQL Query to get current users in each group
    query = """
        SELECT
            customer_id,
            COUNT(order_id) AS order_count,
            SUM(sales) AS total_sales,
            ROUND(SUM(sales) / COUNT(order_id), 2) AS average_order_value
        FROM
            tableauadmin.tableauadmin_demosuperstore
        GROUP BY
            customer_id
    """

    # Execute the SQL query and return the DataFrame for current users
    df = redshift_query(query)

    corr =  df['order_count'].corr(df['average_order_value'])
    return corr

if __name__ == "__main__":
    correlation = superstore_corr()
    print("Correlation coefficient between order count and AOV:", correlation)