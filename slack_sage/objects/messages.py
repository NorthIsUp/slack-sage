from slack_sage import api
from . import user
from . import channels


class Message(api.APIContext):
    user = None
    channel = None
    text = None
    ts = None
    source_team = None
    team = None

    @staticmethod
    def parse(obj):
        return Message(
            channel=channels.Channel(channel_id=obj.get('channel')),
            user=user.SlackUser(user_id=obj.get('user')),
            text=obj.get('text'),
            ts=obj.get('ts'),
            team=obj.get('team'),
            source_team=obj.get('source_team'),
        )
