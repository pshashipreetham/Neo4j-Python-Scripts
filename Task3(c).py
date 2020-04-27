import numpy as np
from neo4j import GraphDatabase, BoltStatementResult, graph
from matplotlib import pyplot as plt

driver = GraphDatabase.driver("bolt://localhost:11011", auth=("neo4j", "wwe1"))
session = driver.session()
x = np.arange(0, 50, 1)
# setting a style to use
plt.style.use('fivethirtyeight')

# create a figure
fig = plt.figure()

# define subplots and their positions in figure
plt1 = fig.add_subplot(221)
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)
plt4 = fig.add_subplot(224)
list_Paragraph = []
list_Mentions = []
listx1=[1]
listx2=[1]
listx3=[1]
listx4=[1]
listy1=[1]
listy2=[1]
listy3=[1]
listy4=[1]

x= {"regrex":"V.x*"}
ab = '''MATCH (n)
DETACH DELETE n'''
data=session.run(ab,x)
a = '''CREATE(Paragraph:Paragraph{name:'Natsha',number:26,mentions:12})'''
data=session.run(a,x)
b = '''			CREATE(Paragraph:Paragraph{name:'Pierre',number: 32,mentions:43})'''
data=session.run(b,x)
c = '''		CREATE(Paragraph:Paragraph{name:'Napolean',number: 33,mentions:22})'''
data=session.run(c,x)
d = '''		CREATE(Paragraph:Paragraph{name:'Sonya',number: 14,mentions:18})'''
data=session.run(d,x)
q = '''MATCH (n)    
    RETURN n.number, n.mentions   
    ORDER BY n.number'''
data=session.run(q,x)

plt.xlabel("Line Numbers")
plt.ylabel("Cumaltive Mentions")
plt.title('Pooja')
for city in data:
    print(city)
    list_Paragraph.append(city["n.number"])
    list_Mentions.append(city["n.mentions"])
print(list_Paragraph)
#plotting points on each subplot
listx1.append(list_Paragraph[0])
listy1.append(list_Mentions[0])
listx2.append(list_Paragraph[1])
listy2.append(list_Mentions[1])
listx3.append(list_Paragraph[2])
listy3.append(list_Mentions[2])
listx4.append(list_Paragraph[3])
listy4.append(list_Mentions[3])
#
plt1.plot(listx1, listy1, color='r')
plt1.set_title('Natasha')
#
#
plt2.plot(listx2, listy2, color='b')
plt2.set_title('Pierre')
#
#
plt3.plot(listx3, listy3, color='g')
plt3.set_title('Prince Andrew')
#
#
plt4.plot(listx4, listy4, color='k')
plt4.set_title('Naploleon')

# adjusting space between subplots
fig.subplots_adjust(hspace=.5, wspace=0.5)
plt.show()
driver.close()