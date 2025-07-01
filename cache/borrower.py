from . import redis_client

def test():
    return "redis connect ok"

def get_borrowed_books(borrower: str) -> list[str]:
    key = f"borrower:{borrower}:books"
    return redis_client.lrange(key, 0, -1)