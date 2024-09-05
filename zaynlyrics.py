import tweepy
import random
import time
import os
from datetime import datetime, timedelta

# File to keep track of posted lyrics
POSTED_LYRICS_FILE = 'posted_lyrics.txt'

# Replace these values with your Twitter API credentials
API_KEY = '3R8iAL9UZy6joaGvJmpAsj0Um'
API_SECRET_KEY = 'hkBJUp3HfjxOWxXZeJHhBMn5HPuemoS12S0u0GqUkT6h1jTVev'
ACCESS_TOKEN = '1698957609204662272-gtBPnsEmoeCKFW2FyR3xBc7Ssaedql'
ACCESS_TOKEN_SECRET = '0NCLCPBL4L3qZ2hzjmCFf1V9eWizsuTvaTGLUSRP3gNCw'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAH7KuwEAAAAAqog8WCTYoz4JTat1FL1%2BGBVpiCs%3Dr8eClhSxlIH6AkGbGsVLKJFQvmXJF3FGRT665XneADheplygVO'  # Required for API v2

#MoM
lyrics = [
        #Let Me
        "Sweet baby, our sex has meaning",
        "Baby, let me be your man, so I can love you",
        "Baby, let me be your man, so I can love you \nAnd if you let me be your man then I'll take care of you",
        "For the rest of my life, for the rest of yours, for the rest of ours",
        "Baby, let me be your man, so I can love you \nAnd if you let me be your man then I'll take care of you\nFor the rest of my life, for the rest of yours, for the rest of ours",
        "We're drinkin' the finest label, dirty dancing on top of the table",
        "Long walks on the beach in April",
        "I promise, darling, that I'll be faithful",
        "Give me your body and let me love you like I do",
        "Come a little closer and let me do those things to you",
        "This feelin' will last forever, baby, that's the truth",
        "For the rest of my life, for the rest of yours\nFor the rest of ours",

        #Natural
        "It's just like breathin', speakin', when we touch, like a force of nature",
        "Not just a feelin', let's believe it, the birth of love like a force of nature",
        "Undeniable, unforgettable, it's our love",
        "Nothing compares to when I feel you on my skin. It feels so natural, natural",
        "It feels so natural, natural, when we come together, like a force of nature",
        "Pure heart, deeper\nBeautiful, like the bluest ocean\nLike a wave, we broke down\nThe barriers, like the bluest ocean",
        "It's incredible, unforgettable (It's our love)",
        "Nothing compares to when I feel you on my skin",
        "Like a hurricane when we come together",
        "Let's come together, come together, right now, right now",

        #Back To Life
        "What if I changed my mind? What if I said it's over?",
        "I been flying so long, can't remember what it was like to be sober",
        "What if I lost my lives? What if I said game over? What if I forget my lines and I lose all my composure?",
        "Honestly she's the only one that's watching over me, gives me oxygen when it gets hard to breathe",
        "If I'm wrong or right, she's always on my side",
        "If I lose the fight, I know she'll bring me back, bring me back to life",
        "What if we never met? What if I never saw her?",
        "I've been burning up for so long in a world that just keeps getting colder",
        "I know she'll bring me back, bring me back to life",
        "Nobody does this like you",
        "I've been around the world, I seen a lot of girls. I been a lot of places, I seen a lot of faces, nobody does this like you",

        #Common
        "Always felt isolated, I don't know why I was so defensive, I'll find a way to let you in",
        "I will die if I don't try, damned if I ask why",
        "This is somethin' real, this is somethin' right",
        "Never been in love, never felt it all until now",
        "As I lay here in your bed, I need you on my chest to warm me all the time, to take away your breath",
        "It's written on your lips, there ain't nothin' common 'bout us",
        "In this ordinary world where nothin' is enough, everything is gray, mistakin' love for lust, when I hold you in my arms, there ain't nothin' common 'bout us",
        "There ain't nothin' common 'bout us",
        "I see all your flaws and imperfections but that's what makes me love you more", 
        "We got such a spiritual connection",
        "Don't you know you're fuckin' beautiful",
        "I wanna feel your love, just give me all your trust",
        "Common ain't us 'cause common ain't enough"

        #Imprint
        "We can leave an imprint",
        "This minute that I'm in, this minute's where I live with you, where I stay with you if you wanna stay up late",
        "Girl we'd still make it if the planets all faded away",
        "You might think I'm crazy but I know you're my baby anyway",
        "Girl you took two minutes out of my life",
        "Girl you took two minutes out of my life\nYeah who told ya I ain't with it? I need ya\nI don't want 'em back, I just want you back in my bed",
        "I just want you back in my bed",
        "You can take it all off 'cause this love ain't got no cost",
        "I guess we all got a story",
        "Change the scenario, jumpin' like Mario\nGotta give it all a go, don't lose a life",

        #Stand Still
        "Skies of blue and birds of yellow, flowers growing just to bloom\nA million chances of our glances, catching eyes across the room",
        "If time stands still, move I will to you",
        "This world's filled, somehow I see you",
        "Rain could pour upon your face now and yet your beauty would still shine",
        "I would live a thousand lifetimes if it's you I'm sent to find",
        "If time stands still, move I will to you\nThis world's filled, somehow I see you"
        "Move all the water, babe\nLift the rocks up, tide getting stuck\nNothing can stop us",

        #Tonight
        "Just let me talk, you know what I'm sayin'",
        "Where you goin'? You feel that space, it's mine\nSaid we're goin', in every space and time",
        "Love me tonight, speak all your mind\nTake all your time, I know that you're mine",
        "Love me like we don't have tomorrow",
        "Love me like we don't have tomorrow, like there's no time at all, love",
        "Love me like tomorrow's never gonna come",
        "Love me like we don't have tomorrow",
        "I know that you're mine",
        "Tell me why it's always different in the mornin', last night you were by my side",
        "Space and time, I wanna fall into your eyes",
        "There's no point in stallin', there's nothin' to hide",
        "Right now it's priceless, some things you can't buy",
        "You're that protection that keeps me alive",
        "No matter where you are or where you'll be, when you're feelin' yourself I know you're thinkin' of me",

        #Flight Of Stars
        "I go where you go, go through Armageddon, girl I got you",
        "There's no goodbyes, only us",
        "I will follow, hold you close standing on the edge of no tomorrow",
        "I been feeling high when I touch your body",
        "Can't believe my eyes I swear you glow, I follow you close",
        "Fingertips touch, all I want your body",
        "All I want, all I ever wanted, it's in front of me, right in front of me",
        "This could be the end of me",
        "I been feeling like I deserve somebody",
        "You burn so bright you can blind somebody",
        "You go following flights to the stars and these cars can get us home",
        "As long as you feeling the same, I'll follow you into the flames",
        "I'll follow you into the flames",

        #If I Got You
        "Think I'm from space, my soul fell down\nI found the Earth not leaving now\nI know your face, think you fell too and ain't no place now, if I got you",
        "Anywhere, anywhere you go round the universe, I'll be there, I'll be there wherever you go, babe",
        "I don't care wherever you been, 'cause now you're with me",
        "Floating through the night, feels like we're dancing\nIs this the feeling. the feeling of falling in love?",
        "Is this the feeling. the feeling of falling in love?",
        "Is this the feeling. the feeling of falling in love? 'Cause I know that we met before, babe",

        #Talk To Me
        "You look through, the hair on your face, the way that you say the things that you do. I've been through all of the games, all of the ways that you been fooled",
        "I've been through all of the games, all of the ways that you been fooled",
        "I know I seen your face in different times and places",
        "Come get a little closer I wanna get to know ya",
        "We ain't keeping no secrets, there'll be no sheets between us tonight",
        "Talk to me, let's go deeper, you already know I need ya",
        "I wanna see you, leave on the lights",
        "Talk to me, talk to me, Talk to me, talk to me, Talk to me, talk to me, Talk to me",
        "Say your peace, the words that come out, out of your mouth, I wanna hear",
        "We can be something divine, planets align where we should be",
        "Baby, in my head we can love forever \nHere in my bed where we lay together"
        "Baby, in my head we can love forever",

        #There You Are
        "Only you know me, the way you know me",
        "Only you forgive me, when I'm sorry",
        "Need you when I'm broken, when I'm fixed",
        "Need you when I'm well and when I'm sick",
        "Friends that I rely on don't come through, they run like the river but not you"
        "Can't see when I'm falling, losing myself but then I hear you calling\nThere you are, there you are, you're there with open arms",
        "Only you know me, the way you know me\nOnly you forgive me, when I'm sorry",
        "Need you when I'm broken, when I'm fixed\nNeed you when I'm well and when I'm sick",
        "I got myself in a mess and without you, I'm in more",
        "You are my sober when I'm on the floor",
        "There you are, you're there with open arms, there you are and I run",
        "Need you when I'm hot and when I'm cold",
        "Need you when I'm young, when I'm old",
        "You won't be far",
        "When you're caught in the crowds, when you're up in the clouds, there you are",
        "Need you when I'm hot and when I'm cold\nNeed you when I'm young, when I'm old\nYou won't be far",

        #I Dont Mind
        "I don't mind falling, if it means I get to fly again",
        "I don't mind wishing , we're just dancing in the dark again",
        "Don't wanna spend time on the issue, we'll never grow old when I'm with you",
        "When I'm with you, the sun never comes up",
        "When I'm with, when I'm with, when I'm with, when I'm with you\nIt's lit, you can't put it out",
        "I can find you when you're lost",
        "Girl you'll never see me running out",
        "Fuck anybody else, there's only you",
        "You know I got your back, I'm on your side",
        "You can tell me your lies, I don't mind",
        "You can tell me all night when I'm with you, when you know I don't mind",
        "I don't mind waiting if you need some time to love again",
        "I don't want nothing just a little something for the pain",
        "I don't mind wishing, we're just dancing in the dark again",
        "Don't wanna spend time on the issue",
        "We'll never grow old when I'm with you",
        "I really don't mind if it's love, been waiting for a sign in the night",
        "I really don't mind if it's love",

        #Icarus Interlude
        "Call me Icarus",
        "Call me Icarus, I guess I flew too close to the sun",
        "Myth'll call me legend, and I'ma be one",
        "Get the bees coming in for the honey I supply",
        "Get the bees coming in for the honey I supply\nAnd if you ain't got it now, then you're in for a surprise",
        "I'm in the right place at the right time",
        "Girl, you love me better than anyone\nGirl, you love me better than I've known\nGirl, you love me better than I've known before",
        "Ain't no stopping what I feel\nPlays on my mind in slo-mo\nEvery time as if it were real\nEvery night, oh, it's you I feel\nThat's how you're in my mind",
        "I've been lying to the liars",

        #Good Guy
        "Don't you fall for me, girl\nI'm not the right kind, I'm a bad man\nI will do all I can to keep you by my side\nJust 'cause I know it feels right",
        "Explain every story, not boring\nGirl, I'll be the only thing up when you're dropping\nFrom purpose",
        "Present and future\nHi, Mr. President, a pleasure to meet you\nHope you feel my presence 'cause it's making a feature\nWorking on instinct like an extinct creature",
        "Street lamps lit like they're trying to teach us",
        "I've seen this scene before, real life",
        "The nature wrote the score, my lines",
        "I'm not a good guy",
        "I'm not a good guy\nBut I know you're mine",
        "I've seen this scene before, real life\nThe nature wrote the score, my lines",

        #You Wish You Knew
        "Girl I got a problem unless we trust",
        "You could be the best friend or you could be the one",
        "Girl I got a problem unless we trust\nYou could be the best friend or you could be the one",
        "Don't wanna put my love in you\nDon't wanna make a headline and lose\nDon't wanna be the one that you choose\n'Cause I'm the one, the one, the one that\nYou wish you knew",
        "Don't wanna make a headline and lose",
        "I'm the one, the one, the one that, You wish you knew",
        "Don't wanna be the one that you choose\n'Cause I'm the one, the one, the one that\nYou wish you knew",
        "Do you hear yourself when you speak?\nDo you see yourself desperately\nTalking shit trying to act like you mad?\nI don't know you like that",
        "I don't know you like that",


        #Sour Diesel
        "Walks in the place, hands on her waist gun on her thigh, big shooter game. She did this before, murdered to gain, promised her ma she won't kill again",
        "She got it and she know she got it, I'm takin' off like a rocket. Spaceship so high, I can't stop it",
        "Like sour diesel, I can't stop the feelin'",
        "Lips on her face, back in the place, Legs in the air, all dirty again",
        "She got it and she know she got it",
        "I'm so glad I found you",
        "I'm takin' off like a rocket, spaceship so high, I can't stop it",

        #Satisfaction
        "Nobody said this would be easy, nobody said this would be hard",
        "Nobody gave me a rulebook to follow",
        "You see, we gotta find our place and we'll go there now\nI can't get no satisfaction alone"
        "'Cause I can't, you can't, we can't get no Satisfaction"
        "All in my zone, all in my space; Life is always in the way",
        "Nobody said that you would leave me\nNobody says that in this dark",
        "As you try your best to pull away something surges, urges you to stay",
        "We gotta find our place and we'll go there now\nI can't get no satisfaction alone\nI can't get no satisfaction all alone",
                                        
        #Scripted
        "Blurry TV screens, fuzzy broken scenes\nFinding words don't have flow\nBlurry TV screens, fuzzy broken scenes\nHold her close finding love",
        "Hearts don't feel the same and the names we like to say\nChange with time and age, so I\nI don't wanna say what's scripted",
        "Hearts don't feel the same and the names we like to say change with time and age",
        "I, I don't wanna say what's scripted",
        "Whether you are or aren't with it, I know what I need\n'Cause I, I don't wanna say what's scripted",
        "You still remember my eyes even if the Men In Black flashed their light into your eyes",
        "For the second time this night, it feels right, then it's only you and I",
        "Oh, you and I\nOh, you and I",
        "I don't wanna say what's scripted\nWhether you are or aren't with it, I know what I need",
                                                                        
        #Entertainer
        "You thought you had me, didn't you?\nWhen you lied to my face, I could see the truth\nEvery step of the way I knew how you fooled me, boo",
        "You thought you had me, didn't you?",
        "When you lied to my face, I could see the truth",
        "Guess you didn't know that, you were my favorite entertainer",
        "I'd watch you, I'd laugh, I would fuck with you\nDon't you take me for a fool, in this game, I own the rules",
        "You were my favorite entertainer",
        "I'd watch you, I'd laugh, I would fake it too\nDon't you take me for a fool, I'ma show you a thing or two",
        "Never see me coming, I'll turn you down\nWhen you need me the most, I will turn you down",
        "Thought that you were smarter, I'm ashamed for you\nI knew it right away when you stopped lovin' me\nIt happened when your touch wasn't enough for me",
        "I knew it right away when you stopped lovin' me. It happened when your touch wasn't enough for me",
        "Know it's harder to take, and let's face it\nNo one's playing your games, but let's face it",
        "I know fake love when I see it anyway",
        "I'ma turn you down when you need me anyway, anyway, anyway",
        "I know you need me the most",

        #All That
        "When I woke up this morning the sun had just dawned in\nMy bed, or your bed was the first or the last time\nI don't care, it feels right, I'm not, not stopping all night",
        "Things fall apart and in a part you feel distant\nReactions are instant if emotions are constant\nLet's say for instance that you had a conscience\nWould you take the time then to weigh out the options",
        "Reactions are instant if emotions are constant",
        "All that, all that, You can give me all that",
        "All that, all that, You can give me all that\nStay here in the morning, You can take it all back",
        "Lay here, if you want to , You can give me\nAll that, all that, all that",
        "You can give me all that, all that, all that\nStay here in the morning, you can take it all back, all back, all back\nLay here, if you want to, you can give me all that, all that, all that",
        "Never cross my mind, have I crossed the lines\nOr is there more to find, more to find?",
        "I think inside immortalized, mortalized, more to life",                                                                   
        "Coming from both sides an attack of the mind\nLike Optimus Prime in his prime\nKick it, don't skip it, to the finish line, This minute's mine",

        #Good Years
        "I'd rather be anywhere, anywhere but here",
        "I'd rather be anywhere, anywhere but here\nI close my eyes and see a crowd of a thousand tears\nI pray to God I didn't waste all my good years",
        "The voices screaming loud as hell, we don't care 'bout no one else\nNothing in the world could bring us down\nNow we're so high among the stars without a worry\nAnd neither one, one of us wants to say we're sorry",
        "I pray to God I didn't waste all my good years",
        "Too much drugs and alcohol, what the hell were we fighting for?\n'Cause now the whole damn world will know\nThat we're too numb and just too dumb to change the story\nNeither one, one of us wants to say we're sorry",
        "What the hell were we fighting for?",
        "Neither one, one of us wants to say we're sorry",
        "Need a chance just to breathe, feel alive\nAnd when the day meets the night, show me the light\nFeel the wind and the fire, hold the pain deep inside\nIt's in my eyes, in my eyes",
        "Need a chance just to breathe, feel alive and when the day meets the night, show me the light",
        "Feel the wind and the fire, hold the pain deep inside, it's in my eyes, in my eyes",
        "Nothing in the world could bring us down",

        #Fresh Air
        "You could be a changed man if you wanted\nYou could make the doves cry if you wanted\nTell me that you want that, but you don't\nTell me that you want that, but you don't",
        "I say I'm sorry, but you're never sober\nI start drinking, it's too much thinking, oh\nIt's the same every time that you're with me",
        "I think I need some fresh air (Fresh air, fresh air)\nFeeling under pressure (Pressure, pressure)\nDon't wanna talk about it ('Bout it, 'bout it)\nDon't even get me started over you\nYou know I ain't tryna go pressure you",
        "You and me got differences, differences\nYou and me got differences\nWhy you on some different shit?",
        "You and me got differences",
        "We're caught in a cycle, so pardon my psycho\nWe could've been right, though, guess that's how life go\nThere's nothing that I can do for you",
        "We could've been right, though, guess that's how life go",

        #Rainberry
        "Rainberry, please\nYou think I'm on my knees, but don't you worry\nI know what you don't know",
        "Don't even start, the truth won't break my heart\nNo, don't you worry. I already know",
        "Too many bones inside your closet\nYou thought you buried deep\nBut they never let me get a minute of peace\nHow do you sleep?",
        "Rainberry, falling down your blood-red lips\nWhy are your eyes heavy?\nIs there somebody else you missed?",
        "Tell me what's going on before I go too far",
        "Rainberry, is there somebody else, somebody else now?",
        "Dry your eyes 'cause it won't work this timeI already dried mine, and I won't drown in yours",
        "Go wash your hands, but you can't change your past\nThose stories ain't shit now. You don't mean it, I'm sure",
        "Rainberry, please",

        #Insomnia
        "Am I a fool, waiting for you?\nWhat if you never come back?",
        "What if we never know why hearts deceive us?",
        "The night calls to dreamers",
        "My sleep was stolen, I'm searching for thieves\nThese memories in my head so vivid to see",
        "My sleep was stolen, I'm searching for thieves",
        "When I close my eyes I feel it all again, I can't find no peace",

        #No Candle No Light
        "We gotta, we gotta, we gotta face it\nThe fire, the fire ain't no longer blazin'",
        "I woke up on the wrong side of ya\nYou don't even know that I left, do ya?",
        "Can't handle my love, Can't handle your lies\nNo friend zone to my love, Quit burning all of my time",
        "No candle, no light for you\nNo candle, no light for you\nNo candle, no light for you",
        "I can't do it, no baby, I can't do it\nI only end up losing, ooh we're really fooling this",
        "Agree to disagree, some things aren't meant to be\n But I wanted you and me",
        "Some things aren't meant to be",

        #Fingers
        "Fucked and I want ya",
        "I been fucked and I want ya, I can't even text ya\n'Cause my fingers ain't working, but my heart is",
        "If you wanna, let me know where you are, then I can come and love",
        "I been fucked and I want ya, I can't even text ya\n'Cause my fingers ain't working, but my heart is\nIf you wanna, let me know where you are, then\nI can come and love",
        "What did I tell ya? Typo said I loved ya\nDidn't mean what I was sayin'\nNo, I wasn't playin', just confused",

        #Too Much
        "I think we met and the time flies",
        "I guess I want too much (Too much)\nI just want love and lust (Uh)\nYou just can't love enough (Yeah)\nThat's why I need a touch",
        "When the room becomes a game we play\nWhite lines, they seem to turn to snakes\nI guess I'll turn you 'way, say white lies to your face\nYou know I know my place, nothin' I can say",
        "Felt good but now I feel bad\nI think I know I can't take it back\nNo, there's nothin' I can say",
        "Felt good but now I feel bad, I think I know I can't take it back",
        "I never meant to, but I did though,I gotta keep it on the d-low\nThen again, what the fuck do I know? You're always on my mind so",

        #Still Got Time
        "Just stop lookin' for love\nGirl, you're young, you still got time"
        "This could be something if you let it be something, don't scare me away\nTurning somethings into nothing, babe\nYou're already used to the games, babe\nYou play your role and I play the same",
        "That smile gon' take you places",
        "This could be something if you let it be something, don't scare me away",

        #Calamity
        "Nostalgia what a funny feelin'",
        "I feel depleted from feelings I've been revealin'",
        "It's do or die I'm not goin' willing",
        "But when it's time wrap in white linen",
        "I rap this I say it for my sanity",
        "Whatever the calamity I did this for myself",
        "Fuck all of your fantasies",
        "You're a snake fell off the ladder",
        "I prefer speakin' in analogies",
        "I've had enough of all this wet",
        "I can't trust that you're my family",
        "I don't know what's next",
        "My brain lives with the cannabis\nCan I resist the dark abyss?",
        "My mind's in a prism shape and in times like a prison state",
        "There's no right that I feel of late",
        "There's no light if my view's at stake",
        "And which life should I choose to take",
        "What's left is it room or space",
        "There are rumours we have to face",
        "I prefer sooner than after late",
        "I seen actors after BAFTA's be more straight",
        "I mean down the barrel, I hear 'em sing it's the same carol",
        "They're tryna sprint in a long run Mo Farah",
        "They're tryna fix when it's long gone don't bother",
        "There's no other the thought shudders through most lovers",
        "I wanna bed you but still sleep is death's cousin",
        "Years that pass by can't press no rewind, just watch my life by and lock the right ties",
        "Nobody nobody is listenin' to me",
        "Nobody, nobody is listenin'",

        #Better
        "Hope I only leave good vibes on your living room floor",
        "It hurts so bad that I didn't when you asked for more",
        "Your dad probably loves me more than he ever did now 'cause I finally got out, yeah, we finally knocked down",
        "Sometimes it's better that way, gotta let it go so your heart don't break, 'cause I love you",
        "Just this one time, hear what I'm tryna say, know you might not feel quite the same way but I love you",
        "I tell you, I love you",
        "Why? Why wait to fight? Give it a try",
        "I say goodbye while it's right",
        "Can we save tears in your eyes?",
        "Why wait to hate? Can we save love?",
        "I fell in, I'm falling, I'm for you",
        "I fell in, I'm falling, I'm for you\nI can't let you fall through the floor too",
        "It's a gamble to take any more of you",
        "Still in my mind sometimes, I must admit it\nLike it's a crime, on trial, I got acquitted",
        "Me and you wasn't meant, we wasn't fitted like it's a glove, I hated to admit it",
        "Me and you wasn't meant, we wasn't fitted",
        "'Cause obviously, we go back so why would we ruin that?",
        "In too deep, we're rearranged, now you wanna ask for names",
        "We can't let this fruit go bad, sayin' things we can't take back",
        "Say you feel the same",
        "Why wait to hate, can we save love?",

        #Outside
        "Two wrongs make no right",
        "When it's left, at least we tried",
        "I'll be back tonight",
        "I'll let you decide to leave my life outside",
        "Leave my life outside or let me in",
        "I know I'm always in my head but some things, they must be said",
        "Hurts me when I think about it someone else bein' in your bed",
        "I know I'm not so innocent but the love I had for you was real",
        "Hope it hurts you when you think about it, the both of us just have to dip",
        "T-shirt that you're wearing, that's my favorite",
        "First time that I touched you, you could save it",
        "Two wrongs make no right when it's left, at least we tried (Oh)",
        "It wasn't all bad, now, was it? All the things that we've been through",
        "The way you snuck out of your parents, just you and me up on the roof",
        "We didn't have much, but, yeah, we did it, starin' at the perfect view",
        "The way you snuck out of your parents, just you and me up on the roof\nWe didn't have much, but, yeah, we did it, starin' at the perfect view",
        "Do I keep the dog or do you want him? When I look at him, I think of you",
        "The T-shirt that you're wearing, that's my favorite",
        "Damn, I really thought that we would make it, yeah",
        "Leave all of my shit outside, leave my life outside or let me in",

        #Vibez
        "Don't keep me waitin', I been waitin' all night to get closer",
        "Don't keep me waitin', I been waitin' all night to get closer and you already know I got it for ya, you know the vibes, know the vibes",
        "If we're movin' too fast, we can slow up\nBaby, this far from mediocre, you know the vibes, know the vibes",
        "It's you and me here in this room, imaginin' things we could do",
        "Won't tell no lies, no lies to you, I need you here, I need you here",
        "Mind runnin' wild, we touchin' slow, just say the word, I'm ready to go, oh",
        "Anticipation plays after four, I need you now",
        "Baby, I'ma get you right, I will", 
        "When I touch you, tell me how it feel, tTrust me, I'ma make it feel surreal",
        "Baby, mind of mine",
        "I'ma do all the things, type of things that happen in your dreams",
        "Get you right where you need to be",
        "You know the vibes, know the vibes",
        "You got the vibes, got the vibes",
        
        #When Love's Around
        "Never feels right, never feel that type of way",
        "I need you in my life, yeah, you could be my wife for real",
        "Only takes a woman to show you what it means to love, to love",
        "I'm missin' you tonight, I'm wishin' you were right here",
        "Keep me up until the mornin', you could see it in my aura",
        "You've been givin' it your all and I'm fallin' for you",
        "'Cause when love's around",

        #Connexion
        "Funny when you come to mind, that's when you hit me up, that's when we feel a little closer",
        "Funny when you come to mind, that's when you hit me up\nThat's when we feel a little closer, just when I started thinkin'\nIt's like a force we can't explain, work like a magnet, babe",
        "Could be my suspicion, maybe I'm just out here overthinkin'",
        "Like you come into the picture",
        "When I start to feel like something's missin' (Missin'), oh, oh-ooh",
        "Could be my suspicion, maybe I'm just out here overthinkin'\nLike you come into the picture when I start to feel like something's missin'",
        "I don't wanna miss out on another love, so I'm gonna dive right in, go head first into the unknown like it's all I know",
        "Call it a digital but physical connection ",
        "Love you every single night that's when I feel your love, that's when I take your clothes off",
        "Can we stay in the bedroom? 'Cause you're always on my brain, I can't get away",

        #Sweat
        "Stayin' up for you, day and night for you",
        "We've been losing track of time, reaching higher heights, only one thing on my mind",
        "Let me touch you where you like it, let me do it for ya",
        "Give you all of my attention, dive into that ocean of your love",
        "Let me show you just how much I want ya",
        "Oh, drippin' down your body like gold, slowly steamin' up the windows\nMy skin on your skin, again and again, sweat for me, sweat for me",
        "Love it when I tear off your clothes, slowly steamin' up the windows\nMy skin on your skin, again and again, sweat for me, sweat for me",
        "Damn, I could get lost in a heartbeat, damn, I can't get over your body\nCan't take my eyes off you, baby, let me love you, baby",
        "I could get lost in a heartbeat, I can get lost in your body",
        "Can't take my eyes off you, baby",
        "Let me love you, baby",
        "Sweat for me, sweat for me",
        "I could get lost in a heartbeat",

        #Unfuckwitable
        "I'm unfuckwithable in a world of my own, that's why my shoulder's so cold",
        "I'm unfuckwithable",
        "So tired of fake friends and fake love, you know",
        "No time for no lie and I'm here to show, I found a way higher",
        "Me is all I need to be inspired",
        "My vibe and my life are all my design, your sentiment's irrelevant",
        "I get down and up again 'cause I had the time of my life",
        "I'm just unfuckwithable in a world of my own",
        "Can't nobody take me home",
        "I'm worth my weight in gold",
        "Forget whatever you've been told, I am unfuckwithable, unfuckwithable",
        "They all said I wouldn't do shit, now they all about my new shit",
        "Thinkin' we were always cool when I was never even all on your mind",
        "Happens all the time",
        "You probably thought I couldn't turn water to wine\nWater to wine, happens all the time",

        #Windowsill
        "Fuckin' on the countertop, window to the floor, she been on my mind, I swear she the type to roll",
        "She with me when I flow, she with me when I don't",
        "Fuckin' on the countertops, elevated her",
        "She could rob me blind, I'd give anything she want\nI never let her know so she come back for more",
        "Are you done yet? 'Cause I'm right here\nAre you waitin' for the right time to call me back?",
        "Cigarettes and fuckin' on the windowsill, in my bed, yeah, tell me when you're gettin' here",
        "Only thing I wanna know is how far away you are",
        "Cigarettes and fuckin' on the windowsill, break the glass, go and show me how you really feel",
        "I see the way she lookin' like she lookin' in my soul, I ain't stoppin', maybe this could be the somethin' that I want",
        "Fuckin' on the countertops, elevated her, she could rob me blind, I'd give anything she want",
        "Are you done yet? 'Cause I'm right here",
        "Are you waitin' for the right time to call me back?",
        "Cigarettes and fuckin' on the windowsill",


        #Tightrope
        "Why's it gotta feel like I'm walkin' a tightrope?",
        "Why you wanna see how far I fall?",
        "I'm already up here and I got my eyes closed and I ain't never fell from a love this tall",
        "Why's it gotta feel like I'm walkin' a tightrope? Why you wanna see how far I fall?",
        "Are you ready? 'Cause I'm ready to let go",
        "Never thought that I'd be ready again",
        "Guess there's somethin' 'bout the neon red glow, got me thinkin' 'bout givin' all in",
        "Somethin' told me it was you",
        "Somethin' told me it was you\nSomethin' told me it was you\nSomethin' told me it was you",
        "I'm sittin' with my legs across your torso, we are who we are when we're alone",
        "Baby, I'm ready, any minute, we might fall\nLately, I feel like my grip is gone but you got my arm",
        "Lately, I feel like my grip is gone but you got my arm",
        "Guess there's somethin' 'bout the neon red glow",
        "Why's it gotta feel like I'm walkin' a tightrope? Why you wanna see how far I fall?'Cause I'm already up here and I got my eyes closed and I ain't never fell from a love this tall",
        "चौदवीं का चाँद हो, या आफ़ताब हो?\nजो भी हो तुम खुदा कि क़सम, लाजवाब हो",
        "Are you the full moon or the sun?\nWhatever you are, I swear to God, you are beyond compare",

        #River Road
        "We don't define each other",
        "Stand on your own, be a pillar",
        "Call you my lover, drinks to my liver, I cried now a river full of tears",
        "Don't you ever hope for something else?",
        "Breeze outside my window turned to color, know that I will see the sun again",
        "Leaves have turned into a tint of orange",
        "Answers that will lie inside myself",
        "What will I leave behind me? Where will I choose to go?",
        "To tell the truth, I'm tired of falling, when I'm floating, I'm closer to you",
        "We can't control all the outcomes, let go of the reins, ride the rhythm",
        "Doubled my vision",
        "Searchin' for meaning, still don't believe it, stopped at the ceiling, all these years",
        "Lightly floating ecstasy",
        "Don't you ever hope for something else?",
        "Breeze outside my window turned to color, know that I will see the sun again\nLeaves have turned into a tint of orange, answers that will lie inside myself",
        "We don't define each other, stand on your own, be a pillar, lay on my pillow",
        "We don't define each other, stand on your own, be a pillar, lay on my pillow\nCall you my lover, drinks to my liver, I cried now a river full of tears",
        
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

        #Dusk Till Dawn
        "Not tryna be indie, not tryna be cool",
        "Not tryna be indie, not tryna be cool. Just tryna be in this, tell me, are you too?",
        "Can you feel where the wind is? Can you feel it through all of the windows inside this room?",
        "I wanna touch you, baby and I wanna feel you too, I wanna see the sun rise on your sins, just me and you",
        "Light it up, on the run, let's make love tonight. Make it up, fall in love, try",
        "Baby, I'm right here",
        "Let's make love tonight",
        "You'll never be alone, I'll be with you from dusk till dawn",
        "I'll be with you from dusk till dawn, baby, I'm right here",
        "I'll hold you when things go wrong,I'll be with you from dusk till dawn, I'll be with you from dusk till dawn",
        "We were shut like a jacket so do your zip",
        "We would roll down the rapids to find a wave that fits",
        "Girl, give love to your body, It's only you that can stop it",
        "Girl, give love to your body",

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

# Function to tweet a random lyric, ensuring no duplicates
def tweet_lyric(client, posted_lyrics):
    remaining_lyrics = [lyric for lyric in lyrics if lyric not in posted_lyrics]
    if not remaining_lyrics:
        print("All lyrics have been posted. Exiting.")
        return False  # Stop the script if all lyrics have been posted

    lyric_to_post = random.choice(remaining_lyrics)
    print(f"Attempting to post lyric: {lyric_to_post}")

    # Post the lyric
    try:
        response = client.create_tweet(text=lyric_to_post)
        if response and response.data and response.data.get('id'):
            print(f"Successfully posted: {lyric_to_post}")
            save_posted_lyrics(lyric_to_post)
            posted_lyrics.add(lyric_to_post)  # Add the lyric to the posted_lyrics set
            return True
        else:
            print(f"Failed to post the lyric: {lyric_to_post}. Response: {response}")
            return False
    except Exception as e:
        print(f"Error posting lyric: {e}")
        return False

# Main function
def main():
    client = authenticate()
    posted_lyrics = load_posted_lyrics()

    while tweet_lyric(client, posted_lyrics):
        next_tweet_time = datetime.now() + timedelta(hours=6)
        print(f"\nNext tweet scheduled at {next_tweet_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Wait 6 hours before posting the next lyric
        countdown_timer(6 * 3600)

if __name__ == "__main__":
    main()
