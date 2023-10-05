from base import app
from base.com.controller.category_controller import CategoryResource
from flask_restful import Api
if __name__ == "__main__":
    api = Api(app)
    api.add_resource(CategoryResource, '/categories', '/categories/<int:category_id>')
    app.run(debug=True, threaded=True, host='localhost', port=5000)

