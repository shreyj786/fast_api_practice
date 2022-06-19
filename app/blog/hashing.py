from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:

    def bcrypt(password: str):
        return pwd_context.hash(password)

    def verify(hashed_password, plain_passowrd):
        return pwd_context.verify(plain_passowrd,hashed_password)

