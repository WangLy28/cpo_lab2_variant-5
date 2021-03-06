import unittest
from hashmap import HMOpenAddressSet, length, cons, remove, member, \
    intersection, to_list, from_list, concat, Map, reduce, filter, Empty
from hypothesis import given
import hypothesis.strategies as st
import itertools


class TestHMOpenAddressSet(unittest.TestCase):
    def test_api(self):
        empty = HMOpenAddressSet()
        self.assertEqual(str(cons(None, empty).set), "{None}")
        l1 = cons(None, cons(1, empty))
        l2 = cons(1, cons(None, empty))
        self.assertEqual(str(empty.set), str(set([])))
        self.assertTrue(str(l1.set) == "{None, 1}"
                        or str(l1.set) == "{1, None}")
        self.assertNotEqual(empty, l1)
        self.assertNotEqual(empty, l2)
        self.assertEqual(l1, l2)
        self.assertEqual(l1, cons(None, cons(1, l1)))
        self.assertEqual(length(empty.table), 0)
        self.assertEqual(length(l1.table), 2)
        self.assertEqual(length(l2.table), 2)
        self.assertEqual(str(remove(l1, None)), "{1}")
        self.assertEqual(str(remove(l1, 1)), "{None}")
        self.assertFalse(member(None, empty))
        self.assertTrue(member(None, l1))
        self.assertTrue(member(1, l1))
        self.assertFalse(member(2, l1))
        self.assertEqual(intersection(l1, l2), l1)
        self.assertEqual(intersection(l1, l2), l2)
        self.assertEqual(intersection(l1, empty), empty)
        self.assertEqual(intersection(
            l1, cons(None, empty)), cons(None, empty))
        self.assertTrue(to_list(l1) == [None, 1] or to_list(l1) == [1, None])
        self.assertEqual(l1, from_list([None, 1]))
        self.assertEqual(l1, from_list([1, None, 1]))
        self.assertEqual(concat(l1, l2), from_list([None, 1, 1, None]))
        buf = []
        for e in l1.set:
            buf.append(e)
        self.assertIn(buf, map(list, itertools.permutations([1, None])))
        lst = to_list(l1) + to_list(l2)
        for e in l1.set:
            lst.remove(e)
        for e in l2.set:
            lst.remove(e)
        self.assertEqual(lst, [])

    def test_filter(self) -> None:
        '''test filter'''

        def is_even(data) -> bool:
            if data % 2 == 0:
                return True
            else:
                return False

        self.assertIn(filter(HMOpenAddressSet([0, 1, 2]), is_even).set,
                      [{0, 2}, {2, 0}])

    def test_Map(self) -> None:
        '''test Map'''
        empty = HMOpenAddressSet()
        self.assertIn(Map(cons(None, cons(1, empty)).table, str),
                      [['None', '1'], ['1', 'None']])

    def test_reduce(self) -> None:
        '''test reduce'''
        empty = HMOpenAddressSet()
        self.assertEqual(reduce(cons(None, cons(1, empty)).table, sum), 1)
        self.assertEqual(reduce(HMOpenAddressSet([0, 1, 2]).table, sum), 3)

    def test_Empty(self) -> None:
        '''test Empty'''
        empty = HMOpenAddressSet()
        self.assertEqual(Empty(cons(None, cons(1, empty))), empty)

    @given(st.lists(st.integers()))
    def test_length(self, a) -> None:
        a = to_list(HMOpenAddressSet(a))
        b = from_list(a)
        self.assertEqual(length(b.table), len(a))

    @given(a=st.integers(), b=st.integers(), c=st.integers())
    def test_monoid(self, a, b, c) -> None:
        testset = from_list([a, b, c])
        self.assertEqual(concat(HMOpenAddressSet(), testset), testset)
        self.assertEqual(concat(testset, HMOpenAddressSet()), testset)
        self.assertEqual(intersection(HMOpenAddressSet(), testset).table, [])
        self.assertEqual(intersection(testset, HMOpenAddressSet()).table, [])

    @given(a=st.integers(), b=st.integers(), c=st.integers())
    def test_immutability_check(self, a, b, c):
        if a == 0:
            a = a + 2
        if b == 0:
            b = b + 4
        if c == 0:
            c = c + 8
        if a == b:
            a = a * 2
        if b == c:
            c = c * 4
        if a == c:
            c = c * 8
        testset = HMOpenAddressSet([a, b])
        test1 = cons(c, testset)
        self.assertNotEqual(test1, testset)
        test2 = remove(testset, b)
        self.assertNotEqual(test2, test1.set)
        test3 = Empty(test2)
        self.assertNotEqual(test3.set, test2)
        test4 = concat(test3, HMOpenAddressSet([b]))
        self.assertNotEqual(test4, test3)

        def add(d):
            return d * 2

        test5 = Map(testset.table, add)
        self.assertNotEqual(test5, testset.table)


if __name__ == '__main__':
    unittest.main()
