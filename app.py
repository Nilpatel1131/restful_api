# Import necessary modules and classes
from base import app  # Assuming 'app' is your Flask application instance
from base.com.controller.category_controller import CategoryResource
from base.com.controller.subcategory_controller import SubcategoryResource
from flask_restful import Api

# Check if the script is being run directly
if __name__ == "__main__":
    # Create an instance of Flask-RESTful Api with your Flask application
    api = Api(app)

    # Add CategoryResource to handle routes related to categories
    api.add_resource(CategoryResource, '/categories', '/categories/<int:category_id>')

    # Add SubcategoryResource to handle routes related to subcategories
    api.add_resource(SubcategoryResource, '/subcategories', '/subcategories/<int:subcategory_id>')

    # Run the Flask application
    app.run(debug=True, threaded=True, host='localhost', port=5000)
