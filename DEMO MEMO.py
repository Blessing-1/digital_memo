class Memo:
    def __init__(self, sender, recipient, subject, message, approval_status=False):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.message = message
        self.approval_status = approval_status
        self.responses = []

    def approve(self):
        self.approval_status = True
        print("Memo approved.")

    def reply(self, sender, message):
        reply_memo = Memo(sender, self.sender, "RE: " + self.subject, message)
        self.responses.append(reply_memo)
        print("Reply sent.")

    def forward(self, sender, recipient):
        forwarded_memo = Memo(sender, recipient, "FW: " + self.subject, self.message)
        return forwarded_memo

    def display(self):
        print(f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\nMessage: {self.message}\nApproved: {self.approval_status}\n")


class MemoSystem:
    def __init__(self):
        self.memos = []

    def compose_memo(self, sender, recipient, subject, message):
        new_memo = Memo(sender, recipient, subject, message)
        self.memos.append(new_memo)
        print("Memo composed and added to system.")

    def send_memo(self, memo):
        if memo in self.memos:
            print("Sending memo...")
            memo.display()
        else:
            print("Memo not found in system.")

    def forward_memo(self, memo_id, sender, recipient):
        if memo_id < len(self.memos):
            forwarded_memo = self.memos[memo_id].forward(sender, recipient)
            self.memos.append(forwarded_memo)
            print("Memo forwarded.")
        else:
            print("Memo ID not found.")

    def reply_to_memo(self, memo_id, sender, message):
        if memo_id < len(self.memos):
            self.memos[memo_id].reply(sender, message)
        else:
            print("Memo ID not found.")

    def approve_memo(self, memo_id):
        if memo_id < len(self.memos) and not self.memos[memo_id].approval_status:
            self.memos[memo_id].approve()
        else:
            print("Memo ID not found or already approved.")

    def display_memos(self):
        for i, memo in enumerate(self.memos):
            print(f"Memo ID: {i}")
            memo.display()

# Example usage
memo_system = MemoSystem()
memo_system.compose_memo("Alice", "Bob", "Project Update", "Please find the project update attached.")
memo_system.compose_memo("Bob", "Alice", "RE: Project Update", "Thanks for the update, Alice.")

memo_system.display_memos()

memo_system.approve_memo(0)
memo_system.reply_to_memo(0, "Bob", "Got it, thanks!")
memo_system.forward_memo(1, "Alice", "Charlie")

memo_system.display_memos()