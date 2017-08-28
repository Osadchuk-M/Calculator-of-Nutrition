from flask import render_template, jsonify

from ..models import Food
from . import main


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/get_product_names')
def get_product_names():
    return jsonify([obj.name for obj in Food.query.all()])
