from neo4j import GraphDatabase, BoltStatementResult, graph
from matplotlib import pyplot as plt

driver = GraphDatabase.driver("bolt://localhost:11011", auth=("neo4j", "wwe1"))
session = driver.session()
list = []
list1 = []
list2 = []
list3 = []
count =0
x= {"regrex":"V.x*"}
a = '''CREATE(f:Paragraph{number:4,mentions:12}),
	(g:Paragraph{number: 12,mentions:23}),
	(h:Paragraph{number: 16,mentions:32}),
	(j:Paragraph{number: 17,mentions:42}),
	(k:Paragraph{number: 21,mentions:44})'''
data = session.run(a, x)
q = '''MATCH (n)    
        RETURN n.mentions, n.number   
        ORDER BY n.number'''
data = session.run(q, x)

plt.xlabel("Line Numbers")
plt.ylabel("Cumaltive Mentions")
plt.title('Sonya and Natasha')
for city in data:
    list.append(city["n.number"])
    list1.append(city["n.mentions"])
a = '''CREATE(a:Paragraph{number:2,mentions1:6}),
    	(b:Paragraph{number1: 15,mentions1:14}),
    	(c:Paragraph{number1: 21,mentions1:24}),
    	(d:Paragraph{number1: 25,mentions1:32}),
    	(e:Paragraph{number1: 32,mentions1:40})'''
data = session.run(a, x)
q = '''MATCH (n)    
        RETURN n.mentions1, n.number1   
        ORDER BY n.number1'''
data = session.run(q, x)
for city in data:
    list2.append(city["n.number1"])
    list3.append(city["n.mentions1"])
plt.plot(list,list1,label = "Sonya")
plt.plot(list2,list3,label = "Natasha")
plt.legend()
plt.show()
driver.close()


