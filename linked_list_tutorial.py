"""
=====================================================================
 COMPLETE LINKED LIST TUTORIAL IN PYTHON
=====================================================================
A linked list is a chain of "nodes". Each node stores:
   1) data  -> the actual value
   2) next  -> a reference (pointer) to the NEXT node in the chain

The list itself only needs to remember the FIRST node, called "head".
From head, you can walk (traverse) node.next -> node.next -> ... 
until you hit None, which marks the end of the list.

Why use it instead of a Python list?
   - Inserting/deleting at the BEGINNING is O(1) (no shifting needed)
   - Size can grow/shrink without reallocating a big array
   - Downside: no random access (no list[i]); must walk from head

Run this file top to bottom: `python linked_list_tutorial.py`
Every section prints its own output so you can see it work.
=====================================================================
"""

# =====================================================================
# 1) CREATE A NODE
# =====================================================================
class Node:
    """A single link in the chain."""

    def __init__(self, data):
        self.data = data   # store the value passed in (e.g. 10)
        self.next = None   # no connection yet -> this node points to
                            # "nothing" until we link it manually

# Let's create ONE node and inspect it, line by line:
n = Node(10)        # __init__ runs: n.data = 10, n.next = None
print("Single node data:", n.data)   # -> 10
print("Single node next:", n.next)   # -> None (not linked to anything yet)


# =====================================================================
# 2) CREATE 5 NODES
# =====================================================================
# We simply call the Node() constructor 5 times.
# Right now these 5 nodes are FLOATING/INDEPENDENT - none point to
# each other yet. That's the next step (Connect nodes).
node1 = Node(10)   # node1.data = 10, node1.next = None
node2 = Node(20)   # node2.data = 20, node2.next = None
node3 = Node(30)   # node3.data = 30, node3.next = None
node4 = Node(40)   # node4.data = 40, node4.next = None
node5 = Node(50)   # node5.data = 50, node5.next = None

print("\n5 nodes created (not linked yet):")
for temp_node in (node1, node2, node3, node4, node5):
    print(f"  data={temp_node.data}, next={temp_node.next}")


# =====================================================================
# 3) CONNECT NODES  (manually, to understand the mechanism)
# =====================================================================
# "Connecting" simply means: set nodeA.next = nodeB
# This makes nodeA point to nodeB, forming a chain.
node1.next = node2   # node1 -> node2   (node1's arrow now points to node2)
node2.next = node3   # node2 -> node3
node3.next = node4   # node3 -> node4
node4.next = node5   # node4 -> node5
# node5.next is still None -> node5 is the LAST node (the "tail")

# The chain now looks like:
#   node1(10) -> node2(20) -> node3(30) -> node4(40) -> node5(50) -> None
head = node1   # "head" is our entry point into the list; we only need
               # to remember this ONE variable to access the whole chain

print("\nManually connected chain, walked from head:")
current = head                 # start walking at head
while current is not None:     # keep going until we fall off the end
    print(f"  {current.data}", end=" -> " if current.next else " -> None\n")
    current = current.next     # move to the next node


# =====================================================================
# Now we wrap all of this into a reusable LinkedList CLASS so we don't
# have to manually wire nodes every time. Below, every method is
# explained line-by-line in its own comments.
# =====================================================================

