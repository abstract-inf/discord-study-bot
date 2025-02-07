import random
import os
import re

# Basic ANSI escape sequences for coloring the text in print statements
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"  # Purple color
CYAN = "\033[36m"  # Cyan color
WHITE = "\033[97m"  # White color
RESET = "\033[0m"  # Reset color

def greeting(msg):
    # a list of some of the possible greetings that the user might say
    possible_user_greetings = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening', 'good night',
                      'howdy', 'sup', 'what\'s up', 'yo', 'hi there', 'hello there', 'hey there', 'hiya', 'heya', 'hola',
                      'bonjour', 'salut', 'ciao', 'hallo', 'namaste', 'salaam', 'salam', 'shalom', 'konnichiwa', 'ohayo', 'konbanwa',
                      'konnichiha', 'konbanha', 'koncha', 'moshi moshi', 'nihao', 'nihaoma', 'nihaohao', 'nihaoh', 'nihaohao ma',
                      'مرحبا', 'مرحباً', 'مرحباً بك', 'مرحبا بك', 'مرحب', 'مرحبا بكم', 'مرحباً بكم', 'مرحبا بكما', 'مرحباً بكما',
                      'اهلا', 'اهلاً', 'اهلا بك', 'اهلاً بك', 'اهلا بكم', 'اهلاً بكم', 'اهلا بكما', 'اهلاً بكما', 'اهلا وسهلا', 'اهلا وسهلاً',
                      'كيفك', 'كيف حالك', 'كيف الحال', 'كيف الاحوال', 'كيف الاحوال', 'كيف الحالات', 'كيف الاحوال الصحية', 'كيف الاحوال الصحية',
                      'الو', 'السلام عليكم', 'سلام', 'السلام عليكم ورحمة الله وبركاته', 'السلام عليكم ورحمة الله', 'السلام عليكم ورحمة الله وبركاته']

    bad_words = [
        "anal", "anus", "arse", "ass", "asshole", "ass hole", "balls", "ballsack", "bastard", "biatch", "bitch", "bloody",
        "blow job", "blowjob", "bollock", "bollok", "boner", "boob", "bugger", "bum", "butt", "buttplug",
        "clitoris", "cock", "cum", "cumming" "coon", "crap", "cunt", "damn", "dick", "dildo", "dyke", "fucking", "fag",
        "feck", "felching", "fellate", "fellatio", "flange", "fuck", "fudge packer", "fudgepacker",
        "God damn", "Goddamn", "homo", "jerk", "jizz", "knob end", "kill yourself", "kys", "knobend", "labia", "lmao",
        "lmfao", "muff", "nigga", "nigger", "omg", "penis", "piss", "poop", "prick", "pube", "pussy",
        "queer", "s hit", "scrotum", "sex", "sh1t", "shit", "shitting", "slut", "smegma", "spunk", "tit", "tosser",
        "turd", "twat", "vagina", "wank", "whore", "wtf", "سكس", "طيز", "شرج", "لعق", "لحس", "مص",
        "تمص", "بيضان", "ثدي", "بز", "بزاز", "حلمة", "مفلقسة", "بظر", "كس", "فرج", "شهوة", "شاذ",
        "مبادل", "عاهرة", "جماع", "قضيب", "زب", "لوطي", "لواط", "سحاق", "سحاقية", "اغتصاب", "خنثي",
        "احتلام", "نيك", "متناك", "متناكة", "شرموطة", "عرص", "خول", "قحبة", "لبوة"
]
    # handle bad words
    if any(
        re.search(
            r'\b' + ''.join(f'{re.escape(letter)}[^a-zA-Z]*' for letter in bad_word if letter.isalpha()) + r'\b',
            msg,
            flags=re.IGNORECASE
        )
        for bad_word in bad_words
    ):
        bad_words_responses = ["Oh, fantastic. That's exactly what I wanted to hear. 🙄",
                                "You must be having a great time with this, huh? Well, I'm not. 😤",
                                "Wow, you're really pushing it now. Keep it up and see what happens. 😡",
                                "Seriously? Is this what you call a conversation? 🤦‍♂️",
                                "That's a great way to get on my bad side. Just saying.",
                                "If you think that's funny, you're sadly mistaken. 😑",
                                "Keep talking like that and I'll stop reading your messages. 👎",
                                "Is this supposed to impress me? Because it's not. 🙄",
                                "Oh, this is just perfect. Nothing better than being disrespected. 🙃",
                                "You've got a real talent for annoying people, huh? Good job. 👏"
                                ]

        return random.choice(bad_words_responses)

    # handle greetings
    if msg.strip().split()[0] in possible_user_greetings:
        # possible responses that the bot can respond with
        responses = ["Hello! How's it going?",
            "Hey there! 👋",
            "Hi! What's up?",
            "Greetings! Hope you're having a great day!",
            "Hello, friend! 😊",
            "Hey! How can I assist you today?",
            "Hi! Need anything?",
            "Hello! Always a pleasure to chat.",
            "Hey! Nice to see you!",
            "Hi! What's on your mind?",
            "Hello! How can I help you?",
            "Hey! How can I be of service?",
            "Hi! How can I assist you today?",
            "Hello! What's new?",
            "Hey! What's new with you?",
            "Hi! How are you doing today?",
            "Hello! How are you today?",
            "Hey! How's your day going?",
            "Hi! How's your day going?",
            "Hello! How's everything?",
            "Hey! How's everything going?"
        ]
        response = random.choice(responses)
        return response
    
def send_sound_file(msg):
    sound_files = {
        'amro is': 'media/CDs/amro/amro.jpg',
        'bin rami is': 'media/CDs/brami/bin rami.jpg',
        'bin bilal is': 'media/CDs/bilal/علاوي.wav',
        'bilal is': 'media/CDs/bilal/علاوي.wav',
        '$bin bilal is': 'media/CDs/bilal/علاوي.wav',
        '$bilal is': 'media/CDs/bilal/علاوي.wav'
    }

    if msg in sound_files and os.path.exists(sound_files[msg]):
        print(f"{GREEN}Sent media file for:{RESET} {msg}")
        return {'file': sound_files[msg]} # this is the format for sending a file


def send_logs(msg):
    if msg == '!study_logs':
        print(f"{GREEN}Sent study_logs.csv{RESET}")
        return {'file': 'study_logs.csv'} # this is the format for sending a file
    elif msg == '!channel_logs':
        print(f"{GREEN}Sent channel_logs.csv{RESET}")
        return {'file': 'channel_logs.csv'} # this is the format for sending a file
    

def find_response(msg):
    # a list of all the functionalities that the bot can do based on the message
    functionalities = [greeting, send_sound_file, send_logs]

    # iterate over the functionalities to find which response to return
    for function in functionalities:
        response = function(msg) # call the function with the message
        if response:
            return response
    
    # if no response was found, return None
    return None


if __name__ == '__main__':
    input_message = input("Enter a message: ")
    response = find_response(input_message)

    if response:
        print(response)
    else:
        print("No response found")