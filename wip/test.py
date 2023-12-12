import json # Import json library to easy data extraction
import pprint as pprint # For testing purposes, does not currently have a use case

def findID(filePath, search_term=None, search_by_id=False):
    """
    Finds the ID of an item based on the name or shortname of the item.
    If search_by_id is set to True, it will search by ID instead of name.

    Parameters:
    filePath (str): The path to the file containing the item data.
    search_term (str): The name or ID of the item to search for.
    search_by_id (bool): If True, will search by ID instead of name.

    Returns:
    info['name'] (str): The name of the item.
    id (str): The ID of the item.
    "Not a valid item name or id." (str): If no match is found.

    """

    # If no search term is provided, ask for one
    if search_term == None:
        search_term = input("Enter item name or id: ").lower()
    
    # Open the file and load the data into a dictionary
    with open(filePath, 'r', encoding='utf-8') as f:
        data = json.load(f)  

    # Loop through the dictionary and return the ID if the search term matches 
    # the name or shortname of the item
    # If search_by_id is True, it will search by ID instead of name
    # If no match is found, it will return "Not a valid item name or id."   
    for id, info in data.items():
        if search_by_id:
            if id.lower() == search_term:
                return info['name']
        elif info['name'].lower() == search_term:
            return id
        elif info['shortname'] == search_term:
                return id
    return "Not a valid item name or id."


# TODO: 
# Commenting
# def findDeployableDurability(filePath: str):
#     """
#     Finds the durability of an item based on the name or shortname of the item.
    
#     Parameters:
#     filePath (str): The path to the file containing the item data.

#     Returns:
#     To be added

#     """
#     global itemsFile
#     id = findID(itemsFile)
#     itemname = findID(itemsFile, id, True)
#     cheapest = float('inf')

#     # Open the file and load the data into a dictionary
#     with open(filePath, 'r', encoding='utf-8') as f:
#         data = json.load(f)
    
#     dict_ = {}
#     list_ = []
#     dellist = []
#     # Lot of for loops, thx rustlabs
#     # Currently prints all the items that can do damage to 
#     # the item with the id that was found
#     # (i.e., input 'Bradley APC' returns all the weapons that can damage it)
#     for info in data.values():
#         for item, dictionary in info.items():
#             if item == id:
#                 for i in dictionary:
#                     for key,value in i.items():
#                         if key == "group":
#                             list_.append(value)
#                         if key == "toolId":
#                             raidTool = findID(itemsFile, value, True)
#                         elif key == "quantity":
#                             list_.append(value)
#                         elif key == "timetostring":
#                             list_.append(value)
#                         elif key == "fuel":
#                             list_.append(value)
#                         elif key == "sulfur":
#                             list_.append(value)
#                     dict_[raidTool] = list_
#                     list_ = []
    
#     for key, value in dict_.items():
#         if value[0] != "explosive":
#             dellist.append(key)

#     for i in dellist:
#         del dict_[i]

#     for key, value in dict_.items():
#         if value[3] != None:
#             if value[3] < cheapest:
#                 cheapest = value[3] 
#         else: continue

#     for key, value in dict_.items():
#         if value[3] == cheapest:
#             return f"Trying to raid: {itemname}\nBest option to raid: {key}\nCost: {value[3]} sulfur\nQuantity needed: {value[1]}"

# def findBuildingDurability(durabFile: str):
#     global itemsFile

#     with open(durabFile, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     input_ = input("Enter building name: ")
#     dict_ = {}
#     list_ = []
#     dellist = []
#     cheapest = float('inf')

#     for info in data.values():
#         for building, dictionary in info.items():
#             if building == input_:
#                 for i in dictionary:
#                     for key, value in i.items():
#                         if key == "group":
#                             list_.append(value)
#                         if key == "toolId":
#                             raidTool = findID(itemsFile, value, True)
#                         elif key == "quantity":
#                             list_.append(value)
#                         elif key == "timetostring":
#                             list_.append(value)
#                         elif key == "fuel":
#                             list_.append(value)
#                         elif key == "sulfur":
#                             list_.append(value)
#                     dict_[raidTool] = list_
#                     list_ = []
#     for key, value in dict_.items():
#         if value[0] != "explosive":
#             dellist.append(key)

#     for i in dellist:
#         del dict_[i]

#     for key, value in dict_.items():
#         if value[3] != None:
#             if value[3] < cheapest:
#                 cheapest = value[3] 
#         else: continue

