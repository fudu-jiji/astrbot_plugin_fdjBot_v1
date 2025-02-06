from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api.all import * 

@register("astrbot_plugin_fdjBot", "fuduji", "复读姬机器人第一代", "1.0.0", "https://github.com/fudu-jiji/astrbot_plugin_fdjBot_v1")
class fdjPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    # 注册指令
    @filter.command("最新活动")
    async def helloworld(self, event: AstrMessageEvent):
        '''最新的活动消息''' # 描述
        user_name = event.get_sender_name()
        yield event.plain_result(f"最近有2025年的第一个预售,包括了一个新春大礼包和碧蓝的春节系列卡片和DC最后三期! \n本期预售预计3月发货!") # 发送一条纯文本消息
