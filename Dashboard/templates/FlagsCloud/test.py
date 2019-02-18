from Dashboard.templates.FlagsCloud.wordclouds import flags
frequencies = {
            "Ukraine":2000,
            "Poland": 1000,
            "Trump": 200,
        }

flags(frequencies=frequencies,image='flags/ua.jpg',texts='alice.txt')