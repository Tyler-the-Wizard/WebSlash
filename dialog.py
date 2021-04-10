import settings

def popup(message):
    settings.dialog_busy = True
    settings.dialog_message = message