from OrekiProm import ND, OWNER_ID


if __name__ == "__main__":
     ND.run()
     with ND:
         ND.send_message(chat_id=OWNER_ID, text="🆒 lvl up!")
