#  Data Model

## NotificationEvent
- id (UUID)
- user_id
- event_type
- message
- priority_hint
- timestamp
- channel
- expires_at

## UserNotificationHistory
- user_id
- notifications_last_hour
- notifications_last_day
- last_sent_time

## SuppressionRecord
- dedupe_hash
- timestamp

## DeferredNotification
- notification_id
- scheduled_time

## AuditLog
- notification_id
- decision
- reason
- timestamp
