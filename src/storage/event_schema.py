EVENT_SCHEMA = {
    "event_id": str,
    "project": str,
    "camera": {
        "camera_id": str,
        "location": str,
        "stream": str
    },
    "session": {
        "session_name": str,
        "started_at": str
    },
    "event": {
        "type": str,
        "start_frame": int,
        "end_frame": int
    },
    "files": {
        "attention_video": str,
        "session_video": str,
        "possible_snapshot": str
    },
    "model": {
        "motion_model": str,
        "history": int,
        "attention_window": int
    },
    "created_at": str,
    "notification": {
        "enabled": bool,
        "status": str,
        "channel": str,
        "sent_at": str,
        "retry_count": int,
        "last_error": str
    }
}


CAMERA_SCHEMA = {
    "camera_id": str,
    "project": str,
    "location": str,
    "stream": str,
    "status": str,
    "current_session": str,
    "output_dir": str,
    "last_seen_at": str,
    "updated_at": str
}


SESSION_SCHEMA = {
    "session_name": str,
    "camera_id": str,
    "project": str,
    "status": str,
    "started_at": str,
    "ended_at": str,
    "created_at": str
}


SYSTEM_LOG_SCHEMA = {
    "log_type": str,
    "level": str,
    "message": str,
    "metadata": dict,
    "created_at": str
}
