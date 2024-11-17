
## TODO Gestión de excepciones
import re
import logging




class EmailValidator:
    def __init__(self):
        self.regex = re.compile(r'([A-Za-z]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        self.logger = logging.getLogger(__name__)  #logger específico para esta clase

    def validar(self, correo: str):
        """
        Valida si el correo cumple con el patrón.
        Maneja excepciones si el formato de entrada es inválido.
        """

    def validar(self, correo: str):
        """
        Valida si el correo cumple con el patrón y registra eventos en logs. No he modificado la funcion
        """
        self.logger.debug(f"Validando el correo: {correo}")
        try:
            result = re.fullmatch(self.regex, correo)
            if result:
                self.logger.info(f"Correo válido: {correo}")
            else:
                self.logger.warning(f"Correo inválido: {correo}")
            return result
        except Exception as e:
            self.logger.error(f"Error al validar el correo '{correo}': {e}")
            raise
        
