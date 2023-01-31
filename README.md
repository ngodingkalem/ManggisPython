# ManggisPython

ManggisPython adalah sebuah script untuk Bot Telegram yang menggunakan metode long polling, dan di jalankan dengan bahasa pemrograman Python.

## Modul

- requests
- json
- sys
- time
- datetime
- pytz
- re
- inspect

## Mengatur Token Bot dan Zona Waktu

Ubah `BOT_TOKEN` dan `TIME_ZONE` sesuai dengan token bot dan zona waktu user.

```python
bot = Telegram('1234567890:AAEbM9Unep5MSrjNGlJHZNqbVBROg6librw', 'Etc/GMT-7')
```

| Time Zone | Zona Waktu |
| :-: | :-: |
| Etc/GMT-7 | Waktu Indonesia Bagian Barat |
| Etc/GMT-8 | Waktu Indonesia Bagian Tengah |
| Etc/GMT-9 | Waktu Indonesia Bagian Timur |

## centMessage

`centMessage` digunakan untuk mengecek apakah ada pesan masuk atau tidak. 

## coftMessage()

`coftMessage()` di gunakan untuk memfilter atau mengecek sebuah pesan, apabila sesuai maka pesan tersebut akan diterima dan dibalas sesuai pengaturan user. Dengan memasukkan beberapa parameter yang tersedia di bawah ini.

| Argumen | Isi Argumen | Jumlah Isi | Tipe | Regex | Dicocokkan Dengan Field/Properti | Deskripsi |
| :- | :- | :- | :- | :- | :- | :- |
| `userId` | Opsional | ∞ | Integer | Tidak | `fromId` | Mengecek id user. |
| `userFirstName` | Opsional | ∞ | String | Ya | `fromFirstName` | Mengecek nama depan user. |
| `userLastname` | Opsional | ∞ | String | Ya | `fromLastName` | Mengecek nama akhir user. |
| `userUsername` | Opsional | ∞ | String | Ya | `fromUsername` | Mengecek username user. |
| `checkUserUsername` | `True` atau `False` | 1 | Booelan | Tidak | `msgFrom` | Mengecek apakah user menggunakan username atau tidak. `True` untuk Ya, `False` untuk tidak. |
| `time` | `0` - `23`, `0` - `59`, `0` - `59` | 6 | Integer | Tidak | `timeZoneHour`, `timeZoneMinute` dan `timeZoneSecond` | Mengecek apakah waktu dimana pesan diterima sama seperti yang telah di atur di argumen `time`. Contoh `time=[1, 30, 30, 23, 0, 5]`, artinya hanya menerima pesan di antara jam `01.30.30` sampai `23.00.05`. |
| `day` | `0` - `6` | ∞ | Integer | Tidak | `timeZoneDay` | Mengecek apakah hari dimana pesan diterima sama seperti yang telah di atur di argumen `day`. Contoh `day=[0, 5]`, artinya hanya menerima pesan di hari `Ahad` dan `Kamis`. |
| `dOTM` | `1` - `31` | ∞ | Integer | Tidak | `timeZoneDOTM` | Mengecek apakah tanggal dimana pesan diterima sama seperti yang telah di atur di argumen `dOTM`. Contoh `dOTM=[29, 3]`, artinya hanya menerima pesan di tanggal `29` dan `3`. |
| `month` | `1` - `12` | ∞ | Integer | Tidak | `timeZoneMonth` | Mengecek apakah bulan dimana pesan diterima sama seperti yang telah di atur di argumen `month`. Contoh `month=[2, 11]`, artinya hanya menerima pesan di bulan `Februari` dan `November`. |
| `chatId` | Opsional | ∞ | Integer | Tidak | `chatId` | Mengecek id chat. |
| `chatType` | `private`, `group`, `supergroup` atau `channel` | ∞ | String | Tidak | `chatType` | Mengecek tipe chat. Isi argumen bisa saja berbeda, tergantung pada tipe chat yang tersedia di `https://core.telegram.org/bots/api`. |
| `chatTitle` | Opsional | ∞ | String | Ya | `chatTitle` | Mengecek title chat. |
| `chatUsername` | Opsional | ∞ | String | Ya | `chatUsername` | Mengecek usename chat. |
| `checkChatUsername` | `True` atau `False` | 1 | Booelan | Tidak | `msgChat` | Mengecek apakah chat menggunakan username atau tidak. |
| `chatFirstName` | Opsional | ∞ | String | Ya | `chatFirstName` | Mengecek nama depan chat. |
| `chatLastName` | Opsional | ∞ | String | Ya | `chatLastName` | Mengecek nama akhir chat. |
| `messageText` | Opsional | ∞ | String | Ya | `msgText` | Mengecek teks pesan. |
| `messageFormat` | `animation`, `audio`, `document`, `photo`, `sticker`, `video`, `video_note`, `voice`, `contact`, `dice`, `game`, `poll`, `venue`, `location`, `invoice` | ∞ | String | Tidak | `message` | Mengecek format pesan. Isi argumen bisa saja berbeda, tergantung pada format pesan di `https://core.telegram.org/bots/api` |
| `messageCaption` | Opsional | ∞ | String | Ya | `msgCaption` | Mengecek caption dari pesan `animation`, `audio`, `document`, `photo`, `video`, `atau` `voice`. |

