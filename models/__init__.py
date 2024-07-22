#!/usr/bin/python3
"""__init__ file for the application"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
