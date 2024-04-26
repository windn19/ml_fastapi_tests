# An example of ML Application with the pretrained model and test.

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.

Tests GitHub Actions

# Start API

1. Install python
2. Install requirements

```bush
pip install -r requirements.txt
```

3. Run web application

```bush
uvicorn main:app
```
4. The project has two access points: index and predict:

- when sending a GET request to the address /index - json will be returned - with the text "Hello World!!!"

- when sending a POST request to the address /predict/ with the transmission of the “text” parameter
 in the request body, in which the text for tone detection is transmitted

- by GET request to the address /docs - automatically generated documentation will be displayed indicating
access points and parameters for sending requests, as well as the form of the responses received.