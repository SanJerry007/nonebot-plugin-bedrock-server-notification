from nonebot import on_command
from nonebot.adapters.console import Message as ConsoleMessage
from nonebot.params import CommandArg
from nonebot.rule import to_me

weather = on_command("weather", rule=to_me(), aliases={"天气"})


# weather = on_command("天气", rule=to_me(), aliases={"weather", "查天气"}, priority=10, block=True)


@weather.handle()
async def get_weather(args: ConsoleMessage = CommandArg()):
    if location := args.extract_plain_text():
        result = f"{location}"
        await weather.send(result)
        await weather.finish(result)
    else:
        await weather.finish("请输入要查询的地点")


# from nonebot_plugin_saa import MessageFactory, Text
# @weather.handle()
# async def get_weather(args: ConsoleMessage = CommandArg()):
#     if location := args.extract_plain_text():
#         result = f"{location}"
#         await weather.send(result)
#         await MessageFactory(
#             [
#                 Text(result),
#             ]
#         ).finish(at_sender=True, reply=True)
#     else:
#         await Text("请输入要查询的地点").finish()
