from interaction.continuously.interactions.core.questions import CoreQuestions
from interaction.continuously.interactions.core.responses import CoreResponses


class InteractionCore:
    interaction = None
    questions = None
    responses = None

    def __init__(self, interaction):
        self.interaction = interaction

        self.questions = CoreQuestions(self)
        self.responses = CoreResponses(self)

    @property
    def karvis(self):
        return self.interaction.karvis
