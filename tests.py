from packages.world.world import *;

#this test will create a world with some areas and print the world to see if they were created with the correct
#names and descriptions
#Test will ensure duplicate areas cannot be created and that the correct world and areas were created.
def newAreaTest():
    testWorld = World("Death Valley","A very dark and spooky place.", player("Johnny"))
    testWorld.newArea("Woods", "A very dense forest, you can hear the birds.")
    testWorld.newArea("Pond", "Its a deep pond, I cant see the bottom.")
    testWorld.printWorld()
    print "Two areas succesfully made."
    try:
        testWorld.newArea("Pond", "Its a deep pond, I cant see the bottom.")
    except:
        print "Duplicate area was not able to be created."

    print "#################################### END newAreaTest ####################################"


#This test will create a world with areas and transitions.
#It will ensure that transitions can be made and that invalid transitions cannot be made.
def newTransitionTest():

    #testing creation of valid transitions
    testWorld = World("Death Valley","A very dark and spooky place.", player("Johnny"))
    testWorld.newArea("Woods", "A very dense forest, you can hear the birds.")
    testWorld.newArea("Pond", "Its a deep pond, I cant see the bottom.")

    #Create twoway transitions in all directions possible.
    testWorld.newTransition("path1",["Woods","  NorTh  "], ["Pond","eAsT"], True, "Its path1")
    testWorld.newTransition("path2",["Woods","   SoUtH"], ["Pond","wEsT"], True, "Its path2")
    testWorld.newTransition("path3",["Woods","   northeAst "], ["Pond","SouThEast"], True, "Its path3")
    testWorld.newTransition("path4",["Woods","   SoUtHWeSt  "], ["Pond","noRtHwEsT"], True, "Its path4")
    testWorld.newTransition("path5",["Woods","   Up  "], ["Pond","  dOwN "], True, "Its path5")
    #Create oneway transitions in all directions possible.
    testWorld.newTransition("path6",["Woods","  NorTh  "], ["Pond","eAsT"], False, "Its path6")
    testWorld.newTransition("path7",["Woods","   SoUtH"], ["Pond","wEsT"], False, "Its path7")
    testWorld.newTransition("path8",["Woods","   northeAst "], ["Pond","SouThEast"], False, "Its path8")
    testWorld.newTransition("path9",["Woods","   SoUtHWeSt  "], ["Pond","noRtHwEsT"], False, "Its path9")
    testWorld.newTransition("path10",["Woods","   Up  "], ["Pond","  dOwN "], False, "Its path10")
    print "All 10 transitions successfully made."

    #Create invalid transitions, expect Exceptions to be raised.
    try:
        testWorld.newTransition("path10",["Wood","   Up  "], ["Pond","  dOwN "], False, "Its path10")
    except Exception as e:
        print e.args[0]

    try:
        testWorld.newTransition("path10",["Woods","   Up  "], ["Ponda","  dOwN "], False, "Its path10")
    except Exception as e:
        print e.args[0]

    try:
        testWorld.newTransition("path10",["Woods","bad"], ["Pond"," north"], False, "Its path10")
    except Exception as e:
        print e.args[0]

    try:
        testWorld.newTransition("path10",["Woods","   Up  "], ["Pond","  BAD "], False, "Its path10")
    except Exception as e:
        print e.args[0]

    print "#################################### END newTransitionTest ####################################"

