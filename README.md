# Instawork Assignment

## Running the project

The simplest way to get this project would be using docker-compose. Simply run `docker-compose up --build` and the API server should be up.

If you wish to run the project locally, copy the `.env.sample` file to `.env`, replace the MYSQL env variables with your local MySQL instance details, run `python manage.py migrate` to run the migrations, and finally run `python manage.py runserver` to run the service

## APIs

There are 2 APIs available:

1. A list API at `/api/v1/team/` which allows you to view all the members and create a new member
   - Send a GET request to view all the stored members.
     ```shell
     curl -XGET 'http://localhost:8000/api/v1/team/'
     ```
   - Send a POST request with JSON parameters to create a new member. The request accepts `first_name`, `last_name`, `phone_number`, `email` and `role` fields
     ```shell
     curl -XPOST -H "Content-type: application/json" -d '{"first_name":"First","last_name":"Name","phone_number":"9876543210"}' 'http://localhost:8000/api/v1/team/'
     ```
2. A detail API at `/api/v1/team/<member_id>` that allows you to view a particular member at the provided ID, update the member partially and delete the member
   - Send a GET request to view the member details
     ```shell
     curl -XGET 'http://localhost:8000/api/v1/team/244a3c82-1828-4c54-844d-37fc0ba4e5c7/'
     ```
   - Send a PUT request to update the member
     ```shell
     curl -XPUT -H "Content-type: application/json" -d '{"phone_number":"9876543210"}' 'http://localhost:8000/api/v1/team/244a3c82-1828-4c54-844d-37fc0ba4e5c7/'
     ```
   - Send a DELETE request to delete the member entirely
     ```shell
     curl -XDELETE 'http://localhost:8000/api/v1/team/244a3c82-1828-4c54-844d-37fc0ba4e5c7/'
     ```
