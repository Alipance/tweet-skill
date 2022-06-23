from mycroft import MycroftSkill, intent_file_handler


class Tweet(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tweet.intent')
    def handle_tweet(self, message):
        self.speak_dialog('tweet')


def create_skill():
    return Tweet()

