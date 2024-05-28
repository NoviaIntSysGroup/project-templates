from {{ cookiecutter.package_name }}.hello import hello


def test_hello():
    expected = "Hello World"
    result = hello("World")
    assert result == expected