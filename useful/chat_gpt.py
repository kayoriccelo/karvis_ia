import openai

openai.api_key = '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'


def try_get_information_chatgpt(question, try_times=3):
    """

    :param question:
    :param try_times:
    :return:
    """

    if try_times > 0:
        try:
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}]
            )

            return chat.choices[0].message.content

        except:
            return try_get_information_chatgpt(question, try_times - 1)
