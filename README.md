# Budget


## Project Description

A sophisticated budgeting platform using Flask, Python, SQL, JavaScript, PostgreSQL, HTML, and CSS. The application boasts a user-friendly interface with dynamic containers that empower users to effortlessly monitor, analyze, and manage their financial activities in real-time.

### Key Features:
- **Default Expense Categories:** Includes pre-defined or base expense categories.
- **Custom Expenses:** Allows users to create and manage their custom expenses tailored to their financial needs.
- **Dynamic Div Rendering:** Dynamically generates divs for both default and custom expenses, ensuring a flexible and responsive interface.


## Installation Instructions

1. Clone the repository:
- https://github.com/Alex-Merkel/Budget.git:
- cd Budget

2. Install the required Python libraries:
- pip install -r requirements.txt

3. Set up and configure your PostgreSQL database.


## Usage

### Backend (Flask):

**Start the Flask Server within a Virtual Environment:**

   - First, create and activate a virtual environment:
     ```
     python -m venv venv
     source venv/bin/activate   # For Unix/macOS
     .\venv\Scripts\activate    # For Windows
     ```
   
   - Install required dependencies if not installed:
     ```
     pip install -r requirements.txt
     ```
   
   - Start the Flask server:
     ```
     flask run
     ```

**To effectively use the budgeting platform, follow these steps:**

1. Sign In or Sign Up:
- If you're a new user, sign up by submitting your user details. After registration, log in using your credentials. For existing users, log in using your credentials.

2. Navigate to the 'Budget' Page:
- Upon successful login, navigate to the 'Budget' page within the application.

3. Add Expenses:
- Begin by adding expenses for the default fields. Input your expenses for various categories provided.

4. Customize Expenses:
- To add a custom expense under a specific category, select the 'Add Expense' option below the respective category.

5. Reset Data (Optional):
- If you wish to reset all data, including deleting custom expense categories and resetting default expenses to zero, use the 'Reset' button located at the bottom of the page.


## Configuration

### Database Configuration using Environment Variables:

This project uses environment variables to manage sensitive information, such as database credentials, without exposing them in the repository. To configure your database connection:

1. Create a `.env` file in the root directory of the project (if not already present).

2. Add the following line to the `.env` file and replace 'YOUR_DATABASE_URI' with your actual database connection URI:
DATABASE_URI=YOUR_DATABASE_URI

2. Obtain your database connection URI, typically in the format:
   postgresql://username:password@hostname:port/database_name

3. Ensure that the `.env` file is included in the project's `.gitignore` to prevent it from being committed to the repository.

4. In your Flask application, reference the environment variable for the database configuration, for example:

### Load environment variables
from dotenv import load_dotenv

### Load variables from .env file
load_dotenv()

### Use the environment variable for the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')


## Contributing

### Bug Reports:

If you stumble upon a bug, I'd love to hear about it! Please open an issue and include detailed steps to help me reproduce the bug. Your input is incredibly valuable in improving this application.

### Feature Suggestions:

Excited about a new feature idea? Don't hesitate to share it with me by opening an issue! Your clear description of the proposed feature helps me understand your needs better.

### Note for Contributors:
I welcome and appreciate your contributions! While this project maintains its codebase, your suggestions and improvements are integral to its growth. Please feel free to suggest enhancements and report issues. However, any code modifications require explicit permission.

Thank you for being a part of this project's journey to improvement and excellence!


## License

This project is licensed under the MIT License. While this license allows users to report issues and suggest enhancements, it does not grant permissions to modify or distribute the codebase without explicit permission.


## Contact

For inquiries or suggestions, feel free to reach out:
- **Email:** alexander.j.merkel@gmail.com
- **GitHub:** [GitHub](https://github.com/Alex-Merkel)
- **LinkedIn:** [LinkedIn](https://www.linkedin.com/in/alex-merkel-8750b0274/)
