import string

from unicodedata import normalize
from nltk.corpus import stopwords


def list_pairs_char(term):
    """

    :param term:
    :return:
    """

    tokens = term.split(' ')
    result_list = []

    for token in tokens:
        if len(token) == 1:
            result_list.append(token)

        else:
            for item in range(1, len(token)):
                result_list.append(token[item - 1] + token[item])

    return result_list


def count_same_items(list_1, list_2):
    """

    :param list_1:
    :param list_2:
    :return:
    """

    i = 0

    for item in list_1:
        if item in list_2:
            i += 1
            list_2.remove(item)

    return i


def text_process(token):
    """

    :param token:
    :return:
    """

    token = token.lower()

    token = normalize('NFKD', token).encode('ASCII', 'ignore').decode('ASCII')

    token = [char for char in token if char not in string.punctuation]
    token = ''.join(token)

    try:
        token_args = [word for word in token.split() if word.lower() not in stopwords.words('portuguese')]  # TODO - Kayo: adding words in configuration.

        token = ' '.join(token_args)
    except:
        pass

    token = token.strip()

    return token


def words_limit(term, limite):
    """

    :param temr:
    :param limite:
    :return:
    """

    tokens = term.split()
    result_token = ''
    i = 1

    for token in tokens:
        if i > limite:
            return result_token

        result_token = f'{result_token} {token}'
        i += 1

    return result_token


def similar(term_1, term_2, count_token=10):
    """

    :param term_1:
    :param term_2:
    :param count_token:
    :return:
    """

    token1 = text_process(term_1)
    token2 = text_process(term_2)

    token1 = words_limit(token1, count_token)
    token2 = words_limit(token2, count_token)

    l1 = list_pairs_char(token1)
    l2 = list_pairs_char(token2)

    union = (len(l1) + len(l2))

    return (2 * count_same_items(l1, l2)) / union
