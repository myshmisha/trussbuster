import numpy as np
from dataclasses import dataclass

@dataclass
class Node:
    id: int
    x: float
    y: float

@dataclass
class Member:
    id: int
    n1: int
    n2: int

def solve_truss(nodes, members):
    """Simple fictitious solver just computes member length-based forces (demo)."""
    forces = {}
    if not members:
        return forces
    # fake loads: downward on each node
    F_total = 1000.0
    for m in members:
        n1 = next(n for n in nodes if n.id == m.n1)
        n2 = next(n for n in nodes if n.id == m.n2)
        L = ((n2.x-n1.x)**2 + (n2.y-n1.y)**2)**0.5
        forces[m] = (F_total / len(members)) * (1 if (n2.y < n1.y) else -1)
    return forces
