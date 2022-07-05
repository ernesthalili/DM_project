from neo4j import GraphDatabase
import time
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "ernest"))

n_repeats = 10000
cypher = "MATCH (c1:CompetitionID)-[r1:PARTOF]->(country:CountryID)<-[r2:PARTOF]-(c2:CompetitionID) RETURN distinct(country)"

with driver.session() as session:
    total_time = 0
    for _ in range(n_repeats):
        with session.begin_transaction() as tx:
            start = time.time()
            result = tx.run(cypher)
            records = list(result)  # consume the records
            tx.commit()
            total_time += time.time() - start

avg_time = total_time*1000 / n_repeats
print('Average execution time:', avg_time, 'ms')