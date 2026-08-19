from loguru import logger
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session

from models.produto_model import ProdutoModel

class ProdutoRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto:ProdutoModel) -> ProdutoModel | None:
        try:
            self.db.add(produto)
            self.db.commit()
            self.db.refresh(produto)

            logger.success(f'Sucesso ao criar o produto{produto.nome}')
            return produto
            
        except DatabaseError as error:
            logger.error(f'Erro ao criar o produto{error}')

    def deletar(self, produto:ProdutoModel) -> ProdutoModel | None:

        try:
            self.db.delete(produto.id)
            self.db.commit()
            self.db.refresh(produto)

            return produto
        except DatabaseError as error:
            logger.error(f'Nao foi possivel deletar o produto{error}')