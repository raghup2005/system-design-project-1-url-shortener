from sqlalchemy import Column, String
from databases import Base

class URL(Base):
    __tablename__ = "urls"

    short_code = Column(String, primary_key=True, index=True)
    original_url = Column(String, nullable=False)





