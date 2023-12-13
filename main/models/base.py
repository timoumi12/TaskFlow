from sqlalchemy.ext.declarative import declarative_base
import models
Base = declarative_base()
class utils:

    def save(self):
        """save"""
        models.storage.new(self)
        models.storage.save()
    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
