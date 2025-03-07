---
marp: true
theme: gaia
paginate: true
class:
  - lead
  - invert
header: 'Async Programming in Python'
footer: 'Satyam Soni | [![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/-satyamsoni/)'
---

<style>
section {
   font-size: 20px;
}
</style>

# Async Programming in Python

---

## What is Async Programming ?

Async programming is a programming paradigm that allows for the execution of tasks in a non-blocking manner. It allows program to execute tasks without blocking the main thread thus improving responsiveness.


___

## Preemptive MultiTasking vs Cooperative MultiTasking

**Preemptive MultiTasking:**
- In preemptive multitasking, the operating system decides when a context switch should occur, allowing the CPU to switch between tasks.
- It ensures that all tasks get CPU time, preventing any single task from monopolizing the CPU.
- This approach is commonly used in modern operating systems like Windows, Linux, and macOS.
- It can lead to more complex code due to the need for synchronization mechanisms to handle shared resources.

---

**Cooperative MultiTasking:**
- In cooperative multitasking, tasks voluntarily yield control of the CPU, allowing other tasks to run.
- Each task is responsible for giving up the CPU, which can lead to issues if a task fails to yield.
- It simplifies the design of the operating system but can lead to unresponsive systems if tasks do not cooperate properly.

In the context of async programming, cooperative multitasking is more relevant as it relies on tasks yielding control explicitly using constructs like `await` in Python.


___

### Caveats with Threading

- GIL prevents Python from leveraging Multiple Cores for Multithreading, thus all the threads run within context of single native thread unlike C#, Java. ( Each thread share same interpreter instance.)
- GIL has minumum effect on I/O bound operations, and thus allow context switching easily. (Python offloads I/O waits thus allowing other threads to use CPU time)
- Context switching amongst Threading is expensive, as OS is responsible to switch threads and allocate them with CPU time.
- Maintaining threads and synchronising between them requires expertise and can be messy.

---

## Why Async ?

- Simpler API.
- More Responsive.
- Better control over code.
- Handles most of the bottlenecks of concurrent programming - Race Conditions, Deadlocks etc. most of the times.
- Lets you focus on essential details offloading everything else to Event loop.


___

## Basic Components of Async Programming


1. **Coroutines**: Coroutines are special functions that can pause and resume their execution. They are defined using the `async def` syntax. They use the `await` keyword to yield control back to the event loop, allowing other tasks to run.

2. **Event Loop**: The event loop is the core of async programming. It manages the execution of tasks, handling their scheduling and switching between them. It runs continuously, checking for completed tasks and executing the next steps in the program.

3. **Tasks**: Tasks are used to schedule coroutines for execution. They are created using the `asyncio.create_task()` function. Tasks allow multiple coroutines to run concurrently, sharing the same event loop.

4. **Futures**: Futures represent a placeholder for a result that is initially unknown but will be available at some point. They are used to handle the results of asynchronous operations, allowing the program to continue executing while waiting for the result.

5. **Awaitables**: Awaitables are objects that can be used with the `await` keyword.

___

## Event Loop - Heart of Async Programming

---


### **Understanding the Event Loop:**

The event loop is the central component of asynchronous programming. It is responsible for managing and coordinating the execution of asynchronous tasks. Here's how it works:

- **Initialization**: The event loop is initialized and starts running, waiting for tasks to be added to its queue.
- **Task Scheduling**: Asynchronous tasks, such as coroutines, are scheduled to run on the event loop. These tasks are added to the event loop's queue.
- **Execution**: The event loop continuously checks for tasks that are ready to run. It executes these tasks, allowing them to perform their operations.
- **Task Switching**: When a task reaches a point where it needs to wait (e.g., for I/O operations), it yields control back to the event loop. The event loop then switches to another task that is ready to run.
- **Completion**: Once a task completes its execution, the event loop removes it from the queue and may handle any results or exceptions.

---

**Key Characteristics:**

- **Single-threaded**: The event loop runs in a single thread, which means it can only execute one task at a time. However, it can switch between tasks very quickly, giving the illusion of concurrency.
- **Non-blocking**: The event loop is designed to be non-blocking, meaning it does not wait for tasks to complete before moving on to the next one. This allows it to handle many tasks efficiently.
- **Efficient I/O Handling**: The event loop is particularly well-suited for I/O-bound tasks, such as network requests, where tasks spend a lot of time waiting for external resources.



---

## Async Program basic Structure

- Import Statements
- Coroutines
- Entry point

```python
import asyncio # import statement

async def foo(): # coroutine
    ...

asyncio.run(foo())
```

---

## Running Multiple Coroutines Concurrently

---

## Tasks & TaskGroups

In asynchronous programming, tasks are fundamental units of work that can be scheduled and executed by the event loop. TaskGroups, on the other hand, are a way to manage multiple tasks concurrently, allowing for better organization and error handling.

#### **Tasks:**

- **Creation**: Tasks are created from coroutines using the `asyncio.create_task()` function. This schedules the coroutine to be run on the event loop.
- **Execution**: Once created, tasks are executed by the event loop. They can be awaited to get their result or handle exceptions.
- **Lifecycle**: A task goes through several states: pending, running, and finished. The event loop manages these states.



---

## Async Looping and Context Manager

---

## Awaiting mechanisms

- **gather** - Excepts coroutines as arguments and wraps them to `Tasks` and schedules for execution.
- **wait** - Waits for iterable of `Tasks` to complete.
- **wait_for** - Wait for a Task to complete within given timeout.
- **await** - Can be used on any awaitable to yield execution to event loop

---

## Blocking Code vs Non Blocking Code

---
## Offloading blocking Code

---
## Futures

A Future represents an eventual result of an asynchronous operation. Not thread-safe.

Future is an awaitable object. Coroutines can await on Future objects until they either have a result or an exception set, or until they are cancelled. A Future can be awaited multiple times and the result is same..

---

## Synchronization Primitives

Synchronization primitives are tools used to manage access to shared resources in concurrent programming. Common types include:

- **Locks**: Ensure that only one coroutine accesses a resource at a time.
- **Events**: Allow coroutines to wait for a certain condition to be met.
- **Semaphores**: Control access to a resource by a set number of coroutines.
- **Conditions**: Enable coroutines to wait for certain conditions while releasing the lock temporarily.
- **Barriers**: Synchronize a fixed number of coroutines at a specific point in their execution.

---

## Key Things to remember

- Async is suitable for IO bound operations
- Avoid heavy uplifting, CPU bound tasks.
- Async is suitable with libraries supporting Async programming paradigm.

---

## QA
