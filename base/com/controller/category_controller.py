from flask import request
from flask_restful import Resource
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO


class CategoryResource(Resource):
    def get(self, category_id=None):
        try:
            category_dao = CategoryDAO()

            # If category_id is provided, fetch a specific category
            if category_id:
                category_vo = category_dao.get_category_by_id(category_id)
                if category_vo:
                    return category_vo.serialize(), 200
                else:
                    return {'message': 'Category not found'}, 404
            else:
                # If no category_id provided, fetch all categories
                category_vo_list = category_dao.view_category()
                return [category.serialize() for category in category_vo_list], 200
        except Exception as e:
            return {'message': 'Error occurred while processing your request: {}'.format(str(e))}, 500

    def post(self):
        try:
            data = request.get_json()
            category_name = data.get('category_name')
            category_description = data.get('category_description')

            category_vo = CategoryVO(category_name=category_name, category_description=category_description)
            category_dao = CategoryDAO()
            category_dao.insert_category(category_vo)
            return {'message': 'Category added successfully'}, 201
        except Exception as e:
            return {'message': 'Error occurred while processing your request: {}'.format(str(e))}, 500

    def put(self, category_id):
        try:
            data = request.get_json()
            category_name = data.get('category_name')
            category_description = data.get('category_description')

            category_dao = CategoryDAO()
            category_vo = category_dao.get_category_by_id(category_id)
            if not category_vo:
                return {'message': 'Category not found'}, 404

            category_vo.category_name = category_name
            category_vo.category_description = category_description
            category_dao.update_category(category_vo)
            return {'message': 'Category updated successfully'}, 200
        except Exception as e:
            return {'message': 'Error occurred while processing your request: {}'.format(str(e))}, 500

    def delete(self, category_id):
        try:
            category_dao = CategoryDAO()
            category_vo = category_dao.get_category_by_id(category_id)
            if not category_vo:
                return {'message': 'Category not found'}, 404
            category_dao.delete_category(category_vo)
            return {'message': 'Category deleted successfully'}, 200
        except Exception as e:
            return {'message': 'Error occurred while processing your request: {}'.format(str(e))}, 500
