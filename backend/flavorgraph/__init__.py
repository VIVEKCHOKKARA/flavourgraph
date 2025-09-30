"""
FlavorGraph package initializer.

Modules:
- data: load recipes and substitutions
- graph: build ingredient co-occurrence graphs
- search: greedy and backtracking recipe search
- subs: ingredient substitution logic
"""

from . import data, graph, search, subs

__all__ = ["data", "graph", "search", "subs"]
