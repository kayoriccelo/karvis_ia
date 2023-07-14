from data.dialog.models import Dialog
from data.intention.choices import TYPE_INTENTION_HI_AI
from data.intention.methods import check_an_intent, check_an_intent_text
from interaction.continuously import InteractionContinuously
from listen.continuously import ListenContinuously
from artificial_intelligent.choices import AI_CONTINUOUSLY
from speak.base import Speak
from useful.exceptions import ListenClientError, UnderstandAudioError, VocabularyNotFoundError


class Karvis:
    listen = None
    speak = None
    interaction = None
    type_ai = None
    language = None
    frame_rate = None
    dialog = None
    percentage_salutation = None
    try_times_interaction = None

    def __init__(self, type_ai, language, percentage_salutation=0.6, try_times_interaction=3, frame_rate=None):
        self.type_ai = type_ai
        self.language = language
        self.percentage_salutation = percentage_salutation
        self.try_times_interaction = try_times_interaction
        self.frame_rate = frame_rate

        # TODO - Kayo: learn vocabularies, intentions and knowledges

        self.speak = Speak(self.language, self.frame_rate)

        if self.type_ai == AI_CONTINUOUSLY:
            self.listen = ListenContinuously(self.language, self.salutation, phrase_time_limit_continuously=5)

            self.interaction = InteractionContinuously(self)

    def salutation(self, salutation_in_text):
        def _salution_with_interaction(text):
            intention_hi, new_text = check_an_intent_text(text, TYPE_INTENTION_HI_AI)

            if intention_hi:
                intention = check_an_intent(new_text)

                if intention:
                    self.interact(intention)

        if check_an_intent(salutation_in_text, TYPE_INTENTION_HI_AI, self.percentage_salutation):
            self.interact()

        else:
            _salution_with_interaction(salutation_in_text)

    def interact(self, intention=None):
        if self.type_ai == AI_CONTINUOUSLY:
            self.dialog = Dialog.objects.create()  # TODO - Kayo: check dialog in progress.

            if intention:
                dialog_question = self.interaction.core.questions.offer_help_without_interaction()

                self.interaction.response(dialog_question, intention)

            else:
                self.interaction.core.questions.offer_help()

            self.interaction.core.questions.anything_else()  # TODO - Kayo: improve anything else

            self.dialog = None

    def start(self):
        def _start_continuously():
            try:
                # self.speak.say_introduce_yourself()

                self.listen.to_stay_listening_continuously()

            except VocabularyNotFoundError:
                self.speak.say("I don't have vocabulary to communicate.")

            except ListenClientError:
                self.speak.say("I can not hear")

            except UnderstandAudioError:
                self.speak.say("I don't understand")

        if self.type_ai == AI_CONTINUOUSLY:
            self.listen.stop_listening = False

            _start_continuously()

    def finish(self):
        if self.type_ai == AI_CONTINUOUSLY:
            self.listen.stop_listening = True
