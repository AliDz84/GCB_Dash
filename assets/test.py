import sqlite3
import pandas as pd

cxn = sqlite3.connect('db.db')
wb = pd.read_excel('data.xlsx',sheet_name = 'commodity')
wb.to_sql(name='commodity',con=cxn,if_exists='replace',index=True)
cxn.commit()
cxn.close()
