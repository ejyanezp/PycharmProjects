from collections import defaultdict, OrderedDict, namedtuple, deque


def task1():
    my_dict = defaultdict(lambda: 'unkown')
    my_dict['Alan'] = 'Manchester'
    # print(my_dict['Ed'])
    return my_dict


def task2(arg_od: OrderedDict):
    arg_od.popitem()
    arg_od.popitem(False)
    # Con True (default) el item se mueve al extremo derecho
    arg_od.move_to_end('Bob')
    # Con False, el ítem se mueve al extremo izquierdo
    arg_od.move_to_end('Dan', False)


def task3(p_name: str, p_club: str):
    Player = namedtuple('Player', ['name', 'club'])
    player = Player(name=p_name, club=p_club)
    return player


def task4(arg_deque: deque):
    arg_deque.pop()
    elem = arg_deque.popleft()
    arg_deque.append(elem)
    arg_deque.appendleft('Zack')
    print(arg_deque)


print(task1())
d = {'Alan': 'Manchester', 'Bob': 'London', 'Chris': 'Lisbon',
     'Dan': 'Paris', 'Eden': 'Liverpool', 'Frank': 'newcastle'}
od = OrderedDict(d)
task2(od)
print(od)
ply = task3('Jose', 'Caracas')
print(ply)

my_deque = deque('ghijk')
print(my_deque)
task4(my_deque)
