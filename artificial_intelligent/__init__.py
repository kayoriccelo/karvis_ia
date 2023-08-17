from .choices import AI_CONTINUOUSLY, AI_BACKGROUND
from .types.continuously import Continuously


class Karvis:
    type_ai = None
    language = None
    dialog = None
    listen = None
    speak = None
    interaction = None
    frame_rate = None
    percentage_salutation = None
    try_times_interaction = None
    artificial_intelligent = None

    def __init__(self, type_ai, language, percentage_salutation=0.6, try_times_interaction=3, frame_rate=None):
        self.type_ai = type_ai
        self.language = language
        self.percentage_salutation = percentage_salutation
        self.try_times_interaction = try_times_interaction
        self.frame_rate = frame_rate

        # TODO - Kayo: learn vocabularies, intentions and knowledges

        if self.type_ai == AI_CONTINUOUSLY:
            self.artificial_intelligent = Continuously(self)

    def interact(self, **kwargs):
        return self.artificial_intelligent.interact(**kwargs)

    def start(self, **kwargs):
        self.artificial_intelligent.start(**kwargs)

    def finish(self, **kwargs):
        self.dialog = None
