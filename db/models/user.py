from ..db_setup import Base
from sqlalchemy import Boolean,Column,ForeignKey,Integer,Enum,Text,String
from sqlalchemy.orm import relationship

import enum
class Role(enum.Enum):
    teacher = 1
    student = 2

# User and Profile are one to one relationship
# uselist = False for that

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,unique=True,index=True,nullable=False)
    role = Column(Enum(Role))

    profile = relationship("Profile",back_populates="owner",uselist=False)

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    bio = email = Column(Text,nullable=True)
    is_active = Column(Boolean,default = False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)

    owner = relationship("User",back_populates="profile")