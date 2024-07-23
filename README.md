---
# Caktus Django Coding Exercise

## Overview

This project is a crossword drill exercise program built using Django. It presents clues to users and accepts guesses for answers, tracking the number of clues offered and correctly answered. The project includes fixtures with realistic crossword puzzle data and features two main views for drilling and answering clues.

## Project Requirements

### Data Models

The project includes three main models:

- **Puzzle:** Represents a published crossword puzzle.
  - `title`: Optional, max length 255 characters
  - `date`: Required, publication date
  - `byline`: Required, max length 255 characters
  - `publisher`: Required, max length 12 characters

- **Entry:** Represents a crossword entry.
  - `entry_text`: Required, unique, max length 50 characters

- **Clue:** Represents a clue for an entry in a puzzle.
  - `entry`: ForeignKey reference to `Entry`
  - `puzzle`: ForeignKey reference to `Puzzle`
  - `clue_text`: Required, max length 512 characters
  - `theme`: Boolean, default `False` (not used in the project but included in the fixtures)

### Views

- **Drill View:** Displays a random clue and allows users to input guesses. Incorrect guesses re-display the clue with an error message, while correct guesses redirect to the Answer View. Provides an "escape hatch" link to reveal the answer.

- **Answer View:** Congratulates the user on a correct guess and provides additional information about the clue, including a count of occurrences if the clue appears more than once.

## API Endpoints

### Drill View

**Endpoint:** `/drill/`

**Method:** GET

**Description:** Displays a random clue and a form for users to submit their guesses.

**Response:**

- **200 OK**: The page includes a clue and a form to submit answers.

**Errors:**

- **400 Bad Request**: When the form submission is missing required fields.

### Drill View - Post Answer

**Endpoint:** `/drill/`

**Method:** POST

**Description:** Accepts the answer for the clue provided on the GET request.

**Request Parameters:**

- `clue_id`: ID of the clue being answered
- `answer`: User's answer

**Response:**

- **200 OK**: Displays the clue again with an error message if the answer is incorrect, or redirects to the Answer View if the answer is correct.

**Example Request:**

```bash
curl -X POST -d "clue_id=1&answer=apple" http://127.0.0.1:8000/drill/
```

### Answer View

**Endpoint:** `/answer/<int:pk>/`

**Method:** GET

**Description:** Displays the result of the user's guess, including statistics about the clue and its occurrences.

**Response:**

- **200 OK**: Shows the clue's answer, occurrence statistics, and additional information.

**Errors:**

- **404 Not Found**: When the clue ID does not exist.

## Directory Structure

```
/home/dev/Documents/tdd_exercise_internal-0.1.1/
│
├── xword_data/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── tests/
│   │   ├── factories.py
│   │   ├── test_models.py
│   │   └── test_views.py
│   └── urls.py
│
├── tdd_exercise/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── templates/
│       ├── base.html
│       ├── answer.html
│       └── drill.html
│
├── fixtures/
│   └── xword_data.json
│
├── manage.py
├── requirements.txt
├── README.md
└── venv/

```

## Setup and Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Django

### Installation

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd tdd_exercise_internal-0.1.1
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Load Fixtures**

   ```bash
   python manage.py loaddata fixtures/xword_data.json
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

## Testing

To run the tests, use the following command:

```bash
python manage.py test
```

The tests include checks for models and views using `factory_boy` for test data and `beautifulsoup4` for HTML parsing.

## Contribution

Contributions are welcome! To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## Conclusion

This project provides a foundational framework for a crossword drill exercise, showcasing basic Django features such as models, views, and fixtures. It includes essential functionalities for presenting clues, accepting guesses, and providing feedback. Feel free to enhance and customize the project according to your needs, and contribute to its development by following the guidelines provided.
---
