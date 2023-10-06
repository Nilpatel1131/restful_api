from base import db

class CategoryVO(db.Model):
    # Define the table name in the database
    __tablename__ = 'category_table'

    # Define columns for the category_table
    category_id = db.Column('category_id', db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column('category_name', db.String(255), nullable=False)
    category_description = db.Column('category_description', db.Text, nullable=False)

    def __init__(self, category_name, category_description):
        """
        Constructor to initialize CategoryVO object with provided category_name and category_description.

        Args:
            category_name (str): Name of the category.
            category_description (str): Description of the category.

        """
        self.category_name = category_name
        self.category_description = category_description

    def serialize(self):
        """
        Method to serialize the CategoryVO object into a dictionary.

        Returns:
            dict: A dictionary containing category details.

        """
        return {
            'category_id': self.category_id,
            'category_name': self.category_name,
            'category_description': self.category_description
        }
