import random
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
import os 
from dotenv import load_dotenv
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
import json
from django.http import JsonResponse
# from __future__ import print_function

@shared_task
def add(x, y):
    return x + y

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)


import os
from celery import shared_task
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from django.http import JsonResponse

@shared_task(name='send_the_email')
def send_mail_func(first_name, email):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.getenv("YOUR_API_V3_KEY")

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = "This Email is for Registration"
    html_content = "<html><body><h1>This is my first Celery transactional email</h1></body></html>"
    sender = {"name": "Aradhya", "email": "nikkiimeena02@gmail.com"}
    to = [{"email": email, "name": first_name}]
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
        response_data = {"message": "Email sent successfully!"}
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
        response_data = {"message": "Failed to send email."}

    response = JsonResponse(response_data)
    response['X-Frame-Options'] = 'DENY'
    return response