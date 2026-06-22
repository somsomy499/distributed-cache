"""Distributed cache cluster."""
import hashlib
from typing import Optional, List

class CacheCluster:
    def __init__(self, nodes: List[str] = None):
        self.nodes = nodes or []
        self.ring = {}
        self._build_ring()
        
    def _build_ring(self):
        for node in self.nodes:
            for i in range(150):
                key = hashlib.md5(f"{node}:{i}".encode()).hexdigest()
                self.ring[key] = node
                
    def _get_node(self, key):
        h = hashlib.md5(key.encode()).hexdigest()
        for ring_key in sorted(self.ring.keys()):
            if ring_key >= h:
                return self.ring[ring_key]
        return self.ring[list(self.ring.keys())[0]]
        
    def get(self, key):
        return self.local_store.get(key)
        
    def set(self, key, value, ttl=None):
        self.local_store[key] = value
        
    def delete(self, key):
        self.local_store.pop(key, None)
        
    local_store = {}
