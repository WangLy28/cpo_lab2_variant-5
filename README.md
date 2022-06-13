# UNION - lab 2 - variant 5

Objectives:

- Design algorithms and data structures in immutable styles
- Usage of recursion
- Develop unit and property-based tests

- Design algorithms and data structures in immutable styles
- Usage of recursion
- Develop unit and property-based tests

## Project structure

- `hashmap.py` -- implementation of immutable`HMOpenAddressSet`class
   with`cons`,`length`,`remove`,`member`,`intersection`, `to_list`,
   `from_list`, `concat`, `Map`, `reduce`, `filter`, `Empty` features.

- `hashmap_test.py` -- unit and PBT tests for `hashmap`

## Features

- `length()` -- return the length of existing data.

- `cons(value,HMOSet)` -- add value to the HMOSet.

- `remove(HMOSet,value)` -- delete  value from HMOSet.

- `member(value,HMOSet)` -- check whether value is

  in HMOSet.

- `intersection(HMOSet1,HMOSet2)` -- return the intersection of HMOSet1 and HMOSet2.

- `to_list(HMOSet)` -- convert HMOSet to a list

- `from_list(lst)` -- build a hash map based on lst.

- `Map(lst,function,res)` -- map structure by specific function

- `filter(HMOSet)` -- filter HMOSet by specific predicate

- `Empty()` -- empty the hash map.

- `concat(HMOSet1,HMOSet2)` -- merge HMOSet1 and HMOSet2.

## Contribution

- Liao Pengfei (212320014@hdu.edu.cn)
- Wang Luyao(wlysbox@126.com)

## Changelog

- 09.06.2022
  - Add `hashmap.py`
  - Add `hashmap_test.py`
  - Add README.
- 13.06.2022
  - Add PBT test for monoid properties.
  - Update README.

## Design notes

- For mutable and immutable, I think the biggest difference is

  whether the initial variable changes. So for Mutability, I will

  add and remove elements from the Hash map built into the

  data structure of the Hash Map. For mutability, I define the

  two operations independently and accept the change using

  the variable new instead of the initial variable.

- For a Hash Map, I specify that the number of times it finds

  a space is 10, so the maximum allowed is 10 elements with

  the same Hash value. The growth factors for the Hash map

  can be set by yourself, but only if the Hash map is initialized,

  and then by default if more space is needed. My design is for

  positive numbers only.
