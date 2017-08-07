#unfinished recipe
duckIngredients = {'Pekin (Long Island) duck': '1 5- to 6-pound', 'kosher salt': '3 tablespoons', '5-spice powder, preferably homemade': '1 tablespoon',
'large orange zested and cut into 6 wedges': '1', 'grated ginger': '1 tablespoon', 'grated garlic': '1 tablespoon'}

instructions = ["step 1: clean duck", "step 2: Heat oven to 350 degrees. Meanwhile, bring duck to room temperature and make the glaze: Bring orange juice, honey, sugar and soy sauce to a simmer. Add sliced ginger and star anise, then reduce mixture until you have a medium-thick syrup, about 10 minutes. Remove."]

for item in instructions:
    print(item)

for i in duckIngredients:
    print(i, duckIngredients[i])
#                                                                       //honestly unsure why this part works ??
#glazeIngredients = ["2 cups orange juice", "1 tablespoons honey", "2 tablespoons Demerara sugar", "2 tablespoons soy sauce",
#"1 2-inch piece of ginger, thickly sliced", "3 star anise"]            //i was originally going to make two kinds of ingredients

#print "You will need" + duckIngredients + "for the duck."              //i was trying to print the ingredients
#print "You will need" + glazeIngredients + "for the glaze."

#cookBook = {instructions: {'step 1': 'Rinse duck and pat dry. Remove neck and giblets and save for another purpose. Remove excess fat from cavity and tail area and trim off a bit of flappy neck skin. Prick duck skin all over with tip of sharp paring knife, making sure not to penetrate meat.',
#'step 2': 'Mix together salt and 5-spice powder. Season interior of duck with 1 tablespoon salt mixture; use remainder to generously season exterior (you may have a little left over). Combine orange zest with grated ginger and garlic, then smear mixture inside cavity. Place orange wedges in cavity. Tie legs together. Secure neck flap with wooden skewer or toothpicks. Place duck on rack in roasting pan breast-side-up and refrigerate overnight, uncovered.',
#'step 3': 'Heat oven to 350 degrees. Meanwhile, bring duck to room temperature and make the glaze: Bring orange juice, honey, sugar and soy sauce to a simmer. Add sliced ginger and star anise, then reduce mixture until you have a medium-thick syrup, about 10 minutes. Remove from heat and set aside.',
#'step 4': 'Roast duck for 2 hours, carefully pouring off fat and turning duck over every 30 minutes. Paint with glaze and roast another 30 minutes (2 1/2 hours in all). Tent with foil if glaze begins to get too dark. Duck is done when temperature at thickest part of leg reads 165 degrees. Paint duck once more, keep warm and let rest 20 minutes. Use poultry shears to cut into quarters (remove backbone first) or carve in the traditional way, removing legs from carcass and slicing breast. Serve with mashed butternut squash if desired.'}, duckIngredients: {'Pekin (Long Island) duck': 1 5- to 6-pound, 'kosher salt': 3 tablespoons,
#", "1 tablespoon 5-spice powder, preferably homemade",
#"1 large orange, zested and cut into 6 wedges", "1 tablespoon grated ginger", "1 tablespoon grated garlic"}
            #       // i was trying to make a dictionary inside of a dictionary

#print "Here's how to make a Roast Duck with Orange and Ginger!"        //i was trying to make it an ask-answer thing
#print "Do you want to see the INGREDIENTS or the INSTRUCTIONS?"
#user_input= input()
#if user_input = ingredients
#    print "ingredients for the DUCK or for the GLAZE?"
#    user_input = input()
#    if user_input
