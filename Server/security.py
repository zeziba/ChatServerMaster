from .security_model import pwd_context


def get_hash(pwd: str) -> str:
    return pwd_context.hash(pwd)


def verify(pwd: str, _hash: str) -> bool:
    return pwd_context.verify(pwd, _hash)
