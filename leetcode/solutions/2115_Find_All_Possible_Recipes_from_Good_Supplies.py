from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        # this is almost like a dependency graph u do toplogical dfs or what not 
        # so what u shld do is for each recipe count how many ingredients we need 
        # we add it to our set of ingredentents maybe as a queeu

        q = deque(supplies)
        canMake = set() 
        countParts = []
        partIsInDict = defaultdict(list)
        for i in range(n):
            countParts.append(len(ingredients[i]))
            for ingredient in ingredients[i]:
                partIsInDict[ingredient].append(i)
        
        while q:
            part = q.popleft() # we book keep that we have this part in all the recipes
            print(countParts)
            for i in partIsInDict[part]: # so i is every item that can be made from this recipe
                countParts[i] -= 1 
                if countParts[i] == 0:
                    canMake.add(recipes[i])
                    q.append(recipes[i])

        return list(canMake)
            
        