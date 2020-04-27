from neo4j import GraphDatabase, BoltStatementResult, graph
from matplotlib import pyplot as plt

list1 = []
list2 = []
driver = GraphDatabase.driver("bolt://localhost:11011", auth=("neo4j", "wwe1"))
session = driver.session()
x = {"regrex": "V.x*"}
ab = '''MATCH (n)
DETACH DELETE n'''
data1=session.run(ab,x)
a = '''CREATE(Paragraph:Paragraph{name1:'Pierre',name2:'Natsha'}),(Person:Person{name:'Natsha'})'''
data=session.run(a,x)
a = '''CREATE(Person:Person{name:'Pierre'})'''
data=session.run(a,x)
q = '''MATCH (n)

RETURN n.name1, n.name2'''
data = session.run(q, x)
length = 0
for city in data:
    list1.append(city["n.name1"])
    list2.append(city["n.name2"])
print(list1)
print(list2)

for len in range(len(list2)):
    print("length= ", len)
    if list2[len] is None:
        length = len - 1
        break
if length != 0:
    for tq in range(length):
        q = '''MATCH (a:Person),(b:Person)
WHERE a.name='Pierre' AND b.name='Natsha'
CREATE (a)-[:Co_MENTIONED_WITH]->(b)'''.format(list1[tq], list2[tq])
        data = session.run(q, x)
else:
    q = '''MATCH (a:Person),(b:Person)
    WHERE a.name='{}' AND b.name='{}'
    CREATE (a)-[:Co_MENTIONED_WITH]->(b)'''.format(list1[length], list2[length])
    data = session.run(q, x)
print(length)
