from data.dialog.models import Dialog
from data.intention.choices import TYPE_INTENTION_HI_AI
from data.intention.methods import check_an_intent_text, check_an_intent
from interaction.continuously import InteractionContinuously
from listen.continuously import ListenContinuously
from speak import Speak
from useful.exceptions import VocabularyNotFoundError, ListenClientError, UnderstandAudioError


class Continuously:
    karvis = None

    def __init__(self, karvis):
        if not karvis:
            raise Exception('Karvis not found.')

        self.karvis = karvis
        self.karvis.speak = Speak(karvis.language, karvis.frame_rate)
        self.karvis.listen = ListenContinuously(karvis.language, self._salutation, phrase_time_limit_continuously=5)
        self.karvis.interaction = InteractionContinuously(karvis)

    def _salutation(self, salutation_in_text):
        def _salutation_with_interaction(text):
            intention_hi, new_text = check_an_intent_text(text, TYPE_INTENTION_HI_AI)

            if intention_hi:
                intention = check_an_intent(new_text)

                if intention:
                    self.interact(intention=intention)

        if check_an_intent(salutation_in_text, TYPE_INTENTION_HI_AI, self.karvis.percentage_salutation):
            self.interact()

        else:
            _salutation_with_interaction(salutation_in_text)

    def interact(self, **kwargs):
        self.karvis.dialog = Dialog.objects.create()  # TODO - Kayo: check dialog in progress.
        intention = kwargs.get('intention', None)

        if intention:
            dialog_question = self.karvis.interaction.core.questions.offer_help_without_interaction()

            response = self.karvis.interaction.response(dialog_question, intention, anything_else=True)

        else:
            response = self.karvis.interaction.core.questions.offer_help(anything_else=True)

        if response:
            self.karvis.speak.say_i_happy_to_help()

        self.karvis.dialog = None

    def start(self, **kwargs):
        try:
            # self.speak.say_introduce_yourself()

            self.karvis.listen.to_stay_listening_continuously()

        except VocabularyNotFoundError:
            self.karvis.speak.say("I don't have vocabulary to communicate.")

        except ListenClientError:
            self.karvis.speak.say("I can not hear")

        except UnderstandAudioError:
            self.karvis.speak.say("I don't understand")
