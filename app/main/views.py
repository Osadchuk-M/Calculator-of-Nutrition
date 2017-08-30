from flask import render_template, jsonify, request

from ..models import Food
from . import main


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/calculate', methods=['GET', 'POST'])
def calculate():
    nutrients_need = Food.nutrients_need(float(request.json['weight']))
    nutrients_got = Food.nutrients_got(request.json['products'])
    return jsonify({
        'need': nutrients_need,
        'got': nutrients_got
    })


@main.route('/get_product_names')
def get_product_names():
    return jsonify([obj.name for obj in Food.query.all()])
