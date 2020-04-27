import tkinter as tk
from functools import partial
from neo4j import GraphDatabase, BoltStatementResult, graph
from matplotlib import pyplot as plt
driver = GraphDatabase.driver("bolt://localhost:11011", auth=("neo4j", "wwe1"))
session = driver.session()

def call_result(label_result, n1, n2):
    num1 = (n1.get())
    print(num1)
    list = []
    list1 = []
    count = 0
    x = {"regrex": "V.x*"}

    ab = '''MATCH (n)
    DETACH DELETE n'''
    data1 = session.run(ab, x)
    a = '''CREATE(a:Paragraph{number:4,mentions:12}),
    	(b:Paragraph{number: 12,mentions:23}),
    	(c:Paragraph{number: 16,mentions:32}),
    	(d:Paragraph{number: 17,mentions:42}),
    	(e:Paragraph{number: 21,mentions:44})'''
    data = session.run(a, x)
    q = '''MATCH (n)    
        RETURN n.mentions, n.number   
        ORDER BY n.number'''
    data = session.run(q, x)
    plt.xlabel("Line Numbers")
    plt.ylabel("Cumaltive Mentions")
    plt.title(num1)
    for city in data:
        list.append(city["n.mentions"])
        list1.append(city["n.number"])

    print(list)
    print(list1)
    plt.plot(list, list1)
    plt.show()
    driver.close()

    return


root = tk.Tk()
root.geometry('400x200+100+200')

root.title('Task 5 Using Widget')

number1 = tk.StringVar()
number2 = tk.StringVar()


labelNum1 = tk.Label(root, text="Name").grid(row=1, column=0)


labelResult = tk.Label(root)

labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)

call_result = partial(call_result, labelResult, number1, number2)

buttonCal = tk.Button(root, text="Submit", command=call_result).grid(row=3, column=0)

root.mainloop()