class LinkedList:
    def __init__(self):
        self.head = None   # empty list -> no nodes yet

    # -----------------------------------------------------------------
    # DISPLAY LIST
    # -----------------------------------------------------------------
    def display(self):
        """Walk from head to end, printing each node's data."""
        current = self.head        # start at the first node
        values = []                # collect values to print nicely
        while current:              # loop runs while current is not None
            values.append(str(current.data))  # record this node's data
            current = current.next  # step forward to the next node
        print(" -> ".join(values) + " -> None" if values else "Empty list")

    # -----------------------------------------------------------------
    # COUNT NODES
    # -----------------------------------------------------------------
    def count_nodes(self):
        count = 0                  # start counting from 0
        current = self.head        # begin at head
        while current:              # visit every node once
            count += 1              # one more node found
            current = current.next  # move forward
        return count                # total nodes visited

    # -----------------------------------------------------------------
    # SUM OF NODES
    # -----------------------------------------------------------------
    def sum_nodes(self):
        total = 0                  # accumulator starts at 0
        current = self.head
        while current:
            total += current.data   # add this node's value to total
            current = current.next
        return total

    # -----------------------------------------------------------------
    # FIND MAXIMUM
    # -----------------------------------------------------------------
    def find_max(self):
        if self.head is None:       # guard: empty list has no max
            return None
        max_val = self.head.data    # assume first node is max so far
        current = self.head.next    # start comparing from 2nd node
        while current:
            if current.data > max_val:  # found a bigger value
                max_val = current.data  # update our running max
            current = current.next
        return max_val

    # -----------------------------------------------------------------
    # FIND MINIMUM
    # -----------------------------------------------------------------
    def find_min(self):
        if self.head is None:
            return None
        min_val = self.head.data    # assume first node is min so far
        current = self.head.next
        while current:
            if current.data < min_val:  # found a smaller value
                min_val = current.data
            current = current.next
        return min_val

    # -----------------------------------------------------------------
    # SEARCH ELEMENT
    # -----------------------------------------------------------------
    def search(self, target):
        current = self.head
        position = 0                 # track index of current node
        while current:
            if current.data == target:   # match found!
                return position           # return index where found
            current = current.next
            position += 1
        return -1                    # loop finished, never matched

    # -----------------------------------------------------------------
    # UPDATE VALUE (change data at a given index)
    # -----------------------------------------------------------------
    def update_value(self, index, new_value):
        current = self.head
        pos = 0
        while current:
            if pos == index:              # reached the target index
                current.data = new_value  # overwrite its data
                return True
            current = current.next
            pos += 1
        return False                  # index was out of range

    # -----------------------------------------------------------------
    # INSERT AT BEGINNING
    # -----------------------------------------------------------------
    def insert_beginning(self, data):
        new_node = Node(data)       # create the new node (next=None)
        new_node.next = self.head   # new node points to OLD head
        self.head = new_node        # list's head is now the new node
        # Order matters! We must link new_node.next BEFORE reassigning
        # self.head, otherwise we'd lose the reference to the old chain.

    # -----------------------------------------------------------------
    # INSERT AT END
    # -----------------------------------------------------------------
    def insert_end(self, data):
        new_node = Node(data)       # new node, next=None (it'll be last)
        if self.head is None:       # special case: list was empty
            self.head = new_node    # new node becomes the only node
            return
        current = self.head
        while current.next:         # walk until current is the LAST node
            current = current.next  # (current.next is None -> stop)
        current.next = new_node     # attach new node after the last one

    # -----------------------------------------------------------------
    # INSERT AT POSITION (0-indexed)
    # -----------------------------------------------------------------
    def insert_position(self, index, data):
        if index == 0:               # inserting at front = insert_beginning
            self.insert_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        pos = 0
        while current and pos < index - 1:  # stop at node BEFORE target index
            current = current.next
            pos += 1
        if current is None:          # index was beyond the list length
            print("Position out of range")
            return
        new_node.next = current.next  # new node points to what follows
        current.next = new_node       # previous node points to new node
        # Sequence matters here too: set new_node.next FIRST so we don't
        # lose the reference to the rest of the chain.

    # -----------------------------------------------------------------
    # DELETE AT BEGINNING
    # -----------------------------------------------------------------
    def delete_beginning(self):
        if self.head is None:        # nothing to delete
            print("List is empty")
            return
        self.head = self.head.next   # head jumps to 2nd node;
        # the old first node has no more references pointing to it,
        # so Python's garbage collector will clean it up automatically.

    # -----------------------------------------------------------------
    # DELETE AT END
    # -----------------------------------------------------------------
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:   # only ONE node in the list
            self.head = None         # list becomes empty
            return
        current = self.head
        while current.next.next:     # stop when current is SECOND-LAST node
            current = current.next
        current.next = None          # cut the link to the last node

    # -----------------------------------------------------------------
    # DELETE AT POSITION (0-indexed)
    # -----------------------------------------------------------------
    def delete_position(self, index):
        if self.head is None:
            print("List is empty")
            return
        if index == 0:                # deleting first node
            self.delete_beginning()
            return
        current = self.head
        pos = 0
        while current and pos < index - 1:  # stop at node BEFORE target
            current = current.next
            pos += 1
        if current is None or current.next is None:  # index invalid
            print("Position out of range")
            return
        current.next = current.next.next   # skip over the target node,
        # linking directly to the node AFTER it — this "removes" it
        # from the chain (no one points to it anymore)

    # -----------------------------------------------------------------
    # REVERSE THE LIST
    # -----------------------------------------------------------------
    def reverse(self):
        prev = None            # will become the new "next" for each node
        current = self.head    # start walking from the original head
        while current:
            next_node = current.next  # save the next node BEFORE we
                                       # overwrite current.next below
            current.next = prev       # flip the arrow: point backwards
            prev = current             # move prev forward to current
            current = next_node        # move current forward (using saved ref)
        self.head = prev        # after loop, prev is the new first node
        # Visualize with 1->2->3->None:
        #  step1: None<-1   2->3->None   (current=2, prev=1)
        #  step2: None<-1<-2  3->None    (current=3, prev=2)
        #  step3: None<-1<-2<-3          (current=None, prev=3)
        #  loop ends -> self.head = 3    -> list is now 3->2->1->None

    # -----------------------------------------------------------------
    # FIND MIDDLE NODE (slow & fast pointer / "tortoise and hare")
    # -----------------------------------------------------------------
    def find_middle(self):
        if self.head is None:
            return None
        slow = self.head       # moves 1 step at a time
        fast = self.head       # moves 2 steps at a time
        while fast and fast.next:
            slow = slow.next          # advance slow by 1
            fast = fast.next.next     # advance fast by 2
        # When fast reaches the end, slow has covered half the distance,
        # so slow is sitting on the middle node.
        return slow.data

    # -----------------------------------------------------------------
    # FIND LAST NODE
    # -----------------------------------------------------------------
    def find_last_node(self):
        if self.head is None:
            return None
        current = self.head
        while current.next:     # keep going until next is None
            current = current.next
        return current.data     # current is now the last node

    # -----------------------------------------------------------------
    # FIND Nth NODE (0-indexed)
    # -----------------------------------------------------------------
    def find_nth_node(self, n):
        current = self.head
        pos = 0
        while current:
            if pos == n:             # reached the requested index
                return current.data
            current = current.next
            pos += 1
        return None                  # n was out of range


