from dataclasses import dataclass
from datetime import datetime
from typing import Literal


@dataclass
class AgentMessage:
    msg_id: str
    from_agent: str
    to_agent: str  # "*"" for broadcast
    msg_type: Literal["task", "result", "error", "heartbeat"]
    content: dict
    reply_to: str | None = None
    created_at: datetime = None
    ttl: int = 30
    retries: int = 0

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.utcnow()
