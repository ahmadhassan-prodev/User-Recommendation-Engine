# User Recommendation Engine

A simple Python-based recommendation system that suggests **"People You May Know"** and **"Pages You Might Like"** using basic graph traversal and collaborative filtering concepts.

## Overview

This repository demonstrates a lightweight **social recommendation engine** built from scratch in Python. It uses sample user data (friends list and liked pages) to generate personalized suggestions:

- **Friend recommendations** (mutual friends logic)
- **Page recommendations** (based on users with similar interests)

Perfect for learning basic recommendation algorithms, data processing with JSON, and social network concepts.

## Repository Purpose

This is a **learning / practice project** focused on:
- Implementing simple recommendation logic
- Working with graph-like relationships (friends)
- Data cleaning and preprocessing
- Collaborative filtering fundamentals

## Key Features

- **Data Cleaning**: Removes invalid entries and duplicates
- **People You May Know**: Suggests friends based on mutual connections
- **Pages You Might Like**: Recommends pages based on shared interests
- **JSON-based Data Store**: Easy to read, modify, and extend

## Technologies Used

- **Python 3**
- **JSON** (standard library)
- No external dependencies

## Project Structure

```bash
User-Recommendation-Engine/
├── codebook_data.json           # Original sample dataset
├── codebook_data_2.json         # Cleaned dataset (generated)
├── clean_data.py                # Data cleaning and preprocessing
├── load_data.py                 # Load and display data
├── people_you_may_know.py       # Friend recommendation logic
├── pages_you_might_like.py      # Page recommendation logic
├── README.md
└── .gitignore
```

**How It Works**

**1\. Data Loading & Cleaning (clean_data.py)**

- Filters users with valid names
- Removes duplicate friends
- Keeps only active users (with friends or liked pages)
- Removes duplicate pages

**2\. Friend Recommendations (people_you_may_know.py)**

- Builds a friend network using sets for fast lookup
- For each user, finds friends-of-friends who are not already connected
- Suggests potential new connections

**3\. Page Recommendations (pages_you_might_like.py)**

- Identifies users who share common liked pages
- Recommends other pages liked by similar users
- Excludes pages the user has already liked

**Usage**

**1\. Clone the repository**

Bash

git clone <https://github.com/ahmadhassan-prodev/User-Recommendation-Engine.git>

cd User-Recommendation-Engine

**2\. Run the scripts**

**Clean the data:**

Bash

python clean_data.py

**View the dataset:**

Bash

python load_data.py

**Get friend suggestions:**

Bash

python people_you_may_know.py

**Get page suggestions:**

Bash

python pages_you_might_like.py

**Sample Output**

**People You May Know:**

text

User ID: 1 Suggested friends: {4}

User ID: 2 Suggested friends: {3}

**Pages You Might Like:**

text

User ID: 1 Suggested_pages: \[102, 103\]

**Learning Outcomes**

By studying this project, you will learn:

- How to model social relationships using Python dictionaries and sets
- Basic collaborative filtering techniques
- Data validation and cleaning strategies
- Implementing recommendation logic without machine learning libraries
- Working with JSON datasets

**Future Improvements**

- Add user input to generate recommendations for a specific user
- Implement scoring/ranking for suggestions (e.g., by number of mutual friends)
- Add a simple CLI interface
- Extend to content-based filtering using page descriptions
- Integrate with a database (SQLite)
- Add visualization of the social graph

**Contributing**

Feel free to fork this repository and enhance the recommendation logic or add new features!
