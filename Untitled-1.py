import duckdb
con=duckdb.connect('swati_files.duckdb')
re=con.execute("select count(Gender) as male from employees").fetchall()
print(re)
con.close()