class Proposal:
    def __init__(self, proposer, text):
        self.text = text
        self.proposer = proposer
        self.votes = {"yes": 0, "no": 0}
        self.voters = []

    def vote(self, actor, choice):
        if actor.voted:
            print(f"{actor.name} has already voted!")
            return
        if choice.lower() == "yes":
            self.votes["yes"] += actor.tokens
        elif choice.lower() == "no":
            self.votes["no"] += actor.tokens
        else:
            print(f"Invalid vote by {actor.name}")
            return
        actor.voted = True
        self.voters.append(actor.name)

    def result(self):
        print("\n📊 Voting Results:")
        print(f"✅ YES Votes: {self.votes['yes']}")
        print(f"❌ NO Votes:  {self.votes['no']}")
        if self.votes["yes"] > self.votes["no"]:
            print("\n🎉 Proposal ACCEPTED!")
            return "accepted"
        elif self.votes["yes"] < self.votes["no"]:
            print("\n❌ Proposal REJECTED!")
            return "rejected"
        else:
            print("\n⚠️ TIE — No decision (might trigger crisis handling!)")
            return "tie"

    def reset_votes(self, actors):
        for a in actors:
            a.voted = False
