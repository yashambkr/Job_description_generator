## Job Description API

**Generate compelling job descriptions with the power of AI.**

This API leverages the cutting-edge GPT-3.5-Turbo model from OpenAI to craft engaging and informative job descriptions, tailored to your specific needs. Unlock the benefits of:

* **Efficiency:** Save time and effort by automatically generating job descriptions.
* **Creativity:** Produce unique and captivating descriptions that attract top talent.
* **Accuracy:** Get consistent results based on your input data.
* **Scalability:** Generate descriptions for multiple positions with ease.

### Getting Started

**1. Prerequisites:**

* Python 3.6+
* Flask
* OpenAI
* A .env file

**2. Installation:**

1. Install the required libraries:
    ```
    pip install flask openai
    ```
2. Create a .env file and add your OpenAI API key as `OPENAI_API_KEY`.
3. Store your API key for authentication as `API_KEY` in the .env file.

**3. Running the API:**

```
python app.py
```

**4. Generating a Job Description:**

Send a POST request to `/generate_job_description` with the following JSON data:

```json
{
  "company": "Acme Inc.",
  "job_title": "Software Engineer",
  "job_type": "Full-time",
  "location": "Remote",
  "experience": "3 years",
  "tags": ["backend", "web development"]
}
```

The API will return a JSON response with the generated job description.

### Authentication

Access to the API requires authorization using a Bearer token in the `Authorization` header:

```
Authorization: Bearer <your_api_key>
```

Replace `<your_api_key>` with the value of the `API_KEY` environment variable.

### Example Usage

```
POST /generate_job_description
Content-Type: application/json

{
  "company": "Acme Inc.",
  "job_title": "Data Scientist",
  "job_type": "Full-time",
  "location": "San Francisco",
  "experience": "5 years",
  "tags": ["machine learning", "data analysis"]
}
```

This request will generate a job description for a full-time data scientist position at Acme Inc., located in San Francisco, requiring 5 years of experience in machine learning and data analysis.

### Limitations

* The API is still under development and may not always generate perfect results.
* The quality of the generated job description depends on the accuracy and completeness of your input data.
* The API currently supports only English language generation.

### Feedback

We actively seek your feedback and suggestions for improvement. Please share your thoughts and questions.



