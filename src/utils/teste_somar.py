import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from main import somar


def test_somar_positivos():
    assert somar(2, 3) == 5


def test_somar_negativos():
    assert somar(-4, 7) == 3


def test_somar_zero():
    assert somar(0, 0) == 0


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-v"]))
