from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    source_url: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )