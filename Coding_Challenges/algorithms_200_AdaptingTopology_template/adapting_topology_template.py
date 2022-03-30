#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml

graph = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1],
    4: [1, 5, 7, 8],
    5: [4, 6],
    6: [5, 7],
    7: [4, 6],
    8: [4],
}


def n_swaps(cnot):
    """Count the minimum number of swaps needed to create the equivalent CNOT.

    Args:
        - cnot (qml.Operation): A CNOT gate that needs to be implemented on the hardware
        You can find out the wires on which an operator works by asking for the 'wires' attribute: 'cnot.wires'

    Returns:
        - (int): minimum number of swaps
    """

    # QHACK #
    wire1, wire2 = cnot.wires

    color = dict()
    for v in graph:
        color[v] = 'white'
        
    P = dict()
    P[wire1] = None
    color[wire1] = 'gray'
    Q = [wire1]
    while Q:
        u = Q[0]
        for v in graph[u]:
            if color[v] == 'white':
                P[v] = u
                color[v] = 'gray'
                Q.append(v)
        Q.pop(0)
        color[u] = 'black'
    
    count = 0
    while P[wire2] != None:
        count += 1
        wire2 = P[wire2]
    return (count - 1) * 2
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    output = n_swaps(qml.CNOT(wires=[int(i) for i in inputs]))
    print(f"{output}")
