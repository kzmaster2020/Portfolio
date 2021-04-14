import pandas

import psycopg2
#from configparser import ConfigParser

thistuple = ["apple", "banana", "cherry"]
print(str(thistuple[1]))

df = pandas.read_csv("train.csv")



print(df.head(10))

history = df['LoanAmount'].hist(bins=20)

print(history)

dn = pandas.DataFrame(df, columns=['Loan_ID', 'Gender'])
print(dn)
conn = psycopg2.connect("host=shinji.cs.ndsu.nodak.edu dbname=zanders_db765f20 user=zanders_765f20 password=SEw3S77uMC port=5432")

cur = conn.cursor()
print (conn)

cur.execute("CREATE TABLE LOAN_DATA ( Loan_ID SERIAL PRIMARY KEY, Gender VARCHAR(10), Married VARCHAR(3), Dependents SMALLINT, Education VARCHAR(25), Self_Employed VARCHAR(3), ApplicantIncome INT, CoapplicantIncome INT, LoanAmount INT, Loan_Amount_Term INT, Credit_History SMALLINT, Property_Area VARCHAR(25), Loan_Status VARCHAR(30));")
for row in dn.itertuples():
	cur.execute("INSERT INTO trainStuff(Loan_ID, Gender) VALUES (%s, %s)", row.Loan_ID,  row.Gender)
#cur.execute("SELECT * FROM trainSheet;")
#cur.fetchone()

conn.commit()
cur.close()
conn.close()
