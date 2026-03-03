from sqlalchemy.orm import declarative_base, Mapped, mapped_column

base_class_not_pyd = declarative_base()

class BaseClass(base_class_not_pyd):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
