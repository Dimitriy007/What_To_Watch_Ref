import csv

import click

from . import app, db
from .models import Opinion


@app.cli.command('load_opinions')
def load_opinions():
    """Загрузка данных из CSV файла в БД."""
    with open('opinions.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            opinion = Opinion(
                title=row['title'],
                text=row['text'],
                source=row['source'],
                added_by=row['added_by']
            )
            db.session.add(opinion)
        db.session.commit()
    click.echo('Загрузка данных завершена!')