#This test will ensure that the player has the ability to move through all available transitions in the area they are in.
#It will ensure that they can only move 1 way through 1 way transitions and 2 ways otherwise.
#It will ensure that a message will be printed if a player attempts to move through an non-existent route or direction
def movePlayerTest():

        testWorld = World("Death Valley","A very dark and spooky place.", player("Johnny"))
        testWorld.newArea("Woods", "A very dense forest, you can hear the birds.")
        testWorld.newArea("Pond", "Its a deep pond, I cant see the bottom.")


        #Create twoway transitions in all directions possible.
        testWorld.newTransition("path1",["Woods","  NorTh  "], ["Pond","eAsT"], True, "Its path1")
        testWorld.newTransition("path2",["Woods","   SoUtH"], ["Pond","wEsT"], True, "Its path2")
        testWorld.newTransition("path3",["Woods","   northeAst "], ["Pond","SouThEast"], True, "Its path3")
        testWorld.newTransition("path4",["Woods","   SoUtHWeSt  "], ["Pond","noRtHwEsT"], True, "Its path4")
        testWorld.newTransition("path5",["Woods","   Up  "], ["Pond","  dOwN "], True, "Its path5")
        #Create oneway transitions in all directions possible.
        testWorld.newTransition("path6",["Woods","  NorTh  "], ["Pond","eAsT"], False, "Its path6")
        testWorld.newTransition("path7",["Woods","   SoUtH"], ["Pond","wEsT"], False, "Its path7")
        testWorld.newTransition("path8",["Woods","   northeAst "], ["Pond","SouThEast"], False, "Its path8")
        testWorld.newTransition("path9",["Woods","   SoUtHWeSt  "], ["Pond","noRtHwEsT"], False, "Its path9")
        testWorld.newTransition("path10",["Woods","   Up  "], ["Pond","  dOwN "], False, "Its path10")

        #Test movement through all valid routes. Player begins in the woods.
        testWorld.movePlayer("north")
        testWorld.movePlayer("east")
        testWorld.movePlayer("south")
        testWorld.movePlayer("west")
        testWorld.movePlayer("northeast")
        testWorld.movePlayer("southeast")
        testWorld.movePlayer("southwest")
        testWorld.movePlayer("northwest")
        testWorld.movePlayer("up")

        testWorld.movePlayer("down")


        #Test movement through an invalid route expect and exception to be raised
        try:
            testWorld.movePlayer("down")
        except Exception as e:
            print e.args[0]
        print "#################################### END movePlayerTest ####################################"
# This test will ensure that when passed no arguments, look will display the area and the transitions inside that area.
# If any arguments are passed, an error message will be displayed because there is no implementation for that yet.
def lookTest():
    testWorld = World("Death Valley","A very dark and spooky place.", player("Johnny" , "A handsome lad."))
    testWorld.newArea("Woods", "A very dense forest, you can hear the birds.")
    testWorld.newArea("Pond", "Its a deep pond, you cant see the bottom.")

    testWorld.newTransition("path1",["Woods","  NorTh  "], ["Pond","eAsT"], True, "Its path1")
    testWorld.newTransition("path2",["Woods","   SoUtH"], ["Pond","wEsT"], True, "Its path2")
    testWorld.newTransition("path3",["Woods","   northeAst "], ["Pond","SouThEast"], True, "Its path3")

    testWorld.look()
    testWorld.look("me")
    #should display error message.
    testWorld.look("path1")


    print "#################################### END lookTest ####################################"


def saveLoadTests():

    testWorld = World("Death Valley","A very dark and spooky place.", player("Johnny"))
    testWorld.newArea("Woods", "A very dense forest, you can hear the birds.")
    testWorld.newArea("Pond", "Its a deep pond, I cant see the bottom.")
    testWorld.newTransition("path1",["Woods","  NorTh  "], ["Pond","eAsT"], True, "Its path1")
    testWorld.newTransition("path2",["Woods","   SoUtH"], ["Pond","wEsT"], True, "Its path2")
    testWorld.newTransition("path3",["Woods","   northeAst "], ["Pond","SouThEast"], True, "Its path3")


    testWorld.saveProgress()

    firstSave = open("./Johnny.txt", "r")
    firstSave = firstSave.read()

    testWorld.loadGame("Johnny.txt", True)
    testWorld.saveProgress()

    secondSave = open("./Johnny.txt", "r")
    secondSave = secondSave.read()

    firstSave, secondSave = json.dumps(firstSave, sort_keys=True), json.dumps(secondSave, sort_keys=True)


    if firstSave == secondSave:
        print "First save is equal to save after loading.\nNow the test will move the player and check the same equality."

    testWorld.movePlayer("north")

    testWorld.saveProgress()

    firstSave = open("./Johnny.txt", "r")
    firstSave = firstSave.read()

    testWorld.loadGame("Johnny.txt", True)
    testWorld.saveProgress()

    secondSave = open("./Johnny.txt", "r")
    secondSave = secondSave.read()

    firstSave, secondSave = json.dumps(firstSave, sort_keys=True), json.dumps(secondSave, sort_keys=True)

    if firstSave == secondSave:
        print "First save is equal to save after moving player and loading.\nNow the test will attempt to open a broken file and see if it is handled."

    testWorld.loadGame("brokensave.txt", True)

def runTests():
    #newAreaTest()
    #newTransitionTest()
    #movePlayerTest()
    #lookTest()
    saveLoadTests()
runTests()
