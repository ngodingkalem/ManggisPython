from requests import post
from json import loads
from sys import stdout
from time import sleep
from datetime import datetime
from pytz import timezone
from re import sub, match
from inspect import getframeinfo, stack

class Telegram:
    def __init__(self, bot_token, time_zone):
        for a, b in zip(['url', 'timeZone', 'response', 'responseResult', 'accTriggerTime'], ['f"https://api.telegram.org/bot{bot_token}/"', 'time_zone', 'post(f"{self.url}getUpdates", {"offset": -1})', 'loads(self.response.text).get("result")', '0']):
            exec(f'self.{a} = {b}')
        if self.response.ok:
            if self.responseResult == []:
                self.writeRun('Silahkan kirim pesan terlebih dahulu ke bot anda!\n')
                exit()
            else:
                self.writeRun('Bot mulai berjalan ...\n')
                self.offset = self.responseResult[0]['update_id'] + 1
        else:
            if self.response.status_code == 401:
                self.writeRun('Ada kesalahan pada token bot, silahkan cek kembali token bot anda!\n')
                exit()
            else:
                self.writeRun(f'ERROR {str(self.response.status_code)}\nDescription: {loads(self.response.text)["description"]}\n')
                exit()
        
    def writeRun(self, arg):
        for x in arg:
            stdout.write(x)
            stdout.flush()
            sleep(0.01)
        
    @property
    def centMessage(self):
        for a, b in zip(['response', 'responseResult'], ['post(f"{self.url}getUpdates", {"offset": self.offset})', 'loads(self.response.text)["result"]']):
            exec(f'self.{a} = {b}')
        if self.responseResult == []:
            pass
        else:
            self.update, self.offset = self.responseResult[0], self.offset + 1
            for a, b, c in zip(['message', 'msgId', 'msgFrom', 'fromId', 'fromFirstName', 'fromLastName', 'fromUsername', 'msgDate', 'msgChat', 'chatId', 'chatType', 'chatTitle', 'chatUsername', 'chatFirstName', 'chatLastName', 'msgText', 'msgCaption'], ['update', 'message', 'message', 'msgFrom', 'msgFrom', 'msgFrom', 'msgFrom', 'message', 'message', 'msgChat', 'msgChat', 'msgChat', 'msgChat', 'msgChat', 'msgChat', 'message', 'message'], ['message', 'message_id', 'from', 'id', 'first_name', 'last_name', 'username', 'date', 'chat', 'id', 'type', 'title', 'username', 'first_name', 'last_name', 'text', 'caption']):
                exec(f'self.{a} = self.{b}.get("{c}") if self.{b} is not None and "{c}" in self.{b} else None')
            return True
        
    def getField(self, arg):
        return eval('self.update.get("' + sub('\.', '").get("', arg) + '") if self.update is not None else None')
        
    def coftMessage(self, **kwargs):
        for a, b in zip(['coftMessageVar', 'timeZoneDate', 'timeZoneHour', 'timeZoneMinute', 'timeZoneSecond', 'timeZoneDay', 'timeZoneDOTM', 'timeZoneMonth', 'userFirstNameVar', 'userLastNameVar', 'userUsernameVar', 'chatTypeVar', 'chatTitleVar', 'chatUsernameVar', 'chatFirstNameVar', 'chatLastNameVar', 'messageTextVar', 'messageFormatVar', 'messageCaptionVar'], ['[]', 'datetime.now(timezone(self.timeZone))', 'int(self.timeZoneDate.strftime("%-H"))', 'int(self.timeZoneDate.strftime("%-M"))', 'int(self.timeZoneDate.strftime("%-S"))', 'int(self.timeZoneDate.strftime("%w"))', 'int(self.timeZoneDate.strftime("%-d"))', 'int(self.timeZoneDate.strftime("%-m"))', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False']):
            exec(f'self.{a} = {b}')
        for x in kwargs:
            if x == 'userId':
                self.coftMessageVar.append(True,) if self.fromId in kwargs['userId'] else self.coftMessageVar.append(False,)
            elif x == 'userFirstName':
                for z in kwargs['userFirstName']:
                    if match(z, str(self.fromFirstName)):
                        self.userFirstNameVar = True
                self.coftMessageVar.append(True,) if self.userFirstNameVar else self.coftMessageVar.append(False,)
            elif x == 'userLastName':
                for z in kwargs['userLastName']:
                    if match(z, str(self.fromLastName)):
                        self.userLastNameVar = True
                self.coftMessageVar.append(True,) if self.userLastNameVar else self.coftMessageVar.append(False,)
            elif x == 'userUsername':
                for z in kwargs['userUsername']:
                    if match(z, str(self.fromUsername)):
                        self.userUsernameVar = True
                self.coftMessageVar.append(True,) if self.userUsernameVar else self.coftMessageVar.append(False,)
            elif x == 'checkUserUsername':
                if kwargs['checkUserUsername']:
                    self.coftMessageVar.append(True,) if 'username' in self.msgFrom else self.coftMessageVar.append(False,)
                else:
                    self.coftMessageVar.append(True,) if 'username' not in self.msgFrom else self.coftMessageVar.append(False,)
            elif x == 'time':
                self.timeVar = kwargs['time']
                if self.timeVar[0] == self.timeZoneHour:
                    if self.timeVar[1] == self.timeZoneMinute:
                        if self.timeVar[2] == self.timeZoneSecond or self.timeVar[2] < self.timeZoneSecond:
                            if self.timeVar[3] == self.timeZoneHour:
                                if self.timeVar[4] == self.timeZoneMinute:
                                    self.coftMessageVar.append(True,) if self.timeVar[5] == self.timeZoneSecond or self.timeVar[5] > self.timeZoneSecond else self.coftMessageVar.append(False,)
                                elif self.tineVar[4] > self.timeZoneMinute:
                                    self.coftMessageVar.append(True,)
                                else:
                                    self.coftMessageVar.append(False,)
                            elif self.timeVar[3] > self.timeZoneHour:
                                self.coftMessageVar.append(True,)
                            else:
                                self.coftMessageVar.append(False,)
                        else:
                            self.coftMessageVar.append(False,)
                    elif self.timeVar[1] < self.timeZoneMinute:
                        if self.timeVar[3] == self.timeZoneHour:
                            if self.timeVar[4] == self.timeZoneMinute:
                                self.coftMessageVar.append(True,) if self.timeVar[5] == self.timeZoneSecond or self.timeVar[5] > self.timeZoneSecond else self.coftMessageVar.append(False,)
                            elif self.tineVar[4] > self.timeZoneMinute:
                                self.coftMessageVar.append(True,)
                            else:
                                self.coftMessageVar.append(False,)
                        elif self.timeVar[3] > self.timeZoneHour:
                            self.coftMessageVar.append(True,)
                        else:
                            self.coftMessageVar.append(False,)
                    else:
                        self.coftMessageVar.append(False,)
                elif self.timeVar[0] < self.timeZoneHour:
                    if self.timeVar[3] == self.timeZoneHour:
                        if self.timeVar[4] == self.timeZoneMinute:
                            self.coftMessageVar.append(True,) if self.timeVar[5] == self.timeZoneSecond or self.timeVar[5] > self.timeZoneSecond else self.coftMessageVar.append(False,)
                        elif self.tineVar[4] > self.timeZoneMinute:
                            self.coftMessageVar.append(True,)
                        else:
                            self.coftMessageVar.append(False,)
                    elif self.timeVar[3] > self.timeZoneHour:
                        self.coftMessageVar.append(True,)
                    else:
                        self.coftMessageVar.append(False,)
                else:
                    self.coftMessageVar.append(False,)
            elif x == 'day':
                self.coftMessageVar.append(True,) if self.timeZoneDay in kwargs['day'] else self.coftMessageVar.append(False,)
            elif x == 'dOTM':
                self.coftMessageVar.append(True,) if self.timeZoneDOTM in kwargs['dOTM'] else self.coftMessageVar.append(False,)
            elif x == 'month':
                self.coftMessageVar.append(True,) if self.timeZoneMonth in kwargs['month'] else self.coftMessageVar.append(False,)
            elif x == 'chatId':
                self.coftMessageVar.append(True,) if self.chatId in kwargs['chatId'] else self.coftMessageVar.append(False,)
            elif x == 'chatType':
                for z in kwargs['chatType']:
                    if z == str(self.chatType):
                        self.chatTypeVar = True
                self.coftMessageVar.append(True,) if self.chatTypeVar else self.coftMessageVar.append(False,)
            elif x == 'chatTitle':
                for z in kwargs['chatTitle']:
                    if match(z, str(self.chatTitle)):
                        self.chatTitleVar = True
                self.coftMessageVar.append(True,) if self.chatTitleVar else self.coftMessageVar.append(False,)
            elif x == 'chatUsername':
                for z in kwargs['chatUsername']:
                    if match(z, str(self.chatUsername)):
                        self.chatUsernameVar = True
                self.coftMessageVar.append(True,) if self.chatUsernameVar else self.coftMessageVar.append(False,)
            elif x == 'checkChatUsername':
                if kwargs['checkChatUsername']:
                    self.coftMessageVar.append(True,) if 'username' in self.msgChat else self.coftMessageVar.append(False,)
                else:
                    self.coftMessageVar.append(True,) if 'username' not in self.msgChat else self.coftMessageVar.append(False,)
            elif x == 'chatFirstName':
                for z in kwargs['chatFirstName']:
                    if match(z, str(self.chatFirstName)):
                        self.chatFirstNameVar = True
                self.coftMessageVar.append(True,) if self.chatFirstNameVar else self.coftMessageVar.append(False,)
            elif x == 'chatLastName':
                for z in kwargs['chatLastName']:
                    if match(z, str(self.chatLastName)):
                        self.chatLastNameVar = True
                self.coftMessageVar.append(True,) if self.chatLastNameVar else self.coftMessageVar.append(False,)
            elif x == 'messageText':
                for z in kwargs['messageText']:
                    if match(z, str(self.msgText)):
                        self.messageTextVar = True
                self.coftMessageVar.append(True,) if self.messageTextVar else self.coftMessageVar.append(False,)
            elif x == 'messageFormat':
                for z in kwargs['messageFormat']:
                    if self.message is not None:
                        if z in self.message:
                            self.messageFormatVar = True
                self.coftMessageVar.append(True,) if self.messageFormatVar else self.coftMessageVar.append(False,)
            elif x == 'messageCaption':
                for z in kwargs['messageCaption']:
                    if match(z, str(self.msgCaption)):
                        self.messageCaptionVar = True
                self.coftMessageVar.append(True,) if self.messageCaptionVar else self.coftMessageVar.append(False,)
        return True if False not in self.coftMessageVar else False
        
    @property
    def timeStamp(self):
        return int(str(datetime.now(timezone(self.timeZone)).timestamp()).split('.')[0])
        
    def trigger(self, **kwargs):
        for a, b in zip(['triggerVar', 'timeZoneDate', 'timeZoneHour', 'timeZoneMinute', 'timeZoneSecond', 'timeZoneDay', 'timeZoneDOTM', 'timeZoneMonth', 'timeStampVar'], ['[]', 'datetime.now(timezone(self.timeZone))', 'int(self.timeZoneDate.strftime("%-H"))', 'int(self.timeZoneDate.strftime("%-M"))', 'int(self.timeZoneDate.strftime("%-S"))', 'int(self.timeZoneDate.strftime("%w"))', 'int(self.timeZoneDate.strftime("%-d"))', 'int(self.timeZoneDate.strftime("%-m"))', 'False']):
            exec(f'self.{a} = {b}')
        if self.accTriggerTime < self.timeStamp:
            for x in kwargs:
                if x == 'time':
                    self.triggerVar.append(True,) if kwargs['time'][0] == self.timeZoneHour and kwargs['time'][1] == self.timeZoneMinute and kwargs['time'][2] == self.timeZoneSecond else self.triggerVar.append(False,)
                elif x == 'day':
                    self.triggerVar.append(True,) if self.timeZoneDay in kwargs['day'] else self.triggerVar.append(False,)
                elif x == 'dOTM':
                    self.triggerVar.append(True,) if self.timeZoneDOTM in kwargs['dOTM'] else self.triggerVar.append(False,)
                elif x == 'month':
                    self.triggerVar.append(True,) if self.timeZoneMonth in kwargs['month'] else self.triggerVar.append(False,)
                elif x == 'timeStamp':
                    for z in kwargs['timeStamp']:
                        if z == self.timeStamp:
                            self.timeStampVar = True
                    self.triggerVar.append(True,) if self.timeStampVar else self.triggerVar.append(False,)
        if False not in self.triggerVar and [] != self.triggerVar:
            self.accTriggerTime = self.timeStamp + 9
        else:
            pass
        return True if False not in self.triggerVar and [] != self.triggerVar else False
        
    def postReq(self, method, **parameter):
        self.requestResponse = loads(post(f'{self.url}{method}', parameter).text)
        if self.requestResponse['ok'] is False:
            post(f'{self.url}sendMessage', {'chat_id': self.chatId, 'text': f'<b>⎆ ERROR {str(self.requestResponse["error_code"])}\nDescription:</b> {self.requestResponse["description"]}\n<b>Line:</b> {str(getframeinfo(stack()[1][0]).lineno)}', 'parse_mode': 'HTML'})
    