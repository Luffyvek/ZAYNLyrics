#!/usr/bin/env python3

import tweepy
import random
import time
import os
import ast
from datetime import datetime, timedelta
from dotenv import load_dotenv



# File to keep track of posted lyrics
POSTED_LYRICS_FILE = 'posted_lyrics.txt'


# Replace these values with your Twitter API credentials
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# Lyrics of the song (replace with your favorite artist's song lyrics)
lyrics = [
        #Dreamin
        "One, two, three, go",
        "Yeah, I'm dreamin' my life away",
        "I’ve been dreamin', feelin' this way. I've been needin' something else\nI'll know what it is when I see it",
        "Did I mention life's intention never steered me the right way?",
        "Say I've been fallin' in love and in the mornin' thеn I feel nothing again",
        "Don't call me again, when you faded, no need to call me again",
        
        #What I Am
        "Am I crazy? Am I foolish? Am I stupid for playin' these games with you?",
        "If I told you I loved you would you say that it's fucked up?",
        "Don't take me for what I'm sayin', just take me for what I am ",
        "Livin' in the moment feels good to me till it hurts and I need somebody",
        "Ain't no conspiracy that can save me",
        "I've been readin' old shit and I can't make sense of it",
        "Don't take me for what I'm sayin', just take me for what I am\n'Cause this is where I'm stayin', my two feet are in the sand",
        "Take me as I am\nI'm tired of dancin' around the point\nSharp and it is jagged\nLike the shape of glass and it steals my voice",
        
        #Grateful
        "I'm grateful for you",
        "Love it when the rain comes down, love it when the waves calm down",
        "And it feels good and I knew it would",
        "When I'm tellin' this story it's complicated, some mishaps I've been mournin' but I'm grateful for it",
        "These days I live to my depiction, nowadays I'm findin' no affliction\nThese days I'm needin' no restriction, feel like I'm finding new addiction",
        "Things change and I'm okay with what I'm not",
        "It feels wasteful to be hateful, I'll be grateful for what I got",
        "Things change and I'm okay with what I'm not\nIt feels wasteful to be hateful, I'll be grateful for what I got",
        
        #Alienated
        "No two people are the same",
        "Stand beside you, but just far enough away",
        "See, I feel alright already on my own",
        "Can you let me be intoxicated on my own?",
        "Do I need to answer or right my wrongs?",
        "Am I home if I don't know this place?",
        "I've been feeling alienated on my spaceship alone",
        "Say goodbye to the past, leave it all with a laugh",
        "Know my reasons for the pain but if you brought it in front of me, I know I'd do it all again",
        "I know from all the years that my feelings nеver change",
        "Did the winds make the noise of change?",
        "Can the wings on your skin help you fly away?",
        "'Cause it's always raining and the clouds are always grey when you're away",

        #My Woman
        "Love me partly, leave me tonight. Say, 'Don't fall in pieces,' I might\nJust for the fun of it, let my mind just roll with it tonight",
        "Love me partly, leave me tonight",
        "I fill my cup to forget her",
        "This is my dеmise",
        "I fill my cup to forget her, known it from the get up. This is my dеmise",
        "Where did you wanna go? Where did you stay last night? Save my mind, save my time",
        "Yeah, I know, I've been holdin’ on to somethin’ for so long, with no eyes. Yeah, I've been blind",
        "Where did you wanna go? Where did you stay last night? Save my mind, save my time\nYeah, I know, I've been holdin’ on to somethin’ for so long, mm, with no eyes. Yeah, I've been blind",
        "Just for the fun of it tonight",

        #How It Feels
        "I've been getting old standin' by the river, watch the water move but I don't move with her\nShivers down my spine, never forget to remind me I'm alive",
        "I've been getting old standin' by the river, watch the water move but I don't move with her",
        "Shivers down my spine, never forget to remind me I'm alive",
        "Till I let go of this moment, something holdin' me to this place",
        "I've been breakin', always fakin', I'm just lyin' to your face and I can't tell you how it feels",
        "Can you tell me just one thing? Can you give me a reason to stay?\n'Cause the feelings I'm harborin' don't seem to see the light of day",
        "Can you give me a reason to stay?",
        "The feelings I'm harborin' don't seem to see the light of day",
        "Bring me to my knees, I begged and pleaded, I asked to leave\nBut you insisted on stayin' and breakin' my heart",
        "I begged and pleaded, I asked to leave\nBut you insisted on stayin' and breakin' my heart",

        #Stardust
        "Pretty Christmas on a cardboard cup, I wait outside for you to pick me up",
        "There's somethin' different in the way you touch, Different in the way you love",
        "Feels like stardust, floatin' all around us, shootin' right across a big black sky",
        "Feels like stardust, fallin' all around us, funny how it found us\nMaybe I, maybe I",
        "I love to be there with you and I love to be there, baby too\n'Cause you make anywhere at all feel like stardust",
        "You make anywhere at all feel like stardust",

        #Gates of Hell
        "So fucked, I can't feel my face",
        "Know a couple people might call me a disgrace but fuck them, I ain't looking up",
        "Ain't never been one to give a second look",
        "I don't like you very much but I keep putting up with your shit",
        "I don't like you very much",
        "We drift away like islands and I wanna float on this wave\nA different day, time and meaning and I know I'd do it all the same",
        "You always come to mind when I think to myself what could have been if we were living in Utopia",

        #Birds On A Cloud
        "Please give me one more day of happiness. I need it, I need it",
        "Know when something's wrong, but somethin' inside tells me it's all okay. Even if it's strange, it's our love",
        "Even if it's strange, it's our love",
        "From this place I'm runnin' from, I hope I kept my grace",
        "From this place I'm runnin' from, I know I can't escape",
        "From this place I'm runnin' from, I hope I kept my grace\nFrom this place I'm runnin' from, I know I can't escape",
        "When I think of things lost, think I fell off, took my foot off the pedal\nThink it's all suss and once I make a fuss, I don't need any medals",

        #Concrete Kisses
        "All I wanted was a cup of coffee, I got somethin' else or so it seems\nConcrete kisses on my face and forehead from where I fell last night on the street\nWhen I fell hard, all these scars on my skin where you left marks",
        "This might not sound right, but it's alright, it's real\nI'm finding my way on the highway this year",
        "All I wanted was a cup of coffee",
        "This might not sound right, but it's alright, it's real",
        "I'm finding my way on the highway this year",
        "Got a big ol' cup of shit, told me to drink it, Middle finger to what you believe",
        "Beginnings have a habit of endin'\nPurgatory, I'm stuck here in between",
        "Middle finger to what you believe",
        "Beginnings have a habit of endin'",
        "Why does this pain feel so good? Pumpin' my brain like drunk blood",
        "Feeling this way, there's no such thing as happy endings",
        "See on my face, my heart changed",
        "Realize that I'm too good for games we've been playin'",
        "Why does this pain feel so good?",

        #False Starts
        "Fast car, fast heart, trouble in my brain\nBig dreams, false starts and I know I've changed",
        "Don't want the things we can't have",
        "Old rooms, new paint, still it looks the same",
        "Sad thoughts, bad luck, with no one to blame",
        "They say the trouble don't last",
        "Sometimes the pain makes me laugh",
        "It's hard, but it only gets harder",
        "Tonight we can go it alone",
        "No one ever has to know\nNo one ever has to know\nNo one ever has to know",
        "No one ever has to know but I know I have to go",
        "I'm shakin', my heart's naked out of control, oh-oh-oh, oh-oh-oh, oh-oh",
        "oh-oh-oh, oh-oh-oh, oh-oh, oh-oh-oh, oh-oh-oh, oh-oh, oh-oh-oh, oh-oh-oh, oh-oh, oh-oh-oh, oh-oh-oh, oh-oh,oh-oh-oh, oh-oh-oh, oh-oh",
        "What do you want? We don't havе to stay\nTrust me you're not gonna crash",
        "Old rooms, new paint, still it looks the same\nSad thoughts, bad luck, with no one to blame",
        "It's hard, but it only gets harder. Tonight we can go it alone",

        #The Time
        "Yesterday just came and went and if today I wake up late, I won't forgive myself",
        "Never fell for the fame thing, they fell in love with the same things\nLet me know when the rain ends, see all I need is you",
        "All I need is you",
        "Ain’t it special? Ain't it precious? The time that we have\nWhen I'm laid in your bed and you tell me you lovе me",
        "Ain’t it special? Ain't it precious? The time that we have",
        "Feedin' families, forget the fame, I'm doing it now for a second name",
        "I could cry when you tell me that you love me and I'd die for you if you asked me to",
        "I'd die for you if you asked me to",

        #Something In The Water
        "Must be somethin' in the water, I can feel you in the atmosphere",
        "Don't say much until we speak in tongues, One-on-one, swear you flowin' through my blood",
        "Must be somethin' in the water",
        "Am I goin' out my mind?",
        "Said it was the last, last two or three times, spent the whole day till we woke up last night. Nothing's makin' sense no more",
        "Nothing's makin' sense no more",
        "Caught a glimpse of you gaze, I was frozen\nGot a grip on my heart, now it's stolen\nHad a lock on the door, now it's open",
        "Must be somethin' in the water\nI can feel you in the atmosphere\nDon't say much until we spеak in tongues, One on one\nSwеar you flowin' through my blood",
        "Got me drippin' in that old school love, pour me some, feelings got me goin' numb\nMust be somethin' in the water",
        "You got my heart doin' things it don't do but I'm not gon' fight it",
        "You got my heart doin' things it don't do but I'm not gon' fight it\nYou’re in control, just show me what to do, I'm not afraid",
        "I might let myself sink deep into the bottom, can't hear myself think\n'Cause all I wanna hear is your voice pull me out of that void\nIt's an instinct, I don't have a choice tonight",
        "Must be somethin' in the water, on the edge until you pull me in\nGot me drippin' in that old school love, pour me some, feelings got me goin' numb",
        "Must be somethin' in the water, in the water",

        #Shoot At Will
        "Just took a drag, oh, ain't it a drag? When you feel like history's pullin' you back",
        "I've been runnin' bare feet in a field. Yeah, a dream gon' bad 'Cause it feels like history's pullin' me back",
        "When I look at her, all I see is you\nWhen you look at her, do you see me too?",
        "Does it not occur to you? Do you not prefer the truth? I was in love with you though I didn't show the proof",
        "I hold my hands up for the firing squad and if you want, you can take it all. I don't really know, I can't give no more",
        "Shoot at will because she shoots to kill and I'm dyin' inside",
        "I hold my hands up for the firing squad and if you want, you can take it all. I don't really know, I can't give no more\nShoot at will because she shoots to kill and I'm dyin' inside",

        #Fuchsia Sea
        "I'm tired of the grey, I'm sick of the pain\nI'm tired of the pain,I'm sick of the grey",
        "I gotta love this feelin' to keep myself from dreamin' about somethin' else",
        "You keep me entertained 'cause I saw the flame, and you still walked through it",
        "I bet you knew it, that I would do it if I'm given the chance",
        "Ferocious devotion",
        "I can't keep it up, I'm fallin' into motion",
        "Ferocious devotion\nI can't keep it up, I'm fallin' into motion",
        "How can you break when you're broken to begin with?",
        "I can't see it with you, I can't live with you. Don't you hear me when I'm talkin'?",
        "I gotta love this feelin' to keep myself from dreamin' about somethin' else\nYou keep me entertained 'cause I saw the flame, and you still walked through it",
        "I'm tired of the grey, I'm sick of the pain\nI'm tired of the pain, I'm sick of the grey",

    # Add more lyrics here
]

