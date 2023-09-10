# Shoe Slug Monitor

![Python](https://img.shields.io/badge/Python-3.9.0-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

This Python script monitors Nike shoe slugs for changes and sends notifications to a Discord channel when differences are detected. It's designed to help you stay updated on new Nike shoe releases.

## Prerequisites

- Python 3.9.0 or higher

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/monera023/SlugMonitor.git
   cd SlugMonitor
2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt

4. Update the Discord webhook URL in `slug-monitor.py`.

5. Run the script:
   The script will start monitoring Nike shoe slugs and send notifications to Discord when differences are found.
  ```bash
  python slugMonitor.py
  ```    


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Thanks to DiscordWebhook for the Discord integration.

## Contributing
Contributions are welcome! Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

Support
For support or questions, please create an issue in this repository.