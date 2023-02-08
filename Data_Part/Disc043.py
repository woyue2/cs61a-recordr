"""
2 Data Abstraction

Data abstraction is a powerful concept in computer science that allows programmers to 
treat code as objects. That way, programmers don’t have to
worry about how code is implemented — they just have to know what it
does.

Data abstraction mimics how we think about the world. For example, when
you want to drive a car, you don’t need to know how the engine was built
or what kind of material the tires are made of. You just have to know how
to turn the wheel and press the gas pedal.

Data abstraction is useful when dealing with compound values, or values
that consist of more than one component. An example of such a value is a
rational number, or a number than can be written as x / y, which consists
of a numerator and a denominator.

We can represent these types of values as abstract data types (ADTs).
An abstract data type consists of two types of functions:
• Constructors: functions that build the abstract data type.
• Selectors: functions that retrieve information from the data type.

<In fact, you should never assume anything about how the constructors and
selectors for an abstract data type are implemented. Doing so is called a
data abstraction violation.>KEY SENTENCE

As an example, here is one implemenation for the rational constructor.
def rational(n, d):
    return [n, d]

Given this constructor, the following would be considered a data abstraction
violation:
>>> frac1 = rational(3, 4)
>>> frac2 = rational(5, 6)
>>> frac1[0] * frac2[0]
15
"""
#Question
"""
The TAs have decided to reveal the implementation of the discussion section
ADT. Use these function definitions to answer the next two questions:"""
def make_discussion(ta, time, students):
    return [name, time, students]

def get_ta(disc):
    return disc[0]

def get_time(disc):
    return disc[1]

def get_students(disc):
    return disc[2]
#不想做了，基本了解了，就是用list做construct，用index做select