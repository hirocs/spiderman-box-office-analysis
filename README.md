# 🕷️ Spider-Man Box Office Analysis

A data science and machine learning project analyzing the box office performance of Spider-Man movies.

This project explores how factors such as budget, opening weekend revenue, IMDb rating, Rotten Tomatoes score, and runtime relate to worldwide box office revenue. It also demonstrates a complete machine learning workflow using Linear Regression to predict the performance of a hypothetical Spider-Man movie.

## Objectives

- Analyze Spider-Man movie data using Python and Pandas
- Visualize relationships between movie features and worldwide revenue
- Build and evaluate a Linear Regression model
- Predict the worldwide revenue of a hypothetical Spider-Man movie
- Interpret model performance and discuss its limitations

## Dataset

The dataset contains information for 10 Spider-Man movies released between 2002 and 2023.

### Features

- Movie
- Release Year
- Character
- Budget (USD Millions)
- Opening Weekend (USD Millions)
- Worldwide Box Office (USD Millions)
- IMDb Rating
- Rotten Tomatoes Score
- Runtime (minutes)

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Git
- GitHub

## Data Visualization

The project includes several visualizations to better understand the dataset.

### Worldwide Box Office Revenue

- Bar chart comparing the worldwide revenue of all Spider-Man movies.

### Budget vs Worldwide Revenue

- Scatter plot showing the relationship between production budget and worldwide box office revenue.

### Key Finding

The scatter plot shows that a higher production budget does **not necessarily** result in higher worldwide box office revenue.

## Machine Learning

A Linear Regression model was built using Scikit-learn to predict worldwide box office revenue.

### Features (X)

The model was trained using the following features:

- Budget
- Opening Weekend Revenue
- IMDb Rating
- Rotten Tomatoes Score
- Runtime

### Target (y)

- Worldwide Box Office Revenue

### Machine Learning Workflow

1. Load the dataset with Pandas
2. Select features (X) and target (y)
3. Split the dataset into training and testing sets
4. Train a Linear Regression model
5. Make predictions on the test set
6. Evaluate the model using MAE and R² Score
7. Predict the revenue of a hypothetical Spider-Man movie
8. Compare the prediction with existing Spider-Man movies

### Model Evaluation

The model produced the following results:

- Mean Absolute Error (MAE): **1018.64**
- R² Score: **-4.16**

Although the model successfully completed the machine learning workflow, its predictions were not reliable because the dataset contains only 10 movies.

### Prediction Example

The model predicted the worldwide revenue of a hypothetical Spider-Man movie using the following input:

| Feature | Value |
|---------|------:|
| Budget | 250 |
| Opening Weekend | 180 |
| IMDb | 8.7 |
| Rotten Tomatoes | 95 |
| Runtime | 145 |

The predicted worldwide revenue was **-661.01 million USD**, which is not realistic.

This demonstrates an important machine learning concept: a model can successfully train and make predictions while still producing poor results if the training dataset is too small.

## Project Structure

## Project Structure

```text
spiderman-box-office-analysis/
│
├── main.py                     # Data analysis and visualization
├── machine_learning.py         # Linear Regression model
├── spiderman_movies.csv        # Dataset
├── worldwide_box_office.png    # Bar chart
├── budget_vs_worldwide.png     # Scatter plot
├── requirements.txt            # Python dependencies
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/hirocs/spiderman-box-office-analysis.git
```

Move into the project directory:

```bash
cd spiderman-box-office-analysis
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the data analysis:

```bash
python main.py
```

Run the machine learning model:

```bash
python machine_learning.py
```

## Future Improvements

This project can be improved by:

- Expanding the dataset to include more superhero or Marvel movies
- Testing additional machine learning algorithms such as Decision Trees or Random Forests
- Performing feature engineering
- Predicting upcoming movie performance using only features available before release
- Deploying the project as an interactive web application

## Lessons Learned

Through this project, I learned how to:

- Analyze datasets using Pandas
- Create visualizations with Matplotlib
- Prepare data for machine learning
- Train and evaluate a Linear Regression model
- Interpret model coefficients and evaluation metrics
- Use Git and GitHub for version control
- Document a complete data science project