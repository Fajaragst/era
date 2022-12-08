"""
see https://github.com/juliotrigo/sqlalchemy-filters/blob/7222192421c2b235ba1a6cb806ce61fdb165bd79/sqlalchemy_filters/models.py#L10
"""

from sqlalchemy.inspection import inspect
from sqlalchemy.util import symbol
import types

def _is_hybrid_property(orm_descriptor):
    return orm_descriptor.extension_type == symbol('HYBRID_PROPERTY')


def _is_hybrid_method(orm_descriptor):
    return orm_descriptor.extension_type == symbol('HYBRID_METHOD')

class Field(object):

    def __init__(self, model, field_name):
        self.model = model
        self.field_name = field_name

    def get_sqlalchemy_field(self):
        """Method to find sqlalchemy field by string (return: SqlAlchemy.Model)"""
        if self.field_name not in self._get_valid_field_names():
            return None
    
        sqlalchemy_field = getattr(self.model, self.field_name)

        # If it's a hybrid method, then we call it so that we can work with
        # the result of the execution and not with the method object itself
        if isinstance(sqlalchemy_field, types.MethodType):
            sqlalchemy_field = sqlalchemy_field()

        return sqlalchemy_field

    def _get_valid_field_names(self):
        inspect_mapper = inspect(self.model)
        columns = inspect_mapper.columns
        orm_descriptors = inspect_mapper.all_orm_descriptors

        column_names = columns.keys()
        hybrid_names = [
            key for key, item in orm_descriptors.items()
            if _is_hybrid_property(item) or _is_hybrid_method(item)
        ]

        return set(column_names) | set(hybrid_names)