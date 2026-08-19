from loguru import logger
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session

from models.usuario_model import EnderecoModel, UsuarioModel


class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, usuario:UsuarioModel) -> UsuarioModel | None:
        try:
            self.db.add(usuario)
            self.db.commit()
            self.db.refresh(usuario)

            return usuario
        except DatabaseError as error:
            logger.error(f'Erro ao criar o usuario: {error}')

    def deletar(self, usuario:UsuarioModel) -> UsuarioModel | None:
        try:
            self.db.delete(usuario)
            self.db.commit()
            self.db.refresh(usuario)

            return usuario
        except DatabaseError as error:
           logger.error(f'Erro ao deleter o usuario{error}')
           
    def buscar_usuario(self, email: str)-> UsuarioModel | None:
        try:
            usuario = self.db.query(UsuarioModel).filter_by(email=email).first()
            return usuario
        except DatabaseError as error:
            logger.error(f'Usuario nao encontrado: {error}')