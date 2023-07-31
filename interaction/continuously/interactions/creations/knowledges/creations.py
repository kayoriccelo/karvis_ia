from data.intention.choices import TYPE_INTENTION_NEGATION
from data.intention.models import Intention
from data.knowledge_base.models import KnowledgeBase
from data.vocabulary.choices import (
    TYPE_VOCABULARY_WHAT_INTENT_YOU_WANT_CREATE, TYPE_VOCABULARY_WANT_ADD_NEW_INTENT,
    TYPE_VOCABULARY_WHAT_KNOWLEDGE_WANT_TEACH, TYPE_VOCABULARY_WANT_YOU_WANT_SEARCH_CHATGPT
)


def _create_intentions(dialog):
    """

    :param dialog:
    :return:
    """

    dialogs_questions_new_intentions = dialog.dialogs_question.filter(
        vocabulary__type__in=[TYPE_VOCABULARY_WHAT_INTENT_YOU_WANT_CREATE, TYPE_VOCABULARY_WANT_ADD_NEW_INTENT]
    ).exclude(
        dialogs_response__intention__type=TYPE_INTENTION_NEGATION
    )

    intentions = []

    for dialog_question in dialogs_questions_new_intentions:
        dialogs_response = dialog_question.dialogs_response.all()

        for dialog_response in dialogs_response:
            intention = Intention.objects.create(description=dialog_response.response)

            intentions.append(intention)

    return intentions


def _create_knowledges(dialogs_questions_new_knowledge, intentions):
    """

    :param dialog:
    :param intentions:
    :return:
    """

    for dialog_question in dialogs_questions_new_knowledge:
        dialogs_response = dialog_question.dialogs_response.all()

        for dialog_response in dialogs_response:
            knowledge = KnowledgeBase.objects.create(description=dialog_response.response)

            if len(intentions) > 0:
                for intention in intentions:
                    knowledge.intentions.add(intention)

                knowledge.save()


def create_knowledge_informed(dialog):
    """

    :param dialog:
    :return:
    """

    intentions = _create_intentions(dialog)

    dialogs_questions_new_knowledge = dialog.dialogs_question.filter(
        vocabulary__type=TYPE_VOCABULARY_WHAT_KNOWLEDGE_WANT_TEACH
    )

    _create_knowledges(dialogs_questions_new_knowledge, intentions)


def create_knowledge_chatgpt(dialog):
    """

    :param dialog:
    :return:
    """

    intentions = _create_intentions(dialog)

    dialogs_questions_new_knowledge = dialog.dialogs_question.filter(
        vocabulary__type=TYPE_VOCABULARY_WANT_YOU_WANT_SEARCH_CHATGPT
    )

    _create_knowledges(dialogs_questions_new_knowledge, intentions)
