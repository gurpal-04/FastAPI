
from sqlalchemy import Column, Integer, String, Float, Boolean, Uuid
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID, uuid4
from ..db import Base


class Item(Base):
    __tablename__ = "items"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    title = Column(String, index=True, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)