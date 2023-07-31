from data.dialog.choices import AUTHOR_DIALOG_AI
from useful.word_2_number import word_to_num
from data.vocabulary.choices import (
    TYPE_VOCABULARY_WHAT_INTENT_YOU_WANT_CREATE, TYPE_VOCABULARY_WANT_ADD_NEW_INTENT,
    TYPE_VOCABULARY_HOW_MANY_MINUTES_INFORM_KNOWLEDGE, TYPE_VOCABULARY_WHAT_KNOWLEDGE_WANT_TEACH,
    TYPE_VOCABULARY_WHAT_YOU_WANT_SEARCH_CHATGPT, TYPE_VOCABULARY_CONFIRMS_THIS_INFORMATION_FOR_KNOWLEDGE
)


class CreationQuestions:
    intentions = {}
    vocabularys = {}
    interaction_creation = None

    def __init__(self, interaction_creation):
        self.interaction_creation = interaction_creation

        self.vocabularys = {
            TYPE_VOCABULARY_WHAT_INTENT_YOU_WANT_CREATE: self.what_intent_you_want_create,
            TYPE_VOCABULARY_WANT_ADD_NEW_INTENT: self.want_add_new_intent,
            TYPE_VOCABULARY_HOW_MANY_MINUTES_INFORM_KNOWLEDGE: self.how_many_minutes_inform_knowledge,
            TYPE_VOCABULARY_WHAT_KNOWLEDGE_WANT_TEACH: self.what_knowledge_want_teach,
            TYPE_VOCABULARY_WHAT_YOU_WANT_SEARCH_CHATGPT: self.what_you_want_search_chatgpt,
            TYPE_VOCABULARY_CONFIRMS_THIS_INFORMATION_FOR_KNOWLEDGE: self.confirms_this_information_for_knowledge,
        }

    @property
    def interaction(self):
        return self.interaction_creation.interaction

    @property
    def karvis(self):
        return self.interaction.karvis

    def what_intent_you_want_create(self, **kwargs):
        vocabulary = self.karvis.speak.say_what_intent_you_want_create()

        dialog_question = self.interaction.dialog.dialogs_question.create(
            author=AUTHOR_DIALOG_AI, vocabulary=vocabulary
        )

        return self.interaction.try_response_question_with_intention(dialog_question)

    def want_add_new_intent(self, **kwargs):
        vocabulary = self.karvis.speak.say_want_add_new_intent()

        dialog_question = self.interaction.dialog.dialogs_question.create(
            author=AUTHOR_DIALOG_AI, vocabulary=vocabulary
        )

        return self.interaction.try_response_question_with_intention(dialog_question)

    def want_inform_knowledge(self, **kwargs):
        vocabulary = self.karvis.speak.say_want_inform_knowledge()

        dialog_question = self.interaction.dialog.dialogs_question.create(
            author=AUTHOR_DIALOG_AI, vocabulary=vocabulary
        )

        return self.interaction.try_response_question_with_intention(dialog_question)

    def how_many_minutes_inform_knowledge(self, **kwargs):
        vocabulary = self.karvis.speak.say_how_many_minutes_inform_knowledge()

        dialog_question = self.interaction.dialog.dialogs_question.create(
            author=AUTHOR_DIALOG_AI, vocabulary=vocabulary
        )

        return self.interaction.try_response_question_with_voice_text(dialog_question)

    def what_knowledge_want_teach(self, **kwargs):
        def _get_response_phrase_time_limit():
            dialog_question = kwargs.get('dialog_question', None)

            if dialog_question:
                dialog_response = dialog_question.dialogs_response.first()
                minutes = word_to_num(dialog_response.response)

                return minutes * 60

        vocabulary = self.karvis.speak.say_what_knowledge_want_teach()

        dialog_question = self.interaction.dialog.dialogs_question.create(
            author=AUTHOR_DIALOG_AI, vocabulary=vocabulary
        )

        phrase_time_limit = _get_response_phrase_time_limit()

        return self.interaction.try_response_question_with_voice_text(
            dialog_question, phrase_time_limit=phrase_time_limit
        )

    def what_you_want_search_chatgpt(self, **kwargs):
        vocabulary = self.karvis.speak.say_what_you_want_search_chatgpt()

        dialog_question = self.interaction.dialog.dialogs_question.create(
            author=AUTHOR_DIALOG_AI, vocabulary=vocabulary
        )

        return self.interaction.try_response_question_with_voice_text(dialog_question)

    def confirms_this_information_for_knowledge(self, **kwargs):
        vocabulary = self.karvis.speak.say_confirms_this_information_for_knowledge()

        dialog_question = self.interaction.dialog.dialogs_question.create(
            author=AUTHOR_DIALOG_AI, vocabulary=vocabulary
        )

        return self.interaction.try_response_question_with_intention(dialog_question)
