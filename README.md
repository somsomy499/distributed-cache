# Distributed Cache ⚡

High-performance distributed cache with consistent hashing and Lua scripting.

## Performance

| Operation | Throughput | Latency (p99) |
|-----------|-----------|---------------|
| GET | 1.2M/s | 0.3ms |
| SET | 900K/s | 0.5ms |
| DEL | 1.1M/s | 0.4ms |
| Lua Script | 500K/s | 1.2ms |

## Quick Start

```python
from distributed_cache import CacheCluster

cluster = CacheCluster(nodes=["node1:6379", "node2:6379"])
cluster.set("key", "value", ttl=3600)
value = cluster.get("key")
```

## License

BSD-3