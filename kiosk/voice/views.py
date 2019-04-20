from django.shortcuts import render
from django.views.generic import TemplateView
#import pandas as pd
#import re
#from nltk.corpus import stopwords
import os
from django.views.decorators.http import require_http_methods
# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'

# def index(request):
#     return render(request,'voice/index.html')
@require_http_methods(["GET", "POST"])
def hook_receiver_view(request):
    # Listens only for GET and POST requests
    # returns django.http.HttpResponseNotAllowed for other requests

    # Handle the event appropriately
    return HttpResponse('success')


def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')

    # return a fulfillment response
    return {'fulfillmentText': 'This is a response from webhook.'}

def webhook():
    # return response
    return make_response(jsonify(results()))

import argparse
import uuid

def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.
    Using the same `session_id` between requests allows continuation
    of the conversation."""

    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
        return response.query_result.fulfillment_text
        # print(response.query_result.fulfillment_text)
# [END dialogflow_detect_intent_text]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '--project-id',
        help='Project/agent id.  Required.',
        required=True)
    parser.add_argument(
        '--session-id',
        help='Identifier of the DetectIntent session. '
        'Defaults to a random UUID.',
        default=str(uuid.uuid4()))
    parser.add_argument(
        '--language-code',
        help='Language code of the query. Defaults to "en-US".',
        default='en-US')
    parser.add_argument(
        'texts',
        nargs='+',
        type=str,
        help='Text inputs.')

    args = parser.parse_args()







def submit(request):
    a=request.POST['textvalue'];
    print(a)
    # keyword=str(a)
    # keyword = re.sub('[^a-zA-Z]',' ',keyword)
    # keyword = keyword.lower()
    # keyword = keyword.split()
    # keyword = [word for word in keyword if not word in set(stopwords.words('english'))]
    # # print(keyword)
    # x = os.path.join(os.path.dirname(__file__),"static/js/text.txt")
    # f=open(x,'w');
    # for i in keyword:
    #     f.write(i+"\t")
    # print(a);
    print('pranshita')
    t=[]
    t.append(a)
    # t=['what is the fees?']
    a = detect_intent_texts(
          'automatedkiosk', '73d742d5-8dac-5b9d-a518-56df18c0ee96',t, 'en')
    my_dict = {'insert_me':a}
    return render(request,'voice/submit.html',context=my_dict)
