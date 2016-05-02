# Data Structures & Sorting Algorithms
A collection of classical data structures and Sorting Algorithms

## BST
A self balancing binary search tree.

Composed of a BST class and a Node class.
User should only interact with the bst class directly.

### Methods available for use:

pre_order():
    Returns a generator that, when put into a list returns a preordered
    traversal of the tree.

in_order():
    Returns a generator that, when put into a list returns a preordered
    traversal of the tree.


post_order():
    Returns a generator that, when put into a list returns a preordered
    traversal of the tree.

insert(value):
    If value not contained in tree, insert new node containing value
    into the appropriate spot on the tree.

## Merge Sort
    Implementation of the Merge Sort.

    Merge sort recursively splits the list in half and creates a 
    new list by comparing items from left to right in each of those lists.

    Time Complexity: O(nlogn)

## Insertion

`insertion_sort(list)`:
    Takes a list of integers and sorts them smallest to biggest using the insertion_sort
    insertion algorithm.
