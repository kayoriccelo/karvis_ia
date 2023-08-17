from data.vocabulary.models import Vocabulary
from useful.exceptions import VocabularyNotFoundError


def try_get_vocabulary(type_vocabulary):
    """

    :param type_vocabulary:
    :return:
    """

    try:
        return Vocabulary.objects.get(type=type_vocabulary, active=True)

    except Vocabulary.MultipleObjectsReturned:
        return Vocabulary.objects.filter(type_vocabulary, active=True).first()

    except Vocabulary.DoesNotExist:
        raise VocabularyNotFoundError(f"Vocabulary not found.")
