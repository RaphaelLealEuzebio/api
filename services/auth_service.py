from sqlalchemy.orm import Session

class AuthService():
    def __init__(self, db: Session):
        self.db = db

    def buscar_usuario(self,email:str) -> bool:
        usuario_email = self.db.query(email).filter_by(email=email).firs()
        if not usuario_email:
            print('usuario nao encontrado')
            usuario = False
        else:
            print('usuario encontrado')
            usuario = True
        return usuario
    
    def verificar_usuario(usuario):
        pass
    def gerar_token():
        pass
    
    