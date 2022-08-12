import streamlit as st


st.title('10 Cool Beginner Python Tricks that Will Make Your Life Easier')

st.markdown('----')

st.markdown(
"""
# 1. The Walrus operator :tada:

**The Walrus** or _:=_ operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.
---

```python
Mylist = [1,2,3]
if(l := len(mylist) > 2)
print(l)
```
"""
)

st.markdown(
"""
```python
3
```
"""
)

st.markdown('----')

st.markdown(
"""
# 2. Splitting a string

If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!
---

```python
string = “hello world”
string.split()
```
"""
)

st.markdown(
"""
```python
[‘hello’, ‘world’]
```
"""
)

st.markdown('----')

st.markdown(
"""
# 3. Reversing a string

If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.
---

```python
str=”hello world!”
a=str[::-1]
print(a)
```
"""
)

st.markdown(
"""
```python
!dlrow olleh
```
"""
)

st.markdown('----')

st.markdown(
"""
# 4. Merging two dictionaries

This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary:
---

```python
d1 = {“a”: 10, “b”:20}
d2 = {“c”: 30, “d”:40}
d3 = {**d1, **d2}
print(d3)
```
"""
)

st.markdown(
"""
```python
{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}
```
"""
)

st.markdown('----')

st.markdown(
"""
# 5. The zip() function

The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.
---

```python
colour = [“red”, “yellow”, “green”]
fruits = [‘apple’, ‘banana’, ‘mango’]
for colour, fruits in zip(colour, fruits):
print(colour, fruits)
```
"""
)

st.markdown(
"""
```python
red apple
yellow banana
green mango
```
"""

)