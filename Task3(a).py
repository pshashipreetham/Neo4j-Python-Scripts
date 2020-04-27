from neo4j import GraphDatabase, BoltStatementResult, graph
from matplotlib import pyplot as plt

driver = GraphDatabase.driver("bolt://localhost:11011", auth=("neo4j", "wwe1"))
session = driver.session()
list = []
list1 = []
count =0
x= {"regrex":"V.x*"}

ab = '''MATCH (n)
DETACH DELETE n'''
data1=session.run(ab,x)
a = '''CREATE(a:Paragraph{number:4,mentions:12}),
	(b:Paragraph{number: 12,mentions:23}),
	(c:Paragraph{number: 16,mentions:32}),
	(d:Paragraph{number: 17,mentions:42}),
	(e:Paragraph{number: 21,mentions:44})'''
data=session.run(a,x)
q = '''MATCH (n)    
    RETURN n.mentions, n.number   
    ORDER BY n.number'''
data=session.run(q,x)
plt.xlabel("Line Numbers")
plt.ylabel("Cumaltive Mentions")
plt.title('Sonya')
for city in data:
    list.append(city["n.mentions"])
    list1.append(city["n.number"])

print(list)
print(list1)
plt.plot(list,list1)
plt.show()
driver.close()


