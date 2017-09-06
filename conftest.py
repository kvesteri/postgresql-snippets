# -*- coding: utf-8 -*-
import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


@pytest.fixture
def db_user():
    return os.environ.get('POSTGRESQL_SNIPPETS_TEST_USER', 'postgres')


@pytest.fixture
def db_name():
    return os.environ.get(
        'POSTGRESQL_SNIPPETS_TEST_DB',
        'postgresql_snippets_test'
    )


@pytest.fixture
def dns(db_user, db_name):
    return 'postgres://{}@localhost/{}'.format(db_user, db_name)


@pytest.fixture
def base():
    return declarative_base()


@pytest.yield_fixture
def engine(dns):
    engine = create_engine(dns)
    engine.echo = bool(os.environ.get('POSTGRESQL_AUDIT_TEST_ECHO'))
    yield engine
    engine.dispose()


@pytest.yield_fixture
def connection(engine):
    conn = engine.connect()
    yield conn
    conn.close()


@pytest.fixture
def truthy_func(connection):
    with open('truthy.sql', 'r') as file:
        sql = file.read()
    connection.execute(sql)
