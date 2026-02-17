import sqlite3

# 1. Connect to SQLite (this automatically creates a file named 'crm.db')
conn = sqlite3.connect('crm.db')
cursor = conn.cursor()

# 2. Create a table for Maintenance Tickets
cursor.execute('''
CREATE TABLE IF NOT EXISTS Maintenance_Tickets (
    Ticket_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Property_ID TEXT,
    Status TEXT,
    Risk_Percentage REAL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()
print("Success! Database 'crm.db' and 'Maintenance_Tickets' table created.")