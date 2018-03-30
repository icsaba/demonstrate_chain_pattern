# Demonstrating chain and observer design pattern

The goal is to demonstrate the chain design patter. I implemented a simple stupid code.
It basically does nothing complicated, we have a Company object, and we wanna add staff.

I know this is a very dummy code, and you can write it in many different ways but i would like to show an example for
chain design pattern.

I have 5 different implementations based on my personal experience how I've been writing code since primary school.

## First code - kindergarden
It is a simple code for implementing a Company object. One simple file, that's all (spaghetti code)

## Second code - intern
Refactoring the code, creating methods, using tuples as return value.

## Thrid code - experienced intern
Refactoring the code, realising there are objects, and inheritance exists.

## Fourth code - real programmer
A real programmer realises that there are design patterns that could be useful during his/her career.
Final refactor step.

## Fifth code - sensei
Overkilled code base, extending the programmer code with the Observer design patter. It's a litle bit too much but seems to be a great fun. The purpose of the observer patter is that, we should recalculate the CEO and the partners' salary when a new employee is added.