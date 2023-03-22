#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

if not storage_mode().is_db():
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

else:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
storage.reload()

def storage_mode():
    """Define storage mode based on os.environ"""
    import os
    st_mode = os.getenv('HBNB_TYPE_STORAGE', default='file')
    
    def is_db():
        """Check if the storage type is a database"""
        if st_mode == 'db':
            return True
        return False

if __name__ = '__main__':
    storage_mode()

