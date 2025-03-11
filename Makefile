# Setup dependencies (installing required packages)
setup:
	pip install -r Music_Emotion_Classification/requirements.txt
	pip install -r Chatbot/requirements.txt
	pip install -r Semantic_Book_Recommender/requirements.txt

# Format the code with black
format:
	black .
	isort .

# Lint the code with flake8
lint:
	flake8 .

# Test step (currently no tests, placeholder)
test:
	echo "No tests available. Add tests to the 'tests/' folder."
