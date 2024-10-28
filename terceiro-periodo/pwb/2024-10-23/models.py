from sqlmodel import Field, Session, SQLModel, create_engine, select


class ClubeBase(SQLModel):
    nome: str = Field(min_length=3)
    serie: str = Field(min_length=1, max_length=1)


class Clube(ClubeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class RequestClube(ClubeBase):
    pass

