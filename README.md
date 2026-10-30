🎬 CineSense AI – Content-Based Movie Recommendation Engine

Discover your next cinematic obsession with CineSense AI, a movie recommendation system powered by Machine Learning.

CineSense AI analyzes movie content and recommends similar movies based on their genre and content similarities through an interactive Streamlit web application.

🌐 Live Demo

Try CineSense AI here:
https://cinsenseai.streamlit.app

✨ Features

- 🎥 Select a movie from an interactive dropdown.
- 🤖 Get personalized movie recommendations.
- 🧠 Content-based filtering using Machine Learning.
- 📊 Similarity calculation using Cosine Similarity.
- 🔍 Movie recommendations based on content similarity.
- 🎨 Interactive and visually enhanced Streamlit interface.
- ⚡ Fast movie recommendations.

🛠️ Tech Stack

Technology| Purpose
Python| Core programming language
Pandas| Data manipulation and preprocessing
NumPy| Numerical operations
Scikit-learn| Machine Learning and similarity calculation
Streamlit| Interactive web application
Requests| HTTP requests

🧠 Machine Learning Approach

CineSense AI uses Content-Based Filtering to recommend movies similar to the user's selected movie.

The recommendation pipeline involves:

1. Data Loading: Load and explore the movie dataset.
2. Data Preprocessing: Clean and prepare movie information.
3. Feature Extraction: Convert movie content into numerical vectors using CountVectorizer.
4. Similarity Calculation: Calculate similarities between movies using Cosine Similarity.
5. Recommendation: Identify and return the top 5 most similar movies.

How It Works

The system compares the content features of movies and recommends titles with the highest similarity scores.

This approach does not depend on user ratings or collaborative filtering.

📂 Project Structure

Content-Based-Movie-Recommendation-Engine/
│
├── datasets/
│   └── Movie dataset files
│
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation and Setup

Follow these steps to run CineSense AI locally.

1. Clone the repository

git clone https://github.com/ajnuu/Content-Based-Movie-Recommendation-Engine.git

2. Navigate to the project directory

cd Content-Based-Movie-Recommendation-Engine

3. Install dependencies

pip install -r requirements.txt

4. Run the application

streamlit run app.py

5. Open in your browser

Streamlit will provide a local URL, usually:

http://localhost:8501

📦 Dependencies

The project uses the following Python libraries:

- streamlit
- pandas
- numpy
- scikit-learn
- requests

All dependencies are listed in "requirements.txt".

🚀 Deployment

The application is deployed using Streamlit Community Cloud and connected to the GitHub repository.

Live Application: https://cinesenseai.streamlit.app

🎯 Learning Outcomes

Through this project, I explored:

- Understanding and preprocessing real-world datasets.
- Implementing content-based recommendation systems.
- Feature extraction using CountVectorizer.
- Measuring similarity using Cosine Similarity.
- Building interactive ML applications using Streamlit.
- Managing projects with Git and GitHub.
- Deploying Machine Learning applications to the cloud.

🔮 Future Improvements

Potential enhancements include:

- Movie poster integration.
- Improved recommendation explanations.
- Additional movie metadata.
- Search and filtering enhancements.
- More advanced recommendation techniques.

👩‍💻 Author

Ajnu

GitHub: https://github.com/ajnuu

---

⭐ If you find this project interesting, feel free to explore the repository!

Built as part of my Machine Learning learning journey.
