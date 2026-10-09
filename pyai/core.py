import random

class RuleBasedModel:
    def __init__(self, name, traindata):
        self.name = name
        self.training_data = traindata
        self.trained = {}
        self.saved = ""
    def train(self):
        turn = "user"
        for line in self.training_data.splitlines():
            if not line:
                continue
            
            if turn == "user":
                self.saved = line
                self.trained[line] = ""
                turn = "ai"
            elif turn == "ai":
                self.trained[self.saved] = line
                turn = "user"
    def main(self):
        while True:
            user = input("You: ")
            response = self.trained.get(user)
            if not response is None:
                print(f"{self.name}: " + response)
            elif user == "exit":
                break
            else:
                print(f"{self.name}: I do not understand that.")

class MarkovModel:
    def __init__(self, name, training_data):
        self.name = name
        self.training_data = training_data
        self.chain = {}
    def train(self):
        words = self.training_data.split()
        for i in range(len(words) - 1):
            word = words[i].strip()
            nextWord = words[i + 1]

            if word not in self.chain:
                self.chain[word] = []

            self.chain[word].append(nextWord)
    def main(self):
        while True:
            user = input("You: ")

            if user == "exit":
                break
            else:
                words = user.split()
                current = words[-1]
                response = []

                for _ in range(20):
                    if current not in self.chain:
                        break

                    current = random.choice(self.chain[current])
                    response.append(current)
                print(self.name + ":", " ".join(response))

class UserRuleModel:
    def __init__(self, name):
        self.name = name
        self.rules = {}
    def main(self):
        self.help()
        while True:
            user = input("You: ")
            if user == "exit":
                break
            elif user == "help":
                self.help()
            elif user.startswith("addrule "):
                nuser = user.replace("addrule ", "").strip()
                rule, res = nuser.split("-> ", 1)
                self.rules[rule.strip()] = res
                print(f"Rule added: {rule} -> {self.rules[rule.strip()]}")
            else:
                current = self.rules.get(user)
                if current == None:
                    print(f"{self.name}: I do not understand that")
                else:
                    print(f"{self.name}: {current}")
    def help(self):
        print("Help:")
        print("    addrule [RULE] -> [RESPONSE]")
        print("    help")

class RandomModel:
    def __init__(self, name, responses):
        self.name = name
        self.responses = responses
    def main(self):
        while True:
            user = input("You: ")
            if user == "exit":
                break
            else:
                print(self.name + ": " + random.choice(self.responses))
