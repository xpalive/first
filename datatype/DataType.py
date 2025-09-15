from collections.abc import Hashable


def data_type():
    int = 1
    int2 = int
    int = 2
    str = 'name'
    tuple = ('name', 'age')
    list = ['name', 'age']
    dict = {'name': 'name', 'age': 'age'}
    print(f'{type(int)}, {is_immutable(int)} => {int2}')
    print(f'{type(str)}, {is_immutable(str)} => {str}')
    print(f'{type(tuple)}, {is_immutable(tuple)} => {tuple}')
    print(f'{type(list)}, {is_immutable(list)} => {list}')
    print(f'{type(dict)}, {is_immutable(dict)} => {dict}')

def is_immutable(obj):
    return isinstance(obj, Hashable)

if __name__ == "__main__":
    data_type()