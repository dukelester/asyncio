# Python Asyncio

Asyncio is a Python library that’s used to write concurrent code with `async` and `await` syntax. It’s used primarily in I/O-bound tasks, such as web page development or fetching data from APIs.

## CPU-Bound tasks VS I/O-bound task

A CPU-bound task spends most of its time doing heavy calculations with the CPUs. If you are a data scientist and need to crunch a huge amount of data to train machine learning models, then it’s a CPU-bound task. In this case, you should use multiprocessing to run your jobs in parallel and make full use of your CPUs.

An I/O-bound task spends most of its time waiting for I/O responses, which can be responses from web pages, databases or disks. If you’re developing a web page where a request needs to fetch data from APIs or databases, it’s an I/O-bound task. Concurrency can be achieved for I/O-bound tasks with either threading or asyncio to minimize the waiting time from external resources.


## Threading Vs Asyncio

First, threading uses multiple threads, whereas asyncio uses only one. Threading is easier to understand because the threads take turns to run the code and thus achieve concurrency. But how is it possible to achieve concurrency with a single thread?

Well, threading achieves concurrency with preemptive multitasking, which means we can’t determine when to run which code in which thread. It’s the operating system that determines which code should be run in which thread. The operating system can switch the control at any point between threads. This is why we often see random results with threading. 

On the other hand, asyncio achieves concurrency with cooperative multitasking. We decide which part of the code can be awaited, which then switches the control to run other parts of the code. The tasks need to cooperate and announce when the control will be switched out. And all this is done in a single thread with the await command. 

## What Is a Coroutine in Asyncio?

“Coroutines are a more generalized form of subroutines. Subroutines are entered at one point and exited at another point. Coroutines can be entered, exited, and resumed at many different points,”  according to Python documentation.
We can understand subroutines as functions, despite the differences between the two. Normally, a function is entered and exited only once when it’s called. However, there is a special function in Python called generator, which can be entered and exited many times.
Coroutines have become a native feature in Python now and can be defined with the new `async def` syntax. 