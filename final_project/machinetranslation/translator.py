# """This is the docstring that is no longer missing"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('siO6lpZx4Zl68judfOoqZrf3zRf3txGosjphgqDk7IsE')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/81637c67-51aa-4897-8767-a23247a39d5f'
)
# """ this is the en-fr and reverse translation"""
def englishToFrench(englishText):
#pylint: disable=invalid-name
    translator= language_translator.translate(text=englishText, model_id="en-fr").get_result()
    frenchText=translator['translations'][0]['translation']
#pylint: disable=invalid-name
    return frenchText
# """see above"""
def frenchToEnglish(frenchText):
#pylint: disable=invalid-name
    translator= language_translator.translate(text=frenchText, model_id="fr-en").get_result()
    englishText=translator['translations'][0]['translation']
    return englishText