from base import db
from base.com.vo.category_vo import CategoryVO

class CategoryDAO:
    def insert_category(self, category_vo):
        """
        Method to insert a new category into the database.

        Args:
            category_vo (CategoryVO): CategoryVO object containing category details.

        Raises:
            Exception: If an error occurs while inserting the category into the database.

        """
        try:
            with db.session.begin():
                db.session.add(category_vo)
        except Exception as e:
            db.session.rollback()
            raise e

    def view_category(self):
        """
        Method to retrieve all categories from the database.

        Returns:
            list: List of CategoryVO objects representing categories in the database.

        Raises:
            Exception: If an error occurs while retrieving categories from the database.

        """
        try:
            category_vo_list = CategoryVO.query.all()
            return category_vo_list
        except Exception as e:
            raise e

    def get_category_by_id(self, category_id):
        """
        Method to retrieve a category by its ID from the database.

        Args:
            category_id (int): ID of the category to be retrieved.

        Returns:
            CategoryVO: CategoryVO object representing the retrieved category.

        Raises:
            Exception: If an error occurs while retrieving the category from the database.

        """
        try:
            category_vo = CategoryVO.query.get(category_id)
            return category_vo
        except Exception as e:
            raise e

    def delete_category(self, category_vo):
        """
        Method to delete a category from the database.

        Args:
            category_vo (CategoryVO): CategoryVO object to be deleted.

        Raises:
            Exception: If an error occurs while deleting the category from the database.

        """
        try:
            with db.session.begin():
                db.session.delete(category_vo)
        except Exception as e:
            db.session.rollback()
            raise e

    def update_category(self, category_vo):
        """
        Method to update a category in the database.

        Args:
            category_vo (CategoryVO): CategoryVO object containing updated category details.

        Raises:
            Exception: If an error occurs while updating the category in the database.

        """
        try:
            with db.session.begin():
                db.session.merge(category_vo)
        except Exception as e:
            db.session.rollback()
            raise e
