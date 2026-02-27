#  Decision Logic

## Classification Strategy

Each notification is evaluated based on:

- priority_hint
- event_type
- user notification history
- quiet hours
- expiry time
- duplicate detection

---

## Rule Hierarchy

1. Expired notifications → SUPPRESS
2. Duplicate detected → SUPPRESS
3. Critical priority → SEND NOW
4. User overload detected → DEFER
5. Promotional during noisy period → DEFER
6. Default → SEND NOW

---

## Example Pseudocode

IF expires_at < current_time:
    decision = NEVER
ELIF duplicate_found:
    decision = NEVER
ELIF priority == "critical":
    decision = NOW
ELIF notifications_last_hour > threshold:
    decision = LATER
ELSE:
    decision = NOW
