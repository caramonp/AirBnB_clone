#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)
