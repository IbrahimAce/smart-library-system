# Smart Library System

A Python package for managing a library using OOP, dunder methods, decorators, closures, and duck typing.

## Setup
- Install: No external deps needed.
- Run demo: `python3 -m library_system`

## MRO Analysis
If we create a `DigitalBook` class that inherits from both `Book` (from this package) and a hypothetical `Software` class, Python uses the C3 Linearization algorithm for Method Resolution Order (MRO).

Assume:
- `class Software: pass`
- `class DigitalBook(Book, Software): pass`

C3 linearization merges the MROs of parents while preserving order:
1. Start with `DigitalBook`.
2. Merge MRO of `Book` (Book -> object) and MRO of `Software` (Software -> object).
3. Result: DigitalBook -> Book -> Software -> object.

To verify: `print(DigitalBook.__mro__)` would show `(<class '__main__.DigitalBook'>, <class '__main__.Book'>, <class '__main__.Software'>, <class 'object'>)`.

This ensures no diamond problem issues, as C3 maintains consistent order.

## Duck Typing
The `borrow_item(item)` method uses duck typing: It only requires the `item` to have a `.title` attribute at runtime, without explicit type checks.
