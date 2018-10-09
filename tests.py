from packages.world.world import *;

#this test will create a world with some areas and print the world to see if they were created with the correct
#names and descriptions
#Test will ensure duplicate areas cannot be created and that the correct world and areas were created.
def newAreaTest():
    testWorld = World("Death Valley","A very dark and spooky place.", player("Johnny"))
    testWorld.newArea("Woods", "A very dense forest, you can hear the birds.")
    testWorld.newArea("Pond", "Its a deep pond, I cant see the bottom.")
    testWorld.printWorld()
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


    testWorld.printWorld()

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
        print "Player in " + testWorld.player.currentArea.name
        testWorld.movePlayer("north")
        print "Player in " + testWorld.player.currentArea.name
        testWorld.movePlayer("east")
        print "Player in " + testWorld.player.currentArea.name
        testWorld.movePlayer("south")
        print "Player in " + testWorld.player.currentArea.name
        testWorld.movePlayer("west")
        print "Player in " + testWorld.player.currentArea.name
        testWorld.movePlayer("northeast")
        print "Player in " + testWorld.player.currentArea.name
        testWorld.movePlayer("southeast")
        print "Player in " + testWorld.player.currentArea.name
        testWorld.movePlayer("southwest")
        print "Player in " + testWorld.player.currentArea.name
        testWorld.movePlayer("northwest")
        print "Player in " + testWorld.player.currentArea.name
        testWorld.movePlayer("up")
        print "Player in " + testWorld.player.currentArea.name
        testWorld.movePlayer("down")
        print "Player in " + testWorld.player.currentArea.name

        #Test movement through an invalid route expect and exception to be raised
        try:
            testWorld.movePlayer("down")
        except Exception as e:
            print e.args[0]



def runTests():
    newAreaTest()
    newTransitionTest()
    movePlayerTest()

runTests()
