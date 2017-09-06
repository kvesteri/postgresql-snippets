import pytest


def get_sql():
    with open('tests/truthy.sql', 'r') as f:
        return f.readlines()


@pytest.mark.parametrize(
    'sql',
    get_sql()
)
def test_truthy_test(connection, truthy_func, sql):
    assert connection.execute(sql).scalar(), sql.strip()
