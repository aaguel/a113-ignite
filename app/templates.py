# templates.py — BookTok content brief generator
# Maps predicted labels to concrete content strategies a creator can actually use

from app.data import LABEL_NAMES

# ── Content playbooks per label ───────────────────────────────────────────────
# For each BookTok angle, we define:
#   - hook: the opening line of a TikTok caption
#   - content_idea: what the creator should actually film
#   - audio_vibe: what kind of sound to use
#   - caption_templates: 3 ready-to-use captions

PLAYBOOKS = {
    "dark_academia": {
        "hook": "this book has no right being this atmospheric 🕯️",
        "content_idea": "Film yourself reading by candlelight or near a rainy window. Show the cover dramatically. No context.",
        "audio_vibe": "Soft classical piano or 'aesthetic study' sounds — think Chopin or lo-fi strings",
        "caption_templates": [
            "books that make you want to move into a gothic library and never leave 🕯️📚 #booktok #darkacademia #aestheticreads",
            "the atmosphere in this book is UNREAL. i felt like i was there 🖤 #darkacademia #booktok #mustread",
            "if you love dark academia vibes, stop what you're doing and read this 📖🕯️ #booktok #darkacademiabooks"
        ]
    },
    "emotional_devastation": {
        "hook": "i am not okay and you won't be either 😭",
        "content_idea": "React in real time to the gut-punch moment. Tissues optional but encouraged. Film the ugly cry.",
        "audio_vibe": "Sad piano — 'River' by Joni Mitchell style, or any trending sad sound on TikTok",
        "caption_templates": [
            "this book absolutely destroyed me and i am telling everyone to read it 😭📚 #booktok #sadbooks #emotionalread",
            "i need someone to talk to about this ending RIGHT NOW 😭 #booktok #bookends #devastated",
            "crying in the club because of a middle grade novel. no further questions 😭 #booktok #bookcrush"
        ]
    },
    "romance_slowburn": {
        "hook": "the slowest burn i have ever experienced and i loved every second 🔥",
        "content_idea": "Compile the almost-moments. Use text overlay to count down to the confession. Maximum yearning energy.",
        "audio_vibe": "Trending slow burn sounds — 'Slow Burn' by Kacey Musgraves or any pining audio",
        "caption_templates": [
            "THE SLOW BURN. THE PINING. I AM NOT WELL 🔥 #booktok #slowburn #romancebooks",
            "if you love books where they take FOREVER to get together, this is your sign 💫 #booktok #slowburn #romance",
            "i was rooting for them from page one and the payoff was WORTH IT 🔥📚 #booktok #slowburnromance"
        ]
    },
    "enemies_to_lovers": {
        "hook": "they hated each other. reader, they did not hate each other 👀",
        "content_idea": "Do a 'first meeting vs final chapter' comparison. Use the 'enemies to lovers pipeline' audio if it's trending.",
        "audio_vibe": "Dramatic classical to romantic pop transition — or any trending enemies-to-lovers sound",
        "caption_templates": [
            "enemies to lovers DONE RIGHT. i am obsessed 👀🔥 #booktok #enemiestolovers #romance",
            "they were so mean to each other and now i ship them more than anything 😭 #booktok #enemiestolovers",
            "the tension in this book had me in a chokehold from chapter one 👀 #booktok #slowburn #enemiestolovers"
        ]
    },
    "fandom_nostalgia": {
        "hook": "they made a book about it and my inner child is THRIVING 🥹",
        "content_idea": "React as a lifelong fan. Show childhood memorabilia alongside the book. 'I've waited years for this' energy.",
        "audio_vibe": "Original Disney theme or nostalgic childhood music — lean into the emotional callback",
        "caption_templates": [
            "my childhood self would have LOST IT over this book 🥹✨ #booktok #disney #nostalgia",
            "they really said 'here's more content from the thing you grew up loving' 🥹 #booktok #fandom #nostalgia",
            "disney adults rise up, this one is for us 🏰✨ #booktok #disney #disneyadult"
        ]
    },
    "mystery_hook": {
        "hook": "i stayed up until 3am because i HAD to know who did it 🔦",
        "content_idea": "Do a 'things that kept me up at night' list from the book. No spoilers — just vibes and dread.",
        "audio_vibe": "Tense thriller music — think Hans Zimmer suspense or true crime podcast energy",
        "caption_templates": [
            "i physically could not put this down until i had answers 🔦😰 #booktok #thriller #mysterybooks",
            "the twists in this book HAD ME. did not see any of that coming 😳 #booktok #thriller #mustread",
            "if you love staying up way too late because you NEED to know what happens 🔦 #booktok #mystery"
        ]
    },
    "identity_coming_of_age": {
        "hook": "this book understood me in ways i didn't know i needed 🥹",
        "content_idea": "Personal essay style — film yourself talking about why this book hit different. Authentic, no performance.",
        "audio_vibe": "Soft indie — Phoebe Bridgers, Gracie Abrams, or any introspective acoustic sound",
        "caption_templates": [
            "this book said everything i never had the words for 🥹📚 #booktok #comingofage #mustread",
            "if you're figuring yourself out, this book needs to be on your list 💫 #booktok #ya #comingofage",
            "the kind of book that makes you feel less alone 🥹 #booktok #representation #bookrecommendation"
        ]
    },
    "aesthetic_vibes": {
        "hook": "this came straight out of my vision board ✨",
        "content_idea": "Create a mood board video — book cover, color palette, aesthetic images that match the vibe. Very visual.",
        "audio_vibe": "Whatever is trending aesthetically on TikTok — cottagecore, K-pop, dark fantasy sounds",
        "caption_templates": [
            "the vibes in this book are IMMACULATE 😮‍💨✨ #booktok #aesthetic #bookaesthetic",
            "made a whole mood board for this book and i regret nothing ✨ #booktok #aesthetic #bookish",
            "if the aesthetic of a book matters to you, this one is everything 🌸 #booktok #bookaesthetic"
        ]
    },
    "fandom_franchise": {
        "hook": "more content from the universe i never knew i needed 🙌",
        "content_idea": "Hype video for existing fans. Reference specific moments from the original. Make it a love letter to the franchise.",
        "audio_vibe": "Original franchise music or fan-favorite soundtrack moments",
        "caption_templates": [
            "they really expanded the universe and i am NOT calm about it 🙌 #booktok #fandom #expandeduniverse",
            "for everyone who couldn't get enough of the original — this is for us 🙌 #booktok #fandom",
            "the lore just got so much deeper and i am here for every second 📚✨ #booktok #fandom #mustread"
        ]
    },
    "found_family": {
        "hook": "the found family in this book has my whole heart 🥹",
        "content_idea": "Make a 'meet the found family' video — introduce each character like you're introducing your own friends.",
        "audio_vibe": "Warm, feel-good indie — 'You've Got a Friend' energy or any cozy acoustic sound",
        "caption_templates": [
            "the found family dynamic in this book absolutely wrecked me (affectionately) 🥹 #booktok #foundfamily",
            "these characters are my friends now and i will not be taking questions 🥹📚 #booktok #foundfamily",
            "if found family is your weakness this book will destroy you in the best way 🥹 #booktok #foundfamily"
        ]
    },
    "cultural_identity": {
        "hook": "a book that made me proud of where i come from 🌍",
        "content_idea": "Share what the cultural representation meant to you personally. Or if you're not from that culture — share why it educated and moved you.",
        "audio_vibe": "Music from the featured culture — lean into the specificity, it's the whole point",
        "caption_templates": [
            "representation that actually gets it right 🌍✨ #booktok #ownvoices #representation",
            "the cultural details in this book are so specific and so beautiful 🌸 #booktok #diversebooks #mustread",
            "books that make you want to learn everything about a culture 🌍📚 #booktok #ownvoices #diversereads"
        ]
    },
    "lgbtq+": {
        "hook": "here's why everyone should read this",
        "content_idea": "For queer readers: personal reaction, what this rep meant. For allies: 'here's why everyone should read this'.",
        "audio_vibe": "Queer anthems or soft sapphic/mlm sounds — whatever is trending in LGBTQ+ BookTok",
        "caption_templates": [
            " #booktok #lgbtqbooks #representation",
            "wlw/mlm BookTok, this one is for you #booktok #queerbooks #lgbtq",
        ]
    }
}


def generate_brief(title, author, predicted_angles):
    """
    Takes a book title, author, and dict of {label: confidence}
    Returns a structured content brief for a BookTok creator.
    """
    if not predicted_angles:
        return {
            "title": title,
            "author": author,
            "angles": [],
            "summary": "No strong BookTok angles detected. Consider repositioning the premise."
        }

    angles = []
    for label, confidence in predicted_angles.items():
        if label in PLAYBOOKS:
            playbook = PLAYBOOKS[label]
            angles.append({
                "label": label,
                "confidence": confidence,
                "hook": playbook["hook"],
                "content_idea": playbook["content_idea"],
                "audio_vibe": playbook["audio_vibe"],
                "captions": playbook["caption_templates"]
            })

    # Top angle is the primary recommendation
    top = angles[0] if angles else None

    return {
        "title": title,
        "author": author,
        "top_angle": top["label"] if top else None,
        "angles": angles,
        "dramabox_note": f"For DramaBox: lead with the '{top['label'].replace('_', ' ')}' angle. "
                         f"Episode 1 hook should establish {top['hook']}" if top else ""
    }