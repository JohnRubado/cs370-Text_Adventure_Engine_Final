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

    #Now creating the areas.
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

def lookTest():
    testWorld = World("Death Valley","A very dark and spooky place.", player("Johnny" , "A handsome lad."))
    testWorld.newArea("Woods", "A very dense forest, you can hear the birds.")
    testWorld.newArea("Pond", "Its a deep pond, you cant see the bottom.")

    itemOne = testWorld.newItem("itemOne","simple itemOne", "Woods", True)
    itemOne.detailedDescription = "detailed itemOne"
    itemTwo = testWorld.newItem("itemTwo", "simple itemTwo", "Woods", True)

    inPath, outPath = testWorld.newTransition("path1",["Woods","  NorTh  "], ["Pond","eAsT"], True, "Its path1")
    testWorld.newTransition("path2",["Woods","   SoUtH"], ["Pond","wEsT"], True, "Its path2")
    testWorld.newTransition("path3",["Woods","   northeAst "], ["Pond","SouThEast"], True, "Its path3")

    print "Test is looking at area player is in. Followed by player looking at themselves"
    print "Expect simple descriptions upon a generic look() call"
    testWorld.look()

    print "Test is now looking specifically at the objects. Expected detailed itemOne and simple itemTwo \n"

    testWorld.look("itemOne")
    testWorld.look("itemTwo")

    print "Test will now pickUp the items and move player and repeat the specific looking to verify viewability of items in inventory"

    testWorld.pickUpItem("itemOne")
    testWorld.pickUpItem("itemTwo")
    testWorld.movePlayer("path1")
    testWorld.look("itemOne")
    testWorld.look("itemTwo")
    testWorld.look("me")
    testWorld.movePlayer("path1")
    testWorld.dropItem("itemOne")
    testWorld.dropItem("itemTwo")


    print "Saving and loading and repeating all previous look tests. Expect same output."
    testWorld.saveProgress()
    testWorld.loadGame("./Johnny.txt", True)
    print "Test is looking at area player is in. Followed by player looking at themselves"
    print "Expect simple descriptions upon a generic look() call"
    testWorld.look()

    print "Test is now looking specifically at the objects. Expected detailed itemOne and simple itemTwo \n"

    testWorld.look("itemOne")
    testWorld.look("itemTwo")

    print "Test will now pickUp the items and move player and repeat the specific looking to verify viewability of items in inventory"

    testWorld.pickUpItem("itemOne")
    testWorld.pickUpItem("itemTwo")
    testWorld.movePlayer("path1")
    testWorld.look("itemOne")
    testWorld.look("itemTwo")
    testWorld.look("me")


    print "#################################### END lookTest ####################################"

#This test will create a world and ensure that loading a saved world will be an exact copy of the world that was saved.
#Then it will attempt to open a broken save file to make sure it will be handled.
#It will then put some items into the players inventory,move the player, drop 1 item, and save, testing for a replica after loading.
#Finally it will add scripts to all existing elements, then save, then test for an exact replica again.
#This test includes exhaustive embedded transition script tests as well.
def saveLoadTests():

    def scriptOne():
        print "Script one ran"

    def scriptTwo():
        print "Script two ran"


    testWorld = World("Death Valley","A very dark and spooky place.", player("Johnny"))
    testWorld.newArea("Woods", "A very dense forest, you can hear the birds.")
    testWorld.newArea("Pond", "Its a deep pond, I cant see the bottom.")
    inPath1, outPath1 = testWorld.newTransition("path1",["Woods","  NorTh  "], ["Pond","eAsT"], True, "Its path1")
    inPath2, outPath2= testWorld.newTransition("path2",["Woods","   SoUtH"], ["Pond","wEsT"], True, "Its path2")
    inPath3, outPath3 = testWorld.newTransition("path3",["Woods","   northeAst "], ["Pond","SouThEast"], True, "Its path3")


    testWorld.saveProgress()

    firstSave = open("./Johnny.txt", "r")
    firstSave = firstSave.read()

    testWorld.loadGame("Johnny.txt", True)
    testWorld.saveProgress()

    secondSave = open("./Johnny.txt", "r")
    secondSave = secondSave.read()

    firstSave, secondSave = pickle.dumps(firstSave), pickle.dumps(secondSave)


    if firstSave == secondSave:
        print "SUCCESS - First save is equal to save after loading.\nNow the test will move the player and check the same equality."
    else:
        print "FAIL - Saves not equal"
    ########################################################################################

    testWorld.movePlayer("north")

    testWorld.saveProgress()

    firstSave = open("./Johnny.txt", "r")
    firstSave = firstSave.read()

    testWorld.loadGame("Johnny.txt", True)
    testWorld.saveProgress()

    secondSave = open("./Johnny.txt", "r")
    secondSave = secondSave.read()

    firstSave, secondSave = pickle.dumps(firstSave), pickle.dumps(secondSave)

    if firstSave == secondSave:
        print "SUCCESS - First save is equal to save after moving player and loading.\nNow the test will attempt to open a broken file and see if it is handled."
    else:
        print "FAIL - Saves not equal"
    ########################################################################################
    testWorld.loadGame("brokensave.txt", True)
    ########################################################################################
    print "SUCCESS - Now the test will add items to the world, player will pick up 2 items, move to a new area, drop 1 item,  and test for equality of saves."

    itemOne = testWorld.newItem("itemOne","one", "Woods", True)
    itemTwo = testWorld.newItem("itemTwo", "two", "Woods", False)
    testWorld.newItem("itemThree", "three", "Pond", True)
    testWorld.newItem("itemFour", "four", "Pond", False)
    testWorld.newItem("itemFive", "five", "Pond", True)
    testWorld.newItem("itemSix", "six", "Pond", False)
    testWorld.pickUpItem("itemFive")
    testWorld.pickUpItem("itemThree")

    testWorld.movePlayer("east")
    testWorld.dropItem("itemThree")

    testWorld.saveProgress()

    firstSave = open("./Johnny.txt", "r")
    firstSave = firstSave.read()

    testWorld.loadGame("Johnny.txt", True)

    testWorld.saveProgress()
    secondSave = open("./Johnny.txt", "r")
    secondSave = secondSave.read()



    firstSave, secondSave = pickle.dumps(firstSave), pickle.dumps(secondSave)


    if firstSave == secondSave:
        print "SUCCESS - First save is equal to save after adding items to world and to player inventory, and  then moving player.\nNow the test will attempt to add scripts to all these items and transitions to check for equality between saves.\nExpect scriptOne and scriptTwo messages before and after loading."
    else:
        print "FAIL - Saves not equal"

    ########################################################################################

    for area in testWorld.areas:
        for transition in area.transitions:
            transition.onSuccessScripts.append(scriptOne)
        for item in area.items:
            item.onSuccessScripts.append(scriptTwo)


    testWorld.pickUpItem("itemOne")
    testWorld.movePlayer("path1")

    testWorld.saveProgress()
    firstSave = open("./Johnny.txt", "r")
    firstSave = firstSave.read()

    testWorld.loadGame("Johnny.txt", True)

    testWorld.saveProgress()
    secondSave = open("./Johnny.txt", "r")
    secondSave = secondSave.read()

    testWorld.dropItem("itemOne")
    testWorld.pickUpItem("itemOne")
    testWorld.movePlayer("path1")

    firstSave, secondSave = pickle.dumps(firstSave), pickle.dumps(secondSave)

    if firstSave == secondSave:
        print "SUCCESS - First save is equal to save after adding scripts to objects, interacting with those objects and saving."
    else:
        print "FAIL - Saves not equal"
    print "#################################### END saveLoadTests ####################################"

