from datetime import datetime


def health_check():
    return {
        "status": "healthy",
        "service": "Enterprise AI Platform",
        "version": "0.1.0",
        "timestamp": datetime.utcnow().isoformat()
    }
