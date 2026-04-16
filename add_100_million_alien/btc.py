import os

import pandas as pd
import sqlite3

from add_100_million_alien.configs import DB_FILE


def load_data():
    table_name = 'btc-usd-minute'
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)

    df = pd.read_csv(os.path.join(parent_dir, 'data', 'data.csv'))

    conn = sqlite3.connect(DB_FILE)

    df.to_sql(table_name, conn, if_exists='replace')

    conn.close()

load_data()