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
  
- Run unittest in app folder:
  ```sh
    ./run_tests.sh
  ```