from data.dialog.choices import AUTHOR_DIALOG_AI
from data.vocabulary.choices import TYPE_VOCABULARY_WHAT_INFORM_KNOWLEDGE


class InformationQuestions:
    intentions = {}
    vocabularys = {}
    interaction_information = None

    def __init__(self, interaction_information):
        self.interaction_information = interaction_information

        self.vocabularys = {
            TYPE_VOCABULARY_WHAT_INFORM_KNOWLEDGE: self.what_inform_knowledge,
        }

    @property
    def interaction(self):
        return self.interaction_information.interaction

    @property
    def artificial_intelligent(self):
        return self.interaction.artificial_intelligent

    def what_inform_knowledge(self, **kwargs):
        vocabulary = self.artificial_intelligent.speak.say_vocabulary_what_inform_knowledge()

        dialog_question = self.interaction.dialog.dialogs_question.create(
            author=AUTHOR_DIALOG_AI, vocabulary=vocabulary
        )

        return self.interaction.try_response_question_with_intention(dialog_question)
