import requests, discord
from random import randrange
from datetime import timedelta


def get_url_status(url):  # checks status for each url in list urls
    # print("\n" + "Url: " + url)
    # print("GetUrlStatus: " + str(requests.get(url).status_code))
    return requests.get(url).status_code


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


# send a random message from past which has a high probability of being a meme attachment link
async def forbidden_function(ctx):
    def getmsg_if_valid(message):
        # Returns a URL to validate or None
        if (
            message.content.startswith("https://cdn.discordapp.com/attachments/")
            and get_url_status(message.content) == 200
        ):
            return message
        if (
            message.content.startswith("https://www.youtube.com/watch?v=")
            and get_url_status(message.content) == 200
        ):
            return message
        if (
            message.content.startswith("https://i.imgur.com/")
            and get_url_status(message.content) == 200
        ):
            return message
        if message.attachments and get_url_status(message.attachments[0].url) == 200:
            message.content += " " + message.attachments[0].url
            return message
        return None

    async def forbidden_collect(ctx):
        # get messages
        found_messages = []
        randd = random_date(start_date, end_date)
        print(randd)
        print("searching for forbidden messages. Around: " + str(randd))
        all_messages = [
            message async for message in ctx.channel.history(limit=10, around=randd)
        ]
        for msg in all_messages:
            if msg.author.id != ctx.bot.user.id:
                v_msg = getmsg_if_valid(msg)
                if v_msg is not None:
                    found_messages.append(v_msg)
        return found_messages

    async def forbidden_check_send(ctx, selected_messages):
        # check messages
        if len(selected_messages) > 0:
            print(
                "\n" + "found ({0}) forbidden messages".format(len(selected_messages))
            )
            randi = randrange(len(selected_messages))
            print("selected index: {0}".format(randi))
            chosen_message = selected_messages[randi]
            print("Sending Message\n*****\n" + chosen_message.content + "\n*****")

            response = chosen_message.content
            await chosen_message.reply(
                response,
                mention_author=False,
                allowed_mentions=discord.AllowedMentions(
                    users=False,  # Whether to ping individual user @mentions
                    everyone=False,  # Whether to ping @everyone or @here mentions
                    roles=False,  # Whether to ping role @mentions
                    replied_user=False,
                ),
            )

        else:
            response = "Couldn't find a forbidden message"

            await ctx.channel.send(
                response,
                allowed_mentions=discord.AllowedMentions(
                    users=False,  # Whether to ping individual user @mentions
                    everyone=False,  # Whether to ping @everyone or @here mentions
                    roles=False,  # Whether to ping role @mentions
                    replied_user=False,
                ),
            )

    print("\n\nStarting Forbidden Function")
    print("Requested by: {0}".format(ctx.author.name))
    start_date = [
        message async for message in ctx.channel.history(limit=2, oldest_first=True)
    ]
    start_date = start_date[0].created_at
    end_date = [
        message async for message in ctx.channel.history(limit=2, oldest_first=False)
    ]
    end_date = end_date[0].created_at
    selected_messages = []
    try_count = 0

    while len(selected_messages) < 1 and try_count < 150:
        try_count += 1
        print(f"try count #{try_count}")
        found_messages = await forbidden_collect(ctx)
        for f_msg in found_messages:
            selected_messages.append(f_msg)

    await forbidden_check_send(ctx, selected_messages)
