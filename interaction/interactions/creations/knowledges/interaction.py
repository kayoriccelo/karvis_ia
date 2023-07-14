from interaction.interactions.creations.knowledges.questions import CreationQuestions
from interaction.interactions.creations.knowledges.responses import CreationResponses


class InteractionCreationKnowledge:
    interaction = None
    questions = None
    responses = None

    def __init__(self, interaction):
        self.interaction = interaction

        self.questions = CreationQuestions(self)
        self.responses = CreationResponses(self)

    @property
    def artificial_intelligent(self):
        return self.interaction.artificial_intelligent
