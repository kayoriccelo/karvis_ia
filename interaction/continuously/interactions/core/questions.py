from data.dialog.choices import AUTHOR_DIALOG_AI
from data.vocabulary.choices import TYPE_VOCABULARY_OFFER_HELP
from data.vocabulary.methods import try_get_vocabulary


class CoreQuestions:
    intentions = {}
    vocabularys = {}
    interaction_core = None

    def __init__(self, interaction_core):
        self.interaction_core = interaction_core

    @property
    def interaction(self):
        return self.interaction_core.interaction

    @property
    def karvis(self):
        return self.interaction.karvis

    def offer_help_without_interaction(self, vocabulary_offer_help=None):
        if not vocabulary_offer_help:
            vocabulary_offer_help = try_get_vocabulary(TYPE_VOCABULARY_OFFER_HELP)

        return self.interaction.dialog.dialogs_question.create(
            author=AUTHOR_DIALOG_AI, vocabulary=vocabulary_offer_help
        )

    def offer_help(self, anything_else=False):
        def _offer_help():
            vocabulary_offer_help = self.karvis.speak.say_offer_help()

            dialog_question = self.offer_help_without_interaction(vocabulary_offer_help)

            return self.interaction.try_response_question_with_intention(dialog_question, anything_else=anything_else)

        return self.interaction.try_interact(_offer_help)

    def anything_else(self, tentative=True):
        def _anything_else():
            vocabulary_anything_else = self.karvis.speak.say_anything_else()

            dialog_question = self.interaction.dialog.dialogs_question.create(
                author=AUTHOR_DIALOG_AI, vocabulary=vocabulary_anything_else
            )

            return self.interaction.try_response_question_with_intention(dialog_question)

        if tentative:
            return self.interaction.try_interact(_anything_else)

        else:
            return _anything_else()
