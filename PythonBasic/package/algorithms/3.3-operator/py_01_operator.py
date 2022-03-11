"""
P183-P190, operator: Functional interface to built-in operation

! What?

The operator module defines functions thatcorrespond to 
the built-in arithmetic, comparison, and other operations for the standard object APIs.

! Why?

Programming using iterators occasionally requires creating small functions for simple expressions. 
Sometimes, these can be implemented as lambda functions, but for some operations new functions are not needed at all.

! How?

operator
|-- logical operations                          "逻"
|-- comparison operators                        "比"
|-- arithmetic operators                        "算"
|-- sequence operators                          "序"
|-- in-place operators                          "原地爆炸"
|-- attribute and item "Getters"                "拿"
|-- combining operators and custom classes      "组"

"""