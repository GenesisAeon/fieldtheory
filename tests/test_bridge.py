"""Tests for fieldtheory.entropy_table_bridge."""

from pathlib import Path

import yaml

from fieldtheory.entropy_table_bridge import FieldtheoryBridge


def test_bridge_instantiates():
    bridge = FieldtheoryBridge()
    assert bridge.domain == "fieldtheory"


def test_bridge_custom_domain():
    bridge = FieldtheoryBridge(domain="test-domain")
    assert bridge.domain == "test-domain"


def test_add_relation_stores_value():
    bridge = FieldtheoryBridge()
    bridge.add_relation("S_mod_mean", 0.9)
    assert bridge._relations["S_mod_mean"] == 0.9


def test_export_creates_file(tmp_path):
    bridge = FieldtheoryBridge(domain="test")
    bridge.add_relation("collapse_threshold", 0.618)
    output = tmp_path / "out.yaml"
    result = bridge.export(output)
    assert result == output
    assert output.exists()


def test_export_yaml_schema(tmp_path):
    bridge = FieldtheoryBridge(domain="myfield")
    bridge.add_relation("mean", 1.23)
    output = tmp_path / "domains.yaml"
    bridge.export(output)
    data = yaml.safe_load(output.read_text())
    assert "domains" in data
    assert "myfield" in data["domains"]
    assert data["domains"]["myfield"]["mean"] == 1.23


def test_export_default_path(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    bridge = FieldtheoryBridge(domain="ft")
    bridge.add_relation("x", 0.5)
    result = bridge.export()
    assert Path(result).name == "domains.yaml"
