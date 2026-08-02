# Day 13 Notes

## 1. Lambda Function

A lambda function is a small anonymous function.

Syntax

```python
lambda arguments : expression
```

Example

```python
square = lambda x: x*x
print(square(5))
```

Output

```
25
```

Time Complexity

O(1)

---

## 2. map()

Applies one function to every item.

Example

```python
numbers=[1,2,3]

square=list(map(lambda x:x*x,numbers))
```

Output

```
[1,4,9]
```

Time Complexity

O(n)

---

## 3. filter()

Filters data based on condition.

Example

```python
numbers=[1,2,3,4]

even=list(filter(lambda x:x%2==0,numbers))
```

Output

```
[2,4]
```

Time Complexity

O(n)

---

## 4. reduce()

Combines all values into one value.

Import

```python
from functools import reduce
```

Example

```python
numbers=[1,2,3]

total=reduce(lambda x,y:x+y,numbers)
```

Output

```
6
```

Time Complexity

O(n)

---

## 5. List Comprehension

Short way of creating lists.

Example

```python
square=[i*i for i in range(5)]
```

Output

```
[0,1,4,9,16]
```

Time Complexity

O(n)
