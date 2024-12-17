## Setup

Create a virtual environment (first time only):

```sh
conda create -n smiski-quiz python=3.10
```

Activate the environment (whenever you come back to this project):

```sh
conda activate smiski-quiz
```

Install packages:

```sh
pip install -r requirements.txt
```
## Usage

Run the example script:

```sh
python app/smiski_quiz.py
```

### Web App
Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

Run tests:

```sh
pytest
```