# Function to load posted lyrics from a file
def load_posted_lyrics():
    if os.path.exists(POSTED_LYRICS_FILE):
        with open(POSTED_LYRICS_FILE, 'r') as file:
            posted_lyrics = set(line.strip().replace('<newline>', '\n') for line in file)
            print(f"Loaded posted lyrics: {posted_lyrics}")
            return posted_lyrics
    return set()

# Function to save posted lyrics to a file
def save_posted_lyrics(lyric):
    with open(POSTED_LYRICS_FILE, 'a') as file:
        file.write(f"{lyric.replace('\n', '<newline>')}\n")
    print(f"Saved lyric: {lyric}")

# Function to authenticate to Twitter using API v2
def authenticate():
    client = tweepy.Client(bearer_token=BEARER_TOKEN,
                           consumer_key=API_KEY,
                           consumer_secret=API_SECRET_KEY,
                           access_token=ACCESS_TOKEN,
                           access_token_secret=ACCESS_TOKEN_SECRET)
    return client

# Function to tweet a random lyric using API v2
def tweet_lyric(client, posted_lyrics):
    remaining_lyrics = [lyric for lyric in lyrics if lyric not in posted_lyrics]
    print(f"Remaining lyrics: {remaining_lyrics}")
    if not remaining_lyrics:
        print("All lyrics have been posted. Exiting.")
        return False  # Stop the script if all lyrics have been posted

    lyric_to_post = random.choice(remaining_lyrics)
    print(f"Lyric to post: {lyric_to_post}")
    response = client.create_tweet(text=lyric_to_post)
    if response and response.data and response.data.get('id'):
        print(f"Successfully posted: {lyric_to_post}")
        save_posted_lyrics(lyric_to_post)
        posted_lyrics.add(lyric_to_post)  # Add the lyric to the posted_lyrics set
        return True
    else:
        print(f"Failed to post the lyric: {lyric_to_post}. Response: {response}")
        return False  # Stop the script if posting fails
        
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        timeformat = f"{hours:02}:{mins:02}:{secs:02}"
        print(f"Time for a new tweet is in {timeformat}", end='\r')
        time.sleep(1)
        seconds -= 1


def main():
    client = authenticate()
    posted_lyrics = load_posted_lyrics()
    
    while tweet_lyric(client, posted_lyrics):
        next_tweet_time = datetime.now() + timedelta(hours=6)
        print(f"Time for a new tweet is at {next_tweet_time.strftime('%Y-%m-%d %H:%M:%S')}")

        # Wait 6 hours before posting the next lyric
        time.sleep(6 * 3600)
        

if __name__ == "__main__":
    main()
