#  Duplicate Prevention Strategy

## Exact Duplicates
- Use dedupe_key if available
- Generate hash(event_type + message + source)

## Near-Duplicates
- Text similarity comparison
- Time window suppression (e.g., 5 minutes)

## Storage
Store recent hashes in Redis or cache with TTL.
