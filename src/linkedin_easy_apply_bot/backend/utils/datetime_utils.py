from datetime import datetime
from datetime import timezone

def now():
    return datetime.now(timezone.utc)

def to_datetime_string(timestamp: datetime):
    return timestamp.isoformat()
