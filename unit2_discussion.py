"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        # Using a standard Python list. Appending and popping from the end
        # of a list occurs in 0(1) constant time, making it ideal for a stack.
        self._items= []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Appending to the end of the list places the element at the top of the stack.
        self._items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Handling an empty stack safely prevents IndexError crashes.
        # If empty, it returns None
        if self.is_empty():
            return None
        # remove and return the last item in the list (the top of the stack)
        return self._items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek checks the value at index -1 (the top/end of the stack)
        # without calling pop(), which keeps the stack state unchanged.
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        # Returns True if the list length is 0.
        return len(self._items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        # Using collections.deque because it is optimized for fast 0(1) pops
        # from the front and appends to the back.
        self._items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Appending to the right side adds the element to the back of the line.
        # This supports FIFO behavior because new items wait for their turn behind other items,
        # ensuring items are processed in the exact order the arrived.
        self._items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Handling an empty queue safely prevents an IndexError.
        # If the queue has items, popLeft() removes and returns the oldest item.
        if self.is_empty():
            return None
        return self._items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front returns the item at index 0 (the oldest element currently waiting in line)
        # without removing it, preserving the queue's state and order.
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        # Returns True if the deque contains no elements.
        return len(self._items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")

    # 1. Create a stack oject.
    my_stack = Stack()

    # 2. Add at least 4 values to the stack.
    print("Pushing actions to the stack: 'Open App', 'Click Link', 'Type Text', 'Upload Image'")
    my_stack.push('Open App')
    my_stack.push('Click Link')
    my_stack.push('Type Text')
    my_stack.push('Upload Image')


    # 3 & 4. Demonstrate LIFO behavior with descriptive print statements.
    print(f"Current top of stack (peek): {my_stack.peek()}")
    print(f"Popping last of stack (Undo): {my_stack.pop()}")
    print(f"Popping next action (Undo): {my_stack.pop()}")
    print(f"Notice that 'Upload Image' and 'Type Text' were removed first. This proves LIFO behavior.")

    # 5 & 6. Edge Cases: Pop and Peek on an empty stack.
    empty_stack = Stack()
    print("\n--- Testing Stack Edge Cases ---")
    print(f"Peeking at an empty stack returns: {empty_stack.peek()}")
    print(f"Popping from an empty stack returns: {empty_stack.pop()}")

    # 7. Single-item stack life cycle validation.
    single_stack = Stack()
    single_stack.push("Solitary Item")
    print(f"Created single-item stack. Is empty?: {single_stack.is_empty()}")
    print(f"Removed item: '{single_stack.pop()}'")
    print(f"Vertified: Is the single-item stack empty now? {single_stack.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.
    print("\n=== QUEUE DEMO ===")

    # 1. Create a Queue object.
    my_queue = Queue()

    # 2. Add at least 4 values to the queue.
    print("Enqueuing customer requests: 'Ticket #101', 'Ticket #102', 'Ticket #103', 'Ticket #104'")
    my_queue.enqueue('Ticket #101')
    my_queue.enqueue('Ticket #102')
    my_queue.enqueue('Ticket #103')
    my_queue.enqueue('Ticket #104')

    # 3 & 4. Demonstrate FIFO behavior with descriptive print statemetns.
    print(f"Current front of the queue: {my_queue.front()}")
    print(f"Processing (dequeue): {my_queue.dequeue()}")
    print(f"Processing (dequeue): {my_queue.dequeue()}")
    print("Notice that 'Ticket #101' and 'Ticket #102' were processed first. This proves FIFO behavior.")

    # 5 & 6. Edge Cases: Dequeue amd front on an empty queue.
    empty_queue = Queue()
    print(f"\n--- Testing Queue Edge Cases ---")
    print(f"Viewing front of an empty queue returns: {empty_queue.front()}")
    print(f"Dequeuing from an empty queue returns: {empty_queue.dequeue()}")

    # 7. Single-item queue life cycle validation.
    single_queue = Queue()
    single_queue.enqueue('Lone Customer')
    print(f"Created single-item queue. Is empty?: {single_queue.is_empty()}")
    print(f"Served customer:{single_queue.dequeue()}")
    print(f"Verified: Is the single-item queue empty now?: {single_queue.is_empty()}")

    # ===========================================================
    # REAL WORLD SCENARIO: CUSTOMER SUPPORT WITH UNDO HISTORY
    # ===========================================================

    print('\n=== REAL WORLD SCENARIO: HELP DESK SYSTEM ===')
    print("Scenario: Customer issues accrive chronologically (Queue).")
    print("As a technician resolves them, the revolved ticket is logged into a history log(stack)")
    print("so the technician can undo their last resolution if an error occurred. \n")

    incoming_tickets = Queue()
    resolution_history = Stack()
    # Tickets arrive
    incoming_tickets.enqueue("Reset Password for User 1")
    incoming_tickets.enqueue("Fix Network Drop in Room 23B")
    incoming_tickets.enqueue("Install Driver for Printer X")

    # Tech resolves the first ticket
    current_job = incoming_tickets.dequeue()
    print(f"[ACTION] Tech pulls job from queue: '{current_job}' ")
    print(f"[ACTION] Tech completes work and logs to history stack ")
    resolution_history.push(f"RESOLVED: {current_job}")

    # Tech resolves the second ticket
    current_job = incoming_tickets.dequeue()
    print(f"[ACTION] Tech pulls job from queue: '{current_job}' ")
    print(f"[ACTION] Tech completes work and logs to history stack ")
    resolution_history.push(f"RESOLVED: {current_job}")

    # Tech realizes they made a mistake on the network drop setup.
    print(f"\n[MISTAKE] Tech realizes the last modification was incorrect.")
    last_action = resolution_history.pop()
    print(f"[UNDO] Reversing from history stack: {last_action}'")
    print("The system has successfully rolled back the change using LIFO history.")


if __name__ == "__main__":
    main()
