from datetime import timedelta
from flask import Flask, request, jsonify
from openai import OpenAI
import os
# Import dotenv
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Access OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Replace your actual API key with "YOUR_OPENAI_API_KEY"
openai = OpenAI(api_key=openai_api_key)


API_KEY = os.getenv("API_KEY_HEADER")

# Define GPT model
model = "gpt-3.5-turbo"

@app.route("/generate_job_description", methods=["POST"])

def generate_job_description():
    """
    API endpoint to generate job descriptions.

    Expects a POST request with the following JSON body:
    {
        "company": "Acme Inc.",
        "job_title": "Software Engineer",
        "job_type": "Full-time",
        "location": "Remote",
        "experience": "3 years",
        "tags": ["backend", "web development"],
    }
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing or invalid authorization header"}), 401

    # Extract and verify API key
    token = auth_header.split(" ")[1]
    if token != API_KEY:
        return jsonify({"error": "Invalid API key"}), 401

    try:
        # Get request data
        data = request.get_json()

        # Validate required fields
        required_fields = ["company", "job_title", "job_type", "location", "experience", "tags"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        company = data["company"]
        job_title = data["job_title"]
        job_type = data["job_type"]
        location = data["location"]
        experience = data["experience"]
        tags = data["tags"]

        # Prepare prompt for OpenAI API
        prompt = f"""
## Job Description

| Field | Value |
|---|---|
| Company | {company} |
| Job Title | {job_title} |
| Job Type | {job_type} |
| Location | {location} |
| Experience | {experience} |

**Tags:**
- {", ".join(tags)}

**Description:**

[Write a compelling job description for the position above. Be sure to highlight the required skills and experience, as well as the benefits of working for your company.]"""

        # Generate job description using OpenAI
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
            ],
        )

        # Extract generated text
        job_description = response.choices[0].message.content

        # Return JSON response
        return jsonify({"job_description": job_description})

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=False)