## postReq()

Gunakan `postReq()` untuk request ke api Telegram. Contoh:

```python
postReq('sendMessage', text='Hello Wolrd!', chat_id=1234567890)
```

## getField()

Gunakan `getField()` untuk mendapatkan field sesuai keinginan. Contoh:

```python
getField('message.from.chat_id')
```

## Field/Properti Bawaan

```
message = result⪼message
msgId = message⪼id
msgFrom = message⪼from
fromId = message⪼from⪼id
fromFirstName = message⪼from⪼first_name
fromLastName = message⪼from⪼last_name
fromUsername = message⪼from⪼username
msgDate = message⪼date
msgChat = message⪼chat
chatId = message⪼chat⪼id
chatType = message⪼chat⪼type
chatTitle = message⪼chat⪼title
chatUsername = message⪼chat⪼username
chatFirstName = message⪼chat⪼first_name
chatLastName = message⪼chat⪼last_name
msgText = message⪼text
msgCaption = message⪼caption
```

| Properti | Value |
| :- | :- |
| `timeStamp` | Cap waktu(jumlah detik) |
| `timeZoneHour` | Jam |
| `timeZoneMinute` | Menit |
| `timeZoneSecond` | Detik |
| `timeZoneDay` | Hari dalam angka(dimulai dari angka 0) |
| `timeZoneDOTM` | Tanggal |
| `timeZoneMonth` | Bulan dalam angka |


## trigger()

Gunakan `trigger()` untuk melakukan pesan terjadwal. Dengan memasukkan beberapa argumen yang tersedia di bawah ini

| Argumen | Isi Argumen | Jumlah Isi | Tipe | Regex | Dicocokkan Dengan Properti | Deskripsi |
| :- | :- | :- | :- | :- | :- | :- |
| `time` | `0` - `24`, `0` - `59`, `0` - `59` | 3 | Integer | Tidak | `timeZoneHour`, `timeZoneMinute` dan `timeZoneSecond` | Mengecek apakah waktu dimana pesan diterima sama seperti yang telah di atur di argumen `time`. Contoh `time=[1, 30, 0]`, artinya hanya menerima di jam `01.30.00`. |
| `day` | `0` - `6` | ∞ | Integer | Tidak | `timeZoneDay` | Mengecek apakah hari sekarang sama seperti yang telah di atur di argumen `day`. Contoh `day=[0, 5]`, artinya hanya menerima di hari `Ahad` dan `Kamis`. |
| `dOTM` | `1` - `31` | ∞ | Integer | Tidak | `timeZoneDOTM` | Mengecek apakah tanggal sekarang sama seperti yang telah di atur di argumen `dOTM`. Contoh `dOTM=[29, 3]`, artinya hanya menerima di tanggal `29` dan `3`. |
| `month` | `1` - `12` | ∞ | Integer | Tidak | `timeZoneMonth` | Mengecek apakah bulan sekarang sama seperti yang telah di atur di argumen `month`. Contoh `month=[2, 11]`, artinya hanya menerima di bulan `Februari` dan `November`. |
| `timeStamp` | Opsional | ∞ | Integer | Tidak | `timeStamp` | Mengecek apakah `timeStamp` sekarang sama seperti yang telah di atur di argumen `timeStamp`. |

> `trigger()` mempunyai cooldown 10 detik.

## Contoh

