import unittest
import os
import joblib
from cyberwatch.cyber_watch import CyberWatch

class CyberWatchTestCase(unittest.TestCase):
    def setUp(self):
        self.cyber_watch = CyberWatch()

    def test_cyberbullying_short_texts(self):
        text_1 = "OMG!!!! you are such a duumb asss 🤬🤬🤬. u shuld just stop talking !!! 😠🤬 #hatelosers #whitepower"
        self.assertEqual(self.cyber_watch.predict(text_1), "cyberbullying")

        text_2 = "just go and kill ur self !!!!!!  🤣🤣 soooo STBY! :D Your never gonna make it ever 🤣🤣🤣🤣  #worlddontneedyou #suckateverything"
        self.assertEqual(self.cyber_watch.predict(text_2), "cyberbullying")

        text_3 = "Your face looks like it was hitt by a truck :-P !!!! 😂😂 Disgasting #ugly #loser #nofriends www.youareugly123.com 😂😂"
        self.assertEqual(self.cyber_watch.predict(text_3), "cyberbullying")

        text_4 = "Hey!!!!! I just saw ur MSG 😂😂😂. That was hilarious 😝. How r u doing???? 🤔 bettertogther@bestie.com"
        self.assertEqual(self.cyber_watch.predict(text_4), "not_cyberbullying")

        text_5 = "I hve no idea y u r so srs all the time :-). U shud lighten up 100% ☺️ #YOLO"
        self.assertEqual(self.cyber_watch.predict(text_5), "not_cyberbullying")

        text_6 = "Hey man, HRU? Havent seen u in ages 🤔. Howz lifee treting u? 😊 Hope to SYS #LongTimeNoSee"
        self.assertEqual(self.cyber_watch.predict(text_6), "not_cyberbullying")

    def test_cyberbullying_long_text(self):
        text_7 = "I heard you tolking behind my back yestrday. That was really rude and uncalled for. And then u had the audacity to post a picture with me on Instagram!!!! Do you really think that's fuunny???? You need to grow up!!!! 😡👿 #HatersGonnaHate"
        self.assertEqual(self.cyber_watch.predict(text_7), "cyberbullying")

        text_8 = "I can't beleve I won the lottery!!! 🤩🤩🤩 My heart is raacing and I can't stop shaking !!!! This is such a huge blessing and I am so grateful. #blessed #luckyme 🤩"
        self.assertEqual(self.cyber_watch.predict(text_8), "not_cyberbullying")
        
        text_8 = "I can't beleve I won the lottery!!! 🤩🤩🤩 My heart is raacing and I can't stop shaking !!!! This is such a huge blessing and I am so grateful. #blessed #luckyme 🤩"
        self.assertEqual(self.cyber_watch.predict(text_8), "not_cyberbullying")

        text_9 = "You're such a loser, always whining about everything. Nobody likes you! #pathetic #loser #getalife"
        self.assertEqual(self.cyber_watch.predict(text_9), "cyberbullying")

        text_10 = "Here at home. Neighbors pick on my family and I. Mind you my son is autistic. It feels like high school. They call us names attack us for no reason and bully us all the time. Can't step on my front porch without them doing something to us,cyberbullying"
        self.assertEqual(self.cyber_watch.predict(text_10), "cyberbullying")

        text_11 = "\"Being bullied at school: High-achieving boys use further strategies to maintain masculinity, for example becoming bullies themselves, disrupting the lessons, or devaluing girlsâ€™ achievements https://www.bipartisanalliance.com/2019/12/being-bullied-at-school-high-achieving.html?spref=tw\",cyberbullying"
        self.assertEqual(self.cyber_watch.predict(text_11), "cyberbullying")

        text_12 = "\"There was a girl in my class in 6th grade who was a little autistic, and her parents thought itâ€™d be better to send her to a public school. She didnâ€™t fit in with the class and was lowkey bullied (it was actually high key but the teacher downplayed it and did nothing)\",cyberbullying"
        self.assertEqual(self.cyber_watch.predict(text_12), "cyberbullying")

        text_13 = "Heâ€™s probably a white gay kid from some suburb. We donâ€™t want him to shoot up his school...so no one bully him.,cyberbullying"
        self.assertEqual(self.cyber_watch.predict(text_13), "cyberbullying")


    def test_slang_and_hashtags(self):
        text_14 = "WTF NFW we are gonna let #Niggas to #RunThisCountry. USA belongs to #WhitePeopleOnly #WeMakeOurOwnRules"
        self.assertEqual(self.cyber_watch.predict(text_14), "cyberbullying")

        text_15 = "OMFG you are such a PITA #noonereallycaresaboutyou you better #goandlive your #funnylittlesadlife LMAO"
        self.assertEqual(self.cyber_watch.predict(text_15), "cyberbullying")

    def tearDown(self):
        # Clean up any resources used in the tests
        pass

if __name__ == "__main__":
    unittest.main()
