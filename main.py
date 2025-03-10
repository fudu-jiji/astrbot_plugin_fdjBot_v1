from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api.all import * 

@register("astrbot_plugin_fdjBot", "fuduji", "复读姬机器人第一代", "1.0.0", "https://github.com/fudu-jiji/astrbot_plugin_fdjBot_v1")
class fdjPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    # 注册指令
    @filter.command("最新活动")
    async def 最新活动(self, event: AstrMessageEvent):
        '''最新的活动消息''' # 描述
        user_name = event.get_sender_name()
        yield event.plain_result(f"10日晚主活动室纳新庆祝会,请每人携带一份食材!黑暗火锅再临!!") # 发送一条纯文本消息
       # yield event.plain_result(f"最近有2025年的第一个预售,包括了一个新春大礼包和碧蓝的春节系列卡片和DC最后三期! \n本期预售预计3月发货!") # 发送一条纯文本消息
    # 注册指令
    @filter.command("参加预售")
    async def 参加预售(self, event: AstrMessageEvent):
        '''最新的活动消息''' # 描述
        user_name = event.get_sender_name()
        yield event.plain_result(f"# 有序列表 私聊管理员参加我们的活动哦!") # 发送一条纯文本消息
       # yield event.plain_result(f"预售六折，并且送特典或者礼品\n预售会一期接着一期，收到预售的快递后一个周后就会出新的预售\n一直跟预售就会最便宜的价格买最全的卡\n预售链接在群公告。") # 发送一条纯文本消息
  
    # 注册指令
    @filter.command("卡面预览")
    async def 卡面预览(self, event: AstrMessageEvent):
        '''最新的活动消息''' # 描述
        chain = [
        At(qq=event.get_sender_id()), # At 消息发送者
        Plain("图片在群文件哦!"), 
        #Image.fromFileSystem("G:/WS_Code/dev/astrbot_plugin_fdjBot_v1/astrbot_plugin_fdjBot_v1/img/fdj8.png"), # 从本地文件目录发送图片
        #Plain("密码fuduji8\n里面有所有现货的预览图和实拍图!\n预售预览: 在群文件，或者群精华消息内！如果没有就表示还没选好图\n预售的图并不是固定的,做卡的时候发现不适合的会更换图片或者是修改原图。")
          ]
        yield event.chain_result(chain)
      #  yield event.plain_result(f"'现货预览:浏览器输入 fdj.bar 密码fuduji8\n里面有所有现货的预览图和实拍图!\n预售预览: 在群文件，或者群精华消息内！如果没有就表示还没选好图\n预售的图并不是固定的,做卡的时候发现不适合的会更换图片或者是修改原图。") # 发送一条纯文本消息
    # 群聊事件监听
#@event_message_type(EventMessageType.ALL)
#async def on_private_message(self, event: AstrMessageEvent):
#    yield event.plain_result("收到了一条消息。")