```python
from module import Telegram

bot = Telegram('5813820926:AAEbN9Unep4MSrjMGlJHZNqbVKROg9librw', 'Etc/GMT-7')

while True:
    if bot.centMessage:
        if bot.coftMessage(messageText=['/start'], chatType=['private']):
            bot.postReq('sendMessage', reply_to_message_id=bot.msgId, chat_id=bot.chatId, text='Hai kak!')
        elif bot.coftMessage(messageFormat=['photo']):
            bot.postReq('sendMessage', text='Hemm...', chat_id=bot.getField('message.chat.id'))
        elif bot.coftMessage(messageText=['/time'], time=[7, 18, 00, 9, 53, 00]):
            bot.postReq('sendMessage', chat_id=bot.chatId, text='Saat ini bot online!')
        elif bot.coftMessage(messageText=['/time']):
            bot.postReq('sendMessage', chat_id=bot.chatId, text='Saat ini bot offline!')
        elif bot.coftMessage(messageFormat=['contact']):
            bot.postReq('sendMessage', chat_id=bot.chatId, text='Nomor siapa itu kak?', reply_to_message_id=bot.msgId)
        elif bot.coftMessage(messageText=['/namadepan'], userFirstName=['admin']):
            bot.postReq('sendMessage', chat_id=bot.chatId, text=f'Anda adalah {bot.fromFirstName}')
        elif bot.coftMessage(messageText=['/namadepan']):
            bot.postReq('sendMessage', chat_id=bot.chatId, text='Anda bukan admin\!, silahkan ubah nama depan anda dengan *admin*', parse_mode='MarkdownV2')
        elif bot.coftMessage(messageText=['/day'], day=[3]):
            bot.postReq('sendMessage', text='Sekarang hari rabu!', chat_id=bot.chatId)
        elif bot.coftMessage(messageText=['/start'], chatType=['group'], chatTitle=['Tes Bot']):
            bot.postReq('sendMessage', chat_i=bot.chatId, text=f'Hai member group{bot.chatTitle}')
    if bot.trigger(time=[21, 10, 00], dOTM=[34] day=[0], month=[1, 2]):
        bot.postReq('sendMessage', chat_id=bot.chatId, text='Sekarang jam 21:10:00!')
```

Agar lebih mudah untuk dipahami bisa di tulis seperti di bawah ini

```python
from module import Telegram

bot = Telegram('5813820926:AAEbN9Unep4MSrjMGlJHZNqbVKROg9librw', 'Etc/GMT-7')

while True:
    if bot.centMessage:
        if bot.coftMessage(messageText=['/start'], chatType=['private']):
            bot.postReq('sendMessage', reply_to_message_id=bot.msgId, chat_id=bot.chatId, text='Hai kak!')
            
        elif bot.coftMessage(messageFormat=['photo']):
            bot.postReq('sendMessage', text='Hemm...', chat_id=bot.getField('message.chat.id'))
            
        elif bot.coftMessage(messageText=['/time'], time=[7, 18, 00, 9, 53, 00]):
            bot.postReq('sendMessage', chat_id=bot.chatId, text='Saat ini bot online!')
            
        elif bot.coftMessage(messageText=['/time']):
            bot.postReq('sendMessage', chat_id=bot.chatId, text='Saat ini bot offline!')
            
        elif bot.coftMessage(messageFormat=['contact']):
            bot.postReq('sendMessage', chat_id=bot.chatId, text='Nomor siapa itu kak?', reply_to_message_id=bot.msgId)
            
        elif bot.coftMessage(messageText=['/namadepan'], userFirstName=['admin']):
            bot.postReq('sendMessage', chat_id=bot.chatId, text=f'Anda adalah {bot.fromFirstName}')
            
        elif bot.coftMessage(messageText=['/namadepan']):
            bot.postReq('sendMessage', chat_id=bot.chatId, text='Anda bukan admin\!, silahkan ubah nama depan anda dengan *admin*', parse_mode='MarkdownV2')
            
        elif bot.coftMessage(messageText=['/day'], day=[3]):
            bot.postReq('sendMessage', text='Sekarang hari rabu!', chat_id=bot.chatId)
            
        elif bot.coftMessage(messageText=['/start'], chatType=['group'], chatTitle=['Tes Bot']):
            bot.postReq('sendMessage', chat_i=bot.chatId, text=f'Hai member group{bot.chatTitle}')
            
    if bot.trigger(time=[21, 10, 00], dOTM=[34] day=[0], month=[1, 2]):
        bot.postReq('sendMessage', chat_id=bot.chatId, text='Sekarang jam 21:10:00!')
```

## Lisensi

Lihat lisensi di file LICENSE
