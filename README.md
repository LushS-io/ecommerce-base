# Getting Started with Flask on Azure App Service

This is a simple Flask app that can be deployed to Azure App Service. It is meant to be used as a starting point for building your own Flask apps that can be deployed to Azure.

## Developer Documentation: Getting Started

### Prerequisites

- Python 3.10.9+ installed on your machine *(lower versions may work but are not tested)*
- Git installed on your machine
- Visual Studio Code installed on your machine

### Setup

1. Clone the repository to your local machine using Git.
2. Open the cloned repository in Visual Studio Code.
3. Create a Python virtual environment at the root of the project by running the following command in the terminal:

   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment by running the following command in the terminal:

   ```shell
   source venv/bin/activate
   ```

5. Install the required packages by running the following command in the terminal:

   ```shell
   pip install -r requirements.txt
   ```

6. Create a `.env` file at the root of the project and add the following line:

   ```shell
   ENV=development
   ```

Sure! Here's the updated section with the revised instructions for toggling the debug mode:

### Running the App Locally

1. Open the `.vscode/launch.json` file included in the project.
2. In the `configurations` section, you will find a configuration named `Flask: App (Local)`. This configuration is already set up to run the Flask app locally.
3. To enable the debug mode and see debug information on the UI, make sure the `noDebug` option in the `launch.json` file is set to `false`.
4. To disable the debug mode and not see debug information on the UI, you can comment out the `args` key in the `Flask: App (Local)` configuration by adding `//` before the line.
5. Click on the "Run and Debug" button in Visual Studio Code (or press `F5`) to start the app.
6. Open your web browser and navigate to `http://localhost:5000` to access the app.

Note: Make sure the virtual environment is activated before running the app locally.

### Viewing the Local Database

1. The Flask app uses a local database instance for storing data.
2. To view the contents of the local database, you can use the recommended extensions for Visual Studio Code located in `.vscode/extensions.json`.
3. Once the extension is installed, you can connect to the local database instance and view its contents directly within Visual Studio Code.

Note: The specific steps for connecting to and viewing the local database may vary depending on the extension you choose. Please refer to the documentation of the extension for detailed instructions.

### Project Structure Details

The project structure for the Flask app is as follows:

```tree
flask_api
├─ .deployment
├─ .gitignore
├─ .vscode
│  ├─ extensions.json
│  ├─ launch.json
│  └─ settings.json
├─ app.py
├─ config.py
├─ extensions.py
├─ instance
│  └─ app.db
├─ modules
│  ├─ __init__.py
│  ├─ forms.py
│  ├─ loginManager.py
│  ├─ models.py
│  └─ routes.py
├─ requirements.txt
├─ run.py
├─ startup.txt
├─ templates
│  ├─ base.html
│  ├─ homepage.html
│  ├─ index.html
│  ├─ login.html
│  └─ register.html
└─ tests
   ├─ __init__.py
   └─ test_routes.py
```

Here is a breakdown of the different directories and files in the project:

- `.deployment`: Contains deployment-specific configuration files for Azure App Service.
- `.gitignore`: Specifies files and directories that should be ignored by Git version control.
- `.vscode`: Contains configuration files for Visual Studio Code IDE.
  - `extensions.json`: Lists recommended extensions for the project.
  - `launch.json`: Configures the launch configurations for running the app locally.
  - `settings.json`: Customizes the settings for the Visual Studio Code workspace.
- `app.py`: The main entry point of the Flask application.
- `config.py`: Contains configuration settings for the Flask app.
- `extensions.py`: Initializes and configures Flask extensions used in the app.
- `instance`: Directory for storing instance-specific data (e.g., local database file).
- `modules`: Directory for organizing different modules of the Flask app.
  - `__init__.py`: Initializes the Flask module.
  - `forms.py`: Defines forms used in the app.
  - `loginManager.py`: Configures the login manager for user authentication.
  - `models.py`: Defines the database models for the app.
  - `routes.py`: Defines the routes and corresponding view functions for the app.
- `requirements.txt`: Lists the required Python packages and their versions.
- `run.py`: A script to run the Flask app.
- `startup.txt`: Contains instructions or notes for setting up and running the app.
- `templates`: Directory for storing HTML templates used in the app.
- `tests`: Directory for storing unit tests for the app.

This project structure follows common conventions for organizing a Flask application, separating concerns into different modules and directories.

That's the overview of the project structure. It provides a clear separation of concerns and makes it easier to navigate and maintain the Flask app codebase.
