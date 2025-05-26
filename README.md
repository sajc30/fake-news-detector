# AI Fake News Detector

## Project Overview

This project is an AI-powered full-stack application designed to detect misleading or false news articles by analyzing text content. The primary goal is to combat the spread of misinformation by providing users with a tool to assess the credibility of news articles. This version focuses on analyzing general news articles written in English.

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Live Demo Link](#live-demo-link)
- [Screenshots](#screenshots)
- [Data Sources](#data-sources)
- [Installation and Setup](#installation-and-setup)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Model Details](#model-details)
- [Testing](#testing)
- [Ethical Considerations](#ethical-considerations)
- [Future Improvements](#future-improvements)
- [Author](#author)
- [License](#license)

## Tech Stack

### Frontend
- **Framework:** React.js
- **Styling:** Tailwind CSS
- **State Management:** (To be decided - e.g., Context API, Redux Toolkit)
- **HTTP Client:** Axios (or Fetch API)

### Backend
- **Framework:** Python with Flask
- **AI/ML Libraries:**
    - Hugging Face Transformers (for models like BERT/RoBERTa)
    - PyTorch (as the backend for Hugging Face models)
- **Data Handling:** Pandas, NumPy
- **NLP Preprocessing:** NLTK (for initial text cleaning, if needed beyond tokenizer capabilities)

### Database
- **Type:** NoSQL
- **Database:** MongoDB (for storing article analysis results, user feedback, logs)

### DevOps & Deployment
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Cloud Platform:** Amazon Web Services (AWS) - (Specific services like EC2, S3, ECS/EKS, Lambda, API Gateway to be determined based on architecture)

### Version Control
- **System:** Git
- **Platform:** GitHub

## Features

*(You will fill this section out as you develop the features. Examples:)*
-   User-friendly interface for submitting news article text.
-   AI-powered analysis providing a prediction (e.g., "Likely Real," "Likely Fake").
-   Display of confidence score for the prediction.
-   (Optional) User feedback mechanism for predictions.
-   (Optional) History of analyzed articles for registered users.

## Live Demo Link

*(Once deployed, you'll add the link here)*
-   **Application URL:** [To be added]

## Screenshots

*(After developing the UI, add screenshots here to showcase your application)*
-   [Screenshot of the main analysis page]
-   [Screenshot of results display]

## Data Sources

*(After you select and explore your dataset(s), update this section)*
-   **Dataset Name(s):** [To be added - e.g., "Kaggle Fake News Corpus"]
-   **Source:** [Link to where the dataset can be found - e.g., Kaggle URL]
-   **Description:** Briefly describe the dataset, including the types of articles, number of samples, and label distribution (e.g., "Contains X articles with 'title', 'text', and 'label' columns. Labels are 0 for fake, 1 for real. Approximately Y% fake news.").
-   **Preprocessing Steps:** Briefly mention key preprocessing steps (e.g., "Lowercasing, removal of URLs and special characters, tokenization using Hugging Face BERT tokenizer").

## Installation and Setup

### Prerequisites
-   Python (3.8+)
-   Node.js (LTS version recommended) & npm
-   Git
-   Docker (Recommended for easier setup and deployment)
-   AWS Account & AWS CLI (for deployment)
-   MongoDB (running locally or on a cloud service like MongoDB Atlas)

### Backend Setup

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <your-repo-url>
    cd fake-news-detector/backend
    ```
2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```
3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up environment variables:**
    Create a `.env` file in the `backend` directory (this file should be in `.gitignore`).
    Add necessary environment variables (e.g., `DATABASE_URL`, `SECRET_KEY` - will be defined later).
    ```
    # backend/.env example
    FLASK_APP=app.py
    FLASK_ENV=development
    # Add other variables as needed
    ```
5.  **Run the Flask development server:**
    ```bash
    flask run
    ```
    The backend should be running on `http://127.0.0.1:5000/`.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    # from project root
    cd frontend
    ```
2.  **Install Node.js dependencies:**
    ```bash
    npm install
    ```
3.  **Start the React development server:**
    ```bash
    npm start
    ```
    The frontend should be running on `http://localhost:3000/` and will open in your browser.

## Usage

*(Once the application is functional, explain how a user interacts with it)*
1.  Open the application in your web browser.
2.  Navigate to the analysis page.
3.  Paste the news article text into the input field.
4.  Click the "Analyze" button.
5.  View the prediction result and confidence score.

## Model Details

*(After training and selecting your model, fill this in)*
-   **Model Architecture:** [e.g., Fine-tuned BERT (bert-base-uncased) with a sequential classification head]
-   **Training Data:** [Brief description or link back to Data Sources section]
-   **Key Hyperparameters:** [e.g., Learning rate, batch size, number of epochs]
-   **Performance Metrics:** [e.g., Accuracy, Precision, Recall, F1-score on the test set]
    -   Accuracy: X%
    -   Precision (Fake): Y%
    -   Recall (Fake): Z%
    -   F1-score (Fake): A%

## Testing

*(Describe your testing strategy)*
-   **Unit Tests:** Backend (Python `unittest` or `pytest`) and Frontend (Jest, React Testing Library).
-   **Integration Tests:** Testing interactions between frontend, backend, and model.
-   **Manual Testing:** Performed throughout development to ensure UI/UX quality.
-   **CI:** GitHub Actions are set up to run tests on every push/pull request.

## Ethical Considerations

-   **Bias:** The model's performance may be influenced by biases present in the training data. Efforts have been made to use diverse datasets where possible, but users should be aware that predictions are not infallible.
-   **Misinterpretation:** This tool is an aid and not an absolute arbiter of truth. Predictions indicate statistical likelihood based on patterns learned from data. Users are encouraged to use critical thinking and consult multiple sources.
-   **Transparency:** While providing a prediction, the model's internal reasoning can be complex. Future work may include exploring explainability techniques (e.g., LIME, SHAP) if feasible.
-   **Limitations:** The model is trained on specific datasets and may not generalize perfectly to all types of news or evolving misinformation tactics. Continuous monitoring and retraining are necessary for real-world robustness.
-   **No Censorship:** This tool aims to inform, not to censor.

## Future Improvements

*(List potential enhancements)*
-   Support for URL-based article submission (requiring web scraping/content extraction).
-   Implementation of model explainability features.
-   User accounts and personalized history.
-   Integration with browser extensions for on-the-fly analysis.
-   Regular retraining of the model with new data.
-   Expansion to support other languages.

## Author

-   Sajandeep Cheema/ sajc30
-   [GitHub Profile](https://github.com/sajc30)
-   [LinkedIn](https://www.linkedin.com/in/sajandeep-cheema-8bb478263)

## License

*(Choose a license, e.g., MIT License is common for open-source projects)*
-   This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details (you'll need to create this file if you choose a license).