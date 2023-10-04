class Bowler:

# ****** scaler data members
    __name = None   # Bowler's full name
    __nick = None   # short public name
    __country = None   # Country of bowler
    __debut = None   # year of debut in international career
    __arm = None   # left or right
    __category = None   # fast, mediam fast, leg spinner, off spinner, dark horse

# ****** list data members
    __against = []   # match against
    __runs = []   # runs given
    __wickets = []   # wickets taken

# ****** properties
    @property
    def nick(self):
        return self.__nick
    @nick.setter
    def nick(self, nn):
        self.__nick = nn

    @property
    def arm(self):
        return self.__arm
    @arm.setter
    def arm(self, arm):
        if arm == "left" or arm == "right":
            self.__arm = arm
        else:
            raise Exception("Invalid option for arm of the bowler")

    @property
    def Match(self, no=0):
        return self.__against[no], self.__runs[no], self.__wickets[no]
    @Match.setter
    def Match(self, mt):
        self.__against.append(mt[0])
        self.__runs.append(mt[1])
        self.__wickets.append(mt[2])

    @property
    def fiveWichets(self):
        fw = 0
        j = 0
        while j < len(self.__wickets):
            if self.__wickets[j] >= 5:
                fw += 1
            j = j+1
        return fw

# ****** magic/dunder methods
    def __str__(self):
        b = ""
        b += "("
        b += self.nick
        b += ", "
        b += self.arm
        b += " arm)\n"
        j = 0
        while j < len(self.__against):
            b += "Match No. "
            b += str(j+1)
            b += ": "
            b += self.__against[j]
            b += ", "
            b += str(self.__runs[j])
            b += ", "
            b += str(self.__wickets[j])
            b += "\n"
            j = j+1
        return b

# ****** init
    def __init__(self, nk, am):
        self.nick = nk
        self.arm = am

# ****** method / function members
    def update(self, no, mt):
        self.__against[no-1] = mt[0]
        self.__runs[no-1] = mt[1]
        self.__wickets[no-1] = mt[2]

    def updateWickets(self, no, wk):
        self.__wickets[no-1] = wk



