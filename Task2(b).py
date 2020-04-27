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
a = '''CREATE(Person: Person{name: 'Natsha',number: 6})'''
data=session.run(a,x)
b = '''CREATE(Person: Person{name: 'Pierre', number: 2})'''
data=session.run(b,x)
c = '''	CREATE(Person: Person{name: 'Na', number: 3})'''
data=session.run(c,x)
d = '''CREATE(Person: Person{name: 'Sonya', number: 4})'''
data=session.run(d,x)
e = '''CREATE(Person: Person{name: 'PrinceAndrew', number: 5})'''
data=session.run(e,x)
q = '''MATCH (a:Person),(b:Person)
WHERE a.number > b.number
CREATE (a)-[:STRONGEST]->(b)'''
data = session.run(q, x)