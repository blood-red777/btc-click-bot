# Kiếm Tiền Du Học Vlog
# DogeClick Bot Channel from dogeclick.com
# Auto join 5 bot click telegram

import asyncio
import logging
import re
import time
import os
import sys

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

''' DogeClick Bot Channel from dogeclick.com
Options:
1. Dogecoin_click_bot
2. Litecoin_click_bot
3. BCH_click_bot
4. Zcash_click_bot
5. Bitcoinclick_bot
# '''
dogeclick_channel = 'Litecoin_click_bot'

def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

async def main():
	print(Fore.MAGENTA + 'Kiếm Tiền Du Học Vlog \n' + Fore.RESET)
	print(Fore.GREEN + '       ------Kiếm Tiền Du Học Vlog------   \n' + Fore.RESET)
                                
	# Check if phone number is not specified
	if len(sys.argv) < 2:
		print('Usage: python start.py phone_number')
		print('-> Input number in international format (example: +639162995600)\n')
		e = input('Press any key to exit...')
		exit(1)
		
	phone_number = sys.argv[1]
	
	if not os.path.exists("session"):
		os.mkdir("session")
   
	# Connect to client
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()
	
	print(f'Current account: {me.first_name}({me.username})\n')
	print_msg_time('Tool Thành Công!! đang chạy lệnh python 2.py')
	
	# Start command /join
	await client.send_message(dogeclick_channel, '/join')
	
	# Join the channel
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'You must join' in message:	
			channel_name = re.search(r'You must join @(.*?) to earn', message).group(1)
			print_msg_time(f'Joining @{channel_name}...')
			
			# Join the channel
			await client(JoinChannelRequest(channel_name))
			print_msg_time(f'Đang Kiểm Tra...Nếu Không Chạy Là Do App Telegram Lỗi mạng Ở Kênh Join')
			
			# Clicks the joined
			await client(GetBotCallbackAnswerRequest(
				peer=dogeclick_channel,
				msg_id=event.message.id,
				data=event.message.reply_markup.rows[0].buttons[1].data
			))
	
	# Print waiting hours
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def wait_hours(event):
		message = event.raw_text
		if 'You must stay' in message:	
			waiting_hours = re.search(r'at least (.*?) to earn', message).group(1)
			print_msg_time(Fore.GREEN + f'Hoàn Thành! Hãy Giữ Kênh Trong {waiting_hours} Sẽ Nhận Được Coin\n' + Fore.RESET)
			
	# No more ads
	@client.on(events.NewMessage(chats=dogeclick_channel, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'no new ads available' in message:	
			print_msg_time(Fore.RED + 'Đã Hết Kênh Để Tool Join Rồi!\n' + Fore.RESET)
			e = input('Nhấn Enter Và Tiếp Tục Với Lệnh python 1.py +Number Phone')
			exit(1)
			
	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())