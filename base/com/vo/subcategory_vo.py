from base import db
from base.com.vo.category_vo import CategoryVO

class SubCategoryVO(db.Model):
    # Define the table name in the database
    __tablename__ = 'subcategory_table'

    # Define columns for the subcategory_table
    subcategory_id = db.Column('subcategory_id', db.Integer, primary_key=True, autoincrement=True)
    subcategory_name = db.Column('subcategory_name', db.String(255), nullable=False)
    subcategory_description = db.Column('subcategory_description', db.Text, nullable=False)
    subcategory_category_id = db.Column('subcategory_category_id', db.Integer,
                                        db.ForeignKey(CategoryVO.category_id, ondelete='CASCADE', onupdate='CASCADE'),
                                        nullable=False)

    # Define relationship with CategoryVO using foreign key
    category = db.relationship(CategoryVO, backref='subcategories')

    def __init__(self, subcategory_name, subcategory_description, subcategory_category_id):
        """
        Constructor to initialize SubCategoryVO object with provided details.

        Args:
            subcategory_name (str): Name of the subcategory.
            subcategory_description (str): Description of the subcategory.
            subcategory_category_id (int): ID of the associated category.

        """
        self.subcategory_name = subcategory_name
        self.subcategory_description = subcategory_description
        self.subcategory_category_id = subcategory_category_id

    def serialize(self):
        """
        Method to serialize the SubCategoryVO object into a dictionary.

        Returns:
            dict: A dictionary containing subcategory details.

        """
        return {
            'subcategory_id': self.subcategory_id,
            'subcategory_name': self.subcategory_name,
            'subcategory_description': self.subcategory_description,
            'subcategory_category_id': self.subcategory_category_id
        }
