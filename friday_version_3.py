from command_modules import *

wake = ""
listening: bool = True
command_list = {
    "play a song": play,
    "tell me a joke": jokes,
    "search google": google_search,
    "what time is it": what_time,
    "search wikipedia": wiki_search,
    "tell me the weather": my_weather,
    "take note": my_note,
    "open note": open_note,
    "read me a book": read_book}


def run_jarvis():
    check_first_time()
    while True:
        commands = get_audio()
        if commands.count(wake.lower()) > 0:
            speech(f"What can I do for you, {get_user_name()}?")
            commands = get_audio().lower()
            if commands == "shut yourself down":
                speech("Awww. I'm shutting down, but missing you already.")
                break
            elif commands in command_list.keys():
                command_list[commands]()
            else:
                speech("Hmm. That feature isn't available, yet.")


run_jarvis()
