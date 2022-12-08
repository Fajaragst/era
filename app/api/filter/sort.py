from app.api.filter.field import Field

class Sort:

    SQL_ALCHEMY_SORT_FNC = {
        "desc" : lambda x : x.desc(),
        "asc" : lambda x : x.asc()
    }

    def __init__(self, model, order, field_name) -> None:
        self.model = model
        self.order = order
        self.field_name = field_name

    def get_sqlalchemy_sort_func(self):
        """Method to find sort func (result: SQLAlchemy.Model.desc())"""

        field = Field(self.model, self.field_name)
        sqlalchemy_field = field.get_sqlalchemy_field()
        if sqlalchemy_field is None:
            return None
        
        sort_fnc = self.SQL_ALCHEMY_SORT_FNC.get(self.order)
        
        if sort_fnc is None:
            return sqlalchemy_field
        
        return sort_fnc(sqlalchemy_field)

