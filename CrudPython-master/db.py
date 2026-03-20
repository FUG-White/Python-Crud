from sqlalchemy import create_engine, Column,Integer, String,Boolean
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine("sqlite:///banco.db")
Base=declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome= Column(String)
    email= Column(String(60), nullable=False, unique=True) 
    idade=Column(Integer)
    ativo=Column(Boolean, default= True)

Base.metadata.create_all(bind=engine)
Session= sessionmaker(engine)