from neo4j import GraphDatabase, BoltStatementResult, graph
from matplotlib import pyplot as plt

driver = GraphDatabase.driver("bolt://localhost:11011", auth=("neo4j", "wwe1"))
session = driver.session()
list1 = []
list2 = []

x = {"regrex": "V.x*"}
ab = '''MATCH (n)
DETACH DELETE n'''
data1=session.run(ab,x)
# q = '''MERGE (Natasha:Person {id:'Natasha'})
# MERGE (Pierre:Person {id:'Pierre'})
# MERGE (Sonya:Person {id:'Sonya'})
# MERGE (Andrew:Person {id:'Andrew'})
# MERGE (Napolean:Person {id:'Napolean'})
# MERGE (Prince:Person {id:'Prince'})
#
# MERGE (Natasha)-[:STRONGEST]->(Pierre)
# MERGE (Natasha)-[:STRONGEST]->(Sonya)
# MERGE (Natasha)-[:STRONGEST]->(Andrew)
# MERGE (Napolean)-[:STRONGEST]->(Natasha)
# MERGE (Sonya)-[:STRONGEST]->(Prince);'''

q = '''MERGE (nNatasha:User {id:'Natasha'})
MERGE (nPierre:User {id:'Pierre'})
MERGE (nSonya:User {id:'Sonya'})
MERGE (nAndrew:User {id:'Andrew'})
MERGE (nNapolean:User {id:'Napolean'})
MERGE (nPrince:User {id:'Prince'})

MERGE (nNatasha)-[:MANAGE]->(nPierre)
MERGE (nNatasha)-[:MANAGE]->(nCharles)
MERGE (nNatasha)-[:MANAGE]->(nAndrew)
MERGE (nNapolean)-[:MANAGE]->(nNatasha)
MERGE (nSonya)-[:MANAGE]->(Prince);'''
data1 = session.run(q, x)
e = '''CALL algo.betweenness.stream('User','MANAGE',{direction:'out'})
YIELD nodeId, centrality

MATCH (user:User) WHERE id(user) = nodeId

RETURN user.id AS user,centrality
ORDER BY centrality DESC;'''
data = session.run(e, x)
for city in data:
    list1.append(city["user"])
    list2.append(city["centrality"])
print(list1)
print(list2)
plt.xlabel("Persons")
plt.ylabel("Centrality")
plt.title('Centrality')
plt.bar(list1, list2)
plt.show()
