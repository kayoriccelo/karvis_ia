from django.db import transaction

from data.dialog.choices import AUTHOR_DIALOG_USER
from data.intention.choices import TYPE_INTENTION_NEGATION, TYPE_INTENTION_CONFIRMATION
from data.intention.methods import check_an_intent
from interaction.base import InteractionBase
from useful.exceptions import VocabularyNotFoundError


class InteractionContinuously(InteractionBase):
    def try_interact(self, interaction, try_times=None):
        if not try_times and try_times != 0:
            try_times = self.artificial_intelligent.try_times_interaction

        if try_times > 0:
            try:
                with transaction.atomic():
                    return interaction()

            except VocabularyNotFoundError:
                self.artificial_intelligent.speak.say(
                    "Infelizmente não possuo vocabulário para dar continuidade."
                )  # TODO - Kayo: create new vocabulary

                return

            except Exception as e:
                print(str(e))  # TODO - Kayo: send exception to admin email or sentry.

                try_times -= 1

                if try_times > 0:
                    if try_times == 2:
                        self.artificial_intelligent.speak.say_i_dont_understand_talking_again()

                    else:
                        self.artificial_intelligent.speak.say_i_still_dont_understand_repeat()

                return self.try_interact(interaction, try_times)

        self.artificial_intelligent.speak.say_did_not_understand_what_you_said()

    def try_response_question_with_intention(self, dialog_question, author=AUTHOR_DIALOG_USER):
        def _response_question_with_intention():
            response_how_text = self.artificial_intelligent.listen.listen_voice_text()

            response_how_intention = check_an_intent(response_how_text)

            dialog_question.dialogs_response.create(
                author=author, intention=response_how_intention, response=response_how_text
            )

            return self.response(dialog_question, response_how_intention)

        return self.try_interact(_response_question_with_intention)

    def try_response_question_with_voice_text(
        self, dialog_question, author=AUTHOR_DIALOG_USER, phrase_time_limit=None
    ):
        def _response_question_with_voice_text():
            phrase_time_limit_initial = self.artificial_intelligent.listen.phrase_time_limit

            if phrase_time_limit:
                self.artificial_intelligent.listen.phrase_time_limit = phrase_time_limit

            response_how_text = self.artificial_intelligent.listen.listen_voice_text()

            self.artificial_intelligent.listen.phrase_time_limit = phrase_time_limit_initial

            dialog_question.dialogs_response.create(author=author, response=response_how_text)

            intention = None

            intention_negation = check_an_intent(response_how_text, TYPE_INTENTION_NEGATION)

            if intention_negation:
                intention = intention_negation

            intention_confirmation = check_an_intent(response_how_text, TYPE_INTENTION_CONFIRMATION)

            if intention_confirmation:
                intention = intention_confirmation

            return self.response(dialog_question, intention)

        return self.try_interact(_response_question_with_voice_text)

    def response(self, dialog_question, intention=None):
        def _execute_interaction():
            def _try_get_interaction():
                def _get_interaction():
                    if intention and intention.type in interaction.responses.intentions.keys():
                        return interaction.responses.intentions[intention.type]

                    if dialog_question and dialog_question.vocabulary:
                        if dialog_question.vocabulary.type in interaction.responses.vocabularys.keys():
                            return interaction.responses.vocabularys[dialog_question.vocabulary.type]

                        if dialog_question.vocabulary.type in interaction.questions.vocabularys.keys():
                            return interaction.questions.vocabularys[dialog_question.vocabulary.type]

                for interaction in self.interactions:
                    interaction = _get_interaction()

                    if interaction:
                        return interaction

            interaction_response = _try_get_interaction()

            if interaction_response:
                return interaction_response(dialog_question=dialog_question, intention=intention)

        self.try_interact(_execute_interaction)