#Inventory test will test inventory functionality with embedded item script functionality.
def inventoryTests():

    def scriptOne():
        print "Script one ran"

    def scriptTwo():
        print "Script two ran"

    testWorld = World("Death Valley","A very dark and spooky place.", player("Johnny"))
    testWorld.newArea("Woods", "A very dense forest, you can hear the birds.")
    testWorld.newArea("Pond", "Its a deep pond, I cant see the bottom.")
    inPath1, outPath1 = testWorld.newTransition("path1",["Woods","  NorTh  "], ["Pond","eAsT"], True, "Its path1")

    itemOne = testWorld.newItem("itemOne","one", "Woods", True)
    itemTwo = testWorld.newItem("itemTwo", "two", "Woods", False)
    itemOne.onSuccessScripts.append(scriptOne)
    itemTwo.onFailureScripts.append(scriptTwo)
    testWorld.newItem("itemThree", "three", "Pond", True)
    testWorld.newItem("itemFour", "four", "Pond", False)
    testWorld.newItem("itemFive", "five", "Pond", True)
    testWorld.newItem("itemSix", "six", "Pond", False)

    #Test picking up an item that exists and putting it down, then attempting to take an item that is not takeable.
    #Test for both custom and default messages.
    itemOne.onSuccess = "Custom success message for itemOne"
    itemTwo.onFailure = "Custom failure message for itemTwo"
    print "Test picking up itemOne and dropping... Expect 1 custom success message, a drop message, and a scriptOne message. "
    testWorld.pickUpItem("itemOne")
    testWorld.dropItem("itemOne")
    print "Test picking up itemTwo... Expect 1 custom failure message and 1 scriptTwo message."
    testWorld.pickUpItem("itemTwo")
    print "Test picking up itemOne and itemTwo with default messages, expect 1 default success message and 1 default failure message along with scriptOne and scriptTwo messages."
    itemOne.onSuccess = None
    itemTwo.onFailure = None
    testWorld.pickUpItem("itemOne")
    testWorld.pickUpItem("itemTwo")
    testWorld.dropItem("itemOne")


    #Test picking up a non-existent item and attempting to drop it.
    print "Test attempting to pickup and drop a non existent item. Expect 2 messages 'There is no fakeitem' and 'You do not have a fakeitem'"
    testWorld.pickUpItem("fakeitem")
    testWorld.dropItem("fakeitem")

    #Test for picking up an existing item, but player is not in the area with the item.
    print "Test attempting to take an item that exists, but it is in another area, and then attempts to drop it. Expect 'There is no itemOne' and 'You do not have a itemOne'"
    testWorld.movePlayer("path1")
    testWorld.pickUpItem("itemOne")
    testWorld.dropItem("itemOne")



def runTests():
    #newAreaTest()
    #newTransitionTest()
    #movePlayerTest()
    #lookTest()
    #saveLoadTests()
    inventoryTests()
runTests()
