from flask import request
from flask_restful import Resource
from base import db
from base.com.vo.category_vo import CategoryVO
from base.com.vo.subcategory_vo import SubCategoryVO

class SubcategoryResource(Resource):
    def get(self, subcategory_id=None):
        try:
            if subcategory_id:
                subcategory_vo = SubCategoryVO.query.get(subcategory_id)
                if subcategory_vo:
                    return subcategory_vo.as_dict()
                return {'message': 'Subcategory not found'}, 404
            else:
                subcategory_vo_list = SubCategoryVO.query.all()
                return {'subcategories': [subcategory.as_dict() for subcategory in subcategory_vo_list]}
        except Exception as ex:
            return {'error': str(ex)}, 500

    def post(self):
        try:
            data = request.get_json()
            subcategory_name = data.get('subcategory_name')
            subcategory_description = data.get('subcategory_description')
            subcategory_category_id = data.get('subcategory_category_id')
            category_vo = CategoryVO.query.get(subcategory_category_id)

            if not category_vo:
                return {'message': 'Invalid Category ID'}, 400

            subcategory_vo = SubCategoryVO(subcategory_name=subcategory_name,
                                           subcategory_description=subcategory_description,
                                           subcategory_category_id=subcategory_category_id)

            db.session.add(subcategory_vo)
            db.session.commit()
            return {'message': 'Subcategory created successfully'}, 201
        except Exception as ex:
            db.session.rollback()
            return {'error': str(ex)}, 500

    def put(self, subcategory_id):
        try:
            data = request.get_json()
            subcategory_vo = SubCategoryVO.query.get(subcategory_id)
            if not subcategory_vo:
                return {'message': 'Subcategory not found'}, 404

            subcategory_vo.subcategory_name = data.get('subcategory_name')
            subcategory_vo.subcategory_description = data.get('subcategory_description')
            subcategory_vo.subcategory_category_id = data.get('subcategory_category_id')
            db.session.commit()
            return {'message': 'Subcategory updated successfully'}
        except Exception as ex:
            db.session.rollback()
            return {'error': str(ex)}, 500

    def delete(self, subcategory_id):
        try:
            subcategory_vo = SubCategoryVO.query.get(subcategory_id)
            if not subcategory_vo:
                return {'message': 'Subcategory not found'}, 404
            db.session.delete(subcategory_vo)
            db.session.commit()
            return {'message': 'Subcategory deleted successfully'}

        except Exception as ex:
            db.session.rollback()
            return {'error': str(ex)}, 500





