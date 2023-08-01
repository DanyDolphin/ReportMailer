# Utils
import os

# SQLAlchemy
from sqlalchemy import ForeignKey, String, Integer, Float, create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    email = mapped_column(String(60), primary_key=True)
    name = mapped_column(String(60))

    transactions = relationship(
        'Transaction', back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name})"


class Transaction(Base):
    __tablename__ = "transaction"

    id = mapped_column(Integer(), primary_key=True)
    email = mapped_column(ForeignKey("user.email"))
    date = mapped_column(String(60))
    transaction = mapped_column(Float())

    user = relationship('User', back_populates="transactions")

    def __repr__(self) -> str:
        return (
            f"Address(id={self.id}, email={self.email}, date={self.date}, "
            f"transaction={self.transaction})")


def get_engine():
    uri = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
        f"/{os.getenv('DB_NAME')}")
    return create_engine(uri, echo=True)


engine = get_engine()
