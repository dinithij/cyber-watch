from cyberwatch.cyber_watch import CyberWatch

watch = CyberWatch()
spel_param = {"spelling": False}
pred = watch.predict("LMK when you are in the NYC #Letsgrabsomecoffee #longtimenosee really want to #meetyousoon LYSM")
print(pred)
