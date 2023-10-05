from base import db
from base.com.vo.category_vo import CategoryVO

class CategoryDAO:
    def insert_category(self, category_vo):
        with db.session.begin():
            db.session.add(category_vo)

    def view_category(self):
        try:
            category_vo_list = CategoryVO.query.all()
            return category_vo_list
        except Exception as e:
            raise e

    def get_category_by_id(self, category_id):
        try:
            category_vo = CategoryVO.query.get(category_id)
            return category_vo
        except Exception as e:
            raise e

    def delete_category(self, category_vo):
        try:
            with db.session.begin():
                db.session.delete(category_vo)
        except Exception as e:
            db.session.rollback()
            raise e

    def update_category(self, category_vo):
        try:
            with db.session.begin():
                db.session.merge(category_vo)
        except Exception as e:
            db.session.rollback()
            raise e
