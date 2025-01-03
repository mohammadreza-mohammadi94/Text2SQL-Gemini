# Text-to-SQL Query Generator with Gemini

This project is a web application that utilizes the power of Google's Gemini model to convert natural language questions into SQL queries. The application retrieves data from a SQLite database based on user queries. It's built using **Streamlit** for the frontend, **Google Gemini** for natural language processing, and **SQLite** as the database.

## Features

- Convert English natural language questions into SQL queries.
- Execute the SQL queries on a SQLite database and display the results.
- Display results as a DataFrame or a single value (e.g., AVG, COUNT).
- Easy-to-use web interface for querying the database.

## Technologies Used

- **Streamlit**: For building the web application interface.
- **Google Gemini API**: For converting natural language questions into SQL queries.
- **SQLite**: For storing and retrieving student records.
- **Pandas**: For displaying SQL query results in a user-friendly format.

## Setup Instructions

To run this project locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Text-to-SQL-Query-Generator.git
cd Text-to-SQL-Query-Generator
```

### 2. Install required dependencies

Create a virtual environment and activate it, then install the required libraries using the following commands:

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
# For Windows
venv\Scripts\activate
# For Mac/Linux
source venv/bin/activate

# Install the required libraries
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root directory of the project and add the following environment variables:

```bash
DATABASE_URL=student.db
GENAI_API_KEY=your_google_gemini_api_key
```

Replace `your_google_gemini_api_key` with your actual Google Gemini API key.

### 4. Running the App

After setting up the environment, run the Streamlit application using the following command:

```bash
streamlit run app.py
```

This will start the Streamlit app locally, and you can access it by opening a browser and going to:

```
http://localhost:8501
```

### 5. Database Setup

Ensure you have the SQLite database file `student.db` with the appropriate data in the same directory as `app.py` or set up the database according to your needs. You can use the provided `sql.py` script to create the database and insert sample data.

## Sample Queries

Here are some examples of questions you can ask in the app:

- "How many students are there in the database?"
- "What are the names of students studying Data Science?"
- "What is the average marks of students?"

## Project Structure

```
Text-to-SQL-Query-Generator/
│
├── app.py              # Streamlit app that interacts with the user and runs the query
├── sql.py              # Script for setting up the SQLite database and inserting data
├── requirements.txt    # Python dependencies for the project
├── .env                # Environment variables (GENAI_API_KEY, DATABASE_URL)
└── README.md           # Project documentation
```

## Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes. Ensure you follow the project structure and add appropriate tests for new features.

## License

This project is licensed under the MIT License.
