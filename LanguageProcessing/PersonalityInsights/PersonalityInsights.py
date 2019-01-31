# class PersonalityInsights:
#
#     def connect(self):
#


#  start https://cloud.ibm.com/apidocs/personality-insights?language=python
# input  https://cloud.ibm.com/docs/services/personality-insights/input.html#sufficient


import json

from watson_developer_cloud import PersonalityInsightsV3

personality_insights = PersonalityInsightsV3(
  version='2018-08-01',
  iam_apikey='3SxyLvrknAbDrpuUwKZAhkyx6Y8pfYbSRUBrpM1x5yCW',
  url='https://gateway-lon.watsonplatform.net/personality-insights/api'
)

data = {
   "contentItems": [

      {
        "content": "Supersoulers let's lift our spirits pray and hold Paris in the Light\ud83d\ude4f\ud83c\udffe",

        # Non Mandatory fields

        # "contenttype": "text/plain",
        # "created": 1447602477000,
        # "id": "665919171062927360",
        # "language": "en"
      },

      {
         "content": "Wow, I liked @TheRock before, now I really SEE how special he is. The daughter story was IT for me. So great! #MasterClass",
      },
      {
         "content": ".@TheRock how did you Know to listen to your gut and Not go back to football? #Masterclass",
      },
      {
         "content": ".@TheRock moving back in with your parents so humbling. \" on the other side of your pain is something good if you can hold on\" #masterclass",
      },
      {
         "content": "Wow aren't you loving @TheRock and his candor? #Masterclass",
      },
      {
         "content": "RT @patt_t: @TheRock @Oprah @RichOnOWN @OWNTV this interview makes me like you as a fellow human even more for being so real.",
      },
      {
         "content": "\"Be You\".. That's the best advice ever @TheRock #MastersClass",
      },
      {
         "content": "RT @DeepakChopra: What I learned in week 1: Become What You Believe 21-Day Meditation Experience - https:\/\/t.co\/kqaMaMqEUp #GoogleAlerts",
      },
      {
         "content": "Watching Bryan Stevenson on #SuperSoulSunday! \"You are not the worst mistake you ever made\".\nAren't we glad  about that.",
      },
      {
         "content": ".@CherylStrayed  BRAVE ENOUGH my new favorite thing! Gonna buy a copy for all my girls. #Perfectgift https:\/\/t.co\/gz1tnv8t8K",
      },
      {
         "content": "Stevie Wonder singing \"Happy Birthday to you!\" to my dear  mariashriver. A phenomenal woman and\u2026 https:\/\/t.co\/Ygm5eDIs4f",
      },
      {
         "content": "It\u2019s my faaaaavorite time of the Year!  For the first time you can shop the list on @amazon! https:\/\/t.co\/a6GMvVrhjN https:\/\/t.co\/sJlQMROq5U",
      },
      {
         "content": "Incredible story \"the spirit of the Lord is on you\" thanks for sharing @smokey_robinson #Masterclass",
      },
      {
         "content": "Wasnt that incredible story about @smokey_robinson 's dad leaving his family at 12. #MasterClass",
      },
      {
         "content": "Gayle, Charlie, Nora @CBSThisMorning  Congratulations!  #1000thshow",
      },
      {
         "content": "I believe your home should rise up to meet you. @TheEllenShow you nailed it with HOME.  Tweethearts, grab a copy! https:\/\/t.co\/iFMnpRAsno",
      },
      {
         "content": "Can I get a Witness?!\u270b\ud83c\udffe https:\/\/t.co\/tZ1QyAeSdE",
      },
      {
         "content": ".@TheEllenShow you're a treasure.\nYour truth set a lot of people free.\n#Masterclass",
      },
      {
         "content": "Hope you all are enjoying @TheEllenShow on #MasterClass.",
      },
      {
         "content": ".@GloriaSteinem, shero to women everywhere, on how far we\u2019ve come and how far we need to go. #SuperSoulSunday 7p\/6c.\nhttps:\/\/t.co\/3e7oxXW02J",
      },
      {
         "content": "RT @TheEllenShow: I told a story from my @OWNTV's #MasterClass on my show. Normally I\u2019d save it all for Sunday, but @Oprah made me. https:\/\u2026",
      },
      {
         "content": ".@TheEllenShow is a master teacher of living her truth &amp; living authentically as herself. #MasterClass tonight 8\/7c.\nhttps:\/\/t.co\/iLT2KgRsSw",
      },
      {
         "content": ".@SheriSalata , @jonnysinc @part2pictures . Tears of joy and gratitude to you and our entire #BeliefTeam We DID IT!! My heart is full.\ud83d\ude4f\ud83c\udffe\ud83d\ude4f\ud83c\udffe",
      },
      {
         "content": "Donna and Bob saw the tape of their story just days before she passed. They appreciated it. #RIPDonna",
      },
      {
         "content": "RT @rempower: .@Oprah this series allowed me to slide into people's lives around the world and see the same in them ... we all have a belie\u2026",
      },
      {
         "content": "All the stories moved me, My favorite line \" I must pass the stories on to my grandson otherwise our people will loose their way. #Belief",
      },
      {
         "content": ".@part2pictures some of your best imagery yet. Filming Alex on the rock.#Belief",
      },
      {
         "content": "I just love Alex and his daring #Belief to live fully the present Moment.",
      },
      {
         "content": "RT @GrowingOWN: Let's do this! #Belief finale tweet tweet party. Thank you @Oprah! \ud83d\ude4f",
      },
      {
         "content": "RT @lizkinnell: The epic finale of #Belief on @OWNTV is about to start.  8\/et  Are you ready? What do you Believe?",
      },
      {
         "content": "Thank you all for another beautiful night of Belief. Belief runs all day tomorrow for bingers and final episode!",
      },
      {
         "content": "RT @OWNingLight: #Belief is the ultimate travel map to mass acceptance. \ud83d\ude4f\ud83c\udffb\u2764\ufe0f\ud83c\udf0d @Oprah",
      },
      {
         "content": "\" I can feel my heart opening and faith coming back in\".. What's better than that? #Belief",
      },
      {
         "content": "Hey Belief team mates can yo believe how quickly the week has passed? #Belief",
      },
      {
         "content": "Ran into @5SOS backstage. Fun times with @TheEllenShow today! https:\/\/t.co\/2PP3W3RzXc",
      },
      {
         "content": "Thanks All for another great night of #BELIEF",
      },
      {
         "content": "RT @3LWTV: #BecomeWhatYouBelieve New meditation w\/ @Oprah @DeepakChopra begins 11\/2  Register https:\/\/t.co\/x0R9HWTAX0 #Belief https:\/\/t.co\/\u2026",
      },
      {
         "content": "Ok west coast let's do it! #belief",
      },
      {
         "content": "Thank u kind gentleman who told me I had kale in my teeth. Was eating kale chips with  Quincy Jones. Went straight to @LairdLife party.",
      },
      {
         "content": "Hello west coast twitterati.. See you at 8 for #Belief",
      },
      {
         "content": "Thank you all for another beautiful night.#Belief",
      },
      {
         "content": "RT @PRanganathan: \"Transformation is the rule of the game. The universe is not standing still.\" - Marcelo @OWNTV @Oprah #Belief",
      },
      {
         "content": "\"The Universe is not standing still.. The whole Universe is expanding\"  I love the dance between science and spirituality! #Belief",
      },
      {
         "content": "\"Without our prayers and our songs we won't be here\" Apache leader.#Belief",
      },
      {
         "content": "Notice her mother crying. She knows its last tine she will ever see her daughter.#Belief",
      }
   ]
}

profile = personality_insights.profile(
        data,
        content_type='application/json',
        consumption_preferences=True,
        raw_scores=True
    ).get_result()

print(json.dumps(profile, indent=2))