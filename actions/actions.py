# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from serpapi import GoogleSearch

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class GoogleSearch(Action):

    def name(self) -> Text:

        return "action_out_of_scope"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        msg = tracker.latest_message

        params = {"api_key": "109578248b35fe6863d9c0bf9ceed8938f411aeada9fb737e49a422674e2f805",
                "engine": "google",
                "q": msg,
                "google_domain": "google.com",
                "gl": "us",
                "hl": "en"
                }

        search = GoogleSearch(params)
        results = search.get_dict()

        dispatcher.utter_message(f"Here's some ideas: {results["answer_box"]["list"]}")

        return []
