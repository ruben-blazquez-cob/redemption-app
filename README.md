# Code Generator App

This project consists of two main components: a Firestore script for adding and changing the status of codes in the database, and a web application designed for deployment to Google Cloud Run.

## Project Structure

- `/firestore`: Contains scripts to interact with Firestore for adding and updating codes in the database.
- `/web app`: Contains the Flask web application intended for deployment to Google Cloud Run.

## Firestore Usage

The `/firestore` directory includes Python scripts to interact with Google Cloud Firestore. These scripts are used to add new codes to the database and update their statuses.

## Web Application

The web application in the `/web-app` directory is a Flask-based application that can be containerized and deployed to Google Cloud Run.

### Building the Container

To build the Docker container for the web application, follow these steps:

1. Navigate to the `/web-app` directory.
2. Build the Docker image using the following command:

    ```sh
    docker build -t gcr.io/[PROJECT-ID]/[IMAGE-NAME] .
    ```

    Replace `[PROJECT-ID]` with your Google Cloud project ID and `[IMAGE-NAME]` with a name for your Docker image.

### Deploying to Google Cloud Run

After building your Docker image, deploy it to Google Cloud Run:

1. Submit the Docker image to Google Container Registry:

    ```sh
    gcloud builds submit --tag gcr.io/[PROJECT-ID]/[IMAGE-NAME]
    ```

2. Deploy the image to Cloud Run:

    ```sh
    gcloud run deploy --image gcr.io/[PROJECT-ID]/[IMAGE-NAME] --platform managed
    ```

    Follow the prompts to specify the service name, region, and other configurations.

