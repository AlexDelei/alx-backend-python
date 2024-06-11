### Async IO in python

[Real Python](https://realpython.com/async-io-python/) - This tutorial is focused on the subcomponent that is async IO, how to use it, and the APIs that have sprung up around it.

[Python docs - asyncio documentation](https://docs.python.org/3/library/asyncio.html) - asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

#### Objectives to be met while learning asyncio in python
- async and await syntax ✔︎
- How to execute an async program with asyncio. ✔︎
- How to run concurrent coroutines.
- How to create asyncio tasks.
- How to use the random module.


## The Rules of Async IO
<br>
- The syntax async def introduces either a native coroutine or an asynchronous generator.
- The keyword await passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) If Python encounters an await f() expression in the scope of g(), this is how await tells the event loop, “Suspend execution of g() until whatever I’m waiting on—the result of f()is returned. In the meantime, go let something else run.”

```
async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r
```
<br>
There’s also a strict set of rules around when and how you can and cannot use async/await. These can be handy whether you are still picking up the syntax or already have exposure to using async/await:

- A function that you introduce with async def is a coroutine. It may use await, return, or yield, but all of these are optional. Declaring async def noop(): pass is valid:
  - Using await and/or return creates a coroutine function. To call a coroutine function, you must await it to get its results.