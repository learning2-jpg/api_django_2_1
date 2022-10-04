# -*- coding: utf-8 -*-

from django.apps import AppConfig


class ClienteConfig(AppConfig):
    """creamos una app.py para que django sepa que estamos agregando el modelo cliente."""

    name = 'apps.clientes'
    verbose_name = 'Cliente'
    verbose_name_plural = 'Clientes'

