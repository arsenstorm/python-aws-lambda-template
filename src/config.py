# Imports
import os

# Configuration file for your app

# Your OpenAI API key
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')

# you can use if os.environ.get('DEPLOYED_ON_AWS'): 
# to check if the app is running on AWS since we've
# set the DEPLOYED_ON_AWS environment variable in the
# serverless.yml file