# =====================================================================
# DEMO: exercising every LinkedList method above
# =====================================================================
print("\n" + "=" * 60)
print("LINKED LIST CLASS DEMO")
print("=" * 60)

ll = LinkedList()                       # ll.head = None (empty list)
for value in (10, 20, 30, 40, 50):      # build 10->20->30->40->50
    ll.insert_end(value)                # each call walks to the tail
                                         # and attaches a new node there

print("Display:            ", end=""); ll.display()
print("Count nodes:         ", ll.count_nodes())
print("Sum of nodes:        ", ll.sum_nodes())
print("Maximum:             ", ll.find_max())
print("Minimum:             ", ll.find_min())
print("Search 30 (index):   ", ll.search(30))
print("Search 99 (index):   ", ll.search(99))   # -1, not found

ll.update_value(2, 300)                 # change index 2 (value 30) to 300
print("After update index2: ", end=""); ll.display()

ll.insert_beginning(5)                  # 5->10->20->300->40->50
print("After insert_begin:  ", end=""); ll.display()

ll.insert_end(60)                       # ...->50->60
print("After insert_end:    ", end=""); ll.display()

ll.insert_position(3, 999)              # insert 999 at index 3
print("After insert_pos(3): ", end=""); ll.display()

ll.delete_beginning()                   # remove the 5 we added
print("After delete_begin:  ", end=""); ll.display()

ll.delete_end()                         # remove the 60 we added
print("After delete_end:    ", end=""); ll.display()

ll.delete_position(3)                   # remove the 999 we inserted
print("After delete_pos(3): ", end=""); ll.display()

print("Middle node:         ", ll.find_middle())
print("Last node:           ", ll.find_last_node())
print("Node at index 2:     ", ll.find_nth_node(2))

ll.reverse()
print("After reverse:       ", end=""); ll.display()


