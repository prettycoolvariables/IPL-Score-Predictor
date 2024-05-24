
# IPL Score Predictor

Welcome to the IPL Score Predictor project! This project is aimed at predicting the total runs scored by a team in an IPL cricket match based on various factors such as venue, innings, current score, current wickets, batting team, and bowling team. The prediction model utilizes machine learning techniques to provide accurate estimates.

## Project Overview

In this project, we've developed a web application using Flask, a lightweight WSGI web application framework, to host the IPL Score Predictor. Users can access the application through a web browser and input relevant match details to obtain a predicted total score.

## Getting Started

To run the IPL Score Predictor locally on your machine, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/prettycoolvariables/IPL-Score-Predictor.git
```

2. Navigate to the project directory:

```bash
cd IPL-Score-Predictor
```

3. Install the required dependencies. It's recommended to use a virtual environment:

```bash
pip install -r requirements.txt
```

4. Run the Flask application:

```bash
python app.py
```

5. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. **Homepage**: Upon accessing the application, you'll be directed to the homepage where you can proceed with match prediction.

2. **Match Prediction**: Navigate to the prediction page where you can input match details such as venue, innings, current ball, batting team, bowling team, current score, and current wickets. Click on the predict button to get the predicted total score.

3. **User Authentication**: Users can create an account by providing necessary details such as first name, last name, username, email, and password. Existing users can log in using their credentials.

4. **Logout**: Users can securely log out of their accounts.

## Deployment

The IPL Score Predictor application is deployed on Microsoft Azure using Azure App Service. Continuous Integration and Continuous Deployment (CI/CD) are implemented using GitHub Actions. The live version of the application is accessible at [IPL Score Predictor](https://miniproject-iplscorepredictor.azurewebsites.net).

## Repository Structure

- **app.py**: Flask application script containing routes and prediction logic.
- **templates/**: Directory containing HTML templates for different pages.
- **model.pkl**: Pickled machine learning model for predicting total runs.
- **requirements.txt**: File containing project dependencies.
- **2013-2022_cleaned.csv**: Dataset used for model training.
- **README.md**: Project documentation.



Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
