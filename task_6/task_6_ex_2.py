"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.

The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods __getitem__, __setitem__, __delitem__.


Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""
class Item:
    """
    A node in a unidirectional linked list.
    """
    def __init__(self, data):
        self.item = data
        self.ref = None


class CustomList:
    """
    An unidirectional linked list.
    """
    def __init__(self, *args):
        self.start_node = None
        for i in args:
            self.append(i)

    def display(self):
        display = []
        n = self.start_node
        while n is not None:
            display.append(n.item)
            n = n.ref
        print(display)

    def add_start(self, data):
        new_node = Item(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def append(self, data):
        new_node = Item(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def remove(self, value):
        if self.start_node is None:
            raise Exception("The list has no element to delete")

        if self.start_node.item == value:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        while n.ref is not None:
            if n.ref.item == value:
                n.ref = n.ref.ref
                return
            n = n.ref

        raise Exception("Item was not found in the list")

    def find(self, value):
        n = self.start_node
        index = 0
        while n is not None:
            if n.item == value:
                return index
            n = n.ref
            index += 1
        raise Exception("Item not found")

    def clear(self):
        self.start_node = None

    def __len__(self):
        n = self.start_node
        count = 0
        while n is not None:
            count += 1
            n = n.ref
        return count

    def __getitem__(self, index):
        if self.start_node is None:
            raise Exception("List has no elements")

        if index == 0:
            return self.start_node.item

        n = self.start_node
        enum = 0

        while enum != index:
            if n is None:
                raise Exception("List index out of range")
            n = n.ref
            enum += 1
        return n.item

    def __setitem__(self, index, data):
        n = self.start_node
        enum = 0

        while enum != index:
            if n is None:
                raise Exception("List index out of range")
            n = n.ref
            enum += 1
        n.item = data

    def __delitem__(self, index):
        if self.start_node is None:
            raise Exception("List has no elements")

        if index == 0:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        enum = 0

        while n is not None:
            enum += 1
            n = n.ref

        if index > enum-1:
            raise Exception("List index out of range")

        if index == enum:
            n.ref = None
            return

        n = self.start_node
        enum = 1

        while enum != index:
            enum += 1
            n = n.ref
        n.ref = n.ref.ref

    def __iter__(self):
        if self.start_node is None:
            raise StopIteration
        self.next_node = self.start_node
        return self

    def __next__(self):
        self.current_node = self.next_node
        if self.current_node is None:
            raise StopIteration
        self.next_node = self.next_node.ref
        return self.current_node.item
