import os
import unittest
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import foring.core as fc


class Testforing(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.dir_path = Path(self.test_dir.name)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_json_handling(self):
        filepath = str(self.dir_path / "test.json")
        sample = {"user": "Shayan", "active": True}
        fc.write(sample, filepath)
        self.assertEqual(fc.read(filepath), sample)

    def test_csv_handling(self):
        filepath = str(self.dir_path / "test.csv")
        sample = [["A", "B"], ["1", "2"]]
        fc.write(sample, filepath)
        self.assertEqual(fc.read(filepath), sample)

    def test_ini_handling(self):
        filepath = str(self.dir_path / "test.ini")
        sample = {"DEMO": {"key": "value"}}
        fc.write(sample, filepath)
        self.assertEqual(fc.read(filepath), sample)

    def test_yaml_handling(self):
        """Test both .yml and .yaml syntax layouts."""
        sample_data = {
            "app": "foring",
            "features": ["simple", "flexible", "fast"],
            "version": 1.0
        }
        
        # Test .yaml path
        yaml_path = str(self.dir_path / "config.yaml")
        fc.write(sample_data, yaml_path)
        self.assertEqual(fc.read(yaml_path), sample_data)
        
        # Test .yml path
        yml_path = str(self.dir_path / "config.yml")
        fc.write(sample_data, yml_path)
        self.assertEqual(fc.read(yml_path), sample_data)

    def test_xml_handling(self):
        """Test XML parsing using Element objects."""
        filepath = str(self.dir_path / "data.xml")
        
        # Build a standard XML Element structure
        root = ET.Element("root")
        child = ET.SubElement(root, "element")
        child.text = "Hello XML"
        child.set("status", "verified")
        
        # Write the element tree structure
        fc.write(root, filepath)
        
        # Read back and confirm parsing integrity
        parsed_root = fc.read(filepath)
        self.assertEqual(parsed_root.tag, "root")
        self.assertEqual(parsed_root.find("element").text, "Hello XML")
        self.assertEqual(parsed_root.find("element").get("status"), "verified")

    def test_plain_text(self):
        filepath = str(self.dir_path / "notes.txt")
        sample = "foring text evaluation process."
        fc.write(sample, filepath)
        self.assertEqual(fc.read(filepath), sample)

    def test_binary_fallback(self):
        filepath = str(self.dir_path / "blob.bin")
        sample = b"\x00\x01\x02\x03\xff"
        fc.write(sample, filepath)
        self.assertEqual(fc.read(filepath), sample)

    def test_pickle_serialization(self):
        filepath = str(self.dir_path / "object.pkl")
        sample = (10, 20, [30, 40])
        fc.write(sample, filepath)
        self.assertEqual(fc.read(filepath), sample)


if __name__ == "__main__":
    unittest.main()