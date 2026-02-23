from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime
from datetime import datetime
from ..core.base_class import BaseClass

class FinDocs(BaseClass):
    __tablename__ = "fin_docs"

    operation_type: Mapped[str] = mapped_column(String(30), nullable=False)
    overall_sum: Mapped[float] = mapped_column()
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True))

