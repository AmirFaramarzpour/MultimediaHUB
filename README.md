```markdown
# File Hosting Server Management

This project is a file hosting server management tool. It allows users to start and stop a file hosting service, manage user accounts, and list connected devices. It also includes a web-based file hosting service built with Flask.

## Features

- Start and stop the file hosting service
- Manage user accounts (add, remove, list users)
- List connected devices
- Web-based interface for browsing and downloading files

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/AmirFaramarzpour/MultimediaHUB.git
   cd MultimediaHUB.git
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Start the main application:
   ```sh
   python app.py
   ```

2. Follow the on-screen instructions to manage the file hosting service.

3. Access the web-based file hosting service by navigating to `http://localhost:5000` in your web browser.
4. You can connect Ngrok authtoken and account to tunnel localhost:5000 address.

## File Structure

- `app.py`: Main application file for managing the file hosting service and user accounts.
- `server.py`: Flask web server for the file hosting service.
- `users.json`: JSON file for storing user accounts.
- `templates/`: Directory containing HTML templates for the web interface (Front-end).

## License

This project is licensed under the MIT License.
```

Next, here's the `requirements.txt` file for your project:

```txt
Flask
```

