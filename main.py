
from emails.validator import EmailValidator
from logs.logging_config import setup_logging

if __name__ == "__main__":
    # Configurar logging
    setup_logging()

    validator = EmailValidator()

    # Pruebas de validación
    correos = [
        "usuario@gmail.com",         # Válido
        "usuario.nombre@gmail.com",  # Válido
        "usuario@@gmail",            # Inválido
        12345,                       # Tipo inválido
        None,                        # Tipo inválido
        "",                          # Vacío (Inválido)
    ]

    for correo in correos:
        resultado = validator.validar(correo)
        print(f"Validación de '{correo}': {'Válido' if resultado else 'Inválido'}")