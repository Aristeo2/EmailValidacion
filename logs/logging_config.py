import logging
import logging.config
import os



# Configuración de logging
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,  # No deshabilitar loggers existentes
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
        "simple": {      
            "format": "%(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",  # Nivel de registro para el archivo
            "class": "logging.FileHandler",
            "filename": os.path.join("logs", "email_validator.log"),
            "formatter": "default",
             "mode": "w", #Se sobreescriben los logs anteriores
        },
        "console": {
            "level": "INFO",  # Nivel de registro para la consola
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "root": {
        "level": "DEBUG",  # Nivel de registro global
        "handlers": ["file", "console"]
    },
}

def setup_logging():
    """Aplica la configuración de logging."""
    logging.config.dictConfig(LOGGING_CONFIG)