#     for key, value in dict_.items():
#         if value[3] == cheapest:
#             return f"Trying to raid: {input_}\nBest option to raid: {key}\nCost: {value[3]} sulfur\nQuantity needed: {value[1]}"
        
# def findVehicleDurability(durabFile: str):
#     global itemsFile

#     with open(durabFile, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     input_ = input("Enter vehicle name: ")
#     dict_ = {}
#     list_ = []
#     dellist = []
#     cheapest = float('inf')

#     for info in data.values():
#         for vehicle, dictionary in info.items():
#             if vehicle == input_:
#                 for i in dictionary:
#                     for key, value in i.items():
#                         if key == "group":
#                             list_.append(value)
#                         if key == "toolId":
#                             raidTool = findID(itemsFile, value, True)
#                         elif key == "quantity":
#                             list_.append(value)
#                         elif key == "timetostring":
#                             list_.append(value)
#                         elif key == "fuel":
#                             list_.append(value)
#                         elif key == "sulfur":
#                             list_.append(value)
#                     dict_[raidTool] = list_
#                     list_ = []
#     for key, value in dict_.items():
#         if value[0] != "explosive":
#             dellist.append(key)

#     for i in dellist:
#         del dict_[i]

#     for key, value in dict_.items():
#         if value[3] != None:
#             if value[3] < cheapest:
#                 cheapest = value[3] 
#         else: continue

#     for key, value in dict_.items():
#         if value[3] == cheapest:
#             return f"Trying to raid: {input_}\nBest option to raid: {key}\nCost: {value[3]} sulfur\nQuantity needed: {value[1]}"

def findDurability(durabFile: str, itemType: str, itemName: str, raidType: str = 'explo'):
    raidTypeList = ['eco', 'explo']
    itemTypeList = ['deployable', 'vehicle', 'building']
    global itemsFile
    cheapest = float('inf')

    with open(durabFile, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if raidType not in raidTypeList:
        return "Invalid Raid Type"
    if itemType not in itemTypeList:
        return "Invalid Item Type"

    if itemType == 'deployable':
        search_term = findID(itemsFile, itemName)
    elif itemType == 'vehicle' or 'building':
        search_term = itemName
    
    
    dict_ = {}
    list_ = []
    dellist = []

    for info in data.values():
        for item, dictionary in info.items():
            if search_term == item:
                for i in dictionary:
                    for key,value in i.items():
                        if key == "group":
                            list_.append(value)
                        if key == "toolId":
                            raidTool = findID(itemsFile, value, True)
                        elif key == "quantity":
                            list_.append(value)
                        elif key == "time":
                            list_.append(value)
                        elif key == "timeString":
                            list_.append(value)
                        elif key == "fuel":
                            list_.append(value)
                        elif key == "sulfur":
                            list_.append(value)
                    dict_[raidTool] = list_
                    list_ = []

    if raidType == 'eco':
        for key,value in dict_.items():
            if value[0] != 'melee':
                dellist.append(key)
    elif raidType == 'explo':
        for key,value in dict_.items():
            if value[0] != 'explosive':
                dellist.append(key)

    for i in dellist:
        del dict_[i]

    if raidType == 'explo':
        for key, value in dict_.items():
            if value[-1] != None:
                if value[-1] < cheapest:
                    cheapest = value[-1] 

        for key, value in dict_.items():
            if value[-1] == cheapest:
                return f"Trying to {raidType}raid: {itemName}\nBest option to {raidType}raid: {key}\nCost: {value[-1]} sulfur\nTime to raid: {value[3]}\nQuantity needed: {value[1]}"
    elif raidType == 'eco':
        for key, value in dict_.items():
            if value[2] != None:
                if value[2] < cheapest:
                    cheapest = value[2]
        for key,value in dict_.items():
            if value[2] == cheapest:
                return f"Trying to {raidType}raid: {itemName}\nBest option to {raidType}raid: {key}\nTime to {raidType}raid: {value[3]}\nQuantity needed: {value[1]}"

    

    


# File Locations
itemsFile = r'data\items.json'
durabFile = r'data\rustlabsDurabilityData.json'

# print(findBuildingDurability(durabFile))
# print(findID(itemsFile, 'bed'))
print(findDurability(durabFile, 'deployable', 'workbench level 3', 'eco'))