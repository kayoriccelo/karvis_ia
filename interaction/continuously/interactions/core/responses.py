from data.intention.choices import TYPE_INTENTION_NEGATION, TYPE_INTENTION_CONFIRMATION


class CoreResponses:
    intentions = {}
    vocabularys = {}
    interaction_core = None

    def __init__(self, interaction_core):
        self.interaction_core = interaction_core

        self.intentions = {
            TYPE_INTENTION_NEGATION: self.negation,
            TYPE_INTENTION_CONFIRMATION: self.confirmation,
        }

    @property
    def interaction(self):
        return self.interaction_core.interaction

    @property
    def karvis(self):
        return self.interaction.karvis

    def negation(self, **kwargs):
        dialog_question = kwargs.get('dialog_question', None)

        if dialog_question and dialog_question.vocabulary:
            return self.interaction.response(dialog_question)

    def confirmation(self, **kwargs):
        dialog_question = kwargs.get('dialog_question', None)

        if dialog_question and dialog_question.vocabulary:
            return self.interaction.response(dialog_question)
