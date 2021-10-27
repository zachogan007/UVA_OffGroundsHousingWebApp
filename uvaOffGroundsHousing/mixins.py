from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests
import json
import datetime
from humanfriendly import format_timespan
from django.http import JsonResponse


def FormErrors(*args):
    # this handles form errors, passed back into AJAX calls
    # if we ever overwrite the form valid method, and if there is an error, then this method is called
    # return a string of a message contains all the errors that you can pass through the front end
    message = ""
    for f in args:
        if f.errors:
            message = f.errors.as_text()
    return message
