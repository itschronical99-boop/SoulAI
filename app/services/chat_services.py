def generate_reply(message:str):
    return{
        "user_message":message,
        "reply":f"You said:{message}"
    }