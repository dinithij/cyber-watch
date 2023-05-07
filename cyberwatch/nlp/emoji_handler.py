import re

def removeEmojis(text):
  text = u''+text+''
  regrex_pattern = re.compile(pattern="["
                                      u"\U0001F600-\U0001F64F"  # emojis
                                      u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                      u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                      u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                      "]+", flags=re.UNICODE)
  text = regrex_pattern.sub(r'', text)
  return text

def removeEmoticons(text):
    # approach 1: pattern for "generic smiley"
    eyes, noses, mouths = r":;8BX=", r"-~'^", r")(/\|DPpXxBbSs"
    pattern1 = "[%s][%s]?[%s]" % tuple(map(re.escape, [eyes, noses, mouths]))

    # approach 2: disjunction of a list of smileys
    smileys = """:-) :) :o) :] :3 :c) :> =] 8) =) :} :^) 
                 :D 8-D 8D x-D xD X-D XD =-D =D =-3 =3 B^D""".split()
    pattern2 = "|".join(map(re.escape, smileys))

    for emoticon in re.findall(pattern1, text):
        text = text.replace(emoticon, '')

    return text