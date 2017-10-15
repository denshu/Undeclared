# You can place the script of your game in this file.

# Declare images below this line, using the image statement.

image black = "#000000"
image logo = im.Scale("img/logo.png", 800, 600)

image bg dorm_hall = im.Scale("img/bg/dorm_hall.png", 800, 600)
image bg dorm_room_common = im.Scale("img/bg/dorm_room_common.png", 800, 600)
image bg dorm_room_empty = im.Scale("img/bg/dorm_room_empty.png", 800, 600)
image bg dorm_room_furnished = im.Scale("img/bg/dorm_room_furnished.png", 800, 600)

image bg campus_day = im.Scale("img/bg/campus_day.png", 800, 600)
image bg campus_night = im.Scale("img/bg/campus_night.png", 800, 600)
image bg club_fair = im.Scale("img/bg/club_fair.png", 800, 600)

image cg becca_intro = im.Scale("img/cg/cg_flat_becca.png", 800, 600)
image cg charlie_intro = im.Scale("img/cg/cg_flat_charlie.png", 800, 600)
image cg erika_intro = im.Scale("img/cg/cg_flat_erika.png", 800, 600)
image cg julianne_intro = im.Scale("img/cg/cg_flat_julianne.png", 800, 600)
image cg nikki_intro = im.Scale("img/cg/cg_flat_nikki.png", 800, 600)

# eg. image eileen happy = "eileen_happy.png"
image charlie default = "img/sprite/charlie_default.png"
image charlie happy = "img/sprite/charlie_happy.png"
image charlie surprised = "img/sprite/charlie_surprised.png"
image charlie thinking = "img/sprite/charlie_thinking.png"

image erika default = "img/sprite/erika_default.png"
image erika bored = "img/sprite/erika_bored.png"
image erika happy = "img/sprite/erika_happy.png"

image becca default = "img/sprite/becca_default.png"
image becca happy = "img/sprite/becca_happy.png"
image becca sheepish = "img/sprite/becca_sheepish.png"
image becca surprised = "img/sprite/becca_surprised.png"

image nikki default = "img/sprite/nikki_default.png"
image nikki happy = "img/sprite/nikki_happy.png"
image nikki surprised = "img/sprite/nikki_surprised.png"
image nikki talk = "img/sprite/nikki_talk.png"

image julianne default = "img/sprite/julianne_default.png"
image julianne happy = "img/sprite/julianne_happy.png"
image julianne surprised = "img/sprite/julianne_surprised.png"
image julianne wink = "img/sprite/julianne_wink.png"


# Declare characters used by this game.
define mc = Character('Me', color="#000000")
define me = Character('Me', color="#000000")
define charlie = Character('Charlie', color="#000000")
define erika = Character('Erika', color="#000000")
define becca = Character('Becca', color="#000000")
define nikki = Character('Nikki', color="#000000")
define julianne = Character('Julianne', color="#000000")
define unknown = Character('???', color="#000000")

