from data.dialog.choices import AUTHOR_DIALOG_AI, AUTHOR_DIALOG_USER
from data.intention.choices import TYPE_INTENTION_NEGATION
from data.intention.methods import check_an_intent
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
    def artificial_intelligent(self):
        return self.interaction.artificial_intelligent

    def offer_help_without_interaction(self, vocabulary_offer_help=None):
        if not vocabulary_offer_help:
            vocabulary_offer_help = try_get_vocabulary(TYPE_VOCABULARY_OFFER_HELP)

        return self.interaction.dialog.dialogs_question.create(
            author=AUTHOR_DIALOG_AI, vocabulary=vocabulary_offer_help
        )

    def offer_help(self):
        def _offer_help():
            vocabulary_offer_help = self.artificial_intelligent.speak.say_offer_help()

            dialog_question = self.offer_help_without_interaction(vocabulary_offer_help)

            return self.interaction.try_response_question_with_intention(dialog_question)

        return self.interaction.try_interact(_offer_help)

    def anything_else(self, tentative=True):
        def _anything_else():
            vocabulary_anything_else = self.artificial_intelligent.speak.say_anything_else()

            dialog_question = self.interaction.dialog.dialogs_question.create(
                author=AUTHOR_DIALOG_AI, vocabulary=vocabulary_anything_else
            )

            response_how_text = self.artificial_intelligent.listen.listen_voice_text()

            response_how_intention = check_an_intent(response_how_text)

            if response_how_intention.type == TYPE_INTENTION_NEGATION:
                dialog_question.dialogs_response.create(
                    author=AUTHOR_DIALOG_USER, intention=response_how_intention, response=response_how_text
                )

            else:
                return self.offer_help()

        if tentative:
            return self.interaction.try_interact(_anything_else)

        else:
            return _anything_else()
