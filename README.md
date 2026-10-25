# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

## Reflection
Completing this assignment solidified my practical understanding of structural data management using sequential logic. By building custom classes around raw collections, I learned how to cleanly enforce structural integrity, translating abstract algorithmic behavior into explicit programmatic rules.
My primary roadblock was a standard reference typo during the real-world validation section, where an accidental comma instead of a dot syntax threw a Name Error. Stepping back to parse the interpreter's traceback log reminded me how critical precision is when handling instances, helping me quickly catch and swap the typo. Additionally, testing edge cases highlighted the necessity of defensive empty-check constraints to avoid sudden runtime index crashes.
In real-world applications, the difference between these two structures comes down to how you need to prioritize order. Queues are all about fairness and chronology through FIFO (First-In, First-Out). It’s the exact logic used for things like printer queues or customer support tickets, where whoever waits the longest gets served first. Stacks, however, rely on LIFO (Last-In, First-Out), making them perfect for chronological rollbacks.
