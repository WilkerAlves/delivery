import click
from delivery.ext.db import db
from delivery.ext.site import models # noqa


def init_app(app):
    @app.cli.command()
    def create_db():
        """Este comando inicializa o db"""
        db.create_all()

    @app.cli.command()
    def list_orders():
        # return "Lista de pedidos"
        click.echo("Lista de pedidos")

    @app.cli.command()
    def list_users():
        # return "Lista de usuarios"
        click.echo("Lista de usuarios")
