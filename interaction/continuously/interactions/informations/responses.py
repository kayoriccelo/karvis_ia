from data.dialog.choices import AUTHOR_DIALOG_AI
from data.intention.choices import TYPE_INTENTION_NEED_INFORMATION, TYPE_INTENTION_WHAT_INFORMATION_WANT
from data.vocabulary.choices import TYPE_VOCABULARY_WHAT_INFORMATION_WANT


class InformationResponses:
    intentions = {}
    vocabularys = {}
    interaction_information = None

    def __init__(self, interaction_information):
        self.interaction_information = interaction_information

        self.intentions = {
            TYPE_INTENTION_NEED_INFORMATION: self.need_information,
            TYPE_INTENTION_WHAT_INFORMATION_WANT: self.what_information_want,
        }

        self.vocabularys = {
            TYPE_VOCABULARY_WHAT_INFORMATION_WANT: self.what_information_want,
        }

    @property
    def interaction(self):
        return self.interaction_information.interaction

    @property
    def karvis(self):
        return self.interaction.karvis

    def need_information(self, **kwargs):
        vocabulary = self.karvis.speak.say_what_information_want()

        dialog_question = self.interaction.dialog.dialogs_question.create(
            author=AUTHOR_DIALOG_AI, vocabulary=vocabulary
        )

        return self.interaction.try_response_question_with_intention(dialog_question)

    def what_information_want(self, **kwargs):
        dialog_question = kwargs.get('dialog_question', None)
        intention = kwargs.get('intention', None)

        if not dialog_question:
            dialog_question = self.interaction.dialog.dialogs_question.create(
                author=AUTHOR_DIALOG_AI, intention=intention
            )

        if not intention.knowledge_bases.exists():
            raise Exception('Knowledge not found.')

        for knowledge_base in intention.knowledge_bases.all():
            self.karvis.speak.say(knowledge_base.description)

            dialog_question.dialogs_response.create(author=AUTHOR_DIALOG_AI, knowledge_base=knowledge_base)

        return True
