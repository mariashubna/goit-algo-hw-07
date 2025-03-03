class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False
    
    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.is_deleted = True

    def display(self, indent=0):
        if not self.is_deleted:
            print("    " * indent + f"{self.author}: {self.text}")
            for reply in self.replies:
                reply.display(indent + 1)
        else:
            print("    " * indent + "Цей коментар було видалено.")
            for reply in self.replies:
                reply.display(indent + 1)


root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()

    