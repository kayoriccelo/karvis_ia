from data.dialog.choices import AUTHOR_DIALOG_AI
from data.intention.choices import (
    TYPE_INTENTION_ADDING_NEW_KNOWLEDGE, TYPE_INTENTION_NEGATION, TYPE_INTENTION_CONFIRMATION
)
from interaction.interactions.creations.knowledges.creations import create_knowledge_chatgpt, create_knowledge_informed
from useful.chat_gpt import try_get_information_chatgpt
from data.vocabulary.choices import (
    TYPE_VOCABULARY_WANT_ADD_NEW_INTENT, TYPE_VOCABULARY_WANT_INFORM_KNOWLEDGE,
    TYPE_VOCABULARY_HOW_MANY_MINUTES_INFORM_KNOWLEDGE, TYPE_VOCABULARY_WHAT_KNOWLEDGE_WANT_TEACH,
    TYPE_VOCABULARY_WANT_YOU_WANT_SEARCH_CHATGPT, TYPE_VOCABULARY_CONFIRMS_THIS_INFORMATION_FOR_KNOWLEDGE,
    TYPE_VOCABULARY_WHAT_INTENT_YOU_WANT_CREATE
)


class CreationResponses:
    intentions = {}
    vocabularys = {}
    interaction_creation = None

    def __init__(self, interaction_creation):
        self.interaction_creation = interaction_creation

        self.intentions = {
            TYPE_INTENTION_ADDING_NEW_KNOWLEDGE: self.adding_new_knowledge,
        }

        self.vocabularys = {
            TYPE_VOCABULARY_WHAT_INTENT_YOU_WANT_CREATE: self.what_intent_you_want_create,
            TYPE_VOCABULARY_WANT_ADD_NEW_INTENT: self.want_add_new_intent,
            TYPE_VOCABULARY_WANT_INFORM_KNOWLEDGE: self.want_inform_knowledge,
            TYPE_VOCABULARY_HOW_MANY_MINUTES_INFORM_KNOWLEDGE: self.how_many_minutes_inform_knowledge,
            TYPE_VOCABULARY_WHAT_KNOWLEDGE_WANT_TEACH: self.what_knowledge_want_teach,
            TYPE_VOCABULARY_WANT_YOU_WANT_SEARCH_CHATGPT: self.what_you_want_search_chatgpt,
            TYPE_VOCABULARY_CONFIRMS_THIS_INFORMATION_FOR_KNOWLEDGE: self.confirms_this_information_for_knowledge
        }

    @property
    def interaction(self):
        return self.interaction_creation.interaction

    @property
    def artificial_intelligent(self):
        return self.interaction.artificial_intelligent

    def adding_new_knowledge(self, **kwargs):
        return self.interaction_creation.questions.what_intent_you_want_create()

    def what_intent_you_want_create(self, **kwargs):
        return self.interaction_creation.questions.want_add_new_intent()

    def want_add_new_intent(self, **kwargs):
        dialog_question = kwargs.get('dialog_question', None)

        # TODO - Kayo: say I understand

        if dialog_question:
            dialog_response = dialog_question.dialogs_response.first()

            if dialog_response and dialog_response.intention:
                if dialog_response.intention.type == TYPE_INTENTION_NEGATION:
                    return self.interaction_creation.questions.want_inform_knowledge()

        return self.interaction_creation.questions.want_add_new_intent()

    def want_inform_knowledge(self, **kwargs):
        dialog_question = kwargs.get('dialog_question', None)

        if dialog_question:
            dialog_response = dialog_question.dialogs_response.first()

            if dialog_response and dialog_response.intention:
                if dialog_response.intention.type == TYPE_INTENTION_CONFIRMATION:
                    return self.interaction_creation.questions.how_many_minutes_inform_knowledge()

        return self.interaction_creation.questions.what_you_want_search_chatgpt()

    def how_many_minutes_inform_knowledge(self, **kwargs):
        dialog_question = kwargs.get('dialog_question')

        return self.interaction_creation.questions.what_knowledge_want_teach(dialog_question=dialog_question)

    def what_knowledge_want_teach(self, **kwargs):
        create_knowledge_informed(self.interaction.artificial_intelligent.dialog)

        self.artificial_intelligent.speak.say_thanks_for_the_new_knowledge()

    def what_you_want_search_chatgpt(self, **kwargs):
        dialog_question = kwargs.get('dialog_question', None)

        if dialog_question:
            dialog_response = dialog_question.dialogs_response.first()

            knowledge_chatgpt = try_get_information_chatgpt(dialog_response.response)

            self.artificial_intelligent.speak.say_i_found_the_following_information()
            self.artificial_intelligent.speak.say(knowledge_chatgpt)

            dialog_question.dialogs_response.create(author=AUTHOR_DIALOG_AI, response=knowledge_chatgpt)

            return self.interaction_creation.questions.confirms_this_information_for_knowledge()

    def confirms_this_information_for_knowledge(self, **kwargs):
        dialog_question = kwargs.get('dialog_question', None)

        if dialog_question:
            dialog_response = dialog_question.dialogs_response.first()

            if dialog_response and dialog_response.intention:
                if dialog_response.intention.type == TYPE_INTENTION_CONFIRMATION:
                    create_knowledge_chatgpt(dialog_question.dialog)

                    self.artificial_intelligent.speak.say_thanks_for_the_new_knowledge()
                    return

        return self.interaction_creation.questions.want_inform_knowledge()
