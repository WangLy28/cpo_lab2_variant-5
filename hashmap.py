from typing import Callable, TypeVar, Any, Generic
import typing
import itertools

Value = TypeVar("Value", str, int, float, object, bool, list, Any)


class HMOpenAddressSet(Generic[Value]):
    def __init__(self,
                 lst: typing.List[typing.Any] = [],
                 factor: int = 1
                 ) -> None:
        '''initial function'''
        if len(lst) == 0:
            self.table: typing.List[typing.Any] = []
            self.set: typing.Set[typing.Any] = set([])
            self.factor = factor
        else:
            realset = []
            for value in lst:
                if value in realset:
                    continue
                realset.append(value)
            j = len(realset)
            self.table = [None] * j
            self.factor = factor
            for value in realset:
                if value is None:
                    continue
                else:
                    if value < 0:
                        index = (-value) % j
                    else:
                        index = value % j
                    i = j
                    while i != 0:
                        if self.table[index % j] is None:
                            self.table[index % j] = value
                            break
                        else:
                            index += 1
                            i -= 1
            self.set = set(self.table)

    def __eq__(self, other: 'HMOpenAddressSet') -> bool:
        if (len(self.table) == 0) and (len(other.table) > 0):
            return False
        if (len(self.table) > 0) and (len(other.table) == 0):
            return False
        for value in self.set:
            if value not in other.set:
                return False
        return True


def length(lst: typing.List[typing.Any]) -> int:
    '''size of HMOpenAddressSet'''
    if len(lst) == 0:
        return 0
    return 1 + length(lst[1:])


def cons(value: typing.Any, HMOSet: 'HMOpenAddressSet') -> 'HMOpenAddressSet':
    if value in HMOSet.set:
        return HMOSet
    if value is None:
        if None not in HMOSet.set:
            NewHMOSet = HMOpenAddressSet(HMOSet.table)
            NewHMOSet.table += [None]
            NewHMOSet.set = set(NewHMOSet.table)
        return NewHMOSet
    NewHMOSet = HMOpenAddressSet(HMOSet.table)
    NewHMOSet.table += [None]
    j = len(NewHMOSet.table)
    if value < 0:
        index = (-value) % j
    else:
        index = value % j
    i = j
    while i != 0:
        if NewHMOSet.table[index % j] is None:
            NewHMOSet.table[index % j] = value
            break
        else:
            index += 1
            i -= 1
    NewHMOSet.set = set(NewHMOSet.table)
    return NewHMOSet


def remove(HMOSet: 'HMOpenAddressSet', value: typing.Any) -> set:
    '''delete the value'''
    if value not in HMOSet.table:
        return HMOSet
    NewHMOSet = HMOpenAddressSet(HMOSet.table)
    temp = NewHMOSet.table.index(value)
    del NewHMOSet.table[temp]
    NewHMOSet.set = set(NewHMOSet.table)
    return NewHMOSet.set


def member(value: typing.Any, HMOSet: 'HMOpenAddressSet') -> bool:
    '''is member'''
    if value not in HMOSet.table:
        return False
    else:
        return True


def intersection(HMOSet1: 'HMOpenAddressSet',
                 HMOSet2: 'HMOpenAddressSet') -> 'HMOpenAddressSet':
    '''intersection'''
    lst = []
    if (len(HMOSet1.table) == 0) or (len(HMOSet2.table) == 0):
        return HMOpenAddressSet(lst)
    else:
        for value in HMOSet1.table:
            if value in HMOSet2.table:
                lst.append(value)
    return HMOpenAddressSet(lst)


def to_list(HMOSet: 'HMOpenAddressSet') -> typing.List[typing.Any]:
    '''return table '''
    return HMOSet.table


def from_list(lst: typing.List[typing.Any]) -> 'HMOpenAddressSet':
    '''return table '''
    if len(lst) == 0:
        return HMOpenAddressSet()
    return cons(lst[0], from_list(lst[1:]))


def concat(HMOSet1: 'HMOpenAddressSet',
           HMOSet2: 'HMOpenAddressSet') -> 'HMOpenAddressSet':
    '''concat of two sets'''
    if length(HMOSet2.table) == 0:
        return HMOSet1
    else:
        cap = len(HMOSet2.table)
        cur = 0
        NewHMOSet = HMOpenAddressSet(HMOSet1.table)
        while cur < cap:
            temp = HMOSet2.table[cur]
            if temp in HMOSet1.table:
                cur += 1
            else:
                NewHMOSet.table.append(temp)
                cur += 1
        NewHMOSet.set = set(NewHMOSet.table)
    return NewHMOSet


def Map(lst: typing.List[typing.Any],
        function: typing.Callable,
        res: typing.List[typing.Any] = []
        ) -> typing.List[typing.Any]:
    '''map value, the rule is defined by function'''
    if len(lst) == 0:
        return []
    return res + [function(lst[0])] + Map(lst[1:], function)


def reduce(lst: typing.List[typing.Any],
           function: typing.Callable) -> int:
    '''Reduce process elements and build a value by the function'''
    if len(lst) == 0:
        return 0
    if lst[0] == None:
        return 0
    return function(lst[0:1], reduce(lst[1:], function))


def filter(HMOSet: 'HMOpenAddressSet',
           function: typing.Callable) -> 'HMOpenAddressSet':
    '''filter set'''
    new_table: typing.List[typing.Any]
    new_table = []
    for value in HMOSet.table:
        if function(value) is True:
            if value not in new_table:
                new_table.append(value)
    NewHMOSet = HMOpenAddressSet(new_table)
    return NewHMOSet


def Empty(HMOSet: 'HMOpenAddressSet') -> 'HMOpenAddressSet':
    '''clear set'''
    NewHMOSet = HMOpenAddressSet([])
    return NewHMOSet
