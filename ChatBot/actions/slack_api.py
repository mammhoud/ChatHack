from slack import WebClient


class SlackApp:
    def __init__(self, channel_name=None, channel_id=None):
        self.token = open("secret_slack_token.txt", "r").readlines()[0]
        self.client = WebClient(token=self.token)

        self.users = self.client.users_list()

        self.channel = None
        self.channel_name = channel_name
        self.channel_id = channel_id

        if channel_name:
            self.getChannelId(channel_name)

    def getChannelId(self, channel_name=None):
        """Get the Channel's ID from its name"""
        name = channel_name if channel_name else self.channel_name

        try:
            for channel in self.client.conversations_list()["channels"]:
                if channel["name"] == name:
                    self.channel = channel
                    self.channel_name = channel["name"]
                    self.channel_id = channel["id"]
                    return channel["id"]
            return None

        except Exception as e:
            print(f"SlackApp getChannelId Error: {e}")
            return None

    def sendMessage(self, message="", channel_name=None):
        """Check https://api.slack.com/reference/surfaces/formatting for message formatting"""
        channel_id = (
            self.getChannelId(channel_name)
            if (channel_name or not self.channel_id)
            else self.channel_id
        )

        try:
            result = self.client.chat_postMessage(channel=channel_id, text=message)
            return result

        except Exception as e:
            print(f"SlackApp sendMessage Error: {e}")
            return None

