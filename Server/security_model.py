from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256", "des_crypt"],
    deprecated="auto",
    pbkdf2_sha256__rounds=29000
)

if __name__ == "__main__":
    pass
