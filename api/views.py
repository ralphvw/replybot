from rest_framework.decorators import api_view
from rest_framework.response import Response
from replybot.settings import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

def get_completion(prompt, model='gpt-3.5-turbo',temperature=0):
    messages = [{'role': 'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message['content']

@api_view(['POST'])
def respond(request):
    review = request.data.review
    prompt = f"""
        You are a customer service AI assistant.
        Your task is to send an email reply to a valued customer.
        Given the customer email delimited by ```, \
        Generate a reply to thank the customer for their review.
        Check for the sentiment of the email \
        If the sentiment is positive or neutral, thank them for \
        their review.
        If the sentiment is negative, apologize and suggest that \
        they can reach out to customer service. 
        Make sure to use specific details from the review.
        Write in a concise and professional tone.
        Sign the email as `AI customer agent`.
        Customer review: ```{review}```
        """
    response = get_completion(prompt, temperature=0.7)
    return Response(response)
