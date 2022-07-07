import mariadb
import time
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="example",
        host="0.0.0.0",
        port=3306,
        database="footballdb"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

total_time = 0
n_repeats = 10000
for _ in range(n_repeats):
	start = time.time()
	cur.execute("SELECT CountryID, CompetitionName " \
         "FROM competition_country_r AS CC, competitions_node AS CN " \
         "WHERE CC.CompetitionID = CN.CompetitionID " \
         "GROUP BY CountryID, CompetitionName")
	conn.commit() 
	total_time += time.time() - start


avg_time = total_time*1000 / n_repeats
print('Average execution time:', avg_time, 'ms')
