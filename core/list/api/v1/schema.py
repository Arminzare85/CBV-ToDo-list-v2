from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def openapi_schema(request):

    schema = {
        "openapi": "3.0.0",

        "info": {
            "title": "Todo List API",
            "version": "1.0.0",
            "description": "API documentation for Todo List"
        },

        "paths": {

            "/todo/api/v1/task/": {

                "get": {
                    "summary": "List all tasks",
                    "responses": {
                        "200": {
                            "description": "List of tasks"
                        }
                    }
                },

                "post": {
                    "summary": "Create a task",
                    "responses": {
                        "201": {
                            "description": "Task created"
                        }
                    }
                }
            },

            "/todo/api/v1/task/{id}/": {

                "get": {
                    "summary": "Retrieve a task"
                },

                "put": {
                    "summary": "Update a task"
                },

                "patch": {
                    "summary": "Partially update a task"
                },

                "delete": {
                    "summary": "Delete a task"
                }
            }
        }
    }

    return Response(schema)