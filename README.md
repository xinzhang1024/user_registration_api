- Set environment variable:
  - Linux:
      ```sh
      export ENV="dev"
      ```
  - Windows:
      ```sh
      set ENV=dev
      ```

- Build the app by running this command:
    ```sh
    docker-compose up --build -d
    ```
  
- Test in container:
    ```sh
    curl -X GET http://127.0.0.1:8000
    ```

- Test on local browser:
    ```sh
    http://127.0.0.1:80
    ```
    or
    ```sh
    http://localhost
    ```
  
- Openapi:
  ```sh
  http://localhost/docs
  ```

- How to test
  1. with path /register and method POST to register user,
     enter email and password, a 4 digits code will be printed in console.
  2. with path /email_validation/{code} and method GET to verify in 1 minute,
     enter code, and email, password under basic auth.