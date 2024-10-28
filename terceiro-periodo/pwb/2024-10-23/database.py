from sqlmodel import Field, Session, SQLModel, create_engine, select



def get_engine():
    return create_engine("sqlite:///clubes.db")
    