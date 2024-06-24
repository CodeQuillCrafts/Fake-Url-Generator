# Fake URL Generator

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Important Notice](#important-notice)
* [Contributing](#contributing)
* [License](#license)

## Overview

The Fake URL Generator is a simple Django web application that allows users to input a URL and receive a fake version. This Fake URL redirects to the original URL when accessed. This project is intended for educational purposes and fun, and not to be used for any malicious activities.

## Features

* Input a URL to generate a fake version.
* Unique Fake URLs to prevent conflicts.
* Simple and intuitive interface.
* Handles redirection to the original URL.

## Requirements

* Python
* Pip
* Django

## Installation

1. __Create and activate a virtual environment__:
   ```md
   python -m venv venv
   venv\Scripts
   activate
   ```

2. __Clone the repository__:
   ```md
   git clone https://github.com/CodeQuillCrafts/Fake-Url-Generator
   cd Fake-Url-Generator
   ```

3. __Install the required packages__:
   ```md
   pip install -r requirements.txt
   ```

4. __Run the Django development server__:
   ```md
   python manage.py runserver
   ```

5. __Access the application__:
   Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

### Generating a Shortened URL

1. Enter a URL in the provided input field.
2. Click the "Generate Url" button.
3. The Fake URL will be displayed, and you can use it to redirect to the original URL.

### Redirecting

When you access the URL, it will redirect you to the original URL.

## Important Notice

This project is created for fun and educational purposes only. It is not intended to be used for any malicious activities or to harm anyone. Use it responsibly.

## Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request. We welcome all improvements and suggestions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
