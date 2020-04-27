
from neo4j import GraphDatabase, BoltStatementResult, graph
from matplotlib import pyplot as plt

driver = GraphDatabase.driver("bolt://localhost:11011", auth=("neo4j", "wwe1"))
session = driver.session()
list1 = []
list2 = []
x= {"regrex":"V.x*"}
q= '''MERGE (Natasha:Person {name:'Natasha'})
MERGE (Pierre:Person {name:'Pierre'})
MERGE (PrinceAndrew:Person {name:'PrinceAndrew'})
MERGE (Sonya:Person {name:'Sonya'})
MERGE (Napoleon:Person {name:'Napoleon'})
MERGE (Natasha)-[:STRONGEST]->(Pierre)
MERGE (Pierre)-[:STRONGEST]->(Natasha)
MERGE (product)-[:STRONGEST]->(Natasha)
MERGE (Pierre)-[:STRONGEST]->(Napoleon)
MERGE (Sonya)-[:STRONGEST]->(Napoleon)
MERGE (Natasha)-[:STRONGEST]->(Sonya)
MERGE (Pierre)-[:STRONGEST]->(PrinceAndrew)
MERGE (Sonya)-[:STRONGEST]->(PrinceAndrew)
MERGE (Natasha)-[:STRONGEST]->(PrinceAndrew)
MERGE (Napoleon)-[:STRONGEST]->(Napoleon)
MERGE (Napoleon)-[:STRONGEST]->(Sonya)'''
data1 =session.run(q,x)
e = '''CALL algo.pageRank.stream('Person', 'STRONGEST', {iterations:20, dampingFactor:0.85})
YIELD nodeId, score

RETURN algo.asNode(nodeId).name AS Person,score
ORDER BY score DESC'''
data = session.run(e,x)
for city in data:
    list1.append(city["Person"])
    list2.append(city["score"])
print(list1)
print(list2)
plt.xlabel("Persons")
plt.ylabel("PageRank")
plt.title('PageRank')
plt.bar(list1,list2)
plt.show()