# The game starts here.
label start:

    stop music fadeout 3.0

    scene black with Pixellate(3.0, 20)

    $ renpy.pause(2.0)

    $ mcname = ""

    "{i}Bzzt... bzzzzzzzt.....{/i}"

    "I felt my phone buzz in my pocket as I walked down the hall."
    
    "I didn't pull my eyes away from my dorm map, except to occasionally check the room numbers as I passed by. I wasn't really in the mood to check my messages."
    
    "I'm sure it was something like \"wish you were here :P\" anyway. The only thing that could make this day worse would be a reminder of everything that I had left behind."
    
    "I took a sharp left and reached the end of the hall."

    me "...Ah, here we go."

    scene bg dorm_hall
    with fade

    play music "bgm/Monday_Morning.mp3"
    
    "The last room on the right. I stood in front of the door to my dorm, my new \"home away from home\", dreading my first step."
    
    "Apparently my roommate was also a late addition too, so I had nothing to work off of. What was she like? Would we be able to live together for a whole year? Is she even gonna be in there?"
    
    "Thoughts and fears filled my head as I stood out in the middle of the hallway."
    
    "..."
    
    "Well, I couldn't keep putting it off. I had to drop my stuff off and get ready for my morning class."
    
    # [Later the MC puts her headphones back on but there's no mention of her taking them off in the first place, so I added it here.]

    "I inserted my room key and turned the handle, taking my headphones off with my other hand just in case I met this roommate of mine."

    scene bg dorm_room_common
    with fade

    "Light poured in through two windows on the far wall, illuminating the common room."

    me "Well, this doesn't seem too bad."

    "The common room was a lot spacier than I would have expected from the outside. The school had supplied us with a couch, two armchairs, a small coffee table, and even a chest with a TV on top."
    
    "While our room didn't come with a kitchenette, we did get a communal fridge and freezer, which was pretty nice."
    
    "It didn't seem like my roommate was here, but it was clear from the state of the area before me that she had already dropped off her stuff."
    
    "There were a couple posters on the wall and blankets strewn across the couch. I also spotted some exercise equipment at one corner of the room and a couple duffel bags at another corner."

    "That's about it for this room. With my roommate absent, I wasn't expecting to talk to anyone anytime soon, so I threw my headphones back on and walked over to my bedroom to unload my stuff before trying to make sense of my campus map."

    scene bg dorm_room_empty
    with fade

    "Bed, desk, closet, drawers... basically, what you'd expect from a furnished dorm bedroom."

    "I had a little bit of time to spare before class, so I threw my bags onto the bed and started pulling out some of the extra stuff I'd brought from home to help spruce up this plain room."

    scene bg dorm_room_furnished
    with dissolve

    "Even just a couple posters and a few stuffed animals really lightened up the atmosphere of the room. With so many unknowns ahead of me, I felt a bit more comfortable knowing there's at least one place here that feels like home already."
    
    "I took a step back to look over the room once more."

    me "Well, this is it... the next year of my life."

    scene bg dorm_room_common
    with dissolve

    "I sighed before readjusting my school bag and heading out to try and see if I could find my first class."

    scene bg dorm_hall
    with dissolve
    
    "Maybe if I was lucky, I could run into a professor or someone that could point me in the direction of m--"

    # {screen shakes}

    scene black with vpunch

    stop music fadeout 1.0

    me "Uwaah!" with vpunch

    "As soon as I walked out the door, I collided into something and fell backwards."

    unknown "Oof... haha, wow, talk about running into someone."

    # {CG, Charlie sitting up on the floor}

    show cg charlie_intro with Dissolve(1.0)

    $ renpy.pause(1.0)

    play music "bgm/Vivacity.mp3"

    "When I finally saw what... or I guess {b}{i}who{/i}{/b} I had run into, I was greeted by the sight of a short-haired girl in a similar position to mine. She rubbed her head and looked up at me, smiling."

    unknown "Oh, you must be my roommate, then? Let's try this \"greeting\" thing again."

    # {CG change}

    "My apparent roommate held out her hand towards me. I tried to smile back but couldn’t get over my embarrassment of running into her."

    charlie "My name's Charlotte, but you can call me Charlie. I'm a sophomore here. And you are?"

    # {name entry}

    $ mcname = renpy.input('Enter your name!', default='Name Namerson',  allow=None, exclude=None, length=20, with_none=None, pixel_width=None) or "Me"
    $ mcname = mcname.strip()

    define mc = Character(_("[mcname]"), color="#000000")

    mc "I'm... [mcname]. Um, a freshman."

    charlie "It's a pleasure to meet you, [mcname]! Did you just get done dropping off your stuff? Where are you headed?"

    mc "Um, well, I have to figure out where my first class is since it starts soon. I tried looking at the campus map but I don't even know where I am right now..."

    charlie "Hmm. Well, what building's your first class in? I don't have anything going on until later in the morning, so I could show you to your first class and give a quick tour on the way. What do you say?"

    mc "Oh! I mean, if you don't mind, that'd help me a lot."

    charlie "No problem at all! I'd be more than happy to. I was only going to organize my room but this sounds way more fun. What's another half an hour of slacking anyways?"

    # fade cg back to hallway

    scene black
    with fade

    scene bg dorm_hall
    with fade

    show charlie default with dissolve

    "Charlie stood up and extended out her hand towards me again, this time to help me up."

    show charlie happy

    "I slowly grabbed her hand and got to my feet. I picked up my bag from the floor and couldn't help but smile a little."

    mc "Whew, thanks..."

    hide charlie with dissolve

    mc "(Maybe things won't be too bad after all...)"

    "While I was thinking that, Charlie had already started heading down the hallway."

    charlie "Hurry up or you're gonna be late!"

    mc "O-okay!"

    stop music fadeout 1.0

    scene black with fade

    # {campus, outside, day}

    scene bg campus_day with fade

    play music "bgm/Monday_Morning.mp3"
    
    "We learned that my first class was all the way on the other side of campus, so Charlie was able to give me a pretty in-depth tour of all the major areas along the way." 

    "The campus looked overwhelmingly large at first, but with Charlie pointing out the key places I would frequently visit, I started feeling that maybe I could make my way around without too much trouble."

    show charlie default with dissolve

    charlie "...So, [mcname], why'd you choose to come here?"

    mc "Oh! Well... I wasn't quite sure what I wanted to do coming out of high school, but I knew I was pretty good at math."

    mc "So, I thought going somewhere with a diverse general studies program would be nice while I figure out exactly what I want to do."

    charlie "Ah, okay, that makes sense. But there's a lot of colleges that do that, right? What made this one special? Hmm..."

    show charlie thinking

    "Charlie paused, deep in thought."

    show charlie default

    charlie "Oh, I know. Valley View University is an all-girls' college -- did that influence you in any way?"

    mc "Hmm... I guess it just felt comfortable? I went to an all-girls' high school as well, so I thought going here would make for an easier transition."

    show charlie surprised

    charlie "Oh cool! Did anyone from your school come here too?"

    "Oh. My shoulders slumped a bit as I let out a sigh."

    mc "No, everyone I talked to wanted to stay in-state. Either they were interested in another field or they just felt more comfortable living at home."

    show charlie thinking

    charlie "Ooh, that's rough. So you don't know anyone else around here, huh?"

    mc "No one."

    charlie "Aw, sorry to hear that. Getting used to a new place where you don't really know anyone can be tough..."

    show charlie happy

    charlie "But hey, you heard about the club fair next week, right? We have a ton of different clubs here and I'm sure you'll find one that suits you. You can make plenty of friends there!"

    mc "I dunno, I never really did extracurricular stuff in high school. Where would I even begin?"

    show charlie default

    charlie "Don't worry, a lot of freshmen feel the same way. I was in the same boat as you, actually! I joined the botany club here without knowing much about it."

    charlie "There's even clubs that just watch TV or hang out, too."

    mc "Oh, okay, maybe I'll check it out then. I might as well, right?"

    show charlie happy

    charlie "Yeah, for sure!"

    show charlie default

    charlie "Well, whatever you end up doing -- even if you don't choose a club at all! -- I'm sure you'll have a good time here and make the most of it."

    mc "I sure hope so..."

    show charlie happy

    charlie "Chin up, buddy. It's only the first day! You've got 4 years' worth of fun memories ahead of you."

    hide charlie with dissolve

    "..."

    charlie "Oh, we're here."

    "Charlie had stopped in front of a small building. It took me a moment to notice, so I had to backtrack a bit and walk back to where she was."

    show charlie happy with dissolve

    charlie "Hey, lucky you. Looks like you won't have to worry about running up endless staircases to get to your first class. You should be able to find your classroom just fine."

    mc "Thanks! I dunno how long it would've taken to find this place if I were on my own."

    show charlie default

    charlie "No prob, [mcname], good luck today. I'll see you after my classes. By the way, feel free to decorate our room however you'd like!"

    hide charlie with dissolve

    # [Feel free to replace this with the original text in the google doc. I wanted to expand on the anxiety MC might feel, given her characterization thus far]

    "And before I could say goodbye, she was already heading back towards the dorms."

    "I turned towards the double doors leading into the building, now appearing more imposing than they were just a moment ago, and I sighed out what felt like the entirety of the air in my lungs."
    
    "With one more sigh for good measure, I took hold of the door handle and gave it a good pull."

    "I didn't know if I was ready to take on the semester and my new life ahead of me, but one way or another it looks like I didn't have much of a choice."
    
    "I took a step inside, anxiously examining the interior." 

    $ renpy.pause(1.0)
    
    "A few more steps, less anxiously." 

    $ renpy.pause(1.0)
    
    "Look out now, I've got more steps where that came from."

    $ renpy.pause(1.0)

    "The thumping of shoe against tile echoed down the hallway, mingling with muffled conversations from the classrooms within."

    stop music fadeout 2.0

    scene black with fade
    
    "Well, at least for the next hour or so, one of those classrooms was where I belonged."

    # END PROLOGUE! GOOD JOB TEAM WE DID IT. WE OUT HERE

    # SHOW THAT TITLE, BABY!!

    scene logo with Fade(1.0, 0.0, 1.5)

    $ renpy.pause(4.0)

    scene black with Fade(1.5, 0.0, 1.0)

    # Okay it's time for Act 1

    # Week 2, Monday

    # Campus, outside, night

    "After classes had ended, I made my way over to the activities building to check out the club fair."

    scene bg campus_night with fade

    play music "bgm/Android_Star.mp3"

    "Wow, it's really packed here tonight! Not that it should surprise anyone, since it's the day of the club fair, but I've never seen this many students gathered in one area whenever I'm walking around campus."

    # inside hall

    scene bg club_fair with dissolve

    "I came here not really having any idea of what kind of club I wanted to join, so my hope is that as I'm scoping out the tables, I'll run into something I'll like."

    "I had already seen a couple clubs near the entrance that might be fun to visit occasionally, but I was looking for one that I'd be interested in attending every week."

    "It looks like there'll be pretty heavy traffic no matter where I go... I guess I'll just start somewhere."

    $ erika_visited = False
    $ becca_visited = False
    $ nikki_visited = False
    $ julianne_visited = False

    $ erika_talked = False
    $ becca_talked = False
    $ nikki_talked = False
    $ julianne_talked = False


    label clubfair_rowchoice:

        "Where to go?"

        menu:
        
            with dissolve

            "First row" if not erika_visited:

                jump clubfair_erika

            "Second row" if not becca_visited:

                jump clubfair_becca

            "Third row" if not nikki_visited:

                jump clubfair_nikki

            "Go outside" if (erika_visited and becca_visited and nikki_visited):

                jump clubfair_outside

    # this is where i stop editing and just straight-up paste from the doc.
    # i will go back at some point but i want to get the functionality done first

    label clubfair_erika:

        $ erika_visited = True

        "The first row seemed to be predominantly made up of sports clubs, and they seemed to have gone all-out in terms of spirit."

        "The cheerleading team had gotten a couple members to do some cheer routines, which was impressive given the tight space they had to work with."

        "The ping pong club had a couple of people in front of their stand doing tricks and routines with each other."

        "While I was passing through, I noticed one table seemed to be hidden in between two bigger displays."

        "..."

        "As I got closer, it actually seemed like the table might be empty? I saw a couple flyers and stuff on there, but nothing really eye-catching about it."

        unknown "Hey."

        "Whoa! I was startled by the sudden voice." with vpunch

        stop music fadeout 1.0

        # Erika CG 1

        show cg erika_intro with Dissolve(1.0)

        play music "bgm/Erika.mp3"

        $ renpy.pause(1.0)

        "The girl sitting at the table looked... less than enthused to be there. She had her head resting on one of her hands, and a stare that seemed to cut right through you."

        "I involuntarily took a step back as her brows began to knit. She lazily twirled some of her hair with her fingers and spoke up again."

        unknown "Are you looking for the tennis club?"

        mc "Oh, is that what this table's for? I couldn't tell."

        unknown "Yeah, this is the tennis club table. If you wanna join, you can take an application form and turn it in during our next meeting."

        "She nudged the papers towards me and glared, as if to signal that I should finish up soon and leave."

        menu:
            with dissolve
            "Take papers and leave":
                jump clubfair_erika_leave

            "Stay and talk to her":
                jump clubfair_erika_stay

        label clubfair_erika_leave:

            mc "Th-thanks..."

            stop music fadeout 1.0

            "I quickly grabbed a paper and continued on my way. It was clear she didn't want to talk to others."

            "So why was she here at the club fair? Who knows, but that's one hell of a first impression to give."

            scene bg club_fair with Dissolve(1.0)

            play music "bgm/Android_Star.mp3"

            jump clubfair_rowchoice

        label clubfair_erika_stay:

            $ erika_talked = True

            "I kinda wanted to know what was going on here."

            mc "Are... are you the head of the tennis club?"

            # change scene to inside hall

            scene bg club_fair with Dissolve(1.0)

            show erika default with dissolve

            "The girl let out a large sigh and half-heartedly adjusted herself at the table."

            unknown "Nope, just one of the new members stuck with taking care of the table while the seniors take care of other business."

            show erika bored

            "She huffed and crossed her arms. Looks like she wasn't exactly pleased with the situation."

            mc "\"Members\"? So are there supposed to be others here?"

            show erika default

            unknown "Yeah, there were supposed to be other people with me but none of them showed up when it came time to set up."

            show erika bored

            unknown "And they were supposed to be in charge of the decor, too. Ugh."

            show erika default

            "She paused for a moment before staring me in the eyes. Was she trying to figure something out...?"

            unknown "So, what're you doing? Did you just come for the tennis club or something?"

            mc "Ah! N-no, just scoping out the fair and I was trying to figure out what the table was for. There are a lot of options, I dunno if I could choose..."

            unknown "Do you have any experience playing tennis?"

            mc "N-No, unless you count a round of Wii Sports as \"experience\"."

            show erika happy

            "I couldn't believe I just said that out loud. She smirked."

            unknown "Hmph. Well, if you took a paper, no reason you couldn't show up for a meeting and see what it's like. I can promise that our practices are a lot more organized than our table might imply."

            "I couldn't help but chuckle."

            mc "I'll keep that in mind. Thanks for the info, good luck with the rest of the fair."

            hide erika with dissolve

            "She gave a single nod and returned to her original resting position as I turned to head back into the crowd. As I was about to step away though, I turned back around."

            mc "Oh! I just realized I never got your name!"

            show erika default with dissolve

            erika "Don't worry about it; it's Erika. See you on the court."

            mc "Alright Erika. Thanks again, I'll think about the tennis club!"

            hide erika with dissolve

            "She gave a limp wave to me and starting picking at something on the table."

            "A little standoffish, but she didn't seem too bad. Makes me wonder what she must be like during a game."

            stop music fadeout 1.0
            
            "With nothing left to say, I headed back into the crowd of students."

            play music "bgm/Android_Star.mp3"

            jump clubfair_rowchoice

    label clubfair_becca: 

        $ becca_visited = True

        # [SECOND ROW]
        # (Becca's introduction, soccer club)

        "Down this row, it seemed like it was a mix of casual clubs with a couple stray sports clubs leaking over from the row next to it."

        "The photography club had set up a small collage full of different shots that had been made the previous year, both on campus and on their club field trips."

        "That might be fun for getting off-campus every so often..."

        "The chess club seemed to have put together a game of speed chess between some of its members to help show off the more exciting ways to play."

        "I continued on, nearing the end of the row when-"

        # {cutout, soccer ball flies across the screen}

        mc "Uwaah!!" with vpunch

        $ renpy.pause(1.0)

        "What was that?! I thought I saw a ball or something pass right in front of my face. I stumbled backwards a little bit, catching myself on another student before I fell to the ground."

        "It looks like the flying ball had grabbed the attention of other nearby students as well, as an athletic-looking girl ran across the room to retrieve her soccer ball."

        show becca surprised with dissolve

        "As she picked up the ball and turned to see all the attention she'd garnered, she looked embarrassed as she walked back to her table."

        show becca sheepish

        unknown "Eh heh heh... Sorry everyone! Guess I still have to work on my coordination..."

        hide becca with dissolve

        "As soon as she reached the table again, things in the activities building returned to normal."

        $ renpy.pause(1.0)

        show becca default with dissolve

        "As I walked by the soccer table, the same girl who almost hit me called out in my direction."

        show becca happy

        unknown "Excuse me!"

        menu:
            with dissolve

            "Stop and talk to her":
                jump clubfair_becca_stop

            "Continue walking":
                jump clubfair_becca_continue

        label clubfair_becca_continue:

            hide becca with dissolve

            "I decided to keep moving through the clubs. I dunno what might happen if I stick around there any longer."

            jump clubfair_rowchoice

        label clubfair_becca_stop:

            $ becca_talked = True

            "I thought it'd be rude if I didn't at least hear this girl out."

            stop music fadeout 1.0

            # {CG, Becca, balancing a soccer ball on her foot}

            show cg becca_intro with Dissolve(1.0)

            play music "bgm/Becca.mp3"

            $ renpy.pause(1.0)

            unknown "Sorry about that, I can't believe I almost hit you there! And just after the coach had complimented me on my improved control..."

            "The girl looked at me with a nervous smile before looking back to the soccer ball she was handling. She rocked a little back and forth, trying to keep the ball balanced."

            "I'm surprised how at ease she looked, both because of what had just happened as well as the hoodie she was wearing. I thought it would restrict her movements, but apparently not."

            unknown "A couple girls had walked up asking to see if I could do some tricks, but I guess I got a little carried away. Anyways, I think I should probably give a proper greeting."

            # {CG change}

            scene bg club_fair with Dissolve(1.0)

            "She kicked the ball up into her hand and held out the other towards me."

            show becca happy with dissolve

            becca "I'm Becca, sophomore! Nice to meet you!"

            "I flinched slightly as she kicked the ball, worried it might slip out of her hold and fly towards me, but it seemed like her grip was pretty good."

            mc "I'm... [mcname]. Nice to meet you. So I'm guessing this is the soccer club?"

            show becca default

            becca "Yep, that's us! And I swear the rest of the team is better at handling than I am, haha."

            # {CG return}

            show cg becca_intro with Dissolve(1.0)

            $ renpy.pause(1.0)

            "She returned to her balancing exercise."

            mc "It doesn't look like you're too bad yourself, honestly."

            becca "Hahaha, maybe, but there are definitely better players on our team!"

            becca "So, didja wanna join the soccer team?"

            mc "Hm? Oh, I dunno about that, I haven't played soccer with a team since I was in grade school..."

            "And the last time I did, I ended up getting benched for missing too many kicks and hitting other kids. Maybe not the best idea to test out my skills again."

            becca "Oh, you don't have to worry about any of that."

            becca "I mean hell, I hadn't played a proper soccer game until I decided to join the club here, and now I'm sitting as a second-string midfielder! The seniors are all really helpful and happy to teach newcomers."

            "Wow, that is pretty impressive if she's made that much progress over a year. Maybe trying again wouldn't be so bad in this kind of setting..."

            "I decided to grab a sign-up sheet from the table."

            mc "I'll think about it. No harm in giving it a shot, right?"

            becca "Oh goodie! I guess it's not all bad that I messed up my trick earlier then!"

            "I gave a nervous chuckle."

            mc "Y-yeah, I guess so. I'll see you around then, alright?"

            "Becca nodded vigorously."

            becca "For sure! Nice to meetcha, [mcname], and I'll see you out on the field!"

            scene bg club_fair with Dissolve(1.0)

            "She was still waving and yelling something at me as the crowd started to drown her out."

            "She's definitely an excitable girl, which probably makes her perfect for being on the field. Certainly didn't seem like there could be a dull moment with her around."

            stop music fadeout 1.0

            "Making one last check for any additional flying soccer balls, I made my way back into the crowd."

            play music "bgm/Android_Star.mp3"

            jump clubfair_rowchoice

    label clubfair_nikki:

        $ nikki_visited = True

        # [THIRD ROW]
        # (Nikki's introduction, radio station)
        
        "As I turned the corner down this row of tables, something immediately grabbed my attention amidst the displays."

        # {cutout of the table}

        "One table in the middle was completely walled off from the rest, and the wall behind the table barely fit into the row."

        "Alright, now I had to know what was going on over there. I slowly pushed my through the crowd to the curious table."

        mc "Excuse m-"

        stop music fadeout 1.0

        # {CG, Nikki sitting at the table with a laptop and mic set up}

        show cg nikki_intro with Dissolve(1.0)

        play music "bgm/Nikki.mp3"

        $ renpy.pause(1.0)

        "I quickly cut my question short as I noticed what was going on."
        
        "It was almost tough to see the person manning the table behind all of her equipment. A red-haired girl sat behind a large standing microphone and a small laptop, seemingly separated from the fair going on."
        
        "I didn't want to intrude, so I kept quiet as she continued speaking into the mic. I wasn't even sure she had noticed me."

        if becca_visited:

            # [INCIDENTAL DIALOGUE, ONLY APPEARS IF BECCA WAS SEEN FIRST]

            unknown "...The fair is still going strong as we reach the final exhibition hour."

            unknown "A rampant soccer ball flew across the building earlier, but as far as I can tell there were no casualties and the fair is continuing as planned."

        unknown "Next up, we'll be playing a track from denshuto called \"This Moment, Together With You\"."

        unknown "A reminder that you can stop by our table at the club fair for more information on the radio station, as well as upcoming events."

        unknown "This is Nikki with the Monday Night Mash-Up, and I'll see you after the break."

        # {CG change}

        scene bg club_fair with Dissolve(1.0)

        show nikki default with dissolve

        "She flipped a switch on her mic and pulled her headphones off, then started typing quickly on her laptop."

        unknown "Alright, song's going. Did you want to pick up an application or something?"

        "I was a little startled, since she talked without her eyes ever leaving the screen."

        mc "Ah! Well, I was just curious about what kind of club would be set up like this, but I guess this is for the radio station?"

        nikki "That's right. I'm Nikki, the student president of the radio station and one of the DJs."

        $ renpy.pause(1.0)

        "I couldn't tell if she wanted me to leave or not, but I was interested in learning more about what she was doing, so I tried to spark up a conversation."

        mc "So... how hard is it to do all of..."

        "I awkwardly gestured towards the complicated setup behind Nikki's table."

        mc "...this, in the middle of a crowded area?"

        show nikki talk

        nikki "It's not much of a struggle. Just gotta monitor the sound levels constantly to make sure the mic isn't picking up too much crowd noise."

        nikki "I had to do some appeal work to make sure I got a spot next to an outlet, and I've got some wires running underneath the table to help stabilize my connection so that the show doesn't experience any dead air."

        show nikki default

        "It sounded like a pretty complicated process, but the way she talked about it made it sound effortless."

        mc "I'm kind of impressed that you can run your show and handle the club fair at the same time."

        nikki "It's not too bad, honestly. Most people don't stick around too long and if they do I threaten them with an interview if they wanna stay longer."

        mc "Oh! Well... I guess I should probably get going, don't wanna hold you up..."

        $ renpy.pause(1.0)

        "Nikki looked up at me from behind her laptop without moving her head."

        show nikki talk

        nikki "I was kidding, don't worry about it. You can stay however long you want, I just might have to do another bumper in the middle of a conversation."

        show nikki default

        mc "O-oh, haha..."

        "She was a dangerous one. Her expression hadn't changed, so I couldn't tell she was joking at all."

        menu:
            with dissolve
            "Head out":
                jump clubfair_nikki_headout
            
            "Stay and chat":
                jump clubfair_nikki_chat

        label clubfair_nikki_headout:

            mc "Alright, well either way I should probably get going, plenty more to see at the fair."

            "Nikki only nodded in response, caught up in something on her laptop."

            hide nikki with dissolve

            "Not the most sociable person, but she definitely seems dedicated to what she does. I wonder what her show is like..."

            stop music fadeout 1.0

            "These are the thoughts that passed through my mind as I headed back into the crowd."

            play music "bgm/Android_Star.mp3"

            jump clubfair_rowchoice

        label clubfair_nikki_chat:

            $ nikki_talked = True

            "I hadn't really thought about it before, but having a radio show might be neat. Even on a college station, you get to broadcast yourself out to people near campus."

            "That kind of attention is a little intimidating, but exciting at the same time."

            "I picked up one of the sign-up sheets off the table and looked over it a bit."

            mc "I don't see anything on here about experience, does that mean anyone can sign-up for a show?"

            # [Nikki has already looked away from her screen, to explain to MC that she was just joking about the interview.]

            "Nikki looked me straight in the eyes."

            show nikki talk

            nikki "Oh, not at all. If we let any student have a show, do you know how many edgy \"shock jock\" shows we'd have every day?"

            show nikki default

            mc "Ah, haha, I guess you've got a point."

            show nikki talk

            nikki "It's not too hard to get a show though."

            nikki "With a couple weeks of studying under another DJ you'll get all the experience you need, and as long as you have an interesting or unique show idea you'll probably get a slot somewhere in the week."

            nikki "That said, if you don't think you could run a show on your own, you can always bring a friend along or join a currently running show. We've had more than a couple duos start out that way."

            show nikki happy

            nikki "We also ask you to contribute a bit to the station, either by handling incoming CDs or going out for any of the events we cover or participate in for community service."

            nikki "It might seem like a heavier load than other clubs, but with as members as we have, you only tend to go to one or two events a year."

            "Wow, Nikki did a complete 180 once she started talking about the station. She seemed almost... animated as she went over the process with an unexpected vigor."

            show nikki default

            $ renpy.pause(1.0)

            nikki "...Ah."

            "Just as I had thought that, though, she seemed to have realized something."

            "Nikki quickly returned to her laptop."

            nikki "Sorry, got a little carried away there. If you come to our first meeting this weekend, you'll hear all that and more when we go over the process for all incoming members."

            mc "Oh, okay. Where do you guys meet?"

            nikki "Broadcast building is behind the main hall, you'll be able to find it by the large beacon on the roof."

            "An alarm went off as she finished her sentence."

            nikki "Well, looks like it's about time for me to get back on air."

            mc "Alright, I better head out too. Maybe I'll see you at the meeting?"

            hide nikki with dissolve

            "Nikki gave a quick thumbs up as she put on her headphones and prepared the microphone, and I turned to head back into the crowd."

            stop music fadeout 1.0

            "I left feeling... surprisingly enthused about the idea of joining the radio station. I'll have to keep that in mind for the weekend."

            play music "bgm/Android_Star.mp3"

            jump clubfair_rowchoice

    label clubfair_outside:

        # (Julianne's introduction, jazz band)

        stop music fadeout 1.0

        "The sounds of excited students died out as I exited the activities building, but outside there seemed to be a different commotion."

        # {Campus, outside night}

        scene bg campus_night with dissolve

        "It seems like the music clubs had been taking turns on a makeshift stage outside the building playing songs in order to drum up interest from passing students."

        "I guess I was catching the tail end since the only group not packing up instruments or their tables was the jazz band, who barely fit on the little stage."

        # {CG, Julianne grooving on stage w/ bass, partial band in partial background}

        show cg julianne_intro with Dissolve(1.0)

        play music "bgm/Funky_Chunk.mp3"

        $ renpy.pause(1.0)

        "Everyone seemed to be having a good time performing, but the girl on the bass seemed to be having a blast. She used her mobility to her advantage, dancing along to the beat, hair flowing behind her."

        "She was full of energy and helped to make it feel like more of a performance than just a demonstration."

        "I couldn't take my eyes off of her throughout the song."

        # {campus, outside, night}

        scene bg campus_night with Dissolve(1.0)

        stop music fadeout 3.0

        "It seems like I had made it just in time for the last song of the night, because as soon as the last note rang out, the band took a bow and began to pack up. I applauded the performance, never taking my eyes off the energetic bassist."

        $ renpy.pause(0.5)

        show julianne happy with dissolve

        $ renpy.pause(0.5)

        show julianne default

        "She had wiped the sweat from her face with a towel, and noticed me staring once she had finished."

        $ renpy.pause(0.5)

        show julianne wink

        $ renpy.pause(0.5)

        show julianne happy

        "She winked at me and I blushed, completely stunned from embarrassment."

        menu:

            with dissolve
            "Leave in a hurry":
                jump clubfair_julianne_leave

            "Walk forward":
                jump clubfair_julianne_approach

        label clubfair_julianne_leave:

            hide julianne with dissolve

            "I was so embarrassed I didn't know what else to do. I quickly turned and fled. What made me do that? Some kind of survival instinct, maybe."

            "Either way, I was gone in a flash, leaving that girl in the dust."

            jump clubfair_end

        label clubfair_julianne_approach:

            $ julianne_talked = True

            "I was embarrassed, but I couldn't just leave without some kind of congratulations or something."

            "I felt like I needed to show my appreciation for the performance somehow, so I timidly walked towards the bassist, who was the only one not currently packing up."

            play music "bgm/Julianne.mp3"

            show julianne happy with dissolve

            unknown "Hey you! Seems like you enjoyed the show."

            mc "Y-yeah. I'm not usually one for jazz or anything, but the energy you all played with really got me into it."

            unknown "Hahaha, I like to think that's our charm; we're not the best band or the most technical, but we make up for it with our showmanship."

            "She put her hand out to greet me."

            show julianne default

            julianne "The name's Julianne, and I'm one of the co-directors for the jazz band. Well, and the concert band, but we wouldn't have been able to get them all out here tonight, haha."

            "I shook her hand, hoping she wouldn't notice mine was trembling."

            mc "I'm... [mcname]."

            julianne "Well it's a pleasure to meet you, [mcname]. Ever thought of performing, or are you more comfortable in the audience?"

            mc "I mean, I played recorder back in grade school, but I don't think that really counts..."

            show julianne happy

            julianne "Haha, any experience can help! If you're interested, there's no time like the present, right?"

            julianne "We've got plenty of teachers you can take private lessons with, and even if you don't perform this year, with enough practice you could properly join a group next year."

            "I was a little overwhelmed just by the thought of it all. She certainly had a sort of energy that made me consider the idea though."

            show julianne default

            julianne "Even if you don't wanna join, you can always sit in on our practices to listen or come to the shows we do every semester."

            julianne "We usually have one night for jazz performances and one for concerts, so it's not that big of a commitment."

            hide julianne with dissolve

            $ renpy.pause(0.5)

            show julianne happy with dissolve

            "She quickly dug through her bag behind the amplifier and passed me a flyer detailing all the different groups on campus."

            julianne "You can feel free to come to any of the practices and see which fits you best, if you're still interested in joining one of the groups."

            julianne "The schedules for the practices are there, and the concerts will be announced later."

            show julianne default

            "As Julianne finally stopped talking, I unfortunately stared at her, mouth slightly agape as I tried to process everything she had just said."

            show julianne surprised

            julianne "Oh, sorry! I'm told I have a problem of talking a bit too fast when it comes to this sort of stuff."

            show julianne default

            julianne "But if you get the chance, drop by a practice and you'll have more time to talk to any of the members and learn more about our programs."

            mc "O-okay."

            julianne "Alright, I've gotta run out since the director is trying to give a pep talk to everyone, but I hope to see you sometime late this week. Bye, [mcname]!"

            hide julianne with dissolve

            stop music fadeout 2.0

            "I was able to mutter out a weak \"Yeah\" before she unplugged her bass and ran off to join the rest of the band."

            "I was still a little overwhelmed by all the information Julianne had dropped on me, but I got the major gist of it."

            "Even though it all seemed really intimidating, she gave off an aura that made me think that even I could eventually learn an instrument."

    label clubfair_end:

        # fade to black

        scene black with Fade(2.0, 0.0, 2.0)

        play music "bgm/Summer_Night_Sky.mp3"

        "A little fried from everything that had happened this evening, I turned to make my way back to my dorm room, in order to unwind and sort out the papers I had gotten."

        # change scene to dorm room

        scene bg dorm_room_furnished with fade

        "As soon as I had entered my room, I fell face-first on the bed, letting the applications fall from my hands and onto the floor."

        "All the pushing and shoving during the fair, the soccer ball accident, everything about the night had been exhausting."

        mc "At least my first class tomorrow doesn't start until noon..."

        "I was covered in sweat, and I was pretty sure that most of it wasn't mine. I'd need a lot of time to feel good again in the morning."

        "Thankfully, Charlie and I had separate bathrooms, so I wouldn't have to worry about inconveniencing her."

        $ renpy.pause(1.0)

        "Speaking of, Charlie apparently was home and had started rapping on my bedroom door."

        show charlie happy with dissolve

        charlie "Well hey, look who's back! Didn't know when you were gonna make it, how'd it go?"

        "I could only moan in response. I slowly moved myself into a sitting position as Charlie pulled up a chair."

        show charlie default

        charlie "Haha, that bad huh? I know what you mean, that building can be hell to navigate when it's full of students."

        mc "Did you not go?"

        charlie "Nah, I'm busy enough as it is with one club, so I'm not looking for another commitment."

        "She looked around the room a bit before her eyes settled on the papers I had dropped on the way in."

        show charlie happy

        charlie "Oh, you picked up some applications, that's good! Anything in particular catch your eye?"

        "How many clubs had I seen tonight? Could I even distinguish the different tables from each other? I racked my brain for some ideas."

        "What stood out in my mind most was..."

        menu:
            with dissolve
            "The soccer club":
                jump clubfair_end_soccer

            "The tennis club":
                jump clubfair_end_tennis

            "The radio station":
                jump clubfair_end_radio

            "The jazz band":
                jump clubfair_end_band

            "Nothing in particular, actually...":
                jump clubfair_end_none

        label clubfair_end_soccer:

            "I involuntarily rubbed my forehead as I thought about my close encounter with the soccer club."

            mc "Well, it's not so much that the club caught my eye as much as I almost caught a soccer ball with my face."

            show charlie surprised

            charlie "Holy shit? What happened there?"

            "I recounted my fair experience with Becca to Charlie, from the near collision to the follow-up discussion."

            show charlie happy

            charlie "Oh wow, that's certain one way to get people's attention, hahaha!"

            "I couldn't help but laugh along with Charlie, the absurdity of the whole thing getting to me."

            if becca_talked:

                show charlie default

                charlie "Well, it was nice of her to apologize for it afterwards, and it seemed like you had a pretty good attitude about it."

                mc "Yeah, she actually seemed pretty cool, just a little clumsy is all. No need to get too worked up about it."

                "I thought about how nice she was to me after the near-accident, and how her enthusiasm was almost infectious."

                "Even though I wasn't much for the sport, the way she talked about it made me want to try."

                charlie "So after an experience like that, do you think you're gonna join the soccer team?"

                mc "I dunno. I haven't touched a soccer ball in years. It'd probably just be a year of practice, but it might be fun if everyone's as energetic as Becca."

            else:

                show charlie default

                charlie "So after an experience like that, do you think you're gonna join the soccer team?"

                mc "I dunno. I haven't touched a soccer ball in years. It'd probably just be a year of practice, but it might be fun."

            charlie "Well I hear they do a lot of recreational games in between their tournament matches, so you might see some action near the end of the season."

            "I thought about the prospect for a while."

            "It's not like I was really concerned about playing professionally or anything, so a little exercise and a chance to make friends didn't sound too bad."

            mc "Well, I'll think about it."

            jump clubfair_sleep

        label clubfair_end_tennis:

            "I thought about all the flashy and interesting tables before my mind wandered to the single desolate table I had encountered."

            mc "Well, I guess the most interesting table to me was the one that was completely bare."

            show charlie surprised

            charlie "What!? Some poor club didn't even take the time to decorate their table?"

            mc "From what I was told by the girl running it, the other members of the tennis club who were supposed to help out just completely ditched the fair."

            show charlie thinking

            charlie "Oh, I bet she wasn't happy about that."

            if erika_talked:

                mc "Haha, that'd be an understatement. She almost scared me away with the way she looked at me, but she seemed okay once I started talking to her."

                show charlie default

                charlie "That's good to hear! At least she could be personable to prospective members."

                "I thought about our conversation, and my embarrassing admission when she asked about my tennis experience."

                "But even though she laughed, I felt like it was in good fun. Erika seemed like a deadly serious person, but it might be nice to hang out with her more."

            else:

                mc "Haha, that'd be an understatement. Her stare terrified me, so quickly took one of the applications and left as soon as I could."

                show charlie surprised

                charlie "Geez, I heard the tennis club took itself seriously, but I didn't know that translated to their club fair activities too."

            show charlie default

            charlie "So are you considering joining?"

            mc "I dunno. I've never actually played tennis before, but learning something new could be fun."

            show charlie happy

            charlie "That's a good attitude to take about it! Plus, this school is pretty well-known for its tennis team, so you're in the right place to get started."

            mc "Also, I wouldn't have to worry about being in any of the games, so I wouldn't hold anyone back."

            jump clubfair_sleep

        label clubfair_end_radio:

            "As I tried to recall all the different tables I had seen, I remembered the odd display I had seen while walking through the building."

            mc "Well, I was surprised to see that the radio station had a table and was broadcasting a show from inside the fair building."

            show charlie surprised

            charlie "Oh wow, really?"

            "I told Charlie about Nikki and her fair broadcast."

            show charlie happy

            charlie "That's pretty cool actually! Last year, it was just set up like a merch table and some of the DJs were giving away shirts and bumper stickers for the station."

            mc "She seemed like she was in the zone the whole time, because even when she was talking to me, she was working on something on her laptop."

            if nikki_talked:

                mc "...Except for when I asked about how the radio station was run. She was really into the process and seemed to know a lot. I guess that's why she's president."

                mc "Like I looked at her setup and was intimidated just by how much seemed to be going on, but the way she talked about it made it seem so easy."

                mc "I'd love to be that confident about something I'm passionate about, haha..."

                # (something else goes here)

            show charlie default

            charlie "Would've never pegged you for someone who'd want to be on the radio. You seem more the reserved type."

            mc "Yeah... but I dunno, I'm not really addressing anyone, am I? I just sit behind a microphone and play music for a while."

            mc "Seems like a pretty nice way to spend some time during the week. I'd just have to get through some training."

            show charlie happy

            charlie "Well, if it does work out, know that you've got at least one listener!"

            "She gave me a thumbs up and I chuckled."

            mc "Thanks."

            mc "Nikki said the first meeting would be an introduction to the work and process I'd have to go through, so maybe I'll stop by and let my impressions there guide me."

            jump clubfair_sleep

        label clubfair_end_band:

            "Of all the things that happened at the fair, it was what happened outside of the fair that had come to mind."

            mc "Well, I caught the end of the jazz band's performance as I was heading back."

            show charlie default

            charlie "Oh, some of my friends have been trying to get me to come to a performance for a while, but jazz isn't really my thing. How was it?"

            mc "I mean I'm not much for music but I loved their performance. They all looked like they were having a lot of fun, dancing along as they played."

            $ renpy.pause(1.0)

            "I unconsciously started twirling my hair with my fingers."

            $ renpy.pause(1.0)

            mc "...Especially the girl who was on bass."

            show charlie happy

            charlie "Ooo, looks like someone's interested. Tell me more, tell me more!"

            if julianne_talked:

                mc "Well..."

                "I told Charlie about watching Julianne during the performance and my quick, sorta one-sided discussion with her afterwards."

                charlie "Hahaha, sounds like someone has a little crush!"

                "I made a bit of a huff at that comment, but I couldn't really deny it."

            else:

                mc "Oh! W-well, uh... I didn't talk to her or anything, I just thought she was cool and had an upbeat attitude about the whole thing."

            $ renpy.pause(0.5)

            show charlie thinking

            $ renpy.pause(0.5)

            charlie "It'd probably be tough to learn an instrument and play in the group. You have to worry about keeping up with practice as well as tutoring so you can catch up with everyone else."

            mc "Yeah, that might be a lot of work while I'm still getting used to everything here at school… I'll have to think about this more."

            jump clubfair_sleep

        label clubfair_end_none:

            mc "I dunno, nothing really grabbed me, I guess. Maybe I'll go to a couple first meetings and shop around some more."

            show charlie happy

            charlie "Well if that's the case, maybe you can swing by the botany club!"

            show charlie default

            charlie "At the start of the year everyone gets to put together their own little flower bed to take care of for the semester."

            charlie "If nothing else, it'll be easier to enjoy club activities with someone you already know, right?"

            mc "Yeah, you may be right about that..."

            charlie "Give it some thought, okay? We don't meet until Thursday so you've got some time. I'd love to have another friend join!"

            mc "Sure, I'll let you know by Wednesday then."

            jump clubfair_sleep

        label clubfair_sleep:

            $ renpy.pause(1.0)

            "I looked over to my clock and was shocked by just how late the club fair had run."

            mc "Well, it's been nice, but I think it's about time I hit the hay."

            show charlie happy

            charlie "No prob! I have a morning class tomorrow so I should probably get to bed too. See you tomorrow!"

            mc "Yeah, see you..."

            stop music fadeout 3.0

            scene black with Fade(3.0, 0.0, 3.0)

            "I barely finished my sentence before my fatigue set in and I closed my eyes. The last thing I heard before falling asleep was Charlie closing my door."

            $ renpy.pause(2.0)

            "I dreamt of my future here. What lied in store for me?"

            # WE DID IT! WE OUT HERE

            # SHOW THAT LOGO AGAIN, BABY

            scene logo with Fade(2.0, 0.0, 2.0)

            $ renpy.pause(5.0)

            scene black with Fade(2.0, 0.0, 2.0)

    return
