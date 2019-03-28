import sqlite3

sqlite_file = 'my_db.sqlite'
table_name1 = 'my_clinicaltrials_id'
table_name2 = 'primary_keys'
new_field = 'NCT_id'
field_type = 'TEXT'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({nf} {ft})'\
	.format(tn=table_name1, nf=new_field, ft=field_type))
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
	.format(tn=table_name2, nf=new_field, ft=field_type))

conn.commit()
conn.close()
