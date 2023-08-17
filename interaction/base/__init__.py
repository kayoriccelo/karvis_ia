
class InteractionBase:
    karvis = None
    interactions = []
    questions = None
    responses = None

    def __init__(self, karvis):
        self.karvis = karvis

        self.interactions = [
            self.creations_knowledge,
            self.informations,
            self.core,
        ]

        # TODO - Kayo: learn interactions using vocabularies, intents and methods.
        #  define interactions on itself with property function

    @property
    def dialog(self):
        return self.karvis.dialog

    @property
    def core(self):
        raise NotImplementedError("Need to implement the method for the operation")

    @property
    def informations(self):
        raise NotImplementedError("Need to implement the method for the operation")

    @property
    def creations_knowledge(self):
        raise NotImplementedError("Need to implement the method for the operation")
