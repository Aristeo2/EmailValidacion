import unittest
import pytest
from emails.validator import EmailValidator


# Instancia de EmailValidator
validator = EmailValidator()

def test_email_valido_simple():
    """Prueba con un correo válido simple"""
    assert validator.validar("usuario@gmail.com")

def test_email_valido_con_puntos_y_guion():
    """Prueba con un correo válido que contiene puntos y guiones"""
    assert validator.validar("usuario.nombre-apellido@gmail.com")

def test_email_valido_subdominio():
    """Prueba con un correo válido que contiene un subdominio"""
    assert validator.validar("usuario@mail.subdominio.com")

def test_email_invalido_doble_arroba():
    """Prueba con un correo inválido que contiene doble '@'"""
    assert not validator.validar("usuario@@gmail.com")

def test_email_invalido_sin_tld():
    """Prueba con un correo inválido que no tiene dominio de nivel superior"""
    assert not validator.validar("usuario@gmail")

def test_email_invalido_caracteres_especiales():
    """Prueba con un correo inválido que contiene caracteres especiales no permitidos"""
    assert not validator.validar("us$er@gmail.com")

def test_email_invalido_sin_usuario():
    """Prueba con un correo inválido que no tiene parte de usuario"""
    assert not validator.validar("@gmail.com")

def test_email_invalido_sin_arroba():
    """Prueba con un correo inválido que no contiene el carácter '@'"""
    assert not validator.validar("usuariogmail.com")

def test_email_valido_con_tld_largo():
    """Prueba con un correo válido con un TLD largo"""
    assert validator.validar("usuario@dominio.museum")

def test_email_invalido_con_vaio():
    """Prueba con un coreo inválido, vacio"""
    assert not validator.validar("")

