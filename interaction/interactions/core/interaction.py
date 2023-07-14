from interaction.interactions.core.questions import CoreQuestions
from interaction.interactions.core.responses import CoreResponses


class InteractionCore:
    interaction = None
    questions = None
    responses = None

    def __init__(self, interaction):
        self.interaction = interaction

        self.questions = CoreQuestions(self)
        self.responses = CoreResponses(self)

    @property
    def artificial_intelligent(self):
        return self.interaction.artificial_intelligent
