from interaction.interactions.core.interaction import InteractionCore
from interaction.interactions.creations.knowledges.interaction import InteractionCreationKnowledge
from interaction.interactions.informations.interaction import InteractionInformations


class InteractionBase:
    artificial_intelligent = None
    interactions = []
    questions = None
    responses = None

    def __init__(self, artificial_intelligent):
        self.artificial_intelligent = artificial_intelligent

        self.interactions = [
            self.core,
            self.informations,
            self.creations_knowledge
        ]

        # TODO - Kayo: learn interactions using vocabularies, intents and methods.
        #  define interactions on itself with property function

    @property
    def dialog(self):
        return self.artificial_intelligent.dialog

    @property
    def core(self):
        if not hasattr(self, '_core'):
            setattr(self, '_core', InteractionCore(self))

        return getattr(self, '_core')

    @property
    def informations(self):
        if not hasattr(self, '_informations'):
            setattr(self, '_informations', InteractionInformations(self))

        return getattr(self, '_informations')

    @property
    def creations_knowledge(self):
        if not hasattr(self, '_creations'):
            setattr(self, '_creations', InteractionCreationKnowledge(self))

        return getattr(self, '_creations')
