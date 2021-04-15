graph1 = [
    ('dom', 'szkoła'), ('dom', 'bar'), ('dom', 'kościół'),
    ('szkoła', 'dom'), ('szkoła', 'szpital'),
    ('szpital', 'kino'), ('szpital', 'teatr'), ('szpital', 'szkoła'), ('szpital', 'bar'),
    ('teatr', 'szpital'), ('teatr', 'kino'),
    ('kino', 'teatr'), ('kino', 'szpital'), ('kino', 'kościół'),
    ('bar', 'kościół'), ('bar', 'szpital'), ('bar', 'dom'),
    ('kościół', 'dom'), ('kościół', 'kino'), ('kościół', 'bar')
         ]

graph = {
    'dom': ['szkoła', 'kościół', 'bar'],
    'szkoła': ['dom', 'szpital'],
    'szpital': ['kino', 'teatr', 'szkoła', 'bar'],
    'teatr': ['szpital', 'kino'],
    'kino': ['teatr', 'szpital', 'kościół'],
    'bar': ['kościół', 'szpital', 'dom'],
    'kościół': ['dom', 'kino', 'bar']

}


for item in graph:
    print('\n----> krawędzie z', item)
    for i in graph[item]:
        print(item, '----', i)


def print_graph():
    graph0 = [
        ('szkoła', 'kościół', 'bar'),
        ('dom', 'szpital'),
        ('kino', 'teatr', 'szkoła', 'bar'),
        ('szpital', 'kino'),
        ('teatr', 'szpital', 'kościół'),
        ('kościół', 'szpital', 'dom'),
        ('dom', 'kino', 'bar')
    ]
    for x in graph0:
        print('-'.join(x))

print_graph()