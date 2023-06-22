'''
Question 1
In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions
will be mathematical operators.
*
'hello'
-87.8
-
/
+
6

'''

'''
Answer:

Values:  'hello' , -87.8, 6
Expressions: * - / +
'''

'''
Question 2:
What is the difference between string and variable?
'''

'''
Answer:

Variables: Variable is a name given to a data object to store its value in the memory.
String: String is one of the data types or objects, which represents a sequence of character or text data enclosed within
quotes

'''

name = "Jijina"
name = "Ranjith"

'''
In the above example, the string variable 'name' holds the value "Jijina", when the first assignment instruction is executed.
When the second assignment statement is executed, it creates a new string variable 'name' with value "Ranjith".
That means value of existing string variable cannot be changed ex. Jijina cannot be changed to Vijina by using operations
such as name[0]='V'. It replaces the entire string value by recreating the object itself.
'''
print(name)
'''
Question 3:
Describe three different data types.

'''

'''
Answer:

int: Data type to store value of integer. ex: 77
str: String Data type to store text data within double quotes "". ex: "77rocks"
float: Data type to store float values. ex: 7.777
list: Ordered collection of items. ex: fruits = [mango, apple, banana]. It is mutable and can hold heterogeneous data
tuples: Ordered collection of items. ex. fruits = (mango, apple, banana). It is immutable and hold heterogeneous data
dictionary: Unordered collection of key value pair {"name": "jijina", "age": 7}. Key is immutable and value is mutable
set: Unordered list of heterogeneous data where every element is unique. It does not allow dublicate items.
'''
