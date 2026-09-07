from random import randint

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import OpinionForm
from .models import Opinion


@app.route('/')
def index_view():
    quantity = Opinion.query.count()
    if not quantity:
        return render_template('index.html', opinion=None)
    offset_value = randint(0, quantity - 1)
    opinion = Opinion.query.offset(offset_value).first()
    return render_template('index.html', opinion=opinion)


@app.route('/add', methods=['GET', 'POST'])
def add_opinion_view():
    form = OpinionForm()
    if form.validate_on_submit():
        opinion = Opinion(
            title=form.title.data,
            text=form.text.data,
            source=form.source.data
        )
        db.session.add(opinion)
        db.session.commit()
        return redirect(url_for('opinion_view', id=opinion.id))
    return render_template('add_opinion.html', form=form)


@app.route('/opinions/<int:id>')
def opinion_view(id):
    opinion = Opinion.query.get_or_404(id)
    return render_template('opinion.html', opinion=opinion)