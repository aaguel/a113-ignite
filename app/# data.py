# data.py — A113 Ignite training dataset
# Every book hand-labeled by Althea Aguel, Disney Publishing 2023-2026

BOOKS = [
    # Each book: (title, author, year, audience, genre, tone, is_franchise, is_series, has_romance,
    #             dark_academia, emotional_devastation, romance_slowburn, enemies_to_lovers,
    #             fandom_nostalgia, mystery_hook, identity_COA, aesthetic_vibes,
    #             fandom_franchise, found_family, cultural_identity, lgbtq+)

    # ── 2026 ──
    ("In Between Days", "Camryn Garrett", 2026, "YA", "contemporary", "emotional", 0, 0, 1,
     0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1),

    ("The Last Rhee Witch", "Jenna Lee-Yun", 2026, "MG", "fantasy", "atmospheric", 0, 1, 0,
     0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0),

    ("Wish Upon a K-Star", "Kat Cho", 2026, "YA", "contemporary", "lighthearted", 0, 0, 1,
     0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0),

    ("Body Count", "Codie Crowley", 2026, "YA", "horror", "dark", 0, 0, 0,
     0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0),

    ("Griffin Speaker", "Matt Rockefeller & Jan M. Flynn", 2026, "MG", "fantasy", "action-packed", 0, 0, 0,
     0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0),

    ("A Descendants Mystery", "Melissa de la Cruz", 2026, "YA", "franchise-fantasy", "lighthearted", 1, 1, 1,
     0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0),

    ("Don't Close This Book! (Toy Story 5)", "Satoshi Hashimoto & Phaea Crede", 2026, "CH", "franchise", "funny", 1, 0, 0,
     0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0),

    # ── 2025 ──
    ("How Far I'll Go (Twisted Tale)", "Keala Kendall", 2025, "YA", "franchise-fantasy", "lighthearted", 1, 1, 0,
     0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0),

    ("Mufasa: The Lion King Novelization", "Disney Press", 2025, "MG", "franchise", "emotional", 1, 0, 0,
     0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0),

    ("Snow White Novelization", "Elizabeth Rudnick", 2025, "MG", "franchise", "lighthearted", 1, 0, 1,
     0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0),

    ("Encanto: Nightmares y Sueños", "Alex Segura", 2025, "YA", "franchise-fantasy", "atmospheric", 1, 0, 0,
     0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0),

    ("Reasons We Break", "Jasmeen Kaur Deo", 2025, "YA", "contemporary", "emotional", 0, 0, 1,
     0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0),

    ("Seeing Stars: A Mashad Family Novel", "Unknown", 2025, "YA", "contemporary", "lighthearted", 0, 1, 1,
     0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0),

    ("The Wishless Ones", "Hafsah Faizal", 2025, "YA", "fantasy", "atmospheric", 0, 1, 1,
     1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0),

    ("Grandmas Are Magic", "Yamile Saied Méndez", 2025, "CH", "picture-book", "lighthearted", 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),

    ("5-Minute Moana Stories", "Disney Storybook Art Team", 2025, "CH", "franchise", "lighthearted", 1, 0, 0,
     0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0),

    # ── 2024 ──
    ("Inside Out 2 Junior Novelization", "Disney Press", 2024, "MG", "franchise", "emotional", 1, 0, 0,
     0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0),

    ("Go the Distance (Twisted Tale)", "Jen Calonita", 2024, "YA", "franchise-fantasy", "emotional", 1, 1, 1,
     0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0),

    ("A Drop of Venom", "Sajni Patel", 2024, "YA", "fantasy", "dark", 0, 0, 1,
     1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0),

    ("Dream Chasing", "Bob Weis", 2024, "Adult", "nonfiction", "lighthearted", 0, 0, 0,
     0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0),

    ("Breaking the Dark: A Jessica Jones Novel", "Lisa Jewell", 2024, "Adult", "mystery", "dark", 1, 0, 0,
     0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0),

    ("National Geographic Kids Almanac 2024", "National Geographic", 2024, "CH", "nonfiction", "lighthearted", 0, 1, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),

    # ── 2023 ──
    ("The Story of Disney: 100 Years of Wonder", "Disney Editions", 2023, "Adult", "nonfiction", "lighthearted", 1, 0, 0,
     0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0),

    ("The Disney Book: New Edition", "DK Publishing", 2023, "Adult", "nonfiction", "lighthearted", 1, 0, 0,
     0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0),

    ("Disney 100 Years of Wonder Storybook Collection", "Disney Press", 2023, "MG", "nonfiction", "lighthearted", 1, 0, 0,
     0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0),

    ("A Twisted Tale Anthology", "Elizabeth Lim", 2023, "YA", "franchise-fantasy", "mixed", 1, 0, 1,
     0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0),

    ("Star Wars: Quest for Planet X", "Tessa Gratton", 2023, "MG", "sci-fi", "action-packed", 1, 1, 0,
     0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0),

    ("Star Wars: Path of Vengeance", "Justina Ireland", 2023, "YA", "sci-fi", "dark", 1, 1, 0,
     0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0),

    ("Stories of Jedi and Sith", "Preeti Chhibber", 2023, "YA", "nonfiction", "action-packed", 1, 0, 0,
     0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0),

    ("The Sun and the Star", "Rick Riordan & Mark Oshiro", 2023, "YA", "fantasy", "emotional", 1, 0, 1,
     0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1),

    ("The Chalice of the Gods", "Rick Riordan", 2023, "YA", "fantasy", "action-packed", 1, 1, 1,
     0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0),

    ("Worth Fighting For", "Jesse Q. Sutanto", 2023, "YA", "contemporary", "emotional", 0, 0, 1,
     0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0),

    ("Gradchanted", "Morgan Matson", 2023, "YA", "contemporary", "lighthearted", 0, 0, 1,
     0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0),

    ("Kill the Beast (Villains Series)", "Serena Valentino", 2023, "YA", "franchise-fantasy", "dark", 1, 1, 0,
     1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0),
]

LABEL_NAMES = [
    "dark_academia",
    "emotional_devastation",
    "romance_slowburn",
    "enemies_to_lovers",
    "fandom_nostalgia",
    "mystery_hook",
    "identity_coming_of_age",
    "aesthetic_vibes",
    "fandom_franchise",
    "found_family",
    "cultural_identity",
    "lgbtq+"
]

GENRES = ["contemporary", "fantasy", "franchise-fantasy", "franchise", "horror",
          "mystery", "sci-fi", "nonfiction", "picture-book"]

TONES = ["dark", "lighthearted", "emotional", "funny", "atmospheric",
         "action-packed", "mixed"]

AUDIENCES = ["CH", "MG", "YA", "Adult"]