from interaction.continuously.interactions.informations.questions import InformationQuestions
from interaction.continuously.interactions.informations.responses import InformationResponses


class InteractionInformations:
    interaction = None
    questions = None
    responses = None

    def __init__(self, interaction):
        self.interaction = interaction

        self.questions = InformationQuestions(self)
        self.responses = InformationResponses(self)

    @property
    def karvis(self):
        return self.interaction.karvis
