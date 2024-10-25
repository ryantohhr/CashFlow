import pytest
import project

def test_main(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: (_ for _ in ()).throw(EOFError))
    assert project.main() == 0

def test_default(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "v")
    assert project.default("rounded_outline") == 0

def test_customise(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "")
    assert project.customise() == "rounded_outline"
    monkeypatch.setattr('builtins.input', lambda _: "plain")
    assert project.customise() == "plain"


