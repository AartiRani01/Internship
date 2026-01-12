# Create two classes Camera and GPS, each having a method feature().
# Create a class SmartPhone that inherits from both Camera and GPS.
# Call the feature() method using a SmartPhone object and observe which method executes

class Camera:
    def features(self):     #Method with same name
        print("Camera features: Capture photo")


class Gps:
    def features(self):    #method with same name
        print("Gps features: Global coverage")


class SmartPhone(Gps,Camera):
    pass

# code to access both
# class SmartPhone(Camera, Gps):
#     def features(self):
#         Camera.features(self)
#         Gps.features(self)


smart_phone = SmartPhone()
smart_phone.features()        #Method Resolution Call (MRO)(decide which method to call)


#Python searches from left to right.
# So it finds features() in:
# Camera → FOUND
# It never reaches Gps
#That’s why Camera’s method is executed.