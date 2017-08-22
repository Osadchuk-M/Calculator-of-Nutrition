#!/usr/bin/env python
from flask_script import Manager, Shell

from app import create_app, db
from app.models import Food
from scraping_with_bs4 import get_products_from_tables


app = create_app()
manager = Manager(app)


def make_shell_context():
    return {
        'app': app,
        'db': db,
        'Food': Food
    }
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def bootstrap():
    db.create_all()
    data = get_products_from_tables()
    db.session.add_all(data)
    db.session.commit()


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
