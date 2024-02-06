from data.dialog.choices import AUTHOR_DIALOG_AI
from data.vocabulary.choices import TYPE_VOCABULARY_WHAT_INFORMATION_WANT


class InformationQuestions:
    intentions = {}
    vocabularies = {}
    interaction_information = None

    def __init__(self, interaction_information):
        self.interaction_information = interaction_information

        self.vocabularies = {
            TYPE_VOCABULARY_WHAT_INFORMATION_WANT: self.what_inform_want,
        }

    @property
    def interaction(self):
        return self.interaction_information.interaction

    @property
    def karvis(self):
        return self.interaction.karvis

    def what_inform_want(self, **kwargs):
        vocabulary = self.karvis.speak.say_what_information_want()

        dialog_question = self.interaction.dialog.dialogs_question.create(
            author=AUTHOR_DIALOG_AI, vocabulary=vocabulary
        )

        return self.interaction.try_response_question_with_intention(dialog_question)
