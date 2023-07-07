from data.intention.models import Intention
from useful.exceptions import IntentionNotFoundError
from useful.similarity import similar


def try_get_intention(type_intention):
    """

    :param type_vocabulary:
    :return:
    """

    intentions = Intention.objects.filter(type=type_intention, active=True)

    if not intentions.exists():
        raise IntentionNotFoundError(f"Intention not found.")

    return intentions


def check_an_intent(voice_text, type_intent=None, percentage_comparison=0.7):
    """

    :param voice_text:
    :param type_intent:
    :param percentage_comparison:
    :return:
    """

    from data.intention.models import Intention

    if type_intent:
        intentions = Intention.objects.filter(type=type_intent, active=True)
    else:
        intentions = Intention.objects.filter(active=True)

    try:
        voice_text_lower = voice_text.lower()

        for intention in intentions:
            description_lower = intention.description.lower()
            similar_percentage = similar(voice_text_lower, description_lower)

            if similar_percentage > percentage_comparison:
                return intention
    except:
        return None

    return None
