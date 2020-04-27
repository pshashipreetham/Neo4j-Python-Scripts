
from neo4j import GraphDatabase, BoltStatementResult, graph
from matplotlib import pyplot as plt

driver = GraphDatabase.driver("bolt://localhost:11011", auth=("neo4j", "wwe1"))
session = driver.session()
f=open('/home/psp316r/Desktop/War and Peace.txt')
lines = f.readlines()
persons = list(lines[0].split("/"))
Paragraph = list(lines[1].split("/"))
print(Paragraph[0])

x= {"regrex":"V.x*"}
for tq in range(0,len(persons)):
    q = '''Create(Person:Person{})'''.format(persons[tq])
    data=session.run(q,x)
    print(q)
for tq in range(0,len(Paragraph)):
    q = '''Create(Paragraph:Paragraph{})'''.format(Paragraph[tq])
    data = session.run(q, x)
    print(q)
dict = (Paragraph[0].split(":"))[1].split("}")
for tq in range(0,len(persons)):
    f = '''MATCH (a:Person),(b:Paragraph)
WHERE a.name={} AND b.name= {}
CREATE (a)-[:CONTAINS ]->(b)'''.format((persons[tq].split(":"))[1].split("}")[0], (persons[tq].split(":"))[1].split("}")[0])
    data=session.run(f, x)