# =====================================================================
# DOUBLY CIRCULAR LINKED LIST
# =====================================================================
# Differences from a singly linked list:
#   - Each node has TWO pointers: `next` AND `prev` (previous)
#     -> lets you walk backwards as well as forwards
#   - It's CIRCULAR: the last node's `next` points back to the head,
#     and the head's `prev` points to the last node (the "tail")
#     -> there is no None at the end; the ring never "stops"
#
# This structure is used e.g. in music-player "playlist loops",
# undo/redo history with both-direction browsing, etc.

class DNode:
    """A node for a doubly linked list: knows both neighbors."""

    def __init__(self, data):
        self.data = data   # the value stored
        self.next = None   # pointer to the NEXT node
        self.prev = None   # pointer to the PREVIOUS node


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None   # empty ring -> no nodes

    # -----------------------------------------------------------------
    # INSERT AT END (building the ring)
    # -----------------------------------------------------------------
    def insert_end(self, data):
        new_node = DNode(data)
        if self.head is None:               # ring is currently empty
            self.head = new_node            # this node is the only one
            new_node.next = new_node        # it points to ITSELF (next)
            new_node.prev = new_node        # and to itself (prev) too
            return
        tail = self.head.prev               # head.prev is ALWAYS the
                                             # current last node (that's
                                             # the trick of circularity)
        tail.next = new_node                # old tail -> new node
        new_node.prev = tail                # new node <- old tail
        new_node.next = self.head           # new node -> head (wrap around)
        self.head.prev = new_node           # head <- new node (wrap around)

    # -----------------------------------------------------------------
    # INSERT AT BEGINNING
    # -----------------------------------------------------------------
    def insert_beginning(self, data):
        self.insert_end(data)      # first, add it as the new LAST node
        self.head = self.head.prev # head.prev is always the tail, and the
        # node we just added IS the new tail -> shifting head to it makes
        # our new node the FIRST node, while the ring order stays intact
        # (old head is now correctly positioned right after it)

    # -----------------------------------------------------------------
    # DELETE A NODE BY VALUE
    # -----------------------------------------------------------------
    def delete_value(self, target):
        if self.head is None:
            print("Ring is empty")
            return
        current = self.head
        while True:
            if current.data == target:      # found the node to remove
                if current.next == current:  # it's the ONLY node in ring
                    self.head = None
                    return
                current.prev.next = current.next  # bypass current forward
                current.next.prev = current.prev  # bypass current backward
                if current == self.head:          # if we removed head,
                    self.head = current.next       # head moves forward
                return
            current = current.next
            if current == self.head:        # walked all the way around
                print("Value not found")
                return

    # -----------------------------------------------------------------
    # DISPLAY FORWARD (one full loop)
    # -----------------------------------------------------------------
    def display_forward(self):
        if self.head is None:
            print("Empty ring")
            return
        current = self.head
        values = []
        while True:
            values.append(str(current.data))
            current = current.next          # move forward
            if current == self.head:        # completed the loop
                break
        print(" <-> ".join(values) + "  (back to " + values[0] + ")")

    # -----------------------------------------------------------------
    # DISPLAY BACKWARD (one full loop, using prev pointers)
    # -----------------------------------------------------------------
    def display_backward(self):
        if self.head is None:
            print("Empty ring")
            return
        tail = self.head.prev               # last node = head.prev
        current = tail
        values = []
        while True:
            values.append(str(current.data))
            current = current.prev          # move backward
            if current == tail:             # completed the loop
                break
        print(" <-> ".join(values) + "  (back to " + values[0] + ")")


print("\n" + "=" * 60)
print("DOUBLY CIRCULAR LINKED LIST DEMO")
print("=" * 60)

dcll = DoublyCircularLinkedList()
for value in (1, 2, 3, 4, 5):
    dcll.insert_end(value)          # build ring: 1<->2<->3<->4<->5<->(back to 1)

print("Forward traversal:  ", end=""); dcll.display_forward()
print("Backward traversal: ", end=""); dcll.display_backward()

dcll.insert_beginning(0)            # 0<->1<->2<->3<->4<->5<->(back to 0)
print("After insert_begin: ", end=""); dcll.display_forward()

dcll.delete_value(3)                # remove node with data=3
print("After delete(3):    ", end=""); dcll.display_forward()
