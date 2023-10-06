from base import db
from base.com.vo.subcategory_vo import SubCategoryVO

class SubCategoryDAO:
    def insert_subcategory(self, subcategory_vo):
        """
        Method to insert a new subcategory into the database.

        Args:
            subcategory_vo (SubCategoryVO): SubCategoryVO object containing subcategory details.

        Raises:
            Exception: If an error occurs while inserting the subcategory into the database.

        """
        try:
            db.session.add(subcategory_vo)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def get_subcategory_by_id(self, subcategory_id):
        """
        Method to retrieve a subcategory by its ID from the database.

        Args:
            subcategory_id (int): ID of the subcategory to be retrieved.

        Returns:
            SubCategoryVO: SubCategoryVO object representing the retrieved subcategory.

        Raises:
            Exception: If an error occurs while retrieving the subcategory from the database.

        """
        try:
            subcategory_vo = SubCategoryVO.query.get(subcategory_id)
            return subcategory_vo
        except Exception as e:
            raise e

    def view_subcategory(self):
        """
        Method to retrieve all subcategories from the database.

        Returns:
            list: List of SubCategoryVO objects representing subcategories in the database.

        Raises:
            Exception: If an error occurs while retrieving subcategories from the database.

        """
        try:
            subcategory_vo_list = SubCategoryVO.query.all()
            return subcategory_vo_list
        except Exception as e:
            raise e

    def update_subcategory(self, subcategory_vo):
        """
        Method to update a subcategory in the database.

        Args:
            subcategory_vo (SubCategoryVO): SubCategoryVO object containing updated subcategory details.

        Raises:
            Exception: If an error occurs while updating the subcategory in the database.

        """
        try:
            db.session.merge(subcategory_vo)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_subcategory(self, subcategory_id):
        """
        Method to delete a subcategory from the database.

        Args:
            subcategory_id (int): ID of the subcategory to be deleted.

        Raises:
            Exception: If an error occurs while deleting the subcategory from the database.

        """
        try:
            subcategory_vo = SubCategoryVO.query.get(subcategory_id)
            db.session.delete(subcategory_vo)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
