from django.db import transaction

from data.dialog.choices import AUTHOR_DIALOG_USER
from interaction.base import InteractionBase
from useful.exceptions import VocabularyNotFoundError


class InteractionBackground(InteractionBase):
    dialog_question_pending = None

    def try_interact(self, interaction, try_times=None):
        if not try_times and try_times != 0:
            try_times = self.karvis.try_times_interaction

        if try_times > 0:
            try:
                with transaction.atomic():
                    return interaction()

            except VocabularyNotFoundError:
                self.karvis.speak.say(
                    "Infelizmente não possuo vocabulário para dar continuidade."
                )  # TODO - Kayo: create new vocabulary

                return

            except Exception as e:
                print(str(e))  # TODO - Kayo: send exception to admin email or sentry.

                try_times -= 1

                if try_times > 0:
                    if try_times == 2:
                        self.karvis.speak.say_i_dont_understand_talking_again()

                    else:
                        self.karvis.speak.say_i_still_dont_understand_repeat()

                return self.try_interact(interaction, try_times)

        self.karvis.speak.say_did_not_understand_what_you_said()

    def try_response_question_with_intention(self, dialog_question, author=AUTHOR_DIALOG_USER):
        pass

    def try_response_question_with_voice_text(self, dialog_question, author=AUTHOR_DIALOG_USER):
        pass

    def response(self, intention=None):
        def _execute_interaction():
            def _try_get_interaction():
                def _get_interaction():
                    if intention and intention.type in interaction.responses.intentions.keys():
                        return interaction.responses.intentions[intention.type]

                    if self.dialog_question_pending and self.dialog_question_pending.vocabulary:
                        vocabulary = self.dialog_question_pending.vocabulary

                        if vocabulary.type in interaction.responses.vocabularies.keys():
                            return interaction.responses.vocabularies[vocabulary.type]

                        elif vocabulary.type in interaction.questions.vocabularies.keys():
                            return interaction.questions.vocabularies[vocabulary.type]

                for interaction in self.interactions:
                    interaction = _get_interaction()

                    if interaction:
                        return interaction

            interaction_response = _try_get_interaction()

            if interaction_response:
                return interaction_response(dialog_question=self.dialog_question_pending, intention=intention)

        self.try_interact(_execute_interaction)
